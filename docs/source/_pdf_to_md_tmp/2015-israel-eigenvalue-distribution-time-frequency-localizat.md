# THE EIGENVALUE DISTRIBUTION OF TIME-FREQUENCY LOCALIZATION OPERATORS

arXiv:1502.04404v1[math.CA]16Feb2015

ARIE ISRAEL

Mathematics Department, University of Texas at Austin.

ABSTRACT. We estimate the distribution of the eigenvalues of a family of time-frequency localization operators whose eigenfunctions are the well-known Prolate Spheroidal Wave Functions from mathematical physics. These operators are fundamental to the theory of bandlimited functions and have applications in signal processing. Unlike previous approaches which rely on complicated formulas for the eigenvalues, our approach is simple: We build an orthonormal basis of modulated bump functions (known as wave packets in time-frequency analysis) which approximately diagonalizes the operator of interest.

1. INTRODUCTION

This paper concerns the distribution of eigenvalues of time-frequency localization operators (TFLOs) of the form

- (1) TI,Jf = RIPJRIf

where I, J are compact intervals, and RI : L2(R) → L2(R), PJ : L2(R) → L2(R) are associated projection operators in the time and frequency variables, i.e.

(RIf)(x) =

f(x) x ∈ I 0 x ∈ R \ I,

- (2)

(PJf)(x) =

J R

- (3) f(y)e−2πiω·(y−x)dydω.


The eigenfunctions of TI,J are the restrictions to I of Prolate Spheroidal Wave Functions (PSWFs), which arose ﬁrst in the study of the Helmholtz equation in mathematical physics [13]. Due to the connection with TFLOs, the PSWFs provide an optimal basis for the representation of bandlimited functions on an interval, as observed in Landau-Pollack [5, 6], Slepian [10, 11], and Slepian-Pollack [12]. More recently, PSWFs have been applied to produce quadrature formulas [8] and interpolation schemes [9] for computing with bandlimited functions.

As demonstrated in [3], the eigenvalues of TI,J display a concentration phenomenon in the asymptotic limit as the parameter Λ := |I|·|J| tends to inﬁnity: For ǫ > 0, there are approximately Λ eigenvalues in the interval [1,1 − ǫ], approximately C log(Λ) · log(1/ǫ) eigenvalues in the interval (ǫ,1 − ǫ), and the remaining eigenvalues form a sequence tending to zero at an exponential rate. This estimate is asymptotic, meaning

that it is guaranteed only for some sufﬁciently large Λ; no quantitative bounds were known for any ﬁnite Λ until recently: A quantitative upper bound on the eigenvalue sequence was proven in Osipov [7].

This paper’s aim is to present an alternate method for estimating the eigenvalues of a TFLO using techniques from time-frequency analysis. We will prove quantitative upper and lower bounds by giving an example of a basis of time-frequency wave packets (the local-cosine basis) that approximately diagonalizes the TFLO. Our results are sub-optimal by a single factor of log(1/ǫ). We hope that the methods given here can be used to study localization operators associated to domains in higher-dimensions. We leave this investigation for a future work.

- 1.1. Statement of main results. We ﬁx intervals J = [−1/2,1/2] and I = [−D/2,D/2], where D ≥ 2.


The operator T = TI,J deﬁned in (1) is compact and positive-semideﬁnite, and its L2 operator norm is at most 1. We write L2(R) as the direct sum H ⊕ ker(T), where H = ker(T)⊥; clearly, L2(R \ I) is a subspace of ker(T). Thus, we may regard T as an operator on L2(I). The spectral theorem for compact operators implies that the spectrum of T is discrete and the positive eigenvalues of T form a non-increasing sequence {λk} in (0,1], with λk → 0 as k → ∞. Furthermore, there exists an orthonormal basis {ψk}k∈N for the subspace H = ker(T)⊥ of L2(I) satisfying the eigenvalue equation Tψk = λkψk for all k ∈ N.

The position of the eigenvalue of T closest to λ = 1/2 is described in the next result from [4].

# Theorem 1. We have

- 1

![image 1](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile1.png>)

- 2


(4) λ[D]−1 ≤

≤ λ[D]. Here, we write [x] to denote the integer part of a real number x.

Our main result bounds the number of eigenvalues contained in an interval centered about λ = 1/2.

## Theorem 2. For each η ∈ (0,1/2] there exists a constant Aη ≥ 1 such that the following holds. Given ǫ ∈ (0,1/2) and D ≥ 2, deﬁne

K = Aη · log log(D) · ǫ−1 1+η · log(D · ǫ−1). Then

k ∈ N : λk ∈ (ǫ,1 − ǫ) ⊂ [D − K,D + K].

