arXiv:1810.01558v3[math.PR]18Apr2020

NONLINEAR LARGE DEVIATION BOUNDS WITH APPLICATIONS TO WIGNER MATRICES AND SPARSE ERDOS–R˝ ENYI´ GRAPHS

By Fanny Augeri∗, Weizmann Institute of Science

We prove general nonlinear large deviation estimates similar to Chatterjee-Dembo’s original bounds except that we do not require any second order smoothness. Our approach relies on convex analysis arguments and is valid for a broad class of distributions. Our results are then applied in three diﬀerent setups. Our ﬁrst application consists in the mean-ﬁeld approximation of the partition function of the Ising model under an optimal assumption on the spectra of the adjacency matrices of the sequence of graphs. Next, we apply our general large deviation bound to investigate the large deviation of the traces of powers of Wigner matrices with sub-Gaussian entries, and the upper tail of cycles counts in sparse Erd˝s–Re´nyi graphs down to the sparsity threshold n−1/2.

1. Introduction. We will be concerned with the following large deviation question: given a random vector X in Rn and a smooth function f : Rn → R, when is shifting the mean of X the optimal large deviation strategy for the random variable f(X)?

In a seminal paper [11], Chatterjee and Dembo provided a suﬃcient criterion, and showed in the case where X is uniformly sampled on the discrete hypercube, that as soon as f has a gradient of low complexity, in the sense that it can be encoded by a small number of bits compared to the dimension, then the large deviations of f(X) are only due to changes of the mean of X. Their framework encompasses a large class of large deviation problems as the mean-ﬁeld approximation of the partition function of the Ising model (see [6]), the large deviation of sub-graph counts in Erd˝os–Re´nyi graphs which were until then tackled using the graphon formalism in [12] - and arithmetic progressions. Later, Yan generalized in [37] their nonlinear large deviation estimate to any compactly supported distribution.

![image 1](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile1.png>)

∗This project has received funding from the European Research Council (ERC) under the European Unions Horizon 2020 research and innovation programme (grant agreement No. 692452).

MSC 2010 subject classiﬁcations: 60F10, 60B20, 05C80, 52A40. Keywords and phrases: Large deviations, convex analysis, mean-ﬁeld approximation,

Wigner matrices, Erd˝s–Re´nyi graphs.

1

As a consequence of powerful structure theorems for probability measures on the discrete hypercube, Eldan obtained in [19] nonlinear large deviation bounds which do not require any second order smoothness on the given function, and where the complexity of the gradient is assessed in terms of the Gaussian mean-width of its image. Using these, he partially recovered a known result of Basak and Mukherjee [6] on the mean-ﬁeld approximation of the partition function of the Ising model, and improved the threshold of sparsity for the large deviation upper tail of triangle counts.

We will improve the error terms in the nonasymptotic bounds of [11], and in particular remove the smoothness terms. The motivation behind these improvements is that it allows for obtaining weaker dimension dependence. In particular, this entails that one can consider large deviation speeds much smaller than the dimension. In turn, this allows us to reach the critical sparsity level - as identiﬁed in [32] and [8] - in the large deviation bounds of cycle counts in sparse Erd˝os–Re´nyi graphs.

We will develop nonlinear large deviations estimates for general distributions, and propose several applications. As a ﬁrst example, we will apply our results to the mean-ﬁeld approximation of the partition function of the Ising model on a sequence of graphs whose spectra satisfy certain assumptions which include star graphs, thus strengthening the previous result of Basak and Mukherjee [6].

Next, we will use our nonlinear large deviation estimate to investigate the large deviation of traces of Wigner matrices with sub-Gaussian entries. Using a truncation argument to reduce the complexity of our function at hand, we show general upper and lower bounds. We will also prove the universality of the rate function for a class of Wigner matrices with sharp sub-Gaussian tails. This complements the results of Guionnet and Husson [20], who introduced this class and showed such universality for the large deviation of the largest eigenvalue.

Finally, we estimate the upper tail of the large deviations of cycle counts in sparse Erd˝os–Re´nyi graphs, down to the sparsity threshold n−1/2 - up to logarithmic corrections -, improving in the case of triangles the recent result of Cook and Dembo [14].

1.1. Main results. We begin with introducing some deﬁnitions. Let µ be a probability measure on Rn whose support is not included in a hyperplane. Let Λµ be the logarithmic Laplace transform of µ, that is,

∀λ ∈ Rn, Λµ(λ) = log e λ,x dµ(x).

It is known that Λµ is a strictly convex function which is C∞ on the interior of its domain denoted by DΛµ. We deﬁne Λ∗µ, the Legendre transform of Λµ, by

∀x ∈ Rn, Λ∗µ(x) = sup λ∈Rn

{ λ,x − Λµ(λ)}.

Following [34, Section 26], we say that a convex function Λ : Rn → R∪{+∞} is essentially smooth if the interior of its domain int(DΛ) is non-empty, Λ is diﬀerentiable on int(DΛ), and steep, that is, for any λk ∈ int(DΛ), converging to a point on the boundary of DΛ,

||∇Λ(λk)|| = +∞.

lim

k→+∞

The interest of this concept of essential smoothness lies in the fact that the Legendre transformation leaves invariant the class of strictly convex functions on Rn which are essentially smooth. More precisely, assuming that Λµ is essentially smooth, then by [34, Theorem 26.5], we know that Λ∗µ is also an essentially smooth function, the map ∇Λµ is one-to-one onto int(DΛ∗

µ), the interior of the domain of Λ∗µ, and the maps ∇Λµ and ∇Λ∗µ are inverse maps from one another.

For any λ ∈ int(DΛµ), one can deﬁne the measure,

- (1.1) µy = e λ,x −Λµ(λ)dµ(x),

where y = ∇Λµ(λ). Observe that diﬀerentiating Λµ, one obtains the barycenter of µy, that is,

- (1.2) y = ∇Λµ(λ) = xdµy(x).


Thus, the family of measures µy represents the collection of tilts of µ, indexed by their barycenters.

Our ﬁrst result is the following non-asymptotic version of Varadhan’s lemma (see [17, Theorem 4.3.1]). This will be instrumental in our treatment of the mean-ﬁeld behavior of the Ising model, see §1.2.1.

Theorem 1.1. Assume µ is compactly supported. Denote by K the convex hull of its support, and by D its diameter. Let f : Rn → R be a continuously diﬀerentiable function. Let δ > 0 and Dδ be a δ/D-net of the convex hull of ∇f(K) for the ℓ2-norm. Then,

log efdµ ≤ sup

{f(y) − Λ∗µ(y)} + log |Dδ| + δ.

Our approximation of the partition function is similar to the one of Chatterjee-Dembo (see [11, Theorem 1.6]), except that we do not have any other error terms but the one coming from the cardinality of the net Dδ. Unlike Eldan’s result (see [19, Corollary 2]) which involves the Gaussian mean-width of the set of gradients, we are assessing the complexity of the gradient in terms of covering numbers. Using Sudakov inequality (see [31, Theorem 3.18]), it is possible to compare [19, Corollary 2] with Theorem 1.1. More precisely, we have the following result as a corollary of Theorem 1.1.

Corollary 1.2. Assume µ is compactly supported. Denote by K the convex hull of its support and assume that the diameter of K is √n. Let f : Rn → R be a continuously diﬀerentiable function and let V = ∇f(K). There exists a numerical constant κ > 0 such that,

![image 2](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile2.png>)

{f(y) − Λ∗µ(y)} + κn31g(V )23, where g(V ) is the Gaussian mean-width of V , deﬁned as

log efdµ ≤ sup y∈Rn

![image 3](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile3.png>)

![image 4](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile4.png>)

g(V ) = E sup

ζ,Γ ,

ζ∈V

with Γ being a standard Gaussian random variable in Rn. Proof. From Theorem 1.1 we have for any δ > 0,

{f(y) − Λ∗µ(y)} + log N co(V ),(δ/√n)Bℓ2 + δ,

log efdµ ≤ sup y∈Rn

![image 5](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile5.png>)

where co(V ) denotes the convex hull of V and N co(V ),(δ/√n)Bℓ2 the covering number of co(V ) by (δ/√n)Bℓ2. By Sudakov inequality (see [31, Theorem 3.18]), we know that there exists a numerical constant c > 0 such that

![image 6](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile6.png>)

![image 7](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile7.png>)

ng(co(V ))2 δ2

log N(co(V ),(δ/√n)Bℓ2) ≤ c

![image 8](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile8.png>)

.

![image 9](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile9.png>)

But as the supremum of a convex function on a set is equal to the supremum on its convex hull, we have g(co(V )) = g(V ). Thus,

ng(V )2 δ2

log efdµ ≤ sup y∈Rn

{f(y) − Λ∗µ(y)} + c

+ δ.

![image 10](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile10.png>)

Optimizing in δ > 0, we obtain that there exists a numerical constant κ > 0 such that

{f(y) − Λ∗µ(y)} + κn13g(V )23.

log efdµ ≤ sup

![image 11](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile11.png>)

![image 12](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile12.png>)

![image 13](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile13.png>)

![image 14](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile14.png>)

![image 15](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile15.png>)

![image 16](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile16.png>)

As for the lower bound, it is a classical fact to note that as a consequence of Jensen’s inequality, one always has the following a lower bound by just changing the barycenter of the underlying reference measure.

Lemma 1.3. Let f : Rn → R be a non-negative measurable function. Then,

log efdµ ≥ sup fdµy − Λ∗µ(y), y ∈ ∇Λµ int(DΛµ) , where µy is deﬁned in (1.1).

Remark 1.4. Note the gap between the lower bound of Lemma 1.3 and the main term sup{f − Λ∗µ} in the upper bound of Proposition 1.1.

When µ is the uniform measure on the discrete hypercube, one can consider, given a function f : {0,1}n → R, its natural harmonic extension, and the just mentioned gap resolves itself. One can view this fact as at the heart of Eldan’s approach [19]. For further discussion on the general case, we refer the reader to Remark 2.2.

We will now state our nonlinear large deviations upper bound. We recall from [17, Section 1.2] that a sequence of random variables (Zn)n∈N taking value in some topological space X equipped with the Borel σ-ﬁeld B, satisﬁes a large deviations principle (LDP) with speed υn, and rate function I : X → [0,+∞], if I is lower semicontinuous, υn increases to inﬁnity, and for all B ∈ B,

1 υn

log P(Zn ∈ B)

− inf

I ≤ liminf

![image 17](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile17.png>)

n→+∞

int(B)

1 υn

log P(Zn ∈ B) ≤ − inf

≤ limsup

- (1.3) I,


![image 18](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile18.png>)

cl(B)

n→+∞

where int(B) denotes the interior of B and cl(B) the closure of B. We recall that I is lower semicontinuous if its t-level sets {x ∈ X : I(x) ≤ t} are closed, for any t ∈ [0,+∞). Furthermore, if all the level sets are compact, then I is said to be a good rate function.

By [17, (1.2.7)], for good rate functions I, the large deviations upper bound, that is the right-most inequality in (1.3), is equivalent to the statement that for any r > 0 and δ > 0,

1 vn

limsup

n→+∞

log P Zn ∈/ Vδ({I ≤ r}) ≤ −r,

![image 19](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile19.png>)

where for any subset A ⊂ R, Vδ(A) denotes the open δ-neighborhood of A, that is,

Vδ(A) = x ∈ R : inf

|x − y| < δ .

y∈A

With that in mind, the following proposition is our general large deviation upper bound.

Theorem 1.5. Let X be a random vector in Rn with law µ such that Λµ is essentially smooth. Let f : Rn → R be a measurable function. Deﬁne,

∀t ∈ R, I(t) = inf{Λ∗µ(y) : f(y) = t,y ∈ Rn}. Let r > 0. Assume there exists κ ≥ r such that denoting by K = {Λ∗µ ≤ κ},

- (1.4) P(X ∈/ K) ≤ e−r. Let W ⊂ Rn be a compact convex set such that,
- (1.5) ∀x,y ∈ K, f(x) − f(y) ≤ sup λ∈W


λ,x − y ,

Denote by D the diameter of K. Let δ > 0 and let Dδ/2 be a δ/2D-net of W for the ℓ2-norm. Then,

κLD

δ ∨ 1 + 2, where L = supλ∈V ||λ||ℓ2.

log P f(X) ∈/ Vδ({I ≤ r}) ≤ −r + log |Dδ/2| + log

![image 20](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile20.png>)

- Remark 1.6. The wording of Theorem 1.5 is intended to include nonsmooth functions which we will encounter in the applications. It is particularly relevant for functions f which are linear combinations of non-smooth convex functions, for which we can take W to be Minkowski sums of sets of subdiﬀerentials of the convex functions involved in the decomposition.
- Remark 1.7. The tightness assumption (1.6) in the Proposition 1.5 is automatically satisﬁed for product measures. Indeed, we know from [17, Lemma 5.1.14] that if µ is a probability measure on R, then for any α ∈ (0,1),


2 1 − α

EeαΛ∗µ(X1) ≤

.

![image 21](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile21.png>)

Taking α = 1/2, we deduce that for κ = 12(r ∧ n), Chernoﬀ’s inequality gives

P(Λ∗µn(X) > κ) ≤ e−r.

As a consequence of Theorem 1.5, we obtain a nonlinear large deviations estimate for the upper tail of a function with a low-complexity gradient.

Corollary 1.8. Let X be a random vector in Rn with law µ such that Λµ is essentially smooth. Let f : Rn → R be a measurable function. Deﬁne,

∀t ∈ R, φ(t) = inf{Λ∗µ(y) : f(y) ≥ t,y ∈ Rn}. Let t,δ > 0 and assume that φ is increasing on [t−δ,+∞). Let κ ≥ φ(t−δ) such that denoting by K = {Λ∗µ ≤ κ},

- (1.6) P(X ∈/ K) ≤ e−φ(t−δ). Let W ⊂ Rn be a compact convex set such that,

∀x,y ∈ K, f(x) − f(y) ≤ sup

λ∈W

λ,x − y ,

Denote by D the diameter of K and let Dδ/2 be a δ/2D-net of W for the ℓ2-norm. Then,

log P f(X) ≥ t ≤ −φ(t − δ) + log |Dδ/2| + log

κLD

![image 22](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile22.png>)

δ ∨ 1 + 2, where L = supλ∈V ||λ||ℓ2.

Proof. We claim that our assumption on the strict monotonicty of φ yields that

- (1.7) {I ≤ φ(t − δ)} ⊂ (−∞,t − δ].


Indeed, for any z ∈ R, if I(z) ≤ φ(t − δ), then in particular φ(z) ≤ φ(t − δ). Since φ is increasing on [t − δ,+∞), we have z ≤ t − δ, which shows (1.7). Therefore, if x ∈ Rn is such that f(x) ≥ t then f(x) ∈/ Vδ({I ≤ φ(t − δ)}). Thus, we have

P(f(X) ≥ t) ≤ P f(X) ∈/ Vδ({I ≤ φ(t − δ)}) , which, by Theorem 1.5, ends the proof.

![image 23](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile23.png>)

![image 24](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile24.png>)

![image 25](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile25.png>)

![image 26](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile26.png>)

Turning our attention to the lower bound, one can always get a large deviations lower bound by ﬁnding a tilting of the underlying measure µ which transforms a large deviations event for µ into a typical event for µh. (This idea is prevalent in the large deviations literature, and is also the basis for the proof of Lemma 1.3). The following lower bound, which builds on

[18, p. 64] quantiﬁes this idea. First, note that diﬀerentiating twice Λµ, one obtains the covariance of the measure µy, that is,

∀η ∈ Rn, Varµy η,X = η,∇2Λµ(λ).η , where y = ∇Λµ(λ). With this notation, one obtains the following lemma.

Lemma 1.9. Let V ⊂ Rn be a measurable subset, and λ ∈ int(DΛµ). Then,

1 µy(V )1/2

µ(V ) ≥ e−Λ∗µ(y)µy(V )exp −

![image 27](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile27.png>)

λ,∇2Λµ(λ).λ 1/2 ,

where y = ∇Λµ(λ), and µy is deﬁned in (1.1).

Proof. Let λ ∈ int(DΛµ) and y = ∇Λµ(λ). Changing the measure µ into µy, we have

µ(V ) =

e−( λ,x −Λµ(λ))dµy(x) = e−Λ∗µ(y)

V

e− λ,x−y dµy(x),

V

where we used the fact that Λ∗µ(y) = λ,y − Λµ(λ). By Jensen’s inequality we deduce,

1 µy(V ) V

µ(V ) ≥ e−Λ∗µ(y)µh(V )exp −

![image 28](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile28.png>)

λ,x − y dµy(x) .

Using Cauchy-Schwarz inequality we get,

V

λ,x − y dµy(x) ≤ µy(V )1/2 λ,x − y 2dµy(x)

1/2

,

which yields the claim.

![image 29](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile29.png>)

![image 30](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile30.png>)

![image 31](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile31.png>)

![image 32](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile32.png>)

1.2. Applications. In this section, we provide several examples in which the gap between the upper bounds (Propositions 1.1 and 1.5) and lower bounds (Lemmas 1.3 and 1.9) is negligible in the large deviation scale.

1.2.1. Mean-ﬁeld approximation in the Ising model. Our ﬁrst example of application is the accuracy of the mean-ﬁeld prediction in the Ising model with large degree. This topic is discussed in [6], [19, section 1.3], [23], [22], and we will improve on some of the results therein.

In particular, we show that the mean-ﬁeld approximation of the Ising model holds true as soon as the empirical distributions of the eigenvalues

of the interaction matrices converge weakly to a Dirac at 0, and the second moments are uniformly bounded.

Let Hn denote the set of Hermitian matrices of size n. For any A ∈ Hn, we denote by µA the empirical distribution of its eigenvalues, deﬁned by,

1 n

µA =

n

δλi,

![image 33](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile33.png>)

i=1

where λ1,... ,λn are the eigenvalues of A.

Proposition 1.10. Let An be a sequence of Hermitian matrices such that for any i ∈ {1,... ,n}, (An)i,i = 0. Assume that the empirical distribution of eigenvalues µAn converges weakly to a Dirac at 0 and that limsupn n−1trA2n < +∞. Let µ be the uniform probability measure on {−1,1}n.

