arXiv:1708.05859v2[math.PR]19Apr2018

Decomposition of mean-ﬁeld Gibbs distributions into product measures

Ronen Eldan∗ and Renan Gross†

Abstract

We show that under a low complexity condition on the gradient of a Hamiltonian, Gibbs distributions on the Boolean hypercube are approximate mixtures of product measures whose probability vectors are critical points of an associated mean-ﬁeld functional. This extends a previous work by the ﬁrst author. As an application, we demonstrate how this framework helps characterize both Ising models satisfying a mean-ﬁeld condition and the conditional distributions which arise in the emerging theory of nonlinear large deviations, both in the dense case and in the polynomially-sparse case.

# Contents

- 1 Introduction 2
- 2 Background and notation 3

- 2.1 Two motivating examples of Hamiltonians . . . . . . . . . . . . . . . . . . . . . . . . 3

- 2.1.1 The Ising model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
- 2.1.2 Nonlinear large deviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


- 2.2 Boolean functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 2.3 Mixture models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5


- 3 Results 6
- 4 Proof of main theorem 10

- 4.1 Notation and review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
- 4.2 Approximate ﬁxed point . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


- 5 Proof of composition theorem 15
- 6 Example applications 17

- 6.1 The Ising model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
- 6.2 Large deviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


- 7 Acknowledgments 22


![image 1](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile1.png>)

∗Weizmann Institute of Science. Email: ronen.eldan@weizmann.ac.il. Partially supported by the Israel Science Foundation, grant 715/16.

†Weizmann Institute of Science. Email: renan.gross@weizmann.ac.il

References 22 A Appendix 22

# 1 Introduction

Let n > 0 and let f : {−1,1}n → R be a function. A probability measure ν on {−1,1}n is called a Gibbs distribution with Hamiltonian f if for X ∼ ν,

Pr [X = x] = exp (f (x)) /Z,

where Z is a normalizing constant. We denote such a distribution by Xnf. Gibbs distributions are central to statistical physics, and appear in applications in computer science, statistics, and economics. However, many important Hamiltonians are far from being analytically tractable.

One method to tackle the diﬃculties entrenched in such Hamiltonians is via mean-ﬁeld approximations. This method goes back to Curie and Weiss and has long been widely used by physicists. More recently, such approximations were established in rigor, see for example [1].

For the case of Gibbs distributions on the Boolean hypercube, [4] showed that if the image of the gradient of the Hamiltonian f has small enough Gaussian-width and Lipschitz constants, then the partition function can be approximated by applying the mean-ﬁeld variant of the Gibbs variational principle. Further, under the same conditions, Xnf can be approximated by a mixture of product measures. This improves an earlier result by Chatterjee and Dembo [2] who consider a slightly diﬀerent notion of complexity.

In this paper, we extend the framework introduced in [4] by showing that if the discrete gradient ∇f also has a small enough Lipschitz constant, then the product measures described above are close to critical points of an associated variational functional which corresponds to the so-called mean-ﬁeld equations. This gives a more precise characterization of the mixture.

An interesting feature of our framework is that it allows us to eﬀectively bypass the need to obtain an accurate approximation of the normalizing constant in the route to understanding the Gibbs distribution. Even though the approximations to the normalizing constant obtained by the framework are far from sharp (they miss by a factor of eo(n) as seen in the examples in [4]), our results still manage to give information about the set where most of the mass resides.

The following is an overview of our results.

- • In Theorem 9, we show that if the Hamiltonian f has low complexity and satisﬁes a Lipschitz condition, the corresponding Gibbs distribution behaves like a mixture of densities of vectors whose entries are i.i.d Bernoulli random variables, and whose expectations X satisfy

X − tanh (∇f (X)) 1 = o(n), where the tanh is applied entrywise.

- • As an example of using this bound, we demonstrate in Corollaries 12 and 13 that Ising models satisfying a mean-ﬁeld assumption can be decomposed into product measures.
- • Theorem 14 concerns compositions: If a function h : R → R has small enough derivatives, then the function h ◦ f also satisﬁes Theorem 9.


- • As an example of this composition, we demonstrate in Theorem 16 that the conditional distribution Pr [Y = y | f (Y ) ≥ tn] arising in large deviation theory can be approximated by a smoothed-cutoﬀ distribution that can be decomposed into product measures, each satisfying an equation which arises from the Lagrange multiplier problem associated with the rate function.


In the sequel work [5], we apply Theorem 9 to exponential random graphs, improving a previously known characterization.

# 2 Background and notation

We denote the Boolean hypercube by Cn = {−1,1}n and the continuous hypercube by Cn = [0,1]n. The uniform measure on Cn is denoted by µ. The space of all product measures on Cn is denoted PMn. For a vector x ∈ Rn, we denote its one-norm by

![image 2](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile2.png>)

n

|xi|.

x 1 =

i=1

## 2.1 Two motivating examples of Hamiltonians

- 2.1.1 The Ising model

An Ising model on n sites can be described as follows: Let x ∈ Cn represent n interacting sites that can be in one of two states. Let A ∈ Rn×n be a real symmetric matrix with 0 on the diagonal representing the intensity of interaction between the sites, so that the interaction between site i and site j is Aij. Let µ ∈ Rn be a vector representing magnetic ﬁeld strengths, so that site i feels a magnetic ﬁeld µi. The Hamiltonian for the system is then deﬁned as

f (x) = x,Ax + µ,x .

If TrA2 = o(n), we say that the model satisﬁes the mean-ﬁeld assumption [1]. We also assume that both µmax and maxi∈[n] j∈[n] |Aij| are O (1), which amounts to the force acting on a single site being bounded.

- 2.1.2 Nonlinear large deviations


Let f : Cn → R be a Hamiltonian. For 0 ≤ p ≤ 1, deﬁne µp to be the measure on Cn where every entry is an i.i.d Bernoulli random variable with success probability p. Let t ∈ R be a real number. The two central questions in the ﬁeld of large deviation theory are:

- 1. For Y ∼ µp, what is the probability Pr [f (Y ) ≥ tn]?
- 2. For Y ∼ µp, what is the conditional distribution Pr[Y = y | f (Y ) ≥ tn]?


One line of approach to answering these questions is to approximate Pr [f (Y ) ≥ tn] and Pr [Y = y | f (Y ) ≥ tn] by using Gibbs distributions. For example, observe that the conditional distribution Pr [Y = y | f (y) ≥ tn] may be obtained from a Gibbs distribution with a “cutoﬀ Hamiltonian” f˜, deﬁned by

n i=1 log 2 1 (1 − yi + 2pyi) f (y) ≥ tn

f˜(y) =

![image 3](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile3.png>)

(1)

−∞ f (y) < tn.

All y with f (y) ≥ tn are thus weighted according to µp, and all y with f (y) < tn have probability

- 0. Unfortunately, f˜ is not smooth enough in order to be applicable for the existing large deviation


frameworks. However, it is possible to get approximations of Xnf˜ by using Hamiltonians which approximate f˜. Such a “smooth-cutoﬀ” Hamiltonian should give a large mass to “good” vectors y such that f (y) ≥ tn and a small mass to “bad” vectors y such that f (y) < tn. Both [4] and [2] follow this approach in order to tackle item (1).

## 2.2 Boolean functions

- Deﬁnition 1 (Discrete gradient, Lipschitz constant). Let f : Cn → R be a real function on the Boolean hypercube. The derivative of f at coordinate i is deﬁned as

∂if (y) =

- 1

![image 4](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile4.png>)

- 2


(f (y1,... ,yi−1,1,y+1,... yn) − f (y1,... ,yi−1,−1,y+1,... yn)) . With this we deﬁne both the the discrete gradient:

∇f (y) = (∂1f (y),... ,∂nf (y)) , and the Lipschitz constant of f:

Lip (f) = max

i∈[n],y∈{−1,1}n

|∂if (y)|.

Every Boolean function f : Cn → R has a unique Fourier decomposition into monomials [7]: f (x) =

S⊆[n]

fˆ(S)

i∈S

xi.

This deﬁnes an extension of f from the discrete hypercube Cn into the continuous hypercube Cn = [−1,1]n by computing the value of the polynomial S⊆[n] fˆ(S) i∈S xi for x ∈ Cn. It can be shown that this is the same extension as the harmonic extension deﬁned in [4, Section 3.1.1]. By Fact 14 in [4], the extension of ∂if agrees with the i-th partial derivative (in the real-diﬀerentiable sense) of the extension of f. Throughout this text, we will always assume that f, and therefore ∇f as well, are extended to Cn.

![image 5](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile5.png>)

![image 6](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile6.png>)

![image 7](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile7.png>)

- Deﬁnition 2 (Gaussian width, gradient complexity). The Gaussian-width of a set K ⊆ Rn is deﬁned as


GW (K) = E sup

x,Γ

x∈K

where Γ ∼ N (0,Id) is a standard Gaussian vector in Rn. For a function f : Cn → R, the gradient complexity of f is deﬁned as

D (f) = GW ({∇f (y) : y ∈ Cn} ∪ {0}) . For a measure ν on Cn, by slight abuse of notation, we deﬁne its complexity as D (ν) = D log