Remark 1. In [7], a one-sided bound k ∈ N : λk ≥ ǫ ⊂ [0,D + K′] is proven, with K′ = C log(D)2 log(1/ǫ). Our result has an improved dependence on D, but sub-optimal dependence on ǫ. The optimal bound is expected to be K′′ = C log(D)log(1/ǫ), as predicted by the asymptotic analysis in [3].

Our strategy for proving Theorem 2 will be to construct an approximate eigenbasis for the operator T. We deﬁne a family of translated and modulated bump functions (the local-cosine basis). The result follows by counting the number of basis functions whose “time-frequency proﬁle” is localized inside the rectangle I × J in phase space.

The outline of the paper is as follows. In Section 2 we present the functional analysis lemma that will be used to control the eigenvalues of our operator. In Section 3 we construct a local-cosine basis and present its basic properties. We prove the key energy estimates for this basis in Section 4. We conclude the paper in Section 5 with the proof of Theorem 2.

- 1.2. Acknowledgements. We are grateful to Mark Tygert for useful discussions and for his comments during the preparation of this work. We are also grateful to Rachel Ward for proofreading an early version of this paper.


2. THE MAIN LEMMA

Let H be a complex Hilbert space, and let {φk}k∈I be an orthonormal basis for H. Denote the inner product on H by  ·,·  and the Hilbert norm on H by ϕ := ϕ,ϕ for ϕ ∈ H.

Let T : H → H be a compact, positive-semideﬁnite operator, with operator norm at most 1. By the spectral theorem for compact operators, there is a sequence 1 ≥ λ1 ≥ λ2 ≥ ··· > 0, and a complete orthonormal basis {ϕℓ}ℓ∈N for the subspace H′ = ker(T)⊥ of H, satisfying the eigenvalue equation Tϕℓ = λℓ · ϕℓ for all ℓ ∈ N. For ǫ ∈ (0,1/2), let Mǫ = Mǫ(T) denote the number of eigenvalues λℓ (counted with multiplicity) that belong to the interval (ǫ,1 − ǫ).

- Lemma 1. Let {φk}k∈I be an orthonormal basis for H. Assume that I is the disjoint union I0 ∪ I1 ∪ I2, where


- (5) k∈I0

Tφk 2 +

k∈I2

Tφk − φk 2 ≤ ǫ3.

Then we have Mǫ ≤ 2 · #(I1).

Proof. Note that Mǫ is the dimension of the subspace Sǫ := span{ϕℓ : λℓ ∈ (ǫ,1 − ǫ)} of H.

Consider the orthogonal projection operator πǫ : H → Sǫ. Note that T and πǫ commute, since Sǫ is spanned by a collection of eigenvectors of T.

By deﬁnition, we have ǫ φ ≤ Tφ and ǫ φ ≤ Tφ − φ for all φ ∈ Sǫ. Hence, ǫ · πǫφ ≤ Tπǫφ = πǫTφ ≤ Tφ , and ǫ · πǫφ ≤ Tπǫφ − πǫφ = πǫ(Tφ − φ) ≤ Tφ − φ for all φ ∈ H.

Using φ = φk (k ∈ I0 ∪ I2) in the above estimates, we see that

k∈I0∪I2

ǫ2 · πǫφk 2 ≤

k∈I0

Tφk 2 +

k∈I2

Tφk − φk 2

(5)

≤ ǫ3.

Therefore,

- (6) k∈I0∪I2


πǫφk 2 ≤ ǫ ≤ 1/2.

We may assume that Mǫ = dim(Sǫ) ≥ 1, for otherwise the conclusion of the lemma is trivial. Then, by the Parseval identity and the fact that πǫ is an orthogonal projection operator for Sǫ, we have

ψ 2 =

k∈I

ψ,φk 2 =

k∈I

ψ,πǫφk 2 for all ψ ∈ Sǫ.

We ﬁx an orthonormal basis for Sǫ and sum the previous estimate over all ψ belonging to that basis. Thus we obtain

- (7) dim(Sǫ) = k∈I

πǫφk 2,

where here again we have used the Parseval identity to simplify the right-hand side. Recall that I is the disjoint union I0 ∪ I1 ∪ I2. Since dim(Sǫ) ≥ 1, we learn from (6) and (7) that

- (8) k∈I1

πǫφk 2 ≥ dim(Sǫ) − 1/2 ≥ (1/2) · dim(Sǫ).

Finally, note that πǫφk 2 ≤ φk 2 = 1 for any k ∈ I1. Thus (8) yields Mǫ = dim(Sǫ) ≤ 2 · #(I1), as desired.

3. LOCAL TRIGONOMETRIC BASES

