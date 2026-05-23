arXiv:1903.08021v1[math.PR]19Mar2019

A transportation approach to the mean-ﬁeld approximation

Fanny Augeri∗ March 20, 2019

Abstract

We develop transportation-entropy inequalities which are saturated for measures such that their log-density with respect to the background measure is an aﬃne function, in the setting of the uniform measure on the discrete hypercube and the exponential measure. In this sense, this extends the well-known result of Talagrand in the Gaussian case. By duality, these transportationentropy inequalities imply a strong integrability inequality for Bernoulli and exponential processes. As a result, we obtain a dimension-free mean-ﬁeld approximation of the free energy of a Gibbs measure and a dimension-free nonlinear large deviations bound on the discrete hypercube. Applied to the Ising model, we deduce that the mean-ﬁeld approximation is within O(√n||J||2) of the free energy, where n is the number of spins and ||J||2 is the Hilbert-Schmidt norm of the interaction matrix. Finally, we obtain a reverse log-Sobolev inequality on the discrete hypercube similar to the one proved recently in the Gaussian case by Eldan and Ledoux.

![image 1](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile1.png>)

# 1 Introduction

A fundamental question in statistical Physics is to understand the behavior of Gibbs measures, in particular through the computation of their free energy. If µ is the uniform measure on the discrete hypercube {−1,1}n and f : {−1,1}n → R is a function, called the potential, one can consider the Gibbs measure associated to f, deﬁned as the probability measure

ν = Zf−1efdµ,

where Zf = efdµ is the partition function of ν. The logarithm of the partition function is called the free energy. The knowledge of the free energy for the family of potentials βf for β > 0 encodes a rich information on the Gibbs measure. Unfortunately, the free energy is generally an intractable quantity, which in turn motivates the search for meaningful large n approximations. The Gibbs variational principle (see [14, Lemma 6.2.13]) asserts that the free energy admits the following variational form

log efdµ = sup

ν

fdν − H(ν|µ) , (1)

![image 2](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile2.png>)

∗Weizmann Institute of Science, Israel, E-mail: fanny.augeri@weizmann.ac.il. This work was supported by the ERC advanced grant LogCorFields.

where the supremum runs over all probability measures ν on {−1,1}n, and H(ν|µ) denotes the relative entropy between ν and µ. The mean-ﬁeld approximation consists in restricting the above supremum over the special class of product probability measures (or more generally tilted measures, that is, measures whose log-density with respect to the background measure is an aﬃne function). As product probability measures on the discrete hypercube are parametrized by their mean, the mean-ﬁeld approximation reduces an optimization problem on probability measures on {−1,1}n into an optimization problem on [−1,1]n, which is much more tractable. The question is then to understand under which condition on the potential f, the mean-ﬁeld approximation can be justiﬁed rigorously. The Gibbs variational principle implies that the mean-ﬁeld approximation always gives a lower bound on the free energy, that is

log efdµ ≥ sup

fdµy − I(y) , (2)

y∈[−1,1]n

where µy is the product measure on {−1,1}n with barycenter y, and I(y) = H(µy|µ). Another way to reformulate the accuracy of the mean-ﬁeld approximation is to say that the above inequality is approximately tight in the large n limit. Our main task in the present work will be to obtain quantitative upper bounds.

In a seminal paper [10], Chatterjee and Dembo showed that given an extension of the potential f to the hypercube [−1,1]n, the mean-ﬁeld approximation is accurate if the set of gradients of f is of low complexity in a ℓ2-metric entropy sense. However, the quantitative error bound from the mean-ﬁeld approximation they obtained is rather intricate, and involves in particular L∞-norms of the partial derivatives of f up to the second order.

In the case of the Ising model, where the potential f is a quadratic form ∀x ∈ {−1,1}n, f(x) = x,Jx ,

given in terms of an interaction matrix J, the convergence of the free energy to the mean-ﬁeld approximation was shown in the context of dense graphs using the graphon framework in [9] and [8]. For general graphs, a ﬁrst breakthrough was made by Basak and Mukherjee [5] who showed the accuracy of the meanﬁeld approximation under the condition that ||J||2 = o(√n), denoting by ||J||2 the Hilbert-Schmidt norm of J. However, this result does not give any information about the speed of convergence. A quantitative error bound from the mean-ﬁeld approximation in O((n||J||2)32) up to a logarithmic factor was derived by Jain, Koehler and Mossel [19] using the Frieze-Kannan regularity lemma.

![image 3](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile3.png>)

![image 4](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile4.png>)

Another approach to this problem goes through the decomposition of the Gibbs measure itself into a mixture of measures where the coordinates are weakly correlated. This line of research was exploited by Jain, Koehler and Risteski in [20] to remove the logarithmic correction in the mean-ﬁeld approximation for the Ising model, and showed that,

- 2

![image 5](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile5.png>)

- 3 . (3)


log e x,Jx dµ(x) ≤ sup

{ y,Jy − I(y)} + O (n||J||2)

y∈[−1,1]n

In [15], Eldan proved a structural theorem for general Gibbs measures in Gaussian space and for the discrete hypercube. He deduced an upper bound on the free energy where the complexity of the discret gradient of the potential

is assessed in terms of its Gaussian mean-width, namely, g(V ) = E sup

ξ,Γ , (4)

ξ∈V

where V = ∇f({−1,1}n) and Γ is a standard Gaussian variable in Rn. His approximation of the free energy [15, Corollary 2] takes the form,

log efdµ ≤ sup

y∈[−1,1]n

1

- 2

![image 6](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile6.png>)

- 3g(V )


fdµy − I(y) + O Lip(f)

![image 7](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile7.png>)

- 2

![image 8](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile8.png>)

- 3 , (5)


3 n

where Lip(f) is the Lipschitz constant of f with respect to the Hamming metric. This approach was further developed by Austin [4] who proved a structure theorem for Gibbs measures on general product spaces and deduced a mean-ﬁeld approximation of the free energy.

In [1], the author proved a mean-ﬁeld approximation for Gibbs measures with respect to general compactly supported background measures which, using Sudakov minoration, implies in the case of the discrete hypercube that

log efdµ ≤ sup

y∈[−1,1]n

1

- 2

![image 9](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile9.png>)

- 3n


3 .

fdµy − I(y) + O g(V )

![image 10](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile10.png>)

In particular, this bound enables one to recover the bound (3) for the Ising model. In the present paper, we will remove the dimension dependence from the above estimate, and prove the dimension-free inequality,

log efdµ ≤ sup

y∈[−1,1]n

fdµy − I(y) + O b(V ) , (6)

where b(V ) = Esupξ∈V ξ,ε , and ε is uniformly distributed on {−1,1}n.

In a recent work [16], Eldan proved a new decomposition theorem which allowed him to show in the case of the Ising model that for any p > 0, the error on the free energy induced by the mean-ﬁeld approximation is O(1+pp(n||J||p)

p

1+p ), where || ||p denotes the p-Schatten norm. This bound recovers for p = 2 the previous O((n||J||2) and Risteski in [20], and can signiﬁcantly improve upon this bound by an appropriate choice of p.

![image 11](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile11.png>)

![image 12](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile12.png>)

- 2

![image 13](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile13.png>)

- 3) error shown by Jain, Koehler


The goal of this paper is to propose a transportation approach for the problem of the mean-ﬁeld approximation of the free energy of Gibbs measures in the speciﬁc case of the discrete hypercube. The main interest of this approach is that it allows us to derive an approximation which is dimension-free, i.e (6). We develop new transportation-entropy inequalities in the case of the Bernoulli and the exponential distribution. Originally, the transportationentropy inequalities were put forward by Marton [24] and Talagrand [29]. They appear to have strong connections with concentration inequalities (see [22, Chapter 6], [13], [25, Chapter 8], or [18, section 4]). They also have many links with other functional inequalities. Quadratic transportation-entropy inequalities are known to imply a spectral gap inequality by [7, section 4.1] (see also [18, section 8.3]), and are weaker that logarithmic Sobolev inequalities by the result of Otto and Villani [26] (see also [7]).

The main feature of the transportation-entropy inequalities we will present is that they are saturated by tilts of the background measure, that is measures with an aﬃne log-density. Given the central role of such probability measures in the mean-ﬁeld approximation, this feature will be particularly crucial.

Using duality, the main consequence we derive from these transportationentropy inequalities is a strong integrability inequality for Bernoulli and exponential processes, similar to the Gaussian case. In turn, this will provide us the main ingredient to obtain a dimension-free mean-ﬁeld approximation of the free energy of Gibbs measures and in a similar fashion, a dimension-free nonlinear large deviations bound on the discrete hypercube. In the setting of the Ising model on {−1,1}n, we deduce that the mean-ﬁeld approximation is within O(√n||J||2) of the free energy, improving the previous known bound (3) involving the Hilbert-Schmidt norm of J. Finally, we prove a dimensionfree reverse log-Sobolev inequality on the discrete hypercube similar as the one existing in the Gaussian case [17].

![image 14](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile14.png>)

# 2 Main results

## 2.1 Transportation-entropy inequalities

Let P(Rn) denote the set of probability measures on Rn. For any µ,ν ∈ P(Rn), and a lower semi-continuous cost function c : Rn × Rn → [0,+∞], one deﬁnes the transportation cost Wc(ν,µ) by,

Wc(ν,µ) = inf