Then,

log e σ,Anσ dµ(σ) = sup

x∈[−1,1]n

x,Anx − Λ∗µ(x) + o(n).

Proof. Note that the lower bound log e σ,Anσ dµ(σ) ≥ sup

x∈[−1,1]n

x,Anx − Λ∗µ(x) ,

follows directly Lemma 1.3. Let ∀x ∈ Rn, f(x) = x,Anx .

The following lemma taken from [6, Lemma 3.4, Remark 4.1] computes the complexity of the gradient of f under the mean-ﬁeld assumption we made.

Lemma 1.11 ( [6, Lemma 3.4, Remark 4.1] ). Under the assumption of Proposition 1.10, for any δ > 0, there exists a δ√n-net Eδ√n for the ℓ2-norm of the set An([−1,1]n), such that,

![image 34](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile34.png>)

![image 35](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile35.png>)

log |Eδ√n| = o(n).

![image 36](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile36.png>)

As ∇f(x) = 2Anx for any x ∈ [−1,1]n, applying Proposition 1.1 and using the above lemma, we deduce that for any δ > 0,

{ x,Anx  −Λ∗µ(x)} +log |Eδ√n| +4δn,

- (1.8) log e σ,Anσ dµ(σ) ≤ sup


![image 37](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile37.png>)

x∈[−1,1]n

which gives the claim.

![image 38](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile38.png>)

![image 39](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile39.png>)

![image 40](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile40.png>)

![image 41](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile41.png>)

Remark 1.12. Instead of using Lemma 1.11 to bound the error term in

- (1.8), one can use alternatively Corollary 1.2, which gives,


- 2

![image 42](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile42.png>)

- 3,


{ x,Anx −Λ∗µ(x)}+κn13 E sup

log e σ,Anσ dµ(σ) ≤ sup

Anx,Γ

![image 43](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile43.png>)

x∈[−1,1]n

x∈[−1,1]n

where κ > 0 and Γ is a standard Gaussian vector in Rn. But, using twice Cauchy-Schwarz inequality and the fact that E||AnΓ||2 = ||An||2, one obtains

√n||An||2,

![image 44](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile44.png>)

Anx,Γ ≤

E sup

x∈[−1,1]n

where || ||2 denotes the Hilbert-Schmidt norm. Thus, log e σ,Anσ dµ(σ) ≤ sup

{ x,Anx − Λ∗µ(x)} + κ(||An||2n)23, thus giving another proof of the result of Jain, Koehler and Risteski [22].

![image 45](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile45.png>)

x∈[−1,1]n

- 1.2.2. Traces of powers of Wigner matrices. In this section, we discuss

the large deviations of the normalized traces of powers of Wigner matrices with sub-Gaussian entries. Under technical assumptions, we show that we can ﬁnd large deviation upper and lower bounds, which match in the case where the entries have sharp sub-Gaussian tails and have the same covariance structure as the GOE or the GUE. In the latter case, the large deviations are universal, that is, the resulting rate function is the same for all such Wigner matrices, and coincides with the Gaussian case. This universality phenomenon was ﬁrst discovered by Guionnet and Husson in [20], in the context of the large deviations of the largest eigenvalue of Wigner matrices.

To state our result we need to introduce some notations. Denote by Hn(β) the set of Hermitian matrices when β = 2, and symmetric matrices when β = 1, of size n, which we will short-hand as Hn whenever there is no ambiguity. Say that X is a Wigner matrix if X is a random Hermitian matrix with independent coeﬃcients (up to the symmetry) such that both (Xi,i)1≤i≤n and (Xi,j)i<j are identically distributed, EX = 0, (ℜX1,2,ℑX1,2) are independent and E|X1,2|2 = 1. By Wigner’s theorem (see [1, Theorem

- 2.1.1, Exercice 2.1.16], [5, Theorem 2.5]), we know that


µX/√n

µsc,

![image 46](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile46.png>)

n→∞

in probability, where denotes the weak convergence, and µsc is the semicircular law deﬁned by,

- 1

![image 47](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile47.png>)

- 2π


µsc =

![image 48](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile48.png>)

4 − x21|x|≤2dx.

If we assume moreover that for any d ∈ N,

max E|X1,1|d,E|X1,2|d < +∞, then we have by [1, Lemmas 2.1.6,2.1.7], the convergence of the moments of µX/√n towards the ones of the semi-circular law, that is for any d ∈ N,

![image 49](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile49.png>)

tr(X/√n)d −→

1 n

µsc(xd), in probability, where µsc(xd) = xddµsc(x). It is known that µsc(xd) =

![image 50](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile50.png>)

![image 51](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile51.png>)

n→+∞

Cd/2 if d is even, 0 if d is odd,

where in the case d is even, Cd/2 = d/2+11 d/ d2 is the d2 th Catalan number. The question we investigate is the one of the large deviations of the these

![image 52](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile52.png>)

![image 53](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile53.png>)

traces around the moments of the semi-circular law.

We will actually prove a large deviation result under a more restrictive assumption than just the one of having sub-Gaussian entries, as we will need to use further concentration arguments in addition to the result of Theorem 1.5. To this end, we introduce a class of random Hermitian matrices satisfying a certain convex concentration property.

Definition 1.13. We say that a random Hermitian matrix X satisﬁes the convex concentration property if there exists c > 0 such that if for any f : Hn → R convex 1-Lipschitz function with respect to the Hilbert-Schmidt norm, Ef(X) exists and for any t > 0,

P |f(X) − Ef(X)| > t ≤ c−1 exp − ct2 .

Remark 1.14. A random Hermitian matrix whose law satisﬁes a logSobolev inequality has normal concentration by [30, Theorem 5.3]. In particular, such random matrices satisfy the above convex concentration property. Workable criteria for log-concave measures to satisfy a log-Sobolev inequality include the strict uniform convexity of the potential, see [30, Theorem 5.2]. Due to the tensorization property of the log-Sobolev inequality (see [30, Corollary 5.7]), any Wigner matrix with entries satisfying a log-Sobolev inequality has the convex concentration property.

Another important family of Wigner matrices satisfying this property are the one with bounded entries, due either to Talagrand’s inequality [30, Corollary 4.10] or due to a result by the transportation method [33, Theorem 8.6] (the latter having the advantage of directly measuring deviations from the mean).

In the following, we denote by Λ the logarithmic Laplace transform of the law of X, that is,

∀H ∈ Hn, Λ(H) = log Eetr(XH),

and by Λi,j the one of the law of each of its entries Xi,j. Finally, we denote by Λ∗ the Legendre transform of Λ.

Using Proposition 1.5, together with a truncation argument which enable us to reduce ourself to a function with a low complexity gradient, we obtain the following large deviation result for traces of Wigner matrices.

Theorem 1.15. Let d ≥ 3, and ℓ > d be an even integer. Let X be a Wigner matrix satisfying the convex concentration property such that Λ1,1 and Λ1,2 have their derivatives of order 2 to ℓ uniformly bounded. For any closed subset F of R,

tr(X/√n)d ∈ F ≤ −inf

1 n

1 n1+d2

![image 54](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile54.png>)

I+, and for any open subset O of R, liminf

log P

limsup

![image 55](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile55.png>)

![image 56](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile56.png>)

F

n→+∞

![image 57](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile57.png>)

tr(X/√n)d ∈ O ≥ −inf

1 n

1 n1+d2

![image 58](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile58.png>)

I−, where for any x ∈ R,

log P

![image 59](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile59.png>)

![image 60](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile60.png>)

n→+∞

O

![image 61](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile61.png>)

I+(x) = sup δ>0

liminf

In,δ(x),

n→+∞

In,δ(x), and for any n ∈ N, δ > 0,

I−(x) = sup δ>0

limsup

n→+∞

Λ∗(Y ) n1+d2

tr(Y/√n)d + µsc(xd) − x| < δ,Y ∈ Hn .

1 n

![image 62](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile62.png>)

: |

In,δ(x) = inf

![image 63](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile63.png>)

![image 64](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile64.png>)

![image 65](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile65.png>)

Remark 1.16. Together with the previous Remark 1.14, we see that any Wigner matrix with bounded entries satisﬁes the assumptions of Theorem 1.15.

We will now specify our result to Wigner matrices with sharp sub-Gaussian tails. Following Guionnet and Husson [20], we say that a real or complex random variable ξ has sharp sub-Gaussian tails if,

- 1

![image 66](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile66.png>)

- 2


∀z ∈ C, Λξ(z) = log Eeℜ(zξ) ≤

z,Σz ,

where Σ is the covariance matrix of (ℜξ,ℑξ), and .,. is the standard inner product in C.

Corollary 1.17. Let d ∈ N,d ≥ 3. Let X be a Wigner matrix such

that EX12,1 ≤ 2/β. Assume that X is real symmetric if β = 1, and if β = 2, that (ℜX1,2,ℑX1,2) are independent each of variance 1/2. In addition to the assumptions of Theorem 1.15, assume that the entries of X have sharp sub-

Gaussian tails. The sequence (n1tr(X/√n)d)N∈N satisﬁes a LDP with speed n1+d2, and good rate function Jd. If d is even, Jd is given by,

![image 67](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile67.png>)

![image 68](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile68.png>)

![image 69](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile69.png>)

∀x ∈ R, Jd(x) =

2

β 4 x − Cd/2

d if x ≥ Cd/2,

![image 70](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile70.png>)

![image 71](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile71.png>)

+∞ otherwise,

where Cd/2 denotes the d2 th Catalan number, and if d is odd,

![image 72](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile72.png>)

β 4 |x|

2

∀x ∈ R, Jd(x) =

d , where β = 1 if X is real symmetric and β = 2 if X is complex Hermitian. Remark 1.18. Distributions which have sharp sub-Gaussian tails in-

![image 73](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile73.png>)

![image 74](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile74.png>)

clude the Rademacher distribution 12δ1+ 12δ−1 and uniform probability measures on intervals symmetric around the 0, see [20, Examples 1.2]. Therefore,

![image 75](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile75.png>)

![image 76](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile76.png>)

the above LDP holds in particular for Wigner matrices with Rademacher entries, or uniformly sampled in [−

√3,√3].

![image 77](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile77.png>)

![image 78](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile78.png>)

1.2.3. Upper tail of cycle counts in sparse Erdo˝s–Re´nyi graphs. Let X be the adjacency matrix of an Erd˝os–Re´nyi graph on n vertices with parameter pn = p. More precisely, we assume that X is a symmetric matrix, such that (Xi,j)i<j are independent Bernoulli random variables of parameter p, whereas Xi,i = 0 for any i ∈ {1,... ,n}.

For a given ﬁnite graph H, denote by XH the number of copies of H in the Erd˝os–Re´nyi graph. A general question is to understand the large deviation of XH of the order of its expectation when n goes to +∞. When p is ﬁxed, the large deviation of these sub-graph counts are well understood now due to the work of Chatterjee and Varadhan [12] on the large deviations of the Erd˝os–Re´nyi graph for the cut-metric.

When p ≪ 1, a ﬁrst question is to estimate the order of the upper tail, that is, for u ≥ 1,

P(XH ≥ uEXH).

In the case of triangles H = K3, it was proven in a series of papers [36], [27], [10], [16], that for any p ≥ 1/n,

log P(XK3 ≥ uEXK3) ≍ −min(n2p2 log(1/p),n3p3),

and then generalized in [15] for cliques of arbitrary size. For general graphs H, the order of the upper tail has been computed up to some log(1/p) factor, by Janson, Oleszkiewicz and Rucin´ski in [25]. In particular, denoting by ∆ is the highest degree in H, they proved in [25, Theorems 1.2,1.5], that

−n2p∆ log(1/p) log P(XH ≥ uEXH) −n2p∆,

for p ≥ n−1/∆. Still, the exact order of this tail is not fully understood for small edge-probability, as the order conjectured in [15] by Kahn and DeMarco was recently disproved by Sileikisˇ and Warnke in [35].

Working instead with homomorphism densities, that is, if H has vertex set V and edge set E,

t(H,X) =

1 n|V|

Xi(v),i(w),

![image 79](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile79.png>)

![image 80](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile80.png>)

![image 81](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile81.png>)

i∈{1,...,n}V (v,w)∈E

![image 82](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile82.png>)

Chatterjee and Dembo showed in [11] that the large deviations of t(H,X) fall into their framework of nonlinear large deviations. The large deviation upper tail is understood by a certain variational problem,

- (1.9) − log P t(H,X) ≥ uEt(H,X) ∼ φn,H(u), with
- (1.10) φn,H(u) = inf Λ∗p(Y ) : t(H,Y ) ≥ uEt(H,Y ), Y ∈ Hn0 ,


where Hn0 is the set of symmetric matrices of size n with null diagonal coeﬃcients, and Λ∗p(Y ) = i<j Ip(Yi,j), where

1 − x 1 − p

x p

+ (1 − x)log

∀x ∈ [0,1], Ip(x) = xlog

,

![image 83](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile83.png>)

![image 84](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile84.png>)

and +∞ otherwise. The equivalent (1.9) was shown to hold in [11, Theorem

- 1.2] for p ≥ n−α(H), for some explicit constant α(H) > 0 depending on H.


In the case where H = K3, the threshold of validity of (1.9) found was n−1/42, up to logarithmic factor, and was pushed later on by Eldan in [19] to n−1/18. Yet, neither of these thresholds are expected to be optimal, and in this case of triangle counts, it is conjectured that (1.9) holds as soon as the variational problem (1.10) gives the right order of the upper tail, that is, with the help of [32], np ≫ log n.

Very recently, Cook and Dembo [14] proved that the nonlinear large deviations of t(H,X) holds for the range n−1/(5∆−4) ≪ p ≪ 1, and more

strongly, in the case of d-cycles counts for n−1/2 log n ≪ p ≪ 1 when d ≥ 4, and n−1/3 ≪ p ≪ 1 when d = 3.

We will give an alternative proof of their result on cycle counts. In the following proposition, we push the estimation of the upper tail for sparsity parameters satisfying n−1/2 log4 n ≪ p ≪ 1, thus improving on Cook and Dembo’s result in the case d = 3.

Proposition 1.19. Let p such that p = o(1) and log4 n = o(np2). Denote by vn = n2p2 log(1/p). For any t ≥ 1,

log P tr(Xd) ≥ tndpd ≤ −φn(t) + o(vn), where

φn(t) = inf Λ∗p(Y ) : tr(Y d) ≥ t(np)d,Y ∈ Hn0 .

The proof, as for the traces of Wigner matrices, rely on a truncation argument which enables us to lower the complexity of our function of interest and apply eﬃciently Proposition 1.5.

In [8, Theorem 1.5] (or [32, Theorem 1.1] for the case d = 3) the variational problem was solved asymptotically. They showed that for np ≫ 1,

- (1.11)

φn(t) vn −→

![image 85](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile85.png>)

n→+∞

Φ(t),

where Φ is given by,

- (1.12) Φ(t) =


min θt, 12(t − 1)d2 if p ≫ n−1/2,

![image 86](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile86.png>)

![image 87](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile87.png>)

- 1

![image 88](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile88.png>)

- 2(t − 1)d2 if n−1 ≪ p ≪ n−1/2,


![image 89](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile89.png>)

with θt the unique solution of the equation PCd(θt) = t, where PCd is the independence polynomial of the d-cycle. The optimizers correspond on one

hand to planting a clique of order np(t − 1)1/d, which gives the 12(t − 1)2/d term, and on the other hand to planting an anti-clique of order np2θt which corresponds to the other θt term.

![image 90](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile90.png>)

With this knowledge of the optimizers, one can obtain the complementary lower bound, so that together with Proposition 1.19, we get, for any t ≥ 1,

1 vn

log P tr(Xd) ≥ tndpd = −Φ(t),

lim

![image 91](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile91.png>)

n→+∞

for any n−1/2 log4 n ≪ p ≪ 1. The edge-probability n−1/2 appears to be critical for cycles in diﬀerent ways. Note that below this threshold, the anticlique construction is no longer available. Moreover, for this parameter, the

order at the exponential scale of the upper tail approaches n. From the point of view of the truncation method we are using, the speed n arises as being impassable (without further dimension reduction): the complexity of the gradient of a truncated trace is at least the one of the (n − 1)-dimensional sphere, as it corresponds to pick the top eigenvector.

Furthermore, the threshold n−1/2 is also critical in the sense that one observes a change of speed in the large deviation lower tail of cycles counts. Indeed, we know by the work of Janson,  Luczak and Rucin´sk [24], and Janson and Warnke [26], that in the regime where p = o(1), for any ﬁnite graph H, and any 0 < u ≤ 1,

log P(XH ≤ uEXH) ≍ −(1 − u)2ΦH,

where ΦH = min{EXJ : J sub-graph of H}. Thus, the speed of the lower tail is driven by the “least expected” sub-graph of H. For example for H = K3, this implies that,

log P(XH ≤ (1 − u)EXH) ≍ −u2 min(n3p3,n2p).

Thus a change of speed happens at n−1/2, and similarly for cycles of greater lengths.

In [14, Theorem 1.2], the authors provided sharp lower tail estimates of homomorphisms densities of d-cycles for sparsity parameters p ≫ n−c (up to logarithmic corrections), with c = 2(dd−−21). We mention also that an entropic perspective on the estimation of the lower tail of triangle counts has been announced by Kozma and Samotij [28] all the way down to p ≫ n−1/2.

![image 92](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile92.png>)

2. Nonlinear large deviation upper bounds. We give here a proof of the two Theorems 1.1 and 1.5.

Proof of Proposition 1.1. Let x,y ∈ K. We have by the mean-value theorem,

f(x) = f(x) − f(y) + Λ∗µ(y) + f(y) − Λ∗µ(y) ≤ sup

 ∇f(t),x − y + Λ∗µ(y) + sup z∈Rn

{f(z) − Λ∗µ(z)}.

t∈K

Denote by W the convex hull of ∇f(K) and hW its support function, that is, hW(y) = supλ∈W λ,y for any y ∈ Rn. With this notation, we get,