In this section we exhibit a smooth compactly supported cutoff function whose Fourier transform has near-exponential decay. We follow an approach found in [2]. Using this cutoff function we construct an orthonormal basis for L2(I) (I a compact interval) consisting of modulated bump functions. This is the local cosine basis of Coifman-Meyer [1].

- 3.1. A cutoff function. Fix an integer m ≥ 1, and deﬁne


- (9) a(x) =


−m

−m

e−(1−x)

e−(x+1)

x ∈ (−1,1)

0 x ∈ (−∞,1] ∪ [1,∞). Write Dkf to denote the k-fold derivative of a function f : R → R.

# Lemma 2. We have

−1)k for k ≥ 0, x ∈ R. Here our notation is that 00 = 1.

|Dka(x)| ≤ (16m)k · k(1+m

−m

Proof. First observe that Dk(e−x

) (x > 0) is equal to the sum of 2k terms of the form Fw,j,r(x) := w · x−[(m+1)j+r] · e−x

−m

,

where w is a real number, and j,r are integers satisfying j + r = k and |w| ≤ mj · [(m + 1)j + r]r. This statement is easily proven by induction on k.

Using the estimate yRe−y ≤ RR, for y,R > 0, we obtain

−1

|Fw,j,r(x)| ≤ mj · [(m + 1)j + r]r · [(m + 1)j + r] · m−1 [(m+1)j+r]·m

−1

= mj+r · [(m + 1)j + r] · m−1 (m+1)·(j+r)·m

−1)·k

≤ mk (1 + m−1) · k (1+m

−1)·k. We conclude that |Dk(e−x

≤ (4m)k · k(1+m

−m

−1)·k for x > 0. Hence, by the Leibniz rule we have

)| ≤ (8m)kk(1+m

|Dka(x)| ≤ 2k · max

0≤k′≤k

′

|Dk

sup

x∈(0,2]

m

e−1/x

| · sup

x∈(0,2]

≤ 2k max

0≤k′≤k

′)mk−k

′

′

