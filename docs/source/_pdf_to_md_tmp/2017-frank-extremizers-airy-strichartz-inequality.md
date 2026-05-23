arXiv:1712.04156v2[math.AP]2May2018

EXTREMIZERS FOR THE AIRY–STRICHARTZ INEQUALITY

RUPERT L. FRANK AND JULIEN SABIN

Abstract. We identify the compactness threshold for optimizing sequences of the Airy– Strichartz inequality as an explicit multiple of the sharp constant in the Strichartz inequality. In particular, if the sharp constant in the Airy–Strichartz inequality is strictly smaller than this multiple of the sharp constant in the Strichartz inequality, then there is an optimizer for the former inequality. Our result is valid for the full range of Airy–Strichartz inequalities (except the endpoints) both in the diagonal and oﬀ-diagonal cases.

1. Introduction The solution of the Cauchy problem for the Airy equation

∂tv + ∂x3v = 0, t ∈ R, x ∈ R, v|t=0 = u ∈ L2x(R)

(1.1)

may be written as v(t, x) = (e−t∂x3u)(x). This solution disperses as |t| → ∞, as reﬂected by the Airy–Strichartz inequalities

R R

3 x

|Dx|γ(e−t∂

q

u)(x)

dx

p/q

dt C ||u||pL2x (1.2)

due to Kenig, Ponce, and Vega [30]. This inequality holds for any exponents satisfying the relations

3 p

1 q

- 1

![image 1](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile1.png>)

- 2


- 1

![image 2](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile2.png>)

- 2


1 p

2 p, q < ∞, −γ +

, −

+

=

< γ

; (1.3)

![image 3](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile3.png>)

![image 4](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile4.png>)

![image 5](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile5.png>)

see [30, Thm. 2.1] for the case γ = 1/p. The other cases of the inequality can be obtained from this case using Sobolev’s embedding theorem as in [30, Thm. 2.4].

We will be interested in the optimal constant in (1.2), that is,

p/q

q

3

|Dx|1/p(e−t∂

dx

xu)(x)

dt ||u||pL2

R R

Ap := sup

, (1.4)

![image 6](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile6.png>)

u =0

where the supremum is taken over all complex valued functions u. In (1.4), we considered the case γ = 1/p, which is critical in a certain sense and has a richer behavior than the case γ < 1/p. Therefore we mostly focus on this case and comment brieﬂy on the necessary modiﬁcations for γ < 1/p in Appendix E. Our goal is to investigate the existence of maximizers for the maximization problem Ap and, more generally, to understand the behaviour of maximizing sequences.

1

For γ = 1/p the constraint (1.3) on the exponents p, q becomes 2/p + 1/q = 1/2, which is the same condition under which Strichartz inequalities are valid for the Schro¨dinger equation in one space dimension

i∂tv − 3∂x2v = 0, t ∈ R, x ∈ R, v|t=0 = u ∈ L2x(R).

(1.5)

For this last equation, the solution may be written as v(t, x) = (e−3it∂x2u)(x), and the Strichartz inequalities [49, 22, 29] correspond to the ﬁniteness of

p/q

q

2 x

(e−3it∂

u)(x)

dx

dt ||u||pL2

R R

Sp := sup

, (1.6)

![image 7](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile7.png>)

u =0

with, as we said, the constraint 2/p + 1/q = 1/2.

The Airy–Strichartz inequality (1.2) belongs to the wider class of Fourier extension inequalities. Indeed, the space-time Fourier transform of e−t∂x3u is supported on the curve η = ξ3. Hence, the estimate (1.2) may be seen as an information about the decay of the Fourier transform of functions supported on this cubic curve. Such estimates have a long history in harmonic analysis. For instance, when the curve is replaced by a compact hypersurface with non-zero curvature, this decay is the content of the Stein–Tomas theorem [48, 53]. When the hypersurface is the paraboloid η = 3ξ2, this corresponds to the problem (1.6) for the Schro¨dinger equation.

Lately, there have been several works concerning extremizers for such Fourier extension inequalities. One group of works tries to ﬁnd the sharp values of the constants and to identify all optimizers. This can be done in some speciﬁc cases; for instance, Foschi [16] (see also [26, 4, 23]) proved that for p = q = 6 the only optimizers for (1.6) up to symmetries are Gaussians, which is also the case for p = 2q = 4 as proved in [4, 10]. A similar result holds for the two-dimensional Strichartz inequality (with p = q = 4) [16] and for the two-dimensional Stein–Tomas inequality on the sphere [17], with constants being the only optimizers up to symmetries. The corresponding questions in other dimensions are still open, with some recent progress for the one-dimensional Stein–Tomas inequality in [11]. All these results rely on the evenness of the exponent of the Lebesgue space in which the Fourier extension lives, in order to apply the Parseval identity followed by some convolution identities.

A second group of works examines the behaviour of extremizing sequences from the point of view of concentration-compactness. This originated in work by Kunze [34] for the problem (1.6) in one space dimension with p = q = 6 and by Shao [45] in higher dimensions (see also [41] when the paraboloid is replaced by the cone, and [28, 27] for a fourth order version). For the Stein–Tomas problem on the sphere, this was carried out by Christ and Shao [14] in dimension two and by Shao [46] in dimension one. In these last two works, the evenness of the Lebesgue exponent again plays a crucial role. The case of higher dimensions (without evenness of the Lebesgue exponent) was treated in [20], which is the work that we rely on. The weakness of these methods is that they merely give the existence of optimizers, without identifying them. On the other hand, they give universal informations about optimizing

sequences. Studying optimizing sequences may also lead to the non-existence of optimizers [42, 43, 12].

The question of existence of optimizers for the Airy–Strichartz inequality (1.2) in the case p = q = 6, γ = 1/p = 1/6 has already been considered by Shao [44]. However, we believe that his argument is not complete. Therefore, our goal in this paper is two-fold: ﬁrst, to correct and complete the argument in [44] and, second, to consider arbitrary exponents p > 4.

In general, the strategy to prove the existence of optimizers is to obtain some kind of compactness for optimizing sequences. There may be several ways to lose this compactness, and the heart of the matter is to identify them exactly. Sometimes, this loss of compactness comes from exact symmetries of the inequality and cannot be avoided. In this case, the best result one may hope for is precompactness of optimizing sequences up to applying wellchosen symmetry transformations to the sequence. What makes the problem interesting and diﬃcult is the presence of ‘approximate symmetries’ which cannot be removed by applying symmetry transformations and which might lead to a more subtle loss of compactness. We will discuss those in more detail below.

In our case, the Airy–Strichartz inequality (1.2) has a large group of (exact) symmetries: for any (t0, x0, λ0) ∈ R × R × (0, ∞) and any u ∈ L2(R), deﬁne the transformation

0,x0,λ0u](x) = λ10/2(e−t

0∂x3u)(λ0x + x0) and the associated group G of all these transformations