dν dµ

.

![image 8](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile8.png>)

## 2.3 Mixture models

- Deﬁnition 3 (ρ-mixtures). For z ∈ [−1,1]n, denote by X (z) the unique random vector in Cn whose coordinates are independent and whose expectation is EX (z) = z. Let ρ be a measure on [−1,1]n. We deﬁne the random vector X (ρ) by

Pr [X (ρ) = x] = Pr [X (z) = x]dρ(z) . (2)

- Deﬁnition 4 (Approximate mixture decomposition). Let δ > 0 and let ρ be a measure on [−1,1]n. A random variable X is called a (ρ,δ)-mixture if there exists a coupling between X (ρ) and X such that

E X (ρ) − X 1 ≤ δn.

A result of [4] roughly states that low complexity Gibbs distributions are (ρ,δ)-mixtures for δ = o(1) and where ρ is such that most of the entropy comes from the individual X (z) rather than from the mixture.

- Deﬁnition 5 (Wasserstein distance). For two distributions ν1 and ν2, the Wasserstein masstransportation distance, denoted W1, is deﬁned as

W1 (ν1,ν2) = inf

(X,Y ) s.t

X∼ν1,Y ∼ν2

- 1

![image 9](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile9.png>)

- 2


E X − Y 1 ,

where the inﬁmum is taken over all joint distributions whose marginals have the laws ν1 and ν2 respectively.

- Deﬁnition 6 (Tilt of a distribution). For a vector θ ∈ Rn, the tilt τθν of the distribution ν is a distribution deﬁned by

d(τθν) dν

![image 10](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile10.png>)

(y) =

e θ,y Cn e θ,z dν

![image 11](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile11.png>)

.

With the notion of ρ-mixture and tilt, we deﬁne what it means for a random variable to break up into small tilts:

- Deﬁnition 7 (Tilt decomposition). Let δ,ε > 0 and let ρ be a measure on [−1,1]n. A random variable X with distribution ν is called a (ρ,δ,ε)-tilt-mixture if there exists a probability measure m on Rn supported on B (0,ε√n) ∩ −14, 14 n such that:


![image 12](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile12.png>)

![image 13](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile13.png>)

![image 14](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile14.png>)

- 1. For every ϕ : Cn → R,

Cn

ϕdν =

Rn Cn

ϕd(τθν) dm(θ).

- 2. For all but a δ-portion of the measure m, the tilt τθν is δn-close to a product measure in Wasserstein distance:

m({θ ∈ Rn : ∃ξ ∈ PMn s.tW1 (τθν,ξ) ≤ δn}) > 1 − δ.

- 3. The measure ρ is the push-forward of the measure m under the map θ  → EX∼τθν [X].


Fact 8. Every (ρ,δ,ε)-tilt-mixture is also a (ρ,4δ)-mixture. Proof. Deﬁne Θ = {θ ∈ Rn : ∃ξ ∈ PMn s.tW1 (τθν,ξ) ≤ δn}, and denote the distribution of X and of X (ρ) by ν and σ respectively. Using item 1 in the deﬁnition of a tilt-mixture, we have

W1 (ν,σ) ≤

W1 (ξθ,τθν)dm(θ)

Rn

≤

W1 (ξθ,τθν)dm(θ) + m([−1/4,1/4]n \Θ) n.

Θ

By item 2 in the deﬁnition of a tilt-mixture, there exists a coupling between X and X (ρ) such that each term on the right hand side is bounded by δn. This gives a 4δ bound on the expectation E X − X (ρ) 1.

![image 15](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile15.png>)

![image 16](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile16.png>)

![image 17](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile17.png>)

![image 18](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile18.png>)

A tilt-mixture decomposition provides more information than generalρ-mixtures: It tells us something about the structure of the elements of the mixture, with the parameter ε in Deﬁnition 7 bounding the support of the tilts to a ball of radius ε√n. Some of our results will rely on the existence of tilt decompositions with small ε.

![image 19](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile19.png>)

# 3 Results

Our main technical contribution is a characterization of the measure ρ described above: With high probability with respect to ρ, the vector z in equation (2) is nearly a critical point of a certain functional associated with f.

Theorem 9 (Main Structural Theorem). Let n > 0, let f : Cn → R be a function and denote

D = D (f) (3) L1 = max {1,Lip(f)} (4) L2 = max 1, max

 ∇f (x) − ∇f (y) 1 x − y 1

. (5)

![image 20](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile20.png>)

x =y∈Cn

Denote by Xf the set

Xf = X ∈ Cn : X − tanh (∇f (X)) 1 ≤ 5000L1L32/4D1/4n3/4 , (6) where ∇f (X) is calculated by harmonically extending ∇f to Cn, and with the tanh applied entrywise to the entries of ∇f (X). Then Xnf is a ρ, 3nD11//44,L32/4 Dn11//44 -tilt-mixture such that

![image 21](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile21.png>)

![image 22](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile22.png>)

![image 23](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile23.png>)

![image 24](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile24.png>)

ρ(Xf) ≥ 1 −

3D1/4 n1/4

. (7)

![image 25](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile25.png>)

In particular, if D = o(n), then Xnf is a (ρ,o(1))-mixture with ρ(Xf) = 1 − o(1).

In other words, almost all the mass of the mixture resides on random vectors X which almost satisfy the ﬁxed point equation

X = tanh (∇f (X)) . (8)

- Remark 10. One can check that the solutions of the ﬁxed point equation are exactly the critical

points of the functional f (X) + H (X) where H (X) = i<,j Xij log Xij + (1 − Xij)log (1 − Xij) is the entropy of X. This is a variant of the functional that arises in the variational problem in [3].

- Remark 11. The following is an example application of Theorem 9 to Ising models, to be compared with the main result of [1].


- Corollary 12 (Ising models). Let f be an Ising model Hamiltonian as described in Section 2.1.1, with interaction matrix A ∈ Rn×n and a magnetic moment vector µ ∈ Rn. Denote

Xf = X ∈ Cn : X − tanh (AX + µ) 1 ≤ 5000L1L32/4D1/4n3/4 , where

![image 26](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile26.png>)

D =

√

![image 27](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile27.png>)

nTrA2 + √nµmax

![image 28](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile28.png>)

L1 = max  

1,µmax + max i∈[n]

j∈[n]

|Aij|

 



L2 = max  

1,max

i∈[n]

j∈[n]

|Aij|

 



.

Then Xnf is a ρ, 3nD11//44,L23/4Dn11//44 -tilt-mixture such that

![image 29](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile29.png>)

![image 30](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile30.png>)

ρ(Xf) ≥ 1 −

3D1/4 n1/4

![image 31](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile31.png>)

.

In particular, if L1 = O (1) and Tr A2 = o(n) (the “mean-ﬁeld assumption”), then Xf is (ρ,o(1))mixture with ρ(Xf) = 1 − o(1).

The simplest example of an Ising model is the Curie-Weiss ferromagnet, for which we can use our framework as a toy example and rederive well-known properties about its distribution.

- Corollary 13. Let β > 0 and let f : Cn → R be the Curie-Weiss Hamiltonian, f (x) = βn i =j xixj. Denote


![image 32](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile32.png>)

βJ n

≤ 5001(1 + β)2 n7/8 ,

![image 33](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile33.png>)

X

Xf = X ∈ Cn : X − tanh

![image 34](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile34.png>)

1

where J is the n × n all-1 matrix. Then Xnf is a ρ,3n−1/8,3n−1/8 -tilt-mixture, and ρ(Xf) ≥

- 1 − 3n−1/8. Further, if β < 1, then every X ∈ Xf satisﬁes


(1 + β)2 1 − β

n7/8.

X 1 ≤ 5001

![image 35](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile35.png>)

For a more detailed application of Theorem 9 for the case of exponential random graphs, see [5]. The following theorem ﬁnds suﬃcient conditions under which composing f with a real-valued

function produces a Hamiltonian with aρ-mixture approximation:

Theorem 14 (Composition Theorem). Let h : R → R be a twice diﬀerentiable function satisfying

h′ (x) < B1 ∀x ∈ R h′′ (x) < B2 ∀x ∈ R.

Let f : Cn → R be a function with parameters D, L1, and L2 as described in Theorem 9. Denote by D˜, L˜1, L˜2 and L˜3 the real numbers

D˜ = B1D + B2L21n

- L˜1 = max{1,B1L1}
- L˜2 = max 1,B1L2 + 3B2L21n L ˜3 = 2B2L21n3/2


and denote by X˜h◦f the set

X˜h◦f = X ∈ Cn : X − tanh h′ (f (X))∇f (X) 1 ≤ 5000L˜1L˜32/4D˜1/4n3/4 + L˜3 , (9) where ∇f (X) is calculated by harmonically extending ∇f to Cn, and with the tanh applied entrywise to the entries of ∇f (X). Then Xnh◦f is a ρ, 3nD˜11//44,L˜32/4Dn˜11//44 -tilt-mixture such that

![image 36](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile36.png>)

![image 37](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile37.png>)

![image 38](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile38.png>)