π

c(x,y)dπ(x,y),

where the inﬁmum runs over all couplings between ν and µ. We say that a given measure µ satisﬁes a transportation-entropy inequality with cost function

- c : Rn → [0,+∞] if, ∀ν ∈ P(Rn), Wc(ν,µ) ≤ H(ν|µ), (7)


where H(ν|µ) denotes the relative entropy. Let µ be a reference probability measure on Rn. We call ν ∈ P(Rn) a tilt of

µ if the log-density with respect to µ, log dµdν , is an aﬃne function. We address the question of ﬁnding a transportation-entropy inequality which is saturated

![image 15](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile15.png>)

by tilts of the reference measure µ. By Talagrand’s result [29], we know that the standard Gaussian measure on Rn, which we denote by γ, satisﬁes a transportation-entropy inequality with cost function (x,y)  → 21||x − y||2ℓ2, where || ||ℓ2 denotes the ℓ2-norm, that is,

![image 16](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile16.png>)

∀ν ∈ P(Rn), W1

(ν,γ) ≤ H(ν|γ). (8)

2|| ||2ℓ2

![image 17](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile17.png>)

As one can observe, this transportation-entropy inequality is tight for tilts of the Gaussian measure, which are just push-forwards by translations.

In the case of the exponential measure η = e−x1x≥0dx , we consider the following cost function,

∀x,y ∈ Rn, c(x,y) =

n

yiΛ∗η

i=1

xi yi

![image 18](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile18.png>)

, (9)

where for any t > 0,

Λ∗η(t) = t − 1 − log t,

and for t ≤ 0, Λ∗η(t) = +∞. With these deﬁnitions, we have the following transportation-entropy inequality.

- 2.1 Proposition. Let η be the probability measure e−x1x≥0dx and ηn be its n-fold product. For any probability measure ν on Rn,

Wc(ν,ηn) ≤ H(ν|ηn). Moreover, the equality holds if ν is a tilt of ηn.

- 2.2 Remark. In [29], Talagrand proved that the symmetric exponential measure m = 12e−|x|dx satisﬁes a certain family of transportation-cost inequalities with costs ct indexed by t ∈ (0,1), deﬁned by,

![image 19](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile19.png>)

∀x ∈ R, ct(x,y) =

1 t − 1 e−t|x−y| + t|x − y| − 1 .

![image 20](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile20.png>)

This family of cost functions has the striking property that for any t there exists a probability measure which achieves the inequality in the transportationcost inequality with cost function ct. In this sense, this is a family of optimal cost functions. However, the probability measures which saturate the inequality are not tilts of the exponential measure, but are more intricate measures whose monotonous rearrangements from the exponential measure satisfy a certain family of diﬀerential equations.

To deal with the singularity of the Bernoulli measure, we propose a variant of the transportation-entropy inequality (7) where we make it possible to enrich the transportation problem by considering another measure than the reference measure. More precisely, we will say that µ satisﬁes a transportationentropy inequality if

∀ν ∈ P(Rn), Wc(ν,µ˜) ≤ H(ν|µ),

- where c : Rn × Rn → [0,+∞] is lower semi-continuous and µ˜ is a ﬁxed probability measure on Rn.


Let p ∈ (0,1) and Ip be the function deﬁned by ∀x ∈ [−1,1], Ip(x) =

- 1 + x

![image 21](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile21.png>)

- 2


log

1 + x 2p

![image 22](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile22.png>)

+

- 1 − x

![image 23](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile23.png>)

- 2


log

1 − x 2(1 − p)

![image 24](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile24.png>)

, (10)

and Ip(x) = +∞ otherwise. We deﬁne the cost function wp : {−1,1}n × [−1,1]n → [0 + ∞] by

∀x ∈ {−1,1}n,u ∈ [−1,1]n, wp(x,u) =

n

i=1

2|Ip′(ui)|1x

i(h0−ui)<0, (11)

and h0 = 2p−1. With these deﬁnitions, we have the following transportationentropy inequality.

- 2.3 Proposition. Let µp = (1−p)δ−1 +pδ1 and U be the uniform probability measure on [−1,1]. For any probability measure ν on {−1,1}n,


(ν,Un) ≤ H(ν|µnp), and equality holds if ν is a product measure.

Wwp

## 2.2 Strong integrability of empirical processes

The ﬁrst consequence we will derive from the transportation-entropy of the previous section consists in the strong integrability of Bernoulli and exponential empirical processes. By empirical process, we mean any process of the form,

( ξ,X )ξ∈V ,

where V is some countable subset of Rn, X is a random vector in Rn with independent and identically distributed coordinates, and .,. denotes the standard inner product in Rn.

In the Gaussian case, it is known that for any countable set V ⊂ Rn,

log esupξ∈V { ξ,x −12||ξ||2ℓ2}dγ(x) ≤ sup ξ∈V

ξ,x dγ(x). (12)

![image 25](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile25.png>)

This inequality was ﬁrst put forward in [31]. It can also be seen as a consequence of Talagrand’s transportation-entropy for the Gaussian measure (8).

We show that a similar estimate holds for the uniform measure on {−1,1}n

and the exponential measure, where the quadratic cost 21||ξ||2ℓ2 is replaced by the logarithmic Laplace transform of the measure considered. In the following,

![image 26](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile26.png>)

for any probability measure µ on Rn we will denote by Λµ its logarithmic Laplace transform, deﬁned as

∀ξ ∈ Rn, Λµ(ξ) = log e ξ,x dµ(x).

For a subset V ⊂ Rn, we will also denote by b(V ) the “Rademacher meanwidth” of V , deﬁned by

b(V ) = E sup

ξ,ε , (13)

ξ∈V

where ε is uniformly sampled on {−1,1}n. With this notation, we have the following result in the discrete setting. This estimate will be the key element of our approach to the mean-ﬁeld approximation.

- 2.4 Proposition. Let µ be the uniform probability measure on {−1,1}n. There exists a universal constant κ > 0, such that for any V ⊂ Rn,

log esupξ∈V { ξ,x −Λµ(ξ)}dµ(x) ≤ κb(V ).

Similarly, we get in the case of the exponential measure the following result.

- 2.5 Proposition. Let η be the probability measure 1x≥0e−xdx. For any countable subset V ⊂ Rn,


log esupξ∈V { ξ,x −Ληn(ξ)}dηn(x) ≤ sup ξ∈V

Λη(ξ),x − u dηn(x),

where u denotes the vector (1,1,...,1), and Λη(ξ) = (Λη(ξ1),...,Λη(ξn)).

## 2.3 Mean-ﬁeld approximation

Building on the previous strong integrability inequality for Bernoulli empirical processes, we prove a dimension-free mean-ﬁeld approximation of the free energy of Gibbs measures. In the following we denote by I the function deﬁned by,

n

∀x ∈ [−1,1]n, I(x) =

i=1

- 1 − xi

![image 27](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile27.png>)

- 2


- 1 + xi

![image 28](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile28.png>)

- 2


log(1 + xi) +

log(1 − xi) , (14)

and I(x) = +∞ otherwise. With this notation, we have the following result.

- 2.6 Theorem. Let µ be the uniform probability measure on {−1,1}n. There exists a universal constant κ > 0, such that for any function f : Rn → R continuously diﬀerentiable,

log efdµ ≤ sup

y∈[−1,1]n

{f(y) − I(y)} + κb(V ),

where V = ∇f([−1,1]n), and b(V ) is deﬁned in (13). One can interpret I by the identity ∀y ∈ [−1,1]n, I(y) = H(µy|µ),

where µy stands for the unique product probability measure on {−1,1}n with mean y.

- 2.7 Remark. If f : {−1,1}n → R is some function deﬁned only on the discrete hypercube, one can extend it harmonically to [−1,1]n by the formula

∀y ∈ [−1,1]n, f(y) = fdµy. We know by [15, Fact 14] that

∇f(h) = ∇fdµy, where the gradient on the right-hand side is the discrete gradient of f, that is,

∀x ∈ {−1,1}n, ∇f(x) = (∂1f(x),...,∂nf(x)), with

∀i ∈ {1,...,n}, ∂if(x) =

- 1

![image 29](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile29.png>)

- 2


f(x+) − f(x−) , where x+ = (x1,...,xi−1,1,xi+1,...,xn) and x− = (x1,...,xi−1,−1,xi+1,...,xn).

Thus, for this extension, the set of gradients ∇f([−1,1]n) is the convex hull of the discrete gradients. Therefore, the error term of Theorem 2.6 is just b(∇f({−1,1}n)).

- 2.8 Remark. If f : Rn → R is a continuously diﬀerentiable function and g

is the harmonic extension of f|{−1,1}n to [−1,1]n described in the previous remark, then

sup

y∈[−1,1]n

f(y) − g(y) ≤ λb(V ),

where V = ∇f([−1,1]n), and λ is a numerical constant. We refer the reader to Lemma 4.2 for a proof of this fact. This implies that in the mean-ﬁeld approximation stated in Theorem 2.6, the extension one chooses does not matter as soon as its set of gradient is of low complexity.

Applying Theorem 2.6 to the Ising model, we obtain the following corollary.

- 2.9 Corollary. Let J be a Hermitian matrix of size n such that Ji,i = 0 for any i ∈ {1,...,n}, and h ∈ Rn. Then,


√n,