f(x) ≤ hW(x − y) + Λ∗µ(y) + sup z∈Rn

{f(z) − Λ∗µ(z)}.

Optimizing in y, we deduce that f(x) ≤ inf

{hW(x − y) + Λ∗µ(y)} + sup z∈Rn

{f(z) − Λ∗µ(z)},

y∈K

Using the minimax theorem (see [13, Theorem 4.36]), we have inf

{hW(x − y) + Λ∗µ(y)} = sup λ∈W

{ λ,x − y + Λ∗µ(y)}

inf

y∈K

y∈K

{ λ,x − Λµ(λ)},

= sup

λ∈W

where we used the fact that Λ∗µ(y) = +∞ if y ∈/ K by the Hahn-Banach theorem, and that Λµ is the Legendre transform of Λ∗µ by [13, Theorem 4.21]. Therefore,

Thus,

{f(z) − Λ∗µ(z)}.

f(x) ≤ sup

{ λ,x − Λµ(λ)} + sup z∈Rn

λ∈W

- (2.1) log efdµ ≤ log esupλ∈W{ λ,x −Λµ(λ)}dµ(x) + sup


{f(z) − Λ∗µ(z)}

z∈Rn

Note that ∇Λµ(Rn) ⊂ K since any point in ∇Λµ(Rn) is a barycenter of a probability measure supported on K by (1.2). Therefore, for any x ∈ K, the function λ  → λ,x  − Λµ(λ) is D-Lipschitz with respect to the ℓ2-norm. Let now δ > 0 and let Dδ be a δ/D-net of V . Then,

log esupλ∈W{ λ,x −Λµ(λ)}dµ(x) ≤ δ + log esupλ∈Dδ{ λ,x −Λµ(λ)}dµ(x).

Using a union bound, we get

log esupλ∈Dδ{ λ,x −Λµ(λ)}dµ(x) ≤ log |Dδ|,

which yields the claim.

![image 93](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile93.png>)

![image 94](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile94.png>)

![image 95](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile95.png>)

![image 96](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile96.png>)

Remark 2.1. In the case suppµ ⊂ [0,1]n, one can get a potentially better bound by using not a net for the ℓ2-norm but for the ℓ1-norm instead. Indeed, for any i ∈ {1,... ,n}, and λ ∈ Rn,

∂iΛ(λ) = x,ei dµy(x),

with y = ∇Λ(λ) and µy is deﬁned in (1.1). Therefore, if suppµ ⊂ [0,1]n, ∂iΛ(λ) ∈ [0,1]. Thus, for ﬁxed x ∈ suppµ, the function λ  → λ,x − Λµ(λ) is 1-Lipschitz w.r.t the ℓ1-norm. In the last step (2.1) of the proof of Proposition 1.1, if one takes δ > 0 and Fδ to be a δ-net for the ℓ1-norm, one obtains,

log esupλ∈V { λ,x −Λµ(λ)}dµ(x) ≤ δ + log |Fδ|.

This yields an error term in the approximation of the partition function getting closer to the one recently found in [4, Proposition 5.1] as a consequence of a structural result on probability measures on product spaces.

Remark 2.2. As observed in Remark 1.4, we see that the above proof of Proposition 1.1 yields an approximation of the partition function which seems a bit oﬀ from the one Lemma 1.3 proposes.

In general, it is expected that when f has a gradient of low complexity, this gap becomes negligible, that is, for any y in an appropriate level set of Λ∗µ,

fdµy ≃ f(y),

where µy is deﬁned in (1.1). Indeed, if µ is the n-fold product measure νn, with ν compactly supported for example, we note that by the mean-value theorem, we have,

fdµy − f(y) ≤ sup t∈K

| ∇f(t),x − y |dµy(x),

where K denotes the convex hull of the support of µ. But, as µy has barycenter y, and is also a product measure with marginals having the same support as the one of ν, we can deduce by the Majorization Theorem (see [31, Theorem 12.16]),

 ∇f(t),x dγn(x),

fdµy − f(y) ≤ c sup t∈K

where c is a positive constant depending on the diameter of the support of ν, and γn is the standard Gaussian measure on Rn.

We now turn our attention to the proof of Theorem 1.5. As the “rate function” we are aiming for, is not a priori convex, we cannot restrict ourselves to estimate the logarithmic Laplace transform of f(X), and use the previous Theorem 1.1. We will actually refrain ourselves from using Chebytchev’s inequality, and prefer to work directly on the probability of deviations, in

contrast with the path followed by Chatterjee and Dembo in [11, section 4, proof of Theorem 1.1].

Proof of Theorem 1.5. To ease the notation, we write Λ, Λ∗ as shorthands for Λµ and Λ∗µ respectively. The key element of this upper bound is a deterministic result which translates the event where f(X) ∈/ Vδ({I ≤ r}) into a large deviation event for the process,

θλ,X − Λ(θλ) θ>0,λ∈W.

The bound of Theorem 1.5 is then obtained by using a net-argument and a union bound to control the deviations of the above process.

Fix κ ≥ r > 0. Denote by K = {Λ∗ ≤ κ}. In a ﬁrst step, we translate in a

more geometric language the event where X ∈ K and f(X) ∈/ Vδ({I ≤ r}), which is the object of the following lemma.

Lemma 2.3. Let x ∈ K. If f(x) ∈/ Vδ({I ≤ r}), then inf

Λ∗(x − z) ≥ r,

z∈δW◦

where W◦ is the polar set of W, that is, denoting by hW(z) = supλ∈W λ,z for z ∈ Rn the support function of W,

W◦ = z ∈ Rn, hW(z) ≤ 1 .

Observe that since Theorem 1.5 is only relevant when W is a small set in terms of complexity, its polar δW◦ can be thought as a large or typical set. The above lemma quantiﬁes the fact that when f(x) ∈/ Vδ({I ≤ r}), x is far away from δW◦ with respect to the cost function Λ∗.

Proof. Let x ∈ K. By deﬁnition of I, for any y ∈ Rn such that Λ∗(y) ≤ r, we have I(f(y)) ≤ r. Therefore, if f(x) ∈/ Vδ({I ≤ r}), then

|f(x) − f(y)| ≥ δ.

inf

Λ∗(y)≤r

Since κ ≥ r, we deduce from the assumption (1.5) that for any y ∈ Rn such that Λ∗(y) ≤ r,

λ,x − y . Therefore, we have

|f(x) − f(y)| ≤ sup

λ∈W

- (2.2) inf Λ∗(y)≤r


sup

λ∈W

λ,x − y ≥ δ.

Let z ∈ δW◦ and assume that Λ∗(x − z) < r. By continuity of hW and the continuity of Λ∗ on its domain, we can assume hW(z) < δ. Using the above inequality (2.2) for y = x − z we get that hW(x − y) = hW(z) ≥ δ, which yields a contradiction. Therefore,

Λ∗(x − z) ≥ r.

inf

z∈δW◦

![image 97](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile97.png>)

![image 98](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile98.png>)

![image 99](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile99.png>)

![image 100](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile100.png>)

As one can observe, Lemma 2.3 involves a convex optimization problem. A speciﬁc feature of such an optimization problem is that it admits a dual concave optimization problem, which is linked through its multipliers to the initial problem. Using this duality, we obtain the following lemma.

Lemma 2.4. Let x ∈ K and θ0 = κ/δ. Then, inf

Λ∗(x − z) ≤ sup

{ θλ,x − Λ(θλ) − θδ},

z∈δW◦

0≤θ≤θ0 λ∈Wθ

where for any θ > 0,

- (2.3) Wθ = λ ∈ W : θλ ∈ int(DΛ), ∇Λ(θλ) ∈ K . Proof. Since Λ∗(x) ≤ κ and 0 ∈ δW◦, we obtain by taking z = 0, that
- (2.4) inf z∈δW◦

Λ∗(x − z) ≤ κ < +∞.

As δW◦ is a closed set and Λ∗ has compact level sets by [17, Lemma 2.2.31], the inﬁmum is achieved at some z∗ ∈ δW◦.

Since Λ∗ and hW are both convex functions, we deduce by Kuhn-Tucker Theorem (see [13, Theorem 9.4]) that there exists (η,θ) = (0,0) with η ∈ {0,1} and θ ≥ 0, such that θ(hW(z∗) − δ) = 0, and

- (2.5) ηΛ∗(x − z∗) = inf ηΛ∗(x − z) + θ(hW(z) − δ) : z ∈ Rn .


Evaluating the function on the right-hand side at z = 0, we obtain that ηΛ∗(x − z∗) ≤ −θδ. Therefore, the non-triviality condition (η,θ) = (0,0) implies that η = 1. By (2.4), we know that x − z∗ ∈ DΛ∗. We claim that further:

Fact 2.5. x − z∗ lies in the interior of DΛ∗.

The intuition behind this fact is that the gradient of Λ∗ blows up around the frontier of its domain whereas the “penalization function” hW remains Lipschitz, so that it can only be beneﬁcial for the minimum to lie in the interior of DΛ∗. We now make this idea rigorous and prove formally Fact

- 2.5.


Proof. Note ﬁrst that the barycenter of µ, which we denote by m, is in the interior of DΛ∗. Indeed, by Jensen’s inequality,

![image 101](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile101.png>)

- (2.6) ∀λ ∈ Rn, Λ(λ) ≥ λ,m . Therefore, Λ∗(m) ≤ 0. Since Λ∗ ≥ 0, we deduce that Λ∗(m) = 0 and in consequence 0 ∈ ∂Λ∗(m). As Λ is strictly convex and essentially smooth, Λ∗ is also strictly convex and essentially smooth by [34, Theorem 26.5]. In particular, Λ∗ is diﬀerentiable on int(DΛ∗) and steep, so that any point with a nonempty subdiﬀerential should lie in int(DΛ∗). Therefore m ∈ int(DΛ∗).

![image 102](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile102.png>)

![image 103](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile103.png>)

![image 104](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile104.png>)

![image 105](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile105.png>)

![image 106](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile106.png>)

To prove that x − z∗ ∈ int(DΛ), we argue by contradiction. We will show that if x − z∗ lies on the frontier of DΛ∗, denoted by fr(DΛ∗), then using the fact that Λ∗ is steep, we can ﬁnd a barycenter of m and x − z∗ at which the cost function in the optimization problem (2.5) is smaller than at x−z∗, thus violating the optimality of x−z∗. Assume now that x−z∗ ∈ fr(DΛ∗). Then, by [34, Theorem 6.1], we deduce that for any t ∈ (0,1], x−z∗−tu ∈ int(DΛ∗), where u = x − z∗ − m, as we are taking a barycenter between an interior point and a frontier point of a convex set. Deﬁne

![image 107](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile107.png>)

![image 108](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile108.png>)

- (2.7) ∀z ∈ Rn, F(z) = Λ∗(x − z) + θhW(z).


For any t > 0, there exists ζt ∈ W such that hW(z∗)−hW(z∗+tu) ≥ −t ζt,u . Using the convexity of Λ∗ we get,

F(z∗) ≥ F(z∗ + tu) +  ∇Λ∗(vt) − θζt,tu ,

where vt = x − z∗ − tu. Besides, Λ∗ is strictly convex and therefore achieves its unique minimum at m where Λ∗(m) = 0. Thus for any t < 1, Λ∗(vt) > 0. Since vt = m+(1−t)u, we deduce by convexity of Λ∗ that  ∇Λ∗(vt),u > 0 for any t < 1. But W is a bounded set, therefore ζt remains bounded as t ∈ (0,1]. Since Λ∗ is steep, we deduce that for t close enough to 0,

![image 109](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile109.png>)

![image 110](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile110.png>)

![image 111](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile111.png>)

 ∇Λ∗(vt) − θζt,u > 0, which gives the desired contradiction.

![image 112](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile112.png>)

![image 113](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile113.png>)

![image 114](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile114.png>)

![image 115](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile115.png>)

Since z∗ is a global minimum of the function F deﬁned in (2.7), we have

- 0 ∈ ∂F(z∗). From Fact 2.5, we know that x − z∗ is an interior point of DΛ∗. As Λ∗ is diﬀerentiable on int(DΛ∗), we have 0 ∈ {−∇Λ∗(x−z∗)}+θ∂hW(z∗) by [13, Theorem 4.10]. By Danskin’s formula (see [13, Theorem 10.22]), the subdiﬀerential of the support function hW, is


∂hW(z) = {λ∗ ∈ W : hW(z) = λ∗,z }. Thus, there is a λ ∈ W satisfying δ = λ,z∗ such that,

- (2.8) ∇Λ∗(x − z∗) = θλ. Therefore,

Λ∗(x − z∗) = θλ,x − z∗ − Λ(θλ) = θλ,x − Λ(θλ) − θδ.

Note that θ and λ depends on x in an implicit way. However, we will show that θ and λ can be restricted to certain subsets uniformly in x such that Λ∗(x) ≤ κ. More precisely, we will prove that θ ≤ κ/δ and λ ∈ Wθ, with Wθ deﬁned in (2.3), thus ending the proof of Lemma 2.4. We start with the bound on θ. Using the convexity of Λ∗, we have,

Λ∗(x) − Λ∗(x − z∗) ≥  ∇Λ∗(x − z∗),z∗ .

Using that λ,z∗ = δ and that Λ∗ is non-negative, we get Λ∗(x) ≥ θδ. Since Λ∗(x) ≤ κ, we obtain that θ ≤ κ/δ. To prove that λ ∈ Wθ, we use the fact that ∇Λ and ∇Λ∗ are inverse maps and (2.4) to deduce that

Λ∗(∇Λ(θλ)) = Λ∗(x − z∗) ≤ Λ∗(x) ≤ κ, which ﬁnally ends the proof.

![image 116](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile116.png>)

![image 117](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile117.png>)

![image 118](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile118.png>)

![image 119](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile119.png>)

Combining Lemmas 2.3 and 2.4, we obtain that if x ∈ K and f(x) ∈/ Vδ({I ≤ r}), then

- (2.9) sup


{ θλ,x − Λ(θλ) − θδ} ≥ r,

0≤θ≤θ0 λ∈Wθ

where Wθ is deﬁned in (2.3) for any θ > 0. In order to be allowed to take the probability of this event, we check the measurability of the supremum appearing in the above inequality.

Fact 2.6. The function x ∈ Rn  → sup0≤θ≤θ0

{ θλ,x − Λ(θλ) − θδ} is measurable.

λ∈Wθ

Proof. Since (θ,λ)  → θλ,x − Λ(θλ) − θδ is a continuous function, it suﬃces to prove that the subset

{θ} × Wθ,

A :=

θ≤θ0

is separable in the sense that it contains a dense subset. Observe that A is a bounded set since Wθ ⊂ W for any θ ≥ 0 and W is bounded by assumption. Therefore its closure, cl(A), is compact. This entails that A is pre-compact, and in consequence that it is separable.

![image 120](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile120.png>)

![image 121](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile121.png>)

![image 122](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile122.png>)

![image 123](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile123.png>)

Deﬁne now the measure,

PK = P(. ∩ {X ∈ K}). From (2.9), we have the upper bound,

- (2.10) PK f(X) ∈/ Vδ({I ≤ r}) ≤ PK sup 0≤θ≤θ0


{ θλ,X −Λ(θλ)−θδ} ≥ r .

λ∈Wθ

In a last step, we control the deviations of the supremum of the process appearing in the right-hand side of (2.10) using a net argument and performing a union bound.

Lemma 2.7. Let D denote the diameter of K. Let Dδ/2 be a δ/2D-net for the ℓ2-norm of W. Then,

log PK sup

0≤θ≤θ0 λ∈Wθ

{ θλ,X −Λ(θλ)−θδ} ≥ r ≤ −r+log |Dδ/2|+log

κLD δ ∨1 +1,

![image 124](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile124.png>)

where θ0 = κ/δ, L = supλ∈W ||λ||ℓ2 and for any θ ≥ 0, Wθ = λ ∈ W : θλ ∈ int(DΛ), ∇Λ(θλ) ∈ K .

Proof. We start by a net argument on θ. For x ∈ K ﬁxed, deﬁne the function

G : θ ∈ R+  → sup

{ θλ,x − Λ(θλ) − θδ}.

λ∈Wθ

We claim that for any θ′ ≤ θ,

- (2.11) G(θ′) − G(θ) ≤ (θ − θ′)LD. We observe ﬁrst the following fact on the monotonicity of the sets Wθ.

Fact 2.8. The family (Wθ)θ≥0 is non-increasing for the inclusion.

Proof. Let θ ≥ 0 and λ ∈ Wθ. Since K = {Λ∗ ≤ κ}, it means that θλ ∈ int(DΛ∗) and Λ∗(∇Λ(θλ)) ≤ κ. We know by (2.6) that m ∈ ∂Λ(0). Since Λ is essentially smooth and Λ has a non-empty subdiﬀerential at 0, the point 0 must lie in the interior of DΛ. Since by [34, Theorem 6.2], int(DΛ) is a convex set, we deduce that for any 0 ≤ θ′ ≤ θ, θ′λ ∈ int(DΛ). In addition, for any θ′ ≤ θ we can compute

![image 125](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile125.png>)

∂ ∂θ′

![image 126](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile126.png>)

Λ∗(∇Λ(θ′λ)) =  ∇Λ∗(∇Λ(θ′λ)),∇2Λ(θ′λ).λ

= θ′ λ,∇2Λ(θ′λ).λ ≥ 0,

where we used the fact that ∇Λ and ∇Λ∗ are inverse maps from one another. Thus, we can conclude that for any θ′ ≤ θ, Λ∗(θ′λ) ≤ Λ∗(θλ) ≤ κ, and therefore λ ∈ Wθ′.

![image 127](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile127.png>)

![image 128](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile128.png>)

![image 129](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile129.png>)

![image 130](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile130.png>)

We now prove (2.11). Let θ′ ≤ θ. By convexity of Λ, we get for any λ ∈ Wθ, θλ,X − Λ(θ′λ) − θ′λ,X − Λ(θ′λ) ≤ (θ − θ′) λ,∇Λ(θ′λ) − X .

Since Wθ ⊂ Wθ′ by Fact 2.8, we have ∇Λ(θ′λ) ∈ K. As we denoted by D the diameter of K, we obtain

