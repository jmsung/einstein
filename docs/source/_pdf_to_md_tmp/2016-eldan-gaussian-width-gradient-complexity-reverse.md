# Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations

### Ronen Eldan∗

arXiv:1612.04346v6[math.PR]29Jun2018

Abstract

We prove structure theorems for measures on the discrete cube and on Gaussian space, which provide sufﬁcient conditions for mean-ﬁeld behavior. These conditions rely on a new notion of complexity for such measures, namely the Gaussian-width of the gradient of the log-density. On the cube {−1,1}n, we show that a measure ν which exhibits low complexity can be written as a mixture of measures {νθ}θ∈I such that: i. for each θ, the measure νθ is a small perturbation of ν such that log dνdνθ is a linear function whose gradient is small and, ii. νθ is close to some product measure, in Wasserstein distance, for most θ. Thus, our framework can be used to study the behavior of low-complexity measures beyond approximation of the partition function, showing that those measures are roughly mixtures of product measures whose entropy is close to that of the original measure. In particular, as a corollary of our theorems, we derive a bound for the na¨ıve mean-ﬁeld approximation of the log-partition function which improves the nonlinear large deviation framework of Chatterjee and Dembo [2016] in several ways: 1. It does not require any bounds on second derivatives. 2. The covering number is replaced by the weaker notion of Gaussian-width 3. We obtain stronger asymptotics with respect to the dimension. Two other corollaries are decomposition theorems for exponential random graphs and large-degree Ising models. In the Gaussian case, we show that measures of low-complexity exhibit an almost-tight reverse Log-Sobolev inequality.

![image 1](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile1.png>)

## Contents

- 1 Introduction 2

- 1.1 Main structure theorems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
- 1.2 A large deviation framework for functions of low complexity . . . . . . . . . . 6 1.2.1 An example application: triangles in G(N, p) . . . . . . . . . . . . . . 7
- 1.3 Mean-ﬁeld behavior of the Ising model with large degree . . . . . . . . . . . . 8
- 1.4 A decomposition theorem for exponential random graphs . . . . . . . . . . . . 9
- 1.5 Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10


- 2 The Gaussian case 12


- 2.1 Tilts are close to product measures . . . . . . . . . . . . . . . . . . . . . . . . 12
- 2.2 A reverse log-Sobolev inequality . . . . . . . . . . . . . . . . . . . . . . . . . 14


![image 2](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile2.png>)

∗Weizmann Institute of Science. Incumbentof the Elaine Blond Career Development Chair. Partially supported by the Israel Science Foundation (grant No. 715/16).

- 3 The discrete case 17

- 3.1 Some preliminary deﬁnitions . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

- 3.1.1 Harmonic extensions . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
- 3.1.2 Some core constructions . . . . . . . . . . . . . . . . . . . . . . . . . 18


- 3.2 Two main steps towards the proof . . . . . . . . . . . . . . . . . . . . . . . . 20
- 3.3 The ﬁrst step: obtaining an estimate on W1 using H . . . . . . . . . . . . . . . 23
- 3.4 The second step: ﬁnding product-like tilts . . . . . . . . . . . . . . . . . . . . 25


- 3.4.1 Stochastic constructions . . . . . . . . . . . . . . . . . . . . . . . . . 25
- 3.4.2 Proof of Proposition 18 . . . . . . . . . . . . . . . . . . . . . . . . . . 28


- 4 The large deviation framework 34
- 5 Exponential random graphs and complexity of subgraph counts 38
- 6 Appendix - proofs of Auxiliary results 41


## 1 Introduction

Let µ be a measure on the discrete hypercube Cn = {−1, 1}n. In this work, we are interested in the following quesiton: Under what natural conditions does this measure admit an approximate decomposition into a mixture of product measures most of which having roughly the same entropy as the measure µ? This form of simplicity is a strong manifestation of what is referred to in the statistical mechanics literature as mean-ﬁeld behavior.

Our main theorem provides a sufﬁcient condition for such behavior, using a new notion of complexity, namely Gaussian-width gradient complexity. We say that a measure has lowcomplexity if one has nontrivial bounds on the Gaussian width of the gradient of its log-density (this is made rigorous and quantitativebelow). Our deﬁnition is inspired by Chatterjee and Dembo

- [2016], where covering numbers are considered.


Our main theorem (Theorem 3 below) shows that for a measure µ on Cn with log-Lipschitz density, a low-complexity condition implies the existence of an approximate decomposition into product measures as described above. Additionally, these measures can be written as small tilts of the original measure, namely, they can be attained by applying a change of density with respect to some log-linear function whose gradient is small.

Perhaps the most studied manifestation of mean ﬁeld behavior is the approximation of the partition function, up to ﬁrst order, via a product measure. More precisely, deﬁning Cn = {−1, 1}n equipped with the uniform measure µ, the Gibbs variational principle states that

log efdµ = sup

ν

fdν − DKL(ν µ) (1)

where the supremum is taken over all probability measures ν on Cn and DKL denotes the Kullback-Leibler divergence (deﬁned below). The na¨ıve mean-ﬁeld approximation is said to hold true when the supremum is approximately saturated by the class of product measures.

Suppose that the quantity log efdµ is of order O(n). One is often interested in cases where the approximation holds in ﬁrst order, hence, the above inequality is saturated by product measures up to an error of o(n). This sort of approximation corresponds to the case that the function f is correlated with a linear function in a region whose measure is at least exp(−o(n)). The main theorem of Chatterjee and Dembo [2016] gives a sufﬁcient condition for such an approximation to hold true. Our work takes another step, giving sufﬁcient conditions for f to

be correlated with a (relatively small) family of linear functions almost-everywhere. In physical terms, whereas the approximation for the partition function is equivalent to the existence of a single pure-state of non-negligible probability, our result gives a decomposition of the entire measure into pure states. As shown in an example below, replacing the unique product measure by a family thereof is necessary.

Our structure theorem applies to several settings, including subgraph-counting functions in random graphs, density of arithmetic progressions, mean-ﬁeld Ising and Potts models and exponential random graphs (see below for background and references). A central corollary of the above-mentioned estimate for the partition function is a general framework deriving large deviation principles for nonlinear functions of Bernoulli random variables (Theorem 5 below) which extends the one in Chatterjee and Dembo [2016] and improves the bounds in the examples considered there. Our framework provides a seemingly cleaner theorem which, in particular, does not require any assumptions on second derivatives.

A central example where the large deviations framework comes in handy is in the derivation of a large deviation principle for the number of triangles (or more generally, subgraph densities) in an Erd¨os-Re´nyi random graph G = G(N, p). Letting T denote the number of triangles in G, the goal is to ﬁnd precise asymptotics for log P(T ≥ (1 + δ)ET) as N → ∞ (with p possibly depending on N). For background and history concerning large deviations for random graphs, we refer the reader to the book Chatterjee [2017] and references therein. When the function f in (1) is the number of triangles T, it turns out that when maximizing over product measures ν, the right hand side becomes a tractable quantity which can be calculated almost precisely, as was done in Lubetzky and Zhao [2014] for the case of triangles, and later in Bhattacharya et al.

- [2017] for general subgraph counts. As we will demonstrate, applying our framework to the these examples seems to be a rather simple task that requires signiﬁcantly less technical work compared to previous works.


In a subsequent work, Eldan and Gross [2017a], our methods are used to derive a theorem showing that these product measures are close to critical points of the associated mean-ﬁeld functional, giving a more precise characterization of the mixture.

### 1.1 Main structure theorems

To formulate our results, let us start with some deﬁnitions. Consider the discrete cube Cn = {−1, 1}n equipped with the uniform probability measure µ. First, we would like to deﬁne a notion of complexity of a function f : Cn → R. To this end, we ﬁrst deﬁne the Gaussian-width of a set K ⊂ Rn as

GW(K) = E sup

x, Γ

x∈K

where Γ ∼ N(0, Id) is a standard Gaussian random vector in Rn. Next, for a function f : Cn → R and a point y = (y1, ..., yn) ∈ Cn and i ∈ [n], we write

- 1

![image 3](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile3.png>)

- 2


∂if(y) =

(f(y1, . . ., yi−1, 1, yi+1, . . .yn) − f(y1, . . ., yi−1, −1, yi+1, . . .yn)) and deﬁne the discrete gradient of f as

∇f(y) = (∂1f(y), . . ., ∂nf(y)). (2) we will also deﬁne

|∂if(y)|,

Lip(f) = max

i∈[n],y∈Cn

the discrete Lipschitz constant of f. Finally, for a function f : Cn → R, the gradient-complexity of f will be deﬁned as

D(f) := GW ({∇f(y) : y ∈ Cn} ∪ {0}) (3) and for a measure ν on Cn, by slight abuse of notation, we deﬁne its complexity as

dν dµ

D(ν) := D log

.

![image 4](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile4.png>)

- Remark 1. In the following, the main regime which is of interest to us is functions f which takes values of order O(n) and whose Lipschitz constant is Lip(f) = O(1). It is clear that such functions trivially have complexity at most O(n). The functions for which our results will be nontrivial are the ones whose complexity is o(n).

For two measures ν1, ν2 on Cn we deﬁne the Wasserstein mass-transportation distance between ν1, ν2 as

W1(ν1, ν2) = inf (X,Y) s.t.

X∼ν1,Y ∼ν2

EdH(X, Y )

where dH denotes the Hamming distance. We say that a measure ξ on Cn is a product measure if X1, . . ., Xn are independent where (X1, . . ., Xn) ∼ ξ.

Roughly speaking, our ﬁrst result states that if ν is a measure of low complexity then there exists another measure ν˜ whose log-density is close to that of ν in L∞ and such that its W1distance to some product measure ξ is small.

Theorem 1. Let ν be a probabilitymeasure on the discrete cube Cn. Then for every ε ∈ (0,1/16), there exists a probability measure ν˜ such that if we deﬁne the functions f, f˜ by the equations dν dµ = ef and dµdν˜ = ef˜ then we have

![image 5](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile5.png>)

![image 6](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile6.png>)

|f(y) − f˜(y)| ≤ εn, ∀y ∈ Cn (4) and for the unique product measure ξ on Cn satisfying ydξ(y) = ydν˜(y), one has that

W1(˜ν, ξ) ≤ 27

![image 7](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile7.png>)

nD(ν) ε

![image 8](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile8.png>)

+ 4ne−

1 64ε2

![image 9](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile9.png>)

.

Furthermore, there exists a set I ⊆ [n] with |I| ≥ n − 2ne−

1 32ε2

![image 10](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile10.png>)

such that the following holds. For a measure ρ on Cn, denote by πI(ρ) the marginal law of ρ on the subset I. Let ξ′ := πI(ξ) × π[n]\I(˜ν). Then one has

W1(˜ν, ξ′) ≤ 26

![image 11](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile11.png>)

nD(ν) ε

![image 12](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile12.png>)

.

- Remark 2. It is important to emphasize that the function f˜ provided by the above theorem is by no means unique. For the sake of intuition, a good example to consider is when f(y) = −βT(G), where T(G) is the number of triangles in the N-vertex graph whose edge set is


deﬁned by the point y ∈ Cn, n = N2 and β = 1/N. In this case, one expects the measure ν to be (in a rough sense) close to a distribution on approximately-bipartite graphs. It is clear

by symmetry that this distribution is invariant under permutations of the vertices. The choice of the function f˜ in the above theorem should then correspond to the choice of the partition, under which the edges should be approximately independent. Note that the entropy associated the choice of this partition is of the order N, which is signiﬁcantly smaller than the entropy we expect to have left after that choice, which is of order n.

Next, we would like to formulate an easy corollary to the above, which will be useful in the context of large deviation theory. For two probability measures ν1, ν2 on Cn, we deﬁne the Kullback-Leibler divergence of ν1 with respect to ν2 as

DKL(ν1 ν2) = log dν

dν2(y) dν1(y). The corollary is analogous to [Chatterjee and Dembo, 2016, Theorem 1.6]. It reads: Corollary 2. For every f : Cn → R, there exists a product probability measure ξ on Cn which satisﬁes

1

![image 13](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile13.png>)

efdµ ≤ fdξ − DKL(ξ µ) + 64Lip(f)2/3D(f)1/3n2/3.

log

Cn

- Remark 3. One can strengthen the above Corollary in the sense that Lip(f) can be replaced by a weaker notion of continuity. An inspection of the proof reveals that for any monotone, bounded and continuous function ϕ : [0, 1] → [0, ∞) with ϕ(0) = 0, the following is true: Under the assumption D(f) = o(n), one gets a nontrivial mean-ﬁeld approximation and as


long as f attains property that for all x, y ∈ Cn, one has |f(x)−nf(y)| ≤ ϕ d

H(x,y)

n . In other words, f does not have to be Lipschitz in a local sense, it only needs to have small oscillations on some mesoscopic scale.

![image 14](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile14.png>)

![image 15](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile15.png>)

We now turn to the formulation of our main structure theorem. For a measure ν on Cn such that dν = efdµ and for a point θ ∈ Rn we deﬁne the tilt of ν with respect to θ, denoted by τθν, by the equation

ef(y)+ θ,y Cn ef(z)+ θ,z dµ

d(τθν) dµ

(y) =

.

![image 16](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile16.png>)

![image 17](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile17.png>)

Moreover, for every measure ν on Cn, deﬁne by ξ(ν) to be the unique product measure having the same marginals as ν. Deﬁne also B(x0, r) := {x ∈ Rn; x − x0 2 ≤ r}.

Our main structure theorem states that any measure ν of low complexity admits a decomposition into small tilts which are close to product measures. Our theorem reads,

- Theorem 3. Let ν be a probability measure on the discrete cube Cn. For every ε ∈


−1/2 and α > 1, there exists a measure m supported on B(0, ε√n) ∩ [−1, 1]n such that ν admits the decomposition

0, 18 log D 4(nν)

![image 18](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile18.png>)

![image 19](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile19.png>)

![image 20](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile20.png>)

ϕdν =

Cn

ϕd(τθν) dm(θ) (5)

B(0,ε√n) Cn

![image 21](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile21.png>)

for every test function ϕ : Cn → R and such that there exists Θ ⊂ Rn with m(Θ) > 1 − n1 − α1 so that for every θ ∈ Θ one has

![image 22](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile22.png>)

![image 23](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile23.png>)

![image 24](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile24.png>)

αnD(ν) ε

W1 τθν, ξθ ≤ 16

, (6)

![image 25](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile25.png>)

for some product measure ξθ. Moreover, we have that

DKL(ν µ) − DKL(τθν µ)dm(θ) ≤ 2εn. (7)

#### Remark 4. In the subsequent work Eldan and Gross [2017a] it is shown that, under an extra technical condition involving the second derivatives of log dµdν, the measures ξθ are critical points of the associated Gibbs functional.

![image 26](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile26.png>)

We move on to formulating our theorem for the Gaussian case. Denote by γ the standard Gaussian measure on Rn. For a differentiable function f : Rn → R we deﬁne the complexity of f as D(f) = GW({∇f(x) : x ∈ Rn}). Let ν be a density with respect to γ such that dν = efdγ. In this case we deﬁne

DKL(ν γ) = fdν, I(ν) = |∇f|2dν

the Kullback-Leibler divergence and the Fisher information of of ν. The log-Sobolev inequality on Gaussian space asserts that for every measure ν,

I(ν) ≥ 2DKL(ν γ). The following theorem reverses this inequality for measures of low complexity.

- Theorem 4. Let ν be a measure on Rn, such that f = log dγdν for some twice-differentiable function f. One has

![image 27](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile27.png>)

I(ν) − 2DKL(ν γ) ≤ 2D(ν)2/3I(ν)1/3 + max − inf