log e x,Jx + h,x dµ(x) ≤ sup

![image 30](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile30.png>)

{ y,Jy + h,y − I(y)} + κ||J||2

y∈[−1,1]n

where κ is a universal positive constant, and || ||2 denotes the Hilbert-Schmidt norm, namely

1/2

|Ji,j|2

||J||2 =

.

1≤i,j≤n

In the interesting large deviation regime, the free energy is expected to be of order n. Thus, the above Corollary 2.9 gives a meaningful upper bound whenever ||J||2 = o(√n). It recovers the qualitative result of Basak and Mukherjee [5] for the Ising model, and gives a quantitative error term which is strictly smaller than the one found in [20], i.e (3).

![image 31](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile31.png>)

- 2.10 Example (d-regular graphs). Let us consider a d-regular graph G with n vertices (n and d are implicitly taken such that nd is even). Let A denote the adjacency matrix of G, and let us consider the Ising model with the interaction matrix J = d1A. This scaling is taken so that the free energy of this model is of order n. As ||J||2 = n/d, Corollary 2.9 gives

![image 32](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile32.png>)

![image 33](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile33.png>)

log e x,Jx dµ(x) = sup

y∈[−1,1]n

{ y,Jy − I(y)} + O

n √

![image 34](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile34.png>)

![image 35](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile35.png>)

d

.

This bound improves the one of Eldan [16, Example 3] who showed that for a d-regular expander, that is such that the second largest eigenvalue λ2(A) = O(

√

![image 36](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile36.png>)

d), one has the error

n √d1−o(1)

![image 37](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile37.png>)

![image 38](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile38.png>)

,

over the mean-ﬁeld approximation, in the regime log d ≪ log n.

- 2.11 Remark. In [16], Eldan proved that for any p > 0 the mean-ﬁeld ap-


p

proximation is within O(p+1p (n||J||p)

p+1) of the free energy of the Ising model with interaction matrix J, where || ||p is the p-Schatten norm. One can note that for p ≥ 2 and in the regime where Eldan’s bound is meaningful, that is ||J||p = O(n1/p), the inequality ||J||2 ≤ n

![image 39](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile39.png>)

![image 40](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile40.png>)

- 1

![image 41](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile41.png>)

- 2−p1 ||J||p, yields that the error term of Corollary 2.9 is smaller than O((n||J||p)


![image 42](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile42.png>)

p

p+1). However, the real interest of Eldan’s bound is when p ≤ 2 and in particular the regime when p → 0 when n grows to inﬁnity. For p < 2, it seems that Eldan’s bound and the one given by

![image 43](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile43.png>)

- Corollary 2.9 cannot be compared in general. For speciﬁc examples, like the Curie-Weiss model or the lattice with mesoscopic interactions (see [16, example 2]) where the eigenvalues of the interaction decrease exponentially fast to 0, Eldan’s bound is better and yields only logarithmic errors, whereas Corollary


- 2.9 can only provide error terms depending polynomially in the dimension.


## 2.4 Nonlinear large deviations

The theory of nonlinear large deviations was introduced by Chatterjee and Dembo [10] in order to understand the large deviations of nonlinear functions of independent Bernoulli random variables. One of the motivation for developing this theory comes from the question of the deviations of sub-graph counts in sparse Erdős–Rényi graphs.

Given a function f : {−1,1}n → R, and X uniformly sampled on {−1,1}n, one can wonder when the optimal change of measure in the large deviations of f(X) is given by product measures. The nonlinear large deviations theory aims at answering this question and at identifying which condition on f can guarantee this mechanism of deviation to happen. Similarly as for the question of the mean-ﬁeld approximation of the free energy, Chatterjee and Dembo showed in [10] that a suﬃcient condition is that the set of gradients of f is of low complexity in a ℓ2-metric entropy sense.

Eﬀorts have been put into improving the original non-asymptotic bound of [10], which has the inconvenient of involving error terms related to the

smoothness of f. In [32], Yan generalizes to products of general compact spaces the nonlinear large deviations bound of [10]. Eldan [15] removed most of the smoothness assumptions and provided a bound where the complexity of the gradient is assessed in term of its Gaussian mean-width. In [12, Corollary

- 2.2], Cook and Dembo proposed a nonlinear large deviation bound which has the speciﬁcity of not relying on the complexity of the gradient but rather on an eﬃcient covering of the space by convex sets.


We propose here a nonlinear large deviations bound in the speciﬁc case of the discrete hypercube whose main feature is to be dimension-free. As we will show, it follows from the strong integrability inequality of Bernoulli processes of Proposition 2.4.

To describe this bound, we extend Ip, deﬁned on R by the formula (10), to Rn by setting,

n

∀y ∈ Rn, Ip(y) :=

Ip(yi). Let f : [−1,1]n → R be a function, and deﬁne the rate function

i=1

∀t ∈ R, ϕp(t) = inf{Ip(y) : f(y) ≥ t,y ∈ Rn}. With this notation, we have the following theorem.

- 2.12 Theorem. Let t ∈ R and δ > 0. Assume that ∀s > t − δ, ϕp(s) > ϕp(t − δ).

Let V = ∇f([−1,1]n) and let X be a random vector sampled according to µnp. There exist universal constants C,κ > 0, such that if

b(V ) ≤ δ/κ, where b(V ) is deﬁned in (13), then

log P f(X) ≥ t ≤ −ϕp(t − δ) + C log

nL log(1/p(1 − p)) δ

![image 44](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile44.png>)

,

where L = supx∈[−1,1]n ||∇f(x)||ℓ2.

- 2.13 Remark. It is actually possible to weaken the regularity assumption on f, and assume that for any x,y ∈ [−1,1]n,


f(x) − f(y) ≤ sup

ξ,x − y ,

ξ∈V

where V is a convex subset of Rn.

## 2.5 Reverse log-Sobolev inequality on the discrete hypercube

Let µ be the uniform measure on {−1,1}n. The logarithmic Sobolev inequality on the discrete hypercube (see [25, Theorem 5.1]) says that for any ν = efdµ probability measure on {−1,1}n,

- 1

![image 45](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile45.png>)

- 2 ||∇f(x)||2ℓ2dν(x), (15)


H(ν|µ) ≤

where ∇f denotes the discrete gradient. The inequality (15) can be improved by replacing the quadratic function || ||2ℓ2/2 by I(∇Λµ), which gives

H(ν|µ) ≤ I(∇Λµ(∇f(x)))dν(x). (16)

From the inequality in dimension 1,

∀λ ∈ R, I(Λ′µ(λ)) ≤

- 1

![image 46](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile46.png>)

- 2


λ2,

we see that (15) is indeed implied by (16).

The proof of inequality (16) goes over induction on the dimension. For n = 1, it is straightforward to see that there is actually equality. For n > 1, one uses the sub-additivity of the relative entropy [22, Proposition 5.6],

n

H(ν|µ) ≤

i=1

H(νx(i)|µ1/2)dν(x),

where νx(i) is the conditional probability measure given x(i) = (x1,...,xi−1,xi+1,...,xn), which is equal in our case to the probability measure proportional to e∂

if(x)xidµ1/2(xi)

The interest of stating the log-Sobolev inequality this way is that it is saturated for product measures. Thus, one can expect that whenever the gradient of f is of low complexity, the inequality (16) above is almost an equality. We will prove that it is indeed the case, and show a reverse logSobolev inequality, similar to the one proved by Eldan and Ledoux [17] in the Gaussian case.

- 2.14 Proposition. Let ν = efdµ be a probability measure on {−1,1}n. Let


I(ν) = I(∇Λµ(∇f(x)))dν(x),

where ∇f is the discrete gradient of f. Then,

 ∇f(y),x dµ(x),

I(ν) ≤ H(ν|µ) + κ sup

y∈Cn

where κ is a universal constant.

# 3 Transportation-entropy inequalities

In this section, we prove the transportation-entropy inequalities of the Propositions 2.1 and 2.3 which are at the base of our results. We start by recalling some standard features of these inequalities. An important property is that they tensorize in a certain way which we recall in the following lemma. The reader may ﬁnd a proof of this result in [18, Proposition 1.3].

- 3.1 Lemma. If for i ∈ {1,2}, µi,µ˜i are probability measures on Rdi


, such that

∀ν ∈ P(Rdi

(ν,µ˜i) ≤ H(µ|µi), × Rdi

), Wci

- where ci : Rdi


→ [0,+∞] is a lower semi-continuous function, then ∀ν ∈ P(Rd1

× Rd2

), Wc1⊕c2(ν,µ˜1 ⊗ µ˜2) ≤ H(ν|µ1 ⊗ µ2), where c1 ⊕ c2 is deﬁned for any x = (x1,x2) ∈ Rd1

× Rd2

and y = (y1,y2) ∈ Rd1

× Rd2

by,

c1 ⊕ c2(x,y) = c(x1,y1) + c(x2,y2).

Note that when µ is a product measure, the tilts of µ are also product measures. Therefore, the question of ﬁnding a transportation-entropy inequality which is saturated for tilts reduces itself to a 1-dimensional problem by the tensorization property described above together with the following fact. It follows from the deﬁnitions of the relative entropy and the transportation cost.

- 3.2 Fact. For i ∈ {1,2}, let µi and νi be probability measures on Rdi


, and × Rdi

- ci : Rdi


→ [0,+∞] be lower semi-continuous functions. Then,