θλ,X − Λ(θ′λ) − θ′λ,X − Λ(θ′λ) ≤ (θ − θ′)LD, which holds for any θ′ ≤ θ and λ ∈ Wθ ⊂ Wθ′. This yields the claim (2.11).

Let E be a 1/(LD)-net of the interval [0,θ0]. One can ﬁnd a net E such that,

- (2.12) |E| ≤ LDθ0 ∨ 1 =


κLD δ ∨ 1.

![image 131](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile131.png>)

For any θ ∈ [0,θ0], one can ﬁnd θ′ ∈ E, such that 0 ≤ θ − θ′ ≤ 1/LD. From

- (2.11), we deduce that


G(θ′) + 1.

G(θ) ≤ sup

sup

θ′∈E

θ∈[0,θ0]

Thus, using a union bound, we get, PK sup

{ θλ,X − Λ(θλ) − θδ} ≥ r

0≤θ≤θ0 λ∈Wθ

≤

- (2.13) { θλ,X − Λ(θλ) − θδ} ≥ r − 1 .

Let us now ﬁx θ ∈ E and perform a net argument on λ ∈ Wθ. Fix x ∈ K and deﬁne the function H taking values in R ∪ {−∞},

H : λ ∈ Rn  → θλ,X − Λ(θλ). We claim that for any λ,λ′ ∈ Wθ,

- (2.14) H(λ) − H(λ′) ≤ θD||λ − λ′||. Indeed, by convexity of Λ, we have for λ,λ′ ∈ Wθ,


PK sup

λ∈Wθ

θ∈E

H(λ) − H(λ′) ≤ θ λ − λ′,x − ∇Λ(θλ′) . Since λ′ ∈ Wθ, we have ∇Λ(θλ′) ∈ K, which yields (2.14).

Let F be a δ/D-net for the ℓ2-norm of Wθ such that F ⊂ Wθ. Using

- (2.14) we obtain that

sup

λ∈Wθ

H(λ) ≤ sup

λ′∈F

H(λ′) + θδ.

Therefore, PK sup

λ∈Wθ

{ θλ,X −Λ(θλ)} ≥ r−1+θδ ≤ PK sup λ∈F

{ θλ,X −Λ(θλ)} ≥ r−1 .

Performing a union bound we get, P sup

λ∈F

{ θλ,X − Λ(θλ)} ≥ r − 1 ≤ |F|e−r+1,

where we used the fact that for any ξ ∈ Rn, and t ≥ 0,

P( ξ,X − Λ(ξ) ≥ t) ≤ e−t, by Chernoﬀ’s inequality. Therefore,

- (2.15) PK sup λ∈Wθ


{ θλ,X − Λ(θλ)} ≥ r − 1 + θδ ≤ |F|e−r+1.

It remains now to show that we can ﬁnd a δ/D-net F of Wθ such that F ⊂ Wθ and relate its cardinal to the one of a net of W. For any A ⊂ Rn and r > 0 we denote by N(A,rBℓ2) and N(A,rBℓ2) the following covering numbers

![image 132](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile132.png>)

N(A,rBℓ2) = min N ∈ N : ∃x1,... ,xN ∈ Rn,A ⊂

N

Bℓ2(xi,r) ,

i=1

![image 133](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile133.png>)

N(A,rBℓ2) = min N ∈ N : ∃x1,... ,xN ∈ A,A ⊂

N

Bℓ2(xi,r) .

i=1

While it is true that the ﬁrst notion of covering number N(A,rBℓ2) is nondecreasing in A for the inclusion, this fact becomes wrong for N(A,rBℓ2). When A is convex, it is known (see [2, Fact 4.1.4]) that both covering numbers deﬁned above coincide. Unfortunately, we cannot prove in general that Wθ is convex. But, up to loose a factor 2 in the mesh of the net, we have the following fact:

![image 134](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile134.png>)

Fact 2.9. Let A ⊂ B ⊂ Rn and r > 0. Then, N(A,rBℓ2) ≤ N(B,(r/2)Bℓ2). Proof. For any A ⊂ Rn and r > 0, let M(A,rBℓ2) be the separation

![image 135](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile135.png>)

number deﬁned as

M(A,rBℓ2) = max N ∈ N : ∃x1,... ,xN ∈ A, ∀i = j,||xi − xj|| ≥ r .

Let A ⊂ B ⊂ Rn. We know by [2, Fact 4.1.11] that N(A,rBℓ2) ≤ M(A,rBℓ2). Since A ⊂ B,

![image 136](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile136.png>)

- M(A,rBℓ2) ≤ M(B,rBℓ2).

Using again [2, Fact 4.1.11], we have

- M(B,rBℓ2) ≤ N(B,(r/2)Bℓ2),


which ends the proof.

![image 137](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile137.png>)

![image 138](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile138.png>)

![image 139](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile139.png>)

![image 140](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile140.png>)

Let Dδ/2 be a δ/2D-net for the ℓ2-norm of W. As Wθ ⊂ W, we deduce from Fact 2.9 that there exists a δ/D-net F of Wθ for the ℓ2-norm such that F ⊂ Wθ and |F| ≤ |Dδ/2|. From the two union bounds (2.13) and (2.15), we obtain

log PK sup

0≤θ≤θ0 λ∈Wθ

{ θλ,X − Λ(θλ) − θδ} ≥ r ≤ log |E| + log |F| − r + 1.

Since |E| ≤ (κLD/δ) ∨ 1 by (2.12) and |F| ≤ |Dδ/2|, we deduce that log PK sup

{ θλ,X − Λ(θλ) − θδ} ≥ r

0≤θ≤θ0,λ∈Wθ

κLD

δ ∨ 1 + 1, whih ends the proof.

≤ −r + log |Dδ/2| + log

![image 141](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile141.png>)

![image 142](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile142.png>)

![image 143](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile143.png>)

![image 144](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile144.png>)

![image 145](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile145.png>)

To ﬁnalize the proof, we choose κ ≥ r such that P(X ∈/ K) ≤ e−r. Using

- (2.10) and Lemma 2.7, we obtain P f(X) ∈/ Vδ({I ≤ r}) ≤ PK f(X) ∈/ Vδ({I ≤ r}) + e−r

≤

κLD

![image 146](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile146.png>)

δ |Dδ/2|e−r+1 + e−r ≤

2κLD

![image 147](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile147.png>)

δ |Dδ/2|e−r+1, which gives us the claim.

![image 148](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile148.png>)

![image 149](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile149.png>)

![image 150](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile150.png>)

![image 151](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile151.png>)

3. Large deviation of traces of Wigner matrices. In this section, we will give a proof of Theorem 1.15 and Corollary 1.17.

3.1. Large deviation upper bound. We start with the large deviation upper bound of Theorem 1.15. The strategy for this upper bound will be similar to the one we adopted to investigate the large deviations of the moments of β-ensembles in [3, section 3]. It consists in truncating the spectrum so as to reduce ourselves to study the deviations of a small fraction of the eigenvalues. Once this truncation made, we will be able to use eﬃciently Theorem 1.5.

We introduce some notation we will use throughout this section. Let Y ∈ Hn. For any k ∈ {1,... ,n}, we denote by tr[k]Y the truncated trace:

- (3.1) tr[k]Y =


k

λi(Y ),

i=1

where λ1(Y ),... ,λn(Y ) are the eigenvalues of Y in non-increasing order. For any measurable function f : R → R, we deﬁne f(Y ) by functional calculus as the Hermitan matrix,

n

f(λi(Y ))uiu∗i ,

f(Y ) =

i=1

where u1,... ,un are the eigenvectors of Y associated to λ1(Y ),... ,λn(Y ). We now deﬁne, for d even,

tr[k](Y/√n)d, whereas for d odd,

1 n

![image 152](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile152.png>)

- (3.2) fk(Y ) =


![image 153](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile153.png>)

fk(Y ) =

tr[k](Y+/√n)d −

1 n

![image 154](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile154.png>)

![image 155](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile155.png>)

tr[k](Y−/√n)d.

1 n

![image 156](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile156.png>)

![image 157](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile157.png>)

The ﬁrst step toward the proof of the upper bound is the following lemma, which will rely on concentration arguments.

Lemma 3.1. Assume X is a Wigner matrix satisfying the convex concentration property. Let k ∈ {1,... ,n} such that n

1

d−1 = o(k) and k = o(n). For any t > 0,

![image 158](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile158.png>)

1 n1+d2

log P

lim

![image 159](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile159.png>)

n→+∞

![image 160](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile160.png>)

tr(X/√n)d − fk(X) − µsc(xd) > t = −∞.

1 n

![image 161](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile161.png>)

![image 162](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile162.png>)

3.1.1. Concentration inequalities. In order to prove Lemma 3.1, we will develop some deviations inequalities for the number of eigenvalues falling outside an interval and for truncated linear statistics of Hermitian random matrices satisfying the convex concentration property deﬁned in 1.13. The proof of these inequalities will follow the now classical path laid by the work of Guionnet and Zeitouni in [21].

Proposition 3.2. Let X be a random Hermitian matrix satisfying the convex concentration property for some constant c > 0. Let k ∈ {1,... ,n} and let f : R → R be a convex 1-Lipschitz function which achieves its inﬁmum on R. For any t > 0,

ct2 k

P tr[k]f(X) − Etr[k]f(X) > t ≤ c−1 exp −

![image 163](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile163.png>)

where tr[k] is the truncated trace deﬁned in (3.1).

,

In order to apply our convex concentration property, we need to prove that the truncated linear statistics are convex Lipschitz functions of the entries. This is the object of the following lemma.

- Lemma 3.3. Let f : R → R be a convex function which achieves its


inﬁmum on R. Let k ∈ {1,... ,n}. The function Tf deﬁned by, ∀X ∈ Hn, Tf(X) = tr[k]f(X),

is convex. Moreover, if f is 1-Lipschitz, then Tf is √

![image 164](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile164.png>)

k-Lipschitz with respect to the Hilbert-Schmidt norm.

Proof. The proof is a variation around the one of Klein’s lemma (see [1,

- Lemma 4.4.12]). Since f achieves its inﬁmum, we know that there exists x0 such that 0 ∈ ∂f(x0). Considering f˜ = f(. + x0) − f(x0), we may and will assume that x0 = 0 and f(0) = 0. We will show the following representation of Tf as supremum of aﬃne functions.


Lemma 3.4. Let f : R → R be a convex function. Assume f(0) = 0 and

- 0 ∈ ∂f(0). Let ζ : R → R be a function such that, ∀x ∈ R, ζ(x) ∈ ∂f(x), and ζ(0) = 0.


Then, for any X ∈ Hn,

- (3.3) Tf(X) = sup rankY ≤k

{trf(Y ) + trζ(Y )(X − Y )}.

Moreover, if f is 1-Lipschitz, then Tf is √

![image 165](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile165.png>)

k-Lipschitz with respect to the Hilbert-Schmidt norm.

Proof. First, we know by [34, Theorem 23.4] that for every x ∈ R, ∂f(x) = ∅, which justiﬁes the existence of ζ. Let λ1,... ,λn be the eigenvalues of X such that f(λ1) ≥ ... ≥ f(λn). Let u1,... ,un be the associated eigenvectors. Note that because we assumed f(0) = 0, then if we take Y = ki=1 λiuiu∗i , we get the equality,

Tf(X) = trf(Y ) + trζ(Y )(X − Y ),

using the orthogonality of the eigenvectors. Therefore only the inequality is left to prove. Let Y ∈ Hn with rank less that k, and denote by e1,... ,en an orthonormal basis of eigenvectors such that ek+1,... ,en are in the kernel, and by µ1,... ,µk the eigenvalues associated to e1,... ,ek. From the convexity of f, we have for any j ∈ {1,... ,n}, i ∈ {1,... ,k},

f(λj) ≥ f(µi) + ζ(µi)(λj − µi).

Multiplying the above inequality by | uj,ei |2, and summing over j ∈ {1,... ,n}, we get

- (3.4)


n

| uj,ei |2f(λj) ≥ f(µi) +

j=1

n

| uj,ei |2ζ(µi)(λj − µi).

j=1

Writing the trace of f′(Y )(X − Y ) in the basis of the ei’s, we have

n

ei,ζ(Y )(X − Y )ei

trζ(Y )(X − Y ) =

i=1

n

ζ(Y )ei,(X − Y )ei

=

i=1

k

ζ(Y )ei,(X − Y )ei ,

=

i=1

where we used the fact that ζ(0) = 0. Finally, using the spectral decomposition of X, we get

k

trζ(Y )(X − Y ) =

i=1

n

| uj,ei |2ζ(µi)(λj − µi).

j=1

Summing (3.4) now over i ∈ {1,... ,k}, we deduce, writing αj = ki=1 | uj,ei |2, that n

αjf(λj) ≥ trf(Y ) + trζ(Y )(X − Y ).

j=1

Observe that αj ∈ [0,1] and j αj = k. The maximum max{

αj = k},

αjf(λj) : αj ∈ [0,1],

j

j

is achieved at the vector α = 1J, where J is the set of indices j corresponding to the k highest values of f(λj). This shows that the representation (3.3) holds, and that Tf is a convex function.

Assume further that f is 1-Lipschitz. This entails that |ζ(x)| ≤ 1 for any x ∈ R. Consequently, ||ζ(Y )||2 ≤

√

![image 166](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile166.png>)

k for any Y ∈ Hn with rank(Y ) ≤ k. We conclude from the representation (3.3) that Tf is

√

![image 167](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile167.png>)

k-Lipschitz w.r.t the Hilbert-Schmidt norm.

![image 168](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile168.png>)

![image 169](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile169.png>)

![image 170](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile170.png>)

![image 171](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile171.png>)

As a consequence of Proposition 3.2, we get the following deviation estimate on the number of eigenvalues present outside the bulk.

Proposition 3.5. Let X be a random Hermitian matrix satisfying the convex concentration property with constant c > 0. Denote by λ1(X) its top eigenvalue and ||X|| its operator norm. For any M ≥ 4E(λ1(X))+, and

- 1 ≤ k ≤ n,


cM2k 16

P N[M,+∞) ≥ k ≤ c−1 exp −

,

![image 172](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile172.png>)

where for any I ⊂ R, N(I) denotes the number of eigenvalues of X in I. As a consequence, for any M ≥ 4E||X|| and 1 ≤ k ≤ n,

cM2k 32

P N (−M,M)c ≥ k ≤ 2c−1 exp −

.

![image 173](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile173.png>)

Proof. Let f(x) = M2 (x − M/2)+ for any x ∈ R. Since f(x) ≥ 1 for x ≥ M, we have, denoting by λ1(X),... ,λn(X) the eigenvalues of X in non-increasing order,

![image 174](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile174.png>)

P N[M,+∞) ≥ k ≤ P

k

f(λi(X)) ≥ k .

i=1

But

E

k

f(λi(X)) ≤

i=1

2 M

k 2

kE(λ1(X))+ ≤

,

![image 175](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile175.png>)

![image 176](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile176.png>)

for M ≥ 4E(λ1(X))+. Thus,

P N[M,+∞) ≥ k ≤ P

k

k

f(λi(X)) − E

i=1

i=1

f(λi(X)) ≥ k/2 .

Applying Proposition 3.2, we deduce that

2 16 , which gives the ﬁrst claim.

- (3.5) P N[M,+∞) ≥ k ≤ c−1e−ckM


![image 177](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile177.png>)

Since by deﬁnition ⌈k/2⌉ − 1 < k/2, we have using a union bound,

P N (−M,M)c ≥ k ≤ P N(−∞,−M] ≥ ℓ + P N[M,+∞) ≥ ℓ , where ℓ = ⌈k/2⌉. For any M ≥ 4E||X||, we obtain by applying inequality

- (3.5) to X and −X alternatively,


2 32 , which gives the second claim.

P N (−M,M)c ≥ k ≤ 2c−1e−ckM

![image 178](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile178.png>)

![image 179](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile179.png>)

![image 180](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile180.png>)

![image 181](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile181.png>)

![image 182](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile182.png>)

3.1.2. An exponential equivalent. In this section, we apply the concentration inequalities we obtained in the previous section to give a proof of the exponential equivalent of Lemma 3.1.

1

Proof of Lemma 3.1. Let k such that n

d−1 = o(k) and k = o(n). We will prove the claim only in the case where d is even, the case where d is odd being almost the same. Let M > 0, and deﬁne the truncated power function, by fM(x) = xd for |x| ≤ M, and for |x| > M by,

![image 183](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile183.png>)

fM(x) = dMd−1(|x| − M) + Md,

Let λ∗1,... ,λ∗n be the eigenvalues of X/√n in decreasing absolute values. We can write,

![image 184](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile184.png>)

n

fM(λ∗i ) = trfM(X/√n) − tr[k]fM(X/√n).

![image 185](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile185.png>)

![image 186](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile186.png>)

i=k+1

As fM(./√n) is dMd−1/√n-Lipschitz, applying Proposition 3.2 alternatively to trfM(X/√n) and tr[k]fM(X/√n), and performing a union bound, we deduce that for any t > 0,

![image 187](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile187.png>)

![image 188](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile188.png>)

![image 189](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile189.png>)

![image 190](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile190.png>)

- (3.6)


n

n

cn2t2

fM(λ∗i ) − E

fM(λ∗i ) > tn ≤ 2c−1 exp −

4d2M2(d−1) , where we used the fact that k ≤ n. On one hand,

P

![image 191](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile191.png>)

i=k+1

i=k+1

n

n

n

λ∗id − E

|λ∗i |d1|λ∗

fM(λ∗i ) ≤ E

E

i |≥M

i=1

i=k+1

i=k+1

Etr|X/√n|d+1. Using twice Cauchy-Schwarz inequality, we get

1 M

![image 192](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile192.png>)

≤

![image 193](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile193.png>)

tr(X/√n)2(d+1) where we used in the last equality [1, Lemma 2.1.6]. Therefore,

Etr|X/√n|d+1 ≤ E

tr(X/√n)2(d+1)

- 1


1 n

1 n

- 1

![image 194](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile194.png>)

- 2 ≤ E