![image 39](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile39.png>)

3D˜1/4 n1/4

ρ(Xh◦f) ≥ 1 −

.

![image 40](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile40.png>)

Remark 15. Theorem 14 bounds the norm X − tanh (h′ (f (X)) ∇f (X)) 1 rather than

X − tanh (∇(h ◦ f)(X)) 1 (which is the analogue of the quantity arising in the main Theorem 9). This is a matter of practicality: For many known Hamiltonians f it is easy to compute ∇f and its extension to Cn, but it is not straightforward to compute ∇(h ◦ f)(X) and its extension to Cn for arbitrary h. In these cases, calculating h′ (f (X))∇f (X) is a much simpler task. Further, as will be shown in Lemma 25, the two quantities h′ (f (X))∇f (X) and ∇(h ◦ f)(X) are close to each other.

![image 41](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile41.png>)

![image 42](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile42.png>)

As an example application of Theorem 14, we show that the conditional distribution Pr [Y = y | f (y) ≥ tn] described in item (2) in Section 2.1.2 can be approximated by a “smoothedout” distribution, which gives equal mass to vectors y satisfying f (y) ≥ nt and no mass to vectors y satisfying f (y) < (t − δ) n. This “smoothed-out” distribution is obtained from a “smoothed-cutoﬀ” approximation to the f˜described in Section 2.1.2. Our framework can be applied to this “smoothedcutoﬀ” function, yielding an equation corresponding to the Lagrange multiplier problem associated with the rate function.

Theorem 16 (Large deviations). Let t > 0. Let f : Cn → R be a Hamiltonian with parameters D, L1 and L2 as described in Theorem 9, and assume that there exists z ∈ Cn such that f (z) ≥ tn. Let δ > 0. There exists a monotone function h : R → R, such that for ϕ = h ◦ f, we have that ϕ(y) = 0 if f (y) < (t − 2δ) n, ϕ(y) = 1 if f (y) ≥ tn and such that the following holds. Denote by σ the measure deﬁned by

ϕdµ Cn ϕdµ

dσ =

,

![image 43](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile43.png>)

and let Xϕ be a random variable whose law is σ. Denote

Xg = X ∈ Cn : ∃λ ∈ Rs.t. X − tanh (λ∇f (X)) 1 ≤ 5000L˜1L˜32/4D˜1/4n3/4 + L˜3

![image 44](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile44.png>)

and f (X) ∈ [(t − 6δ) n,tn]} where

2 δ2

2 δ

D˜ =

L21 L˜1 = max 1,

D +

![image 45](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile45.png>)

![image 46](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile46.png>)

2 δ

L1

![image 47](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile47.png>)

- L ˜2 = max 1,

2 δ

![image 48](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile48.png>)

L22 + 3

2 δ2

![image 49](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile49.png>)

L21

- L ˜3 = 2


2 δ2

L21n1/2.

![image 50](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile50.png>)

Then Xϕ is a ρ,80Dn˜11//44 + 8 · 2−n -mixture such that

![image 51](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile51.png>)

165L1D˜1/4 n1/42δ

ρ(Xg) ≥ 1 −

![image 52](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile52.png>)

1 −

L1 2δ√n − 2−n

![image 53](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile53.png>)

![image 54](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile54.png>)

−1

. (10)

Note that the expression X −tanh(λ∇f (X)) in the deﬁnition of the set Xg is closely related to the rate function: Consider the variational problem

minimizeH (Y ) subject to Ef (Y ) ≥ tn

where Y is a random vector in Cn whose entries are independent. By monotonicity, the minimum is attained on the boundary of the constraint. Denoting EY = y and using the method of Lagrange multipliers, we obtain the equations

∇yH (Y ) = λ∇f (y) (11) f (y) = tn.

Applying the fact that ∇yH (Y ) = tanh−1 (y) on equation (11) gives exactly the equation X − tanh (λ∇f (X)) = 0.

Example 17 (Large deviations for triangle counts). Let N > 0 be an integer representing the number of vertices of a graph, and let n = N2 be the number of possible edges in the graph. We treat each vector v ∈ Cn as a simple graph, with ve = 1 if and only if the edge e appears in the graph. This in turns gives an adjacency matrix (xij)Ni,j=1 with xij = 1 if and only if v{ij} = 1. In this setting, let f be a triangle-counting function,

β N i =j =k

xijxjkxki

f (x) =

![image 55](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile55.png>)

for some real β. It is shown in [4] that D (f) is O n3/4 and in [5] that L1 and L2 are bounded by 200|β|. Thus we can apply Theorem 16 to f, concluding that for a ﬁxed t > 0 there exists some δ = o(1) and a smoothed cutoﬀ function h with h(x) = 1 for x > tn and h(x) = 0 for x < (t − δ)n and such that the random graph G whose density is proportional to h◦f is a (ρ,o(1))-mixture such that ρ(Xg) = 1 − o(1), where

Xg = X ∈ Cn : ∃λ ∈ Rs.t. X − tanh λX2 1 ≤ εn and f (X) ∈ [(t − 6δ) n,tn]}

![image 56](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile56.png>)

for some ε = o(1). Here X ∈ Cn is treated as an n×n symmetric matrix with zeros on the diagonal, and we understand the expression X2 as the usual matrix multiplication, with zeros on the diagonal as well. We conjecture that all of the points of the set Xg are close to the solutions obtained by Lubetzky and Zhao in [6].

![image 57](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile57.png>)

Our results extend to triangle counts on sparse graphs as well. In this case, expected value of f is of order np3, which decays to 0 as p → 0. We should therefore take both t to be proportional to p3 and δ to be o p3 . Since the bound on the vectors in Xg in Theorem 16 is polynomial in δ, we can consider large deviations for graphs whose edge probabilities are proportional to p ∼ n−c for some constant c (for example, if we wish ε to be of order p, we can take p ∼ n−1/160).

The rest of this paper is organized as follows. Theorem 9 is proved in Section 4, while Theorem

- 14 is proved in Section 5. Corollaries 12 and 13 are proved in Section 6.1 and 16 is proved in Section 6.2.


# 4 Proof of main theorem

## 4.1 Notation and review

We use the notation from [4], and rely on the proofs therein. Here is a brief review of the required terms and bounds.

For a probability measure ν on Cn, we deﬁne fν = log (dν/dµ), so that the Gibbs distribution with Hamiltonian fν is exactly ν. For every distribution ν on the hypercube (exponential or otherwise), we deﬁne

⊗2

tanh (∇fν (y))⊗2 dν −

,

tanh (∇fν (y)) dν

H(ν) =

Cn

Cn

which should be thought of as the covariance matrix of the random variable ∇fν (X) with X ∼ ν. We will use the following three results from [4].

- Proposition 18 (Proposition 17 in [4]). Let ν˜ be a probability distribution on Cn. Then there exists a product measure ξ = ξ (˜ν) such that


![image 58](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile58.png>)

W1 (˜ν,ξ) ≤ nTr(H (˜ν)). (12) Moreover, one may take ξ to be the unique product measure whose center of mass lies at

Cn tanh (∇fν˜ (y))dν˜ (y) where the tanh is applied entrywise.

- Proposition 19 (Proposition 18 together with Lemma 16 in [4]). Deﬁne D = D (fν). Let ε ∈


0,1/4 log (4n/D) . Let ν be a probability measure on Cn and deﬁne f = log dµdν . Then there exists a measure m on B (0,ε√n) ∩ [−1/4,1/4]n, such that ν admits the decomposition

![image 59](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile59.png>)

![image 60](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile60.png>)

![image 61](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile61.png>)

ϕdν =

Cn

ϕdτθ (ν) dm(θ) (13)

B(0,ε√n) Cn

![image 62](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile62.png>)

for every test function ϕ : Cn → R, and which satisﬁes

n1/3D2/3 ε2/3 ≥ 1 −

3D1/3 n1/3ε1/3

. (14)

m θ : Tr(H(τθν)) ≤ 256

![image 63](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile63.png>)

![image 64](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile64.png>)

Lemma 20 (Lemma 24 in [4]). Let θ ∈ Rn and let ν,ν˜ be probability measures on Cn. Deﬁne

⊗2

tanh (∇fν (y))⊗2 dν˜ −

tanh (∇fν (y)) dν˜

A =

Cn

Cn

and

⊗2

tanh (∇fτθν (y))⊗2 dν˜ −

. Then

tanh (∇fτθν (y)) dν˜

B =

Cn

Cn

e−4 θ ∞TrB ≤ TrA ≤ e4 θ ∞TrB.

We can now describe the general plan of our proof. Fix ε > 0, and let m be the measure obtained from Proposition 19. Denote by Θ the set

n1/3D2/3 ε2/3

Θ = θ ∈ Rn : Tr (H (τθν)) ≤ 256

![image 65](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile65.png>)

. (15)

For every θ ∈ Rn, denote by ξθ the unique product measure with the same marginals as τθν, and by A(θ) the vector

A(θ) = EX∼τθν [X]. Denote by ρ the push-forward of the measure m under the map θ  → A(θ) and deﬁne

X = {A(θ);θ ∈ Θ}.