H(ν1 ⊗ ν2|µ1 ⊗ µ2) = H(ν1|µ1) + H(ν2|µ2), and

(ν2,µ2).

(ν1,µ1) + Wc2

Wc1⊕c2(ν1 ⊗ ν2,µ1 ⊗ µ2) = Wc1

The main aspect of transportation-entropy inequalities we will use is their dual functional form, which consists of inﬁmum-convolution inequalities. This duality relies on the Kantorvitch duality [30, Theorem 5.10] which states that if c : Rn × Rn → [0,+∞] is lower semi-continuous, then for any ν,µ ∈ P(Rn),

Wc(ν,µ) = sup

ϕ∈L1(ν)

ϕdν − ϕcdµ , (17)

where ϕc the c-conjugate of ϕ deﬁned by, ∀y ∈ Rn, ϕc(y) = sup x∈Rn

{ϕ(x) − c(x,y)}.

Moreover, by [30, Theorem 5.10, (ii)], if Wc(ν,µ) < +∞, then a coupling π between ν and µ is optimal if and only if there exists ϕ ∈ L1(ν) such that π-almost surely,

ϕ(y) − ϕc(x) = c(x,y). (18)

In the next lemma, we recall the equivalence between transportationentropy and inﬁmum-convolution inequalities (see [18, Corollary 3.1] or [30, Theorem 5.26]) and we show that an equality case in the transportationentropy inequality can be translated into an equality case for the inﬁmumconvolution inequality.

- 3.3 Proposition. Let µ,µ˜ ∈ P(Rn) and c : Rn × Rn → [0,+∞] be a lower semi-continuous function. The following statements are equivalent.


(i). µ satisﬁes the transportation-entropy inequality,

∀ν ∈ P(Rn), Wc(ν,µ˜) ≤ H(ν|µ). (19) (ii). µ satisﬁes the inﬁmum-convolution inequality,

log efdµ ≤ fcdµ,˜ (20)

for any f : Rn → R measurable such that fc ∈ L1(µ). Let ν be such that H(ν|µ) < +∞. In the case (i) or (ii) is satisﬁed, equality holds in (19) for ν if and only if equality holds in (20) for f = log dµdν . Proof. A proof of the equivalence between (i) and (ii) can be found in [18,

![image 47](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile47.png>)

- Corollary 3.1] or [30, Theorem 5.26]. We are now left to prove the equivalence between the equality cases. Assume (i) holds and there is equality in (19) for


ν. Denote by f = log dµdν . As H(ν|µ) < +∞, we have that Wc(ν,µ˜) < +∞. By Kantorovich duality (18), there exists ϕ ∈ L1(ν) such that, π-almost surely,

![image 48](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile48.png>)

ϕ(x) − ϕc(y) = c(x,y). (21)

Our goal is to show that ϕ is equal to f up to some additive constant. Indeed, if ϕ = f+α for some constant α ∈ R, then using the fact that (f+α)c = fc+α, we have π-almost surely,

f(x) − fc(y) = c(x,y). Integrating the above equality with respect to π yields, fc(y)dµ˜(y) = f(x)dν(x) − c(x,y)dπ(x,y). As ν achieves the equality in (19), we obtain fc(y)dµ(y) = 0, which would prove the ﬁrst part of the equivalence between the equality cases.

Using Kantorovich duality (17), we have for any η ∈ P(Rn) such that ϕ ∈ L1(η),

Wc(η,µ˜) ≥ ϕdη − ϕcdµ.˜

Integrating (21) with respect to π and combining with the above inequality, we deduce

Wc(η,µ˜) − Wc(ν,µ˜) ≥ ϕd(η − ν). But, as (i) holds and equality holds for ν in (19), we get

H(η|µ) − H(ν|µ) ≥ ϕd(η − ν). (22)

Let ψ : Rn → R be a measurable and bounded function such that

ψdν = 0.

For δ > 0 small enough, we can deﬁne the probability measure νδ = (1 + δψ)dν,

and we have moreover that L1(νδ) = L1(ν), so that ϕ ∈ L1(ν). Since H(νδ|µ) = log 1 + δψ)ef dνδ, we deduce by the Gibbs variational formula (1),

H(νδ|µ) − H(ν|µ) ≤ log (1 + δψ)ef d(νδ − η). Therefore, dividing (22) by δ, we get

log(1 + δψ)ψdν + fψdν ≥ ϕψdν.

Taking δ → 0 we conclude by dominated convergence,

fψdν ≥ ϕψdν,

for any ϕ bounded, measurable such that ψdν = 0. Therefore,

ϕ = f + (ϕ − f)dν, ν-almost surely.

Assume now (i),(ii) and that f achieves the equality in (20). By deﬁnition, H(ν|µ) = fdν. As f achieves the equality in (20), we can write, fdν = f(x)dν(x) − sup

{f(x) − c(x,y)}dµ˜(y) ≤ c(x,y)dπ(x,y), which proves the second part of the equivalence.

x∈Rn

![image 49](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile49.png>)

![image 50](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile50.png>)

![image 51](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile51.png>)

![image 52](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile52.png>)

As we will see in the sequel, when µ is a product measure, a transportationentropy inequality which is saturated by tilts implies by duality a strong integrability inequality for empirical processes. In this paper we carry out this program in the special case where µ is the n-fold product of a measure supported on {−1,1} or of the exponential measure on R+.

## 3.1 The Gaussian case

Before going into the investigation of the discrete setting and the case of the exponential measure, we will review what happens in the Gaussian case, which we will regard as a motivational example. We will see how Talagrand’s transportation-entropy inequality [29] implies a dimension-free mean-ﬁeld approximation of the free energy of Gibbs measures and a nonlinear large deviation bound.

First, we turn our attention to the mean-ﬁeld approximation of the free energy. Using Talagrand’s transportation-entropy (8) and Proposition 3.3, one gets that for any measurable function f : Rn → R,

- 1

![image 53](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile53.png>)

- 2||h||2ℓ2}dγ(x). (23)


log efdγ ≤ sup