x∈Rn

∆f(x), 0 .

1.2 A large deviation framework for functions of low complexity

We now turn to formulating our main theorem concerning nonlinear large deviations, which is parallel to [Chatterjee and Dembo, 2016, Theorem 1.1]. Fix a function f : Cn → R. For

- 0 ≤ p ≤ 1, deﬁne µp to be the measure whose density is dµp

![image 28](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile28.png>)

dµ

(y1, . . ., yn) =

i∈[n]

(1 − yi(1 − 2p)).

Our central deﬁnition is the rate function φp(t) = inf

ξ∈PM(Cn)

DKL(ξ µp) : fdξ ≥ tn . (8)

where PM(Cn) is the space of product probability measures over Cn. Theorem 5. Let p ∈ (0, 1) and let Y ∼ µp. Then for every t, δ ∈ R which satisfy 0 < δ <

- 1




nφp(t − δ), we have the bound

![image 29](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile29.png>)

log P(f(Y ) ≥ tn) ≤ −φp(t − δ) 1 − 64Ln−1/3 with

- 1 δ

![image 30](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile30.png>)

- 2Lip(f) + |log(p(1 − p))| 2/3 2D(f) +


1 δ

Lip(f)2

L =

![image 31](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile31.png>)

1/3

.

Lip(f)2 ≤ 21 holds, we also have the lower bound log P(f(Y ) ≥ (t − δ)n) ≥ −φp(t) 1 +

Moreover, whenever the assumption nδ1

![image 32](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile32.png>)

![image 33](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile33.png>)

2

2 nδ2

Lip(f)2 − 2.

![image 34](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile34.png>)

#### Remark 5. If the function f is O(1)-Lipschitz, the above theorem shows that one is able to obtain a nontrivial bound with some δ → 0 as long as D(f)/n tends to 0.

- 1.2.1 An example application: triangles in G(N, p)


To illustrate how the above theorem can be applied, let us use it to derive a large deviation principle for the number of triangles in G(N, p). A second example application of the framework is to large deviations of the number of arithmetic sequences for random subsets of Z/nZ, which we will not discuss here, was carried out in Bhattacharya et al. [2016].

Let P denote upper triangular arrays of the form y = (yi,j)1≤i<j≤N where yi,j ∈ {−1, 1}. We associate every x ∈ P with the undirected graph Gy = ([N], E) where, for i < j we have (i, j) ∈ E if and only if yi,j = 1. We will also understand y as a point in Cn with n = N2 .

Deﬁne f(y) = N1 T(Gy) where T(G) is the number of triangles in G. Deﬁne also A(y) to be the adjacency matrix of Gy, which is in other words the unique symmetric matrix whose above-diagonal half determined by y. Moreover for a symmetric matrix A deﬁne u(A) ∈ R(

![image 35](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile35.png>)

N 2

) to be the above-diagonal vector associated with A, so that u(A)i,j = Ai,j for i < j. It is easily checked that f(y) = 61N Tr(A(y)3) and ∇f(y) = N1 u(A(y)2). Deﬁne

![image 36](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile36.png>)

![image 37](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile37.png>)

B2 N

: B ∈ MN×N, B = BT, |Bi,j| ≤ 1, ∀i, j ∈ [N] .

A =

![image 38](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile38.png>)

Clearly {∇f(y) : y ∈ Cn} ∈ u(A). We would like to bound GW(u(A)). First remark that for all A ∈ A we have that A is positive deﬁnite with Tr(A) ≤ N, so the Schatten 1-norm of A is bounded by N. The noncommutative H¨older inequality therefore gives that for every N × N matrix Q, one has

sup

Tr(AQ) ≤ N Q OP.

A∈A

N 2

) and deﬁne by M(Γ) the unique symmetric N × N matrix whose diagonal is zero and whose above-diagonal part is equal to Γ. Then we have by the above inequality,

Now let Γ = (Γi,j)1≤i<j≤N be a standard Gaussian random vector in R(

Tr(AM(Γ)) ≤ NE M(Γ) OP ≤ 2N3/2

 ∇f(y), Γ ≤ E sup

E sup

A∈A

y∈Cn

where the last inequality is well-known, and follows for example from an application of Slepian’s lemma. Moreover, remark that the entries of B2/N above are bounded by 1. We conclude the following,

Fact 6. One has that D(f) ≤ 5n3/4 and Lip(f) ≤ 1.

This proof is easily generalized for any subgraph count, see Lemma 33 below. An application of Theorem 5 gives for all t and n−1/2 < δ < n1φp(t − δ),

![image 39](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile39.png>)

2

nδ2 ≤ log P(f(Y ) ≥ tn) ≤ −φp(t − δ) 1 − 64Ln−1/3 with

−φp(t + δ) 1 +

![image 40](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile40.png>)

20 δ

(3 + | log(p(1 − p))|)2/3 n1/4. We now state the solution to the variational problem obtained by Lubetzky and Zhao, Theorem 7 (Lubetzky and Zhao [2014]). If N−1/2 ≪ pN ≪ 1 then one has

L =

![image 41](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile41.png>)

((α + 1)p3N)

- 2

![image 42](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile42.png>)

- 3


φp

= min α2/3,

N

α .

lim

![image 43](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile43.png>)

N

2 p2N log(1/pN)

N→∞

Let pN ∈ (0, 1) be some sequence depending on N. Fix α > 0 and deﬁne tN = (1 + α)p3N and δN = p3N/(log log N). Thus, the assumption

pn ≫ N−1/18 log(N) ﬁnally gives

log P T(G(N, pN)) ≥ (1 + α)p3N

N 3

n 6

= log P f(Y ) ≥ (1 + α)p3N

![image 44](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile44.png>)

= −φp(tN)(1+o(1)).

### 1.3 Mean-ﬁeld behavior of the Ising model with large degree

In this section we demonstrate how our framework can be used to study the behavior of the Ising model satisfying a mean-ﬁeld assumption in the spirit of Basak and Mukherjee [2017]. For the sake of simplicity, we will only discuss the Ising model, however our methods work for the Potts model as well.

Let V = [n] be a set of sites, and consider a spin system taking conﬁgurations σ ∈ {−1, 1}V .

Let A = (Ai,j)ni,j=1 be a real-valued, symmetric interaction matrix, and b = (bi)ni=1 a vector of magnetic moments bi ∈ R. Consider the Hamiltonian

f(σ) = σ, Aσ + b, σ .

Deﬁne ν to be the probability measure whose density is dµdν = f − log Z with Z being the normalizing constant. In order to use our framework, let us try to calculate the complexity of f.

![image 45](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile45.png>)

To this end, ﬁx σ ∈ Cn and i ∈ [n]. Write σ± = (σ1, . . ., σi−1, ±1, σi+1, . . ., σn). We have 2∂if(σ) = σ+, Aσ+ − σ−, Aσ− + b, σ+ − σ− = 2

Ai,jσj + 2bi.

j∈[n]\{i}

With the legitimate assumption Ai,i = 0 for i ∈ [n], we get

∇f(σ) = Aσ + b. We therefore have

Aσ + b, Γ ≤ E sup

D(f) = E sup

σ∈Cn

| Aσ, Γ | + E| b, Γ | ≤

σ∈Cn

√nE sup

![image 46](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile46.png>)

| Ax, Γ | + b 2

x∈B(0,1)

= √nE AΓ 2 + b 2 ≤ nE AΓ 22 + b 2 = n(TrA2 + b2max)

![image 47](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile47.png>)

![image 48](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile48.png>)

![image 49](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile49.png>)

where bmax := maxi∈[n] |bi|. The assumption Tr(A2) = o(n) is referred to in Basak and Mukherjee [2017] as the mean-ﬁeld assumption. Next, we also have that Lip(f) ≤ U(A) + bmax where

| Aσ, ei | = max

U(A) = max

i∈[n]

i∈[n],σ∈Cn

|Ai,j|.

j∈[n]

Invoking Corollary 2, we get the following mean-ﬁeld approximation for Z: there exists a product probability measure ξ on Cn which satisﬁes

1/6

(U(A) + bmax)4 (TrA2 + b2max) n

1 n

log Z − fdξ − DKL(ξ µ) ≤ 64

.

![image 50](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile50.png>)

![image 51](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile51.png>)

In particular, if U(A) = O(1), bmax = O(1) and TrA2 = o(n), then

1 n

![image 52](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile52.png>)

log Z − fdξ + DKL(ξ µ) = o(1).

The result in Basak and Mukherjee [2017] relies on a weaker condition than U(A) = O(1), namely that supσ∈C

Aσ 1 = O(n). However, following remark 3, it is not hard to check that our assumption U(A) = O(1) can be replaced by a weaker assumption: it is enough to assume, for instance, that there exists some p > 1 such that supσ∈C

n

Aσ p = O(n1/p).

n

Aside from the approximation of the partition function, our framework gives more information about the behavior of ν. Under the above conditions, an application of Theorem 3 tells us that ν can be approximately decomposed to a mixture of product measures, whose typical entropy is very close to the entropy of the system.

### 1.4 A decomposition theorem for exponential random graphs

The goal of this subsection is to demonstrate an application of Theorem 3 to exponential random graphs. Loosely speaking, the theorem below states that an exponential random graph is close in Hamming distance to a random graph which can be expressed as a mixture of graphs with independent edges, in a way that most of the entropy comes from the independent graphs (rather than from the mixture).

For a two ﬁnite graphs H, G with m, N vertices respectively, we denote by Hom(H, G) the number of homomorphisms from the vertex set of H to that of G (by homomorphisms, we mean that for every edge in H, the corresponding image should also be found in G, but not necessarily the other way around). The Homomorphism density of H in G is then deﬁned as

Hom(H, G) Nm

t(H, G) =

.

![image 53](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile53.png>)

Let H1, . . ., Hl be ﬁnite simple graphs and β1, . . ., βl be real numbers. Let G be a random simple graph on N vertices deﬁned by

P(G = g) = Z−1 exp N2

l

βit(Hi, g) (9)

i=1

for all simple graph g on n vertices, where Z is a normalizing constant. The graph G is referred to in the literature as an exponential random graph (see e.g. Chatterjee and Diaconis [2013] and references therein).

N 2

) deﬁne by G(N,  p) the random graph whose edges determined by independent Bernoulli random variables whose probabilities correspond to the vector p . Deﬁne

For p  ∈ [0, 1](

I(p ) = −

N 2

)

(i,j)∈(

pi,j log pi,j + (1 − pi,j) log(1 − pi,j) = Ent(G(N, p )).

N 2

Moreover, for a probability measure ρ on [0, 1](

) deﬁne by G(N, ρ) the ”ρ-mixture” satisfying

P(G(N, ρ) = g) = P(G(N,  p) = g)dρ(p )

for all simple graphs g on N vertices.

It is clear that every random graph G on N vertices has the distribution G(N, ρ) for some measure ρ (we can simply take ρ to be supported on {0, 1}(

N 2

) with probabilities corresponding to the individual instances). However, it is interesting to look for a representation where most of the entropy comes from the graphs G(N, p ) rather than from the distribution ρ. We thus make the following deﬁnition.

Deﬁnition 8. We say that a random graph G is an ε-mixture if there exists a measure ρ on [0, 1](

N 2

) such that G = G(N, ρ) and such that

Ent(G) ≤ I(p )dρ(p ) + ε

N 2

= Ent(G(N,  p))dρ(p ) + ε

N 2

.

Finally, for two simple graphs g = (V, E), g′ = (V, E′) deﬁne dH(g, g′) = |E∆E′|, the Hamming distance between the corresponding edge sets. Our theorem roughly says that exponential graphs can be coupled with o(1)-mixtures in a way that the Hamming distance is o N2 .

- Theorem 9. For any integers N, l, ﬁnite simple graphs H1, . . ., Hl, real numbers β1, . . ., βl and ε ∈ (0, 1/2), there exists a coupling (G, G′) such that the marginal G is the associated random exponential graph deﬁned in equation (9), the graph G′ is an ε-mixture, and such that


20 N2 11/12 ε1/3

EdH(G, G′) =

![image 54](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile54.png>)

l

|βi||E(Hi)|

i=1

1/3

.

where E(Hi) denotes the number of edges of Hi.

- Remark 6. The ideas results of this section are extended in a subsequent work Eldan and Gross [2017b], where it is shown that, in the dense regime, the measure ρ is essentially supported on block matrices.


### 1.5 Approach

Our two main theorems, Theorem 3 and Theorem 4, heavily rely on a construction coming from stochastic control theory, of an entropy-optimal coupling of the measure ν to a Brownian motion F¨ollmer [1985], Borell [2002], Lehec [2013], described below. This coupling has proven to be a strong tool for proving functional inequalities: In Borell [2002] it is used to give a proof of the Pre´kopa-Leindler inequality. Later on, in Lehec [2013] a representation formula for the relative entropy was derived which can be used to provide extremely simple proofs of several information-theoretical inequalities on Gaussian space, such as Shannon’s inequality and the Log-Sobolev inequality. In Eldan and Lee [2014] the same coupling was used to prove an L1version of hypercontractivity on Gaussian space, resolving the Gaussian variant of a conjecture by Talagrand whereas in Eldan et al. [2016] it is used to show that a local-curvature condition implies a transportation-entropy inequality for Markov chains.

Let us now describe this coupling and the general lines in which it is used to prove Theorem 3. Fix a measure ν on Cn with dν = efdµ. Deﬁne Cn = [−1, 1]n, the convex hull of Cn. Let

![image 55](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile55.png>)

Bt be a standard Brownian motion on Rn and let Xt be a process satisfying, for all i ∈ [n], d Xt, ei = 1 {| Xt, ei | < 1} d Bt, ei . In other words, Xt is a Brownian motion such that whenever a facet of Cn is hit, the corresponding coordinate stops moving. We will thus have that X∞ has the law µ, the uniform measure on Cn. The idea is to introduce a change of measure on the path space, which reweighs every path of Xt according to the value exp(f(X∞)). In other words, if P was the original measure on Weiner space according to which Bt was a Brownian motion, we consider a new measure Q such that dPdQ ∝ exp(f(X∞)).

![image 56](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile56.png>)

![image 57](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile57.png>)

A-priori, it is not even clear whether under this reweighing, the process Xt is Markovian. However, as it turns out, this reweighing has an alternative interpretation in terms of drift. Namely, it turns out that under the measure Q,

dXt = dB˜t + vtdt

where B˜t is a Brownian motion with respect to Q and vt is an adapted drift (the formula is valid as long as Xt is still in the interior of [−1, 1]n). The drift vt turns out to be entropy-minimizing in the following sense: remark that by deﬁnition, since we reweighed every path according to the value of f at the endpoint, we have that DKL(ν µ) = DKL(Q P). In other words, the relative entropy between the distribution of the whole path of Xt and that of a Brownian motion is equal to the relative entropy between the endpoints, which roughly means that the vt has to minimize the relative entropy at every inﬁnitesimal step. As shown in Lehec [2013], among the drifts vt under which we have X∞ ∼ ν, the drift vt is the one minimizing E 0 ∞ |vt|2dt. An easy consequence of this is that vt has to be a martingale (up to the fact that it becomes zero in coordinates that reach {−1, +1}). Moreover, a calculation gives that

v∞ ≈ ∇f(X∞).

The fact that vt is a martingale tells us that vt = E[v∞|Xt], which means that vt is always approximately inside the convex hull of {∇f(y) : y ∈ Cn}. Thus, our complexity assumption amount to the fact that the drift vt is ”trapped” inside a small set. Another useful consequence of the entropy-minimizing property of vt is that dvt = ΓtdBt for a matrix Γt which dominates the matrix Cov(v∞|Xt) (in a positive-deﬁnite sense). Roughly speaking the latter tells us that if vt is expected to change signiﬁcantly by time ∞, then it must start moving right away (or to put this property in yet simpler words, if vt needs to make a choice at some point, it will try to make this choice asap).

The latter property of vt, which tells us that as long as it has some variance left, it is moving quickly, combined with the property that it needs to be trapped in a set of small Gaussian width tell us that vt must roughly stop moving by a time t which is not too big. This fact, which is at the heart of the proof is the content of Lemma 29 below.

Finally, once the drift vt is roughly deterministic, then the distribution of X∞|Xt becomes close to a product measure (it is easily seen that if vt is deterministic then dXt has independent coordinates). Thus, the relevant decomposition in our theorem 3 will be to the measures deﬁned by the law of X∞|Xt. When the time t is small, the corresponding measures will be nothing but small tilts of the original measure ν.

In Section 2.1 we also demonstrate how one can derive a bound of the spirit of Theorem 1 for the Gaussian case without using the above coupling. This produces a weaker result but may give a better intuition for the way that the low complexity is used.

Acknowledgements. I would like to thank Sourav Chatterjee for the wonderful series of lectures about the topic of nonlinear large deviations which inspired me to work on this topic (the lectures were given at the Texas A&M University Concentration Week on Geometric Functional

Analysis organized by Johnson, Paouris and Rudelson). I’m also thankful to Ramon Van Handel, Amir Dembo, Yair Shenfeld and James Lee for enlightening discussions and suggestions. Finally, I thank the anonymous referee for her extremely useful comments and suggestions which have signiﬁcantly improved the presentation of this paper.

## 2 The Gaussian case

### 2.1 Tilts are close to product measures

The goal of this subsection is to illustrate a general idea of how Gaussian width can produce tilts which are close to Gaussian in transportation distance. The proof in this section is rather straightforward and demonstrates the way in which Gaussian width complexity comes to play: we deﬁne a suitable vector ﬁeld on Rn (which plays the same role of the drift vt deﬁned in Section 1.5) which is restricted to be inside the convex hull of {∇f(x) : x ∈ Rn}. Then, the assumption on the Gaussian width, via an application of the divergence theorem, implies a bound on the divergence of this vector ﬁeld at a point, which in turn implies the existence of a product-like tilt.

Recall that γ denotes the standard Gaussian measure on Rn. Let f : Rn → R be twice

differentiable and ν satisfy dγdν = ef. Now, for all x ∈ Rn, let us consider the measure νx deﬁned by

![image 58](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile58.png>)

dνx(y) =

- exp( x, y )dν(y)

![image 59](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile59.png>)

- exp( x, z )dν(z)


=

- exp(f(y) + x, y )

![image 60](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile60.png>)

- exp(f(z) + x, z )dγ(z)


dγ(y)

When the vector x is small we can think of the measure νx as a ”tilt” of the measure ν towards the direction x. We prove the following,

- Theorem 10. Let ν be a measure on Rn satisfying dν = efdγ for a twice-differentiable function


f, and deﬁne νx as above. Then for every r > 0, there exists a point x0 ∈ Rn with |x0| ≤ r, such that

√n r D(f) − inf

![image 61](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile61.png>)

, γu)2 ≤ 2