![image 195](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile195.png>)

![image 196](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile196.png>)

![image 197](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile197.png>)

![image 198](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile198.png>)

![image 199](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile199.png>)

![image 200](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile200.png>)

n

- 1

![image 201](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile201.png>)

- 2 = O(1),


n

n

λ∗id − E

fM(λ∗i ) = O

E

i=k+1

i=k+1

n M

![image 202](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile202.png>)

.

On the other hand,

n

λ∗id − Etr(X/√n)d| ≤ kE||X/√n||d = O(k),

![image 203](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile203.png>)

![image 204](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile204.png>)

|E

i=k+1

as E||X/√n||d = O(1) by [1, Exercice 2.1.27]. Therefore, if k = o(n) and M goes to inﬁnity with n, then as En1tr(X/√n)d converges to µsc(xd), we have,

![image 205](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile205.png>)

![image 206](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile206.png>)

![image 207](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile207.png>)

- (3.7) µsc(xd) − E

1 n

![image 208](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile208.png>)

n

i=k+1

fM(λ∗i) −→

n→+∞

0.

Fix t > 0. Now let M go to inﬁnity with n such that n1+2/d = o(n2/M2(d−1)), that is M2 = o(na) with a = (d − 2)/(d(d − 1)). The above inequality (3.6) and the convergence (3.7) give

- (3.8) lim n→+∞

1 n1+d2

![image 209](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile209.png>)

![image 210](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile210.png>)

log P

1 n

![image 211](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile211.png>)

n

i=k+1

fM(λ∗i ) − µsc(xd) > t = −∞.

But since E||X|| = O(√n) by [1, Exercice 2.1.29], we deduce from Proposition 3.5 that in order to have that

![image 212](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile212.png>)

- (3.9) lim n→+∞


log P N [−R√n,R√n]c ≥ k = −∞,

1 n1+d2

![image 213](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile213.png>)

![image 214](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile214.png>)

![image 215](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile215.png>)

![image 216](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile216.png>)

it is suﬃcient to take R going to +∞ with n such that n2/d = o(kR2). We assumed that n

1

d−1 = o(k), which is equivalent to say that, nd2 = o(kna). Therefore, we can ﬁnd M going to inﬁnity which satisﬁes both conditions, M2 = o(na), and nd2 = o(kM2).

![image 217](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile217.png>)

![image 218](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile218.png>)

![image 219](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile219.png>)

With this choice of M, both estimates (3.8), and (3.9) with R = M, hold. But then,

P

n

n

fM(λ∗i ) > tn ≤ P N([−M√n,M√n]c) ≥ k

λ∗i d −

![image 220](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile220.png>)

![image 221](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile221.png>)

i=k+1

i=k+1

Therefore,

1 n1+d2

log P

limsup

![image 222](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile222.png>)

n→+∞

![image 223](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile223.png>)

n

n

λ∗i d −

i=k+1

i=k+1

which together with (3.8) give the claim.

fM(λ∗i) > tn = −∞,

![image 224](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile224.png>)

![image 225](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile225.png>)

![image 226](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile226.png>)

![image 227](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile227.png>)

3.1.3. Proof of the large deviation upper bound. From Lemma 3.1, we see that it suﬃces to understand the large deviations of a truncated trace fk(X) deﬁned in (3.2), with n

1

d−1 = o(k), and k = o(n). The point is that this truncation lowers signiﬁcantly the complexity. Indeed, we will be able to encode by O(nk log n) bits the “gradient” of the truncated trace tr[k](Xd). Thus, Proposition 1.5 will give us a relevant upper bound, with respect to the speed n1+d2, as soon as we can take k log n = o(nd2). But, for d ≥ 3, we see that

![image 228](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile228.png>)

![image 229](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile229.png>)

![image 230](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile230.png>)

1 d − 1

2 d

<

.

![image 231](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile231.png>)

![image 232](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile232.png>)

1

Therefore, we can and will take k which satisﬁes both conditions n

d−1 = o(k) and k log n = o(nd2).

![image 233](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile233.png>)

![image 234](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile234.png>)

Property of the rate function I+. We begin with proving that the rate function I+ deﬁned in Theorem 1.15 is a good rate function. It will follow from the next lemma.

Lemma 3.6. Let cn : Rn → R+ and Fn : Rn → R be families of functions indexed by n ∈ N, such that for any r > 0, the subset

Fn({cn ≤ r}),

n∈N

is bounded. Then the functions deﬁned as, ∀x ∈ R, I(n)(x) = sup δ>0

inf

Im,δ(x),

m≥n

and

∀x ∈ R, I+(x) = sup δ>0

In,δ(x), with

liminf

n→+∞

Im,δ(x) = inf cm(h) : |Fm(h) − x| < δ,h ∈ Rm , are good rate functions.

Proof. Let τ > 0. We can write, for any x ∈ R, I(n)(x) ≤ τ ⇐⇒ ∀δ > 0, inf

Im,δ(x) ≤ τ ⇐⇒ ∀δ > 0,∀ε > 0,∃m ≥ n,Im,δ(x) < τ + ε. By deﬁnition of Im,δ, we get I(n)(x) ≤ τ ⇐⇒ ∀ε > 0,∀δ > 0,∃m ≥ n,∃h ∈ Rm,cm(h) < τ + ε,|Fm(h) − x| < δ.

m≥n

Thus,

![image 235](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile235.png>)

{I(n) ≤ τ} =

Fm {cm ≤ τ + ε} .

ε>0 m≥n

This yields that I(n) is a good rate function. As I+ = supn∈N I(n), we deduce that I+ is also a good rate function.

![image 236](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile236.png>)

![image 237](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile237.png>)

![image 238](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile238.png>)

![image 239](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile239.png>)

Let us now check that the assumptions of Lemma 3.6 are fulﬁlled in our setting. We ﬁrst show that X is sub-Gaussian in the sense that there exists C > 0 such that

- (3.10) ∀Y ∈ Hn, Λ∗(Y ) ≥


- 1

![image 240](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile240.png>)

- 2C2


tr(Y 2).

Applying the convex concentration property deﬁned in 1.13, to the function f(X) = tr(XH) with H ∈ Hn ﬁxed, we obtain that for any t > 0,

ct2

P |tr(XH)| > t ≤ c−1e−

![image 241](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile241.png>)

tr(H2).

We deduce that Λ(H) ≤ C22tr(H2), which gives (3.10). But, using the fact that x ∈ R+  → x2/d is sub-additive, we have for any Y ∈ Hn, |tr(Y d)| ≤ tr(|Y |d) ≤ (tr(Y 2))d/2, so that whenever

![image 242](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile242.png>)

Λ∗(Y ) ≤ rn1+d2,

![image 243](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile243.png>)

for some r > 0, then we have |n1tr(Y/√n)d| ≤ (2C2r)d2. This shows that we can apply Lemma 3.6 with cn(Y ) = n−(1+d2)Λ∗(Y ) and Fn(Y ) = µsc(xd) + 1

![image 244](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile244.png>)

![image 245](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile245.png>)

![image 246](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile246.png>)

![image 247](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile247.png>)

ntr(Y/√n)d, and conclude that I+ is a good rate function.

![image 248](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile248.png>)

![image 249](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile249.png>)

Upper bound. We can now proceed with the proof of the upper bound. By [17, Theorem 4.2.13], it is suﬃcient to prove the large deviations upper bound for the sequence (fk(X))n∈N, as (µsc(xd)+fk(X))n∈N is exponentially equivalent to (n1tr(X/√n)d)n∈N by Lemma 3.1. We will ﬁrst make sure that the rate function we are going to obtain by applying Theorem 1.5 is the same as the one we are aiming for, that is:

![image 250](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile250.png>)

![image 251](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile251.png>)

Lemma 3.7. Assume that k goes to +∞ with n. For any n ∈ N, δ > 0, set

∀x ∈ R, Jn,δ(x) = inf

1 n1+d2

Λ∗(Y ) : |fk(Y ) − x| < δ,Y ∈ Hn ,

![image 252](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile252.png>)

![image 253](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile253.png>)

and let

J+ = sup δ>0

liminf

Jn,δ,

n→+∞

where fk is deﬁned in (3.2). For any x ∈ R,

I+(x + µsc(xd)) = sup δ>0

liminf

Jn,δ(x),

n→+∞

- where I+ is deﬁned as


∀x ∈ R, I+(x) = sup δ>0

In,δ(x), and for any n ∈ N, δ > 0,

liminf

n→+∞

Λ∗(Y ) n1+d2

tr(Y/√n)d − µsc(xd) − x| < δ,Y ∈ Hn .

1 n

![image 254](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile254.png>)

: |

In,δ(x) = inf

![image 255](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile255.png>)

![image 256](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile256.png>)

![image 257](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile257.png>)

Proof. We will prove that I+(. + µsc(xd)) and J+ have the same level sets. We will ﬁrst observe that if Y ∈ Hm is a non-negative matrix such that tr(Y 2) = O(m1+d2) then,

![image 258](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile258.png>)

- (3.11) tr(Y d) − tr[k](Y d) = o(m1+d2). Let λ1 ≥ ... ≥ λm ≥ 0 be the eigenvalues of Y . From the fact that tr(Y 2) =


![image 259](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile259.png>)

- O(m1+d2 ), we deduce that for any 1 ≤ ℓ ≤ m,


![image 260](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile260.png>)

λℓ ≤ ℓ−12O(m12+d1). Thus,

![image 261](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile261.png>)

![image 262](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile262.png>)

![image 263](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile263.png>)

λdℓ = O(m1+d2k1−d2),

tr(Y d) − tr[k](Y d) =

![image 264](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile264.png>)

![image 265](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile265.png>)

ℓ>k

which gives (3.11). Let now τ > 0 and x such that J+(x) ≤ τ. Let δ > 0. For any n ∈ N, we have,

Jm,δ(x) ≤ τ. Therefore,

inf

m≥n

Λ∗(Y ) m1+d2

: |fk(Y ) − x| < δ,Λ∗(Y ) ≤ 2τm1+2d

inf

Jm,δ(x) = inf

inf

![image 266](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile266.png>)

![image 267](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile267.png>)

m≥n

m≥n

Y ∈Hm

![image 268](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile268.png>)

For any m ∈ N and Y ∈ Hn such that Λ∗(Y ) ≤ 2τm1+2d, we know by (3.10) that

![image 269](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile269.png>)

tr(Y 2) ≤ 4C2τm1+d2.

![image 270](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile270.png>)

Applying the observation (3.11) to Y+ and Y− alternatively, we deduce that tr(Y d) − fk(Y ) = o(m1+d2). Therefore, for n large enough,

![image 271](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile271.png>)

Jm,δ(x) ≥ inf

inf

Im,2δ(x).

m≥n

m≥n

Therefore,

In,2δ(x) ≤ τ.

liminf

n→+∞

As the above inequality is true for any δ > 0, we obtain I+(x) ≤ τ. Inverting the roles of I+ and J+, we get the other inclusion.

![image 272](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile272.png>)

![image 273](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile273.png>)

![image 274](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile274.png>)

![image 275](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile275.png>)

We come back to the proof of the upper bound of Theorem 1.15. Let F be a closed subset of R. We want to prove that,

1 n1+d2

log P(fk(X) ∈ F) ≤ −inf

J+,

limsup

![image 276](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile276.png>)

F

n→+∞

![image 277](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile277.png>)

- where J+ is deﬁned in Lemma 3.7. We can assume without loss of generality that infF J+ > 0. Let r > 0 such that infF J+ > r. Put in another way,


F ∩ {J+ ≤ r} = ∅. As J+ is a good rate function, we can ﬁnd a δ > 0 such that

F ∩ V2δ({J+ ≤ r}) = ∅. Deﬁne for any n ∈ N,

J(n) = sup δ>0

inf

Jm,δ.

m≥n

Note that as J+ = supn∈N J(n), {J+ ≤ r} =

{J(n) ≤ r}.

n∈N

Using (3.10) and the fact that for any Y ∈ Hn, fk(Y ) ≤ (tr(Y 2))d/2,

we deduce by Lemma 3.6 that J(n) is a good rate function. Therefore, {J(n) ≤ r} is a non-increasing sequence of compact subsets, so that for n large enough,

{J(n) ≤ r} ⊂ Vδ({J+ ≤ r}). Therefore,

F ∩ Vδ {J(n) ≤ r} = ∅. But, {J(n) ≤ r} ⊃ {J ≤ rn1+d2}, where

![image 278](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile278.png>)

J(x) = inf Λ∗(Y ) : fk(Y ) = x,Y ∈ Hn .

Thus,

- (3.12) P fk(X) ∈ F ≤ P fk(X) ∈/ Vδ({J ≤ rn1+d2

![image 279](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile279.png>)

}) .

We are now in the position of applying Theorem 1.5. First, we check that the tightness condition (1.6) is satisﬁed. By [17, Lemma 5.1.14], we know that for any i,j,

Ee

- 1

![image 280](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile280.png>)

- 2Λ∗i,j(Xi,j) ≤ 4(1+1i =j),


using the fact that (ℜXi,j,ℑXi,j) are independent. Therefore, by Chernoﬀ’s inequality,

P(Λ∗(X) > 8n2) ≤ e−4n24n2 ≤ e−n2, which proves that (1.6) is fulﬁlled.

Let K = {Λ∗ ≤ 8n2}. We will now bound the increments of fk on K. As noted before, the level sets of Λ∗ are included in Hilbert-Schmidt balls, more precisely, we know from (3.10),

- (3.13) K ⊂ 4CnB2,

where B2 denotes the ball of radius 1 for the Hilbert-Schmidt norm. By Lemma 3.4, we know that if f : R → R is a convex diﬀerentiable function such that f(0) = f′(0) = 0, then the function

∀Y ∈ Hn, Tf(Y ) = tr[k]f(Y ), admits the variational representation

∀X ∈ Hn, Tf(X) = sup

Y ∈Hn rank(Y )≤k

{trf(Y ) + tr f′(Y )(X − Y ) }.

We deduce that for any X,Y ∈ Hn, Tf(X) − Tf(Y ) ≤ tr f′(Z)(X − Y ) ,

where Z = ki=1 λiuiu∗i , with λ1 ≥ ... ≥ λn the eigenvalues of X and u1,... ,un the associated eigenvectors. If we take f : x  → xd+, x  → xd− or x  → xd in the case d is even, and X ∈ 4CnB2, then we see that f′(Z) is of rank k and ||f′(Z)|| ≤ d||X||d−1 ≤ d(4C)d−1nd−1. As by deﬁnition, fk is a combination of at most two functions Tf associated with the functions x  → xd+, x  → xd− or x  → xd, we get that for any X,Y ∈ 4CB2,

- (3.14) fk(X) − fk(Y ) ≤ sup H∈W


trH(X − Y ),

where

- (3.15) W = {H ∈ Hn : rank(H) ≤ 2k,||H|| ≤ c0nd−1},

where c0 is some positive constant depending on C. Note that by (3.13), the diameter of the level set K is bounded by 8Cn,

and by (3.14), the Lipschitz constant of fk on K is only polynomial in n. By Theorem 1.5, we get

log P fk(X) ∈/ Vδ({J ≤ rn1+d2

![image 281](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile281.png>)

}) ≤ −rn1+d2

![image 282](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile282.png>)

- (3.16) + log N(8ncW,δB2) + O(log n),

where N(8ncW,δB2) denotes the covering number of 8ncW by HilbertSchmidt balls of radius δ. It now remains to compute the covering numbers of W. This is the object of the following lemma.

Lemma 3.8. Let k ∈ {1,... ,n}. Deﬁne the set Mk = {Y ∈ Hn : rank(Y ) ≤ k,||Y || ≤ 1}.

For any ε ∈ (0,1), let N(Mk,εB2) be the covering number of Mk by HilbertSchmidt balls of radius ε. Then,

log N(Mk,εB2) ≤ 2nk log

12k ε

![image 283](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile283.png>)

.

Proof. Let Y ∈ Mk and Z ∈ Hn. Let us spectrally decompose Y , and write Z as,

Y =

k

i=1

λiuiu∗i, Z =

k

i=1

µivivi∗,

where µi are real numbers, vi are unit vectors (not necessarily orthogonal to one another), λ1,... ,λk are the possible non-zero eigenvalues of Y and u1,... ,uk the associated eigenvectors. As the vi’s are unit vectors,

||Y − Z||2 ≤

k

i=1

|λi − µi| +

k

i=1

|λi|.||uiu∗i − vivi∗||2.

Since ||Y || ≤ 1 and ||uv∗||2 = ||u||2||v||2 for any u,v ∈ Cn, we get,

- (3.17) ||Y − Z|| ≤ k max


|λi − µi| + 2k max 1≤i≤k

||ui − vi||2.

1≤i≤k

Let E be a ε/2k-net of [−1,1] and F a ε/4k-net of the unit sphere Sn−1. Then, the set

k

µivivi∗ : µi ∈ E, ui ∈ F ,

Dε =

i=1

is an ε-net of Mk due to the inequality (3.17). Clearly, we can ﬁnd a net E such that |E| ≤ 2k/ε. Moreover, by [9, Lemma 1.4.2], there exists a net F such that,

12k ε

n

|F| ≤

. From the construction of Dε we get ﬁnally,

![image 284](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile284.png>)

12k ε

log |Dε| ≤ 2nk log

.

![image 285](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile285.png>)

![image 286](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile286.png>)

![image 287](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile287.png>)

![image 288](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile288.png>)

![image 289](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile289.png>)

Coming back to the inequality (3.16), we see that we have the inclusion 8CnW ⊂ nbM2k, for some b > 0. Thus, by Lemma 3.8,

n δ

log N(8CnW,δBℓ2) ≤ N(M2k,δn−bBℓ2) = O nk log

.

![image 290](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile290.png>)

As we chose k log n = o(nd2), we get

![image 291](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile291.png>)

1 n1+d2

limsup

n→+∞

log P fk(X) ∈/ Vδ({J ≤ rn1+d2

}) ≤ −r,

![image 292](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile292.png>)