∀x ∈ R, [gt

G := {gt,x,λ, (t, x, λ) ∈ R × R × (0, +∞)}.

The inequality (1.2) is invariant under the group G, in the sense that for any u ∈ L2(R) and for any g ∈ G, we have

||Ψp[gu]||LptLqx = ||Ψp[u]||LptLqx , ||gu||L2x = ||u||L2x , where we used the shortcut notation for (t, x) ∈ R × R,

1 √2π R |ξ|1/peitξ

3+ixξ u(ξ) dξ,

3

Ψp[u](t, x) := |Dx|1/pe−t∂

xu(x) =

![image 8](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile8.png>)

![image 9](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile9.png>)

where u denotes the Fourier transform of u, ∀ξ ∈ R, u(ξ) :=

1 √2π R

u(x)e−ixξ dx.

![image 10](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile10.png>)

![image 11](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile11.png>)

Motivated by the previous discussion, we introduce the following notion of compactness.

- Deﬁnition 1.1. A sequence (un) ⊂ L2(R) is precompact up to symmetries if there are (gn) ⊂ G such that (gnun) is precompact in L2(R).
- Deﬁnition 1.2. A maximizing sequence for Ap is a sequence (un) ⊂ L2x(R) with ||un||L2x = 1


such that ||Ψp[un]||pLp

tLqx → Ap as n → ∞. With these notions at hand, we may state our main result.

- Theorem 1. Let 4 < p < ∞ and q such that 2/p + 1/q = 1/2. Then, all maximizing sequences for Ap are precompact up to symmetries if and only if


Ap > apSp, (1.7) where Ap is deﬁned in (1.4), Sp is deﬁned in (1.6), and

p/q

p/q

Γ(q+12 ) Γ(q+22 )

2π

2p/2 πp/(2q)

- 1

![image 12](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile12.png>)

- 2π


![image 13](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile13.png>)

(1 + cosθ)q/2 dθ

> 1. (1.8)

ap :=

=

![image 14](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile14.png>)

![image 15](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile15.png>)

0

![image 16](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile16.png>)

In particular, if (1.7) holds, then there is a maximizer of Ap.

- Remark 1.3. Since the evolution (1.1) preserves real-valuedness of functions, it is also natural to deﬁne the optimal constant

Ap,R := sup

u∈L2x(R,R)\{0}

R R

|Dx|1/p(e−t∂

3

xu)(x)

q

dx

p/q

dt ||u||pL2

![image 17](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile17.png>)

, (1.9)

where the supremum is taken only over all real valued functions u. Then, the exact same statement holds, replacing Ap by Ap,R, as we will show in Lemma 2.8 at the end of Section 2. (For the precompactness statement, we note also that the symmetry group G preserves real-valuedness of functions.) Actually, we even have

Ap = Ap,R

and there is a maximizer for Ap,R if and only if there is one for Ap. This extends to general extension problems, as we discuss in Appendix F. The question whether Ap is equal to Ap,R was raised by a referee, to whom we are most grateful, after an earlier version of this manuscript was submitted. We solved this problem using a technique from our previous paper [20], but then learned by personal communication from D. Oliveira e Silva and R. Quilodra´n, to whom we are also grateful, that the same proof was found independently in [8].

- Remark 1.4. In [44], the necessary and suﬃcient condition for the existence of maximizers for p = q = 6 are claimed to be A6 > S6 and A6,R > 2−1/2S6 and hence are not correct since a6 = 5/2. We comment on this diﬀerence in Remark 2.7.
- Remark 1.5. In Theorem 4 in the appendix we prove an analogous result for (1.2) with γ < 1/p. In this case maximizing sequences are always precompact up to symmetries, without an assumption like (1.7).
- Remark 1.6. Since the constant ap is explicit, the inequality (1.7) may be tested once knowing an upper bound on Sp and a lower bound for Ap. For p = 6 and p = 8 the maximization problem for Sp is solved by Gaussians, which leads to an explicit value for the number Sp. It sounds natural (but is not proved so far) that Sp is maximized by Gaussians for all p > 4. This would turn the right side of (1.7) into an explicit number and then the condition can be tested by using trial function for the Ap problem. To our knowledge, there is no conjecture on the precise form of maximizers for Ap.


This theorem is the analogue of [20, Thm 1.1], where compactness of maximizing sequences is also conditional on a strict comparison inequality between the full problem and the problem on the paraboloid. This is due to the fact that both the cubic curve η = ξ3 and the sphere are curved, implying that the paraboloid is the ‘local’ model of these hypersurfaces (except at ξ = 0 for the cubic curve). A maximizing sequence which would concentrate at a point would then, after rescaling, only see the problem for the paraboloid (see Remark 2.5 below) and hence be a test function for Sp. However, concentration around a point is clearly an obstacle to compactness, which explains the presence of Sp in the condition (1.7) to rule out this concentration around a point. From a broader perspective, relating compactness to a strict ‘energy’ inequality is a standard fact in several optimization problems: to prove the existence of a ground state for Schro¨dinger operators [36, Thm. 11.5], in the Br´ezisNirenberg [7, Lem. 1.2] or Yamabe [2] problems, and is even one of the main building blocks of the concentration-compactness theory of Lions [37] (the so-called ‘strict sub-additivity conditions’). Let us notice that the idea of ‘embedding’ the Schro¨dinger equation in the Airy equation also appeared in a nonlinear setting, as was noted for instance in [51, 13, 32].

What is peculiar in the strict inequality (1.7) is the presence of the constant ap. The fact that ap is strictly larger than 1 follows from the strict convexity of x  → xq/2 and Jensen’s inequality since dθ/(2π) is a probability measure on [0, 2π]. One of the striking features of our problem is that the main enemy is not concentration around one point, but rather concentration around two opposite points (or antipodal in the case of the sphere). As it turns out (see Lemma 2.4 and Remark 2.5 below), it is ‘energetically’ more favorable to concentrate around such a pair a points (with an equally split L2-mass), rather than at a single point. This is related to the fundamentally non-local nature of the Fourier transform, which implies that ‘bubbles’ concentrating at diﬀerent points on the hypersurface may have a Fourier transforms that ‘interact’, and in the case of these two special points, that may interact ‘attractively’. This mechanism has been discovered in [14] in the case of the sphere, and does not occur for the paraboloid, since no pair of points on the paraboloid have opposite normals. It does not happen either for other model optimization problems like sharp Sobolev (or Br´ezis-Nirenberg, Yamabe inequalities), since there the underlying operator is ‘local’ (the embedding H1 or H˙ 1 ֒→ Lq). Such two-point resonance requires speciﬁc tools, that we started to develop in [20], and investigate further in the present article.

In a certain sense our present work is complementary to [20]. The loss of compactness that we have to overcome here comes from the fact that the modulation symmetry of the Strichartz inequality (1.6) is broken for the Airy equation and becomes an ‘approximate symmetry’ for (1.4). The scaling symmetry of (1.6), however, is still an exact symmetry for (1.4). Conversely, in our work on the Stein–Tomas inequality the scaling symmetry was an ‘approximate symmetry’, while the modulation symmetry was an exact symmetry. For this reason the problems are diﬀerent on a technical level.

It is worth mentioning that the condition (1.7) does not appear in the works [14] or [46]: there, precompactness of optimizing sequences is unconditional. Likewise, we were able in [20] to prove that the condition analogue to (1.7) on the sphere was satisﬁed if maximizers of the Strichartz inequality (1.6) were Gaussians, as is known in dimension one and two.

Indeed, if Sp is attained for Gaussians, then one may ‘glue’ two Gaussians at two antipodal points on the sphere at a scale ε > 0. As ε → 0, the ‘energy’ of such a test function converges to apSp (as in Lemma 2.4). One is even able to compute the next order in ε of the energy, which turns out to be positive: this implies the strict inequality (1.7) on the sphere. In our setting of the cubic curve η = ξ3, one may try the same strategy since we know that in one space dimension and for p = q = 6 the optimizers of (1.6) are Gaussians. Unfortunately, the next order of the energy is negative, which does not allow to deduce (1.7).

A standard approach to proving results of the ﬂavor of Theorem 1 is to consider a maximizing sequence and to ‘follow the mass’. We show that either the mass escapes to small scales around a ﬁxed frequency (which is then ruled out by condition (1.7)), or it must be precompact up to symmetries. Such a strong dichotomy result for quite general sequences (being a maximizing sequence does not tell much about the sequence) usually follows from reﬁned versions of the considered inequality. We prove such a reﬁned Airy–Strichartz estimate in Section 3. Since we are in one space dimension, a reﬁned inequality may be proved in a quite elementary fashion using the Hausdorﬀ–Young inequality. In higher dimensions, it often relies on deep bilinear estimates such as the ones obtained by Tao [50].

Once concentration to small scales is ruled out, the reﬁned inequality typically implies the existence of a non-zero weak limit up to symmetry for the maximizing sequence. Upgrading this weak convergence to strong convergence is the content of the Method of the Missing Mass that was invented by Lieb [35] in the context of the Hardy–Littewood–Sobolev inequality and used later on, for instance, in [18, 19, 20]. A useful tool in order to apply this method is the Br´ezis–Lieb lemma [35, 6]. Here, we need a slightly more general version of this lemma (due to both the presence of mixed Lebesgue spaces and of these two attractively interacting bubbles), that we prove in Appendix A.

The article is organized as follows. In Section 2, we apply and adapt the Method of the Missing Mass to our context. In particular, we choose to present the full proof of Theorem 1 ﬁrst, and to prove the needed technical results in the following sections. We provide the proof in the complex-valued case, and only make remarks on why it also works in the real-valued case. In Section 3, we present the reﬁned Airy–Strichartz inequality. In Section 4, we study some approximate Airy–Strichartz maps and provide some convergence results about them. These results, although a bit technical, carry some crucial features of the proof. Finally, some auxiliary results are provided in the appendices.

Acknowledgments. R.L.F. would like to thank Terence Tao for suggesting to look at this problem for general p and to Diogo Oliveira e Silva, R´ene Quilodra´n and an anonymous referee for discussions concerning the Ap,R problem. Partial support through US National Science Foundation grant DMS-1363432 (R.L.F.) is also acknowledged.

2. Proof of Theorem 1: Method of the Missing Mass

The Method of the Missing Mass shows that a suﬃcient condition for precompactness up to symmetries is the existence of a non-zero weak limit up to symmetries. As a consequence, we will need the following deﬁnition.

Deﬁnition 2.1. Let (un) ⊂ L2(R). We write un ⇀sym 0 if for all (gn) ⊂ G we have gnun ⇀ 0 in L2(R).

We also deﬁne the ‘highest energy of sequences that are not precompact up to symmetry’:

|Ψp[un]|q dx

A∗p := sup limsup

n→∞ R R

p/q

dt : ||un||L2 = 1, un ⇀sym 0 .

Our main result is to identify exactly A∗p.

- Theorem 2. Let p > 4 and q such that 2/p + 1/q = 1/2. Then, we have A∗p = apSp ,


where Sp is deﬁned in (1.6) and ap is deﬁned in (1.8). Furthermore, the supremum deﬁning A∗p is attained, that is, there is a sequence (un) ⊂ L2(R) with ||un||L2 = 1 for all n, such that un ⇀sym 0, and limsupn→∞ ||Ψp[un]||pLp

tLqx = A∗p.

Remark 2.2. One can also deﬁne a quantity A∗p,R analogously to A∗p by restricting to sequences of real-valued functions. Then the exaxt same statement as in Theorem 2 holds, replacing

A∗p by A∗p,R. In fact, we clearly have A∗p,R A∗p and, since the sequence from Lemma 2.4 is real-valued, the proof of Theorem 2 will actually show that A∗p,R apSp. Therefore, the claim in the real-valued case follows from that in the complex-valued case.

Before proving Theorem 2, we explain how it implies Theorem 1 using the Method of the Missing Mass. Proposition 2.3. Let p > 4 and q such that 2/p + 1/q = 1/2. Then, all normalized maximizing sequences for Ap are precompact up to symmetries if and only if

Ap > A∗p.

Clearly, precompactness up to symmetries of maximizing sequences for Ap implies the existence of a maximizer for Ap.

Proof. Since we clearly always have Ap A∗p, the ‘only if’ part follows from the deﬁnition of A∗p and the fact that the supremum deﬁning it is attained, as stated in Theorem 2. Indeed, a sequence (un) satisfying ||un||L2 = 1 and un ⇀sym 0 cannot be precompact up to symmetries. We thus prove the ‘if’ part. Assume that Ap > A∗p, and let us apply the Method of the Missing Mass. Let (un) an optimizing sequence for Ap with ||un||L2 = 1. Since Ap > A∗p, we have un ⇀sym 0 and hence there exists (gn) ⊂ G such that gnun ⇀ v = 0 in L2(R), perhaps up to a subsequence (the sequence (gnun) is bounded in L2(R) and thus admits weak limits up to a subsequence). Let us write vn := gnun and rn := vn − v ⇀ 0 in L2(R). We have

1 = ||un||2L2 = ||vn||2L2 = ||v||2L2 + ||rn||2L2 + on→∞(1). (2.1)

Since rn ⇀ 0 in L2(R), we deduce that Ψp[rn] → 0 a.e. in R2 by Lemma D.1. Hence, by a variant of the Br´ezis–Lieb lemma [35, 6] for mixed Lebesgue spaces that we prove in

Proposition A.2, we have for α = min(p, q)

Aα/pp = ||Ψp[un]||αLptLqx + on→∞(1)

= ||Ψp[vn]||αLptLqx + on→∞(1) ||Ψp[v]||αLptLqx + ||Ψp[rn]||αLptLqx + on→∞(1) Aα/pp (||v||αL2 + ||rn||αL2) + on→∞(1).

Using (2.1) and passing to the limit n → ∞, we ﬁnd, because of Ap > 0,

1 ||v||αL2 + (1 − ||v||2L2)α/2. Since p, q > 2, we always have α = min(p, q) > 2 and thus aα/2 + bα/2 (a + b)α/2 for all a, b 0 with equality if and only if a = 0 or b = 0. Hence, we ﬁnd that either ||v||2L2 = 0 or 1− ||v||2L2 = 0. Since v = 0, this means that 0 = 1−||v||2L2 = limn→∞ ||rn||2L2 = limn→∞ ||vn − v||2L2, implying that (vn) = (gnun) converges strongly in L2(R).

Theorem 1 follows clearly from the combination of Proposition 2.3 and Theorem 2. It remains to prove Theorem 2, that is, to relate A∗p to the best constant in the Strichartz inequality. To make the constant A∗p more explicit, we prove that an optimizing sequence for A∗p must concentrate at two (distinct) opposite frequencies, which is reminiscent of what happens for the Stein–Tomas inequality [14, 46, 20]. We ﬁrst compute the ‘energy’ of such a sequence.

Lemma 2.4. Let p > 4 and q such that 2/p + 1/q = 1/2. Let χ ∈ L2(R), χ = 0, and ε > 0. Deﬁne

![image 18](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile18.png>)

ξ − 1 ε

ξ + 1 ε

∀ξ ∈ R, χε(ξ) = χ

+ χ −

. Then, we have

![image 19](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile19.png>)

![image 20](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile20.png>)

p/q

|Ψp[χε](t, x)|qdx

dt ||χε||pL2

R R

![image 21](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile21.png>)

where ap is deﬁned in (1.8).

ε→0

p/q

2 x

|(e−3it∂

χ)(x)|qdx

dt ||χ||pL2

ap R R

−−→

,

![image 22](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile22.png>)

- Remark 2.5. If the sequence concentrates at one frequency rather than two, by taking for instance χε(ξ) = χ((ξ − 1)/ε), one has


p/q

p/q

2 x

|(e−3it∂

χ)(x)|qdx

|Ψp[χε](t, x)|qdx

dt ||χ||pL2

dt ||χε||pL2

R R

R R

−−→

.

![image 23](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile23.png>)

![image 24](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile24.png>)

ε→0

In particular, since ap > 1 it is ‘energetically’ more favorable to concentrate at two frequencies rather than one. Similarly, our analysis will show that concentrating at more than two points is ‘energetically’ unfavorable.

- Remark 2.6. It is important to notice that the transformation χ → χ((· − 1)/ε) is not a symmetry of the Airy–Strichartz inequality, which means that translations in frequency (Galilean boosts) are not symmetries of the Airy–Strichartz inequality. By taking the limit of such a translation to inﬁnity, one ﬁnds an eﬀective ‘energy’, the Strichartz energy for the standard Schro¨dinger evolution, which is now invariant by Galilean boosts. They are thus ‘approximate symmetries’ of the Airy–Strichartz inequality.
- Remark 2.7. A computation similar to the one in Lemma 2.4 appears in [44, Lem. 6.1], but with a diﬀerent result. We believe that the problem in [44, Lem. 6.1] is the passage from Eq. (89) to Eq. (90). For the same reason there is a problem in [44, Lem. 5.1], because


the L6t,x-norm does not split, for instance, when the sequence concentrates at two opposite frequencies. This does not aﬀect the validity of [44, Thm. 1.5], but it does aﬀect the validity of [44, Thm. 1.9], since [44, Lem. 5.1] is used in its proof. Let us also notice that in the real-valued version of the proﬁle decomposition of [44], two opposite frequencies necessarily carry the same proﬁle.

Proof of Lemma 2.4. First, we clearly have

||χε||2L2 = 2ε ||χ||2L2 + oε→0(1). Next, we have

ε √2π R |1 + εξ|1/qeit(1+εξ)

3+ix(1+εξ) χ(ξ) dξ

Ψp[χε](t, x) = 2Re

![image 25](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile25.png>)

![image 26](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile26.png>)

ε √2π

2ξ2+ε3ξ3)+iεξ(x+3t) χ(ξ) dξ. Changing variables x → x − 3t and then (x, t) → (x/ε, t/ε2), we ﬁnd

|1 + εξ|1/qeit(3ε

ei(x+t)

= 2Re

![image 27](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile27.png>)

![image 28](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile28.png>)

R

1 √2π

ε−ε22t)

ei(

x

- 1

![image 29](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile29.png>)

- 2 2Re


2+εξ3)+ixξ χ(ξ)dξ

|1 + εξ|1/qeit(3ξ

||Ψp[χε]||LptLqx = ε

![image 30](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile30.png>)

![image 31](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile31.png>)

![image 32](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile32.png>)

![image 33](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile33.png>)

Lpt Lqx

R

- 1

![image 34](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile34.png>)

- 2 2Reei(


ε−ε22t)(Tq,εχ)(t, x)

x

= ε

,

![image 35](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile35.png>)

![image 36](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile36.png>)

Lpt Lqx

where the operator Tq,ε is deﬁned in Section 4. In particular, using Lemma 4.1, we deduce that

- 1

![image 37](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile37.png>)

- 2 2Reei(


ε−ε22t)(e−3it∂

x

- 1

![image 38](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile38.png>)

- 2).


2

||Ψp[χε]||LptLqx = ε

+ oε→0(ε For a.e. (t, x) ∈ R2, the function θ ∈ (R/(2πZ))2  → |2Reei(θ

xχ)(x)

![image 39](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile39.png>)

![image 40](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile40.png>)

Lpt Lqx

1−2θ2)(e−3it∂x2χ)(x)|q is continu-

ous, and its maximum, 2q|(e−3it∂x2χ)(x)|q, belongs to Lp/qt L1x(R × R). Using Lemma B.1, we deduce that

p/q

ε−ε22t)(e−3it∂

|2Reei(

x

2

xχ)(x)|q dx

dt

lim

![image 41](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile41.png>)

![image 42](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile42.png>)

ε→0 R R

p/q

2π

2π

- 1

![image 43](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile43.png>)

- 2π


- 1

![image 44](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile44.png>)

- 2π


2 x

|2Reei(θ

1−2θ2)(e−3it∂

χ)(x)|qdxdθ1

=

dtdθ2

0 R

0 R

p/q

2π

- 1

![image 45](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile45.png>)

- 2π


2

|2Reeiθ(e−3it∂

xχ)(x)|qdxdθ

dt.

=

0 R

R

As a consequence, we have

p/q

2π

- 1

![image 46](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile46.png>)

- 2π


2

||Ψp[χε]||pLp

tLqx = εp/2

dt + oε→0(εp/2)

|2Reeiθ(e−3it∂

xχ)(x)|qdxdθ

R

0 R

p/q

p/q

2π

1 2π

2 x

χ)(x)|qdx

(1 + cosθ)q/2 dθ