In order to prove Theorem 9, all we have to do is that show that for each θ ∈ Θ, the corresponding A(θ) is close in the one-norm to tanh (∇f (A(θ))); this will show equation (7). In other words, we need the following proposition:

- Proposition 21. Let θ ∈ Θ and let Y ∼ ξθ. Then for every ε > 0,


n2/3D1/3 ε1/3

tanh (∇f (EY )) − EY 1 ≤ 41L1 112L2

+ εn .

![image 66](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile66.png>)

Relying on the above, we can prove of Theorem 9.

1/4L32/4

Proof of Theorem 9. Deﬁne the measure ρ and the set X as above. Set ε = D

n1/4 . Items (1)-(3) in deﬁnition 7 follow immediately from Proposition 18 and 19 by choice of ε, δ and ρ. By Proposition 21 for all θ ∈ Θ, we have

![image 67](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile67.png>)

tanh (∇f (EY )) − EY 1 ≤ 41L1 113L32/4D1/4n3/4

≤ 5000L1L32/4D1/4n3/4. This implies that X ⊆ Xf, and together with Proposition 19 and by choice of ε, this shows that ρ(Xf) ≥ 1 − 3nD11//44, satisfying equation (7).

![image 68](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile68.png>)

![image 69](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile69.png>)

![image 70](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile70.png>)

![image 71](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile71.png>)

![image 72](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile72.png>)

The rest of this section is devoted to proving Proposition 21.

## 4.2 Approximate ﬁxed point

Let θ ∈ Θ be a tilt and let ξθ be the product measure whose center of mass lies at

Cn tanh (∇fτθν (y)) dτθν (y). Throughout the proof we will assume X ∼ τθν and Y ∼ ξθ. A direct calculation shows that under this notation, EY = Etanh(∇f (X) + θ):

tanh (∇fτθν (y)) dτθν (y)

EY =

Cn

dτθν dν

tanh ∇ log

=

+ log

![image 73](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile73.png>)

Cn

tanh (θ + ∇fν (y)) dτθν (y)

=

Cn

= Etanh (∇f (X) + θ). This gives

dν dµ

![image 74](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile74.png>)

(y) dτθν (y)

EY − Etanh (∇f (X)) 1 ≤ Etanh (∇f (X)) − Etanh(∇f (X) + θ) 1 ≤ θ 1

θ 2 ≤ ε√n ≤ εn. (16) where in the second inequality we use the fact that

![image 75](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile75.png>)

|tanh (x) − tanh (y)| ≤ |x − y|. (17)

- Proposition 22. Let Y ∼ ξθ. Then


n2/3D1/3 ε1/3

+ εn.

E tanh (∇f (Y )) − EY 1 ≤ 64L2

![image 76](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile76.png>)

Proof. For X ∼ τθν, consider the random variable Z = tanh (∇f (X)) − Etanh (∇f (X)) 22. A

short calculation shows that the expectation of Z is roughly TrH (τθν): EZ = E tanh (∇f (X)) − Etanh (∇f (X)) 22

n

n

(Etanh (∇f (X))i)2

E tanh (∇f (X))2i −

=

i=1

i=1

n

n

(Etanh (∇f (X) + θ)i)2

E tanh (∇f (X) + θ)2i −

≤ 3

i=1

i=1

= 3Tr (H (τθν))

where the inequality is by Lemma 20 with ν and ν˜ = τθν and the fact that θ ∞ ≤ 1/4. Thus by equation (14),

n1/3D2/3 ε2/3

E tanh (∇f (X)) − Etanh(∇f (X)) 22 ≤ 3 · 256

, and together with the Cauchy-Schwarz inequality, we have that

![image 77](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile77.png>)

√nE tanh (∇f (X)) − Etanh (∇f (X)) 2 ≤ 32

![image 78](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile78.png>)

E tanh (∇f (X)) − Etanh(∇f (X)) 1 ≤

n2/3D1/3 ε1/3

. (18)

![image 79](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile79.png>)

By Proposition 18, there exists a coupling between τθν and ξθ such that

![image 80](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile80.png>)

E X − Y 1 ≤ 2 nTrH (τθν) (by equation (14)) ≤ 32

n2/3D1/3 ε1/3

.

![image 81](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile81.png>)

Thus, since by equations (5) and (17),

E tanh (∇f (X)) − tanh (∇f (Y )) 1 ≤ E ∇f (X) − ∇f (Y ) 1 ≤ L2E X − Y 1 ≤ 32L2

n2/3D1/3 ε1/3

. (19)

![image 82](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile82.png>)

Combining equations (18), (16) and (19) together with the triangle inequality ﬁnally gives

n2/3D1/3 ε1/3

+ εn

E tanh (∇f (Y )) − EY 1 ≤ 32(1 + L2)

![image 83](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile83.png>)

n2/3D1/3 ε1/3

≤ 64L2

+ εn

![image 84](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile84.png>)

as needed. Lemma 23. Let Z be an almost-surely bounded random variable, |Z| ≤ L with L ≥ 1. Then

|tanh (EZ) − Etanh (Z)| ≤ 20L · E|tanh (Z) − Etanh (Z)| . The proof is postponed to the appendix.

![image 85](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile85.png>)

![image 86](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile86.png>)

![image 87](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile87.png>)

![image 88](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile88.png>)

Claim 24. Let ξ be a product measure on Cn, let Y ∼ ξ, and let f : Cn → R be a function on the hypercube. Then

Ef (Y ) = f (EY ) (20) and

E∇f (Y ) = ∇f (EY ). (21) Proof. The extension of f to Cn is deﬁned by the Fourier decomposition

![image 89](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile89.png>)

fˆ(S)

yi.

f (y) =

i∈S

S⊆[n]

Thus, since ξ is a product measure, Ef (Y ) = E

fˆ(S)

fˆ(S)

EYi = f (EY ).

Yi =

i∈S

i∈S

S⊆[n]

S⊆[n]

Equation 21 is then obtained by applying equation 20 to every component of ∇f. Proof Proposition 21. By the triangle inequality,

![image 90](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile90.png>)

![image 91](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile91.png>)

![image 92](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile92.png>)

![image 93](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile93.png>)

tanh (∇f (EY )) − EY 1 ≤ tanh (∇f (EY )) − Etanh(∇f (Y )) 1 + Etanh (∇f (Y )) − EY 1 (by Claim 24 ) = tanh (E∇f (Y )) − Etanh(∇f (Y )) 1 + Etanh (∇f (Y )) − EY 1 (by convexity) ≤ tanh (E∇f (Y )) − Etanh(∇f (Y )) 1 + E tanh (∇f (Y )) − EY 1 .

(22) Proposition 22 gives a bound on the second term in the right hand side.

For the ﬁrst term, note that by equation (4), for every index j ∈ [n],

∇f (Y )j ≤ L1. We can therefore invoke Lemma 23 on every index, giving that

n

tanh (E∇f (Y ))j − Etanh (∇f (Y ))j

tanh (E∇f (Y )) − Etanh (∇f (Y )) 1 =

j=1

n

(by Lemma 23) ≤ 20L1

E tanh (∇f (Y ))j − Etanh ∇f (Y )j

j=1

= 20L1E tanh (∇f (Y )) − Etanh(∇f (Y )) 1 . (23) For this last term, we again use the triangle inequality and equation (16), giving

E tanh (∇f (Y )) − Etanh(∇f (Y )) 1 ≤ E tanh (∇f (Y )) − Etanh (∇f (X)) 1 +

+ E Etanh (∇f (X)) − Etanh (∇f (Y )) 1 ≤ εn + E tanh (∇f (Y )) − EY 1 +

+ E tanh (∇f (X)) − tanh (∇f (Y )) 1

which, by Proposition 22 and equation (19), gives

n2/3D1/3 ε1/3

+ εn

E tanh (∇f (Y )) − Etanh (∇f (Y )) 1 ≤ εn + 64L2

![image 94](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile94.png>)

n2/3D1/3 ε1/3 ≤ 96L2

+ 32L2

![image 95](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile95.png>)

n2/3D1/3 ε1/3

+ 2εn.

![image 96](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile96.png>)

Putting this into equation (23), we have

n2/3D1/3 ε1/3

tanh (E∇f (Y )) − Etanh(∇f (Y )) 1 ≤ 40L1 48L2

+ εn .

![image 97](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile97.png>)

And ﬁnally, plugging in the bounds into equation (22), we get

n2/3D1/3 ε1/3

+ εn

tanh (∇f (EY )) − EY 1 ≤ 40L1 48L2

![image 98](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile98.png>)

n2/3D1/3 ε1/3

+ 64L2

+ εn

![image 99](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile99.png>)

n2/3D1/3 ε1/3

+ εn .

≤ 41L1 112L2

![image 100](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile100.png>)

![image 101](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile101.png>)

![image 102](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile102.png>)

![image 103](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile103.png>)

![image 104](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile104.png>)

# 5 Proof of composition theorem

We will use two lemmas concerning the relation between f and h ◦ f. The ﬁrst is a discrete chain rule which will be central to our calculations:

- Lemma 25 (Chain rule for discrete gradient). Let f : Cn → R with Lip(f) = L and let h : R → R with |h′′ (x)| < B. Then


- 1. For ever y ∈ Cn, ∇(h ◦ f)(y) − h′ (f (y))∇f (y) 1 ≤ BL2n (24)

and

∇(h ◦ f)(y) − h′ (f (y)) ∇f (y) 2 ≤ BL2√n. (25)

![image 105](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile105.png>)

- 2. For every x ∈ Cn, ∇(h ◦ f)(x) − h′ (f (x)) ∇f (x) 1 ≤ 2BL2n3/2. (26)


![image 106](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile106.png>)

The second lemma concerns the parameters of the function h ◦ f:

- Lemma 26 (Composition parameters). Let h : R → R be a twice diﬀerentiable function satisfying


h′ (x) ≤ B1 h′′ (x) ≤ B2

for all x ∈ R. Let f : Cn → R be a function with parameters D, L1, L2 as described in Theorem 9. Then

D (h ◦ f) ≤ B1D + B2L21n (27) Lip(h ◦ f) ≤ B1L1 (28)

 ∇(h ◦ f)(x) − ∇(h ◦ f)(y) 1

x − y 1 ≤ B1L2 + 3B2L21n. (29) The proofs of both lemmas are postponed to the appendix.

max

![image 107](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile107.png>)

x =y∈Cn

Proof of Theorem 14. Denote by Xh◦f the set

Xh◦f = X ∈ [−1,1]n : X − tanh (∇(h ◦ f)(X)) 1 ≤ 5000L˜1L˜32/4D˜1/4n3/4 . Note that for every X ∈ Xh◦f,

X − tanh h′ (X) ∇f (X) 1 ≤ X − tanh (∇(h ◦ f)(X)) 1

+ tanh (∇(h ◦ f)(X)) − tanh h′ (X) ∇f (X) 1 (by equation (26)) ≤ 5000L˜1L˜32/4D˜1/4n3/4 + 2B2L21n3/2

and so X˜h◦f ⊆ Xh◦f. Applying Theorem 9 for the function h ◦ f with the bounds given by Lemma 26 gives the required results.

![image 108](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile108.png>)

![image 109](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile109.png>)

![image 110](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile110.png>)

![image 111](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile111.png>)

Remark 27. The bound for compositions h ◦ f with domain Cn, given in (26), is worse by a factor of √n than that of compositions with domain Cn, given in (24). This disparity is in fact tight. For example, consider the function

![image 112](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile112.png>)

![image 113](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile113.png>)

 

- 3

![image 114](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile114.png>)

- 4x3 − 14x5 |x| < 1


![image 115](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile115.png>)

- 1

![image 116](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile116.png>)

- 2x2 x ≥ 1 −12x2 x ≤ −1


h(x) =



![image 117](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile117.png>)

applied to the “counting” function

n

xi.

f (x) =

i=1

The function h has a bounded second derivative and satisﬁes h′ (0) = 0. For x = 0, we have f (x) = 0 and so h′ (f (x))∇f (x) = 0 as well. However, a calculation shows that  ∇(h ◦ f)(x) 1 ∼ n3/2, and so  ∇(h ◦ f)(x) − h′ (f (x))∇f (x) 1 ∼ n3/2 as well.

# 6 Example applications

## 6.1 The Ising model

- Proof of Corollary 12. A short calculation shows that ∇f (x) = Ax + µ. The corollary will follow

immediately from Theorem 9 once we have obtained the parameters D, L1 and L2 for f. The calculations for D (f) and Lip(f) are also found in [4, Section 1.3] but we repeat them here for completeness.

Denote µmax = maxi∈[n] |µi|. We then have

- 1. The Gaussian-width is bounded by:

D (f) = E sup

x∈Cn

Ax + µ,Γ ≤ E sup

x∈Cn

Ax,Γ + E| µ,Γ | ≤

√nE sup

![image 118](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile118.png>)

x∈B(0,1)

Ax,Γ + µ 2

= √nE AΓ 2 + µ 2 ≤ nE AΓ 22 + µ 2 ≤

![image 119](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile119.png>)

![image 120](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile120.png>)

√

![image 121](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile121.png>)

nTrA2 + √nµmax.

![image 122](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile122.png>)

- 2. The Lipschitz constant is bounded by

Lip (f) ≤ µmax + max

i∈[n],x∈Cn

Ax,ei ≤ µmax + max

i∈[n]

j∈[n]

|Aij|.

- 3. Regarding the Lipschitz constant of the gradient, note that  ∇f (x) − ∇f (y) 1 =


A(x − y) 1. Suppose that x and y diﬀer only in the i-th coordinate. Then A(|x − y|) is just 2 times the i-th column of A. By the triangle inequality, we then have

 ∇f (x) − ∇f (y) 1 x − y 1 ≤ max

![image 123](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile123.png>)

i∈[n]

j∈[n]

|Aij| .

![image 124](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile124.png>)

![image 125](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile125.png>)

![image 126](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile126.png>)

![image 127](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile127.png>)

- Proof of Corollary 13. The interactions described in Corollary 13 can be represented by an interac-


tion matrix A = βn1, where 1 is the n×n matrix whose oﬀ-diagonal entries are 1 and whose diagonal is 0, and β is interpreted as the inverse temperature. Note that for every x,y ∈ Cn,

![image 128](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile128.png>)

 ∇f (x) − ∇f (y) 1 = A(x − y) 1 ≤ β x − y 1 , (30) so that L2 ≤ 1 + β. A simple calculation also shows that D ≤ β√n and L1 ≤ 1 + β. Denoting

![image 129](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile129.png>)

β1 n

≤ 5000(1 + β)2 n7/8 ,

![image 130](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile130.png>)

X

X = X ∈ Cn : X − tanh

![image 131](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile131.png>)

1

by Corollary 12 we have that Xnf is a ρ,3n−1/8,3n−1/8 -tilt-mixture with ρ(X) ≥ 1 − 3n−1/8. Denote by J = 1 + Id the n × n matrix whose every entry is 1. Then every X ∈ X also satisﬁes

β1 n

β1 n

βJ n

βJ n

= X − tanh

X

X − tanh

X + tanh

X

X − tanh

![image 132](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile132.png>)

![image 133](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile133.png>)

![image 134](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile134.png>)

![image 135](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile135.png>)

1

1 ≤ 5000(1 + β)2 n7/8 + tanh

β (1 + Id) n

β1 n

X − tanh

X

![image 136](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile136.png>)

![image 137](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile137.png>)

1

- ≤ 5000(1 + β)2 (1 + β) n7/8 +

βId n

![image 138](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile138.png>)

X

1

- ≤ 5001(1 + β)2 n7/8.


Thus X ⊆ Xf and the ﬁrst part of Corollary 13 is proved. The ﬁxed point equation X = tanh βnJ X is easier to work with, since all of its exact solutions are constant: Indeed, every entry Xi of a solution satisﬁes Xi = tanh nj=1 nβXj ; every solution X is then of the form X = (x,x,... ,x), and the exact ﬁxed point vector equation reduces to the scalar equation

![image 139](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile139.png>)

![image 140](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile140.png>)

x = tanh (βx).

The value x0 = 0 is always a solution, corresponding to the case where the typical conﬁguration is completely disordered.

For β ≤ 1, this is also the only solution. In this case, for every X ∈ Xf,

βJ n

βJ n

X + tanh

X

X 1 = X − tanh

![image 141](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile141.png>)

![image 142](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile142.png>)

1 ≤ 5001(1 + β)2 n7/8 + tanh

βJ n

X

![image 143](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile143.png>)

1 ≤ 5001(1 + β)2 n7/8 + β X 1 .

Rearranging, we get that every X ∈ Xf is close to 0:

(1 + β)2 1 − β

n7/8.

X 1 ≤ 5001

![image 144](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile144.png>)

This represents the fact that for high temperatures, the system is always disordered.

For β > 1, there are two other solutions, x1 = −x2. These satisfy |x1|,|x2| → 1 as β → ∞, and correspond to the symmetry-broken phase where all spins tend to point in the same direction. Showing that every X ∈ Xf is close to either (x1,x1,... ,x1) or (x2,x2,... ,x2) can then be done by a standard counting argument, which we choose to omit.

![image 145](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile145.png>)

![image 146](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile146.png>)

![image 147](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile147.png>)

![image 148](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile148.png>)

Adding a constant magnetic ﬁeld µ = (µ0,µ0 ... ,µ0) forces a non-zero constant solution for every β > 0, while shifting the values of x1 and x2.

## 6.2 Large deviations

In order to prove Theorem 16, we follow the approach mentioned in Section 2.1.2, and try to approximate function f˜ in equation (1) by a well-behaved Hamiltonian g.

Let t ∈ R and δ > 0. Let h : R → R and ψ : R → R be deﬁned as

 

2x + 1 x ≤ −1 −x2 −1 ≤ x ≤ 0 0 x ≥ 0.

h(x) =



and