![image 293](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile293.png>)

![image 294](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile294.png>)

which implies, because of (3.12),

1 n1+d2

log P fk(X) ∈ F ≤ −r.

limsup

![image 295](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile295.png>)

n→+∞

![image 296](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile296.png>)

As this inequality is true for any r < infF J+, we obtain the large deviation upper bound of Theorem 1.15.

3.2. Large deviation lower bound. In this section we will use Lemma

1.9 to prove the large deviation lower bound for (n1tr(X/√n)d)n∈N. One of the diﬃculty in the derivation of the lower bound is that the domain

![image 297](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile297.png>)

![image 298](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile298.png>)

of Λ∗ may be diﬀerent from Hn. To bypass this problem, we will add a small Gaussian noise, as in the proof of Cramer’s theorem (see [17, Proof of Theorem 2.2.30]).

3.2.1. Regularization by Gaussian noise. Recall that we denote by Hn(β) the set of Hermitian matrices when β = 2, and symmetric matrices when

- β = 1, of size n. We say that Γ belongs to the Gaussian orthogonal ensemble (GOE) when β = 1, or to the Gaussian unitary ensemble (GUE) when
- β = 2, if it distributed according to the law, 1


β

4trH2dℓ(nβ)(H),

e−

![image 299](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile299.png>)

![image 300](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile300.png>)

Zn(β)

where ℓn(β) is the Lebesgue measure on Hn(β).

Lemma 3.9. Let X be a Wigner matrix satisfying the convex concentration property 1.13. Let Γ be a GOE matrix if β = 1 or a GUE matrix if β = 2. For any t > 0,

log P tr(X/√n)d − tr (X + εΓ)/√n d > tn = −∞.

1 n1+d2

![image 301](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile301.png>)

![image 302](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile302.png>)

lim

limsup

![image 303](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile303.png>)

ε→0

n→+∞

![image 304](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile304.png>)

Proof. For σ ∈ {−1,1} and Y ∈ Hn, we write Yσ = Y+ if σ = + and Yσ = Y− if σ = −. With this notation, it is suﬃcient to prove that for σ ∈ {−1,1} and any t > 0,

log P tr(Xσ/√n)d − tr (X + εΓ)σ/√n d > tn = −∞.

1 n1+d2

![image 305](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile305.png>)

![image 306](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile306.png>)

lim

limsup

![image 307](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile307.png>)

ε→0

n→+∞

![image 308](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile308.png>)

Fix σ ∈ {−1,1}. We will ﬁrst show that for any ε ≥ 0, the sequence (n−1tr|X +εΓ|d)n∈N is exponentially tight at the scale n1+d2. This will allow us to reduce ourselves to prove that n−1/d||(X + εΓ)σ/√n||d is an exponentially good approximation of n−1/d||Xσ/√n||d, where || ||d denotes the dth Schatten norm,

![image 309](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile309.png>)

![image 310](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile310.png>)

![image 311](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile311.png>)

- (3.18) || ||d : Y ∈ Hn  → tr|Y |d 1/d.

Since || ||d is a convex 1-Lipschitz function with respect to the HilbertSchmidt norm, we obtain by applying the convex concentration property 1.13 that for any t > 0,

- (3.19) P ||X/√n||d − E||X/√n||d > tn1/d ≤ c−1e−ct2n


1+ 2

![image 312](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile312.png>)

d . But, using Cauchy-Schwarz inequality and Jensen’s inequality we have, E n−1/d||X/√n||d ≤ E

![image 313](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile313.png>)

![image 314](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile314.png>)

tr(X/√n)2d

tr(X/√n)2d

1 n

1 n

- 1

![image 315](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile315.png>)

- 2d ≤ E


- 1

![image 316](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile316.png>)

- 2d .


![image 317](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile317.png>)

![image 318](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile318.png>)

![image 319](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile319.png>)

![image 320](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile320.png>)

![image 321](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile321.png>)

By Wigner’s theorem [1, Lemma 2.1.6], we get that E||X/√n||d = O(n1/d). Therefore, we can deduce from (3.19) that (n1tr|X/√n|d)n∈N is exponentially tight at the scale n1+d2. Using further the triangle inequality for the dth Schatten norm, and the fact that Γ also satisﬁes the convex concentration property by [30, Theorem 5.2, 4.3], we deduce that for any ε ≥ 0, (n1tr|(X + εΓ)/√n|d)n∈N is exponentially tight at the scale n1+d2. Therefore, it suﬃces to show that for arbitrary large but ﬁxed τ > 0 and any t > 0,

![image 322](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile322.png>)

![image 323](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile323.png>)

![image 324](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile324.png>)

![image 325](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile325.png>)

![image 326](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile326.png>)

![image 327](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile327.png>)

![image 328](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile328.png>)

1 n1+d2

log PAτ µX/√n(xdσ) − µ(X+εΓ)/√n(xdσ) > t = −∞,

lim

limsup

![image 329](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile329.png>)

![image 330](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile330.png>)

![image 331](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile331.png>)

ε→0

n→+∞

![image 332](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile332.png>)

where PAτ denotes the measure P(. ∩ Aτ), and Aτ is the event, Aτ = µX/√n(|x|d) ≤ τ, µ(X+εΓ)/√n(|x|d) ≤ τ .

![image 333](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile333.png>)

![image 334](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile334.png>)

Using the uniform continuity of x  → |x|1/d on compact sets, we deduce that it is enough to show for any δ > 0,

1 n1+d2

log P µX/√n(xdσ)

lim

limsup

![image 335](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile335.png>)

![image 336](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile336.png>)

ε→0

n→+∞

![image 337](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile337.png>)

But, by Minkowski’s inequality,

1

d − µ(X+εΓ)/√n(xdσ)

![image 338](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile338.png>)

![image 339](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile339.png>)

1

d > δ = −∞.

![image 340](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile340.png>)

µX/√n(xdσ)

![image 341](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile341.png>)

1

d − µ(X+εΓ)/√n(xdσ)

![image 342](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile342.png>)

![image 343](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile343.png>)

1

d ≤

![image 344](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile344.png>)

n

1 n

![image 345](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile345.png>)

i=1

(λi)σ − (µi)σ d

1

![image 346](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile346.png>)

d,

where λ1 ≥ ... ≥ λn and µ1 ≥ ... ≥ µn are the eigenvalues of respectively X/√n and (X + εΓ)/√n. But,

![image 347](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile347.png>)

![image 348](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile348.png>)

n

i=1

n

(λi)σ − (µi)σ d ≤

i=1

λi − µi d,

and by Lidskii’s theorem (see [7, Theorem III.4.1]),

n

1 n

![image 349](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile349.png>)

i=1

λi − µi d ≤ µεΓ/√n(|x|d).

![image 350](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile350.png>)

Thus it actually suﬃces to prove that for any δ > 0,

1 n1+d2

log P µεΓ/√n(|x|d) > δ = −∞,

lim

limsup

![image 351](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile351.png>)

![image 352](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile352.png>)

ε→0

n→+∞

![image 353](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile353.png>)

But (n1tr|Γ/√n|d) is exponentially tight at the scale n1+d2, therefore we get ﬁnally the claim.

![image 354](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile354.png>)

![image 355](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile355.png>)

![image 356](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile356.png>)

![image 357](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile357.png>)

![image 358](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile358.png>)

![image 359](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile359.png>)

![image 360](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile360.png>)

3.2.2. A tilting strategy. By [17, Theorem 4.2.16], it is suﬃcient to prove

the large deviations lower bound for the sequence (n1tr((X + εΓ)/√n)d)n∈N for any ε > 0 small enough. We denote by Λ∗ε the Legendre transform of the logarithmic Laplace transform Λε of X + εΓ, that is,

![image 361](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile361.png>)

![image 362](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile362.png>)

ε2trH2 β

∀H ∈ Hn(β), Λε(H) = log Eetr[(X+εΓ)] = Λ(H) +

.

![image 363](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile363.png>)

Adding this small Gaussian noise yields that the domain of Λ∗ε is Hn(β). We note also for future record that,

- (3.20) ∀Y ∈ Hn(β), Λ∗ε(Y ) ≤ Λ∗(Y ).

Let us now proceed with the proof of the large deviation lower bound. Denote by Z = X + εΓ. Let x ∈ R, such that I−(x) < +∞. This means, from the deﬁnition of I− in Theorem 1.15, that we can ﬁnd a sequence Y ∈ Hn(β) such that,

- (3.21) lim

n→+∞

µsc(xd) +

1 n

![image 364](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile364.png>)

tr(Y/√n)d −→

![image 365](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile365.png>)

n→+∞

x, lim

n→+∞

Λ∗(Y ) n1+d2

![image 366](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile366.png>)

![image 367](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile367.png>)

= I−(x). Let δ > 0. For n large enough, we have

P

1 n

![image 368](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile368.png>)

tr(Z/√n)d ∈ B(x,2δ) ≥ P

![image 369](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile369.png>)

1 n

![image 370](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile370.png>)

tr(Z/√n)d ∈ B(sn,δ) ,

![image 371](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile371.png>)

where sn = µsc(xd) + n1tr(Y/√n)d. Let E denote the event,

![image 372](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile372.png>)

![image 373](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile373.png>)

E = A ∈ Hn(β) :

1 n

![image 374](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile374.png>)

tr(A/√n)d ∈ B(sn,δ) . Using Lemma 1.9 and (3.20), we have,

![image 375](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile375.png>)

- P(Z ∈ E) ≥ e−Λ∗(Y )PY (Z ∈ E)exp −


1 PY (Z ∈ E)1/2

![image 376](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile376.png>)

H,∇2Λε(H).H 1/2 ,

where H = ∇Λ∗ε(Y ), and under PY , Z follows the tilted law, etr(HZ)−Λε(H)dP(Z). To obtain the lower bound, we will prove on one hand,

- (3.22) H,∇2Λε(H).H = O(Λ∗(Y )). and on the other hand, that
- (3.23) PY (Z ∈ V ) −→ n→+∞


1,

Provided these two claims hold, we get, as Λ∗(Y ) = O(n1+d2 ),

![image 377](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile377.png>)

1 n1+d2

liminf

log P

![image 378](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile378.png>)

n→+∞

![image 379](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile379.png>)

tr(Z/√n)d ∈ B(x,δ) ≥ −I−(x),

1 n

![image 380](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile380.png>)

![image 381](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile381.png>)

which gives the lower bound of Theorem 1.15.

Let us now prove (3.22) and (3.23). For the ﬁrst claim, note that for any A ∈ Hn(β),

- (3.24) ∇2Λε(A) = ∇2Λ(A) +

2ε2 β

![image 382](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile382.png>)

Id,

and for any H ∈ Hn(β),

tr H∇2Λ(A).H =

n

i=1

∂2Λ1,1(Ai,i) ∂A21,1

![image 383](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile383.png>)

Hi,i2 +

i =j

Hi,j,∇2Λ1,2(Ai,j).Hi,j ,

where .,. denotes the scalar product in C2. As we assumed that the second derivatives of Λ1,1 and Λ1,2 are bounded, we deduce that there exists r > 0 such that for any A ∈ Hn(β), ∇2Λε(A) ≤ r, for the matrix order. Thus, it is suﬃcient to prove that for any Y ∈ Hn(β),

- (3.25) trH2 = O(Λ∗(Y )),


where H = ∇Λ∗ε(Y ). From (3.24) we have in particular ∇2Λε(A) ≥ 2βε2 for the matrix order. Therefore, denoting by Λε,(i,j) the logarithmic Laplace transform of Xi,j + εΓi,j for any i,j ∈ {1,... ,n}, and integrating the inequalities,

![image 384](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile384.png>)

∀A ∈ Hn(β), ∀i < j, Λ′′ε,(i,i)(Ai,i) ≥

2ε2 β

2ε2 β

, ∇2Λε,(i,j)(Ai,j) ≥

,

![image 385](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile385.png>)

![image 386](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile386.png>)

(where the last inequality is meant in the matrix order when β = 2), knowing that ∇Λε(0) = 0, we obtain

||∇Λε(H)||2 ≥ ε2||H||2. From (3.10), we deduce that,

- 1

![image 387](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile387.png>)

- 2C2


tr ∇Λε(H) 2 ≥

Λ∗(∇Λε(H)) ≥

ε4 2C2

trH2,

![image 388](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile388.png>)

which proves the estimate (3.25) since by deﬁnition ∇Λε(H) = Y .

For the second claim (3.23), we observe that under PY , Z is a random Hermitian matrix with independent entries up to the symmetry with mean ∇Λε(H) = Y . Moreover, if σi,j2 = EH|Zi,j − EZi,j|2 is the variance of the (i,j)th coordinate for i < j, then

|1 + ε2 − σi,j2 | = |tr∇2Λε,(i,j)(0) − tr∇2Λε,(i,j)(Hi,j)|

= |tr∇2Λi,j(0) − tr∇2Λi,j(Hi,j)|, and

2ε2 β

σi,i2 = Λ′′i,i(Hi,i) +

.

![image 389](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile389.png>)

As we assumed the second and third derivatives of Λi,j to be uniformly bounded, we deduce that |1 + ε2 − σi,j2 | = O(|Hi,j|), and σi,i2 = O(1). Thus, using the fact √x + y ≤

√x + √y for x,y ≥ 0, we get ( 1 + ε2 − σi,j)2 ≤

![image 390](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile390.png>)

![image 391](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile391.png>)

![image 392](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile392.png>)

![image 393](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile393.png>)

|1 + ε2 − σi,j2 | ≤ O n(||H||2 ∨ 1) ,

- (3.26) i,j


i,j

where we further used Cauchy-Schwarz inequality. Therefore, from (3.25), we get

![image 394](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile394.png>)

( 1 + ε2 − σi,j)2 = O n Λ∗(Y )1/2 ∨ 1 .

i,j

But Λ∗(Y ) = O(n1+d2) by (3.21). Thus, we ﬁnally obtain,

![image 395](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile395.png>)

( 1 + ε2 − σi,j)2 = O(n32+d1) = o(n2).

![image 396](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile396.png>)

![image 397](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile397.png>)

![image 398](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile398.png>)

i,j

Thus, to show the claim (3.23), it remains to prove the following lemma, which is where the assumptions we made on the boundedness of the derivatives of Λ play further their roles.

Lemma 3.10. Let d ≥ 3 and ℓ even such that ℓ > d. Let X be a random Hermitian matrix such that (Xi,j)i≤j are independent. Assume that the ℓth moments of Xi,j are uniformly bounded,

tr(EX)2 = O(n1+d2), and

![image 399](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile399.png>)

(1 − σi,j)2 = o(n2),

i,j

where σi,j2 = E|Xi,j − EXi,j|2. Then,

tr(X/√n)d − µsc(xd) −

tr(EX/√n)d −→

1 n

1 n

![image 400](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile400.png>)

![image 401](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile401.png>)

0, in probability.

![image 402](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile402.png>)

![image 403](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile403.png>)

n→+∞

Proof. Let Xˆ = X − EX. From [3, Lemma 2.1 (9)], we know that expanding tr(Xˆ + EX)d, we obtain by bounding the mixed terms using H¨older’s inequality,

trXd − trXˆd − tr(EX)d ≤ 2d max

||Xˆ||kd+1||EX||d2−k,

1≤k≤d−1

where || ||m denotes the mth Schatten norm, which is deﬁned in (3.18). As ℓ > d, we have ||Xˆ||d+1 ≤ ||Xˆ||ℓ. Using the assumption that tr(EX)2 = O(n1+d2), we get,

![image 404](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile404.png>)

||Xˆ||kℓn(21+d1)(d−k) . But as ℓ is even,

trXd − trXˆd − tr(EX)d = O max

![image 405](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile405.png>)

![image 406](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile406.png>)

1≤k≤d−1

- (3.27) EtrXˆℓ = O(n1+2ℓ ),


![image 407](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile407.png>)

by expanding the trace and using the fact that the ℓth moments of the entries X are uniformly bounded. By Markov’s inequality, we deduce that

P(||Xˆ||ℓ ≥ (log n)n1ℓ+12) −→

0. Therefore,

![image 408](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile408.png>)

![image 409](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile409.png>)

n→+∞

n(12+1ℓ)kn(21+d1)(d−k) ,

trXd − trXˆd − tr(EX)d = O (log n)d max

![image 410](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile410.png>)

![image 411](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile411.png>)

![image 412](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile412.png>)

![image 413](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile413.png>)

1≤k≤d−1

with probability going to 1. As ℓ > d, the maximum on the right-hand side is achieved at k = 1, so that

trXd − trXˆd − tr(EX)d = O (log n)dn1+d2n−(d1−1ℓ) = o(n1+d2), with probability going to 1. It now remains to show that,

![image 414](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile414.png>)

![image 415](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile415.png>)

![image 416](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile416.png>)

![image 417](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile417.png>)

tr(X/ˆ √n)d −→

1 n

µsc(xd),

![image 418](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile418.png>)

![image 419](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile419.png>)

n→+∞

in probability. Let Σ = (σi,j)i,j and Yˆ such that Xˆ = Σ ◦ Yˆ, where ◦ denotes the Hadamard product. From Wigner’s theorem, we know that in probability,

µsc,

µYˆ/√n

![image 420](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile420.png>)

n→+∞

weakly. Denote by W2 the L2-Wasserstein distance on the space P(R) of probability measures on R, which is deﬁned by,

∀µ,ν ∈ P(R), W2(µ,ν) = inf

π

|x − y|2dπ(x,y),

where the inﬁmum runs over all couplings between µ and ν. From the assumption on the variance proﬁle of X, we have by Hoﬀman-Weilandt inequality (see [7, Theorem VI.4.1]),

EW2(µX/ˆ √n,µYˆ/√n) −→

0.

![image 421](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile421.png>)

![image 422](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile422.png>)

n→+∞

Thus, together with the weak convergence of µYˆ/√n towards the semi-cercle law, we deduce that W2(µX/ˆ √n,µsc) converges to 0 in probability. But, from