|(e−3it∂

= (2ε)p/2

dt

![image 47](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile47.png>)

R R

0

+ oε→0(εp/2). In the second equality we used the fact that for any z ∈ C we have

2π

2π

- 1

![image 48](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile48.png>)

- 2π


dθ 2π

(1 + cosθ)q/2

|eiθz + e−iθz|q dθ = 2q/2|z|q

. (2.2) This implies the result.

![image 49](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile49.png>)

![image 50](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile50.png>)

0

0

We now turn to the proof of Theorem 2, which interestingly uses a more involved version of the Method of the Missing Mass. Proof of Theorem 2. Let us ﬁrst show that A∗p apSp. For a sequence (εn) ⊂ (0, ∞) converging to 0 and χ ∈ L2(R) with χ = 0 we deﬁne χε

n||L2. Let us show that un ⇀sym 0. Hence, let (gn) = (gt

/ ||χε

as in Lemma 2.4 and set un := χε

n

n

n,xn,λn) ⊂ G, and let us show that gnun ⇀ 0 in L2(R), which is equivalent to showing that any subsequence of (gnun) has a sub-subsequence converging weakly to zero in L2(R). We show it for each one of the two bubbles composing un, which amounts to showing that

ξ  → (λnεn)−1/2 χ

ξ − λn λnεn

![image 51](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile51.png>)

xn λn ξ+iλtn3

ξ3

ei

![image 52](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile52.png>)

![image 53](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile53.png>)

n

has a subsequence converging weakly to zero as n → ∞. Up to a subsequence, we have λnεn → c as n → ∞, with c = 0, 0 < c < ∞, or c = ∞. In the cases c = 0 or c = ∞, it is clear that it converges weakly to zero. If 0 < c < ∞, we must have λn → ∞ and we thus also have weak convergence to zero.

According to Lemma 2.4 we have

p/q

2 x

|(e−3it∂

χ)(x)|qdx

dt ||χ||pL2

p/q

ap R R

|Ψp[un](t, x)|qdx

dt −−−→

lim

![image 54](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile54.png>)

n→∞ R R

n→∞

and therefore

p/q

2

|(e−3it∂

xχ)(x)|qdx

dt ||χ||pL2

A∗p ≥ ap R R

.

![image 55](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile55.png>)

By taking the supremum over χ ∈ L2(R), χ = 0, we conclude that A∗p apSp.

Moreover, from [45] we know that there is a maximizer for the Strichartz problem Sp, and taking χ in the above argument to be this maximizer we obtain a sequence (un) with

un L2 = 1 and un ⇀sym 0 such that limn→∞ Ψp[un] pLp

tLqx → apSp. Thus, once we have shown the reverse inequality A∗p apSp, we have also proved the last statement in Theorem 2.

Thus, it remains to show the inequality A∗p apSp. Let (un) ⊂ L2(R) be a sequence such that ||un||L2 = 1 and un ⇀sym 0, satisfying

p/q

- 1

![image 56](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile56.png>)

- 2A∗p.


|Ψp[un]|qdx

limsup

dt

n→∞ R R

We decompose un as

un = un,> + un,< with un,> = 1R

un. Since Ψp[un] = Ψp[un,>] + Ψp[un,<], we have

un and un,< = 1R

+

−

|Ψp[un]|qdx

R

p/q

2p−1

|Ψp[un,>]|qdx

R

p/q

+

|Ψp[un,<]|qdx

R

p/q

.

Integrating this inequality with respect to t and estimating the right side, we ﬁnd

||Ψp[un,>]||pLp

tLqx 2p max ||Ψp[un,>]||pLp

tLqx , ||Ψp[un,>]||pLp

tLqx . Passing to a subsequence and replacing un to un(−·) if necessary (which is still an admissible sequence for A∗p), we may assume that the maximum is always attained at ||Ψp[un,>]||pLp

tLqx. Thus,

1

||Ψp[un,>]||pLp

2p+1A∗p and, in particular, Ψp[un,>] 0 in LptLqx.

limsup

t Lqx

![image 57](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile57.png>)

n→∞

By Corollary 3.2, there are (gn) ⊂ G and (ηn) ⊂ R+ with ηn 1/2 such that the sequence (( gnun,>)(· + ηn)) has a weak limit v> = 0 in L2(R), with a lower bound

||v>||L2 γ > 0,

where γ only depends on p. We have ηn → ∞, for otherwise ηn → c ∈ R up to a subsequence, and then (gnun,>) has a non-zero weak limit, which then implies that (gnun) has a non-zero weak limit point, which contradicts un ⇀sym 0.

Since supp gnun,>(· + ηn) ⊂ [−ηn, +∞), we may write gnun,>(η + ηn) =: v>(η) + rn,>(η)

= 1η+η

n 0 v>(η) + 1η+η

n 0 rn,>(η)

= v>(η) − 1η+η

n<0 v>(η) + 1η+η

n 0 rn,>(η)

=: v>(η) + rn,>(2) (η) + rn,>(1) (η),

with rn,>(1) ⇀ 0 in L2(R), supp rn,>(1) ⊂ [−ηn, +∞) and rn,>(2) → 0 strongly in L2(R). Furthermore, the sequence ( gnun,<(− · −ηn)) is bounded in L2(R), and hence admits a weak limit v< (which may be zero) in L2(R), up to a subsequence. We split accordingly

gnun,<(− · −ηn) = v< + rn,<(2) + rn,<(1)

with rn,<(1) ⇀ 0 in L2(R), supp rn,<(1) ⊂ [−ηn, +∞) and rn,<(2) → 0 strongly in L2(R). Deﬁning δn := 1/ηn → 0, we now have

||Ψp[un]||LptLqx = ||Ψp[gnun,>] + Ψp[gnun,<]||LptLqx

![image 58](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile58.png>)

(v> + rn,>(1) + rn,>(2) )+e−ix/δ

(v< + rn,<(1) + rn,<(2) )

n+2it/δn2Tp,δ

n−2it/δn2Tp,δ

= eix/δ

n

n

Lpt Lqx

with an operator Tp,δ deﬁned in Section 4. By Lemma 4.3, we deduce that Tp,δ

rn,<(1) → 0 almost everywhere in (t, x) ∈ R × R. By Lemma 4.1, we also deduce that Tp,δ

rn,>(1) → 0 and Tp,δ

n

n

(v< + rn,<(2) ) → e−3it∂

(v> + rn,>(2) ) → e−3it∂

2 x

2 x

v< strongly in LptLqx. Using Proposition A.2 applied with

v> and Tp,δ

n

n

![image 59](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile59.png>)

n+2it/δn2e−3it∂x2v<, ρn := eix/δ

n−2it/δn2e−3it∂x2v> + e−ix/δ

Πn := eix/δ

![image 60](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile60.png>)

rn,<(1) , we deduce that

rn,>(1) + e−ix/δ

n+2it/δn2Tδ

n−2it/δn2Tδ

n

n

||Ψp[un]||αLptLqx A1,n + A2,n + on→∞(1) (2.3) with α = min(p, q) and

 

- A1,n := eix/δ

n−2it/δn2e−3it∂x2v> + e−ix/δ

n+2it/δn2e−3it∂x2v<

![image 61](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile61.png>)

α

Lpt Lqx

,

- A2,n = eix/δ


α

![image 62](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile62.png>)



rn,>(1) + e−ix/δ

rn,<(1)

n+2it/δn2Tδ

n−2it/δn2Tδ

.

n

n

Lpt Lqx

Using Lemma B.1 in the same way as in the proof of Lemma 2.4, we ﬁnd that

lim

A1,n =

n→∞

R

- 1

![image 63](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile63.png>)

- 2π


2π

0 R

q

2

![image 64](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile64.png>)

eiθ(e−3it∂

xv>)(x) + e−iθ(e−3it∂x2v<)(x)

dxdθ

p/q

dt

α/p

.

For any z1, z2 ∈ C we have

2π

- 1

![image 65](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile65.png>)

- 2π


|eiθz1 + e−iθz2|q dθ = (|z1|2 + |z2|2)q/2

0

2π

dθ 2π

(1 + acosθ)q/2

![image 66](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile66.png>)

0

(2.4)

with a = 2|z1||z2|/(|z1|2 + |z2|2) ∈ [0, 1]. (Note that this is the generalization of (2.2) to z1 = z2.) As in the proof of Lemma 6.1 in [20], this last function can be shown to be maximal at a = 1. As a consequence,

![image 67](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile67.png>)

- 1

![image 68](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile68.png>)

- 2π


2π

|eiθz1 + e−iθz2|q dθ (|z1|2 + |z2|2)q/2

0

2π

dθ 2π

(1 + cosθ)q/2

![image 69](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile69.png>)

0

= aq/pp (|z1|2 + |z2|2)q/2,

and thus, by the triangle inequality in Lp/t 2Lq/x 2 (noting that p, q ≥ 2),

A1,n aα/pp

lim

n→∞

R R

2 x

|e−3it∂

2 x

v>|2 + |e−3it∂

v<|2

q/2

dx

p/q

dt

α/p

α/2

2

2

2

2

+ e−3it∂

aα/pp e−3it∂

xv<

xv>

Lpt Lqx

Lpt Lqx

α/2 .

aα/pp Spα/p ||v>||2L2 + ||v<||2L2

Concerning the term A2,n, reversing the change of variables in (t, x, η) that we have done, we ﬁnd that

A2,n = ||Ψp[wn]||αLptLqx , with

wn(η) := rn,>(1) (η − ηn) + rn,<(1) (−η − ηn)

= gnun(η) − v>(η − ηn) − v<(−η − ηn) − rn,>(2) (η − ηn) − rn,<(2) (−η − ηn).

Let us show that wn ⇀sym 0. Since un ⇀sym 0, we also have gnun ⇀sym 0. As we have seen in the beginning of the proof, translating a ﬁxed proﬁle to inﬁnity in frequencies gives a sequences that vanishes weakly up to any symmetry. Hence, the terms involving v> and v< also ⇀sym 0. Finally, the terms involving rn,>(2) and rn,<(2) converge strongly to zero in L2, and thus also ⇀sym 0. Hence, we have proved that wn ⇀sym 0.

Since

supp rn,>(1) (· − ηn) ⊂ R+, supp rn,<(1) (− · −ηn) ⊂ R−, we deduce that

2 L2

2 L2

+ rn,<(1)

||wn||2L2 = rn,>(1)

. By the deﬁnitions of rn,>(1) and rn,<(1) and their weak convergence to zero, we also have rn,>(1)

2 L2

2 L2

= ||un,>||2L2 − ||v>||2L2 + o(1), rn,<(1)

= ||un,<||2L2 − ||v<||2L2 + o(1), which implies that

||wn||2L2 = ||un||2L2 − ||v>||2L2 − ||v<||2L2 + o(1) = 1 − ||v>||2L2 − ||v<||2L2 + o(1). If ||v>||2L2 + ||v<||2L2 < 1, then wn/ ||wn||L2 ⇀sym 0 and by deﬁnition of A∗p we ﬁnd that limsup

||Ψp[wn]||pLp

tLqx A∗p(1 − ||v>||2L2 − ||v<||2L2)p/2.

n→∞

If ||v>||2L2 +||v<||2L2 = 1, then wn → 0 strongly in L2, so that the same inequality holds by the Airy–Strichartz inequality.

We now insert our asymptotic estimates on A1,n and A2,n into (2.3) and take the limit n → ∞. This yields the inequality

α/2 + (A∗p)α/p(1 − ||v>||2L2 − ||v<||2L2)α/2,

||Ψp[un]||αLptLqx aα/pp Spα/p ||v>||2L2 + ||v<||2L2

limsup

n→∞

which we may rewrite as

α/2

1 − (1 − ||v>||2L2 − ||v<||2L2)α/2 (A∗p)α/p − aα/pp Spα/p ||v>||2L2 + ||v<||2L2

||Ψp[un]||αLptLqx

(A∗p)α/p − limsup

n→∞

By the elementary estimate 1 − (1 − x)α/2 xα/2 valid for all x ∈ [0, 1] since α > 2, this implies that

α/2 ((A∗p)α/p − aα/pp Spα/p)

||Ψp[un]||αLptLqx ||v>||2L2 + ||v<||2L2

(A∗p)α/p − limsup

n→∞

γα((A∗p)α/p − aα/pp Spα/p). Taking the supremum over all such sequences (un), the left side vanishes, indeed showing that A∗p apSp.

We end this section by some remarks about the real-valued case.

- Lemma 2.8. For any triplet (p, q, γ) with p, q 2, we have


|Dx|γe−t∂x3u

|Dx|γe−t∂x3u

Lpt Lqx

Lpt Lqx

sup

= sup

. (2.5)

![image 70](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile70.png>)

![image 71](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile71.png>)

||u||L2x

||u||L2x

u∈L2(R,C)\{0}

u∈L2(R,R)\{0}

Moreover, there is a maximizer for the supremum on the left side if and only if there is one for the supremum on the right side.

Proof. While the inequality is clear, let us show the inequality . Hence, let u ∈ L2(R, C), u = 0. Splitting u as u = Reu + iImu and using that the operator |Dx|γe−t∂x3 preserves real-valuedness, we deduce that

3 x

3 x

3 x

Imu)2, so that

||Dx|γe−t∂