x n − t /δ .

ψ (x) = n · h

![image 149](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile149.png>)

Note that |h′ (x)| ≤ 2 and |h′′ (x)| ≤ 2 for all x ∈ R. Thus

x n − t /δ ·

1 nδ ≤

ψ′ (x) = n · h′

![image 150](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile150.png>)

![image 151](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile151.png>)

2 δ

![image 152](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile152.png>)

and

Let g : Cn → R be deﬁned as

x n − t /δ ·

1 n2δ2 ≤

ψ′′ (x) = n · h′′

![image 153](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile153.png>)

![image 154](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile154.png>)

2 nδ2

.

![image 155](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile155.png>)

g (y) = ψ (f (y)) .

Denote by ν the measure deﬁned by Xng. The function g is an approximation for f˜, in the sense that almost of all the mass of ν is supported on vectors on which f attains a large value.

- Proposition 28. Let δ′ = log 4+12 δ and deﬁne B = y ∈ Cn : f (y) ≤ t − δ′ n .


![image 156](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile156.png>)

If there exists a z ∈ Cn such that f (z) ≥ tn, then

ν (B) ≤ 2−n. Proof. Let y ∈ B. By deﬁnition of g,

f (y)

n − t /δ (h is increasing) ≤ n · h

g (y) = n · h

![image 157](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile157.png>)

(t − δ′) n n − t /δ

![image 158](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile158.png>)

= n · h −δ′/δ since δ′ > δ = n 1 − 2

δ′ δ

![image 159](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile159.png>)

= −(log 4) n.

Let z ∈ Cn be such that f (z) ≥ tn. Then under ν the probability for obtaining z is proportional to eg(z) = e0 = 1. On the other hand, for every y ∈ B, the probability for obtaining y is proportional

to a value smaller than e−log 4·n = 4−n = 2−2n. Since there are no more than 2n possible vectors in Cn, we thus obtain

ν (B) ν (z) ≤ 2n2−2n = 2−n.

ν (B) ≤

![image 160](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile160.png>)

![image 161](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile161.png>)

![image 162](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile162.png>)

![image 163](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile163.png>)

![image 164](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile164.png>)

Proposition 28 allows us to approximate ν with a distribution that does not give any mass at all to vectors y ∈ Cn with f (y) < (t − δ′) n. Deﬁne the function ϕ : Cn → R by

 

0 f (y) < (t − δ′) n eg(y) (t − δ′)n ≤ f (y) < tn 1 f (y) ≥ tn,

ϕ(y) =



and observe that ϕ(y) agrees with eg(y) for all y such that f (y) ≥ (t − δ′)n. Denote by σ the measure deﬁned by dσ = ϕdµ

Cn ϕdµ and by Xϕ a random variable whose law is σ.

![image 165](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile165.png>)

- Proposition 29. Assume that there exists a z ∈ Cn such that f (z) ≥ tn. Then there exists a coupling between Xng and Xϕ such that


E Xng − Xϕ 1 ≤ 2n · 2−n. We postpone the proof to the appendix.

Proof of Theorem 16. Applying Theorem 14 to g, there exists a ρ-mixture and a coupling between X (ρ) and Xng such that

80D˜1/4 n1/4

(31) and

ρ(Xg) ≥ 1 −

![image 166](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile166.png>)

E X (ρ) − Xng 1 ≤ 80n3/4D˜1/4. Therefore by Proposition 29 there exists a coupling between X (ρ) and Xϕ such that

E X (ρ) − Xϕ 1 ≤ 80n3/4D˜1/4 + 2n · 2−n.

This shows that Xϕ is a ρ,80Dn˜11//44 + 8 · 2−n -mixture. To obtain equation (10), denote Yg = {X ∈ Xg : f (X) < (t − 3δ′)n}, and let X ∈ Yg. Denote by ξX the product measure on Cn such that if YX ∼ ξX then EYX = X. We then have

![image 167](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile167.png>)

Pr f (YX) ≥ t − 2δ′ n ≤ Pr f (YX) ≥ f (EYX) + δ′n

≤ Pr |f (YX) − f (EYX)| ≥ δ′n (by Markov’s inequality) ≤

E|f (YX) − f (EYX)| δ′n (by Proposition 32 ) ≤

![image 168](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile168.png>)

L1 δ′√n

. (32)

![image 169](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile169.png>)

![image 170](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile170.png>)

Denote by AX the event AX = f (YX) < t − 2δ′ n ∩ f (Xng) > t − δ′ n .

Equation (32) and Proposition 28 together imply that

L1

δ′√n − 2−n. Under AX we have that

Pr [AX] ≥ 1 −

![image 171](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile171.png>)

![image 172](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile172.png>)

δ′n ≤ f (Xng) − f (YX) ≤ L1 YX − Xng 1 , yielding

δ′n L1

YX − Xng 1 ≥

. (33)

![image 173](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile173.png>)

Since E X (ρ) − Xng 1 is small, this inequality sets a constraint on the measure of Yg. Letting Z be a random variables with law ρ, coupled with X (ρ) so that X (ρ) | Z ∼ YZ, one has

E X (ρ) − Xng 1 =

E[ YZ − Xng 1 | Z]dρ(Z) ≥

![image 174](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile174.png>)

Cn

E[ YZ − Xng 1 | Z]dρ(Z)

Yg

E[ YZ − Xng 1 | Z ∧ AZ]Pr [AZ] dρ(Z)

≥

Yg

δ′n L1

L1 δ′√n − 2−n

(by equation (33)) ≥ 1 −

dρ(Z)

![image 175](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile175.png>)

![image 176](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile176.png>)

![image 177](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile177.png>)

Yg

δ′n 2L1

L1 δ′√n − 2−n ρ(Yg)

= 1 −

.

![image 178](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile178.png>)

![image 179](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile179.png>)

![image 180](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile180.png>)

We thus obtain

−1

80L1D˜1/4 n1/4δ′

L1 δ′√n − 2−n

1 −

ρ(Yg) ≤

. Together with equation (31), this gives

![image 181](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile181.png>)

![image 182](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile182.png>)

![image 183](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile183.png>)

as needed.

161L1D˜1/4 n1/4δ′

ρ(Xg\Yg) ≥ 1 −

![image 184](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile184.png>)

L1 δ′√n − 2−n

1 −

![image 185](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile185.png>)

![image 186](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile186.png>)

−1

![image 187](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile187.png>)

![image 188](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile188.png>)

![image 189](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile189.png>)

![image 190](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile190.png>)

- Remark 30. A particular type of Hamiltonian that has been of considerable interest in the ﬁeld of large deviations that of subgraph-counting functions. It was recently shown in [5] that for these types of Hamiltonians, ∇f (X) is close to a stochastic block matrix. Since h′ f(nX) − t /δ is a scalar, this implies that every X ∈ Xg is also close to a stochastic block matrix.

![image 191](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile191.png>)

- Remark 31. Theorem 16 corresponds to the unconditioned distribution µp with p = 1/2. To deal with the case p = 1/2, deﬁne g (y) as


- 1

![image 192](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile192.png>)

- 2


(1 − yi + 2pyi) . Analogues of Propositions 28 and 29 can then be proved following the same line.

g (y) = ψ (f (y)) + log

# 7 Acknowledgments

The ﬁrst author is grateful to Sourav Chatterjee for inspiring him to work on this topic and for an enlightening discussion. We thank Amir Dembo and Sumit Mukherjee for insightful discussions, and Yufei Zhao for his motivating comments on sparse bounds. Finally we thank the anonymous referee for comments improving the presentation of this work.

# References

- [1] Anirban Basak and Sumit Mukherjee. Universality of the mean-ﬁeld for the potts model. Probability Theory and Related Fields, 168(3):557–600, Aug 2017.
- [2] Sourav Chatterjee and Amir Dembo. Nonlinear large deviations. arXiv:1401.3495, January 2014.
- [3] Sourav Chatterjee and Persi Diaconis. Estimating and understanding exponential random graph models. Ann. Statist., 41(5):2428–2461, October 2013.
- [4] Ronen Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations. arXiv:1612.04346, December 2016.
- [5] Ronen Eldan and Renan Gross. Exponential random graphs behave like mixtures of stochastic block models. arXiv:1707.01227, July 2017.
- [6] Eyal Lubetzky and Yufei Zhao. On the variational problem for upper tails in sparse random graphs. Random Structures Algorithms, 50(3):420–436, 2017.
- [7] Ryan O’Donnell. Analysis of Boolean Functions. Cambridge University Press, New York, NY, USA, 2014.
- [8] Gerhard Winkler. Extreme points of moment sets. Mathematics of Operations Research, 13(4):581–587, 1988.


# A Appendix

Proof of Lemma 23. Denote Y = tanh Z, and denote the bound of Y by α = tanh L ≥ tanh (1). Under this notation, we wish to show that

tanh Etanh−1 Y − EY ≤ 20tanh−1 (α) · E|Y − EY |. (34)

We will prove this inequality by considering it as a variational problem on the distribution µ of Y . Speciﬁcally, we will show that for every a ∈ [−α,α], every distribution µ of Y satisﬁes