![image 423](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile423.png>)

![image 424](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile424.png>)

- (3.27), we get by Markov’s inequality,


P µX/ˆ √n(xℓ) ≥ τ −→

0. Therefore, we can integrate the limit and deduce that

lim

limsup

![image 425](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile425.png>)

n→+∞

τ→+∞

n→+∞

tr(X/ˆ √n)d = µsc(xd) + o(1), in probability.

1 n

![image 426](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile426.png>)

![image 427](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile427.png>)

![image 428](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile428.png>)

![image 429](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile429.png>)

![image 430](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile430.png>)

![image 431](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile431.png>)

3.3. Computation of the rate function. In this section we give a proof of Corollary 1.17. We ﬁrst prove a general upper bound on the lower bound rate function I−. This bound corresponds to the strategy of increasing (or decreasing) uniformly the mean of the oﬀ-diagonal entries.

Lemma 3.11. Assume X is a Wigner matrix such that in the case β = 2, (ℜX1,2,ℑX1,2) are each of variance 1/2. Then,

β 4

xd2, where

∀x ≥ 0, limsup

In(x) ≤

![image 432](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile432.png>)

![image 433](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile433.png>)

n→+∞

Λ∗(Y ) n1+d2

tr(Y/√n)d = x,Y ∈ Hn(β) . In particular,

1 n

![image 434](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile434.png>)

:

In(x) = inf

![image 435](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile435.png>)

![image 436](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile436.png>)

![image 437](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile437.png>)

2

β 4 x − µsc(xd)

d if d is even and x ≥ µsc(xd),

![image 438](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile438.png>)

![image 439](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile439.png>)

I−(x) ≤

β 4|x|d2 if d is odd and x ∈ R.

![image 440](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile440.png>)

![image 441](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile441.png>)

1

dn12+d1, and deﬁne

![image 442](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile442.png>)

Proof. Let x ≥ 0. Let y = (n−1)d x+(n−1)

![image 443](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile443.png>)

![image 444](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile444.png>)

![image 445](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile445.png>)





0 y y y

![image 446](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile446.png>)

![image 447](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile447.png>)

![image 448](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile448.png>)

![image 449](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile449.png>)

![image 450](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile450.png>)

![image 451](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile451.png>)

![image 452](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile452.png>)

![image 453](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile453.png>)

![image 454](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile454.png>)

![image 455](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile455.png>)

![image 456](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile456.png>)

![image 457](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile457.png>)

![image 458](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile458.png>)

![image 459](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile459.png>)

![image 460](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile460.png>)

![image 461](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile461.png>)

![image 462](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile462.png>)

![image 463](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile463.png>)

![image 464](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile464.png>)

![image 465](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile465.png>)

![image 466](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile466.png>)

![image 467](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile467.png>)

![image 468](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile468.png>)

![image 469](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile469.png>)

![image 470](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile470.png>)

![image 471](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile471.png>)

![image 472](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile472.png>)

![image 473](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile473.png>)

![image 474](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile474.png>)

![image 475](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile475.png>)

![image 476](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile476.png>)

![image 477](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile477.png>)

![image 478](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile478.png>)

![image 479](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile479.png>)

![image 480](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile480.png>)

![image 481](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile481.png>)

![image 482](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile482.png>)

![image 483](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile483.png>)

![image 484](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile484.png>)

![image 485](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile485.png>)

![image 486](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile486.png>)

![image 487](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile487.png>)

![image 488](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile488.png>)

![image 489](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile489.png>)

∈ Hn.

Y =

![image 490](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile490.png>)

![image 491](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile491.png>)

![image 492](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile492.png>)

![image 493](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile493.png>)

![image 494](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile494.png>)

![image 495](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile495.png>)

![image 496](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile496.png>)

![image 497](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile497.png>)

![image 498](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile498.png>)

![image 499](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile499.png>)

![image 500](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile500.png>)

![image 501](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile501.png>)

![image 502](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile502.png>)

![image 503](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile503.png>)

![image 504](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile504.png>)

![image 505](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile505.png>)

![image 506](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile506.png>)

![image 507](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile507.png>)

![image 508](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile508.png>)

![image 509](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile509.png>)

![image 510](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile510.png>)

y y y 0

![image 511](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile511.png>)

![image 512](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile512.png>)

![image 513](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile513.png>)

![image 514](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile514.png>)

![image 515](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile515.png>)

![image 516](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile516.png>)

![image 517](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile517.png>)

![image 518](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile518.png>)

![image 519](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile519.png>)

![image 520](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile520.png>)

![image 521](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile521.png>)

![image 522](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile522.png>)

![image 523](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile523.png>)

![image 524](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile524.png>)

![image 525](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile525.png>)

 

 

![image 526](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile526.png>)

![image 527](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile527.png>)

![image 528](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile528.png>)

![image 529](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile529.png>)

![image 530](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile530.png>)

![image 531](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile531.png>)

![image 532](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile532.png>)

![image 533](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile533.png>)

![image 534](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile534.png>)

![image 535](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile535.png>)

![image 536](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile536.png>)

![image 537](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile537.png>)

![image 538](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile538.png>)

![image 539](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile539.png>)

![image 540](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile540.png>)

![image 541](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile541.png>)

![image 542](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile542.png>)

![image 543](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile543.png>)

![image 544](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile544.png>)

![image 545](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile545.png>)

![image 546](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile546.png>)

![image 547](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile547.png>)

![image 548](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile548.png>)

![image 549](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile549.png>)

![image 550](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile550.png>)

![image 551](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile551.png>)

![image 552](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile552.png>)

![image 553](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile553.png>)

![image 554](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile554.png>)

![image 555](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile555.png>)

![image 556](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile556.png>)

![image 557](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile557.png>)

![image 558](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile558.png>)

![image 559](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile559.png>)

![image 560](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile560.png>)

![image 561](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile561.png>)

Then, tr(Y d) = xn1+d2, and

![image 562](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile562.png>)

n(n − 1) 2

Λ∗(Y ) =

Λ∗ℜX1,2(y).

![image 563](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile563.png>)

But y ∼ nd1−12xd1. As ℜX1,2 has variance 1/β, we claim that the Taylor expansion of Λ∗ around 0 gives Λ∗ℜX

![image 564](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile564.png>)

![image 565](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile565.png>)

![image 566](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile566.png>)

(y) = βy22 + o(y2). Indeed, if we let g = Λ∗ℜX

![image 567](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile567.png>)

1,2

, then one can derive from the identity (g∗)′ ◦ g′ = Id the fact that

1,2

1 g′′(λ)

∀λ ∈ R, (g∗)′′(g′(λ)) =

.

![image 568](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile568.png>)

Since ℜX1,2 is centered and has variance 1/β. We have g′(0) = 0 and g′′(0) = 1/β. Thus, (g∗)′′(0) = β and therefore Λ∗ℜX

(y) = βy22 + o(y2) as y → 0. Thus,

![image 569](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile569.png>)

1,2

n(n − 1) 2

β 2

β 4

xd2 + o(1) n1+d2, which ends the proof.

xd2nd2−1 + o(nd2−1) =

Λ∗(Y ) =

![image 570](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile570.png>)

![image 571](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile571.png>)

![image 572](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile572.png>)

![image 573](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile573.png>)

![image 574](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile574.png>)

![image 575](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile575.png>)

![image 576](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile576.png>)

![image 577](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile577.png>)

![image 578](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile578.png>)

![image 579](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile579.png>)

![image 580](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile580.png>)

![image 581](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile581.png>)

Remark 3.12. One can produce a second upper bound on I− which corresponds this time to the strategy of having one very large entry on the diagonal (for example). It reads,

Λ∗1,1(xd1nd1+21) n1+d2

![image 582](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile582.png>)

![image 583](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile583.png>)

![image 584](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile584.png>)

∀x ≥ 0, I−(x + µsc(xd)) ≤ limsup

,

![image 585](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile585.png>)

n→+∞

![image 586](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile586.png>)

which is nontrivial if Λ∗1,1 has a quadratic behavior at inﬁnity. In particular, this bound shows that one can have a rate function very diﬀerent from the

one of the GOE or GUE. Indeed, if Λ1,1(λ) ≃+∞ B2 λ2, then Λ∗1,1(x) ≃+∞

![image 587](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile587.png>)

- 1

![image 588](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile588.png>)

- 2Bx2, so that,


- 1

![image 589](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile589.png>)

- 2B


xd2.

∀x ≥ 0, I−(x + µsc(xd)) ≤

![image 590](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile590.png>)

This bound is somewhat related to the large deviations of the traces of Wigner matrices with entries having super-Gaussian tails (see [3] for more details), where a heavy-tail phenomenon arises, in the sense that only the large entries of the matrix are controlling the large deviation of the trace.

In the case where the entries of X have sharp sub-Gaussian tails, we show in the following proposition that the upper bound on I− proved in Lemma 3.11 is also a lower bound on I+. By Theorem 1.15, this fact immediately implies that a full LDP holds for the traces of this class of Wigner matrices, as announced in Corollary 1.17.

Proposition 3.13. Assume X is a Wigner matrix whose entries have

sharp sub-Gaussian tail. Assume further that EX12,1 ≤ β/2, and in the case β = 2 that (ℜX1,2,ℑX1,2) are each of variance 1/2. Then,

I+ = I− = Jd, where Jd is deﬁned in Corollary 1.17, and where for any x ∈ R,

I+(x) = sup δ>0

liminf

In,δ(x),

n→+∞

In,δ(x), and for any n ∈ N, δ > 0,

I−(x) = sup δ>0

limsup

n→+∞

Λ∗(Y ) n1+d2

tr(Y/√n)d + µsc(xd) − x| < δ,Y ∈ Hn .

1 n

![image 591](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile591.png>)

: |

In,δ(x) = inf

![image 592](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile592.png>)

![image 593](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile593.png>)

![image 594](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile594.png>)

Proof. Since the entries of X have sharp sub-Gaussian tails, we deduce from our assumptions on the covariance structure that for any H ∈ Hn(β), Λ(H) ≤ (1/β)trH2. Therefore we have for any Y ∈ Hn(β),

β 4

trY 2.

Λ∗(Y ) ≥

![image 595](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile595.png>)

But, |tr(Y d)| ≤ tr(|Y |d) ≤ (tr(Y 2))d/2, therefore,

β 4 |tr(Y d)|2

Λ∗(Y ) ≥

d. Thus, for any x ∈ R,

![image 596](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile596.png>)

![image 597](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile597.png>)

β 4 |y|2

d : y + µsc(xd) = x,y ∈ R .

I+(x) ≥ inf

![image 598](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile598.png>)

![image 599](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile599.png>)

In the case d is even, we see that the function on the right-hand side is inﬁnite if x < µ(xd) and otherwise equal to (β/4)(x−µsc(xd))2/d. If d is odd, then one obtains I+(x) ≥ (β/4)|x|2/d. In conclusion, we have the inequality I+ ≥ Jd. But, by Lemma 3.11, I− ≤ Jd, which completes the proof.

![image 600](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile600.png>)

![image 601](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile601.png>)

![image 602](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile602.png>)

![image 603](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile603.png>)

4. Upper tail of cycle counts in sparse Erd˝s–Re´nyi graphs. In this section, we will give a proof of Proposition 1.19. As for the traces of Wigner matrices, the main idea is to reduce the complexity by showing that we can replace the full trace by a truncated version, involving only the eigenvalues at the edges of the spectrum. Then, using standard complexity computations, we apply Proposition 1.5 to obtain the desired upper bound.

4.1. A truncation argument. We recall that for any Y ∈ Hn, we denote by λ1(Y ),... ,λn(Y ) its eigenvalues in non-decreasing order and for any k ∈ {1,... ,n}, we denote by tr[k]Y the truncated trace:

k

λi(Y ).

tr[k]Y =

i=1

We deﬁne gk the function,

tr[k](Y d) if d is even, tr[k](Y+d) − tr[k](Y−d) if d is odd.

∀Y ∈ Hn, gk(Y ) =

Building on the concentration inequalities we proved in §3.1.1, we will show the following exponential equivalent.

Lemma 4.1. Denote by vn = n2p2 log(1/p). Assume log(1/p) = o(np2). Let k ∈ {1,... ,n} such that log4(1/p) = o(k), and in the case d = 3 such that moreover k = o((np)3/2). For any δ > 0,

1 vn

lim

n→+∞

log P tr(Xd) − gk(X) > δpdnd = −∞.

![image 604](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile604.png>)

Proof. The proof will be slightly more involved than its counterpart for Wigner matrices which we proved in Lemma 3.1. We will actually need here a “slicing argument” as the one used in the proof the large deviations of the moments of β-ensembles (see [3, Proposition 3.5]). In a ﬁrst step, we will prove that for any δ > 0,

1 vn

- (4.1) lim n→+∞


log P Z − EZ > δpdnd = −∞,

![image 605](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile605.png>)

where Z = trXd − gk(X). We will only consider the case where d is odd. In order to show (4.1), we see that it suﬃces to prove that for σ ∈ {−,+}, and for any δ > 0,

1 vn

- (4.2) lim n→+∞


log P

![image 606](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile606.png>)

n

n

λdi − E

λdi > δpdnd = −∞,

i=k+1

i=k+1

where we use λi as a shorthand for λi(Xσ) for any i ∈ {1,... ,n}. Fix σ ∈ {−,+}. Let M > 0, and deﬁne fM the truncated power function, by fM(x) = xd for x ∈ [0,M], and for x > M,

fM(x) = dMd−1(x − M) + Md.

Note that fM is by construction convex and dMd−1-Lipschitz on R+. By [33, Theorem 8.6], we know that X satisﬁes the convex concentration property as deﬁned in 1.13 with constants κ = 1/2 and C = 2. Observe that we can write,

n

fM(λi) = trfM(Xσ) − tr[k]fM(Xσ).

i=k+1

Applying Proposition 3.2 to the function x  → fM(xσ) which is convex and dMd−1-Lipschitz, we get

- (4.3)

P

n

i=k+1

fM(λi) − E

n

i=k+1

fM(λi)| > δndpd ≤ 4exp −

n2d−1p2dδ2 8d2M2(d−1)

![image 607](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile607.png>)

.

Let αn to be a sequence going to +∞ such that,

- (4.4) α2n = o

√np (log(1/p))

![image 608](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile608.png>)

![image 609](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile609.png>)

1 d−1

![image 610](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile610.png>)

,

which is possible since we assumed log(1/p) = o(np2). We set

- (4.5) M = √npαn. Re-writing (4.3) with this choice of M, we have

![image 611](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile611.png>)

- (4.6) P


n

n

ndpd+1δ2 8d2αn2(d−1)

fM(λi) > δndpd ≤ 4exp −

fM(λi)−E

.

![image 612](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile612.png>)

i=k+1

i=k+1

But,

Lemma 4.2. Assume log n = o(np). There exists a constant C0 > 0 such that for any M ≥ C0√np, and k ≥ 1.

![image 613](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile613.png>)

n

(λdi − fM(λi)) = o(ndpd).

E

i=k+1

Proof. We have,

n

λdi −

i=k+1

n

n

1λi≥Mλdi .

fM(λi) ≤

i=k+1

i=k+1

Using the fact that λi ≤ n since the entries of X are bounded by 1, we deduce that,

- (4.7) E

n

i=k+1

(λdi − fM(λi)) ≤ nd+1P max(−λn(X),λ2(X)) ≥ M .

Let u ∈ Rn be the vector (1,1,... ,1), and and let Xˆ = X −puu∗. By Weyl’s inequalities (see [7, Theorem III.2.1]), we have

max(−λn(X),λ2(X)) ≤ ||Xˆ||. Since log n = o(np), we know from [29, Example 4.10], that E||Xˆ|| =

- O(√np). As noted before, Xˆ has the convex concentration property with constants κ = 1/2 and C = 2. Using the fact that the spectral radius of a Hermitian matrix is a convex and 1-Lipschitz function with respect to the Hilbert-Schmidt norm, we deduce that there exist c0,α > 0 such that for any c ≥ c0√np,


![image 614](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile614.png>)

![image 615](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile615.png>)

- (4.8) P(||Xˆ|| ≥ c) ≤ 2e−αc2.

As we assumed log n = o(np), this bound is exponentially small, which, in view of (4.7) ends proof of the lemma.

![image 616](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile616.png>)

![image 617](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile617.png>)

![image 618](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile618.png>)

![image 619](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile619.png>)

By Lemma 4.2, we deduce that for n large enough, we have

|E

n

i=k+1

λdi − fM(λi) | ≤ δndpd.

Therefore, by (4.6), we have for n large enough,

P

n

i=k+1

fM(λi) − E

n

i=k+1

λdi > 2δndpd ≤ 4exp −

δ2ndpd+1 8d2αn2(d−1)

![image 620](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile620.png>)

.

Since d ≥ 3, we have dd−−21 ≤ 12. Thus, from the choice of αn made in (4.4),

![image 621](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile621.png>)

![image 622](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile622.png>)

α2n = o

n

d−2

![image 623](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile623.png>)

d−1p (log(1/p))

![image 624](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile624.png>)

1 d−1

![image 625](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile625.png>)

,

so that

- (4.9) lim n→+∞


n

n

1 vn

λdi | > 2δndpd = −∞.

log P |

fM(λi) − E

![image 626](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile626.png>)

i=k+1

i=k+1

But,

- (4.10) P

n

i=k+1

λdi − fM(λi) > δpdnd ≤ P

n

i=k+1

λdi 1λi≥M > δndpd .

Let R > 0, and denote by N[R,+∞) the number of eigenvalues of Xσ in [R,+∞). By Weyl’s inequalities (see [7, Theorem III.2.1]), we have for any i ≥ 2,