u|2 = (|Dx|γe−t∂

Reu)2 + (|Dx|γe−t∂

1/2

3 x

3 x

3 x

= (|Dx|γe−t∂

Reu)2 + (|Dx|γe−t∂

Imu)2

|Dx|γe−t∂

u

.

Lp/t 2Lq/x 2

Lpt Lqx

Using the triangle inequality in Lp/t 2Lq/x 2, we deduce |Dx|γe−t∂

1/2

2

2

3 x

3 x

3 x

+ |Dx|γe−t∂

|Dx|γe−t∂

Imu

Reu

u

Lpt Lqx

Lpt Lqx

Lpt Lqx

|Dx|γe−t∂x3v

1/2

Lpt Lqx

||Reu||2L2x + ||Imu||2L2x

.

sup

![image 72](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile72.png>)

||v||L2x

v∈L2(R,R)\{0}

1/2

Finally, using that |u|2 = (Reu)2 + (Imu)2 and hence ||Reu||2L2x + ||Imu||2L2x

= ||u||L2x, we deduce the inequality in (2.5) by taking the supremum over all u.

The equality of the suprema in (2.5) implies that, if u is a maximizer for the supremum on the right side, then it is also a maximizer for the one on the left side. Conversely, by tracking the equality cases in the previous proof, one sees that if u is a maximizer for the supremum on the left, then Reu or Imu is a maximizer for the supremum on the right.

- Remark 2.9. It is natural to wonder whether maximizers for Ap are necessarily complex multiples of real-valued functions. We do not know how to deduce this using the above method


of proof. In fact, we from the equality case in the triangle inequality in Lp/t 2Lq/x 2 we learn that either Imu = 0 or there is a λ 0 such that (|Dx|γe−t∂x3 Reu)2 = λ(|Dx|γe−t∂x3 Imu)2 almost everywhere.

- Lemma 2.8 shows that Ap = Ap,R, from which we deduce the ‘if’ part of the analogue of


Theorem 1 in the real-valued case (because any real-valued maximizing sequence for Ap,R is then also a complex-valued maximizing sequence for Ap). The ‘only if’ part follows from the fact that the sequence built in Lemma 2.4 is real-valued.

The rest of the article is devoted to the proofs of the results used during this last section.

3. A refined Airy–Strichartz inequality

3.1. Reﬁned inequality and its consequences. We begin with the compactness result that allows us to extract a non-trivial proﬁle from an optimizing sequence. It will follow from a reﬁned version of the Airy–Strichartz inequality.

Theorem 3. There are θ ∈ (0, 1) and C > 0 such that for all u ∈ L2(R) we have

θ

- 1

![image 73](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile73.png>)

- 2


1 6

||u||1L−2θ , (3.1)

3

3

|Dx|1/6e−t∂

|I|−

|c(I)|−

|Dx|1/6e−t∂

xuI

C sup

xu

![image 74](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile74.png>)

L6t,x(R×R)

L∞t,x

I∈D

where D denotes the family of dyadic intervals of R (see Deﬁnition 3.4 below), |I| denotes the length of the interval I, c(I) its center, and uI := u|I.

Similar reﬁned inequalities appeared previously in the literature, for instance in the context of the Sobolev inequality [21] (see also [33, Prop. 4.8]), the Stein–Tomas inequality [39, 40, 46, 20], or the Strichartz inequality [5, 38, 9, 3]. In the context of the Airy equation, related reﬁned inequalities appeared in [31] (see [44] for a diﬀerent proof). The particularity of our estimate (3.1) is the presence of an L∞t,x-norm on the right side, which provides a rather direct route to compactness as we will shortly see. The strategy via such L∞t,x-norms has been initiated in [52, 33], and we followed it in [20] (see also, for instance, [18]). Contrary to the aforementioned works, the center c(I) of the interval I appears on the right side of (3.1); this is due to the fact that the Airy–Strichartz inequality is not invariant by translations in Fourier space. This is the ﬁrst time we encounter such a phenomenon.

From the reﬁned estimate in L6t,x, we deduce a reﬁned estimate in mixed Lebesgue spaces LptLqx by complex interpolation.

- Corollary 3.1. Let p > 4 and q such that 2/p + 1/q = 1/2. Then, there exist θ ∈ (0, 1) and C > 0 such that for all u ∈ L2(R) we have


θ

1 2

1 6

||u||1L−2θ . (3.2)

3 x

3 x

|I|−

|Dx|1/6e−t∂

|c(I)|−

|Dx|1/pe−t∂

uI

u

C sup

![image 75](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile75.png>)

![image 76](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile76.png>)

Lpt Lqx(R×R)

L∞t,x

I∈D

Proof. When p = 6, this is Theorem 3. When p = 6, we distinguish two cases. If p > 6, we pick p > p and q such that 2/ p + 1/ q = 1/2 so that by Proposition C.1 we have

3 x

|Dx|1/pe−t∂

u

Lpt Lqx

3 x

|Dx|1/ pe−t∂

u

θ

L pt L qx

3 x

|Dx|1/6e−t∂

u

1−θ

,

L6t,x

where θ ∈ (0, 1) is such that 1/p = θ/ p + (1 − θ)/6. By the Airy–Strichartz inequality, we have

3 x

|Dx|1/ pe−t∂

C ||u||L2x .

u

L pt L qx

The L6t,x-part may be estimated by Theorem 3, which gives the result. When p < 6, we interpolate in the same fashion LptLqx between L6t,x and L ptL qx with 4 < p < p, which gives the same result.

Our main interest in proving the reﬁned estimate (3.2) is to ﬁnd a non-trivial weak limit (a ﬁrst ’proﬁle’ in the proﬁle decomposition), in the case of non-vanishing sequences (in the language of concentration-compactness).

- Corollary 3.2. Let p > 4 and q such that 2/p + 1/q = 1/2. Let (un) be a bounded sequence in L2(R) with supp un ⊂ R± such that


3

xun 0 in LptLqx .

|Dx|1/pe−t∂

Then, there are (tn, xn, ξn, λn) ⊂ R × R × R± × R∗+ with λn/|ξn| 2 such that, after passing to a subsequence if necessary, the sequence (( gnun)(· + ξn/λn)) with gn = gt

n,xn,λ−n1 has a non-zero weak limit v in L2(R). Furthermore, if a, b > 0 are such that

3

|Dx|1/pe−t∂

a, ||un||L2 b, then we have the estimate

xun

limsup

Lpt Lqx

n→∞

||v||L2 caαb−β, where c, α, β > 0 depend only on p.

- Remark 3.3. In the previous statement, when we write (ξn) ⊂ R±, we mean that we may choose (ξn) ⊂ R+ if supp un ⊂ R+ or (ξn) ⊂ R− if supp un ⊂ R−.


Proof. By the reﬁned estimate (3.2), there are (tn, xn) ⊂ R×R and dyadic intervals In ⊂ R± such that, along a subsequence,

1 6

|c(In)|−

![image 77](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile77.png>)

- 1

![image 78](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile78.png>)

- 2 In


nξ+itnξ3 un(ξ) dξ ε :=

|ξ|1/6eix

|In|−

a 2Cb1−θ

![image 79](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile79.png>)

1

![image 80](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile80.png>)

θ ,

where C, θ are the constants appearing in (3.2). Denote by ξn := c(In) and λn = |In| so that In = ξn + λn(−1/2, 1/2), and 0 < λn/|ξn| 2 (see Deﬁnition 3.4 below). Up to a subsequence, we may assume that λn/|ξn| → δ ∈ [0, 2]. In the previous integral, write any ξ as ξ = ξn + λnη to obtain

(−1/2,1/2)

1/6

λn ξn

n(ξn+λnη)+itn(ξn+λnη)3λ1n/2 un(ξn + λnη) dη ε

eix

η

1 +

![image 81](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile81.png>)

for all n. The sequence vn(η) := eix

n(ξn+λnη)+itn(ξn+λnη)3λ1n/2 un(ξn + λnη) is bounded in L2(R). Pick any weak limit v of it. Since we have the convergence

1(−1/2,1/2)|1 + (λn/|ξn|) · |1/6 → 1(−1/2,1/2)|1 + δ · |1/6 strongly in L2(R), we deduce that

|1 + δη|1/6v(η) dη ε > 0,

(−1/2,1/2)

implying that v = 0. By the Cauchy-Schwarz inequality, we also have

ε ||v||L2

|1 + δη|1/3 dη

(−1/2,1/2)

1/2

||v||L2

(1 + 2|η|)1/3 dη

(−1/2,1/2)

1/2

,

since δ ∈ [0, 2], which implies the desired lower bound on ||v||L2.

We now turn to the proof of Theorem 3, following the strategy of [52, App. A] and [33, Prop. 4.24], that we also followed in [20]. We ﬁrst state some properties of dyadic intervals.

- 3.2. Dyadic intervals.


- Deﬁnition 3.4. An interval I ⊂ R is dyadic if it can be written as I = [k, k + 1)2ℓ with k ∈ Z and ℓ ∈ Z. For any interval I, we denote by |I| its length and c(I) its center.

Any dyadic interval generates two dyadic sub-intervals of half length, and reciprocally any dyadic interval has a unique parent of double length, which is also a dyadic interval. Two dyadic intervals are said to be adjacent if they have the same length and share an extremity.

- Deﬁnition 3.5. For two dyadic intervals I and I′, we write I ∼ I′ if I and I′ are not adjacent, if their parents are not adjacent, but their grand-parents are adjacent (in particular, they have the same length).


In the following lemma, we record several useful properties of such intervals.

- Lemma 3.6. Assume I and I′ are two dyadic intervals with I ∼ I′ and either I, I′ ⊂ R+ or I, I′ ⊂ R−. Then, the following properties hold:


- (1) ∀η ∈ I, |η| 2|c(I)|,
- (2) |c(I′)| 15|c(I)|,
- (3) ∀η ∈ I, ∀η′ ∈ I′, 54|c(I + I′)| |η + η′| 5 6|c(I + I′)|,

![image 82](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile82.png>)

![image 83](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile83.png>)

- (4) ∀η ∈ I, ∀η′ ∈ I′, 2|I| |η − η′| 8|I|.


Proof. Up to replacing I by −I and I′ by −I′, we may assume that I, I′ ⊂ R+. We thus may write I = [k, k + 1)|I| and I′ = [k′, k′ + 1)|I′| for some k, k′ 0. We have c(I) = (k + 1/2)|I| (1/2)|I|, hence for any η ∈ I, we have η c(I) + (1/2)|I| 2c(I), which is (1). Furthermore, since I ∼ I′, we deduce k′ k + 7, and hence c(I′) = (k′ + 1/2)|I| (k + 15/2)|I| 15(k + 1/2)|I| = 15c(I), which is (2). Now let η ∈ I, η′ ∈ I′. Since I ∼ I′,

we have k +k′ 4, hence c(I +I′) = (k +k′+1)|I| 5|I| which implies |I| (1/5)c(I +I′). As a consequence

6 5

- 4

![image 84](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile84.png>)

- 5


c(I + I′), which is (3). Finally, (4) follows from the fact that I ∼ I′.

c(I + I′) c(I + I′) − |I| η + η′ c(I + I′) + |I|

![image 85](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile85.png>)

- 3.3. Bilinear estimates. Bilinear estimates are the main building blocks to obtain reﬁned inequalities. In the context of the Stein–Tomas or Strichartz inequalities, they are provided by the deep result of [50]. Since we work in one space dimension, bilinear estimates are rather easy to obtain by the Hausdorﬀ–Young inequality (as done for instance in [44, Lem 1.2] or [9, Prop. 2.1]). One special feature of our approach is the distinction between positive or negative frequencies, which we may interpret as the separation between the two ’conjugate’ points ξ and −ξ which are the main enemies for proving compactness.


For any function u ∈ L2(R) and any interval I ⊂ R, we deﬁne the function uI by the relation

uI = 1I u.

- Lemma 3.7. For all q 2, there exists C > 0 such that for all dyadic intervals I ∼ I′ with either I, I′ ⊂ R+ or I, I′ ⊂ R−, and for any u, v ∈ L2(R) we have


3−1q|I|1−

3 q

1

3 x

3 x

|Dx|1/6e−t∂

uI |Dx|1/6e−t∂

||u||L2(R) ||v||L2(R) . (3.3)

C|c(I)|

vI′

![image 86](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile86.png>)

![image 87](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile87.png>)

![image 88](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile88.png>)

Lqt,x(R×R)

Remark 3.8. The point of the previous lemma is to have q < 3. Hence, when assuming some properties of the Fourier support, one can do better than the Airy–Strichartz inequality.

Proof. We have the identity for all x ∈ R |Dx|1/6e−t∂

3

3

xuI (x) |Dx|1/6e−t∂

xvI′ (x)

- 1

![image 89](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile89.png>)

- 2π R R


=

′)+it(η3+η′3)|η|1/6|η′|1/6 uI(η) vI′(η′) dη dη′.

