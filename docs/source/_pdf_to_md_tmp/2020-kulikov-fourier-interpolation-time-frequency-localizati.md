# arXiv:2005.12836v1[math.CA]26May2020

## FOURIER INTERPOLATION AND TIME-FREQUENCY LOCALIZATION

ALEKSEI KULIKOV

Abstract. We prove that under very mild conditions for any interpolation formula f(x) = λ∈Λ f(λ)aλ(x) + µ∈M fˆ(µ)bµ(x) we have a lower bound for the counting functions nΛ(R1) + nM(R2) ≥ 4R1R2 − C log2+ε(4R1R2) which very closely matches interpolation formulas from [8], [3].

1. Introduction

In the recent breakthrough paper [8] Radchenko and Viazovska showed that any Schwartz function can be eﬀectively reconstructed from the values of it and its Fourier transform at the points ±

√n,n ∈ Z≥0 and two more values f (0), fˆ (0). If we consider the counting function nΛ(R) = |Λ ∩ [−R,R]|, which in the case Λ = {±

√n} takes the form nΛ(R) = 1+2[R2], we see that it satisﬁes the inequality nΛ(W)+nΛ(T) ≥ 4WT −O(1) for all W,T. We observe that this bound perfectly matches the famous 4WT Theorem of Slepian [12] which says that the space of functions which are supported on [−T,T] and such that their Fourier transforms are essentially supported on [−W,W] has approximate dimension 4WT.1 We prove that this is not a coincidence and that a similar inequality holds for all such interpolation formulas with a very small error term.

Theorem 1.1. Let Λ,M ⊂ R be two multisets and L be some ﬁxed number. Assume that the following interpolation formula holds for all C∞ compactly supported functions f

- (1.1) f(x) =

λ∈Λ

f(r(λ))(λ)aλ(x) +

µ∈M

fˆ(k(µ))(µ)bµ(x),

where r : Λ → Z≥0,k : M → Z≥0 and aλ,bµ : R → C,λ ∈ Λ,µ ∈ M. Assume additionally that k is at most L, the counting function of M satisﬁes the bound nM(R) ≤ RL for large enough R and that bµ(x) is polynomially bounded in µ and x. Then for any ε > 0 there exists C > 0 (depending on ε and the interpolation formula) such that for all R1,R2 > 1

- (1.2) nΛ(R1) + nM(R2) ≥ 4R1R2 − C log2+ε(4R1R2).


1Slepian called it the 2WT Theorem since he considered intervals [−W,W] and [−T/2,T/2] which is more natural from the engineering point of view.

1

This result reﬂects the idea that for a function from Slepian’s theorem values of this function and its Fourier transform outside of the corresponding intervals are mostly irrelevant and to generate an N-dimensional vector space we need at least N vectors (although the “space” under consideration is by no means a vector space).

The way to make the 4WT Theorem of Slepian precise is to consider the so-called prolate spheroidal wave functions, studied by Slepian, Landau and Pollak [13], [11], [7]. These functions are the eigenvectors of the time-frequency localization operator corresponding to the intervals [−W,W] and [−T,T]. The key ingredient in our proof is the sharp estimate for the corresponding eigenvalues obtained by Israel [6]. However, while we can prove

- Theorem 1.1 using the prolate spheroidal wave functions, it is much more natural for us to use directly the basis functions constructed in [6] because of the decay of their Fourier transforms.

Let us emphasize that for this theorem it is not enough to assume only uniqueness i.e. that any function which vanishes on Λ and whose Fourier transform vanishes on M is zero. We need some quantitative assumption like an interpolation formula or frame property. To illustrate this, let us mention a well-known result of Ascensi, Lyubarskii and Seip [1], which gives us a uniqueness result (but not an interpolation formula) with eﬀectively half the number of points.

- Theorem 1.2 (Ascensi, Lyubarskii, Seip). Let f ∈ L2(R). Assume that it is orthogonal