tanh Etanh−1 Y − a ≤ 20tanh−1 (α) · E|Y − a|. (35) Setting a = EY then gives the desired result.

Suppose that E|Y − a| is ﬁxed. Then the left hand side of (35) is maximized by the Y that gives tanh Etanh−1 Y an extremal value, conditioned on b := E|Y − a| being constant. Since tanh is monotone, this is equivalent to ﬁnding the extremal value of the integral

tanh−1 (x)dµ(x) (36)

while maintaining the constraint

b = E|Y − a|. (37)

The constraint (37) is of the form f (x)dµ = b, where f (x) = |x − a|. By Theorems 2.1 and 3.2 and Proposition 3.1 in [8], the extremal distributions which solve a system of n constraints of the form fi (x)dµ = ci are linear combinations of no more than n+1 singletons, i.e delta distributions. We can therefore write the extremal µ as

µ = pδ (x) + (1 − p) δ (y) (38)

for some two real numbers −α ≤ x,y ≤ α and p ∈ [0,1]. Now, using the triangle inequality, we have that

tanh Etanh−1 Y − a ≤ tanh Etanh−1 Y − EY + E|Y − a|, so it is in fact enough to show that

tanh Etanh−1 Y − EY ≤ 19tanh−1 (α) · E|Y − a| , and since E|Y − EY | ≤ 2E|Y − a| for every a, it actually suﬃces to show that

tanh Etanh−1 Y − EY ≤ 9tanh−1 (α) · E|Y − EY |. (39) Plugging the decomposition (38) into (39), we need to prove that for every such x and y,

tanh ptanh−1 (x) + (1 − p)tanh−1 (y) − (px + (1 − p)y) 2p(1 − p)|x − y|tanh−1 (α) ≤ 9.

![image 193](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile193.png>)

Assume without loss of generality that x > 0 and x > |y|. We will now show that inequality is correct for 0 < p ≤ 12. We omit the similar proof for 12 ≤ p < 1. For these values of p, it suﬃces to show that

![image 194](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile194.png>)

![image 195](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile195.png>)

tanh ptanh−1 (x) + (1 − p)tanh−1 (y) − (px + (1 − p)y)

ptanh−1 (α) (x − y) ≤ 9· (40) For every ﬁxed value of y, we treat the expression on the left hand side as a function of p for p ∈ (0,1). This expression may attain its supremum either at p → 0+, p = 12, or at values of p such that the derivative of the left hand side with respect to p is 0. We’ll now consider each of these three cases.

![image 196](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile196.png>)

![image 197](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile197.png>)

Taking the derivative Comparing the derivative to 0, one obtains the relation

tanh ptanh−1 (x) + (1 − p)tanh−1 (y) − (px + (1 − p)y) = tanh−1 (x) − tanh−1 (y) cosh2 ptanh−1 (x) + (1 − p)tanh−1 (y) − (x − y) p. Plugging this back into (40) and using the triangle inequality, it is enough to show that

![image 198](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile198.png>)

tanh−1(x)−tanh−1(y) cosh2(ptanh−1(x)+(1−p) tanh−1(y))

+ (x − y) tanh−1 (α) (x − y) ≤ 9. (41)

![image 199](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile199.png>)

![image 200](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile200.png>)

Since tanh−1 (α) ≥ 1, the expression tanh−(x1(−αy)()x−y) is bounded by 1, so it remains to show that tanh−1 (x) − tanh−1 (y) tanh−1 (α) cosh2 ptanh−1 (x) + (1 − p)tanh−1 (y) (x − y) ≤ 8. (42) If y < 0 and x ≥ 21, then x − y > 1/2 and we trivially have

![image 201](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile201.png>)

![image 202](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile202.png>)

![image 203](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile203.png>)

tanh−1 (x) − tanh−1 (y) tanh−1 (α)

2

1 cosh2 ptanh−1 (x) + (1 − p)tanh−1 (y) (x − y) ≤

= 4.

![image 204](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile204.png>)

![image 205](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile205.png>)

![image 206](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile206.png>)

- 1

![image 207](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile207.png>)

- 2


If y < 0 and x < 21 then tanh−1 (x) − tanh−1 (y) ≤

![image 208](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile208.png>)

4 3

1 1 − x2

(x − y) ≤

(x − y)

![image 209](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile209.png>)

![image 210](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile210.png>)

and so

tanh−1 (x) − tanh−1 (y) tanh−1 (α) cosh2 ptanh−1 (x) + (1 − p)tanh−1 (y) (x − y) ≤

2 tanh−1 (α)

< 8.

![image 211](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile211.png>)

![image 212](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile212.png>)

For y ≥ 0, the maximal w.r.t p value of the left hand side of (42) is attained when the argument of cosh2 is minimal, i.e at p = 0. Using the fact that cosh tanh−1 (y) = 1/ 1 − y2 > 1/ 2(1 − y) and that tanh−1 (x) = 12 log 11+−xx, it suﬃces to show that

![image 213](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile213.png>)

![image 214](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile214.png>)

![image 215](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile215.png>)

![image 216](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile216.png>)

log 1+1−xx 1+1−yy (1 − y) tanh−1 (α) (x − y) ≤ 8. (43)

![image 217](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile217.png>)

![image 218](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile218.png>)

![image 219](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile219.png>)

We consider two cases. Suppose that 1−y

- 1−x ≥ 2. For any z ≥ 2, it holds that log 2z ≤ 2log z, and

since x,y < 1, it is enough to show that

- 2


![image 220](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile220.png>)

log 11−−xy (1 − y)

![image 221](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile221.png>)

tanh−1 (α) (x − y) ≤ 8. (44) Denote 1 − x = e−a and 1 − y = e−b, with a > b > 0; under this notation, the left hand side becomes 2tanh−1(α()a−b)

![image 222](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile222.png>)

. Note that tanh−1 (α) = 12 log 11+−αα ≥ 12 log 1−1x = 12a. If e−(a−b) < 12,

![image 223](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile223.png>)

![image 224](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile224.png>)

![image 225](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile225.png>)

![image 226](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile226.png>)

![image 227](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile227.png>)

![image 228](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile228.png>)

![image 229](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile229.png>)

(1−e−(a−b))

(1−e−(a−b)) ≤ 2 1(a−b)

then 2tanh−1(α()a−b)

2a(21) ≤ 8. Otherwise, if e−(a−b) ≥ 12, then a − b < 43. By Taylor’s theorem, the 1−e−(a−b) in the denominator can be bounded from below by 12 (a − b), bounding the expression by tanh−81(α) ≤ 8.

![image 230](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile230.png>)

![image 231](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile231.png>)

![image 232](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile232.png>)

![image 233](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile233.png>)

![image 234](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile234.png>)

![image 235](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile235.png>)

![image 236](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile236.png>)

![image 237](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile237.png>)

Now suppose that 1−y

1−x < 2. Since log z ≤ z − 1 for all z, we may then write the left hand side of (43) as

![image 238](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile238.png>)

log 1+1+xy + log 11−−xy (1 − y) tanh−1 (α) (x − y) ≤

1 tanh−1 (α)

![image 239](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile239.png>)

![image 240](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile240.png>)

![image 241](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile241.png>)

![image 242](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile242.png>)

1 tanh−1 (α)

≤

![image 243](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile243.png>)

3 tanh−1 (α)

≤

![image 244](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile244.png>)

- 1 + x

![image 245](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile245.png>)

- 1 + y − 1 +


1 − y 1 + y

1 − y 1 − x

+

![image 246](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile246.png>)

![image 247](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile247.png>)

< 8.

1 − y 1 − x − 1

![image 248](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile248.png>)

1 − y x − y

![image 249](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile249.png>)

- The case p = 0 Using L’HÃŽpital’s rule, the value of the left hand side of (40) attained as p → 0+ is

tanh−1(x)−tanh−1(y)

![image 250](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile250.png>)

cosh2(tanh−1(y)) − (x − y) tanh−1 (α) (x − y)

![image 251](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile251.png>)

.

For y ≥ 0, this is the same expression obtained by setting p = 0 in (41). The case y < 0 is handled similarly as above.

- The case p = 1/2 In this case we must show that


tanh 12 tanh−1 (x) + 12 tanh−1 (y) − 12x + 21y tanh−1 (α) (x − y) ≤

9 2·

![image 252](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile252.png>)

![image 253](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile253.png>)

![image 254](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile254.png>)

![image 255](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile255.png>)

![image 256](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile256.png>)

![image 257](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile257.png>)

This bound can be shown by diﬀerentiating with respect to y to the ﬁnd the maximum of the left hand side.

![image 258](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile258.png>)

![image 259](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile259.png>)

![image 260](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile260.png>)

![image 261](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile261.png>)

Proposition 32. Let f : Cn → R, let ξ be a product measure over Cn, and let Y ∼ ξ. Then E|f (Y ) − f (EY )| ≤