eix(η+η

Denoting by f(η, η′) := |η|1/6|η′|1/6 uI(η) vI′(η′) and changing variables (r, s) = (η + η′, η3 + η′3) = ψ(η, η′), we ﬁnd that

3

3

|Dx|1/6e−t∂

xuI (x) |Dx|1/6e−t∂

xvI′ (x)

dr ds |ψ−1(r, s)21 − ψ−1(r, s)22|

1 6π R R

eixr+itsf(ψ−1(r, s))

,

=

![image 90](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile90.png>)

![image 91](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile91.png>)

which we estimate using the Hausdorﬀ–Young inequality (where q′ is the dual exponent of q)

f(ψ−1(r, s)) |ψ−1(r, s)21 − ψ−1(r, s)22| Lqr,s′

3

3

|Dx|1/6e−t∂

xuI |Dx|1/6e−t∂

C

xvI′

. Undoing the change of variables we ﬁnd

![image 92](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile92.png>)

Lqt,x

f(ψ−1(r, s)) |ψ−1(r, s)21 − ψ−1(r, s)22| Lqr,s′

=

![image 93](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile93.png>)

R R

|η|1/6|η′|1/6 uI(η) vI′(η′) |η2 − η′2|

![image 94](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile94.png>)

q′

3|η2 − η′2| dη dη′

1/q′

.

By Lemma 3.6, we have on the support of the last integral

|η|q′/6|η′|q′/6 |η + η′|q′−1|η − η′|q′−1

- 2

![image 95](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile95.png>)

- 3q′|I|1−q


′

C|c(I)|1−

. Estimating

![image 96](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile96.png>)

′

′/2 ||u||q

′

dη |I|1−q

| uI(η)|q

L2 , we arrive at the result.

R

- 3.4. Proof of Theorem 3. Let u ∈ L2(R). By splitting u as u = u> +u< with u> = 1R


u, we may assume that supp u ⊂ R+ or supp u ⊂ R−. For any dyadic interval I, we use the notation

+

3

ΨI := |Dx|1/6e−t∂

xuI. Since for any (η, η′) ∈ R2 with η = η′, there is a unique pair of dyadic intervals (I, I′) of maximal length with I ∼ I′, η ∈ I, and η′ ∈ I′, the identity

1I(η)1I′(η′) induces the decomposition

∀η = η′, 1 =

I∼I′

3 x

|Dx|1/6e−t∂

u

2

=

ΨIΨI′, (3.4)

I∼I′

which we estimate using the following lemma, exploiting some orthogonality between the Fourier supports of each term under the previous sum.

- Lemma 3.9. There exists C > 0 such that for all u ∈ L2(R) with supp u ⊂ R− or R+, we have


3/2

||ΨIΨI′||3L/32

ΨIΨI′

.

C

t,x

I∼I′

I∼I′

L3t,x

Assuming Lemma 3.9, we ﬁnish the proof of Theorem 3. We estimate ||ΨIΨI′||L3t,x in two diﬀerent ways. First, using Lemma 3.7 and Lemma 3.6 we conclude that for any q ∈ [2, 3),

q 3

1−3q

1

q−13|I|

3

![image 97](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile97.png>)

![image 98](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile98.png>)

1 3

q−1 ||ΨIΨI′||Lqt,x

||ΨIΨI′||L3t,x |c(I)|−

|I|−1 ||ΨIΨI′||L∞t,x

|c(I)|

![image 99](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile99.png>)

![image 100](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile100.png>)

![image 101](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile101.png>)

![image 102](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile102.png>)

1−q3

1−q3

- 2q

![image 103](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile103.png>)

- 3


![image 104](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile104.png>)

![image 105](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile105.png>)

1 6

1 6

- 1

![image 106](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile106.png>)

- 2


- 1

![image 107](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile107.png>)

- 2


|c(I)|−

C |c(I)|−

|I|−

|I|−

||u||

||ΨI′||L∞t,x

||ΨI||L∞t,x

![image 108](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile108.png>)

![image 109](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile109.png>)

L2

2−23q

![image 110](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile110.png>)

- 2q

![image 111](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile111.png>)

- 3


- 1

![image 112](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile112.png>)

- 2


1 6

|I′′|−

|c(I′′)|−

||ΨI′′||L∞t,x

||u||

L2 . (3.5) Secondly, by an elementary estimate, using also Lemma 3.6 we ﬁnd

C sup

![image 113](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile113.png>)

I′′∈D

1 3

||ΨIΨI′||L∞t,x C|c(I)|

|| uI||L1 || uI′||L1 , and then by interpolation with Lemma 3.7 we infer that

![image 114](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile114.png>)

2 s

||ΨIΨI′||L3t,x C|I|1−

![image 115](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile115.png>)

|| uI||Ls || uI′||Ls (3.6)

for some 3/2 ≤ s < 2. In conclusion, from identity (3.4), Lemma 3.9, and estimates (3.5) and (3.6) we deduce that for any r 3/2

3 x

|Dx|1/6e−t∂

u

3

L6t,x

||ΨIΨI′||L3/32

C

t,x

I∼I′

||ΨIΨI′||3L/32−r

C sup

t,x

I∼I′

1 6

|c(I)|−

C sup

![image 116](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile116.png>)

I∈D

|I|−

||ΨIΨI′||rL3t,x

I∼I′

(2−23q)(

2−r)

3

![image 117](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile117.png>)

![image 118](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile118.png>)

- 1

![image 119](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile119.png>)

- 2


||ΨI||L∞t,x

||u||

2q 3

(

![image 120](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile120.png>)

L2

2−r)

3

![image 121](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile121.png>)

I∈D

2 s

|I|1−

![image 122](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile122.png>)

|| uI||2Ls

r

.

We now use [20, Lem. A.3] (which is itself extracted from [52, App. A]) with the choices ν = 2r/s and µ = 2/s and obtain that for r > 1,

r

2 s

|| uI||2Ls

C ||u||2Lr2 . This completes the proof of Theorem 3.

|I|1−

![image 123](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile123.png>)

I∈D

It thus remains to provide the

Proof of Lemma 3.9. Let us explain the strategy of the proof before giving the details. First, without loss of generality, we may assume that supp u ⊂ R+, so that any dyadic interval appearing in the following may be assumed to be included in R+. We will associate to any interval J ⊂ R+ a parallelogram R(J) ⊂ R2 such that

supp Ft,x [ΨIΨI′] ⊂ R(I + I′) , (3.7)

where Ft,x denotes the space-time Fourier transform. We then deﬁne for a parallelogram R(J) and a number α > 0 an enlarged parallelogram (1 + α)R(J). The main point of the proof will be to show that there is a ﬁnite, universal constant such that for any pair (I, I′) with I ∼ I′ the number of pairs ( I, I′) with I ∼ I′ and

(1 + α)R(I + I′) ∩ (1 + α)R( I + I′) = ∅ (3.8)

is bounded by this constant. Once this is shown the conclusion of the lemma follows from [33, Lem. A.9].

Let us now carry out the details of this argument. We clearly have

suppFt,x [ΨIΨI′] ⊂ {(η3 + η′3, η + η′), η ∈ I, η′ ∈ I′}, and we will include this last set into a parallelogram in the following fashion. Let (ω, ξ) ∈ R2 with ω = η3 + η′3, ξ = η + η′ for some η ∈ I, η′ ∈ I′. Deﬁne c = c(I + I′) > 0. A quick computation shows that

- 3

![image 124](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile124.png>)

- 4


1 4

ξ(η − η′)2, which we combine with the identity

ξ3 =

ω −

![image 125](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile125.png>)

ξ3 = (ξ − c)3 + 3(ξ − c)2c + 3(ξ − c)c2 + c3 to infer that

1 4

- 3

![image 126](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile126.png>)

- 4


1 4

3 4

(ξ − c)c2 −

c3 =

ξ(η − η′)2 +

(ξ − c)2(ξ + 2c).

ω −

![image 127](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile127.png>)

![image 128](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile128.png>)

![image 129](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile129.png>)

Using Lemma 3.6, we deduce that

ω − 43(ξ − c)c2 − 41c3 c|I|2

12 5

292 5

![image 130](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile130.png>)

![image 131](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile131.png>)

, which means that we have the inclusion (3.7) with the parallelogram R(J) = (ω, ξ) : ξ ∈ J,

![image 132](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile132.png>)

![image 133](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile133.png>)

![image 134](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile134.png>)

ω − 43(ξ − c(J))c(J)2 − 14c(J)3 c(J)|J|2

73 5

3 5

![image 135](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile135.png>)

![image 136](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile136.png>)

.

![image 137](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile137.png>)

![image 138](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile138.png>)

![image 139](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile139.png>)

Let α > 0 and deﬁne (1+ α)R(J) to be the (1 + α)-dilate of the parallelogram R(J), that is, the parallelogram with the same center as R(J) but whose linear part is multiplied by 1 + α. An elementary computation shows that

ω − 34(ξ − c(J))c(J)2 − 41c(J)3 c(J)|J|2

73 5

3 5 − 7α

![image 140](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile140.png>)

![image 141](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile141.png>)

(1+α)R(J) = (ω, ξ) : ξ ∈ (1 + α)J,

+ 7α

![image 142](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile142.png>)

![image 143](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile143.png>)

![image 144](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile144.png>)

where (1+α)J denotes the interval with the same center as J but with 1+α times its length. We shall now show the universal bound on the number of pairs ( I, I′) with I ∼ I′ satisfying (3.8) for some given pair (I, I′) with I ∼ I′. Let us note J = I + I′ and J = I + I′, and let (ω, ξ) ∈ (1+α)R(J)∩(1+α)R( J). By the same reasoning as in the proof of Lemma 3.6-(3), we have 4−5αc ξ 6+5αc, where c denotes either c(J) or c( J). In particular, we have

![image 145](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile145.png>)

![image 146](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile146.png>)

4 − α 6 + α

6 + α 4 − α

c(J). (3.9) Next, from the relation

c(J) c( J)

![image 147](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile147.png>)

![image 148](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile148.png>)

−3(ξ − c)c2 − c3 + ξ3 = (ξ − c)2(ξ + 2c), we deduce that

1 4

- 3

![image 149](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile149.png>)

- 4


1 4

1 4

ξ3 = ω −

(ξ − c)c2 −

c3 −

(ξ − c)2(ξ + 2c),

ω −

![image 150](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile150.png>)

![image 151](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile151.png>)

![image 152](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile152.png>)

again with c = c(J) or c = c( J). In particular, 2 5 −

561 80

1 4

α cL2 ω −

ξ3

![image 153](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile153.png>)

![image 154](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile154.png>)

![image 155](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile155.png>)

73 5

+ 7α cL2,

![image 156](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile156.png>)

where (c, L) = (c(J), |J|) or (c, L) = (c( J), | J|). Choosing α > 0 small enough such that α < 4, 35 − 7α > 0, and 52 − 56180 α > 0, we deduce that there exist universal numbers a, b > 0 such that a|J| | J| b|J|. This relation together with (3.9) can be satisﬁed only for a universal, ﬁnite number of pairs ( I, I′) with I ∼ I′.

![image 157](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile157.png>)

![image 158](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile158.png>)

![image 159](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile159.png>)

4. Approximate operators

In this section, we provide some properties of the Airy–Strichartz map for functions that concentrate around a frequency. Deﬁne the family of operators for any q 2 and δ ∈ R,

1 √2π R |1 + δξ|1/peixξ+it(3ξ

2+δξ3) u(ξ) dξ.

(Tp,δu)(t, x) =

![image 160](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile160.png>)

![image 161](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile161.png>)

- 4.1. Basic estimates.


- Lemma 4.1. Let p > 4 and q such that 2/p + 1/q = 1/2.


(1) There exists C > 0 such that for any δ ∈ R we have

||Tp,δ||L2x(R)→LptLqx(R×R) C

(2) For any u ∈ L2(R) we have

2 x

Tp,δu → e−3it∂

u as δ → 0, strongly in LptLqx(R × R).

Proof. The ﬁrst item follows from the Airy–Strichartz inequality (1.2) by undoing the scaling as in the proof of Lemma 2.4, which shows that

3 x

||Tp,δ||L2x(R)→LptLqx(R×R) = |Dx|1/pe−t∂

.

L2x(R)→Lpt Lqx(R×R)

For the second item, using the ﬁrst item it is enough to prove it for u such that u ∈ C0∞(R). As in [20, Proof of Prop. 4.1], it is enough to prove the pointwise estimate

|Tp,δu(t, x)| C(t2 + x2)−1/4,

for some C > 0 independent of δ and for δ small enough (both depending on u though). We may write

Tp,δu(t, x) =

eiλΦ(ξ)a(ξ) dξ

R

with λ = (t2 + x2)1/2, Φ(ξ) = ω1ξ + ω2(3ξ2 + δξ3), (ω1, ω2) = (x/λ, t/λ) ∈ S2, a(ξ) = |1+δξ|1/p u(ξ). We apply stationary phase estimates. Let R > 0 such that supp u ⊂ [−R, R]. If δ 1/(2R), the function a is C∞ on R with all its derivatives uniformly bounded in δ. We have

Φ′(ξ) = ω1 + ω2(6ξ + 3δξ2). Assume |ω2| b, then

√

|Φ′(ξ)|

![image 162](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile162.png>)

1 − b2 − CbR,

so that for b = b(R) > 0 small enough, we have |Φ′(ξ)| 1/2. Furthermore, all higher derivatives of Φ are uniformly bounded in δ due to the ξ-localization. Hence, by integration by parts, we get the desired estimate (and even much faster decay) in the region |ω2| b. Let us now consider the case |ω2| > b. In this case, Φ′ has at most 3 critical points, but

Φ′′(ξ) = 6ω2(1 + δξ)

so that |Φ′′(ξ)| 3b, in which case we may apply stationary phase results (again, all higher order derivatives of Φ are uniformly bounded in δ). This concludes the proof of the second item.

- 4.2. Local smoothing. The following result in crucial in order to establish the a.e. con-


vergence (proven in the next subsection) that is used in order to split the LptLqx-norm in the proof of Theorem 2. Interestingly, it needs some assumption about the Fourier support, which is reminiscent of the ‘resonance’ between positive and negative frequencies that is responsible for the presence of the constant ap.

- Lemma 4.2. Let p > 0. For any a ∈ L1(R), there exists C > 0 such that for any δ ∈ R and any u ∈ L2(R) with Fourier transform supported in {1 + δξ 0} we have


a(x) |fδ(−iDx)Tp,δu(t, x)|2 dxdt C ||u||2L2 , where

R R

fδ(ξ) := |ξ|1/2 |1 + δξ|1/p

. Proof. In Fourier variables, the integral can be written as

![image 163](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile163.png>)

![image 164](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile164.png>)

a(ξ′ − ξ)fδ(ξ)fδ(ξ′)|1 + δξ|1/p|1 + δξ′|1/p u(ξ) u(ξ′)δ(3ξ2 + δξ3 − 3ξ′2 − δξ′3) dξ dξ′. As in the proof of Lemma 4.4 in [20], Schur’s test implies that it is enough to bound

R R

sup

ξ: 1+δξ 0 δ∈R

| a(ξ′ − ξ)|fδ(ξ)fδ(ξ′)|1 + δξ|1/p|1 + δξ′|1/pδ(3ξ2 + δξ3 − 3ξ′2 − δξ′3) dξ′

R

|1 + δξ|1/pfδ(ξ)|1 + δξ′|1/pfδ(ξ′) |ξ′||1 + δξ′/2|

|| a||L∞ sup

max

![image 165](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile165.png>)

ξ′ =0: 1+δξ′ 0 3ξ′2+δξ′3=3ξ2+δξ3

ξ: 1+δξ 0 δ∈R

|ξ|1/2 |ξ′|1/2|1 + δξ′/2|

= || a||L∞ sup

max

.

![image 166](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile166.png>)

ξ′ =0: 1+δξ′ 0 3ξ′2+δξ′3=3ξ2+δξ3

ξ: 1+δξ 0 δ∈R

Here, the max is due to the fact that the equation 3ξ′2 + δξ′3 = c may have several (at most three) solutions. Because of the constraint δξ′ −1, we have 1 + δξ′/2 1/2, hence we only have to care about the quotient (|ξ|/|ξ′|)1/2. When δ = 0, the sup is clearly 1. When δ = 0, deﬁning η = δξ −1 and η′ = δξ′ −1, we see that the sup is independent of δ and we have to show that

|η| |η′|

< ∞.

sup

![image 167](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile167.png>)

η,η′: η,η′ −1η′ =0 3η′2+η′3=3η2+η3

Deﬁning g(x) = 3x2 + x3, it is elementary to show that g−1([0, 2]) ∩ [−1, +∞) = [−1, a] for some a ∈ (1/2, 1), and that g is increasing on (a, ∞); so that in the previous sup we may assume η ∈ [−1, a], and η = 0 since η′ = 0. For all η ∈ [−1, a] \ {0}, we have g−1({g(η)}) = {η, yη} with ηyη < 0. Thus, the above supremum equals

max 1, |η| |yη|

sup

.

![image 168](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile168.png>)

η∈[−1,a]\{0}

In the case η > 0, since g is decreasing on [−1, 0] and g(−η) = 3η2 − η3 < 3η2 + η3 = g(η), we deduce yη < −η, thus |yη| > |η|. In the case η < 0, we have g(−η/2) = (3/4)η2 −

(1/8)η3 < 3η2 + η3 = g(η) since η −1 and hence we have yη −η/2 which also implies |η′| (1/2)|η|.

- 4.3. Local convergence. Here is the almost everywhere convergence result that we used in the proof of Theorem 2 in order to apply the generalized Br´ezis–Lieb lemma. Again, the Fourier support condition is crucial.


- Lemma 4.3. Let p 2. Let δn → 0 and (un) ⊂ L2(R) a sequence converging weakly to


zero in L2(R), whose Fourier transform is supported in {1 + δnξ 0}. Then Tp,δ

un → 0 in

n

L2loc,t,x(R × R), and hence almost everywhere on R × R up to a subsequence. Proof. Let K ⊂ R × R a bounded set and a > 0 a Schwartz function. We have

PΛ⊥un,

PΛun + 1KTp,δ

un = 1KTp,δ

1KTp,δ

n

n

n

where PΛ is the Fourier multiplier by 1{|ξ| Λ} for some Λ > 0 and PΛ⊥ = 1−PΛ. We estimate the second term with the local smoothing estimate of Lemma 4.2:

PΛ⊥un L

(−iDx)−1PΛ⊥ L

(−iDx)||L2x→L2t,x fδ

1/a||aTp,δ

x→L2x ||un||L2x

fδ

sup

1KTp,δ

2 t,x

n

n

n

n

2

K

1/p

+ |δn| |ξ|p/2−1

1 |ξ|p/2

,

CK sup

![image 169](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile169.png>)

![image 170](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile170.png>)

|ξ| Λ

which can be made less than ε > 0, for any given ε > 0, provided that n and Λ are large enough (depending only on ε). For such a ﬁxed Λ, we now claim that 1KTp,δ

PΛun → 0 strongly in L2(R) as n → ∞. Indeed, for any (t, x) ∈ R × R,

n

2+δnξ3) un(ξ) dξ → 0 since un → 0 weakly in L2(R) and the function ξ  → |1 + δnξ|1/p1(|ξ| Λ)eixξ+it(3ξ2+δ

|1 + δnξ|1/p1(|ξ| Λ)eixξ+it(3ξ

PΛun(t, x) = 1K(t, x)

1KTp,δ

n

R

nξ3)

converges strongly in L2(R) as n → ∞ (since (δn) converges). Furthermore, we have |1KTp,δ

PΛun(t, x)| 1K(t, x)Λ(1 + |δn|Λ)1/p ||un||L2x C1K(t, x), hence the result follows by dominated convergence.

n

Appendix A. A generalized Br´ezis–Lieb lemma for mixed Lebesgue spaces

Let us review some basics. We assume that (X, dx) and (Y, dy) are measure spaces and consider a sequence (fn) of non-negative measurable functions on X × Y which converges almost everywhere to some function f. Moreover, we ﬁx an exponent r > 0. Our ﬁrst remark is that the monotone convergence theorem remains true, in the sense that, if for each n one has fn+1 ≥ fn almost everywhere, then

r

r

fn dx

f dx

lim

dy =

dy .

n→∞ Y X

Y X

To see this, we ﬁrst apply for almost every ﬁxed y ∈ Y the usual monotone convergence theorem in X to see that gn := X fn dx r converges to g := X f dx r. Indeed, by Fubini’s theorem, for a.e. y ∈ Y , fn(·, y) converges to f(·, y) a.e. on X. Then, we apply the monotone convergence theorem in Y to (gn) and we obtain the claim.

Our second remark is that Fatou’s lemma remains true, in the sense that liminf

r

r

dy ≥

fn dx

f dx

dy

n→∞ Y X

Y X

This follows, as usual, by applying the monotone convergence theorem to Fn := infm≥n fm.

Our third remark is that the dominated convergence theorem remains true, in the sense that, if fn ≤ F with Y X F r dy < ∞, then

r

r

lim

fn dx

dy =

f dx

dy .

n→∞ Y X

Y X

To see it, just apply the usual dominated convergence theorem, ﬁrst to the sequence fn(·, y) for a.e. y ∈ Y , and then to the sequence ( X fn dx)r.

In mixed Lebesgue space, we have the following version of the triangle inequality.

Lemma A.1. Let (X, dx) and (Y, dy) be measure space, let 0 < p, q < ∞, and let f, g ∈ LpxLqy(X × Y ). Then, we have

||f + g||βLp

xLqy ||f||βLp

xLqy + ||g||βLp

xLqy , where β = β(p, q) = min(p, q, 1).

Proof. Throughout the proof, we will use the inequality (a + b)r ar + br for all a, b 0, r ∈ (0, 1]. We distinguish 4 cases. First, if p, q 1, then it follows from the triangle inequality in LpxLqy. Secondly, if p < 1 q, we have

p

||f + g||pLp

||f + g||pLq

||f||pLq

+ ||g||pLq

||f||Lqy + ||g||Lqy

xLqy =

dx

dx

dx. Thirdly, if q < 1 and p q, then

y

y

y

X

X

X

||f + g||qLp

xLqy =

|f + g|q dy

Y

|f|q dy +

Lp/qx Y

|g|q dy

Y

Lp/qx

Finally, if q < 1 and p < q, then

|f|q dy

Y

+

Lp/qx

|g|q dy

Y

.

Lp/qx

||f + g||pLp

xLqy =

|f + g|q dy

X Y

p/q

p/q

|f|q dy +

|f|q dy

dx

dx

X Y

Y

p/q

|f|q dy

|g|q dy

dx +

X Y

X Y

p/q

dx.

After these preliminaries, we can state and prove the one-sided analogue of the Br´ezis– Lieb lemma, which is originally due to [35, 6]. In [20, Lem. 3.1] we have obtained a two-fold generalization of this lemma, namely, we allow the leading term to depend on n and we allow for a remainder that converges strongly to zero. The following proposition is a generalization

of this generalization to the case of mixed Lebesgue spaces. We emphasize that instead of equality we only have an asymptotic inequality.

Proposition A.2. Let (X, dx) and (Y, dy) be measure spaces and (fn) be a sequence of measurable functions on X × Y , and let 0 < p, q < ∞. Assume that

p/q

|fn|q dy

dx < ∞ , and that fn may be split as

sup

n X Y

fn = πn + ρn + σn with |πn| Π for some Π ∈ LpxLqy(X × Y ), ρn → 0 a.e. in (x, y) ∈ X × Y , and σn → 0 in LpxLqy(X × Y ). Then, as n → ∞,

||fn||αLpxLqy ||πn||αLpxLqy + ||ρn||αLpxLqy + o(1), where α = α(p, q) = min(p, q). Proof. We ﬁrst show that we may get rid of σn, that is,

||fn||LpxLqy = ||πn + ρn||LpxLqy + on→∞(1). (A.1) This follows from Lemma A.1, which implies that with β = min(α, 1),

xLqy ||σn||βLp

||fn||βLp

xLqy − ||πn + ρn||βLp

xLqy = on→∞(1) . For α 1 this immediately gives (A.1) and for α < 1 we use in addition the boundedness of fn Lp

xLqy to deduce (A.1). Next, we shall show that

||πn + ρn|q − |πn|q − |ρn|q|dy

X Y

p/q

dx = on→∞(1) . (A.2)

Let us ﬁrst argue that this implies the conclusion. When p q, we use the elementary inequality

Aθ Bθ + Cθ + |A − B − C|θ , A, B, C 0 , 0 < θ 1 , with θ = p/q and A = Y |πn + ρn|q dy, B = Y |πn|q dy and C = Y |ρn|q dy. Then

p/q

|A − B − C|θ dx ≤

||πn + ρn|q − |πn|q − |ρn|q|dy

dx,

X

X Y

so the conclusion follows by integrating the elementary inequality with respect to x. In the other case p > q, the inequality (A.2) implies that

|πn + ρn|q dy =

Y

|πn|q dy +

Y

|ρn|q dy + oLp/q

(1),

x

Y

as n → ∞, so that the result follows from the triangle inequality in Lp/qx . Thus, it remains to prove (A.2). As in the usual Br´ezis–Lieb proof, we use the fact that for any ε > 0 there is a Cε such that for any a, b ∈ C,

||a + b|q − |b|q| ≤ ε|b|q + Cε|a|q .

Let us deﬁne

h(nε) := (||πn + ρn|q − |πn|q − |ρn|q| − ε|ρn|q)+ .

On the full measure set {Π < ∞} ∩ {ρn → 0}, h(nε) → 0 since πn(x, y) is bounded there. Hence, h(nε) → 0 almost everywhere. Since by the above inequality,

||πn + ρn|q − |πn|q − |ρn|q| ≤ ||πn + ρn|q − |ρn|q| + |πn|q ≤ ε|ρn|q + (1 + Cε)|πn|q ,

we have hn(ε) ≤ (1 + Cε)|Π|q. Thus, by the analogue of the dominated convergence theorem recalled above,

p/q

h(nε) dy

dx → 0 . (A.3)

X Y

By deﬁnition of h(nε) we have

||πn + ρn|q − |πn|q − |ρn|q| ≤ ε|ρn|q + h(nε) and therefore

p/q

p/q

||πn + ρn|q − |πn|q − |ρn|q|dy

ε|ρn|q + h(nε) dy

dx ≤

dx. In this inequality we ﬁrst take the limsup as n → ∞ and then we let ε → 0. Again by

X Y

X Y

- Lemma A.1 and (A.3), we have

X Y

ε|ρn|q + h(nε) dy

p/q

dx = εp

X Y

|ρn|qdy

p/q

dx + on→∞(1).

Since the LpxLqy-norm of fn, πn, and σn are uniformly bounded in n, the LpxLqy-norm of ρn is uniformly bounded in n by Lemma A.1. This proves (A.2).

Appendix B. A homogenization result in mixed Lebesgue spaces

The following is an extension of [1, Lem. 5.2] to mixed Lebesgue spaces. We use the convention for the torus

Tk := (R/(2πZ))k and denote by dθ normalized Lebesgue measure on Tk.

- Lemma B.1. Let r > 0, M, N ∈ N∗, and ψ : RM × RN × TM × TN → R+


a function satisfying the following assumptions: there exists a zero measure set E ⊂ RM×RN such that

- (1) For any (x1, x2) ∈/ E, (θ1, θ2)  → ψ(x1, x2, θ1, θ2) is continuous on TM × TN;
- (2) For any (θ1, θ2) ∈ TM × TN, (x1, x2)  → ψ(x1, x2, θ1, θ2) is measurable on RM × RN;
- (3)


r

sup

ψ(x1, x2, θ1, θ2) dx2

(θ1,θ2)∈TM×TN

RM RN

dx1 < ∞.

Then, we have

ψ(x1, x2, x1/ε2, x2/ε) dx2

lim

ε→0 RM RN

r

dx1

=

ψ(x1, x2, θ1, θ2) dx2 dθ2

TM RM TN RN

r

dx1 dθ1 .

Remark B.2. We state the lemma with the scale ε2 for x1 only for our application; it can be replaced by any scale of the form f(ε) with f(ε) → 0 as ε → 0.

Proof. We mimic the proof of [1, Lem. 5.2], adapting it to the context of mixed Lebesgue spaces. Notice that our assumptions imply that ψ is of Carath´eodory type [15, Def. VIII.1.2] so that with the help of Fubini’s theorem, all the integrals that we consider are well-deﬁned (the measurability is the hard part; however by [15, Prop. VIII.1.1] the function ψ coincides with a measurable function on RM × RN × TM × TN a.e. in RM × RN, which imply that all the functions we consider are measurable on the appropriate space). Let (Yi) a paving of TM by disjoint cubes of side length 1/n. We ﬁrst prove the result for the function

ψn(x1, x2, θ1, θ2) :=

i

ψ(x1, x2, yi, θ2)1Y

(θ1),

i

where (yi) are arbitrary points in Yi. We have

ψn(x1, x2, x1/ε2, x2/ε) dx2

RM RN

r

dx1

=

(x1/ε2)

1Y

i

i RM

ψ(x1, x2, yi, x2/ε) dx2

RN

Using Fubini’s theorem and [1, Lem. 5.2], we have for a.e. x1 ∈ RM that lim

ψ(x1, x2, yi, x2/ε) dx2 =

ψ(x1, x2, yi, θ2) dx2 dθ2. Furthermore, we have the uniform bound

ε→0 RN

TN RN

r

dx1.

ψ(x1, x2, yi, x2/ε) dx2

RN

r

−

ψ(x1, x2, yi, θ2) dx2 dθ2

TN RN

r

2

sup

ψ(x1, x2, θ1, θ2) dx2

(θ1,θ2)∈TM×TN

RN

r

which is integrable on RM by assumption. By Lebesgue’s dominated convergence theorem, we deduce that

ψn(x1, x2, x1/ε2, x2/ε) dx2

RM RN

r

dx1

=

(x1/ε2)

1Y

i

i RM

ψ(x1, x2, yi, θ2) dx2 dθ2

TN RN

r

dx1 + oε→0(1).

Applying [1, Lem. 5.2] to the function (x1, θ1)  → 1Y

(θ1)

i

ψ(x1, x2, yi, θ2) dx2 dθ2

TN RN

r

we obtain

r

ψn(x1, x2, x1/ε2, x2/ε) dx2

dx1

RM RN

r

=

(θ1)

ψ(x1, x2, yi, θ2) dx2 dθ2

dx1 dθ1 + oε→0(1)

1Y

i

i TM RM

TN RN

r

=

ψn(x1, x2, θ1, θ2) dx2 dθ2

dx1 dθ1 + oε→0(1) , which is the claimed formula for ψn instead of ψ.

TM RM TN RN

In the remainder of the proof we derive the formula for ψ by showing that ψn approximates ψ in a suitable topology. Indeed, as in [1, Lem. 5.2], we know that the function

|ψn(x1, x2, θ1, θ2) − ψ(x1, x2, θ1, θ2)|

δn(x1, x2) := sup

(θ1,θ2)∈TM×TN

satisﬁes δn → 0 a.e. in (x1, x2) and that 0 δn(x1, x2) g(x1, x2) with

 

g(x1, x2) := 2 sup

ψ(x1, x2, θ1, θ2),

(θ1,θ2)∈TM×TN

r



dx1 < ∞. Again by Fubini’s theorem and Lebesgue’s dominated convergence theorem, we deduce that lim

g(x1, x2) dx2

RM RN

r

δn(x1, x2) dx2

dx1 = 0. For shortness, let us introduce the notations

n→∞ RM RN

r

ψ(x1, x2, x1/ε2, x2/ε) dx2

I1,2,ε[ψ] :=

dx1,

RM RN

r

![image 171](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile171.png>)

I1,2[ψ] :=

ψ(x1, x2, θ1, θ2) dx2 dθ2

dx1 dθ1.

TM RM TN RN

![image 172](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile172.png>)

We need to show that I1,2,ε[ψ] → I1,2[ψ] as ε → 0 and, to do so, we distinguish whether r 1 or r > 1.

If r 1, we split

![image 173](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile173.png>)

![image 174](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile174.png>)

![image 175](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile175.png>)

![image 176](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile176.png>)

I1,2,ε[ψ] − I1,2[ψ] = I1,2,ε[ψ] − I1,2,ε[ψn] + I1,2,ε[ψn] − I1,2[ψn] + I1,2[ψn] − I1,2[ψ]. Using |ar − br| |a − b|r, we deduce that

|I1,2,ε[ψ] − I1,2,ε[ψn]| ||δn||rLrL1 , |I1,2[ψn] − I1,2[ψ]| ||δn||rLrL1 , so that for all α > 0, there is n large enough so that for all ε > 0,

![image 177](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile177.png>)

![image 178](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile178.png>)

![image 179](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile179.png>)

![image 180](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile180.png>)

|I1,2,ε[ψ] − I1,2[ψ]| |I1,2,ε[ψn] − I1,2[ψn]| + α. Taking the limit ε → 0, we ﬁnd the desired result.

If r > 1, we introduce the notation I2,ε[ψ](x1) :=

ψ(x1, x2, x1/ε2, x2/ε) dx2,

RN

![image 181](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile181.png>)

I2[ψ](θ1, x1) :=

ψ(x1, x2, θ1, θ2) dx2 dθ2,

TN RN

so that I1,2,ε[ψ]1/r = ||I2,ε[ψ]||Lrx1 and I1,2[ψ]1/r = I2[ψ] L

![image 182](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile182.png>)

![image 183](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile183.png>)

. We now split

r θ1,x1

I1,2,ε[ψ]1/r − I1,2[ψ]1/r = ||I2,ε[ψ]||Lrx1 − ||I2,ε[ψn]||Lrx1 + ||I2,ε[ψn]||Lrx1 − I2[ψn] L

![image 184](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile184.png>)

![image 185](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile185.png>)

r θ1,x1

![image 186](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile186.png>)

![image 187](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile187.png>)

− I2[ψ] L

+ I2[ψn] L

. We now use the estimates

r θ1,x1

r θ1,x1

||I2,ε[ψ]||Lrx1 − ||I2,ε[ψn]||Lrx1 ||I2,ε[ψ − ψn]||Lrx1 ||δn||LrL1 , I2[ψn] L

![image 188](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile188.png>)

![image 189](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile189.png>)

![image 190](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile190.png>)

− I2[ψ] L

||δn||LrL1 ,

I2[ψn − ψ] L

r θ1,x1

r θ1,x1

r θ1,x1

to deduce similarly as for r ≤ 1 that I1,2,ε[ψ]1/r → I1,2[ψ]1/r as ε → 0. This completes the proof of the lemma.

![image 191](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile191.png>)

Appendix C. A complex interpolation result Proposition C.1. Let 1 < p0, p1, q0, q1 < ∞, α0, α1 > 0 and θ ∈ (0, 1). Deﬁne

1 − θ p0

1 − θ q0

θ p1

1 qθ

θ q1

1 pθ

, αθ = θα1 + (1 − θ)α0.

=

+

,

=

+

![image 192](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile192.png>)

![image 193](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile193.png>)

![image 194](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile194.png>)

![image 195](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile195.png>)

![image 196](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile196.png>)

![image 197](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile197.png>)

Then, there exists C > 0 such that for all f : Rt × Rx → C such that the right side is well-deﬁned, we have

f||θLpt1Lqx1 |||Dx|α

f||1L−pt0θLqx0 .

|||Dx|α

f||LptθLqxθ C |||Dx|α

θ

1

0

Proof. By density, it suﬃces to prove the inequality for any f such that f ∈ C0∞(R2 \ {(t, 0), t ∈ R}), where f is the x-Fourier transform of f. By duality, it is enough to prove that there exists C > 0 such that for all g ∈ Lp′θLqθ′ we have

f||1L−p0θ

f||θLpt1Lqx1 |||Dx|α

|||Dx|α

g, |Dx|α

f C ||g||Lp′

t Lqx0 . (C.1) Hence, let g ∈ Lp′θLqθ′ . We write g as g = |g|h with |g| and h measurable, |h| 1. For z ∈ C, consider the function

θ

0

1

′ θ

θLq

1+(1−z)α0f , gz(t, x) := ||g(t, ·)||cz+d

|g(t, x)|az+bh(t, x), with the convention 0z := 0, and where the parameters a, b, c, d are chosen so that

ϕ(z) = (1 + z)−1 gz, |Dx|zα

Lqθ′

q0′ − q1′ θq0′ + (1 − θ)q1′

p′θ p′0 −

qθ′ q0′

q1′ θq0′ + (1 − θ)q1′

qθ′ q0′

d θ

, c = −

a =

, d =

. These assumptions imply the relations

, b =

=

![image 198](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile198.png>)

![image 199](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile199.png>)

![image 200](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile200.png>)

![image 201](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile201.png>)

![image 202](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile202.png>)

![image 203](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile203.png>)

p′θ p′0

p′θ p′1

qθ′ q1′

, b + d =

, a + b + c + d =

.

a + b =

![image 204](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile204.png>)

![image 205](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile205.png>)

![image 206](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile206.png>)

Let S = {λ+is, λ ∈ (0, 1), s ∈ R} a strip in the complex plane, and let us show that ϕ is analytic on S, continuous on S. For a.e. (t, x), the function z  → gz(t, x)(|Dx|zα

![image 207](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile207.png>)

1+(1−z)α0f)(t, x) is analytic on S, continuous on S by the support assumptions made on f. They also imply that there exists a T > 0 such that for any N ∈ N, there exists CN,f such that for any z = λ + is ∈ S and for any (t, x) ∈ R2 we have

![image 208](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile208.png>)

![image 209](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile209.png>)

![image 210](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile210.png>)

1+(1−z)α0f)(t, x)| CN,fe|s|1[−T,T](t)(1 + |x|)−N.