√2n} and M = {±

to the functions exp(−π(t + λ)2),λ ∈ Λ and exp(−πt2 + 2πiµt),µ ∈ M with Λ = {±

√2n} ∪ {−1,1}. Then this function is identically zero.

If we think of a gaussian as a smoothed version of the δ-function used in formula (1.1) then this result gives us a uniqueness set with half as many points as claimed in the

- Theorem 1.1. Nevertheless there is no contradiction between Theorem 1.1 and Theorem 1.2 because there is no eﬃcient way to reconstruct a function f from its scalar products with the functions from the Theorem 1.2.


The usual way to express eﬀective reconstruction is by imposing the frame property. Recall that the set of vectors {vk} in the Hilbert space H is said to be a frame if for all f ∈ H we have ||f||2 ∼ k | f,vk |2. In this language we can say that the set of functions from Theorem 1.2 is extremely far from being a frame (even if we only care about a lower bound for ||f||2 and put a fairly large weight on | f,vk |2), which can be deduced from the (proof of the) general result of Seip [9] or seen directly by considering the functions fN(t) = exp(−π(t + N)2 + 2πiNt),N → ∞. Theorem 1.1 shows that a density condition akin to that of [9] holds under a much weaker assumption about reconstruction than what follows from the frame property.

Let us also mention a recent interpolation formula of Bondarenko, Radchenko and Seip [3]. They proved that, under suitable conditions, one can recover the value fˆ(x) by means of an interpolation formula from the values of f at the points ±log(4π n) and the values of fˆ at the points ρ−i1/2 with ρ ranging over the nontrivial zeros of the Riemann zeta function. Although in the absence of the Riemann hypothesis these points can be non-real and the formula from [3] converges only after some grouping of terms, one can still apply our techniques to their setting and get the bound

- (1.3) 2N(T) + 2e4πW ≥ 4WT − C log2+ε(WT), where N(T) is the number of zeros ρ of the Riemann zeta function with 0 < (ρ) < T. Choosing W = 41π log(2Tπ) we get the lower bound which matches the Riemann-von Mangoldt formula up to the power of the logarithmic term

- (1.4) N(T) ≥


T 2πe − C log2+ε(T).

T 2π

log

Finally let us remark that our result admits a natural generalization to the space of even/odd functions with 4WT replaced by 2WT. This result also perfectly matches interpolation formulas from [8] and [3].

2. Local cosine basis

A local cosine basis is an orthonormal basis of L2(I) associated with the Whitney decomposition of I that was introduced by Coifman and Meyer in [5] as a tool for smooth localization in Fourier analysis (see also [2] for a nice exposition of this and related matters). In [6] Israel constructed local cosine basis functions which in addition have a strong decay of their Fourier transforms. We shall now list properties of this basis that we will use in our proof.

Let 0 < η < 1 be a ﬁxed real number. For D ≥ 2 let {Ij}j∈J be the Whitney de-

composition of the interval I = [−D2 , D2 ] and set δj = |Ij|. There exists an orthonormal basis {Φj,k}j∈J,k∈Z

of L2(I) with the following properties: Φj,k are C∞(R), compactly supported functions and they satisfy the following Fourier concentration inequality (inequality

≥0

(23) from [6])

- (2.1) |F(Φj,k)(ξ)| ≤ δj1/2Aη exp(−aη(δj|ξ − ξj,k|)1−η) + exp(−aη(δj|ξ + ξj,k|)1−η) ,


and Aη,aη are some positive constants.

where ξj,k = 24kδ+1

j

For our purposes we need a similar bound for the derivatives of F(Φj,k). To get them we will use the following real-analytic inequality.

- Theorem 2.1 (Landau-Kolmogorov inequality on the half-line). For any n,k ∈ N, k < n there exists a constant Cn,k > 0 such that for all f ∈ C∞([0,+∞)) we have


- (2.2) ||f(k)||L∞(0,+∞) ≤ Cn,k||f||L1−∞k/n(0,+∞)||f(n)||k/nL∞(0,+∞). For the proof and various generalizations of this inequality see e.g. [10]. Applying this theorem to the functions Φj,k we get the following corollary.

Corollary 2.2. For any n ∈ N there exist positive constants Cn,dn,sn (possibly also depending on η) such that for |ξ| > ξj,k we have

- (2.3) |F(Φj,k)(n)(ξ)| ≤ CnDd

n

exp(−sn(δj|ξ − ξj,k|)1−η) + exp(−sn(δj|ξ + ξj,k|)1−η) .

Proof. Without loss of generality we may assume that ξ > ξj,k (the other case is completely analogous). Consider the function f(x) = F(Φj,k)(x + ξ). By (2.1) we have for x ≥ 0

- (2.4) |f(x)| ≤ 2D1/2Aη exp(−aη(δj|x + ξ − ξj,k|)1−η) ≤ 2D1/2Aη exp(−aη(δj|ξ − ξj,k|)1−η),

where we used δj ≤ D and |ξ − ξj,k| ≤ |x + ξ − ξj,k| ≤ |x + ξ + ξj,k|.

On the other hand we have F(Φj,k)(m) = F((2πix)mΦj,k). Therefore by the Cauchy– Schwarz inequality we have for all t ∈ R

- (2.5) |F(Φj,k)(m)(t)| ≤ CmDm+1/2.

Since f is just a shift of F(Φj,k) the same bound holds for f as well. Choosing m = 2n and applying (2.2) to f we get

- (2.6) |f(n)(x)| ≤ C2n,nDn+1/2 2AηC2n exp(−

aη 2

(δj|ξ − ξj,k|)1−η).

Applying this for x = 0 and recalling that f(x) = F(Φj,k)(x + ξ) we get the desired inequality.

Remark 2.3. Using the methods from [6] directly instead of applying the general bound

- (2.2), we can get much better quantitative bounds for the constants Cn,dn,sn. But since it is irrelevant for our applications, we decided to follow this route to simplify the exposition.


Let us deduce another corollary from the bound (2.3) which is more convenient for our applications. Corollary 2.4. For all T1,T2,n ≥ 0 there exist constants C,c > 0 such that for k < δj − C log1/(1−η)(D) and |ξ| > 21 we have

- (2.7) |F(Φj,k)(n)(ξ)| ≤


c DT1

### .

|ξ|T

2

Proof. We consider two cases: |ξ| < D and |ξ| ≥ D. In the ﬁrst case we have by (2.3) and our assumption that |ξ| > 12

- (2.8) |F(Φj,k)(n)(ξ)| ≤ 2CnDd

n

exp(−sn(δj(

- 1

- 2 − ξj,k)1−η) .


Since ξj,k = 24kδ+1

j

and k < δj−C log1/(1−η)(D) we have δj(12−ξj,k) > C2 log1/(1−η)(D)−14 ≥

C

4 log1/(1−η)(D) for C ≥ 10. Therefore we get

- (2.9) |F(Φj,k)(n)(ξ)| ≤ 2CnDd

n−sn(

C 4

)1/(1−η). Choosing C so that dn − sn C4 1/(1−η) < −(T1 + T2) we get the desired result. In the second case (2.3) gives us

- (2.10) |F(Φj,k)(n)(ξ)| ≤ 2CnDd

n

exp(−snδj(|ξ| − ξj,k)1−η).

If δj < 1 then k < 1 − C log1/(1−η)(D) < 0 and the claim is vacuously true. Therefore it is enough to consider the case δj ≥ 1. Since D ≤ |ξ|, ξj,k ≤ 21 it suﬃces to prove that for |ξ| ≥ 12 we have

- (2.11) 2Cn|ξ|d


1−η

- 1

- 2


c |ξ|T

exp −sn |ξ| −

≤

1+T2 , which is true for some constant c since exp(t1−η) grows faster than any polynomial.

n

For our purposes we will choose η = 1 − 1+1ε so that 1−1η = 1 + ε. Put J = {j | δj ≥ 1}. Since {Ij}j∈J is a Whitney decomposition of I we have j∈J δj ≥ |I| − O(1) = D − O(1) and there are O(log(|I|)) = O(log(D)) elements in J . In the proof of Theorem 1.1 we

will work with the set S = {(j,k) | j ∈ J ,k < δj − C log1+ε(D)}. Its size is at least j∈J δj − C|J |log1+ε(D) = D − C log2+ε(D).

3. proof of Theorem 1.1

Put D = 4R1R2 and assume that nΛ(R1) + nM(R2) < D − C log2+ε(D). Consider the function f(x) = (j,k)∈S aj,kΦj,k(2R2x). By a linear algebra argument and the lower bound for |S| we can ﬁnd aj,k such that f(r(λ))(λ) = 0,|λ| ≤ R1, fˆ(k(µ))(µ) = 0,|µ| ≤ R2 and |aj,k|2 = 1.

Since Φj,k are supported on [−D2 , D2 ], the function f is supported on [−R1,R1]. Since the functions Φj,k are orthonormal in L2(−D2 , D2 ) we have that ||f||L2(R) = √21R

and therefore

2

there exists x ∈ [−R1,R1] such that |f(x)| ≥ √1D. Consider formula (1.1) with this x. By construction we have f(r(λ))(λ) = 0 for |λ| ≤ R1 but since suppf ⊂ [−R1,R2] the same

holds for λ with |λ| > R1 as well. Therefore the ﬁrst half of the interpolation formula is 0. Similarly in the second half only terms with |µ| > R2 remain. Thus we have

fˆ(k(µ))(µ)bµ(x).

- (3.1) f(x) =


µ∈M,|µ|>R2

Note that we trivially have |aj,k| ≤ 1. Expanding (3.1) into F(Φj,k) and using the bound

- (2.7) (which we can apply since after our scaling by 2R2, the bounds for |x| > 12 correspond to bounds for |x| > R2)

- (3.2)


c(2R2)T

1 √

2

|S|(2R2)−k(µ)

D ≤

bµ(x).

DT1

|µ|T

2

µ∈M,|µ|>R2

Since 2R2 ≥ 1 we have (2R2)−k(µ) ≤ 1. We also have |S| ≤ D. By the assumption of the theorem we have |bµ(x)| ≤ P(x,µ) for some polynomial P. Since |x| ≤ R1 ≤ D and 1 ≤ R2 ≤ µ we have P(x,µ) ≤ c DU|µ|U for some U. Finally since 2R2 ≤ D we have (2R2)T

2. Collecting everything we get

≤ DT

2

- (3.3)

1 √

D ≤

cc DT1−U−T2−1

µ∈M,|µ|>R2

|µ|U−T

2

.

Since nM(R) ≤ RL we can choose T2 large enough so that the last sum converges and is bounded by some absolute constant c . Choosing T1 ≥ U + T2 + 2 we get

- (3.4)

1 √

D ≤

cc c D

,

which is false for large enough D. For smaller D we can artiﬁcially enlarge C and make the conclusion of the theorem vacuously true.

If formula (1.1) is true only for even/odd functions then we put D = 2R1R2 and consider

f(x) = (j,k)∈S aj,kΦj,k(R2(2x − R1)) for x > 0 and f(−x) = ±f(x). The rest is basically the same and we get the bound

- (3.5) nΛ(R1) + nM(R2) ≥ D − C log2+ε(D) = 2R1R2 − C log2+ε(2R1R2).


4. Concluding remerks

We have proved that every interpolation formula satisﬁes a 4WT-type theorem in a very strong form. However, we would like to point out that our methods are very robust: the only things that we need are a suﬃcient number of pairwise orthogonal functions with good time-frequency localization properties and that interpolation is done by means of linear functionals. Due to that and the strong decay of the functions F(Φj,k) which is at the limit of what is allowed by the Beurling–Malliavin theorem we can signiﬁcantly weaken the

assumptions of the theorem as well as prove similar results in diﬀerent settings (although at an expense of a worse error term). We list below some extensions and variations which we believe may be interesting.

- (1) If we use the bound (2.3) directly we can assume much less about the interpolation

formula, essentially up to |bµ(x)| exp((|x| + |µ|)1−ε) and |nM(R)| exp(R1−ε). Moreover, we can even allow a slightly growing function k(µ) (see Remark 2.3).

- (2) We can replace point evaluations (that is convolutions with the δ-function) in the interpolation formula by the convolution with some other fast decaying distribution, for example the gaussian (though in that case we need to assume something about the ﬁrst half of the interpolation formula as well). This gives in particular another proof of the fact that there is no interpolation formula for the functions from Theorem 1.2.
- (3) We can prove a local 4WT Theorem for interpolation formulas. Since time-frequency shifts are isometries on L2(R) we can consider not only intervals [−R1,R1] and [−R2,R2], but arbitrary pair of intervals I,J. In that situation we can show that the total number of points in I and J is at least |I||J| − C log2+η(|I||J|) if I and J are not extremely far from the origin in comparison with their lengths.
- (4) We can allow nonreal interpolation points. Since the Fourier transform of a compactly supported function is an entire function, it makes sense to speak about its value at an arbitrary complex point. A closer examination of the methods from [6] shows that


in that case the bound for the value at the point x + iy is multiplied by e2π|y|R

1, that is we want imaginary parts to be not very large. Fortunately, even in the absence of the Riemann Hypothesis, this is the case for the interpolation formula from [3] which allows us to apply our method to the setting of [3].

Moreover, in [3] it has been proved that any interpolation formula yields a Dirichlet series kernel satisfying a functional equation akin to that of the Riemann zeta function and conversely any interpolation formula comes from contour integration against such a kernel. Therefore, even if the interpolation points are real, it is natural to go to the complex plane and consider a truncated contour integral, assuming in the theorem bounds for the kernel instead of bounds for the interpolation functions bµ(x).

Finally let us mention an interesting question which requires a more substantial modiﬁcation of our methods: how to generalize Theorem 1.1 to interpolation formulas for radial functions in higher dimensions? There are recently discovered interpolation formulas in dimensions 8,24 [4] and in all dimensions larger than or equal to 5 [14] which are similar to (1.1). We expect an analogous 4WT Theorem to be true in this case as well but the methods from [6] by themselves are not suﬃcient to establish this. Indeed, one of the key

ideas in [6] was that multiplication by cos(|x|) on the Fourier transform side corresponds to the superposition of two shifts, and there is no such result in dimension higher than 1. We will return to this problem in a forthcoming paper.

Acknowledgments. I would like to thank Kristian Seip for sharing his hypothesis about the potential connection between Slepian’s 4WT Theorem and Fourier interpolation formulas. I also would like to thank Andrii Bondarenko and Danylo Radchenko for fruitful discussions. This work was supported by Grant 275113 of the Research Council of Norway and in part by the Moebius Contest Foundation for Young Scientists.

References

- [1] G. Ascensi, Y. Lyubarskii, and K. Seip, Phase space distribution of Gabor expansions, Appl. Comput. Harmon. Anal., 26 (2009), pp. 277–282.
- [2] P. Auscher, G. Weiss, and M. V. Wickerhauser, Local sine and cosine bases of Coifman and Meyer and the construction of smooth wavelets, in Wavelets, vol. 2 of Wavelet Anal. Appl., Academic Press, Boston, MA, 1992, pp. 237–256.
- [3] A. Bondarenko, D. Radchenko, and K. Seip, Fourier interpolation with zeros of zeta and Lfunctions, arXiv:2005.02996.
- [4] H. Cohn, A. Kumar, S. Miller, D. Radchenko, and M. Viazovska, Universal optimality of the E8 and Leech lattices and interpolation formulas, arXiv:1902.05438.
- [5] R. R. Coifman and Y. Meyer, Remarques sur l’analyse de Fourier ` feneˆtre, C. R. Acad. Sci. Paris S´er. I Math., 312 (1991), pp. 259–261.
- [6] A. Israel, The Eigenvalue Distribution of Time-Frequency Localization Operators, arXiv:1502.04404.
- [7] H. J. Landau and H. O. Pollak, Prolate spheroidal wave functions, Fourier analysis and uncertainty. III. The dimension of the space of essentially time- and band-limited signals, Bell System Tech. J., 41 (1962), pp. 1295–1336.
- [8] D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci., 129 (2019), pp. 51–81.
- [9] K. Seip, Density theorems for sampling and interpolation in the Bargmann-Fock space. I, J. Reine Angew. Math., 429 (1992), pp. 91–106.
- [10] A. Shadrin, The Landau–Kolmogorov inequality revisited, Discrete Contin. Dyn. Syst., 34 (2014), pp. 1183–1210.
- [11] D. Slepian, Some asymptotic expansions for prolate spheroidal wave functions, J. Math. and Phys., 44 (1965), pp. 99–140.
- [12] , On bandwidth, Proc. IEEE, 64 (1976), pp. 292–300.

- [13] D. Slepian and H. O. Pollak, Prolate spheroidal wave functions, Fourier analysis and uncertainty. I, Bell System Tech. J., 40 (1961), pp. 43–63.
- [14] M. Stoller, Fourier interpolation from spheres, arXiv:2002.11627.


#### Department of Mathematical Sciences, Norwegian University of Science and Technology, NO-7491 Trondheim, Norway lyosha.kulikov@mail.ru