√nLip(f). Proof. Let Mi = E[f (Y ) | Y1,... ,Yi]. Then the variance of f can be bounded by Var [f (Y )] =

![image 262](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile262.png>)

n

n

E(Mi − Mi−1)2 ≤ Lip2 (f)

Var [Yi] ≤ nLip2 (f).

i=1

i=1

By Jensen’s inequality, E|f (Y ) − f (EY )| = E (f (Y ) − f (EY ))2 ≤ E(f (Y ) − f (EY ))2 = Var [f (Y )].

![image 263](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile263.png>)

![image 264](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile264.png>)

![image 265](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile265.png>)

Proof of the chain rule Lemma 25. For y ∈ Cn in the discrete hypercube, denote by Si (y) the vector which is equal to y everywhere, except for the i-th entry, so that

Using this notation, we have that

(Si (y))j =

yj i = j −yj i = j.

h(f (Si (y))) − h(f (y)) 2 − h′ (f (y))∂if (y) . (45)

∂i (h ◦ f)(y) − h′ (f (y)) ∂if (y) = −yi

![image 270](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile270.png>)

Using Taylor’s theorem for h around f (y) with the Lagrange remainder, there exists a z ∈ [f (y),f (Si (y))] such that

- 1

![image 271](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile271.png>)

- 2


(f (Si (y)) − f (y))2 h′′ (z) . Putting this into equation (45), we get

h(f (Si (y))) − h(f (y)) = (f (Si (y)) − f (y))h′ (f (y)) +

∂ih(f (y)) − h′ (f (y)) ∂if (y) =

- 1

![image 272](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile272.png>)

- 2


- 1

![image 273](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile273.png>)

- 2


(f (Si (y)) − f (y))2 h′′ (z) − −h′ (f (y))∂if (y)

yi (f (Si (y)) − f (y))h′ (f (y)) +

= −

yi 4

(f (Si (y)) − f (y))2 h′′ (z) − h′ (f (y))∂if (y)

= ∂if (y)h′ (f (y)) −

![image 274](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile274.png>)

yi 4

(f (Si (y)) − f (y))2 h′′ (z)

=

![image 275](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile275.png>)

= |∂if (y)|2 h′′ (z) ≤ BL2.

Equations (24) and (25) then follow immediately.

For equation (26), let x ∈ Cn and let ξ be the product measure on Cn such that for Y ∼ ξ, EY = x. Applying equation (21) on ∇f and ∇(h ◦ f), we have

![image 276](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile276.png>)

h′ (f (EY ))∇f (EY ) − E∇(h ◦ f)(Y ) 1 = h′ (f (EY )) E∇f (Y ) − E∇(h ◦ f)(Y ) 1

≤ E h′ (f (EY ))∇f (Y ) − h′ (f (Y ))∇f (Y ) 1 + + E h′ (f (Y ))∇f (Y ) − ∇(h ◦ f)(Y ) 1 .

By equation (24), the second term on the right hand side is bounded by BL2n. AS for the ﬁrst term,

E h′ (f (EY )) − h′ (f (Y )) ∇f (Y ) 1 ≤ BE |f (EY ) − f (Y )|∇f (Y ) 1

≤ BE|f (EY ) − f (Y )| nL (by Proposition 32) ≤ BL2n3/2.

Thus h′ (f (EY )) ∇f (EY ) − ∇(h ◦ f)(EY ) 1 ≤ 2BL2n3/2.

Proof of Lemma 26. For a vector y ∈ Cn and an index i = 1,... ,n, denote by yi+ the vector yi+ = (y1,y2,... ,yi−1,1,yi+1,... ,yn), and by yi− the vector yi− = (y1,y2,... ,yi−1,−1,yi+1,... ,yn).

- • The gradient complexity: Denote Af = {∇f (y) : y ∈ Cn} , Ah = {∇(h ◦ f)(y) : y ∈ Cn} .

By equation (25), we have that for every vector v ∈ Rn,

sup

u∈Ah

u,v ≤ max 0,B1 sup u∈Af

u,v + √nB2L21 v 2 .

![image 281](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile281.png>)

Since the expected norm of a Gaussian random vector Γ satisﬁes E Γ 2 ≤

√n, we get that D (h ◦ f) = E sup

![image 282](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile282.png>)

u∈Ah

u,Γ ≤ B1D (f) + B2L21n.

- • The Lipschitz constant: for every y ∈ Cn and every i = 1,... ,n,

|∂i (h ◦ f)(y)| =

h f yi+ − h f yi− 2

![image 283](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile283.png>)

≤ B1

f yi+ − f yi− 2 ≤ B1L1.

![image 284](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile284.png>)

Thus Lip (h ◦ f) ≤ B1L1.

- • The Lipschitz constant of the gradient: Let x = y ∈ Cn. By Lemma 25:


 ∇(h ◦ f)(x) − ∇(h ◦ f)(y) 1 = ∇(h ◦ f)(x) − h′ (f (x)) ∇f (x) + h′ (f (x)) ∇f (x) −

−∇(h ◦ f)(y) − h′ (f (y))∇f (y) + h′ (f (y)) ∇f (y) 1 ≤ 2nB2L21 + h′ (f (x)) ∇f (x) − h′ (f (y))∇f (y) 1 .

The last term on the right hand side can be bounded by

h′ (f (x)) ∇f (x) − h′ (f (y))∇f (y) ≤ h′ (f (x)) ∇f (x) − h′ (f (x)) ∇f (y) 1

+ h′ (f (x))∇f (y) − h′ (f (y)) ∇f (y) 1 ≤ B1  ∇f (x) − ∇f (y) 1 + B2 |f (x) − f (y)|  ∇f (y) 1 ≤ B1L2 x − y 1 + B2L1 x − y 1 L1n.

Putting the terms together, we get  ∇(h ◦ f)(x) − ∇(h ◦ f)(y) 1 x − y 1 ≤ B1L2 + 3B2L21n.

![image 285](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile285.png>)

![image 286](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile286.png>)

![image 287](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile287.png>)

![image 288](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile288.png>)

![image 289](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile289.png>)

Proof of Proposition 29. We will show that the total variation distance between Xng and Xϕ satisﬁes TV (ν,σ) ≤ 2 · 2−n;

the proof of the proposition then follows immediately. Denote by Zg and Zϕ the normalizing constants of ν and σ, respectively. Then

eg(y),

Zg = Zϕ +

y s.t f(y)≤(t−δ′)n

and by the proof of Proposition 28, this implies that

ε := |Zg − Zϕ| ≤ 2−n. The total variation distance is then given by

eg(y) Zg −

- 1

![image 290](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile290.png>)

- 2 y∈C


ϕ(y) Zϕ

TV(ν,σ) =

![image 291](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile291.png>)

![image 292](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile292.png>)

n

eg(y) Zg −

eg(y) Zg −

ϕ(y) Zϕ

ϕ(y) Zϕ

- 1

![image 293](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile293.png>)

- 2 f(y)≥(t−δ′)n


- 1

![image 294](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile294.png>)

- 2 f(y)<(t−δ′)n


+

.

=

![image 295](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile295.png>)

![image 296](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile296.png>)

![image 297](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile297.png>)

![image 298](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile298.png>)

By deﬁnition of ϕ and by Proposition 28, the ﬁrst term on the right hand side is bounded by eg(y) Zg −

eg(y) Zg ≤

ϕ(y) Zϕ

1 2 · 2−n

- 1

![image 299](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile299.png>)

- 2 f(y)<(t−δ′)n


- 1

![image 300](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile300.png>)

- 2 f(y)<(t−δ′)n


=

![image 301](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile301.png>)

![image 302](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile302.png>)

![image 303](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile303.png>)

![image 304](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile304.png>)

The second term is bounded by

- 1

![image 305](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile305.png>)

- 2 f(y)≥(t−δ′)n


eg(y) Zg −

ϕ(y) Zϕ

![image 306](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile306.png>)

![image 307](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile307.png>)

- 1

![image 308](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile308.png>)

- 2


=

- 1

![image 309](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile309.png>)

- 2


=

- 1

![image 310](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile310.png>)

- 2


≤

- 1

![image 311](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile311.png>)

- 2


≤

ϕ(y)

1 Zϕ + ε −

1 Zϕ

![image 312](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile312.png>)

![image 313](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile313.png>)

ϕ(y) Zϕ

![image 314](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile314.png>)

ϕ(y) Zϕ

![image 315](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile315.png>)

ϕ(y) Zϕ

![image 316](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile316.png>)

1 1 + Zε

− 1

![image 317](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile317.png>)

![image 318](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile318.png>)

ϕ

ε2 Zϕ2

ε Zϕ

- 1

![image 319](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile319.png>)

- 2


+

![image 320](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile320.png>)

![image 321](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile321.png>)

2ε Zϕ ≤ 2−n.

![image 322](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile322.png>)

![image 323](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile323.png>)

![image 324](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile324.png>)

![image 325](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile325.png>)

![image 326](<2017-eldan-decomposition-mean-field-gibbs-distributions_images/imageFile326.png>)