∆f(y) where γu is the Gaussian whose centroid is equal to the centroid of νx

W2(νx

![image 62](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile62.png>)

0

y∈Rn

and having identity covariance.

0

Deﬁne also h(x) = exp( x, y − |x|2/2)dν(y) = (2π)−n/2 exp(f(y) + x, y − |y|2/2 − |x|2/2)dy

= exp(f(y + x))dγ(y) Next, we consider the vector ﬁeld

v(x) = ∇ log h(x) = ∇f(x + y) exp(f(y + x) − |y|2/2)dy exp(f(y + x) − |y|2/2)dy

= ∇f(y)dνx(y). (10) A straightforward calculation gives that

![image 63](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile63.png>)

(∇f(x + y)⊗2 + ∇2f(x + y))exp(f(y + x) − |y|2/2)dy exp(f(y + x) − |y|2/2)dy − v(x)⊗2

∇v(x) =

![image 64](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile64.png>)

= ∇f(y)⊗2 + ∇2f(y) dνx(y) − ∇f(y)dνx(y)

⊗2

. (11)

Deﬁne K to be the convex hull of the set {∇f(y) : y ∈ Rn}. By equation (10), it is evident that v(x) ∈ K for all x ∈ Rn.

Now, ﬁx a parameter r > 0 and deﬁne by ωn the n − 1-dimensional Hausdorff measure of Sn−1. By standard estimates concerning the norm of a Gaussian random variable, we have that E[|Γ|] ≥

√n/2 and therefore

![image 65](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile65.png>)

√n 2

![image 66](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile66.png>)

1 rn−1ωn rSn−1

sup

x, θ/r dHn−1(θ)

GW(K) = E sup

x, Γ ≥

![image 67](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile67.png>)

![image 68](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile68.png>)

x∈K

x∈K

where Hn−1 denotes the (n − 1)-dimensional Hausdorff measure. It follows that, in particular

1 ωnrn−1

2 √n

θ/r, v(θ) dHn−1(θ) ≤

GW(K). (12)

![image 69](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile69.png>)

![image 70](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile70.png>)

![image 71](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile71.png>)

rSn−1

On the other hand, by the divergence theorem we have

Tr(∇v(y))dy =

 nθ, v(θ) dHn−1(θ)

rSn−1

|x|≤r

where  nθ denotes the outer unit normal to rSn−1 at θ. Combining the two last inequalities, together with the identity Vol({|x| ≤ r}) = n1rnωn, yields

![image 72](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile72.png>)

√n r

![image 73](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile73.png>)

n rnωn rSn−1

1 Vol({|x| ≤ r}) |x|≤r

Tr(∇v(y))dy =

 nθ, v(θ) dHn−1(θ) ≤ 2

GW(K).

![image 74](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile74.png>)

![image 75](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile75.png>)

![image 76](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile76.png>)

Consequently, there exists a point x0 with |x0| ≤ r such that

√n r

![image 77](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile77.png>)

Tr(∇v(x0)) ≤ 2

GW(K). (13) Using equation (11), we have that

![image 78](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile78.png>)

Tr (∇v(x)) = ∆f(y) + |∇f(y)|2 dνx(y) − |v(x)|2

≥ |∇f(y)|2dνx(y) − |v(x)|2 + inf

y∈Rn

∆f(y). (14)

Deﬁne now a measure γx by dγx = e y,x −|x|2/2dγ(y). Moreover, for a measure ρ consider the Fisher information of ρ with respect to γx, deﬁned as

dρ dγx

(ρ) = ∇ log

Iγx

![image 79](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile79.png>)

2

dρ.

Then we have, by deﬁnition of νx,

2

dνx dγx

dνx = |∇f(y)|2 dνx(y). Combining (13), (14) and the above identity ﬁnally gives

(νx) = ∇ log

Iγx

![image 80](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile80.png>)

√n r

![image 81](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile81.png>)

∆f(y) + |v(x0)|2.

(νx

) ≤ 2

Iγx0

GW(K) − inf

![image 82](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile82.png>)

0

y∈Rn

Recall the transportation-entropy inequality of Talagrand Talagrand [1996], which states that

W2(ρ, γ)2 ≤ 2DKL(ρ γ). for every measure ρ for which the right hand side is deﬁned. Combined with the log-Sobolev inequality 2DKL(ρ γ) ≤ Iγ(ρ), we have that

√n r

![image 83](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile83.png>)

)2 ≤ 2

∆f(y) + |v(x0)|2. (15)

, γx

W2(νx

GW(K) − inf

![image 84](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile84.png>)

0

0

y∈Rn

Finally, remark that by the deﬁnition of h(x) and by integration by parts we have

2/2dy

2/2dy = (2π)−n/2 yef(x+y)e−|y|

∇h(x) = (2π)−n/2 ∇ ef(x+y) e−|y|

2/2 (y − x)ef(y)+ x,y dγ(z) Which implies the identity

= e−|x|

v(x) = (y − x)dνx(y).

Now, since for every pair of random vectors X, Y ∈ Rn one has the parallelogram identity E|X − Y |2 = E|(X − E[X]) − (Y − E[Y ])|2 + |E[X] − E[Y ]|2, we have that

2

, γu)2 = |v(x0)|2 + W2(νx

, γu)2

)2 = ydνx