{f(x + h) −

h∈Rn

Note that replacing f by supλ∈V { λ,x − 12||λ||2ℓ2}, for some countable set V , one obtains the strong integrability inequality of Gaussian processes mentioned

![image 54](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile54.png>)

in (12). Coming back at the estimation of the free energy, we see that using a change of measure and Jensen’s inequality, we have the lower bound

1 2||h||2ℓ2 ≤ log efdγ.

sup

f(x + h)dγ(x) −

![image 55](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile55.png>)

h∈Rn

From these two inequalities, we see that the so-called mean-ﬁeld approximation of the free energy of the Gibbs measure associated with some function f holds as soon as the Gaussian mean-width is small compared to the mean-ﬁeld approximation. More precisely, we have the following proposition.

- 3.4 Proposition. Let f : Rn → R be a continuously diﬀerentiable function. Then,


- 1

![image 56](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile56.png>)

- 2||h||2ℓ2 ≤ log efdγ


sup

f(x + h)dγ(x) −

h∈Rn

√

- 1

![image 57](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile57.png>)

- 2||h||2ℓ2 +


![image 58](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile58.png>)

2g(V ), where V = ∇f(Rn) and g(V ) is deﬁned in (4).

≤ sup

f(x + h)dγ(x) −

h∈Rn

Proof. From (23), we deduce

- 1

![image 59](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile59.png>)

- 2||h||2ℓ2


log efdγ ≤ sup

f(x + h)dγ(x) −

h∈Rn

f(x + h) − f(y + h)dγ(y) dγ(x).

+ sup

h∈Rn

This last error term can be compared to the Gaussian mean-width of ∇f(Rn), by pulling the integral in y out of the supremum and using the mean-value Theorem, namely,

√

![image 60](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile60.png>)

sup

f(x + h) − f(y + h)dγ(y) dγ(x) ≤

2g(V ),

h∈Rn

where V = ∇f(Rn).

![image 61](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile61.png>)

![image 62](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile62.png>)

![image 63](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile63.png>)

![image 64](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile64.png>)

In parallel, Talagrand’s transportation-entropy inequality (8) or more strongly the Gaussian isoperimetric inequality can be used to obtain a dimension-free nonlinear large deviations bound. In [2], this observation was exploited to derive large deviations principles for a class of functions for which the large deviations are due to translations. In the following proposition, we give a non-asymptotic nonlinear large deviations bound in the Gaussian setting.

- 3.5 Proposition. Let f : Rn → R be a continuously diﬀerentiable function and denote by V = ∇f(Rn). Deﬁne the function,

∀t ∈ R, ψ(t) = inf Let t ∈ R,δ > 0. Assume that

- 1

![image 65](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile65.png>)

- 2||h||2ℓ2 : Ef(X + h) ≥ t,h ∈ Rn .


∀s > t − δ, ψ(s) > ψ(t − δ). (24)

Let X be a standard Gaussian vector in Rn. If g(V ) ≤ 2√δ2, then log P(f(X) ≥ t) ≤ −ψ(t − δ).

![image 66](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile66.png>)

![image 67](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile67.png>)

- 3.6 Remark. A close attention to the proof reveals that a weaker suﬃcient condition is that P(Eδ) ≥ 1/2, where


Eδ = x : sup

|f(x + h) − Ef(X + h)| < δ .

||h||2ℓ2≤2ϕ(t−δ)

This observation can be crucial for certain large deviations problems where the function f does not have a gradient of low complexity in the sense of small Gaussian mean-width but instead in the sense that Eδ is a typical set. An example of such a large deviation problem is given by the traces of power of Gaussian Wigner matrices which was studied in [3].

Proof. Let Y be a standard Gaussian random variable independent of Y . As a consequence of the assumption (24), we claim that

P f(X) ≥ t ≤ P inf

||h||2ℓ2≤2ψ(t−δ)

f(X) − Ef(Y + h) ≥ δ . (25)

Indeed, if ||h||2ℓ2 ≤ 2ψ(t − δ), then by the deﬁnition of ψ, ψ Ef(Y + h) ≤ ψ(t − δ).

Therefore Ef(Y + h) ≤ t − δ by (24). Deﬁne the set Eδ = x : sup

(f(x + h) − Ef(Y + h)) < δ .

||h||2ℓ2≤2ψ(t−δ)

With this notation, one can observe that, P inf

![image 68](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile68.png>)

f(X) − Ef(Y + h) ≥ δ ≤ P X ∈/ Eδ + 2ψ(t − δ)Bℓ2 .

||h||2ℓ2≤2ψ(t−δ)

The Gaussian isoperimetric inequality entails that the Gaussian measure has normal concentration by [22, Corollary 2.6], which means that,

![image 69](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile69.png>)

P X ∈/ Eδ + 2ψ(t − δ)Bℓ2 ≤ e−ψ(t−δ),

as soon as P(X ∈ Eδ) ≥ 1/2. The mean-value Theorem and Markov’s inequality yield,

1 δ

 ∇f(x),X − Y , which concludes the proof.

E sup

P(X ∈/ Eδ) ≤

![image 70](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile70.png>)

x∈Rn

![image 71](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile71.png>)

![image 72](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile72.png>)

![image 73](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile73.png>)

![image 74](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile74.png>)

Let us make some closing remarks about the speciﬁcity of the Gaussian setup. For a convex function Λ : Rn → R ∪ {+∞}, one deﬁnes its Legendre transform by the formula,

∀x ∈ Rn, Λ∗(x) = sup ξ∈Rn

ξ,x − Λ(ξ) .

We will also denote by Γ(Rn) the set of convex functions Rn → R∪{+∞} which are lower semi-continuous, and are proper, namely their domain is nonempty. In general, one can show using a small modiﬁcation of [21, Remark 2.12] the following fact on cost functions of transportation-entropy inequalities.

- 3.7 Fact. Let µ be a probability measure on Rn with mean 0 which satisﬁes a transportation-entropy inequality (7) with cost function c of the form,


c : (x,y)  → α(x − y), for some function α ∈ Γ(Rn). Then,

∀x ∈ Rn, α(x) ≤ Λ∗µ(x).

Proof. By Proposition 3.3, we know that for any measurable function f : Rn → R, such that fc ∈ L1(µ),

log efdµ ≤ sup x∈Rn

{f(x) − α(x − y)}dµ(y).

Testing the above inequality for linear forms we get ∀θ ∈ Rn, Λµ(θ) ≤ α∗(θ). As α ∈ Γ(Rn), we can conclude using [11, Theorem 4.21] that α ≤ Λ∗µ.

![image 75](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile75.png>)

![image 76](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile76.png>)

![image 77](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile77.png>)

![image 78](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile78.png>)

Therefore, among the cost functions of the form c(x,y) = α(x − y), with α ∈ Γ(Rn), the best cost function one can expect is

(x,y)  → Λ∗µ(x − y).

Note that Talagrand’s result (8) gives exactly that the Gaussian measure satisﬁes a transportation-entropy inequality with the above cost function. As we now show, the Gaussian measure is the only measure with this property.

- 3.8 Fact. Let µ be a probability measure on Rn with mean 0 such that the

domain of Λµ has nonempty interior and Λ∗µ is strictly convex. If µ satisﬁes the transportation-entropy inequality with cost function

(x,y)  → Λ∗µ(x − y), then µ is a Gaussian measure.

- 3.9 Remark. By [27, Theorem 4.1], a suﬃcient condition for Λ∗µ to be strictly convex is that the support of µ is not included in a hyperplane and Λµ is essentially convex, that is, its domain, denoted by DΛ, has nonempty interior, Λµ is diﬀerentiable on the interior of its domain DΛ◦, and steep, that is, for any ξk ∈ DΛ◦ such that ξk → ξ ∈ ∂DΛ when k → +∞, we have


||∇Λ(ξk)||ℓ2 −→

+∞.

k→+∞

Proof. We write as a short-hand Λ instead of Λµ and DΛ its domain. Let θ ∈ DΛ◦, and deﬁne the probability measure

µθ = e x,θ −Λ(θ)dµ(x).

As Λ∗ is a convex function, it is continuous on the interior of its domain. Therefore, the function

c : (x,y)  → Λ∗(x − y),

is lower semi-continuous. By [30, Theorem 4.1], we know that there exists a coupling π between µθ and µ, such that

Wc(µθ,µ) = Λ∗(x − y)dπ(x,y). Assume µ satisﬁes the transportation-entropy with cost function c. As

H(µθ|µ) = Λ∗(∇Λ(θ)), we have

Λ∗(y − x)dπ(x,y) ≤ Λ∗(∇Λ(θ)). But by convexity of Λ∗, we get,

Λ∗(∇Λ(θ)) = Λ∗ ydµθ(y) ≤ Λ∗(y − x)dπ(x,y) ≤ Λ∗(∇Λ(θ)).

As Λ∗ is strictly convex, the equality in Jensen’s inequality yields that µθ is the push forward of µ by a translation. Since the mean of µθ is ∇Λ(θ) and the one of µ is 0, µθ is the push-forward of µ by the map x  → x + ∇Λ(θ). Comparing the log-Laplace transforms of µθ on one hand, and the one of µ pushed-forward by x  → x + ∇Λ(θ), we ﬁnd that Λ satisﬁes the following functional equation:

∀θ ∈ DΛ,ξ ∈ Rn, Λ(ξ + θ) = Λ(θ) + Λ(ξ) + ξ,∇Λ(θ) . (26)

From this equation, we see that if ξ,θ ∈ DΛ, then ξ + θ ∈ DΛ. As the interior of DΛ is nonempty, we must have DΛ = Rn. Diﬀerentiating (26) with respect to ξ, we get

∀θ,ξ ∈ Rn, ∇Λ(ξ + θ) = ∇Λ(ξ) + ∇Λ(θ).

As ∇Λ is continuous, the above equation implies that ∇Λ is a linear function. Thus, Λ is a quadratic form and µ is a Gaussian measure.

![image 79](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile79.png>)

![image 80](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile80.png>)

![image 81](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile81.png>)

![image 82](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile82.png>)

Even though the Gaussian measure is the only measure µ to satisfy a transportation-entropy inequality with cost function Λ∗µ(x − y), it has been shown in [21] that up to some universal constant β > 0, any symmetric logconcave product measure µ on R satisﬁes a transportation-entropy inequality with cost function Λ∗µ x−βy . A similar result has been proven for measures with log-concave tails in [28] and weak transport-entropy inequalities. However, following the argument of the proof of Proposition 3.4, we see that it entails that for any continuously diﬀerentiable f : Rn → R, and µ a symmetric log-concave product measure,

![image 83](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile83.png>)

h β

log efdµ ≤ sup h∈Rn

f(x + h)dµ(x) − Λ∗µ

![image 84](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile84.png>)

 ∇f(z),x − y dµ(x)dµ(y),

+ sup

z∈Rn

Thus, it yields a multiplicative error from the true entropic cost one expects. But in the applications we have in mind, it will be important for us to have the best constant, that is β = 1, in order to produce a matching upper bound, so that we cannot rely on the mentioned results.

## 3.2 The exponential measure

The moral we deduce from the Gaussian case is that we have to look for cost functions beyond the ones of the form (x,y)  → α(x − y), in order to hope for transportation-entropy inequalities to be saturated by tilted measures. In the case of the exponential measure, we consider the cost function,

∀x,y ∈ Rn, c(x,y) =

n

yiΛ∗η

i=1

xi yi

![image 85](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile85.png>)

. (27)

The form of this cost function can be explained by the natural coupling of all the tilts (ηλ)λ of the exponential measure, where

∀λ > 0, ηλ = 1x≥0λe−x/λdx.

There is a simple way to transport ν onto νλ by the map x  → λx. This fact explains the shape of the cost function (27) as essentially a function of the ratio y/x. We now give a proof of Proposition 2.1.

Proof of Proposition 2.1. By the tensorization property of the transportationentropy inequalities (see Proposition 3.1), it is suﬃcient to prove the statement for n = 1. Let ν be a probability measure on R+. Let ν˜ and η˜ be the pushforward of respectively ν and η by the map x  → log x. Note that,

η˜ = e−ξ(x)dx,

with ξ(x) = ex − x, which is a convex function. From [29] we know that η˜ satisﬁes a transportation-entropy inequality with cost function c˜ deﬁned by,

∀x,y ∈ R, c˜(x,y) = ξ(x) − ξ(y) − ξ′(y)(x − y), that is,

c˜(x,y) = eyΛ∗ν(ex−y). But on one hand,

H(˜ν|η˜) = H(ν|η).

On the other hand,

Wc˜(˜ν,η˜) = Wc(ν,η), which gives the ﬁrst claim.

It only remains to prove that if ν is a tilt of ηn then it achieves the equality in the transportation-entropy inequality of Proposition 2.1. Let λ = (λ1,...,λn) with λi > 0. Denote by ηλ = ηλ

. Let π be a coupling between ηλ and ηn. By Jensen’s inequality we have,

i ⊗ ... ⊗ ηλ

n

n

Λ∗η xidηλ

(xi) ≤

i

i=1

n

yiΛ∗η

i=1

xi yi

![image 86](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile86.png>)

dπ(x,y).

On the other hand,

n

Λ∗η(λi). Thus,

H(ηλ|ηn) =

i=1

Wc(ηλ|ηn) ≥ H(ηλ|ηn), which ends the proof of the equality case.

![image 87](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile87.png>)

![image 88](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile88.png>)

![image 89](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile89.png>)

![image 90](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile90.png>)

Using duality, we can now give a proof of Proposition 2.5 on the integrability of empirical exponential processes. Proof of Proposition 2.5. Let V ⊂ Rn be a countable subset. Deﬁne the function g by,

∀x ∈ Rn, g(x) = sup ξ∈V

{ ξ,x − Ληn(ξ)}. By Propositions 2.1 and 3.3 we have,

log egdν ≤ sup

{g(y) − c(x,y)}dµ(x),

y∈Rn+

where c is deﬁned in (27). But, sup

{g(tx) − x,Λ∗η(t) },

{g(y) − c(x,y)} = sup

y∈Rn+

t∈Rn+

where tx = (t1x1,...,tnxn) and Λ∗η(t) = (Λ∗η(t1),...,Λη(tn)). Therefore, sup

{ ξ,tx − x,Λ∗η(t) − Ληn(ξ)}.

{g(y) − c(x,y)} = sup

sup

y∈Rn+

t∈Rn+

ξ∈V

Fix ξ ∈ V . We have

{ ξ,tx − x,Λ∗η(t) } =

sup

t∈Rn+

=

n

(tξi − Λ∗η(t))xi

sup

t>0

i=1

n

Λη(ξi)xi,

i=1

where we used the fact that Λη is the Legendre transform of Λ∗η.

![image 91](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile91.png>)

![image 92](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile92.png>)

![image 93](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile93.png>)

![image 94](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile94.png>)

## 3.3 The discrete hypercube

Let p ∈ (0,1) and µp = (1 − p)δ−1 + pδ1. Note that the tilts of µnp are exactly the product probability measures on {−1,1}n. One of the diﬃculties in ﬁnding a transportation-entropy inequality on the discrete hypercube which is saturated by product measures comes from the fact that the measure µnp does not carry enough information in order to sample from it all product measures on {−1,1}n. This assessment brings us to the conclusion that one has to enrich the background measure, and consider not a transportation cost between a given probability measure ν on {−1,1}n and µnp, but a transportation cost between ν and the uniform measure on [−1,1]n. In this section, we prove the transportation-entropy inequality of Proposition 2.3.

By the tensorization property of transportation-entropy inequalities, which we recalled in Proposition 3.1, we only have to prove Proposition 2.3 for n = 1. This is the content of the following lemma.

- 3.10 Lemma. For any ν probability measure on {−1,1},


(ν,U) = H(ν|µp), (28) where wp is deﬁned in (11), and U denotes the uniform measure on [−1,1]. Proof. Let h denote the mean of ν. Let π be the law of

Wwp

(U,sg(h − U)),

- where U is uniformly distributed on [−1,1], and sg(x) = 1 if x ≥ 0 and −1 otherwise. By deﬁnition of π,


wp(x,u)dπ(x,u) = 2E|Ip′(U)|1U∈(h,h

0) = Ip(h),

using the fact that Ip(h0) = 0. Besides,

H(ν|µp) = Ip(h), which proves the inequality

(ν,U) ≤ H(ν|µp).

Wwp

To prove the equality, we will prove that equality is achieved in the infconvolution inequality with cost function wp, where we set wp = +∞ on R \ {−1,1}, and use Proposition 3.3. Let t ∈ R, and deﬁne

Yt = max

{tx − wp(x,U)},

x∈{−1,1}

with U uniformly sampled in [−1,1]. We need to prove that

EYt = Λp(t), (29) where we use Λp as a short-hand for Λµ

. We have,

p

,−t + 2Ip′(U)1U<h

Yt = max t − 2Ip′(U)1U>h

0

0

+ max t,−t + 2Ip′(U) 1U<h

= max t − 2Ip′(U),−t 1U>h

.

0

0

There are two cases to consider. First we assume that h0 ≤ Λ′p(t). Observe that Ip is the Legendre transform of Λp. Therefore, Ip′ and Λ′p are inverse functions. We can write,

Yt = t − 2Ip′(U) 1h

0≤U≤Λ′p(t) − t1U>Λ′

. Thus,

p(t) + t1U<h

0

t 2

t 2

t 2

(Λ′p(t) − h0) − Ip(Λ′(t)) −

(1 − Λ′p(t)) +

(h0 + 1), where we used the fact that Ip(h0) = 0. Therefore,

EYt =

![image 95](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile95.png>)

![image 96](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile96.png>)

![image 97](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile97.png>)

EYt = tΛ′p(t) − Ip(Λ′p(t)) = Λp(t), since Ip is the Legendre transform of Λp. If h0 > Λ′p(t), we get Yt = −t1U≥h

p(t) + − t + 2Ip′(U) 1Λ′

+ t1U≤Λ′

p(t)<U<h0, which yields similarly EYt = Λp(t).

0

![image 98](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile98.png>)

![image 99](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile99.png>)

![image 100](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile100.png>)

![image 101](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile101.png>)

# 4 Strong integrability of empirical processes

In this section, we show how transportation-entropy inequalities which are saturated by tilts implies a strong integrability inequality for empirical processes.

- 4.1 Proposition. Let µ be a probability measure on R with support included in [−1,1]. Let µ˜ be a probability measure on R and let w : R × R → [0,+∞] be a lower semi-continuous function such that


∀ν ∈ P(R), Ww(ν,µ˜) ≤ H(ν|µ), and equality holds for the tilts of µ. Then, for any countable subset V ⊂ Rn, log esupξ∈V { x,ξ −Λµn(ξ)}dµn(x) ≤ κb(V ),

where κ is a universal constant, and b(V ) is deﬁned in (13).

Combining Proposition 4.1 with Proposition 2.3, we obtain the result of Proposition 2.4.

Proof. As µ has its support included in [−1,1], we can assume without loss of generality that w(x,y) = +∞ whenever x ∈/ [−1,1]. By the tensorization property of transport-entropy inequality (see Proposition 3.1), µn satisﬁes the transportation-entropy inequality,

∀ν ∈ P(Rn), Ww(ν,µ˜n) ≤ H(ν|µn), where

n

∀x,y ∈ Rn, w(x,y) :=

w(xi,yi).

i=1

Moreover, from the Fact 3.2, equality holds for the tilts of µn. Let V be a countable subset of Rn. By Proposition 3.3, we have

esupξ∈V { ξ,x −Λµn(ξ)}dµn(x) ≤ ϕdµ˜n,

where

∀y ∈ Rn, ϕ(y) = sup ξ∈V

sup

{ ξ,x − w(x,y) − Λµn(ξ)}.

y∈[−r,r]n

Thus, it remains to compute the expectation of a supremum of a certain empirical process. To this end, we will use the characterization of the boundedness of Bernoulli processes, proven by Bednorz and Latała [6]. We start by showing that this process has sub-Gaussian increments with variance factor given by the ℓ2-norm. We write in probabilistic notation,

where for any ξ ∈ Rn,

ϕdµ˜n = E sup ξ∈V

Zξ,

n

Zξ =

i=1

i − Λµ(ξi) ,

Tξ

= maxx∈[−r,r]{ξix − w(x,Yi)}, and Y = (Y1,...,Yn) is sampled according to ν˜n.

with Tξ

i

Let ξ,ζ ∈ Rn. For any i ∈ {1,...,n}, we have Tξ

i ≤ |ξi − ζi|.

i − Tζ

The fundamental fact about the process Zξ is that it is centered. This is due to the fact that equality in the transportation-entropy inequality with cost function w holds for tilts of µ. Indeed, by Proposition 3.3, we deduce that equality holds in the corresponding inf-convolution inequality for linear forms, which exactly says that,

= Λµ(ξi). Therefore, we can write

ETξ

i

n

(∆i − E∆i),

Zξ − Zζ =

i=1

where ∆i are independent, and |∆i| ≤ |ξi−ζi|. Thus, by Hoeﬀding’s inequality (see [25, Theorem 2.8]), for any t > 0,

t2 2||ξ − ζ||2ℓ2

P |Zξ − Zζ| > t ≤ exp −

. (30)

![image 102](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile102.png>)

Therefore, if V ⊂ V1 + V2, then for any ξ ∈ V , ξ = ξ1 + ξ2, with ξi ∈ Vi, Zξ = sup

{ ξ,x − w(x,Y )} − Λµn(ξ) ≤ sup

x∈[−r,r]n

{ ξ2,x − w(x,Y )} − Λµn(ξ2)

x∈[−r,r]n

+ ||ξ1||ℓ1 + Λµn(ξ2) − Λµn(ξ1 + ξ2).

As the support of µ is included in [−1,1], Λµn is 1-Lipschitz with respect to the ℓ1-norm. Therefore,

+ 2||ξ1||ℓ1. But, from the incremental property (30) and the Majorization Theorem (see [23, Theorem 12.16]), we get

Zξ ≤ Zξ

2

Zξ ≤ Lg(V2),

E sup

ξ∈V2

where L is a numerical constant, and g(V2) is the Gaussian width of V2, that is,

ξ,Γ , where Γ is a standard Gaussian random variable in Rn. Therefore, E sup

g(V2) = E sup ξ∈V2

||ξ||ℓ1 + Lg(V2) : V ⊂ V1 + V2 .

Zξ ≤ r inf 2 sup ξ∈V1

ξ∈V

We know from the characterization of the boundedness of Bernoulli processes [6] that there exists a numerical constant C > 0 such that,

||ξ||ℓ1 + g(V2) : V ⊂ V1 + V2 ≤ Cb(V ),

inf sup

ξ∈V1

which gives the claim.

![image 103](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile103.png>)

![image 104](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile104.png>)

![image 105](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile105.png>)

![image 106](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile106.png>)

Using the same comparison arguments between supremum of empirical processes, we obtain the following lemma which enables to estimate the diﬀerence between extensions {−1,1}n to [−1,1]n of functions with a low complexity set of gradient.

- 4.2 Lemma. Let f : Rn → R be a continuously diﬀerentiable function and


g the harmonic extension of f|{−1,1}n to [−1,1]n deﬁned as in remark 2.7. Then,

f(y) − g(y) ≤ κb(V ),

sup

y∈[−1,1]n

where κ is a numerical constant, V = ∇f([−1,1]n) and b(V ) is deﬁned as in

(13). Proof. Let y ∈ [−1,1]n. By deﬁnition,

f(y) − g(y) = Ef(y) − f(Xy),

where Xy is a random vector in {−1,1}n with independent coordinates and mean y. By the mean-value Theorem, we have

f(y) − g(y) ≤ E sup

ξ,Xy − y .

ξ∈V

Repeating the argument of the proof of Proposition 4.1, we see that the characterization of boundedness of Bernoulli processes [6] entails that there exists a universal constant λ > 0, such that

f(y) − g(y) ≤ λb(V ).

![image 107](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile107.png>)

![image 108](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile108.png>)

![image 109](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile109.png>)

![image 110](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile110.png>)

# 5 The mean-ﬁeld approximation

Building on the strong integrability of Bernoulli empirical processes, we give here a proof of the mean-ﬁeld approximation of the free energy of Gibbs measures on the discrete hypercube stated in Theorem 2.6.

In a ﬁrst step we identify the error term induced by the mean-ﬁeld approximation with the help of the following lemma. A proof of this result can be found in [1, Proposition 1.1].

- 5.1 Lemma. Let µ be a compactly supported probability measure on Rn. Denote by K the convex hull of its support. For any f : Rn → R continuously diﬀerentiable,


log efdµ ≤ sup{f − Λ∗µ} + log esupξ∈V { ξ,x −Λµ(ξ)}dµ(x),

- where V is the convex hull of ∇f(K), and Λ∗µ denotes the Legendre transform of Λµ.


Combining Lemma 5.1 with Propositions 2.3 and 4.1, we obtain Theorem 2.6. In fact, we have the following more general result which states that a dimension-free mean-ﬁeld approximation holds as soon as a transportationentropy inequality is saturated by tilts exists.

- 5.2 Proposition. Let µ be a probability measure on R with support included in [−1,1]. Assume there exist µ˜ a probability measure on R and w : R × R → [0,+∞] a lower semi-continuous function such that

∀ν ∈ P(R), Ww(ν,µ˜) ≤ H(ν|µ),

and equality holds for the tilts of µ. Then, there exists a universal constant κ > 0 such that for any f : Rn → R continuously diﬀerentiable,

log efdµ ≤ sup{f − Λ∗µ} + κb(V ), where V = ∇f([−1,1]n) and b(V ) is deﬁned in (13).

- 6 Proof of Theorem 2.12


Contrary to the nonlinear large deviations bounds shown in the previous works [10], [32], and [15], the proof of Theorem 2.12 will not rely on the computation of exponential moments of functions with a low complexity set of gradients. Instead, we will show as a ﬁrst step that one can reformulate the deviations of f(X) in terms of the deviations of the process ( θξ,X − Λµ(θξ))ξ∈V,θ>0. Then, we will use the strong integrability inequality of Bernoulli processes of Proposition 2.4 to control the deviations of the latter process.

In the next lemma, we relate the deviations of f(X) and of the process ( θξ,X − Λµ(θξ))ξ∈V,θ>0. We state it in the general setting where X is distributed to a compactly supported measure.

- 6.1 Lemma. Let µ be a compactly supported probability measure on Rn, whose support is not included in a hyperplane. Denote by K the convex hull of its support. Let f : Rn → R be a continuously diﬀerentiable function and let W be the convex hull of ∇f(K). Deﬁne the function,


∀t ∈ R, ϕ(y) = inf Λ∗µ(y) : f(y) ≥ t . Let t ∈ R and δ > 0. Assume that

∀s > t − δ, ϕ(t − δ) < ϕ(s). For any x ∈ K,

{ θξ,x − Λµ(θξ) − θδ} ≥ ϕ(t − δ),

f(x) ≥ t =⇒ sup

ξ∈W 0≤θ≤θ0

where θ0 = Λ∗µ(x)/δ.

Proof. Let x ∈ K such that and f(x) ≥ t. Arguing as in the proof of Proposition 3.5, we have

inf

f(x) − f(y) ≥ δ.

Λ∗µ(y)≤ϕ(t−δ)

By the mean value Theorem, we deduce that inf

sup

ξ,x − y ≥ δ,

Λ∗µ(y)≤ϕ(t−δ)

ξ∈W

which means,

Λ∗µ(x − z) ≥ ϕ(t − δ),

inf

hW (z)≤δ

where hW denotes the support function of W, namely, hW(z) = supξ∈W ξ,z . Note that Λ∗µ = +∞ on Kc by the Hahn-Banach Theorem. Moreover, Λ∗µ is lower semi-continuous as it is a Legendre transform. Thus Λ∗µ has compact level sets. As {hW ≤ δ} is closed, we deduce that the inﬁmum of Λ∗µ(x −.) on {hW ≤ δ} is achieved at some z∗.

Since Λ∗µ and hW are both convex functions, we deduce by Kuhn-Tucker Theorem (see [11, Theorem 9.4]) that there exists (η,θ) = (0,0) with η ∈ {0,1} and θ ≥ 0, such that θ(hW(z∗) − δ) = 0, and

ηΛ∗µ(x − z∗) = inf ηΛ∗µ(x − z) + θ(hW(z) − δ) : z ∈ Rn . (31)

Evaluating the function on the right-hand side at z = 0, we see that the non-triviality condition (η,θ) = (0,0) implies that η = 1. Moreover,

Λ∗µ(x) − θδ ≥ Λ∗µ(x − z∗) ≥ 0.

Thus, θ ≤ Λ∗µ(x)/δ. As Λ∗µ = +∞ on Kc, the inﬁmum in (31) can be restricted to x − K. Using the Minimax Theorem (see [11, Theorem 4.36]), we obtain,

Λ∗µ(x − z) + θ ξ,z .

inf Λ∗µ(x − z) + θhW(z) : z ∈ x − K = sup ξ∈W

inf

z∈Rn

We can identify this later inﬁmum using the fact that Λµ is the Legendre transform of Λ∗µ by [11, Theorem 4.21],

Λ∗µ(x − z) + θ ξ,z = θξ,x − Λµ(θξ), which ends the claim.

inf

z∈Rn

![image 111](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile111.png>)

![image 112](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile112.png>)

![image 113](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile113.png>)

![image 114](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile114.png>)

We now come back to the proof of Theorem 2.12. We have

1 p(1 − p)

∀x ∈ [−1,1]n, Ip(x) ≤ n log

.

![image 115](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile115.png>)

Denoting by Λp the log-Laplace transform of µnp, and using the preceding lemma, we get,

P(f(X) ≥ t) ≤ P sup

ξ∈W 0≤θ≤θ0

{ θξ,X − Λp(θξ) − θδ} ≥ ϕp(t − δ) ,

with θ0 = −n log(p(1 − p))/δ. We now perform a net argument on θ. Let D be a 1/(2√nL)-net of the interval [0,θ0], where

![image 116](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile116.png>)

L = sup

||∇f(x)||ℓ2 = sup λ∈W

||λ||ℓ2,

x∈K

One can ﬁnd a net D such that,

4n√nκ|log(p(1 − p))|L δ

![image 117](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile117.png>)

|D| ≤

.

![image 118](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile118.png>)

For X ∈ {−1,1}n ﬁxed, deﬁne the function

G : ξ ∈ R+  → sup ξ∈W

{ θξ,X − Λp(θξ) − θδ}.

We claim that for any θ′ ≤ θ,

G(θ) − G(θ′) ≤ 2(θ − θ′)L√n. (32) Indeed, there is some ξ ∈ V such that,

![image 119](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile119.png>)

G(θ) − G(θ′) ≤ (θ − θ′) ξ,X − Λp(θξ) + Λp(θ′ξ) − (θ − θ′)δ. By convexity,

G(θ) − G(θ′) ≤ (θ − θ′) ξ,X − ∇Λp(θ′ξ) . As ||ξ||ℓ2 ≤ L and ∇Λp(θ′ξ) ∈ [−1,1]n, we get the claim (32). Thus, using a union bound, we get, P sup

{ θξ,X − Λp(θξ) − θδ} ≥ ϕp(t − δ)

ξ∈W 0≤θ≤θ0

≤

P sup

{ θξ,X − Λp(θξ) − θδ} ≥ ϕp(t − δ) − 1 .

ξ∈W

θ∈D

Now, ﬁx θ ∈ D. By Chernof’s inequality, we have log P sup

{ θξ,X − Λp(θξ) − θδ} ≥ ϕp(t − δ) − 1 ≤ −ϕp(t − δ) + 1

ξ∈W

+ log Eesupξ∈W{ θξ,X −Λp(θξ)} − θδ. But by Proposition 2.4,

log Eesupξ∈W{ θξ,X −Λp(θξ)} ≤ κb(θW),

where κ is a numerical constant, and b(θW) is deﬁned in (13). Since b(θW) = θb(W), we ﬁnally get

log P sup

{ θξ,X − Λp(θξ) − θδ} ≥ ϕp(t − δ) − 1 ≤ −ϕp(t − δ) + 1

ξ∈W

+ θ(κb(W) − δ). Thus, if b(W) ≤ δ/κ, we obtain

P f(X) ≥ t ≤ |D|e−ϕ

p(t−δ)+1.

To complete the proof, it suﬃces to observe that the Rademacher mean-width of a set is the same as the one of its convex hull, so that b(W) = b(V ).

# 7 Proof of Theorem 2.14

We write Λ as a short-hand for Λµ. We will follow the lines of the argument in the Gaussian case from [17, proof of Theorem 1] which was based on Talagrand’s transportation-entropy inequality [29]. By deﬁnition,

I(ν) =  ∇Λ(∇f(x)),∇f(x) − Λ(∇f(x)) ef(x)dµ(x).

Recall that we denote µ1/2 = 21δ1 + 21δ−1. Let i ∈ {1,...,n}. We have

![image 120](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile120.png>)

![image 121](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile121.png>)

- 1

![image 122](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile122.png>)

- 2


1 2

ef(x

+) +

ef(x

−) ,

Λ′(∂if(x))∂if(x)ef(x)dµ1/2(xi) = Λ′(∂if(x))∂if(x)

![image 123](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile123.png>)

where x+ = (x1,...,xi−1,1,xi−1,...,xn) and x− = (x1,...,xi−1,−1,xi+1,...,xn). But Λ′ = tanh, therefore

ef(x

+) − ef(x

−)

Λ′(∂if(x)) =

ef(x+) + ef(x−). Therefore,

![image 124](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile124.png>)

1 2

Λ′(∂if(x))∂if(x)ef(x)dµ1/2(xi) =

![image 125](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile125.png>)

ef(x

+) − ef(x

−)

= xief(x)dµ1/2(xi). Thus,

Λ′(∂if(x))∂if(x)ef(x)dµ1/2(xi) = xi∂if(x)ef(x)dµ1/2(xi).

Integrating the above equality with respect to (x1,...,xi−1,xi+1,...,xn), and summing over i ∈ {1,...,n}, we deduce

 ∇Λ(∇f(x)),∇f(x) dµ(x) = x,∇f(x) dµ(x).

Therefore,

I(ν) = x,∇f(x) − Λ(∇f(x)) dµ(x). In particular,

x,ξ − Λ(ξ) dµ(x).

I(ν) ≤ sup

ξ∈V

But, the Gibbs variational principle (1) implies that

sup

ξ∈V

x,ξ − Λ(ξ) dµ(x) ≤ H(ν|µ) + log esupξ∈V { ξ,x −Λ(ξ)}dµ(x).

Using Proposition 2.4, we can conclude the proof.

# Acknowledgment

I thank Ofer Zeitouni for many fruitful discussions which helped me build the present paper, as well as his valuable comments on an earlier version of the manuscript. I am grateful to Ronen Eldan for several inﬂuential and helpful discussions.

# References

- [1] F. Augeri. Nonlinear large deviation bounds with applications to Wigner matrices and Erdös-Rényi graphs. arXiv:1810.01558.
- [2] F. Augeri. On heavy-tail phenomena in some large deviations problems. arXiv:1706.06184.
- [3] F. Augeri. On the large deviations of traces of random matrices. Ann. Inst. Henri Poincaré Probab. Stat., 54(4):2239–2285, 2018.
- [4] T. Austin. The structure of low-complexity Gibbs measures on product spaces. arXiv:1810.07278.
- [5] A. Basak and S. Mukherjee. Universality of the mean-ﬁeld for the Potts model. Probab. Theory Related Fields, 168(3-4):557–600, 2017.
- [6] W. Bednorz and R. Latała. On the boundedness of Bernoulli processes. Ann. of Math. (2), 180(3):1167–1203, 2014.
- [7] S. Bobkov, I. Gentil, and M. Ledoux. Hypercontractivity of HamiltonJacobi equations. J. Math. Pures Appl. (9), 80(7):669–696, 2001.
- [8] C. Borgs, J. T. Chayes, H. Cohn, and Y. Zhao. An Lp theory of sparse graph convergence II: LD convergence, quotients and right convergence. Ann. Probab., 46(1):337–396, 2018.
- [9] C. Borgs, J. T. Chayes, L. Lovász, V. T. Sós, and K. Vesztergombi. Convergent sequences of dense graphs II. Multiway cuts and statistical physics. Ann. of Math. (2), 176(1):151–219, 2012.
- [10] S. Chatterjee and A. Dembo. Nonlinear large deviations. Adv. Math., 299:396–450, 2016.
- [11] F. Clarke. Functional analysis, calculus of variations and optimal control, volume 264 of Graduate Texts in Mathematics. Springer, London, 2013.
- [12] N. Cook and A. Dembo. Large deviations of sub-graph counts in sparse Erdős-Rényi. arXiv:1809.11148.
- [13] A. Dembo. Information inequalities and concentration of measure. Ann. Probab., 25(2):927–939, 1997.
- [14] A. Dembo and O. Zeitouni. Large deviations techniques and applications, volume 38 of Stochastic Modelling and Applied Probability. SpringerVerlag, Berlin, 2010. Corrected reprint of the second (1998) edition.
- [15] R. Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations. arXiv:1612.04346.
- [16] R. Eldan. Taming correlations through entropy-eﬃcient measure decompositions with applications to mean-ﬁeld approximation. arXiv:1811.11530.
- [17] R. Eldan and M. Ledoux. A dimension-free reverse logarithmic Sobolev inequality for low-complexity functions in Gaussian space. arXiv:1903.07093.
- [18] N. Gozlan and C. Léonard. Transport inequalities - a survey. Markov Process. Related Fields, (16):635–736, 2010.
- [19] V. Jain, F. Koehler, and E. Mossel. The mean-ﬁeld approximation: Information inequalities, algorithms, and complexity. In Conference On Learning Theory, COLT 2018, Stockholm, Sweden, 6-9 July 2018., pages 1326–1347, 2018.


- [20] V. Jain, F. Koehler, and A. Ristesk. Mean-ﬁeld approximation, convex hierarchies, and the optimality ofcorrelation rounding: a uniﬁed perspective. arXiv:1808.07226.
- [21] R. Latała and J. O. Wojtaszczyk. On the inﬁmum convolution inequality. Studia Math., 189(2):147–187, 2008.
- [22] M. Ledoux. The concentration of measure phenomenon, volume 89 of Mathematical Surveys and Monographs. American Mathematical Society, Providence, RI, 2001.
- [23] M. Ledoux and M. Talagrand. Probability in Banach spaces, volume 23 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1991. Isoperimetry and processes.
- [24] K. Marton. Bounding d-distance by informational divergence: a method to prove measure concentration. Ann. Probab., 24(2):857–866, 1996.

![image 126](<2019-augeri-transportation-approach-mean-field-approximation_images/imageFile126.png>)

- [25] P. Massart, G. Lugosi, and S. Boucheron. Concentration Inequalities : A Nonasymptotic Theory of Independence. Oxford University Press, 2013.
- [26] F. Otto and C. Villani. Generalization of an inequality by Talagrand and links with the logarithmic Sobolev inequality. J. Funct. Anal., 173(2):361– 400, 2000.
- [27] R. T. Rockafellar. Convex analysis. Princeton Landmarks in Mathematics. Princeton University Press, Princeton, NJ, 1997.
- [28] M. Strzelecka, M. Strzelecki, and T. Tkocz. On the convex inﬁmum convolution inequality with optimal cost function. arXiv:1702.07321.
- [29] M. Talagrand. Transportation cost for Gaussian and other product measures. Geom. Funct. Anal., 6(3):587–600, 1996.
- [30] C. Villani. Optimal transport, volume 338 of Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences]. Springer-Verlag, Berlin, 2009. Old and new.
- [31] R. Vitale. The Wills functional and Gaussian processes. Ann. Probab., 24(4):2172–2178, 1996.
- [32] J. Yan. Nonlinear Large Deviations: Beyond the Hypercube. arXiv:1703.08887.