- (4.11) λi(Xˆ) ≤ λi(X) ≤ λi−1(Xˆ), where Xˆ = X − puu∗, with u being the all-ones vector. Therefore,

P N[R,+∞) ≥ k ≤ P |{i : (λi(Xˆ))σ ≥ R}| ≥ k − 1 .

As E||Xˆ|| = O(√np) again by [29, Example 4.10], we deduce by Proposition 3.5 that if R is such that √np = o(R), then for any k ≥ 2,

![image 627](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile627.png>)

![image 628](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile628.png>)

- (4.12) P(N[R,+∞) ≥ k) ≤ 2exp −

R2k 32

![image 629](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile629.png>)

.

Now, take R = vn/βn, with βn = o(k) and βn = o(nplog(1/p)). Our choice of R satisﬁes √np = o(R), and we have

![image 630](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile630.png>)

![image 631](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile631.png>)

lim

n→+∞

1 vn

![image 632](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile632.png>)

log P(N[R/2,+∞) ≥ k) = −∞.

Since we assumed that log4(1/p) = o(k), we can actually set βn to satisfy the conditions,

- (4.13) log4(1/p) = o(βn), βn = o(k) and βn = o(nplog(1/p)),

using the fact that np grows polynomially fast to +∞. Thus, in view of (4.9) and (4.10), it is suﬃcient to prove that,

- (4.14) limsup n→+∞


n

1 vn

λdi 1M≤λi≤R/2 > δndpd = −∞.

log P

![image 633](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile633.png>)

i=k+1

If R/2 < M, then there is nothing left to prove. Assuming that R/2 ≥ M, we are going to use a “slicing argument” to ﬁll the gap between these two levels. To this end, deﬁne an increasing sequence Mm of levels such that M0 = M, and for any m ≥ 0,

Mmd +1 = Rd−2Mm2 ,

that is

2 d

2 d

m

m

log M + 1 −

log R.

log Mm =

![image 634](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile634.png>)

![image 635](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile635.png>)

Let N be such that (2/d)N ≤ log 2/log R. As log R = O(log n), it is possible to ﬁnd such N with N = O(log log n). For such N, we get MN ≥ R/2. Therefore,

P

n

λdi 1M≤λi≤R/2 > δndpd ≤ P

i=k+1

n

λdi 1M≤λi≤MN > δndpd .

i=k+1

Using a union bound we get,

n

N−1

Mmd +1N[Mm,+∞) > δndpd

λdi 1M≤λi≤MN > δndpd ≤ P

- P


m=0

i=k+1

N−1

- (4.15) P N[Mm,+∞) > δndpd/NMmd +1 .


≤

m=0

As Mm ≥ M and √np = o(M) by deﬁnition of M in (4.5), we deduce from (4.12) that for any m ≥ 0,

![image 636](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile636.png>)

δndpd 32NRd−2

P N[Mm,+∞) > δndpd/NMmd +1 ≤ 2exp −

.

![image 637](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile637.png>)

![image 638](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile638.png>)

But R = vn/βn, therefore,

P N[Mm,+∞) > δndpd/NMmd +1 ≤ 2exp(−vncn), with

d−2 n 2

![image 639](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile639.png>)

δβ

cn =

.

![image 640](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile640.png>)

32N logd2(1/p)

![image 641](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile641.png>)

As d/(d − 2) ≤ 3 since d ≥ 3, and N = O(log log n), we see that with our choice of βn which satisﬁes log4(1/p) = o(βn), we have in particular

2

d

N

d−2(1/p) = o(βn). Thus, cn goes to +∞. But, from the union bound (4.15), we have P

d−2 log

![image 642](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile642.png>)

![image 643](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile643.png>)

n

λdi 1M≤λi≤MN > δndpd ≤ N exp(−vncn).

i=k+1

Therefore,

1 vn

log P

lim

![image 644](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile644.png>)

n→+∞

n

λdi 1M≤λi≤MN > δndpd = −∞,

i=k+1

which ends the proof of (4.2), and thus of the claim (4.1).

Now, to end the proof of Lemma 4.1, we need the following lemma which estimates the expectation of the truncated trace involving the bulk eigenvalues.

Lemma 4.3. Assume d ≥ 4 and np2 ≫ 1, or d = 3, log n = o(np) and k = o((np)3/2). Then,

E tr(Xd) − gk(X) = o(ndpd).

Proof. We start with the case d ≥ 4. By Weyl’s inequalities (4.11), we get

tr(Xd) − gk(X) ≤ n||Xˆ||d. But from (4.8), we know that E||Xˆ||d = O((np)d2), thus

![image 645](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile645.png>)

tr(Xd) − gk(X) = O(n(np)d2).

![image 646](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile646.png>)

As d ≥ 4 and np2 → +∞, we have that nd2−1pd2 also goes to +∞, which yields the claim.

![image 647](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile647.png>)

![image 648](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile648.png>)

Assume now that d = 3, log n = o(np) and k = o((np)3/2). As λ1(X) ≥ 0, we have,

ℓ′

λi(X)3,

tr(X3) − tr[k](X+3 ) − tr[k](X−3 ) =

i=ℓ+1

for some ℓ,ℓ′ such that 1 ≤ ℓ ≤ k, and n − ℓ′ ≤ k. We have,

ℓ′

ℓ′

ℓ′

λi(X)3 − tr(Xˆ)3 ≤

λi(Xˆ)3 + 2k||Xˆ||3.

λi(X)3 −

i=ℓ+1

i=ℓ+1

i=ℓ+1

By Weyl’s inequalities (4.11), we have for any i ≥ 2,

λi(Xˆ)3 ≤ λi(X)3 ≤ λi−1(Xˆ)3. Therefore,

ℓ′

ℓ′

λi(Xˆ)3 ≤ 2||Xˆ||3.

λi(X)3 −

0 ≤

i=ℓ+1

i=ℓ+1

Thus,

ℓ′

λi(X)3 ≤ |Etr(Xˆ)3| + 2(k + 1)E||Xˆ||3.

E

i=ℓ+1

But, as (Xˆ)i,i = −p for any i ∈ {1,... ,n} and the oﬀ-diagonal entries of Xˆ are centered, we obtain

Etr(Xˆ)3 = −np3 + O(n2p2) = o(n3p3).

Besides, as log n = o(np), we know from (4.8) that E||Xˆ||3 = O((np)32). Thus,

![image 649](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile649.png>)

ℓ′

λi(X)3| = O(k(np)32) + o(n3p3),

|E

![image 650](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile650.png>)

i=ℓ+1

which gives the claim.

![image 651](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile651.png>)

![image 652](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile652.png>)

![image 653](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile653.png>)

![image 654](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile654.png>)

4.2. Proof of Proposition 1.19. From Lemma 4.1, we see that it suﬃces to consider the upper tail of the truncated trace,

gk(X) =

tr[k]Xd if d is even, tr[k]X+d − tr[k]X−d if d is odd.

for k such that log4(1/p) = o(k), and with the additional condition that k = o((np)3/2) in the case d = 3. As we assume that log4(n) = o(np2), we can ﬁnd k which satisﬁes both conditions

- (4.16) k log n = o(np2 log(1/p)), and log4(1/p) = o(k),


(the additional condition when d = 3 being automatically fulﬁlled).

With this choice of k, we will see that we have reduced the complexity enough to be able to apply Proposition 1.5. Indeed, we will see that we can encode the “gradient” of the truncated trace tr[k]Xd by O(nk log n) bits. Thus, the choice of k made above will guarantee us that the main error term in Proposition 1.5 is negligible with respect to the large deviation speed.

First, we will check that the rate function that Proposition 1.5 is giving us, is as good as the one we are claiming, that is:

Lemma 4.4. Let t ≥ 1 and deﬁne,

ψn(t) = inf Λ∗p(Y ) : gk(Y ) ≥ tndpd,Y ∈ Hn0 .

Then,

ψn(t) ≥ φn t − O(k1−d2) , where φn is deﬁned in Proposition 1.19.

![image 655](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile655.png>)

Proof. Note that when d is even, the claim of the above lemma is trivial, so that we will assume for now on that d is odd. Observe also that ψn(t) = O(vn) by taking C to correspond to planting clique of size r = ⌈(t−1)1/dnp⌉, that is,

1 if i ∧ j ≤ r, p if i ∨ j > r.

∀i < j, Ci,j =

Let then Y ∈ Hn0 be such that Λ∗p(Y ) = O(vn) and gk(Y ) ≥ tndpd. Without loss of generality we can assume that Yi,j ≥ p for any i < j. By [32, Corollary 3.5], we know that for any x ≥ 0,

Λ∗p(p + x) ≥ x2(log(1/p) − o(1)).

We deduce, denoting by U the matrix such that Ui,j = 1 for i = j and null diagonal coeﬃcients, that

tr(Y − pU)2 = O(n2p2). In particular, trY 2 = O(n2p2). We obtain for any i ≥ 1, λi(Y−) = O

np √i

.

![image 656](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile656.png>)

![image 657](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile657.png>)

Therefore,

But,

n

λi(Y−)d = O(ndpdk1−d2).

![image 658](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile658.png>)

i=k+1

n

gk(Y ) ≤ tr(Y d) +

λi(Y−)d,

i=k+1

which gives the claim.

![image 659](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile659.png>)

![image 660](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile660.png>)

![image 661](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile661.png>)

![image 662](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile662.png>)

We can now proceed with the proof of the upper bound of Proposition 1.19. Note that Φ is lower semi-continuous as one can see from its explicit expression (1.12). Therefore, by Lemma 4.1 it is suﬃcient to show that for any t > 1,

1 vn

log P gk(X) ≥ tndpd ≤ −Φ(t),

limsup

![image 663](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile663.png>)

n→+∞

with k such that log4(1/p) = o(k) and k = o(np2).

Fix some t > 1 and δ > 0 such that t − δ > 1. Observe that as Λ∗p is strictly convex, ψn, deﬁned in Lemma 4.4, is strictly increasing. Therefore, we can apply Corollary 1.8. Let Hn0([0,1]) denote the subset of Hn0 which consists of matrix with entries in [0,1]. Observe that for any Y ∈ Hn0([0,1]),

Λ∗p(Y ) ≤ n2 log(1/p), so that the tightness assumption (1.6) of Proposition 1.5 is fulﬁlled with K = Hn0([0,1]) and κ = n2 log(1/p). Arguing as in the proof of (3.14), and using the fact that ||X|| ≤ n for any X ∈ Hn0([0,1]), we obtain that for any X,Y ∈ Hn0([0,1]),

gk(X) − gk(Y ) ≤ sup H∈W

trH(X − Y ),

where

W = H ∈ Hn : rank(H) ≤ 2k, ||H|| ≤ 2dnd−1 ,

using the fact that for any H ∈ Hn([0,1]), ||H|| ≤ n. As the Lipschitz constant of gk on Hn([0,1]) and the diameter of Hn([0,1]) are both only polynomial in n, we get by Corollary 1.8,

P(gk(X) ≥ tndpd) ≤ −ψn(t − δ) + log N(W,(δ/2n)B2) + O(log n),

where N(W,(δ/2n)B2) is the covering number of W by balls of radius δ/n for the Hilbert-Schmidt norm. By Lemma 3.8, we have

log N(W,(δ/2n)B2) = O(nk log n). As we chose k such that k log n = o(np2 log(1/p)), we get P(gk(X) ≥ tndpd) ≤ −ψn(t − δ) + o(vn).

Using Lemma 4.4 and the fact that φn is increasing, we obtain that for n large enough, ψn(t − δ) ≥ φn(t − 2δ). Therefore,

1 vn

log P(gk(X) ≥ tndpd) ≤ −Φ(t − 2δ).

limsup

![image 664](<2018-augeri-nonlinear-large-deviation-bounds_images/imageFile664.png>)

n→+∞

Since this is true for any δ > 0, and Φ is lower semi-continuous, we get the claim by taking δ → 0.

Acknowledgement. I would like to thank Ofer Zeitouni for his enlightening insight and advice. I am also grateful to Ronen Eldan for some inﬂuential discussions and for the remark 1.12, as well as to Anirban Basak for many helpful discussions. Finally, I thank the anonymous referee for the numerous comments and suggestions.

References.

- [1] G. W. Anderson, A. Guionnet, and O. Zeitouni. An introduction to random matrices, volume 118 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2010.
- [2] S. Artstein-Avidan, A. Giannopoulos, and V. D. Milman. Asymptotic geometric analysis. Part I, volume 202 of Mathematical Surveys and Monographs. American Mathematical Society, Providence, RI, 2015.
- [3] F. Augeri. On the large deviations of traces of random matrices. arXiv:1605.03894, to appear in the Annales de l’Institut Poincar´e, May 2016.
- [4] T. Austin. The structure of low-complexity Gibbs measures on product spaces. arXiv:1810.07278.
- [5] Z. Bai and J. W. Silverstein. Spectral analysis of large dimensional random matrices. Springer Series in Statistics. Springer, New York, second edition, 2010.
- [6] A. Basak and S. Mukherjee. Universality of the mean-ﬁeld for the Potts model. arXiv:1508.03949.
- [7] R. Bhatia. Matrix analysis, volume 169 of Graduate Texts in Mathematics. SpringerVerlag, New York, 1997.
- [8] B. Bhattacharya, S. Ganguly, E. Lubetzky, and Y. Zhao. Upper tails and independence polynomials in random graphs. Adv. Math., 319:313–347, 2017.
- [9] D. Chafaı¨, O. Gue´don, G. Lecue´, and A. Pajor. Interactions between compressed sensing random matrices and high dimensional geometry, volume 37 of Panoramas et Synth`eses [Panoramas and Syntheses]. Socie´te´ Mathe´matique de France, Paris, 2012.
- [10] S. Chatterjee. The missing log in large deviations for triangle counts. Random Structures Algorithms, 40(4):437–451, 2012.
- [11] S. Chatterjee and A. Dembo. Nonlinear large deviations. Adv. Math., 299:396–450, 2016.
- [12] S. Chatterjee and S. R. S. Varadhan. The large deviation principle for the Erd˝sRe´nyi random graph. European J. Combin., 32(7):1000–1017, 2011.
- [13] F. Clarke. Functional analysis, calculus of variations and optimal control, volume 264 of Graduate Texts in Mathematics. Springer, London, 2013.
- [14] N. Cook and A. Dembo. Large deviations of sub-graph counts in sparse Erd˝s-Re´nyi. arXiv:1809.11148.
- [15] B. DeMarco and J. Kahn. Tight upper tail bounds for cliques. Random Structures Algorithms, 41(4):469–487, 2012.
- [16] B. DeMarco and J. Kahn. Upper tails for triangles. Random Structures Algorithms, 40(4):452–459, 2012.
- [17] A. Dembo and O. Zeitouni. Large deviations techniques and applications, volume 38 of Stochastic Modelling and Applied Probability. Springer-Verlag, Berlin, 2010. Corrected reprint of the second (1998) edition.
- [18] R. Dobrushin, P. Groeneboom, and M. Ledoux. Lectures on probability theory and statistics, volume 1648 of Lecture Notes in Mathematics. Springer-Verlag, Berlin,

1996. Lectures from the 24th Saint-Flour Summer School held July 7–23, 1994, Edited by P. Bernard.

- [19] R. Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations. Geom. Funct. Anal., 28(6):1548–1596, 2018.
- [20] A. Guionnet and J. Husson. Large deviations for the largest eigenvalue of Rademacher matrices. hal-01828877.
- [21] A. Guionnet and O. Zeitouni. Concentration of the spectral measure for large matrices. Electron. Comm. Probab., 5:119–136 (electronic), 2000.


- [22] V. Jain, F. Koehler, and A. Risteski. Mean-ﬁeld approximation, convex hierarchies, and the optimality of correlation rounding: a uniﬁed perspective. arXiv:1808.07226.
- [23] V. Jain, F. Koehler, and A. Risteski. The Mean-Field Approximation: Information Inequalities, Algorithms, and Complexity. arXiv:1802.06126.
- [24] S. Janson, T. Luczak, and A. Rucin´ski. An exponential bound for the probability of nonexistence of a speciﬁed subgraph in a random graph. Random graphs 87. Wiley, 1990.
- [25] S. Janson, K. Oleszkiewicz, and A. Rucin´ski. Upper tails for subgraph counts in random graphs. Israel J. Math., 142:61–92, 2004.
- [26] S. Janson and L. Warnke. The lower tail: Poisson approximation revisited. Random Struct. Alg., 48:219–246, 2016.
- [27] J. H. Kim and V. H. Vu. Divide and conquer martingales and the number of triangles in a random graph. Random Structures Algorithms, 24(2):166–174, 2004.
- [28] G. Kozma and W. Samotij. private communication.
- [29] R. Lata la, R. van Handel, and P. Youssef. The dimension-free structure of nonhomogeneous random matrices. arXiv:1711.00807.
- [30] M. Ledoux. The concentration of measure phenomenon, volume 89 of Mathematical Surveys and Monographs. American Mathematical Society, Providence, RI, 2001.
- [31] M. Ledoux and M. Talagrand. Probability in Banach spaces, volume 23 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1991. Isoperimetry and processes.
- [32] E. Lubetzky and Y. Zhao. On the variational problem for upper tails in sparse random graphs. Random Structures Algorithms, 50(3):420–436, 2017.
- [33] P. Massart, G. Lugosi, and S. Boucheron. Concentration Inequalities : A Nonasymptotic Theory of Independence. Oxford University Press, 2013.
- [34] R. T. Rockafellar. Convex analysis. Princeton Landmarks in Mathematics. Princeton University Press, Princeton, NJ, 1997.
- [35] M. Sileikisˇ and L. Warnke. A counterexample to the DeMarco-Kahn Upper Tail Conjecture. arXiv:1809.09595.
- [36] Van H. Vu. A large deviation result on the number of small subgraphs of a random graph. Combin. Probab. Comput., 10(1):79–94, 2001.
- [37] J. Yan. Nonlinear Large Deviations: Beyond the Hypercube. arXiv:1703.08887.


Faculty of Mathematics and Computer Science The Weizmann Institute of Science 234 Herzl Street Rehovot 7610001 Israel E-mail: fanny.augeri@weizmann.ac.il