+ W2(νx

(y) − ydγx

(y)

W2(νx

, γx

0

0

0

0

0

0

where u = ydνx

(y) = x0 + v(x0) is the centroid of νx

. Together with equation (15), we get

0

0

√n r

![image 85](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile85.png>)

, γu)2 ≤ 2

W2(νx

∆f(y).

GW(K) − inf

![image 86](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile86.png>)

0

y∈Rn

This ﬁnishes the proof of Theorem 10.

### 2.2 A reverse log-Sobolev inequality

In this subsection we prove theorem 4. Fix the function f and the measure ν, such that dν = efdγ. Assume that f is twice differentiable. Our proof is based on the following stochastic construction, for which we make similar deﬁnitions as in Eldan and Lee [2014]. Let Bt be a standard Brownian motion in Rn adapted to a ﬁltration Ft. Consider the Ornstein-Uhlenbeck convolution operator

|x − y|2 2t

1 (2πt)n/2 Rn

Pt[g](x) =

g(y) exp −

![image 87](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile87.png>)

![image 88](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile88.png>)

dy = E[g(x + Bt)].

Deﬁne

Z(t, x) = P1−t[ef](x), and for t ∈ (0, 1) and x ∈ Rn consider the measure deﬁned by

1)|Bt = x E[ef(B1)|Bt = x]

1∈A}ef(B

P1−t[ef1A](x) P1−t[ef](x)

E 1{B

=

νt,x(A) =

![image 89](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile89.png>)

![image 90](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile90.png>)

for every measurable A ⊂ Rn. Deﬁne also ν1,x = δx, a Dirac measure supported on x. Remark that ν0,0 = ν. Finally consider the vector ﬁeld

v(t, x) = ∇x log Z(t, x) = ∇P1−t[ef](x) P1−t[ef](x)

![image 91](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile91.png>)

Integration by parts yields that

P1−t[∇fef](x) P1−t[ef](x)

=

= ∇f(y)dνt,x(y).

![image 92](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile92.png>)

|x−y|2

|x−y|2

v(t, x) = ∇f(y)ef(y)−

(y − x)ef(y)−

![image 93](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile93.png>)

![image 94](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile94.png>)

2(1−t)dy ef(y)−

2(1−t)dy ef(y)−

= (1−t)−1

= (1−t)−1 (y−x)dνt,x(y).

![image 95](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile95.png>)

![image 96](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile96.png>)

|x−y|2

|x−y|2

![image 97](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile97.png>)

![image 98](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile98.png>)

2(1−t)dy

2(1−t)dy

We also have,

∇xv(t, x) = ∇2 log Z(t, x) = ∇2Z(t, x) Z(t, x) −

![image 99](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile99.png>)

∇Z(t, x) Z(t, x)

![image 100](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile100.png>)

⊗2

= ∇2P1−t[ef](x) P1−t[ef](x) − v(t, x)⊗2 =

P1−t[(∇2f + ∇f⊗2) ef](x)

P1−t[ef](x) − v(t, x)⊗2 which gives the formula

![image 101](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile101.png>)

![image 102](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile102.png>)

∇xv(t, x) = ∇2f(y) + ∇f(y)⊗2 dνt,x(y) − v(t, x)⊗2 =: Γ(t, x). (16)

Consider now the process Xt which solves the stochastic differential equation

X0 = 0, dXt = dBt + vtdt. where we deﬁne

vt := v(t, Xt). The following facts are proven, for instance, in [Eldan and Lee, 2014, Section 2.2]. The representation formula, equation (17) below was shown in Lehec [2013].

Lemma 11. The processes Xt, vt have the following properties

- (i) The random variable X1 has the law ν, and for any time t one has almost surely that

X1|Ft has the law νt,X

t

.

- (ii) The process vt is a martingale.
- (iii) The relative entropy of ν can be expressed as

E

1

0

|vt|2dt = 2DKL(ν γ). (17)

- (iv) The process vt satisﬁes dvt = Γ(t, Xt)dBt. (18)


An immediate corollary is Fact 12. For all t ∈ [0, 1], we have almost surely vt ∈ Conv(∇f(y) : y ∈ Rn). (19)

Proof. Since vt is a martingale we have vt = E[v1|Ft] = E[∇f(X1)|Ft].

![image 103](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile103.png>)

![image 104](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile104.png>)

![image 105](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile105.png>)

![image 106](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile106.png>)

Deﬁning Γt = Γ(t, Xt), we have by (i) in the above lemma that Γt = E[v1⊗2 + ∇2f(X1)|Ft] − vt⊗2. Set Ht = E[(v1 − vt)⊗2|Ft]. Since vt is a martingale, we have that

Ht = E[v1⊗2|Ft] − vt⊗2. By Itˆo’s isometry and by formula (18), we have that

E vs⊗2 − vt⊗2 = E

t

Γ2rdr , ∀0 ≤ t ≤ s ≤ 1.

s

Since Γ2r is positive semi-deﬁnite, a combination of the two last displays gives

ETr(Ht) ≤ ETr(Hs) for all 0 ≤ s ≤ t ≤ 1. We get that

ETr(Ht) − M ≤ ETr(Γs), ∀0 < s < t < 1 (20) where we deﬁne

∆f(x). The following lemma is the central place where the Gaussian-width functional plays a role. Lemma 13. Deﬁne K = Conv({∇f(y) : y ∈ Rn}). For every t ∈ (0, 1) we have

M := − inf

x∈Rn

GW(K) √t

E[Tr(Ht)] ≤

+ M.

![image 107](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile107.png>)

![image 108](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile108.png>)

Proof. We have by Itˆo’s isometry and by (18) that, for all t ∈ (0, 1),

t

(20)

≥ t(ETr(Ht) − M) .

E[ Bt, vt ] = E

Tr(Γs)ds

0

On the other hand, since almost surely vt ∈ K by Fact 12, we have

Bt √t

Bt √t

, x = GW(K).

, vt ≤ E sup

E

![image 109](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile109.png>)

![image 110](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile110.png>)

![image 111](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile111.png>)

![image 112](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile112.png>)

x∈K

Combining the two above inequalities, we get

which completes the proof.

GW(K) √t

+ M

E[Tr(Ht)] ≤

![image 113](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile113.png>)

![image 114](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile114.png>)

![image 115](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile115.png>)

![image 116](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile116.png>)

![image 117](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile117.png>)

![image 118](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile118.png>)

We are ﬁnally ready to prove the reverse log-Sobolev inequality.

Proof of Theorem 4. Fix a time t ∈ (0, 1). Since vt is a martingale, we have that E|vt|2 ≤ E|vs|2 for all t ≤ s, which gives

1

1

2DKL(ν γ) (=17) E

|vs|2ds ≥ E

|vs|2ds ≥ (1 − t)E|vt|2. On the other hand, by Lemma 11 we also have

0

t

I(ν) = E|∇f(X1)|2 = E|v1|2 = E Tr(Ht) + |vt|2 and using Lemma 13 we have

GW(K) √t

I(ν) ≤ E|vt|2 +

+ M.

![image 119](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile119.png>)

![image 120](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile120.png>)

Combining the above inequalities, we have

GW(K) √t

GW(K) √t

I(ν) − 2DKL(ν γ) ≤ tE|vt|2 +

+ M ≤ tI(ν) +

+ M

![image 121](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile121.png>)

![image 122](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile122.png>)

![image 123](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile123.png>)

![image 124](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile124.png>)

Now, if GW(K) ≤ I(ν) then taking t = GWI(ν()K)

![image 125](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile125.png>)

2/3

gives

I(ν) − 2DKL(ν Γ) ≤ 2GW(K)2/3I(ν)1/3 + M

Otherwise if GW(K) > I(ν), we trivially have that I(ν)−2DKL(ν Γ) ≤ 2GW(K)2/3I(ν)1/3. The proof is complete.

![image 126](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile126.png>)

![image 127](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile127.png>)

![image 128](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile128.png>)

![image 129](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile129.png>)

## 3 The discrete case

Our main goal in this section is to prove Theorem 3. We then show that Theorem 1 follows easily. A crucial element of our approach is to consider harmonic extensions of the function f and related functions into the continuous cube, which we do in subsection 3.1. The core idea of the proof is based on a stochastic construction deﬁned in subsection 3.4.1.

### 3.1 Some preliminary deﬁnitions

- 3.1.1 Harmonic extensions


We deﬁne Cn = [−1, 1]n, the convex hull of Cn. In the following, we will use the notation ∇ to denote both a discrete and a continuous gradient, depending on the domain of the function. From here on, for the sake of brevity, the notation y will usually be used for points in Cn while x will be used for points in Cn. Denote by e1, . . ., en the vectors of the standard basis on Rn.

![image 130](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile130.png>)

![image 131](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile131.png>)

For x ∈ [−1, 1] and y ∈ {−1, 1}, deﬁne

- 1 + xy

![image 132](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile132.png>)

- 2


w(x, y) =

so that for all x ∈ [−1, 1], w(x, ·) is a probability density on {−1, 1} of a measure whose expectation is x. By slight abuse of notation, for x ∈ Cn and y ∈ Cn, we write

![image 133](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile133.png>)

w(x, y) =

i

w(xi, yi).

For a function ξ˜: Cn → R, the harmonic extension to Cn is the function deﬁned by the equation ξ(x) =

![image 134](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile134.png>)

w(x, y)ξ˜(y).

y∈Cn

This is the unique function satisfying the following three conditions: (i) it is harmonic in the interior of Cn, (ii) for each k-facet of Cn, it is harmonic inside the relative interior of this facet with respect to the k-Laplacian associated with the corresponding afﬁne subspace and (iii) it coincides with f on Cn.

![image 135](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile135.png>)

![image 136](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile136.png>)

We have the following easy fact.

- Fact 14. If ξ(x) is the harmonic extension of ξ˜ : Cn → R to Cn then ∂iξ is the harmonic extension of ∂iξ˜, or in other words

![image 137](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile137.png>)

∇ξ(x) =

y∈Cn

w(x, y)∇ξ˜(y), ∀x ∈ Cn. (21)

![image 138](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile138.png>)

Proof. Suppose ﬁrst that ξ˜(y) = 1{y=ǫ} for some ǫ ∈ Cn. Then ξ(x) = 2−n

j(1+ǫjxj), which implies that ∂iξ(x) = 2−nǫi j =i(1 + ǫjxj). On the other hand ∂iξ˜(y) = 21ǫi1{y

![image 139](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile139.png>)

−i=ǫ−i}, where the notation v−i stands for the vector v with the i-th coordinate omitted. It is now straightforward to check that ∂iξ(x) is indeed the harmonic extension of ∂iξ˜. The proof is concluded due to the linearity of both sides of (21) with respect to ξ˜.

![image 140](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile140.png>)

![image 141](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile141.png>)

![image 142](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile142.png>)

![image 143](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile143.png>)

As a consequence, we have the following simple but useful result.

- Fact 15. Let ξ˜: Cn → R and let ξ be the harmonic extension of ξ˜to Cn. Then for any diagonal matrix A and for all x ∈ Cn, one has that Tr(A∇2ξ(x)) = 0. Consequently, if Yt is a martingale taking values in Cn such that dYt = σtdBt, where Bt is a Brownian motion and σt is almost surely diagonal for all t, then the process ξ(Yt) is also a martingale.


![image 144](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile144.png>)

![image 145](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile145.png>)

![image 146](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile146.png>)

Proof. Use Fact 14 to conclude that ∇2ξ has zeroes on its diagonal. It follows from Itˆo’s formula that ξ(Yt) is a local martingale. Since ξ(·) is bounded, we conclude that ξ(Yt) is a martingale.

![image 147](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile147.png>)

![image 148](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile148.png>)

![image 149](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile149.png>)

![image 150](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile150.png>)

3.1.2 Some core constructions

Let ν be a probability measure on Cn. Deﬁne fν(y) = log dµdν(y) for all y ∈ Cn. In the following, we abbreviate f = fν whenever there is no ambiguity. For a point y ∈ Cn deﬁne

![image 151](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile151.png>)

v(y) = vν(y) = ∇ef(y) ef(y)

(22)

![image 152](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile152.png>)

(using the deﬁnition of the discrete gradient ∇) with the convention vν(y) = 0 when dµdν(y) = 0. Note that the identity ∇e

![image 153](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile153.png>)

f(y)

ef(y) = ∇f(y) is not true in the discrete setting, but the reader can assume that it is approximately correct for the sake of intuition. The purpose of some of our deﬁnitions below is to overcome this caveat, see Remark 7 below.

![image 154](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile154.png>)

Let hν(x) be the harmonic extension of the function ef to Cn or in other words, h(x) = hν(x) =

![image 155](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile155.png>)

w(x, y)ef(y).

y∈Cn

![image 156](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile156.png>)

We extend the function vν from Cn to Cn by deﬁning

vν(x) = ∇h(x) h(x)

![image 157](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile157.png>)

, ∀x ∈ Cn (23)

![image 158](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile158.png>)

with the convention vν(x) = 0 when h(x) = 0. Remark that vν(x) is not harmonic in general, however Fact 14 implies that the latter deﬁnition is in accordance with equation (22) in the sense that the two deﬁnitions coincide on Cn.

For x ∈ [−1, 1] and g ∈ (−1, 1), consider the function

g 1 + gx and its inverse

ζx(g) =

![image 159](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile159.png>)

v 1 − vx

ζx−1(v) =

. With slight abuse of notation, for g = (g1, ..., gn) ∈ Cn and x = (x1, ..., xn) ∈ Cn we deﬁne ζx(g) = (ζx

![image 160](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile160.png>)

![image 161](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile161.png>)

![image 162](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile162.png>)

(gn)) and deﬁne ζ−1

(g1), . . ., ζx

n

1

x likewise. The point of this deﬁnition will be clariﬁed later, but a useful way to understand ζ is the fact that if v = ζx(g) then

b − a (1 + x)b + (1 − x)a

b − a b + a ⇔ v =

. (24)

g =

![image 163](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile163.png>)

![image 164](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile164.png>)

Both quantities above should be thought of as discrete interpretations the quantity ∇ log ξ for a function ξ : {−1, 1} → (0, ∞) satisfying ξ(1) = b, ξ(−1) = a.

Finally, we will deﬁne the function

gν(y) = ζy−1(vν(y)), ∀y ∈ Cn (25) In other words for i ∈ [n], y ∈ Cn if we denote y+, y− to be the points satisfying y+, ej =

y−, ej = y, ej for all j = i and y±, ei = ±1, then

ef(y

+) − ef(y

−)

y+ + y− 2

gν(y), ei =

, ei . (26)

ef(y+) + ef(y−) = vν

![image 165](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile165.png>)

![image 166](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile166.png>)

- Remark 7. Both the quantities gν(y) and vν(y) should be thought of as approximations of ∇f(y). We will need to distinguish between those approximations because the chain rule ∇ef = ∇fef does not hold true in the discrete setting. Note also that


gν(y) = tanh(∇fν(y)). (27) Next, remark that

gν(y)dν(y) = ydν(y) (28) which is a consequence of the calculation

gν(y)dν(y), ei =

∂ief(y) =

ef(y) gν(y), ei = 2

y∈Cn

y∈Cn

yief(y).

y∈Cn

A central deﬁnition in our proofs will be the matrix

H(ν) :=

gν(y)⊗2dν(y) −

Cn

gν(y)dν(y)

Cn

the covariance matrix of the random vector gν(X) for X ∼ ν.

⊗2

,

The following lemma is a straightforward application of the Sudakov-Fernique inequality: Lemma 16. We have, in the above notation,

GW ({gν(y) : y ∈ Cn}) ≤ D(fν) = D(ν). (29) The proof is postponed to the appendix.

Finally, for the sake of intuition, let us calculate the ﬁeld vν(x) for the case that ν is a tilt of the uniform measure, ν = τθ(µ). In this case, we have

h(x) = Cθ

n

w(x, y) exp( θ, y ) = Cθ

i=1

y∈Cn

where Cθ is a normalization constant. Therefore

1 + xiyi 2

eθ

i

![image 167](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile167.png>)

1 − xiyi 2

e−θ

+

i

![image 168](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile168.png>)

n

1 + xiyi 2

eθ

vν(x) = ∇ log h(x) =

∇ log

i

![image 169](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile169.png>)

i=1

n

eθ

− e−θ

i

i

(1 + xi)eθi + (1 − xi)e−θi ei.

=

![image 170](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile170.png>)

i=1

1 − xiyi 2

e−θ

+

i

![image 171](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile171.png>)

Remark that gν(y) = vν(0) = tanh(θ) for all y ∈ Cn, therefore in this case we have H(ν) = 0. We will later see that this is robust in the sense that whenever the matrix H(ν) is small, the measure ν is close to a product measure.

### 3.2 Two main steps towards the proof

The proof of Theorem 3 consists of two main intermediate results, which are formulated in this section. The ﬁrst step roughly tells us that in order to ﬁnd a product measure close to ν in the W1 metric, it is enough to control the quantity Tr (H(ν)).

- Proposition 17. Let ν˜ be a probability measure on Cn. Then there exists a product measure ξ = ξ(˜ν) such that


![image 172](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile172.png>)

W1(˜ν, ξ) ≤ nTr (H(˜ν)). Moreover, one may take ξ to be the unique product measure whose center of mass lies at the point C

gν˜(y)dν˜(y) which is equal to the center of mass of of ν˜.

n

The second step, which is the more difﬁcult one, is the following proposition which tells us that we can ﬁnd a decomposition of ν via small tilts in a way that controls the matrix H(τθν). For a matrix A whose decreasing rearrangement of diagonal entries is denoted by (αi)1≤i≤n, we denote Trk(A) := ni=⌈k⌉ αi.

- Proposition 18. Deﬁne D = GW ({gν(y) : y ∈ Cn}). Let ν be a probability measure on


Cn and deﬁne f = log dµdν. For all ε ∈ (0, 1/16), there exists a measure m supported on B(0, ε√n) ∩ [−1, 1]n, such that ν admits the decomposition

![image 173](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile173.png>)

![image 174](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile174.png>)

ϕdτθ(ν) dm(θ) (30) for every test function ϕ : Cn → R and which satisﬁes

ϕdν =

B(0,ε√n) Cn

![image 175](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile175.png>)

Cn

28αD ε ≥ 1 −

1 α −

1 n

m θ : Trk(H(τθν)) ≤

, ∀α > 1, (31)

![image 176](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile176.png>)

![image 177](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile177.png>)

![image 178](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile178.png>)

where k ≤ 2ne−1/(32ε2). Furthermore, under the additional assumption ε ≤ 1

√

, the above equation holds true with k = 1.

![image 179](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile179.png>)

![image 180](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile180.png>)

log 4Dn

8

![image 181](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile181.png>)

We will also need the following easy lemma. Lemma 19. For every θ ∈ B(0, ε√n) and for all y ∈ Cn one has log

![image 182](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile182.png>)

dτθν dν

(y) ≤ 2εn. (32) Proof. We have by deﬁnition

![image 183](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile183.png>)

dτθν dν

log

= y, θ − log exp( z, θ )dν(x).

![image 184](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile184.png>)

Now, since θ ∈ B(0, ε√n) we have for all y ∈ Cn that | y, θ | ≤ εn. Consequently we also have log e θ,y dν ≤ εn. The lemma follows.

![image 185](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile185.png>)

![image 186](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile186.png>)

![image 187](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile187.png>)

![image 188](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile188.png>)

![image 189](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile189.png>)

Given the above, the proofs of Theorem 3 and Theorem 1 follow easily.

Proof of Theorem 3. Given the measure ν, apply Proposition 18 with the parameters α, ε to ﬁnd a measure m on B(0, ε√n) ∩ [−1, 1]n such that the decomposition (30) holds. Deﬁne Θ to be the set of θ ∈ Rn such that the event in equation (31) is satisﬁed with k = 1. Then for each θ ∈ Θ, using Proposition 17 with ν˜ = τθν, one concludes that

![image 190](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile190.png>)

![image 191](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile191.png>)

W1(τθν, ξ(τθν)) ≤ nTr (H(τθν)) ≤

![image 192](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile192.png>)

28αnGW({gν(y) : y ∈ Cn}) ε

![image 193](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile193.png>)

![image 194](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile194.png>)

28αnD(ν) ε

(29)

≤

![image 195](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile195.png>)

where, in the second inequality we applied Lemma 16. Finally, by Lemma 19, we have

DKL(τθν µ)dm(θ) − DKL(ν µ) =

Rn

−

(=30)

Cn

(32)

≤ 2

Rn Cn

dν dµ

log

![image 196](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile196.png>)

Rn Cn

dτθν dν

log

(y) + log

![image 197](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile197.png>)

dν dµ

(y) dτθν(y)dm(θ)

![image 198](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile198.png>)

(y)dν(y)

dτθν dν

log

(y)dτθν(y)dm(θ)

![image 199](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile199.png>)

εndτθν(y)dm(θ) ≤ 2εn.

Rn Cn

![image 200](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile200.png>)

![image 201](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile201.png>)

![image 202](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile202.png>)

![image 203](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile203.png>)

Proof of Theorem 1. Given the measure ν, apply Proposition 18 with the measure ν the parameter ε and with the choice α = 3. A consequence of formula (31) is the existence of θ ∈ B(0, ε√n) and of a diagonal projection matrix σ of rank n−k, with k ≤ 2ne−1/(32ε2), such that

![image 204](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile204.png>)

28αD(ν) ε

. Deﬁne ν˜ = τθν and f˜= log dτ

Tr(σH(τθν)) ≤

![image 205](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile205.png>)

θν

dµ so that

![image 206](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile206.png>)

f˜(y) = f(y) + θ, y  − log e θ,y dν.

Now, since θ ∈ B(0, ε√n) we have for all y ∈ Cn that | y, θ | ≤ εn. Consequently we also have log e θ,y dν ≤ εn. We therefore get |f − f˜| ≤ 2εn.

![image 207](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile207.png>)

Deﬁne b = ydν˜(y), the center of mass of ν˜. Let ξ be the unique product measure whose center of mass is at b. Since, by deﬁnition, we have | gν(y), ei | ≤ 1 for all y ∈ Cn and for all i ∈ [n], it follows that ei, H(˜ν)ei ≤ 1. According to Proposition 17, we therefore have

![image 208](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile208.png>)

![image 209](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile209.png>)

W1(˜ν, ξ) ≤ nTr(H(˜ν)) ≤ n(k + Tr(σH(˜ν))) which completes the ﬁrst part of the theorem.

Roughly speaking, the second part of the theorem follows by considering the foliation with respect to σ and invoking Proposition 17 on each sub-cube separately. By rearranging the coordinates, we may assume without loss of generality that the diagonal entries of the matrix σ are increasing. For each y ∈ Ck, consider the sub-cube Ay = {x ∈ Cn; xi = yi, 1 ≤ i ≤ k} and let ν˜y, ξy be the restrictions of the measures ν˜ and ξ to Ay, respectively, normalized to be probability measures. Let b(y) be the center of mass of ν˜y and recall that b is the center of mass of ν˜. Remark that for all i > k, for all y ∈ Ck and for all x ∈ Ay, one has that

(x), ei . Using formula (28), we therefore get

gν˜(x), ei = gν˜

y

b(y), ei = gν˜(x)dν˜y(x), ei .

Consequently, by the law of total variance, we have for all i > k,

VarX∼ν˜ [ gν˜(X), ei ] =

ν˜(Ay) VarY∼ν˜

y

y∈Ck

[ gν˜(Y ), ei ] + b(y) − b, ei 2 .

which gives, by deﬁnition of the matrix H(·), Tr (σH(˜ν)) =

ν˜(Ay) Tr (H(˜νy)) + |σ(b(y) − b)|2 . (33)

y∈Ck

For each y ∈ Ck, we invoke Proposition 17 on ν˜y to conclude that the product measure ξ˜y, whose center of mass lies at b(y), satisﬁes

![image 210](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile210.png>)

W1(ξ˜y, ν˜y) ≤ nTr (H(˜νy)). (34)

Deﬁne ξ′ := πI(ξ) × π[n]\I(˜ν) where I = {i; σi,i = 1}. Since for all y ∈ Ck one has ξ′(Ay) = ν˜(Ay), we have

W1(ξ′, ν˜) ≤

≤

(34)

≤

≤

ν˜(Ay)W1(ξy, ν˜y)

y∈Ck

ν˜(Ay) W1(ξy, ξ˜y) + W1(ξ˜y, ν˜y)

y∈Ck

![image 211](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile211.png>)

ν˜(Ay) σ(b − b(y)) 1 + nTr (H(˜νy))

y∈Ck

√n

![image 212](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile212.png>)

![image 213](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile213.png>)

ν˜(Ay) |σ(b − b(y))| + Tr (H(˜νy))

y∈Ck

![image 214](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile214.png>)

ν˜(Ay) (|σ(b − b(y))|2 + Tr (H(˜νy)))

≤ 2n

y∈Ck

![image 215](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile215.png>)

(=33) 2nTr(σH(˜ν)) ≤ 26 nD(ν) ε

![image 216](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile216.png>)

,

![image 217](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile217.png>)

which is the desired bound.

![image 218](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile218.png>)

![image 219](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile219.png>)

![image 220](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile220.png>)

![image 221](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile221.png>)

### 3.3 The ﬁrst step: obtaining an estimate on W1 using H

The proof of the ﬁrst step is rather straightforward. We choose to prove it directly, but in fact it follows from a combination of two well-known inequalities: the Log-Sobolev inequality and the transportation-entropy inequality. The sketch of this direction goes as follows: let ξ be the product measure having the same expectation as ν. Then, a straightforward calculation gives that TrH(ν) ≈ Iξ(ν) where Iξ(ν) is the Fisher information of ν with respect to ξ. A combination of the two above inequalities then gives W1(ν, ξ)2 ≤ 2nDKL(ν ξ) ≤ nIξ(ν) up to constants.

We now give a direct proof of the proposition.

Proof of Proposition 17. Let U1, . . ., Un be independent random variables uniformly distributed in [−1, 1]. Deﬁne g = (g1, . . ., gn) = gν(y)dν(y) for all i ∈ [n] (where gν is deﬁned in equation (25) above). Let Y = (Y 1, . . ., Y n) be a random point in Cn deﬁned by

![image 222](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile222.png>)

![image 223](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile223.png>)

![image 224](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile224.png>)

Y i =

+1 Ui ≤ gi −1 Ui > gi.

![image 225](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile225.png>)

![image 226](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile226.png>)

We deﬁne ξ to be the law of Y . Clearly, ξ is a product measure. Let us now deﬁne a suitable coupling of Y with a random variable Z = (Z1, . . ., Zn) whose law is ν. Consider the ﬁltration F˜i = σ(U1, . . ., Ui−1). Set also

J(j) := {(y1, . . ., yn) ∈ Cn| yk = Zk, ∀1 ≤ k ≤ j − 1}. Deﬁne a vector Λ(j) = (Λ1(j), . . ., Λn(j)) by the formula

ef(y)g(y) y∈J(j) ef(y)

Λ(j) = y∈J(j)

![image 227](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile227.png>)

where we abbreviate g(y) = gν(y). Finally, we can deﬁne inductively

Zi =

+1 Ui ≤ Λi(i) −1 Ui > Λi(i).

Remark that Λ(j) is F˜j measurable. Let us now show that Z ∼ ν. Deﬁne Z(i) = (Z1, . . ., Zi, 0, . . ., 0). First note that whenever i ≥ j, one has

g(y) ef(y) + ef(y+2e

i)

y∈J(j), yi=−1

Λi(j) =

![image 228](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile228.png>)

y∈J(j) ef(y)

∂ief(y) y∈J(j) ef(y)

y∈J(j), yi=−1

(=26) 2

![image 229](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile229.png>)

∂ief(y) y∈J(j) ef(y)

∂ih(Z(j − 1)) h(Z(j − 1))

= y∈J(j)

(=21)

.

![image 230](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile230.png>)

![image 231](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile231.png>)

The last equation and the deﬁnition of Zi teach us that

So,

1 + s∂

ih(Z(i−1)) h(Z(i−1))

![image 232](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile232.png>)

P(Zi = s|Z(i − 1)) =

![image 233](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile233.png>)

2

h(Z1, . . ., Zi−1, s, 0, . . ., 0) h(Z(i − 1))

=

, s = ±1.

![image 234](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile234.png>)

P(Z = (z1, ..., zn)) =

P Zi = zi Z(i − 1) = z(i − 1) =

i∈[n]

h(z(i)) h(z(i − 1))

= h(z) = ef(z)

![image 235](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile235.png>)

i∈[n]

where we have deﬁned z(i) = (z1, . . ., zi, 0, . . ., 0). This establishes the fact that Z ∼ ν. Moreover, by the last formula it is easily seen that that Z|F˜i has the law e

f(·)1·∈J(i)

y∈J(i)ef(y). Consequently, we have

![image 236](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile236.png>)

Λ(j) = E[g(Z)|F˜j] = E[Λ(n)|F˜j], ∀j ∈ [n] so that Λ(j) is a martingale. By deﬁnition of Λ and H(ν) one may verify that

Cov(Λ(n)) = Cov(g(Z)) = H(ν). The fact that Λ(j) is a martingale implies that

Var[Λi(i)] ≤ Var[Λi(n)] = ei, H(ν)ei and, moreover, we have for all i,

E[Λ(i)] = E[Λ(n)] = E[g(Z)] = g. The last two equalities and the deﬁnition of Zi and Y i give us that E[Zi] = E[Y i] and that P(Zi = Y i) = E P(Ui ≥ gi) − P(Ui ≥ Λi(i)|F˜i)

![image 237](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile237.png>)

![image 238](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile238.png>)

- 1

![image 239](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile239.png>)

- 2


E |gi − Λi(i)| ≤ Var[Λi(i)] ≤ ei, H(ν)ei .

=

![image 240](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile240.png>)

![image 241](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile241.png>)

![image 242](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile242.png>)

Consequently,

W1(ξ, ν) ≤ E

n

1{Yi =Zi} ≤

i=1

i∈[n]

![image 243](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile243.png>)

![image 244](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile244.png>)

ei, H(ν)ei ≤ nTr(H).

Finally note that by deﬁnition, the center of mass of ξ lies at the point g which is by the identity

![image 245](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile245.png>)

(28) equal to the center of mass of ν. The proof is complete.

![image 246](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile246.png>)

![image 247](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile247.png>)

![image 248](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile248.png>)

![image 249](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile249.png>)

- 3.4 The second step: ﬁnding product-like tilts The proof of Proposition 18 is based on several stochastic constructions, introduced henceforth.


- 3.4.1 Stochastic constructions


Let a probability measure ν on Cn be ﬁxed and deﬁne the functions v(x) = vν(x), h(x) = hν(x) and g(y) = gν(y) as in Section 3.1. Let σ : [−1, 1] × [0, ∞) → R be the function

σ(x, t) =   

0 ≤ t < 1 1x∈(−1,1) t ≥ 1.

1x∈ −1

- 1

![image 250](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile250.png>)

- 2


,

![image 251](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile251.png>)

2

![image 252](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile252.png>)

By slight abuse of notation, for x = (x1, . . ., xn) ∈ Cn deﬁne

  .

  

σ(x1, t) 0 0 · · · 0 σ(x2, t) 0 · · · 0 0 σ(x3, t) · · ·

σ(x, t) =

· · ·

Let Bt be a standard Brownian motion in Rn adapted to a ﬁltration Ft. Our central construction is the following: let Xt be the solution of the stochastic differential equation

X0 = 0, dXt = σ(Xt, t)1/2dBt + σ(Xt, t)v(Xt)dt (35) where v(Xt) = vν(Xt) is deﬁned in equation (23).

- Remark 8. The function σ(x, t) is deﬁned in a way that Xt ∈ [−1/2, 1/2]n for t ≤ 1, Xt ∈ Cn for all t and limt→∞ Xt ∈ Cn. The particular choice of function is not important as long as one gets this sort of behavior, and in fact, as long as ε is smaller than the order 1/ logn, it will be enough to deﬁne σ(x, t) = 1x<1 instead.


![image 253](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile253.png>)

Deﬁne also

Mt = log h(Xt) and

σt = σ(Xt, t), vt = v(Xt). We have, by a simple calculation using Itˆo’s formula and by Fact 15,

dh(Xt) = ∇h(Xt), σt1/2dBt + σtvtdt and

- 1

![image 254](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile254.png>)

- 2|σt1/2vt|2dt. (36)


dMt = σt1/2vt, dBt +

Finally, we deﬁne

g(y)w(x, y)ef(y), ∀x ∈ Cn

![image 255](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile255.png>)

q(x) =

y∈Cn

the harmonic extension of g(x)ef(x) to Cn. Consider the process

![image 256](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile256.png>)

q(Xt) h(Xt)

gt :=

. (37)

![image 257](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile257.png>)

Deﬁne X∞ = limt→∞ Xt. By the martingale convergence theorem and by the fact that σ(x) = 1 for x ∈ (−1, 1), t > 1 and σ(±1) = 0, we have that almost surely X∞ ∈ Cn. The following fact is a direct consequence of Girsanov’s formula.

t,y)ef(y) h(Xt) . In other words, for every test function ϕ : Cn → R, one has

Fact 20. For any t > 0, the random variable X∞ conditioned on Ft has the law y → w(X

![image 258](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile258.png>)

1 h(Xt) y∈C

ϕ(y)w(Xt, y)ef(y). (38)

E[ϕ(X∞)|Ft] =

![image 259](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile259.png>)

n

Proof. Fix t > 0. Suppose that {Bs}t≥s is a Brownian motion when the underlying Wiener space is equipped with a measure P. Let Q be a measure, deﬁned on the same underlying Wiener space, by

dQ dP

= exp −

![image 260](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile260.png>)

∞

t

- 1

![image 261](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile261.png>)

- 2


σs1/2vs, dBs +

σs1/2vs 2 dt .

Then, by Girsanov’s formula we have that the process s → Bt+s − Bt + t t+s σr1/2vrdr is a Brownian motion under the measure Q and according to formula (35), the process {Xs}s≥t is a martingale under that measure, whose diffusion matrix is diagonal. Consequently we have that the distribution of X∞|Ft under Q has the density w(Xt, ·), since the latter represents the harmonic measure on Cn with respect to any diagonal martingale started at Xt. Using equation (36), we have that

dP dQ

= exp

![image 262](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile262.png>)

∞

h(X∞) h(Xt)

dMt = eM

∞−Mt =

![image 263](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile263.png>)

t

ef(X

∞)

=

.

![image 264](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile264.png>)

h(Xt)

Thus, we have under the measure P that

dP dQ

EP[ϕ(X∞)|Ft] = EQ

ϕ(X∞) Ft

![image 265](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile265.png>)

ef(X∞) h(Xt)

ϕ(X∞) Ft

= EQ

![image 266](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile266.png>)

1 h(Xt) y∈C

ef(y)w(Xt, y)ϕ(y).

=

![image 267](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile267.png>)

n

The proof is complete.

![image 268](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile268.png>)

![image 269](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile269.png>)

![image 270](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile270.png>)

![image 271](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile271.png>)

- Remark 9. A different way to see that the above identity is correct without using Girsanov’s


f(y)w(Xt,y)

inequality is simply to calculate the Itˆo differential of the process pt := e

h(Xt) and observe that it is a martingale. Therefore, one has P(X∞ = y|Ft) = E[p∞|Ft] = pt.

![image 272](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile272.png>)

Deﬁne a mapping η : Int(Cn) → Rn by

![image 273](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile273.png>)

η(x), ei = log

![image 274](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile274.png>)

1 + x, ei 1 − x, ei

.

![image 275](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile275.png>)

We have by deﬁnition, for every x ∈ Cn and y ∈ Cn, exp( η(x), y ) = i∈[n] 1+x

√ iyi

![image 276](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile276.png>)

= Cxw(x, y) with Cx depending only on x. Therefore

![image 277](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile277.png>)

![image 278](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile278.png>)

(1+xi)(1−xi)

ϕd(τη(X

t)ν) =

Cn

1 h(x) y∈C

![image 279](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile279.png>)

n

ϕ(y)w(Xt, y)ef(y) (=38) E[ϕ(X∞)|Ft]. (39)

The following two corollaries follow immediately from equation (38).

- Corollary 21. For every stopping time τ such that Xτ ∈ Int(Cn) almost surely, one has the following decomposition of the measure ν: for every test function ϕ : Cn → R,

![image 280](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile280.png>)

Cn

ϕdν = E

Cn

ϕd(τη(X

τ)ν) . (40)

Proof. Since E[ϕ(X∞)|Ft] is a martingale, we have by the optional stopping theorem

Cn

ϕdν = E[ϕ(X∞)] = E E[ϕ(X∞)|Fτ] (=39) E

Cn

ϕd(τη(X

τ)ν).

![image 281](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile281.png>)

![image 282](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile282.png>)

![image 283](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile283.png>)

![image 284](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile284.png>)

- Corollary 22. One has the identities vt = E[v(X∞)| Ft], and gt = E[g(X∞)| Ft].


In particular, the processes vt and gt are martingales. Proof. Observe that, by deﬁnition,

1 h(Xt) y∈C

gt =

![image 285](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile285.png>)

n

g(y)w(Xt, y)ef(y)

and

vt = ∇h(Xt) h(Xt)

1 h(Xt) y∈C

(=21)

v(y)w(Xt, y)ef(y).

![image 286](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile286.png>)

![image 287](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile287.png>)

n

Apply equation (38) with the choices ϕ(y) = v(y) and ϕ(y) = g(y).

![image 288](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile288.png>)

![image 289](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile289.png>)

![image 290](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile290.png>)

![image 291](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile291.png>)

The following calculation is central to our proof. It is the consequence of a straightforward calculation using Itˆo’s formula, and its proof is postponed to the appendix. Fact 23. One has,

dgt = Γtσt1/2dBt (41) where

Γt := ∇q(Xt) h(Xt) − gt ⊗ vt. (42)

![image 292](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile292.png>)

Our ﬁnal deﬁnition is that of the matrix-valued stochastic process

Ht := E[(g∞ − gt)⊗2|Ft]. (43) According to formula (38) and since gt is a martingale, we have that also

Recalling that

1 h(Xt) y∈C

Ht =

![image 293](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile293.png>)

n

ef(y)w(Xt, y)g(y)⊗2 − gt ⊗ gt

(=39)

gν(y)⊗2dτη(X

t)ν(y) −

Cn

gν(y)dτη(X

t)ν(y)

Cn

⊗2

.

H τη(X

t)ν =

η(Xt)ν(y)⊗2dτη(X

gτ

t)ν(y) −

Cn

gτ

η(Xt)ν(y)dτη(X

t)ν(y)

Cn

⊗2

,

we immediately see that H0 = H(ν). Furthermore, while the matrices H(τη(X

t)(ν)) and Ht are not exactly equal, they are close to each other when the coordinates of Xt are small, as shown in the next technical lemma, whose proof appears in the appendix.

Lemma 24. Let θ ∈ Rn and let ν, ν˜ be probability measures on Cn. Deﬁne

⊗2

gν(y)⊗2dν˜(y) −

gν(y)dν˜(y)

A =

Cn

Cn

and

⊗2

θν(y)⊗2dν˜(y) −

gτ

θν(y)dν˜(y)

gτ

. Then for all 1 ≤ i ≤ n,

B =

Cn

Cn

e−4 θ

Bi,i ≤ Ai,i ≤ e4 θ

Bi,i.

∞

∞

An immediate consequence of this lemma is that under the event Xt ∈ [−1/2, 1/2]n, we have exp(2| η(Xt), ei |) = 1+| X

t,ei |

1−| Xt,ei | ≤ 3 and therefore Xt ∈ [−1/2, 1/2]n ⇒ Tr(σH(τη(X

![image 294](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile294.png>)

t)ν)) ≤ 9Tr (σHt) (44) for every positive-deﬁnite diagonal matrix σ.

t)(ν)). In view of the above equation it therefore sufﬁces to control the trace of Ht. A key fact in the proof of Proposition 18, which we will see later on, is that the matrix Ht is, in a sense, controlled by the matrix Γt. Intuitively, this means that the martingale gt has to be moving quickly whenever Cov(g∞) is big.