−1)k′ · 23(k−k

23k

mk

(k′)(1+m

−1)·k for all x ∈ R. This completes the proof of the lemma.

≤ (16m)k · k(1+m

′

|Dk−k

m

e−1/x

|

′

−1)(k−k′)

(k − k′)(1+m

We deﬁne

- (10) A(x) :=

π 2 R ady

![image 2](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile2.png>)

·

x

−∞

a(y)dy.

Since a(y) is an even function (see (9)), we have

- (11) A(x) + A(−x) = π/2. Now let θ(x) := sin(A(x)). From (11) we deduce that θ(−x) = cos(A(x)). Therefore,
- (12) θ2(x) + θ2(−x) = sin2(A(x)) + cos2(A(x)) = 1 for any x ∈ R. Since a(x) = 0 for x ∈ R \ [−1,1], we have A(x) = 0 for x ≤ −1, and A(x) = π/2 for x ≥ 1. Hence,
- (13) θ(x) = 0 for x ≤ −1; θ(x) = 1 for x ≥ 1.


The next lemma provides an estimate on the size of the derivatives of θ.

- Lemma 3. Let F : C → C be an entire function, and let f : R → R be C∞. Assume that there exist C ≥ 1 and γ ≥ 1 such that |Dkf(x)| ≤ Ck · kγk for all k ≥ 0. Then there exists C0 ≥ 1 determined by C, γ, and F, such that |Dk [F(f(x))]| ≤ C0k · kγk for all k ≥ 0.


A proof of Lemma 3 is given in [2]. From the deﬁnition (9) it is clear that a(y)dy ≥ e−1 2 ≥ 1/16. We apply Lemma 2 to bound the

derivatives of A(x) deﬁned in (10). Thus we obtain |DkA(x)| ≤ Ck · k(1+m

−1)·k for all k ≥ 0.

We apply Lemma 3 to the functions F(z) = sin(z) and f(x) = A(x). Thus, for each m ≥ 1 there exists Cm ≥ 1 such that

- (14) |Dkθ(x)| ≤ Cmk · k(1+m

−1)·k for all k ≥ 0.

We summarize conclusions (12), (13), and (14), in the following result.

Proposition 1. Given a real number η > 0 there exists a C∞ function θ : R → R satisfying

- (a) θ(x) = 0 for x ≤ −1, and θ(x) = 1 for x ≥ 1.
- (b) θ2(x) + θ2(−x) = 1 for all x ∈ R.
- (c) |Dkθ(x)| ≤ Cηk · k(1+η)·k for all integers k ≥ 0 and all x ∈ R. Here, Cη ≥ 1 is a constant determined by η.


To obtain the previous result from (12), (13), and (14), we choose m > η−1.

- 3.2. Whitney intervals. By a dyadic interval we mean an interval of the form (k·2−ℓ,(k+1)·2−ℓ] for k,ℓ ∈ Z.


Let I = [−D/2,D/2] for D > 0. The Whitney decomposition of I is a collection W = {Ij}j∈J consisting of dyadic intervals. Its basic properties are as follows.

- (W1): The intervals Ij (j ∈ J ) are pairwise-disjoint, and I = j∈J Ij .
- (W2): We have |Ij| ≤ dist(Ij,∂I) ≤ 5 · |Ij| for all j ∈ J .


For a construction of the Whitney decomposition, see [14].

3.3. The local cosine basis. Let W = {Ij}j∈J be the Whitney decomposition of an interval I. We write Ij = (xj,xj + δj] for j ∈ J .

We choose positive real numbers ηj and ηj′ satisfying ηj +ηj′ ≤ 101 δj. Then deﬁne a C∞ function θj : R → R by the formula

![image 3](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile3.png>)

- (15) θj(x) := θ

x − xj ηj

![image 4](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile4.png>)

· θ

(xj + δj) − x ηj′

![image 5](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile5.png>)

.

Part (a) of Proposition 1 implies that θj is supported on xj − 101 δj,xj + 1110δj . Since dist(Ij,∂I) ≥ |Ij| = δj (see (W2)), we have

![image 6](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile6.png>)

![image 7](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile7.png>)

- (16) suppθj ⊂ I for all j ∈ J .

Denote

Γ = {(j,k) : j ∈ J , k ∈ Z, k ≥ 0}. For any (j,k) ∈ Γ we deﬁne Φ(j,k) ∈ Cc∞(I) by

- (17) Φ(j,k)(x) = C(j,k) · δj−1/2 · θj(x)cos π · δj−1 · (k + 1/2) · (x − xj) , where
- (18) C(j,k) = δj · R


−1

θj2(x)cos2 π · δj−1 · (k + 1/2) · (x − xj) dx

.

This deﬁnition of C(j,k) ensures the normalization condition Φ(j,k) L2(I) = 1. Note that θj ≥ 1 on [xj + 101 δj,xj + 109 δj], and that θj is supported on [xj − 101 δj,xj + 1011δj]. Therefore, the value of the integral term in the parentheses in (18) is between 1001 δj and 2δj. We conclude that

![image 8](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile8.png>)

![image 9](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile9.png>)

![image 10](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile10.png>)

![image 11](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile11.png>)

![image 12](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile12.png>)

- (19)

- 1

![image 13](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile13.png>)

- 2


≤ C(j,k) ≤ 100.

A theorem of Coifman-Meyer [1] states that {Φ(j,k)}(j,k)∈Γ is an orthonormal basis for L2(I) for an appropriate choice of the constants ηj and ηj′ which satisfy

- (20)

1 100

![image 14](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile14.png>)

δj ≤ ηj,ηj′ ≤

1 10

![image 15](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile15.png>)

δj.

This is often called the local cosine basis or the Coifman-Meyer basis. We note that the construction in [1] uses a different cutoff function θ. However, the proof of orthonormality requires only the conditions found in parts (a) and (b) of Proposition 15. Consequently, the arguments in [1] establish orthonormality for the basis constructed here. We note that our cutoff function θ satisﬁes the derivative bounds in part (c) of Proposition 15, which will be used later.

We henceforth assume that ηj and ηj′ satisfy (20) and are chosen so that {Φ(j,k)}(j,k)∈Γ is an orthonormal basis for L2(I).

We write f or F(f) to denote the Fourier transform of a function f ∈ L2(R), deﬁned via the formula f(ξ) =

R

f(x)e−2πixξdx.

We require the following lemma from [2].

- Lemma 4. Let θ ∈ C∞(R). Let C ≥ 1 and δ ≥ 1 be such that


- (a) θ is supported on [−1,1], and
- (b) |Dkθ(x)| ≤ Ckkδk for all k ≥ 0 and x ∈ R.


Then | θ(ξ)| ≤ Aexp(−a · |ξ|1/δ) for all ξ ∈ R, where a,A > 0 depend only on C and δ.

We deﬁne ψj(x) := θj(x·δj +xj) for j ∈ J , which can be rewritten as ψj(x) = θ x · ηδj

![image 16](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile16.png>)

j

·θ (1 − x) · ηδj′

![image 17](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile17.png>)

j

(see (15)). From part (c) of Proposition 1 and since ηj,ηj′ ∈ [1001 δj, 101 δj] we conclude that |Dkψj(x)| ≤ Cηk · k(1+η)·k for k ≥ 0 and x ∈ R. By applying Lemma 4 we learn that

![image 18](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile18.png>)

![image 19](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile19.png>)

| ψj(ξ)| ≤ Aη · exp −aη · |ξ|(1+η)

−1

Because of the scaling relationship between ψj and θj and simple properties of the Fourier transform, as well as the bound 1 − η ≤ (1 + η)−1 (η > 0), we conclude that

- (21) | θj(ξ)| ≤ Aη · δj · exp(−aη · |δj · ξ|1−η) for ω ∈ R.


Using the formula (17) and the scaling/translation/modulation properties of the Fourier transform F, we have

F(Φ(j,k))(ξ) = C(j,k) · δj−1/2 ·

- 1

![image 20](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile20.png>)

- 2


· θj ξ −

- 1

![image 21](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile21.png>)

- 2


(k + 1/2) · δj−1 · exp −πi · (k + 1/2) · δj−1 · xj

+ θj ξ +

In particular, thanks to (21) and (19) we have

- 1

![image 22](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile22.png>)

- 2


(k + 1/2) · δj−1 · exp πi · (k + 1/2) · δj−1 · xj .

- (22) |F(Φ(j,k))(ξ)| ≤ Cη · δj1/2 σ=±1

exp −aη · δj · ξ − σ ·

- 1

![image 23](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile23.png>)

- 2


k +

- 1

![image 24](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile24.png>)

- 2


1−η

,

for constants aη > 0 and Cη > 0. For k ∈ Z≥0 and j ∈ J we denote

ξjk = (2k + 1) · (4δj)−1. If we let Bη(ξ) := Aη exp −aη · |ξ|1−η , then the bound (22) states that

- (23) |F(Φ(j,k))(ξ)| ≤ δj1/2 · [Bη (δj · (ξ − ξjk)) + Bη (δj · (ξ + ξjk))].

4. ENERGY ESTIMATES

Recall that J = [−1/2,1/2] is the frequency localization interval and I = [−D/2,D/2] is the time localization interval. We decompose I into its Whitney decomposition W = {Ij}j∈J . We write Ij = (xj,xj +δj].

In the previous section we deﬁned an orthonormal basis {Φ(j,k)}j∈J,k∈Z

≥0

for L2(I). Recall that Φ(j,k) is supported on the interval Ij∗ = (xj − 101 δj,xj + 1011δj]. Moreover, the Fourier transform of Φ(j,k) is (nearly) exponentially concentrated about the frequencies ξ = ±ξjk in the sense of the bound (23). In this section we will derive the main energy estimates on our basis.

![image 25](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile25.png>)

![image 26](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile26.png>)

Let s ≥ 1 and δmin ∈ (0,1) be parameters, which will be determined in the next section. We write X = O(Y ) to indicate the inequality |X| ≤ C · Y , where C is a constant independent of all

parameters. We write X = O(Y ) to indicate the inequality |X| ≤ Cη · Y , where C is a constant depending only on the parameter η.

Consider the basis functions Φ(j,k) (k ∈ Z≥0) associated to a ﬁxed Whitney interval Ij ∈ W. We partition this collection into three groups by partitioning the index set Z≥0 as follows:

- (24) Llowj := {k ∈ Z≥0 : dist((2k + 1)/(4δj),R \ J) ≥ s · δj−1},
- (25) Lmedj := {k ∈ Z≥0 : dist((2k + 1)/(4δj),∂J) < s · δj−1},
- (26) Lhighj := {k ∈ Z≥0 : dist((2k + 1)/(4δj),J) ≥ s · δj−1}.


# Lemma 5. We have

- • #(Llowj ) = δj + O(s) if δj ≥ s,
- • #(Llowj ) = 0 if δj < s,


- • #(Lmedj ) ≤ 10s.


Proof. The numbers ξjk = (2k + 1)/(4δj) (k ∈ N) form an evenly-spaced grid of width 21δ

starting at ξj0 = 41δ

![image 27](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile27.png>)

j

. Recall that J = [−1/2,1/2]. Clearly there are at most δj +1 many indices k ∈ N satisfying ξjk ∈ J. Furthermore, if k ≤ δj − 2s − 1/2 then ξjk = 24kδ+1

![image 28](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile28.png>)

j

, and thus dist(ξjk,R \ J) ≥ s · δj−1. Therefore, we have

≤ 21 − δs

![image 29](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile29.png>)

![image 30](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile30.png>)

![image 31](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile31.png>)

j

j

δj − 2s − 1/2 ≤ #(Llowj ) ≤ δj + 1. This implies the ﬁrst bullet point.

If δj < s then s · δj−1 > 1. There are no points whose distance to R \ [−1/2,1/2] is greater than 1. Thus, in this case Llowj = ∅.

The spacing between consecutive numbers ξjk is equal to 21δ

. Thus, at most 2s + 1 of the ξjk lie in an interval of width s · δj−1 about the boundary point 1/2 ∈ ∂J. The same is true for the boundary point −1/2 ∈ ∂J. Therefore, #(Lmedj ) ≤ 2 · (2s + 1) ≤ 10s.

![image 32](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile32.png>)

j

We partition the index set Γ = J × Z≥0 into three components:

- (27) Γlow = {(j,k) : δj ≥ δmin, k ∈ Llowj }, Γmed = {(j,k) : δj ≥ δmin, k ∈ Lmedj }, Γhigh = {(j,k) : δj ≥ δmin, k ∈ Lhighj } ∪ {(j,k) : δj < δmin, k ∈ Z≥0}.


- Lemma 6. For a numerical constant C ≥ 0, we have #(Γmed) ≤ Cs · log(D/δmin).


Proof. Lemma 5 implies that

#(Lmedj ) ≤

10s.

#(Γmed) =

δj≥δmin

j∈J δj≥δmin

Property (W2) implies that the number of Whitney intervals Ij for which δj ≥ δmin is bounded by C log(diam(I)/δmin) = C log(D/δmin). Hence,

#(Γmed) ≤ Cs · log(D/δmin), as desired.

We will now prove that Fourier transform of a basis function Φ(j,k) indexed by (j,k) ∈ Γlow or (j,k) ∈ Γhigh is sharply concentrated on J or R \ J, respectively.

- Lemma 7. There exist constants C,c > 0 determined by η such that


- (28)  F(Φ(j,k)) 2L2(R\J) ≤ C exp(−c · s1−η) · log(D/δmin)

(j,k)∈Γhigh

- (29)  F(Φ(j,k)) 2L2(J) ≤ C exp(−c · s1−η) · log(D/δmin) + Cδmin.

Proof. Recall our notation: ξjk = 24kδ+1

![image 33](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile33.png>)

j

for (j,k) ∈ Γ = J × Z≥0. For j ∈ J with δj ≥ δmin, we deﬁne

- (30) Llowj,ℓ := {k ∈ Z≥0 : dist(ξjk,R \ J) ∈ [s · 2ℓ/δj,s · 2ℓ+1/δj)}, and
- (31) Lhighj,ℓ := {k ∈ Z≥0 : dist(ξjk,J) ∈ [s · 2ℓ/δj,s · 2ℓ+1/δj)} for ℓ ∈ Z≥0. Note that Llowj = ℓ≥0 Llowj,ℓ and Lhighj = ℓ≥0 Lhighj,ℓ ; see (24)-(26).

The spacing between ξjk and ξjk′ for distinct k,k′ ∈ Z≥0 is at least 21δ

![image 34](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile34.png>)

j

. Thus, a counting argument shows that

- (32) #(Lhighj,ℓ ) ≤ 10s · 2ℓ and
- (33) #(Llowj,ℓ) ≤ 10s · 2ℓ.

From (23), for any k ∈ Z≥0 we have

 F(Φ(j,k)) 2L2(R\J) ≤ C

R\J

δj · Bη(δj · (ξ − ξjk)) + Bη(δj · (ξ + ξjk)) 2dξ.

Since R \ J = (−∞,1) ∪ (1,∞) is symmetric about the origin, we deduce that

 F(Φ(j,k)) 2L2(R\J) ≤ C

R\J

δj · Bη(δj · (ξ − ξjk))2dξ

≤ C

|ξ′|≥δj·dist(ξjk,R\J)

Bη(ξ′)2dξ′

where the second inequality relies on the change of variable ξ′ = δj ·(ξ −ξjk); note that ξ ∈ R\J =⇒ |ξ′| ≥ δj · dist(ξjk,R \ J). Thus, by the deﬁnition Bη(ξ) = Aη · exp(−aη · |ξ|1−η) we conclude that

- (34)  F(Φ(j,k)) 2L2(R\J) ≤ C exp −c · [δj · dist(ξjk,R \ J)]1−η

for constants c,C > 0 that depend only on η. For k ∈ Llowj,ℓ we have dist(ξjk,R \ J) ∼ s · 2ℓ/δj, where we write A ∼ B to mean that cA ≤ B ≤ CA for some constants c,C. Thus, (34) implies that

- (35)  F(Φ(j,k)) 2L2(R\J) ≤ C exp −c · s · 2ℓ 1−η for all k ∈ Llowj,ℓ. The method used to prove (34) also shows that
- (36)  F(Φ(j,k)) 2L2(J) ≤ C exp −c · [δj · dist(ξjk,J)]1−η


(j,k)∈Γlow

- for constants c,C > 0 depending only on η. For k ∈ Lhighj,ℓ we have dist(ξjk,J) ∼ s · 2ℓ/δj. Thus, (36) implies that
- (37)  F(Φ(j,k)) 2L2(J) ≤ C exp −c · s · 2ℓ 1−η for all k ∈ Lhighj,ℓ .

We write Llowj = ℓ≥0 Llowj,ℓ. Applying (33) and (35), we learn that

j:δj≥δmin k∈Llowj

 F(Φ(j,k)) 2L2(R\J) =

j:δj≥δmin

∞

ℓ=0 k∈Llowj,ℓ

- (38)  F(Φ(j,k)) 2L2(R\J)

≤

j:δj≥δmin

∞

ℓ=0

10s2ℓ · C exp(−c · [s2ℓ]1−η)

≤

j:δj≥δmin

C · exp(−c · s1−η)

≤ C exp(−c · s1−η)log(diam(I)/δmin). In view of the deﬁnition of Γlow in (27), this completes the proof of (28).

Next we prove (29). We write Lhighj = ℓ≥0 Lhighj,ℓ . From (32) and (37) we have

j:δj≥δmin

k∈Lhighj

 F(Φ(j,k)) 2L2(J) =

j:δj≥δmin

∞

ℓ=0

k∈Lhighj,ℓ

- (39)  F(Φ(j,k)) 2L2(J)

≤

jδj≥δmin

∞

ℓ=0

10s2ℓ · C exp(−c · [s2ℓ]1−η)

≤

j:δj≥δmin

C · exp(−c · s1−η)

≤ C exp(−c · s1−η)log(diam(I)/δmin).

Alternatively, suppose that j ∈ J is such that δj < δmin. Then (23) implies that

- (40)

k≥0

 F(Φ(j,k)) 2L2(J) ≤

k≥0 J

δj · Bη(δj · (ξ − ξjk)) + Bη(δj · (ξ + ξjk)) 2dξ.

Switching the order of summation and integration in (40) and using the fact that the interval J = [−1/2,1/2] is symmetric about the origin, we have

- (41)


δj · Bη(δj · (ξ − ξjk)) 2dξ.

 F(Φ(j,k)) 2L2(J) ≤ C

J k≥0

k≥0

Since Bη(ξ) is smooth, bounded, and rapidly decaying as ξ → ∞, we can compare a Riemann sum with an integral to prove the estimate

Bη(δj · (ξ − ξjk)) 2 ≤ C

k≥0

Bη(z)2dz ≤ C uniformly for all ξ ∈ R.

R

Therefore, from (41) we have

 F(Φ(j,k) 2L2(J) ≤ Cδj · |J| = Cδj.

k≥0

By summing over all j ∈ J with δj < δmin, we conclude that

- (42)

j:δj<δmin k≥0

 F(Φ(j,k) 2L2(J) ≤ C

j:δj<δmin

δj ≤ Cδmin,

where the last estimate is a consequence of the Whitney conditions (W1) and (W2) (see Section 3.2).

In view of the deﬁnition of Γhigh in (27), we see that (39) and (42) imply the estimate (29), ﬁnishing the proof of the lemma.

5. PROOF OF THEOREM 2

In the previous section we deﬁned an orthonormal basis {Φ(j,k)}(j,k)∈Γ for L2(I), depending on a parameter η ∈ (0,1/2].

Let ǫ ∈ (0,1/2). Let s ≥ 1 and δmin ∈ (0,1) be parameters. We will choose s and δmin in the following paragraphs.

In the previous section we deﬁned a partition of Γ as Γlow ∪ Γmed ∪ Γhigh in terms of the parameters s and δmin; see (24)-(26) and (27).

For all f ∈ L2(I), Plancharel’s theorem implies that

Tf 2L2(I) = RIPJRIf 2L2(I) = RIPJf 2L2(I) ≤ PJf 2L2(R)

=

J

| f(ξ)|2dξ.

Similarly,

f − Tf 2L2(I) = f − RIPJRIf 2L2(I) = RIf − RIPJf 2L2(I) ≤ (I − PJ)f 2L2(R)

=

R\J

| f(ξ)|2dξ.

Thus

(j,k)∈Γhigh

TΦ(j,k) 2L2(I) +

(j,k)∈Γlow

- (43) TΦ(j,k) − Φ(j,k) 2L2(I)


 F(Φ(j,k)) 2L2(R\J)

 F(Φ(j,k)) 2L2(J) +

≤

(j,k)∈Γlow

(j,k)∈Γhigh

Lemma 7

≤ Cη · exp(−cη · s1−η) · log(D/δmin) + Cη · δmin, where Cη,cη > 0 are constants determined only by η.

We are ready, at last, to state our assumptions on s and δmin. We take

- (44)

 



δmin :=

ǫ3 2Cη

![image 35](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile35.png>)

, and

Cη · exp(−cη · s1−η) · log(D/δmin) ≤

- 1

![image 36](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile36.png>)

- 2


ǫ3. The second estimate is equivalent to

s ≥

1 cη

![image 37](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile37.png>)

log

2Cη log(D/δmin) ǫ3

![image 38](<2015-israel-eigenvalue-distribution-time-frequency-localizat_images/imageFile38.png>)

1/(1−η)

Elementary algebra shows that it sufﬁces to take

- (45) s := Aη · log log(D) · ǫ−1 1/(1−η) , for a constant Aη determined only by η. Now using (44) in (43) we see that


(j,k)∈Γhigh

TΦ(j,k) 2L2(I) +

(j,k)∈Γlow

TΦ(j,k) − Φ(j,k) 2L2(I) ≤ ǫ3.

Recall that Γ is equal to the disjoint union Γlow ∪ Γmed ∪ Γhigh. Thus, according to Lemma 1, if we let λk (k ∈ N) denote the positive eigenvalues of T (arranged in non-increasing order), and if we deﬁne Mǫ to be the number of eigenvalues of T in the interval (ǫ,1 − ǫ), then we have

Lemma 6

Mǫ ≤ 2 · #(Γmed)

≤ Cs · log(D/δmin)

= CAη · log log(D) · ǫ−1 1/(1−η) · log(2CηD · ǫ−3) ≤ A′η · log log(D) · ǫ−1 1+2η · log(D · ǫ−1),

for a constant Aη determined only by η. We apply (4) and conclude that {k : λk ∈ (ǫ,1 − ǫ)} ⊂ [D−2Mǫ,D+ 2Mǫ]. According to our upper bound on Mǫ, this yields

{k : λk ∈ (ǫ,1 − ǫ)} ⊂ [D − K,D + K], where

K = A′′η · log log(D) · ǫ−1 1+2η · log(D · ǫ−1) for a constant A′′η determined only by η. This completes the proof of Theorem 2.

REFERENCES

- [1] R.R. Coifman and Y. Meyer. ”Analyse de Fourier adapte´e a` une partition par des intervals de Whitney,” Colloq. Math. 63: 111-117, 1992.
- [2] J. Dziuba´nski and E. Herna´ndez. ”Band-limited wavelets with subexponential decay,” Canad. Math. Bull. 41: 398-403, 1998.
- [3] H.J. Landau. ”Eigenvalue Distribution of Time and Frequency Limiting,” Journal of Math. Analysis and Applications 77: 469-481.
- [4] H.J. Landau. ”On the Density of Phase-Space Expansions,” IEEE Trans. on Information Theory 39 (4): 1152-1156 (1993)
- [5] H. J. Landau and H. O. Pollak, ”Prolate spheroidal wave functions, Fourier analysis, and uncertainty – II,” Bell System Technical Journal 40 (1): 65-84, 1961.
- [6] H. J. Landau and H. O. Pollak, ”Prolate spheroidal wave functions, Fourier analysis, and uncertainty – III: the dimension of the space of essentially time- and band-limited signals,” Bell System Technical Journal 41 (4): 1295-1336, 1962.


- [7] A. Osipov, ”Certain upper bounds on the eigenvalues associated with prolate spheroidal wave functions,” Applied and Computational Harmonic Analysis 35 (2): 309-340, 2013.
- [8] A. Osipov and V. Rokhlin, ”On the evaluation of prolate spheroidal wave functions and associated quadrature rules,” Applied and Computational Harmonic Analysis, http://dx.doi.org/10.1016/j.acha.2013.04.002, 2013.
- [9] A. Osipov and V. Rokhlin, ”Detailed analysis of prolate quadratures and interpolation formulas,” preprint (available online).
- [10] D. Slepian, ”Prolate sphereoidal wave functions, Fourier analysis, and uncertainty – IV: extensions to many dimensions; generalized prolate spheroidal wave functions,” Bell System Technical Journal 43 (6): 3009-3057, 1964.
- [11] D. Slepian, ”Prolate spheroidal wave functions, Fourier analysis, and uncertainty – V: the discrete case,” Bell System Technical Journal 57 (5): 1371-1430, 1978.
- [12] D. Slepian and H. O. Pollak, ”Prolate spheroidal wave functions, Fourier analysis, and uncertainty – I,” Bell System Technical Journal 40 (1): 43-63, 1961.
- [13] J.A. Stratton, ”Spheroidal functions”, Proceedings of the National Academy of Sciences 21: 51-56 (1935).
- [14] E.M. Stein, ”Singular Integrals and Differentiability Properties of Functions,” Princeton U. Press, 1970.