|(|Dx|zα

This can be done by integration by parts in the x-Fourier variables, the factor e|s| coming from the derivatives of |ξ|zα

1+(1−z)α2 which can be bounded by |s|M for some power M depending on N, which we choose to bound independently by e|s|. Furthermore, for any z ∈ S, the extremal values of aλ + b are b = qθ′/q0′ and a + b = qθ′/q1′ so that

![image 211](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile211.png>)

′ x1. As a consequence, we infer that for a.e. t ∈ R,

′

θ/q1′ ∈ Lq

′

θ/q0′ + |g(t, x)|q

′

x0 + Lq

|g(t, x)|aλ+b |g(t, x)|q

gz(t, x)(|Dx|zα

1+(1−z)α0f)(t, x) dx

![image 212](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile212.png>)

z  →

R

is analytic on S and continuous on S. It satisﬁes the bound for any z ∈ S and a.e. t ∈ R

![image 213](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile213.png>)

![image 214](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile214.png>)

1+(1−z)α0f)(t, x) dx CN,f1[−T,T](t)e|s| ||g(t, ·)||(a+c)λ+b+d

![image 215](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile215.png>)

gz(t, x)(|Dx|zα

.

Lqθ′

R

The extremal values of (a + c)λ + b + d are b + d = p′θ/p′0 and a + b + c + d = p′θ/p′1 so that ||g(t, ·)||(a+c)λ+b+d

′ θ/p′0

′ θ/p′1

||g(t, ·)||p

+ ||g(t, ·)||p

′ 1

′ 0

t + Lp

∈ Lp

t .

′ θ

′ θ

′ θ

Lq

Lq

Lq

![image 216](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile216.png>)

This implies that ϕ is analytic on S and continuous on S, with the bound valid for any z = λ + is ∈ S,

![image 217](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile217.png>)

|ϕ(z)| CN,fe|s| ||g||

. On the boundary of S, let us show more precise bounds. For any s ∈ R, we have

′ θ

′ θ

Lp

t Lq

x

![image 218](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile218.png>)

gis(t, x)(|Dx|α

0+is(α1−α0)f)(t, x) dx ||gis(t, ·)||

′ 0

Lq

x

R

|Dx|is(α

1−α0)|Dx|α

.

f Lq0

0

x

For any η ∈ R, the Fourier multiplier by mη(ξ) := |ξ|iη satisﬁes the bounds

|mη(ξ)| 1, |ξ||m′η(ξ)| |η|. By the Marcinkiewicz multiplier theorem [24, Thm. 5.2.2], this implies the Lp-bound for all

- p > 1:


|Dx|iηg L

C(1 + |η|) ||g||Lp , which in our case gives

p

|Dx|is(α

1−α0)|Dx|α

C(1 + |s|) |||Dx|α

f||Lqx0 . Using the bound

f Lq0

0

0

x

||g(t, ·)||b+d

||gis(t, ·)||

,

′ 0

Lq

Lqθ′

x

together with the relation b + d = p′θ/p′0, we deduce that |ϕ(is)| C ||g||

|||Dx|α

f||Lpt0Lqx0 . Here, we see the role of the prefactor (1 + z)−1 in front of ϕ(z) to compensate the growth of the Lp-multiplier norm of mη. By the same method, we have the estimate for all s ∈ R

0

′ θ

′ θ

Lp

t Lq

x

|||Dx|α

|ϕ(is)| C ||g||

f||Lpt1Lqx1

1

′ θ

′ θ

Lp

t Lq

x

using the relations a + b = qθ′/q1′ and a + b + c + d = p′θ/p′1. Using Hadamard’s three line lemma [47, Thm. 5.2.1], we deduce (C.1), which ends the proof.

Appendix D. Weak compactness of the Airy–Strichartz map

- Lemma D.1. Let α ∈ (−1/2, 1) and (un) ⊂ L2(R) a sequence converging weakly to zero in L2(R). Then, up to a subsequence, |Dx|αe−t∂x3un → 0 a.e. in R2.

The proof follows from some local smoothing properties of the Airy kernel:

- Lemma D.2. Let a ∈ L1(R) a non-negative function. Then, for all u ∈ L2(R) we have


1 3 ||a||L1 ||u||2L2 .

2

3 x

a(x) |Dx|e−t∂

dxdt

u(x)

![image 219](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile219.png>)

R2

Proof. By the Plancherel identity, we have

√

2

3 x

![image 220](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile220.png>)

![image 221](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile221.png>)

a(ξ′ − ξ)|ξ||ξ′| u(ξ) u(ξ′)δ(ξ3 − ξ′3) dξ dξ′. Using δ(ξ3 − ξ′3) = δ(ξ − ξ′)/(3ξ2), we deduce

a(x) |Dx|e−t∂

2π

dxdt =

u(x)

R2

R2

√2π 3 R2

![image 222](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile222.png>)

1 3 ||a||L1 ||u||2L2

2

3 x

a(x) |Dx|e−t∂

a(0)| u(ξ)|2 dξ

dxdt =

u(x)

![image 223](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile223.png>)

![image 224](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile224.png>)

R2

Proof of Lemma D.1. We prove that |Dx|αe−t∂x3un → 0 in L2loc(R2), which implies the result. Hence, let K ⊂ R2 a bounded set, and let us show that χK|Dx|αe−t∂x3un → 0 in L2(R2). To this end, let ε > 0 and Λ > 0. Deﬁne PΛ the Fourier multiplier on L2x(R) by 1(|ξ| Λ), and PΛ⊥ := 1−PΛ. We split χK|Dx|αe−t∂x3un = χKPΛ|Dx|αe−t∂x3un +χKPΛ⊥|Dx|αe−t∂x3un, and notice that

3

χKPΛ⊥|Dx|αe−t∂

xun

L2t,x

2

χKex

L∞t,x

2

3 x

e−x

|Dx|e−t∂

L2x→L2t,x

PΛ⊥|Dx|α−1 L2

x→L2x ||un||L2 CKΛα−1,

for some constant CK > 0 independent of n, by Lemma D.1 and the boundedness of (un) in L2(R). Hence, for Λ large enough independent of n, we have

3

χKPΛ⊥|Dx|αe−t∂

xun

L2t,x

ε.

For any ﬁxed t ∈ R, the operator χK(t, ·)PΛ|Dx|αe−t∂x3 is compact on L2x(R), hence χK(t, ·)PΛ|Dx|αe−t∂

3 x

un → 0

strongly in L2x(R) as n → ∞, by weak convergence of (un) in L2(R). Furthermore, we always have

2

- 1

![image 225](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile225.png>)

- 2


3 x

||χK(t, ·)||2L2x , with C > 0 independent of n. By Lebesgue’s dominated convergence theorem, we deduce that χKPΛ|Dx|αe−t∂x3un → 0 in L2(R2) as n → ∞, from which the result follows.

CΛα+

χK(t, ·)|Dx|αPΛe−t∂

un

L2x

Appendix E. Maximizers in the subcritical case

In the subcritical case γ < 1/p, the existence of maximizers is simpler and unconditional. Deﬁne

p/q

q

3

|Dx|γ(e−t∂

dx

xu)(x)

dt ||u||pL2

R R

Aγ,p := sup

(E.1) where q is determined by p and γ as in (1.3). Then, we can prove the following result.

![image 226](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile226.png>)

u =0

Theorem 4. Let p > 4, −1/2 < γ < 1/p, and q such that −γ + 3/p + 1/q = 1/2. Then, any maximizing sequence for Aγ,p is precompact up to symmetries and, in particular, there exists maximizers for Aγ,p.

This result with p = q = 8 is due to [25].

- Remark E.1. The same result holds for real-valued functions, with the same proof.


Proof of Theorem 4. We mimic the proof in Section 2. The analogue of Proposition 2.3 is valid, with the same proof using Lemma D.1 and the condition γ > −1/2. We now show that A∗γ,p = 0, from which the result follows. To do so, we argue by contradiction and assume A∗γ,p > 0, and let (un) a sequence such that ||un||L2 = 1, un ⇀sym 0, and

- 1

![image 227](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile227.png>)

- 2A∗γ,p.


p

3

|Dx|γe−t∂

xun

limsup

Lpt Lqx

n→∞

In particular, we have |Dx|γe−t∂x3un  → 0 in LptLqx. In the subcritical case, we have results identical to Corollary 3.1 and Corollary 3.2 by interpolating (γ, p, q) between ( γ, p, q) and (1/p, p, 2p/(p − 4)) with −1/2 < γ < γ and using Proposition C.1. Hence, there exists (gn) ⊂ G and (ηn) ⊂ R with |ηn| 1/2 such that ( gnun(· + ηn)) has a non-zero weak limit v in L2 (here, we do not need to distinguish between positive and negative frequencies), with a lower bound

||v||L2 ε > 0, where ε only depends on p, γ. Again, we must have |ηn| → ∞. Writing again δn := 1/ηn → 0 and gnun(· + ηn) = v + rn, we have

1

3 x

p−γ ||Tγ,δ

|Dx|γe−t∂

rn||LptLqx , where the approximate operator Tγ,δ is

= |δn|

v + Tγ,δ

un

![image 228](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile228.png>)

n

n

Lpt Lqx

1 √2π R |1 + δξ|γeixξ+it(3ξ

2+δξ3) u(ξ) dξ.

(Tγ,δu)(x) :=

![image 229](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile229.png>)

![image 230](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile230.png>)

As in Lemma 4.1, we have

1

||Tγ,δ||L2x→LptLqx = Cδγ−

p, and for all u ∈ L2x(R) and all γ < 1/p,

![image 231](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile231.png>)

1

p−γ ||Tγ,δu||LptLqx = 0. As a consequence, we ﬁnd that

|δ|

lim

![image 232](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile232.png>)

δ→0

1

3 x

p−γ ||Tγ,δ

|Dx|γe−t∂

= |δn|

rn||LptLqx + on→∞(1), and undoing the change of variables shows that

un

![image 233](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile233.png>)

n

Lpt Lqx

p

p

3 x

3 x

|Dx|γe−t∂

= |Dx|γe−t∂

un

wn

+ on→∞(1), (E.2)

Lpt Lqx

Lpt Lqx

where wn = rn(·−ηn). By weak convergence of rn to zero, we know that ||rn||2L2 → 1−||v||2L2. Hence, as in the proof of Theorem 2, we have wn ⇀sym 0 and

p

3

A∗γ,p(1 − ||v||2L2)p/2, which we insert in (E.2) to obtain limsup n→∞

|Dx|γe−t∂

xwn

limsup

Lpt Lqx

n→∞

p

A∗γ,p(1 − ||v||2L2)p/2 A∗γ,p(1 − ε2)p/2. Taking the supremum over all such sequences (un), we ﬁnd

3 x

|Dx|γe−t∂

un

Lpt Lqx

A∗γ,p A∗γ,p(1 − ε2)p/2 < A∗γ,p, leading to a contradiction. We thus have A∗γ,p = 0, which ﬁnishes the proof. Appendix F. Symmetries for extension problems

In this section we show that the argument provided in Lemma 2.8 about real-valuedness of maximizers extends to a more general setting. A similar remark was made independently in [8]. If N 1, S ⊂ RN, σ is a Borel measure on S, and f ∈ L1(S, σ), we deﬁne its Fourier transform as

∀x ∈ RN, fˇ(x) :=

eix·ωf(ω) dσ(ω).

S

Previously, we considered the case N = 2, S = {(ξ, ξ3), ξ ∈ R} the cubic curve and the measure σ being the push-forward of the measure |ξ|γdξ through the map ξ ∈ R  → (ξ, ξ3) ∈ S. Notice that in the optimization problem (1.4), the L2-norm is taken with respect to another measure on S than σ. As a consequence, let σ′ be another Borel measure on S, and

- q 2. Deﬁne


f ˇ L

q(RN)

M(S, σ, σ′, q) := sup

, f ∈ L1(S, σ) ∩ L2(S, σ′) \ {0}

![image 234](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile234.png>)

||f||L2(S,σ′)

and, under the symmetry assumption S = −S, also its ‘symmetric’ version

f ˇ L

q(RN)

![image 235](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile235.png>)

, f ∈ L1(S, σ) ∩ L2(S, σ′) \ {0}, f(ω) = f(−ω) a.e. on S .

Msym(S, σ, σ′, q) := sup

![image 236](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile236.png>)

||f||L2(S,σ′)

We then have the following statement.

Lemma F.1. Let N 1, S ⊂ RN and σ, σ′ Borel measures on S. Assume that (S, σ) and (S, σ′) are symmetric with respect to the origin, that is, S = −S and σ(A) = σ(−A), σ′(A) = σ′(−A) for all A Borel subset of S. Then, for any q 2, we have

M(S, σ, σ′, q) = Msym(S, σ, σ′, q). Moreover, there is an optimizer for M(S, σ, σ′, q) if and only if there is one for Msym(S, σ, σ′, q).

We emphasize that in the deﬁnition of M(S, σ, σ′, q) and Msym(S, σ, σ′, q) we impose the condition f ∈ L1(S, σ) only in order to have fˇ a priori well-deﬁned. Once it is shown that M(S, σ, σ′, q) < ∞ it follows that fˇ ∈ Lq(RN) for any f ∈ L2(S, σ′) and the condition f ∈ L1(S, σ) can be dropped. In particular, for an optimizer for M(S, σ, σ′, q) or Msym(S, σ, σ′, q) we do not require this condition.

- Remark F.2. This result applies to S = SN−1 and σ = σ′ is the standard surface measure on SN−1, which is the case of the Stein–Tomas theorem.


Proof. Since the inequality is trivial, let us prove the inequality . Let f ∈ L1(S, σ) ∩ L2(S, σ′), f = 0. We split f = f1 + if2 where

![image 237](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile237.png>)

![image 238](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile238.png>)

f(ω) − f(−ω) 2i

f(ω) + f(−ω) 2

, f2(ω) :=

,

f1(ω) :=

![image 239](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile239.png>)

![image 240](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile240.png>)

![image 241](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile241.png>)

![image 242](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile242.png>)

so that f1(−ω) = f1(ω) and f2(−ω) = f2(ω) for a.e. ω ∈ S. Using the symmetry of (S, σ), we deduce that fˇ1 and fˇ2 are real-valued, so that |fˇ|2 = |fˇ1|2+|fˇ2|2 and hence by the triangle inequality in Lq/2(RN)

q(RN) = |fˇ1|2 + |fˇ2|2 1L/q/22(RN) f ˇ1 2L

f ˇ L

q(RN) + f ˇ2 2L

q(RN)

1/2

Msym(S, σ, σ′, q) ||f1||2L2(S,σ′) + ||f2||2L2(S,σ′)

1/2

.

We notice now that |f1(ω)|2 + |f2(ω)|2 = (1/2)(|f(ω)|2 + |f(−ω)|2) for all ω ∈ S, and therefore, by symmetry of S and σ′,

||f1||2L2(S,σ′) + ||f2||2L2(S,σ′) = f 2L2(S,σ′) .

By taking the supremum over all f, we therefore obtain the inequality in the lemma. Moreover, if f is an optimizer and the suprema are ﬁnite, then tracking the case of equality shows that either f1 or f2 is also a maximizer, showing the desired property.

Remark F.3. The previous proof clearly extends to mixed Lebesgue spaces (as in the case of the cubic curve), as long as the Lebesgue exponents are greater than 2.

References

- [1] G. Allaire, Homogenization and two-scale convergence, SIAM J. Math. Anal., 23 (1992), pp. 1482– 1518.
- [2] T. Aubin, e´quations diﬀe´rentielles non line´aires et proble`me de Yamabe concernant la courbure scalaire, J. Math. Pures Appl. (9), 55 (1976), pp. 269–296.
- [3] P. B´egout and A. Vargas, Mass concentration phenomena for the L2-critical nonlinear Schro¨dinger equation, Trans. Amer. Math. Soc., 359 (2007), pp. 5257–5282.
- [4] J. Bennett, N. Bez, A. Carbery, and D. Hundertmark, Heat-ﬂow monotonicity of Strichartz norms, Anal. PDE, 2 (2009), pp. 147–158.
- [5] J. Bourgain, Reﬁnements of Strichartz’ inequality and applications to 2D-NLS with critical nonlinearity, Internat. Math. Res. Notices, (1998), pp. 253–283.
- [6] H. Br´ezis and E. H. Lieb, A relation between pointwise convergence of functions and convergence of functionals, Proceedings of the American Mathematical Society, 88 (1983), pp. 486–490.
- [7] H. Br´ezis and L. Nirenberg, Positive solutions of nonlinear elliptic equations involving critical Sobolev exponents, Comm. Pure Appl. Math., 36 (1983), pp. 437–477.
- [8] G. Brocchi, D. Oliveira e Silva, and R. Quilodran´ , Sharp Strichartz inequalities for fractional and higher order Schro¨dinger equations.
- [9] R. Carles and S. Keraani, On the role of quadratic oscillations in nonlinear Schro¨dinger equations. II. The L2-critical case, Trans. Amer. Math. Soc., 359 (2007), pp. 33–62 (electronic).
- [10] E. Carneiro, A sharp inequality for the Strichartz norm, Int. Math. Res. Not. IMRN, (2009), pp. 3127– 3145.
- [11] E. Carneiro, D. Foschi, D. Oliveria e Silva, and C. Thiele, A sharp trilinear inequality related to fourier restriction on the circle, Rev. Mat. Iberoam., 33 (2017), pp. 1463–1486.
- [12] E. Carneiro, D. Oliveira e Silva, and M. Sousa, Extremizers for Fourier restriction on hyperboloids, arXiv preprint arXiv:1708.03826, (2017).
- [13] M. Christ, J. Colliander, and T. Tao, Asymptotics, frequency modulation, and low regularity ill-posedness for canonical defocusing equations, Amer. J. Math., 125 (2003), pp. 1235–1293.
- [14] M. Christ and S. Shao, Existence of extremals for a Fourier restriction inequality, Anal. PDE, 5

(2012), pp. 261–312.

- [15] I. Ekeland and R. T´emam, Convex analysis and variational problems, vol. 28 of Classics in Applied Mathematics, Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA, english ed.,

1999. Translated from the French.

- [16] D. Foschi, Maximizers for the Strichartz inequality, J. Eur. Math. Soc. (JEMS), 9 (2007), pp. 739–774.
- [17] , Global maximizers for the sphere adjoint Fourier restriction inequality, J. Funct. Anal., 268

![image 243](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile243.png>)

(2015), pp. 690–702.

- [18] R. L. Frank and E. H. Lieb, Sharp constants in several inequalities on the Heisenberg group, Ann. of Math. (2), 176 (2012), pp. 349–381.
- [19] , A compactness lemma and its application to the existence of minimizers for the liquid drop model, SIAM J. Math. Anal., 47 (2015), pp. 4436–4450.

![image 244](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile244.png>)

- [20] R. L. Frank, E. H. Lieb, and J. Sabin, Maximizers for the Stein-Tomas inequality, Geom. Funct. Anal., 26 (2016), pp. 1095–1134.
- [21] P. G´erard, Y. Meyer, and F. Oru, Ine´galite´s de Sobolev pre´cise´es, in S´eminaire sur les Equations´ aux D´eriv´ees Partielles, 1996–1997, Ecole´ Polytech., Palaiseau, 1997, pp. Exp. No. IV, 11.
- [22] J. Ginibre and G. Velo, On a class of nonlinear schr¨odinger equations. i. the cauchy problem, general case, Journal of Functional Analysis, 32 (1979), pp. 1–32.
- [23] F. Gon¸calves, Orthogonal polynomials and sharp estimates for the schr¨odinger equation, International Mathematics Research Notices, (2017).


- [24] L. Grafakos, Classical Fourier analysis, vol. 249 of Graduate Texts in Mathematics, Springer, New York, second ed., 2008.
- [25] D. Hundertmark and S. Shao, Analyticity of extremizers to the Airy-Strichartz inequality, Bull. Lond. Math. Soc., 44 (2012), pp. 336–352.
- [26] D. Hundertmark and V. Zharnitsky, On sharp Strichartz inequalities in low dimensions, Int. Math. Res. Not., (2006), pp. Art. ID 34080, 18.
- [27] J. Jiang, S. Shao, and B. Stovall, Linear proﬁle decompositions for a family of fourth order Schro¨dinger equations, arXiv preprint arXiv:1410.7520, (2014).
- [28] J.-C. Jiang, B. Pausader, and S. Shao, The linear proﬁle decomposition for the fourth order Schro¨dinger equation, J. Diﬀerential Equations, 249 (2010), pp. 2521–2547.
- [29] M. Keel and T. Tao, Endpoint Strichartz estimates, Amer. J. Math., 120 (1998), pp. 955–980.
- [30] C. E. Kenig, G. Ponce, and L. Vega, Oscillatory integrals and regularity of dispersive equations, Indiana Univ. Math. J., 40 (1991), pp. 33–69.
- [31] , On the concentration of blow up solutions for the generalized KdV equation critical in L2, in Nonlinear wave equations (Providence, RI, 1998), vol. 263 of Contemp. Math., Amer. Math. Soc., Providence, RI, 2000, pp. 131–156.

![image 245](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile245.png>)

- [32] R. Killip, S. Kwon, S. Shao, and M. Visan, On the mass-critical generalized KdV equation, Discrete Contin. Dyn. Syst., 32 (2012), pp. 191–221.
- [33] R. Killip and M. Visan, Nonlinear Schro¨dinger equations at critical regularity, Evolution equations, 17 (2013), pp. 325–437.
- [34] M. Kunze, On the existence of a maximizer for the Strichartz inequality, Commun. Math. Phys., 243

(2003), pp. 137–162.

- [35] E. H. Lieb, Sharp constants in the Hardy–Littlewood–Sobolev and related inequalities, Ann. Math., 118

(1983), pp. 349–374.

- [36] E. H. Lieb and M. Loss, Analysis, vol. 14 of Graduate Studies in Mathematics, American Mathematical Society, Providence, RI, second ed., 2001.
- [37] P.-L. Lions, The concentration-compactness principle in the calculus of variations. The locally compact case, Part I, Ann. Inst. Henri Poincar´e, 1 (1984), pp. 109–149.
- [38] F. Merle and L. Vega, Compactness at blow-up time for L2 solutions of the critical nonlinear Schro¨dinger equation in 2D, Internat. Math. Res. Notices, (1998), pp. 399–425.
- [39] A. Moyua, A. Vargas, and L. Vega, Restriction theorems and maximal operators related to oscillatory integrals in R3, Duke Math. J., 96 (1999), pp. 547–574.
- [40] D. Oliveira e Silva, Extremizers for Fourier restriction inequalities: convex arcs, J. Anal. Math., 124 (2014), pp. 337–385.
- [41] R. Quilodran´ , On extremizing sequences for the adjoint restriction inequality on the cone, J. Lond. Math. Soc. (2), 87 (2013), pp. 223–246.
- [42] , Nonexistence of extremals for the adjoint restriction inequality on the hyperboloid, J. Anal. Math., 125 (2015), pp. 37–70.

![image 246](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile246.png>)

- [43] R. Quilodran´ and D. Oliveira e Silva, On extremizers for Strichartz estimates for higher order Schro¨dinger equations, arXiv preprint arXiv:1606.02623, (2016).
- [44] S. Shao, The linear proﬁle decomposition for the Airy equation and the existence of maximizers for the Airy Strichartz inequality, Anal. PDE, 2 (2009), pp. 83–117.
- [45] , Maximizers for the Strichartz inequalities and the Sobolev-Strichartz inequalities for the Schro¨dinger equation, Electronic J. of Diﬀerential Equations, (2009), pp. 1–13.

![image 247](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile247.png>)

- [46] , On existence of extremizers for the Tomas-Stein inequality for S1, J. Funct. Anal., 270 (2016), pp. 3996–4038.

![image 248](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile248.png>)

- [47] B. Simon, Basic complex analysis, A Comprehensive Course in Analysis, Part 2A, American Mathematical Society, Providence, RI, 2015.


- [48] E. M. Stein, Oscillatory integrals in Fourier analysis, in Beijing lectures in harmonic analysis (Beijing, 1984), vol. 112 of Ann. of Math. Stud., Princeton Univ. Press, Princeton, NJ, 1986, pp. 307–355.
- [49] R. Strichartz, Restrictions of Fourier transforms to quadratic surfaces and decay of solutions of wave equations, Duke Math. J., 44 (1977), pp. 705–714.
- [50] T. Tao, A sharp bilinear restriction estimate for paraboloids, Geom. Funct. Anal., 13 (2003), pp. 1359– 1384.
- [51] , Two remarks on the generalised Korteweg-de Vries equation, Discrete Contin. Dyn. Syst., 18

![image 249](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile249.png>)

(2007), pp. 1–14.

- [52] , A pseudoconformal compactiﬁcation of the nonlinear Schro¨dinger equation and applications, New York J. Math., 15 (2009), pp. 265–282.

![image 250](<2017-frank-extremizers-airy-strichartz-inequality_images/imageFile250.png>)

- [53] P. A. Tomas, A restriction theorem for the Fourier transform, Bull. Amer. Math. Soc., 81 (1975), pp. 477–478.


(R. Frank) Mathematisches Institut, Ludwig-Maximilans Universitat¨ Munchen,¨ Theresienstr. 39, 80333 Munchen,¨ Germany, and Department of Mathematics, California Institute of Technology, Pasadena, CA 91125, USA

E-mail address: r.frank@lmu.de (J. Sabin) Laboratoire de Math´ematiques d’Orsay, Universit´e Paris-Sud, CNRS, Universit´e

Paris-Saclay, 91405 Orsay, France E-mail address: Julien.Sabin@math.u-psud.fr