Recall that our ﬁnal objective is to control TrH(τη(X

3.4.2 Proof of Proposition 18 The following simple observation will help us exploit the complexity condition. Observation 25. For every t ≥ 0 we have, almost surely, gt ∈ Conv({g(y) : y ∈ Cn}).

Proof. Since gt is a martingale, and since almost surely there exists some y ∈ Cn such that g∞ = g(y), it follows that gt can be written as

g(y)P(X∞ = y|Ft)

gt =

y∈Cn

which is a convex combination of vectors in the set {g(y), y ∈ Cn}.

![image 295](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile295.png>)

![image 296](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile296.png>)

![image 297](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile297.png>)

![image 298](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile298.png>)

Next, we will need the following lemma which will help us make sense of the matrix Γt deﬁned in (42). Lemma 26. One has almost surely, for all t ≥ 0 and all i ∈ [n],

(E[g∞ ⊗ v∞|Ft])i,i = ∇q(Xt) h(Xt) i,i

.

![image 299](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile299.png>)

Proof. Fix i ∈ [n]. For all y ∈ Cn deﬁne y+ to be the point equal to y on every coordinate except maybe the ith coordinate, where it is equal to +1. Deﬁne y− analogously. We have for all y ∈ Cn,

ef(y

+) − ef(y

−)

qi(y) (=26) ef(y)

![image 300](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile300.png>)

ef(y+) + ef(y−) and thus

−) 2

ef(y

+) − ef(y

1 2

∂iqi(y) =

ef(y+) + ef(y−) . On the other hand, with the help of equation (26) we have

![image 301](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile301.png>)

![image 302](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile302.png>)

ef(y

+) − ef(y

−)

ef(y

+) − ef(y

−)

g(y)iv(y)i =

. Consequently, we have that for all y ∈ Cn,

![image 303](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile303.png>)

![image 304](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile304.png>)

ef(y+) + ef(y−)

2ef(y)

∂iqi(y) = ef(y)g(y)iv(y)i (45) Summing up, we get

1 h(Xt) y∈C

E[(g∞ ⊗ v∞)i,i|Ft] (=38)

![image 305](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile305.png>)

n

1 h(Xt) y∈C

(=45)

![image 306](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile306.png>)

n

∂iqi(Xt) h(Xt) which completes the proof.

(=21)

![image 307](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile307.png>)

w(Xt, y)ef(y)v(y)ig(y)i

w(Xt, y)∂iqi(y)

![image 308](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile308.png>)

![image 309](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile309.png>)

![image 310](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile310.png>)

![image 311](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile311.png>)

Now, consider the matrix

At := E[(g∞ − gt) ⊗ (v∞ − vt)|Ft] = E[g∞ ⊗ v∞|Ft] − gt ⊗ vt (46) (where the second equality follows from the fact that gt and vt are martingales). The result of

- Lemma 26 combined with equation (42) tells us that


Tr(σt1/2Γt) = Tr(σt1/2At). (47) Our next objective is to prove:

- Lemma 27. We have almost surely for all t ≥ 0,

Tr(σt1/2Ht) ≤ 4Tr(σt1/2At). (48)

In order to prove this lemma, we ﬁrst formulate an intermediate technical lemma, whose proof is postponed to the appendix.

- Lemma 28. For all t ≥ 0 and i ∈ [n] we have almost surely


ei, g∞ 1 + Xt, ei ei, g∞ Ft = E ζ X

t,ei ( ei, g∞ ) |Ft . (49)

vt, ei = E

![image 312](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile312.png>)

and

t,ei ( g∞, ei )|Ft]. (50) Moreover, for all x ∈ Cn and i ∈ [n] one has

E[ g∞ − gt, ei v∞, ei |Ft] = E[ g∞ − gt, ei ζ X

![image 313](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile313.png>)

x, ei v(x), ei ≤ 1 (51) and under the additional assumption x ∈ −12, 12 n,

![image 314](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile314.png>)

![image 315](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile315.png>)

| v(x), ei | ≤ 2. (52) Proof of Lemma 27. Fix a coordinate i ∈ [n] and deﬁne G = g∞, ei , V = v∞, ei , x =

![image 316](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile316.png>)

![image 317](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile317.png>)

Xt, ei and G = gt, ei . Since gt is a martingale we have G = E[G|Ft]. Our main step will be to show that

1 4

E[(G − G)2|Ft]. (53) Assuming the latter inequality, deﬁning σi = (σt1/2)i,i we can write

![image 318](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile318.png>)

![image 319](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile319.png>)

E[(G − G)V |Ft] ≥

![image 320](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile320.png>)

Tr(σt1/2At) = E

= E

1 4

(53)

≥

E

![image 321](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile321.png>)

n

σi g∞ − gt, ei v∞ − vt, ei Ft

i=1

n

σi g∞ − gt, ei v∞, ei Ft

i=1

n

1 4

Tr(σt1/2Ht),

σi g∞ − gt, ei 2 Ft =

![image 322](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile322.png>)

i=1

which ﬁnishes the proof. In order to prove (53), we ﬁrst note that the identity

![image 323](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile323.png>)

![image 324](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile324.png>)

E[(G − G)V |Ft] = E[(G − G)ζx(G)|Ft] (54) follows from (50). A calculation shows that for all x, y ∈ (−1, 1),

d dy

1 (1 + xy)2 ≥

1 4

y 1 + xy

d dy

ζx(y) =

=

![image 325](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile325.png>)

![image 326](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile326.png>)

![image 327](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile327.png>)

![image 328](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile328.png>)

![image 329](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile329.png>)

which implies that

1 4|G − G|. (55)

![image 330](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile330.png>)

![image 331](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile331.png>)

ζx(G) − ζx(G) ≥

![image 332](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile332.png>)

Therefore,

E[(G − G)V |Ft] (=54) E[(G − G)ζx(G)|Ft]

![image 333](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile333.png>)

![image 334](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile334.png>)

![image 335](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile335.png>)

![image 336](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile336.png>)

= E (G − G)(ζx(G) − ζx(G))|Ft

![image 337](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile337.png>)

![image 338](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile338.png>)

= E G − G · ζx(G) − ζx(G) |Ft

1 4

(55)

E G − G 2 |Ft , which is (53). The proof is complete.

![image 339](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile339.png>)

≥

![image 340](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile340.png>)

![image 341](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile341.png>)

![image 342](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile342.png>)

![image 343](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile343.png>)

![image 344](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile344.png>)

Deﬁne for all t,

It = |{i ∈ [n]; ei, σtei = 0}|. and for all 0 < ε < 1/2, deﬁne the stopping time

Tε = min t > 0 : Xt 2 = ε√n or It ≥ 2 exp −

1 32ε2

![image 345](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile345.png>)

![image 346](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile346.png>)

n ∧ 1.

Observe that by deﬁnition ei, Htei = Var[ g∞, ei |Ft] ≤ 1. Therefore, for all t ≤ Tε, Tr(σt1/2Ht) ≥ Tr(Ht) − It ≥ Tr(Ht) − 2 exp(−1/(32ε2))n. (56)

The following lemma is the main point where Gaussian width comes to play. Its proof is, roughly speaking, an application of the divergence theorem for the vector ﬁeld hq.

![image 347](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile347.png>)

- Lemma 29. Let Bt be a Brownian motion and let gt be a martingale, both adapted to a ﬁltration Ft. Suppose that dgt = Γ˜tdBt for some matrix-valued process Γ˜t satisfying Tr Γ ˜t ≥ 0 almost


surely for all t. Assume that there exists a set K ⊂ Rn such that for all t one has gt ∈ K. Then one has for all t > 0 and α > 1,

1 α

Tr(Γ˜s) > αGW√(tK) <

.

P min

![image 348](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile348.png>)

![image 349](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile349.png>)

![image 350](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile350.png>)

s≤t

Proof. The key idea is to observe that, by an application of Itˆo’s isometry for the processes gt and Bt, we have that

E[ gt, Bt ] = E

t

Tr Γ ˜s ds

0

Tr(Γ˜s) .

≥ E t min

0≤s≤t

On the other hand, since gt ∈ K almost surely for all t, we have GW(K) ≥ E gt, B

√tt . Therefore,

![image 351](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile351.png>)

![image 352](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile352.png>)

GW(K) √t

Tr(Γ˜s) ≤

E min

.

![image 353](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile353.png>)

![image 354](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile354.png>)

s≤t

Since, by assumption, Tr(Γ˜t) is nonnegative, the lemma is concluded via an application of Markov’s inequality.

![image 355](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile355.png>)

![image 356](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile356.png>)

![image 357](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile357.png>)

![image 358](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile358.png>)

The following statement follows easily from Gaussian tail bounds. Fact 30. Let Zt be a (one dimensional) Itoˆ process satisfying

Z0 = 0; dZt = rtdBt with rt being an adapted process satisfying |rt| < r almost surely, for some r > 0. Then, P max

α2 8r2t for all α, t > 0.

|Zs| ≥ α < 2 exp −

![image 359](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile359.png>)

s≤t

As a corollary, we get Lemma 31. For all n ≥ 4 and for all ε ∈ (0, 1/8), we have

ε2 16

P Tε ≤

< 1/n.

![image 360](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile360.png>)

Proof. We have by Itˆo’s formula and by (35), d Xt 22 = 2 Xt, dXt + d[X]t = 2 Xt, σt1/2dBt + 2 Xt, σtvt dt + Tr(σt)dt.

The bound (51) implies that Xt, ei vt, ei ≤ 1 for all i ∈ [n] which, together with that fact that σt is dominated by the identity, gives

d Xt 22 ≤ 2 Xt, σt1/2dBt + 3ndt. Next, Fact 30 with the fact that Xt 2 ≤ ε√n for all t ≤ Tε, implies that P max

![image 361](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile361.png>)

s

Xr, σr1/2dBr ≥ nε2/2 < 2 exp −nε2/(8t) .

s≤t∧Tε

0

Setting t = 16ε2 gives

![image 362](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile362.png>)

Next, deﬁne

P 

 max

ε2 16∧Tε

s≤

![image 363](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile363.png>)

Xs 22 ≥ ε2n

 ≤ 2 exp(−n).

Jt = i ∈ [n]; max

| Bs, ei | ≥ 1/4 .

s≤t

Then by Fact 30, Jt is the sum of n independent Bernoulli random variables, each with expectation bounded by 2 exp(−1/(8ε2)). Recall that, by the Chernoff-Hoeffding Theorem, if Xi are independent Bernoulli random variables with expectation p and S = n1 ni=1 Xi, then

![image 364](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile364.png>)

αn

(1−α)n

e3/2p α

αn 1 − p 1 − α

p α

p α

αn

3 2

α(1−α)n ≤

, ∀p < α < 21.

≤

e

P(S > α) ≤

![image 365](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile365.png>)

![image 366](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile366.png>)

![image 367](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile367.png>)

![image 368](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile368.png>)

![image 369](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile369.png>)

![image 370](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile370.png>)

where the second inequality uses the fact that 1−1α ≤ e3α/2 for α ≤ 12. Taking p = 2 exp(−1/(8ε2)) and α = max(p1/4, 1/n), this gives

![image 371](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile371.png>)

![image 372](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile372.png>)

P(Jt ≥ 2 exp(−1/(32ε2))n) = P Jt ≥ max 2 exp(−1/(32ε2))n, 1 ≤ exp 4 3 max(np1/4, 1) (log p + 2) .

![image 373](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile373.png>)

The assumption ε < 1/8 amounts to p < e−7 and the expression p1/4(log p + 2) is decreasing on the interval (0, e−7). This implies np1/4(log p+2) ≤ −4 log n+2 for p ≥ n−4. We therefore get 43 max(np1/4, 1) (log p + 2) ≤ −3 log n + 2 for all p < e−7. Consequently,

![image 374](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile374.png>)

- 1

![image 375](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile375.png>)

- 2n


8 n3 ≤

P(Jt > 2 exp(−1/(32ε2))n) ≤

.

![image 376](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile376.png>)

By (52) one has | vt, ei | ≤ 2 for all i ∈ [n] and t ∈ [0, 1] which gives max

| Bs, ei | < 1/4 ⇒ max

| Xs, ei | < 1/2, ∀t ≤ 1/8.

s≤t

s≤t

Combining this with the fact that It is increasing for t ∈ [0, 1], we conclude that It ≤ Jt for all t ≤ 1/8. Finally, remarking that

Xs 22 ≥ ε2n or Jt ≥ 2 exp(−1/(32ε2))n, and applying a union bound with respect to the events in the last display completes the proof.

Tε < t ≤ 1 ⇒ max

s≤t∧Tε

![image 377](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile377.png>)

![image 378](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile378.png>)

![image 379](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile379.png>)

![image 380](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile380.png>)

We can ﬁnally prove:

Proof of Proposition 18. We intend to invoke Lemma 29 with the processes gt and Γ˜t = σt1/2Γt where Γt is deﬁned as in (42). Equations (47) and (48), together with the fact that Ht is positivedeﬁnite, give

4Tr Γ ˜t ≥ Tr σt1/2Ht ≥ 0. (57)

Observation 25 ensures that gt ∈ K := Conv ({g(y) : y ∈ Cn}). Therefore we may invoke Lemma 29 with the choice t = 16ε2 to get

![image 381](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile381.png>)

Tr σs1/2Hs > 16αGWε (K)

Tr(Γ˜s) > 4αGWε (K)

 ≤ P 

P 

1 α

 <

min

min

.

![image 382](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile382.png>)

![image 383](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile383.png>)

![image 384](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile384.png>)

ε2 16

ε2 16

s≤

s≤

![image 385](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile385.png>)

![image 386](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile386.png>)

Deﬁne

τ := min t : Tr σt1/2Ht ≤ 16αGWε (K) ∧ Tε. A union bound gives

![image 387](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile387.png>)

ε2 16

1 α − P Tε ≤

.

P (τ < Tε) ≥ 1 −

![image 388](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile388.png>)

![image 389](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile389.png>)

Remark that if either D > 2−4n or n < 4 then the result of the proposition follows trivially by taking m to be supported at 0, thus we may assume n ≥ 4 and ε < 1/8. Using Lemma 31 therefore gives

1 α −

1 n

P (τ < Tε) ≥ 1 −

. (58) Applying equation (40) with the stopping time τ which tells us that for every test function ϕ,

![image 390](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile390.png>)

![image 391](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile391.png>)

ϕdν = E ϕd τη(X

τ)(ν) .

Set the measure m to be the law of η(Xτ), so that equation (30) holds. Since Tε ≤ 1 and by the deﬁnition of σt, we have Xτ ∞ ≤ 1/2 and Xτ 2 ≤ ε√n. Since |η′(z)| ≤ 4/3 for all |z| < 1/2 this implies that for θ := η(Xτ) one has θ ∞ ≤ 2/3 and θ 2 ≤ ε√n. Therefore, the measure m is supported on [−1, 1]n ∩ B(0, ε√n).

![image 392](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile392.png>)

![image 393](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile393.png>)

![image 394](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile394.png>)

Next, note that by deﬁnition of Tε, we have Tr(στ1/2) ≥ n − 2ne−1/(32ε

2). (59) Apply equation (44) and use the deﬁnition of τ to get

8αGW(K) ε

τ)(ν)) ≤ 10Tr στ1/2Hτ ≤ 2

τ < Tε ⇒ Tr στ1/2H(τη(X

![image 395](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile395.png>)

which, together with equations (58) and (59) implies Equation (31).

It remains to show that under the additional assumption ε ≤ 81 (log(4n/GW(K)))−1/2 ≤ 1, Equation (31) holds with k = 1. To that end, an application of equation (56) gives

![image 396](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile396.png>)

τ < Tε ⇒ Tr(Hτ) ≤ 16αGWε (K) + 2 exp(−1/(32ε2))n ≤ 20αGWε (K). Applying Equation (44), in a similar manner to the above, completes the proof.

![image 397](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile397.png>)

![image 398](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile398.png>)

![image 399](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile399.png>)

![image 400](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile400.png>)

![image 401](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile401.png>)

![image 402](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile402.png>)

## 4 The large deviation framework

In this section we prove Corollary 2 and Theorem 5. The following is a trivial consequence of the chain rule. Its proof is postponed to the appendix.

Fact 32. Let ν be measure on Cn and let ξ be a product measure satisfying E[ξ] = E[ν]. Then DKL(ν µ) ≥ DKL(ξ µ).

Proof of Corollary 2. Deﬁne fˆ(x) = f(x)−log efdµ, so that the measure ν deﬁned by dν = efˆ(x)dµ is a probability measure. Fix ε ∈ (0, 161 ) whose value will be chosen later on. Apply Theorem 1 with ν, ε to obtain (using the second part of the theorem) a function f˜: Cn → R and the measures ν˜ and ξ′ and a subset I ⊂ [n]. The theorem ensures us that

![image 403](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile403.png>)

|fˆ(y) − f˜(y)| ≤ εn (60)

max

y∈Cn

and that

![image 404](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile404.png>)

nD(f) ε

W1(˜ν, ξ′) ≤ 26

. The last inequality clearly implies

![image 405](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile405.png>)

fdξ′ − fdν˜ ≤ 26Lip(f)

Moreover, since ξ′ = πI(ξ′) × π[n]\I(˜ν),

![image 406](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile406.png>)

nD(f) ε

. (61)

![image 407](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile407.png>)

f(y)dξ′(y) =

f(z, w)dπI(ξ′) z dπ[n]\I(˜ν) w .

{−1,1}[n]\I {−1,1}I

f(z, w0)dπI(ξ′)(z) ≥ fdξ′. Deﬁne ξ to be the restriction of ξ′ to {w0} × {−1, 1}I and observe that ξ is a product

The above identity implies the existence of w0 ∈ {−1, 1}[n]\I for which {−1,1}

I

measure, since the marginal of ξ′ on the subset I is a product measure. The above amounts to

fdξ ≥ fdξ′

(61)

≥ fdν˜ − 26Lip(f)

Moreover, equation (60) implies that

![image 408](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile408.png>)

nD(f) ε

.

![image 409](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile409.png>)

fd ˜ ν˜ − fdν˜ − log efdµ ≤ εn.

By Fact 32, together with the chain rule for relative entropy, we have that

DKL(˜ν µ) ≥ DKL πI(˜ν) × π[n]\I(˜ν) µ ≥ DKL(ξ′ µ) ≥ DKL(ξ µ) − (n − |I|) log 2.

Since ef˜ is a probability density, and since n − |I| ≤ 2ne−1/(32ε2), we therefore get

fd ˜ ν˜ = fe ˜ f˜dµ = DKL(˜ν µ) ≥ DKL(ξ µ) − 2ne−1/(32ε

2).

A combination of the above ﬁnally gives

2

fdξ − log efdµ − DKL(ξ µ) ≥ − ε + 2e−1/(32)ε

n − 26Lip(f)

![image 410](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile410.png>)

nD(f) ε

.

![image 411](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile411.png>)

2D(f) n

We choose ε = 4Lip(f)

![image 412](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile412.png>)

1/3

. Remark that we may legitimately assume that

64Lip(f)2/3D(f)1/3n2/3 ≤ nlog 2,

since, otherwise, the result of the corollary holds trivially by taking ξ to be supported on the point where f attains its maximum. This amounts to ε < 2−4. Since 2e−1/(32)ε2 ≤ ε for all ε ∈ (0, 2−4), we get the desired bound.

![image 413](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile413.png>)

![image 414](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile414.png>)

![image 415](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile415.png>)

![image 416](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile416.png>)

Proof of Theorem 5. We begin by following similarlines to the proof of [Chatterjee and Dembo, 2016, Theorem 1.1]. Deﬁne

 

2x + 1 x ≤ −1 −x2 −1 ≤ x ≤ 0 0 x ≥ 0

h(x) =



so that h is concave and |h′| ≤ 2. By a Taylor approximation argument we clearly have for x0, x ∈ R,

|h(x0 + x) − h(x0) − xh′(x0)| ≤ x2. (62) Next, deﬁne

ψ(x) = Kh((x − t)/δ)

for K = φp(t − δ)/n. Thus |ψ′| ≤ 2δK and |ψ′′| ≤ 2δK2

. Now set g(y) = nψ(f(y)/n), ∀y ∈ Cn.

![image 417](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile417.png>)

![image 418](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile418.png>)

Our ﬁrst goal is to give an estimate for the complexity D(g) in terms of D(f). Deﬁne Af = {∇f(y) : y ∈ Cn}, Ag = {∇g(y) : y ∈ Cn}

For y ∈ Cn deﬁne Si(y) to be the unique point all of whose coordinates except for the ith coordinate are equal to the corresponding ones of y (and the i-th coordinate is the negative of its concurrent). Using a Taylor approximation to ψ at f(y)/n, for all y = (y1, . . ., yn) ∈ Cn we have the bound

|∂ig(y) − ψ′(f(y)/n)∂if(y)| = −y

2 g(Si(y)) − g(y) − ψ′(f(y)/n)∂if(y)

i

![image 419](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile419.png>)

= −ny

2 ψ(f(Si(y))/n) − ψ(f(y)/n) − ψ′(f(y)/n)∂if(y)

i

![image 420](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile420.png>)

K 2δ2n

(62)

Lip(f)2, or in other words,

≤

![image 421](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile421.png>)

K δ2√n

|∇g(y) − ψ′(f(y)/n)∇f(y)| ≤

Lip(f)2.

![image 422](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile422.png>)

![image 423](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile423.png>)

Consequently, since |ψ′(f(y)/n)| ≤ 2δK for all y ∈ Cn, we have for every vector v ∈ Rn,

![image 424](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile424.png>)

K δ2√n

2K δ

Lip(f)2|v|.

v, u +

sup

v, u ≤ max 0,

sup

![image 425](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile425.png>)

![image 426](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile426.png>)

![image 427](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile427.png>)

u∈Af

u∈Ag

√n, we get that

![image 428](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile428.png>)

Now, since for a standard Gaussian random vector Γ one has E|Γ| ≤

2K δ D(f) +

K δ2

Lip(f)2. (63) By the same considerations, we also have that

D(g) ≤

![image 429](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile429.png>)

![image 430](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile430.png>)

|ψ′(x)|Lip(f) ≤

Lip(g) ≤ sup

x∈R

Since f(x) ≥ tn ⇒ g(x) = 0 we get that, for Y ∼ µp,

2K δ

Lip(f). (64)

![image 431](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile431.png>)

P(f(Y ) ≥ tn) ≤ E[exp(g(Y ))] =

exp(g(y) + log I(p , y))dµ (65)

Cn

where p  = (−1+2p)(1, . . ., 1) and I(x, y) = i∈[n](1+xiyi), so that log I(p , y) = i log(1− yi + 2pyi). We also easily have

Lip(log I(p , ·)) ≤ | log(p(1 − p))|. Invoking Corollary 2, we learn that for some product measure ξ,

log

exp(g(y) + log I(p ,y))dµ (66)

Cn

≤ gdξ + log I(p ,y)dξ(y) − DKL(ξ µ) + 64(Lip(g) + |log(p)(1 − p)|)2/3D(g)1/3n2/3.

An easy calculation shows that log I(p , y)dξ(y) − DKL(ξ µ) = −DKL(ξ µp). Combining this with (63) and (64) we have that

with

log

exp(g(y))dµp ≤ gdξ − DKL(ξ µp) + 64KLn2/3 (67)

Cn

1 δ

(2Lip(f) + | log(p(1 − p))|)2/3 2D(f) +

L :=

![image 432](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile432.png>)

1 δ

Lip(f)2

![image 433](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile433.png>)

1/3

where we use the assumption δ ≤ n1φp(t − δ) which implies K/δ ≥ 1. Next, we claim that for every product measure ξ one has

![image 434](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile434.png>)

gdξ − DKL(ξ µp) ≤ −φp(t − δ). (68)

Indeed, if ξ is such that fdξ ≥ (t − δ)n then by deﬁnition of φp, we must have that −DKL(ξ µp) ≤ −φp(t − δ), and since g is non-positive, the inequality is correct. So, we may assume that fdξ ≤ (t − δ)n. By the concavity and monotonicity of ψ and by Jensen’s inequality, we have

gdξ = nψ(f(y)/n)dξ(y) ≤ nψ fdξ/n ≤ nψ (t − δ) = −Kn = −φp(t − δ).

This establishes (68). Together with equations (65) and (66), we ﬁnally get

log P(f(Y ) ≥ tn) ≤ −φp(t − δ)(1 − 64Ln−1/3). The proof of the upper bound is complete.

Moving on to the lower bound, we deﬁne the function g in the same way, with the exception that this time we take K = 2(φp(t) + 1)/n. With the help of equation (62) and by Jensen’s inequality we have for every random variable Z,

E[nψ(Z/n)] ≥ n(ψ(E[Z]/n)) −

K δ2n

Var[Z].

![image 435](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile435.png>)

Moreover, clearly if W1, . . ., Wn are independent Bernoulli random variables (with arbitrary expectation) and W = (W1, . . ., Wn) setting Mi = E[f(W)|W1, . . ., Wi] then

n

E(Mi − Mi−1)2 ≤ Lip(f)2

Var[Wi] ≤ nLip(f)2.

Var(f(W)) =

i=1

i∈[n]

The two last displays teach us that for every product measure ξ one has

gdξ ≥ nψ

fdξ n −

K δ2

Lip(f)2.

![image 436](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile436.png>)

![image 437](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile437.png>)

which ﬁnally gives

P(f(Y ) ≥ (t − δ)n) ≥ egdµp −

egdµp

{y:f(y)≤(t−δ)n}

≥ egdµp − exp(−2nK)

gdξ − DKL(ξ µp) − exp(−2φp(t) − 2)

≥ exp sup

ξ∈PM

fdξ n − DKL(ξ µp) −

2K δ2

Lip(f)2 − exp(−2φp(t) − 2)

nψ

≥ exp sup

![image 438](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile438.png>)

![image 439](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile439.png>)

ξ∈PM

1 nδ2

1 nδ2

Lip(f)2 −

Lip(f)2 − exp(−2φp(t) − 2)

≥ exp −φp(t) 1 +

![image 440](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile440.png>)

![image 441](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile441.png>)

1 nδ2

Lip(f)2 − 1 1 − exp(−1)

≥ exp −φp(t) 1 +

![image 442](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile442.png>)

where the last inequality uses the assumption nδ2

![image 443](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile443.png>)

2

Lip(f)2 ≤ 1. We ﬁnally get

log P(f(Y ) ≥ (t − δ)n) ≥ −φp(t) 1 +

2 nδ2

Lip(f)2 − 2.

![image 444](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile444.png>)

The proof is complete.

![image 445](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile445.png>)

![image 446](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile446.png>)

![image 447](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile447.png>)

![image 448](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile448.png>)

## 5 Exponential random graphs and complexity of subgraph counts

Fix an integer N and set n = N2 . Recall that we deﬁne by P the set of above-diagonal sequences (yi,j)1≤i<j≤N, which is identiﬁed with Cn. For a ﬁnite, simple graph H and a point y ∈ Cn we deﬁne

fH(y) = N2t(H, Gy).

where Gy is the graph associated with y and t(H, G) is the homomorphism density deﬁned in section 1.4. The next lemma gives a bound for the Gaussian-width complexity of subgraph counts.

Lemma 33. For every ﬁnite simple graph H = ([k], E) on k vertices, we have D(fH) ≤ |E|N3/2.

Proof. For a ﬁxed y ∈ Cn, let A = A(y) be the adjacency matrix of Gy. We have

1 Nk−2

fH(y) =

Aq

.

ℓ,qℓ′

![image 449](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile449.png>)

q∈[N]k (ℓ,ℓ′)∈E

A calculation gives (see also [Chatterjee and Dembo, 2016, Equation (5.2)])

∂fH(y) ∂yi,j

![image 450](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile450.png>)

=

=

=

where Ji,j(A, a, b, q) =

(a,ℓ)∈E ℓ =b

1 Nk−2

Aq

ℓ,qℓ′

![image 451](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile451.png>)

(ℓ,ℓ′)∈E {ℓ,ℓ′} ={a,b}

(a,b)∈E q∈[N]k

qa=i,qb=j

1 Nk−2

Ai,q

![image 452](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile452.png>)

ℓ

(a,b)∈E q∈[N]k−2 (a,ℓ)∈E

(b,ℓ)∈E ℓ =a

ℓ =b

1 Nk−2

Ji,j(A, a, b, q)

![image 453](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile453.png>)

(a,b)∈E q∈[N]k−2

Aj,q

ℓ

Aq

ℓ,qℓ′

(ℓ,ℓ′)∈E {a,b}∩{ℓ,ℓ′}=∅

(69)

Ai,q

ℓ

Aj,q

ℓ

(b,ℓ)∈E ℓ =a

Aq

(ℓ,ℓ′)∈E {a,b}∩{ℓ,ℓ′}=∅

, ∀(a, b) ∈ E, q ∈ [N]k−2.

ℓ,qℓ′

By construction, we see that for all a, b, q the matrix J(A, a, b, q) is of rank 1. Moreover, clearly the entries of this matrix are all in {0, 1}. Consequently, we have for all M ∈ MN×N

sup

Tr(Ji,j(A, a, b, q)M) ≤ sup

u,v∈{0,1}n

A∈Mn×n q∈[N]k−1,(a,b)∈E

u, Mv ≤ N M OP.

Thus if for θ ∈ Rn we set M(θ) to be the unique symmetric matrix with null diagonal and whose above-diagonal entries that those of θ, then the above inequality combined with (69) yields

1 Nk−2

 ∇fH(y), θ =

Tr(Ji,j(A, a, b, q)M(θ))

![image 454](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile454.png>)

(a,b)∈E q∈[N]k−2

1 2Nk−2

≤

N M(θ) OP

![image 455](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile455.png>)

(a,b)∈E q∈[N]k−2

- 1

![image 456](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile456.png>)

- 2|E| · N M(θ) OP.


≤

Therefore, if Γ is a standard Gaussian random vector in Rn then

- 1

![image 457](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile457.png>)

- 2|E| · NE M(Γ) OP ≤ |E|N3/2.


 ∇fH(y), Γ ≤

E sup

y∈Cn

where the last inequality follows from standard estimates for norms of Gaussian matrices. The proof is complete.

![image 458](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile458.png>)

![image 459](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile459.png>)

![image 460](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile460.png>)

![image 461](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile461.png>)

We can now prove our Theorem about decomposition of exponential random graphs.

Proof of Theorem 9. Setting n = N2 , we identify a point y ∈ Cn with the graph Gy as in Section 1.2.1. Consider the function

l

f(y) = N2

βit(Hi, Gy).

i=1

According to Lemma 33 and since the Gaussian-width is sub-additive, the complexity of f is bounded as follows

l

D(f) ≤ 2n3/4

|βi||E(Hi)|.

i=1

Cn efdµ. Observe that by deﬁnition if Y ∼ ν then GY =d G. We now apply Theorem 3 with the measure ν, ε and some α > 1 whose value will be chosen later on, to obtain a measure m on B(0, ε√n). Moreover, for all θ ∈ Rn deﬁne by ξθ the product measure having the same marginals as τθν, and deﬁne by  p(θ) to be the unique p  ∈ [0, 1](

fdµ

Deﬁne the measure ν on Cn by dν = e

![image 462](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile462.png>)

![image 463](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile463.png>)

N 2

)

such that G(N,  p) has the same distribution as GZ with Z ∼ ξ. Let ρ be push-forward of m under the map θ → p (θ). For all θ let Yθ be a random point having the law τθν. Moreover let θ˜ be a random variable in Rn whose law is m, which is independent from the family {Yθ}. Then by equation (5) we have that

G := GY

θ˜

has the exponential graph distribution (9). Moreover, for all θ ∈ Rn let G′

θ be distributed as G(N,  p(θ)). We may assume that G′θ are deﬁned on the same probability space, and that the family {G′

θ} is independent of θ˜. Now, deﬁne

G′ = G′θ˜. It is clear that G′ has the distribution G(N, ρ). Now, according to equation (6) there exists Θ with m(Θ) ≥ 1 − α1 − n1 such that for all θ ∈ Θ we may couple the graph G′

θ with GY

so that

![image 464](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile464.png>)

![image 465](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile465.png>)

θ

, G′θ ≤ 16

EdH GY

θ

![image 466](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile466.png>)

αnD(ν) ε

.

![image 467](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile467.png>)

Therefore, by taking expectation with respect to θ˜, we have

EdH G, G′ ≤ 16

![image 468](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile468.png>)

αnD(ν) ε

+ n

![image 469](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile469.png>)

1 α

1 n

+

![image 470](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile470.png>)

![image 471](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile471.png>)

.

Choosing α = nD1(/ν3)ε1/3

, we get

![image 472](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile472.png>)

1/3

20n2/3D(ν)1/3 ε1/3 ≤

20n11/12 ε1/3

EdH G, G′ ≤

![image 473](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile473.png>)

![image 474](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile474.png>)

and ﬁnally equation (7) tells us that

l

|βi||E(Hi)|

i=1

1/3

I(p)dρ(p) ≥ Ent(G) − 2εn.

![image 475](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile475.png>)

![image 476](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile476.png>)

![image 477](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile477.png>)

![image 478](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile478.png>)

## 6 Appendix - proofs of Auxiliary results

Proof of Fact 32. This is a straightforward consequence of the chain rule for relative entrory. Let Y = (Y1, . . ., Yn) ∼ ν and Y˜ = (Y˜1, . . ., Y˜n) ∼ ξ. Then we have

nlog 2 − DKL(ν µ) = H((Y1, . . ., Yn))

n

=

H(Yi|(Y1, ..., Yi−1))

i=1

n

≤

H(Yi)

i=1

n

H(Y˜i) = nlog 2 − DKL(ξ µ).

=

i=1

![image 479](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile479.png>)

![image 480](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile480.png>)

![image 481](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile481.png>)

![image 482](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile482.png>)

Proof of Lemma 16. By deﬁnition of the function g(y) = gν(y) (or according to equation (26)), we have that for all y ∈ Cn if we denote gν(y) = (g1, ..., gn) and ∇fν(y) = (d1, ..., dn) then

ed

− 1 edi + 1

i

.

gi = ϕ(di) :=

![image 483](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile483.png>)

Since |ϕ′(x)| ≤ 1 for all x ∈ R, we have that the set {gν(y) : y ∈ Cn} is the image of the set {∇f(y) : y ∈ Cn} under a 1-Lipschitz mapping. In turn, we have for all y1, y2 ∈ Cn,

|gν(y1) − gν(y2)| ≤ |∇fν(y1) − ∇fν(y2)| and therefore

E g(y1) − g(y2), Γ 2 ≤ E  ∇f(y1) − ∇f(y2), Γ 2 where Γ is a standard Gaussian random vector. An application of the Sudakov-Fernique inequality (see e.g., [Ledoux and Talagrand, 2011, Chapter 3]) completes the proof.

![image 484](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile484.png>)

![image 485](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile485.png>)

![image 486](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile486.png>)

![image 487](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile487.png>)

Proof of Fact 23. The proof is a straightforward calculation using Itˆo’s formula,

q(Xt)dh(Xt) h2(Xt)

q(Xt)d[h(X)]t h3(Xt) −

d[q(X), h(X)]t h2(Xt)

dq(Xt) h(Xt) −

+

dgt =

![image 488](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile488.png>)

![image 489](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile489.png>)

![image 490](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile490.png>)

![image 491](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile491.png>)

= ∇q(Xt) h(Xt) −

q(Xt) ⊗ ∇h(Xt) h2(Xt)

σt1/2dBt + σtvtdt

![image 492](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile492.png>)

![image 493](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile493.png>)

q(Xt) σt∇h(Xt), ∇h(Xt) h3(Xt)

∇q(Xt)σt∇h(Xt) h2(Xt)

+

dt −

dt

![image 494](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile494.png>)

![image 495](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile495.png>)

= ∇q(Xt) h(Xt) − gt ⊗ vt σt1/2dBt + σtvtdt

![image 496](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile496.png>)

∇q(Xt)σtvt h(Xt)

dt

+ gt vt, σtvt dt −

![image 497](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile497.png>)

= ∇q(Xt) h(Xt) − gt ⊗ vt σt1/2dBt.

![image 498](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile498.png>)

![image 499](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile499.png>)

![image 500](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile500.png>)

![image 501](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile501.png>)

![image 502](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile502.png>)

Proof of Lemma 24. Let Y ∈ Cn be a random variable with law ν˜. Fix i ∈ [n]. The lemma will be concluded by showing that

θν(Y ), ei ≤ exp(4 θ ∞)Var gν(Y ), ei . (70) Next, by deﬁnition of τθν we have ∇fτ

Var gτ

θν = ∇fν + θ, and equation (27) gives gτ

θν(y)) = tanh(∇fν(y) + θ) = tanh(tanh−1(gν(y)) + θ) for all y ∈ Cn, so that

θν(y) = tanh(∇fτ

( gν(y), ei ), ∀y ∈ Cn, where us(z) := tanh(tanh−1(z) + s).

gτ

θν(y), ei = uθ

i

Deﬁning Z = gν(Y ), ei and using the last display, equation (70) becomes Var[uθ

(Z)] ≤ exp(4 θ ∞)Var[Z].

i

It is straightforward to check that for all x ∈ (−1, 1) and s ∈ R, one has dx d us(x) ≤ exp2|s|. Since for any L-Lipschitz function u and any random variable Z one has Var[u(Z)] ≤ L2Var[Z],

![image 503](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile503.png>)

it follows that

(Z)] ≤ exp(4|θi|)Var[Z]. This yields (70) which completes the proof.

Var [uθ

i

![image 504](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile504.png>)

![image 505](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile505.png>)

![image 506](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile506.png>)

![image 507](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile507.png>)

Proof of Lemma 28. Deﬁne x = Xt, ei , V = v∞, ei and G = g∞, ei . Let p˜ : Cn → R be a function satisfying ∂ip˜ ≡ 0, let p be the harmonic extension of p˜ to Cn and deﬁne P = p˜(X∞). Set C˜n = {(y1, ..., yn), yi = Xt, ei and yj ∈ {−1, 1}, ∀j = i} and let π : {−1, 1}n → {−1, 1}n−1 be the projection deﬁned by π((y1, ..., yn)) = (y1, ..., yi−1, yi+1, ..., yn). We calculate

![image 508](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile508.png>)

1 h(Xt) y∈C

E[V P|Ft] (=38)

w(Xt, y)ef(y)p(y) v(y), ei

![image 509](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile509.png>)

n

1 h(Xt) y∈C

w(Xt, y)p(y)∂ief(y)

=

![image 510](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile510.png>)

n

1 h(Xt)

w(π(Xt), π(˜y))p(˜y)∂ih(˜y)

=

![image 511](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile511.png>)

y ˜∈C˜n

1 h(Xt)

∂ih(˜y) h(˜y)

=

w(π(Xt), π(˜y))h(˜y)p(˜y)

![image 512](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile512.png>)

![image 513](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile513.png>)

y ˜∈C˜n

∂ih(y)

1 h(Xt) y∈C

w(Xt, y)h(y)p(y)

=

![image 514](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile514.png>)

![image 515](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile515.png>)

h (y1, . . ., yi−1, x, yi+1, . . ., yn) (=24)

n

1 h(Xt) y∈C

w(Xt, y)h(y)p(y)ζx( g(y), ei ) (=38) E[ζx(G)P|Ft].

![image 516](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile516.png>)

n

The proof of (49) follows by taking p˜(y) = 1 and that of (50) follows by taking p˜(y) = g(y)− gt, ei . Finally, in order to obtain the bound (52), we combine the formula (49) with the estimate

|ζx(g)| =

1 1 − 12

g 1 + gx ≤

≤ 2, ∀g ∈ [−1, 1], x ∈ [−1/2, 1/2].

![image 517](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile517.png>)

![image 518](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile518.png>)

![image 519](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile519.png>)

To obtain the bound (51), observe that for any x, g ∈ (0, 1) one has

gx

x · ζx(g) =

1 + gx ≤ 1, use the formula (49) and take expectation.

![image 520](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile520.png>)

![image 521](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile521.png>)

![image 522](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile522.png>)

![image 523](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile523.png>)

![image 524](<2016-eldan-gaussian-width-gradient-complexity-reverse_images/imageFile524.png>)

## References

Anirban Basak and Sumit Mukherjee. Universality of the mean-ﬁeld for the Potts model. Probab. Theory Related Fields, 168(3-4):557–600, 2017. ISSN 0178-8051. doi: 10.1007/ s00440-016-0718-0. URL http://dx.doi.org/10.1007/s00440-016-0718-0.

Bhaswar B. Bhattacharya, Shirshendu Ganguly, Xuancheng Shao, and Yufei Zhao. Upper tails for arithmetic progressions in a random set. 2016.

Bhaswar B. Bhattacharya, Shirshendu Ganguly, Eyal Lubetzky, and Yufei Zhao. Upper tails and independence polynomials in random graphs. Adv. Math., 319: 313–347, 2017. ISSN 0001-8708. doi: 10.1016/j.aim.2017.08.003. URL http://dx.doi.org/10.1016/j.aim.2017.08.003.

Christer Borell. Isoperimetry, log-concavity, and elasticity of option prices. In New directions in Mathematical Finance, pages 73–91. Wiley, 2002. Edited by P. Wilmott and H. Rasmussen.

Sourav Chatterjee. Large deviations for random graphs, volume 2197 of Lecture Notes in Mathematics. Springer, Cham, 2017. ISBN 978-3-319-65815-5; 978-3-319-65816-2. URL https://doi.org/10.1007/978-3-319-65816-2. Lecture notes from the 45th Probability Summer School held in Saint-Flour, June 2015, Ecole´ d’Ete´´ de Probabilite´s de Saint-Flour. [Saint-Flour Probability Summer School].

Sourav Chatterjee and Amir Dembo. Nonlinear large deviations. Adv. Math., 299:396–450, 2016. ISSN 0001-8708. doi: 10.1016/j.aim.2016.05.017. URL http://dx.doi.org/10.1016/j.aim.2016.05.017.

Sourav Chatterjee and Persi Diaconis. Estimating and understanding exponential random graph models. Ann. Statist., 41(5):2428–2461, 2013. ISSN 0090-5364. doi: 10.1214/13-AOS1155. URL http://dx.doi.org/10.1214/13-AOS1155.

R. Eldan and J. R. Lee. Regularization under diffusion and anti-concentration of temperature. Preprint: arXiv: 1410.3887, 2014.

Ronen Eldan and Renan Gross. Decomposition of mean-ﬁeld gibbs distributions into product measures, 2017a.

Ronen Eldan and Renan Gross. Exponential random graphs behave like mixtures of stochastic block models, 2017b.

Ronen Eldan, James R. Lee, and Joseph Lehec. Transport-entropy inequalities and curvature in discrete-space markov chains, 2016.

H. F¨ollmer. An entropy approach to the time reversal of diffusion processes. In Stochastic differential systems (Marseille-Luminy, 1984), volume 69 of Lecture Notes in Control and Inform. Sci., pages 156–163. Springer, Berlin, 1985. doi: 10.1007/BFb0005070. URL http://dx.doi.org/10.1007/BFb0005070.

Michel Ledoux and Michel Talagrand. Probability in Banach spaces. Classics in Mathematics. Springer-Verlag, Berlin, 2011. ISBN 978-3-642-20211-7. Isoperimetry and processes, Reprint of the 1991 edition.

Joseph Lehec. Representation formula for the entropy and functional inequalities. Ann. Inst. Henri Poincare´ Probab. Stat., 49(3):885–899, 2013. ISSN 0246-0203.

Eyal Lubetzky and Yufei Zhao. On the variational problem for upper tails in sparse random graphs. 2014.

M. Talagrand. Transportation cost for Gaussian and other product measures. Geom. Funct. Anal., 6(3):587–600, 1996. ISSN 1016-443X. doi: 10.1007/BF02249265. URL http://dx.doi.org/10.1007/BF02249265.

