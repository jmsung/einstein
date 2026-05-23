# arXiv:1604.00772v2[cs.LG]10Mar2023

## The CMA Evolution Strategy: A Tutorial

Nikolaus Hansen Inria Research centre Saclay–ˆIle-de-France

### Contents

Nomenclature 2

- 0 Preliminaries 3

- 0.1 Eigendecomposition of a Positive Deﬁnite Matrix . . . . . . . . . . . . . . . 4
- 0.2 The Multivariate Normal Distribution . . . . . . . . . . . . . . . . . . . . . 5
- 0.3 Randomized Black Box Optimization . . . . . . . . . . . . . . . . . . . . . 6
- 0.4 Hessian and Covariance Matrices . . . . . . . . . . . . . . . . . . . . . . . . 7


- 1 Basic Equation: Sampling 8
- 2 Selection and Recombination: Moving the Mean 8
- 3 Adapting the Covariance Matrix 10

- 3.1 Estimating the Covariance Matrix From Scratch . . . . . . . . . . . . . . . . 10
- 3.2 Rank-µ-Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
- 3.3 Rank-One-Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

- 3.3.1 A Different Viewpoint . . . . . . . . . . . . . . . . . . . . . . . . . 15
- 3.3.2 Cumulation: Utilizing the Evolution Path . . . . . . . . . . . . . . . 16


- 3.4 Combining Rank-µ-Update and Cumulation . . . . . . . . . . . . . . . . . . 18


- 4 Step-Size Control 19
- 5 Discussion 22


- A Algorithm Summary: The CMA-ES 28
- B Implementational Concerns 32

- B.1 Multivariate normal distribution . . . . . . . . . . . . . . . . . . . . . . . . 33
- B.2 Strategy internal numerical effort . . . . . . . . . . . . . . . . . . . . . . . . 33
- B.3 Termination criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
- B.4 Flat ﬁtness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
- B.5 Boundaries and Constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . 34


- C MATLAB Source Code 36
- D Reformulation of Learning Parameter ccov 38


Compiled March 13, 2023

### Nomenclature

We adopt the usual vector notation, where bold letters, v, are column vectors, capital bold letters, A, are matrices, and a transpose is denoted by vT. A list of used abbreviations and symbols is given in alphabetical order.

Abbreviations CMA Covariance Matrix Adaptation EMNA Estimation of Multivariate Normal Algorithm ES Evolution Strategy (µ/µ{I,W},λ)-ES, Evolution Strategy with µ parents, with recombination of all µ parents,

either Intermediate or Weighted, and λ offspring. RHS Right Hand Side.

Greek symbols λ ≥ 2, population size, sample size, number of offspring, see (5). µ ≤ λ parent number, number of (positively) selected search points in the population, num-

ber of strictly positive recombination weights, see (6).

µeﬀ = µi=1 wi2 −1, the variance effective selection mass for the mean, see (8). wj = λi=1 wi, sum of all weights, note that wi ≤ 0 for i > µ, see also (30) and (53). |wi|+ = µi=1 wi = 1, sum of all positive weights. |wi|− = −( wj − |wi|+) = − λi=µ+1 wi ≥ 0, minus the sum of all negative

weights.

σ(g) ∈ R>0, step-size.

Latin symbols B ∈ Rn, an orthogonal matrix. Columns of B are eigenvectors of C with unit length and

correspond to the diagonal elements of D. C(g) ∈ Rn×n, covariance matrix at generation g. cii, diagonal elements of C. c1 ≤ 1 − cµ, learning rate for the rank-one update of the covariance matrix update, see (28),

(30), and (47), and Table 1.

cµ ≤ 1 − c1, learning rate for the rank-µ update of the covariance matrix update, see (16),

(30), and (47), and Table 1.

cσ < 1, decay rate for the cumulation path for the step-size control, see (31) and (43), and

Table 1.

cc ≤ 1, decay rate for cumulation path for the rank-one update of the covariance matrix, see

(24) and (45), and Table 1.

cm = 1, learning rate for the mean.

- D ∈ Rn, a diagonal matrix. The diagonal elements of D are square roots of eigenvalues of C and correspond to the respective columns of B.

di > 0, diagonal elements of diagonal matrix D, d2i are eigenvalues of C. dσ ≈ 1, damping parameter for step-size update, see (32), (37), and (44).

- E Expectation value


- f : Rn → R,x  → f(x), objective function (ﬁtness function) to be minimized. fsphere : Rn → R,x  → x 2 = xTx = ni=1 x2i.
- g ∈ N0, generation counter, iteration number. I ∈ Rn×n, Identity matrix, unity matrix. m(g) ∈ Rn, mean value of the search distribution at generation g. n ∈ N, search space dimension, see f.


N (0,I), multivariate normal distribution with zero mean and unity covariance matrix. A vector distributed according to N (0,I) has independent, (0,1)-normally distributed components.

N (m,C) ∼ m + N (0,C), multivariate normal distribution with mean m ∈ Rn and

covariance matrix C ∈ Rn×n. The matrix C is symmetric and positive deﬁnite. R>0, strictly positive real numbers. p ∈ Rn, evolution path, a sequence of successive (normalized) steps, the strategy takes over

a number of generations. wi, where i = 1,...,λ, recombination weights, see (6) and (16) and (49)–(53). x(kg+1) ∈ Rn, k-th offspring/individual from generation g + 1. We also refer to x(g+1), as

search point, or object parameters/variables, commonly used synonyms are candidate solution, or design variables.

- x(i:gλ+1), i-th best individual out of x(1g+1),...,x(λg+1), see (5). The index i : λ denotes the

index of the i-th ranked individual and f(x(1:gλ+1)) ≤ f(x(2:gλ+1)) ≤ ··· ≤ f(x(λg:λ+1)), where f is the objective function to be minimized.

- y(kg+1) = (x(kg+1) − m(g))/σ(g) corresponding to xk = m + σyk.


### 0 Preliminaries

This tutorial introduces the CMA Evolution Strategy (ES), where CMA stands for Covariance Matrix Adaptation.1 The CMA-ES is a stochastic, or randomized, method for real-parameter (continuous domain) optimization of non-linear, non-convex functions (see also Section 0.3

1Parts of this material have also been presented in [15] and [17], in the context of Estimation of Distribution Algorithms and Adaptive Encoding, respectively. An introduction deriving CMA-ES from the information-geometric concept of a natural gradient can be found in [19].

below).2 We try to motivate and derive the algorithm from intuitive concepts and from requirements of non-linear, non-convex search in continuous domain. For a concise algorithm description see Appendix A. A respective Matlab source code is given in Appendix C.

Before we start to introduce the algorithm in Sect. 1, a few required fundamentals are summed up.

#### 0.1 Eigendecomposition of a Positive Deﬁnite Matrix

A symmetric, positive deﬁnite matrix, C ∈ Rn×n, is characterized in that for all x ∈ Rn\{0} holds xTCx > 0. The matrix C has an orthonormal basis of eigenvectors, B = [b1,...,bn], with corresponding eigenvalues, d21,...,d2n > 0.

That means for each bi holds

Cbi = d2ibi . (1) The important message from (1) is that eigenvectors are not rotated by C. This feature uniquely distinguishes eigenvectors. Because we assume the orthogonal eigenvectors to be

1 if i = j 0 otherwise

of unit length, bTi bj = δij =

, and BTB = I (obviously this means B−1 = BT, and it follows BBT = I). An basis of eigenvectors is practical, because for any v ∈ Rn we can ﬁnd coefﬁcients αi, such that v = i αibi, and then we have Cv = i d2iαibi.

The eigendecomposition of C obeys

C = BD2BT , (2) where

- B is an orthogonal matrix, BTB = BBT = I. Columns of B form an orthonormal basis of eigenvectors.


D2 = DD = diag(d1,...,dn)2 = diag(d21,...,d2n) is a diagonal matrix with eigenvalues

of C as diagonal elements.

D = diag(d1,...,dn) is a diagonal matrix with square roots of eigenvalues of C as diagonal

elements.

The matrix decomposition (2) is unique, apart from signs of columns of B and permutations of columns in B and D2 respectively, given all eigenvalues are different.3

Given the eigendecomposition (2), the inverse C−1 can be computed via

C−1 = BD2BT −1

= BT−1D−2B−1

##### = B D−2BT

1 d21

1 d2n

##### BT .

= B diag

,...,

- 2While CMA variants for multi-objective optimization and elitistic variants have been proposed, this tutorial is solely dedicated to single objective optimization and non-elitistic truncation selection, also referred to as commaselection.
- 3Given m eigenvalues are equal, any orthonormal basis of their m-dimensional subspace can be used as column vectors. For m > 1 there are inﬁnitely many such bases.


| | | |
|---|---|---|


N 0,σ2I N 0,D2 N (0,C)

Figure 1: Ellipsoids depicting one-σ lines of equal density of six different normal distributions, where σ ∈ R>0, D is a diagonal matrix, and C is a positive deﬁnite full covariance matrix. Thin lines depict possible objective function contour lines

From (2) we naturally deﬁne the square root of C as

- 1

- 2 = BDBT (3)


C and therefore

- 1

- 2 = BD−1BT


C−

1 d1

= B diag

1 dn

,...,

BT

- 0.2 The Multivariate Normal Distribution


- A multivariate normal distribution, N (m,C), has a unimodal, “bell-shaped” density, where the top of the bell (the modal value) corresponds to the distribution mean, m. The distribution N (m,C) is uniquely determined by its mean m ∈ Rn and its symmetric and positive deﬁnite covariance matrix C ∈ Rn×n. Covariance (positive deﬁnite) matrices have an appealing geometrical interpretation: they can be uniquely identiﬁed with the (hyper-)ellipsoid {x ∈ Rn |xTC−1x = 1}, as shown in Fig. 1. The ellipsoid is a surface of equal density of the distribution. The principal axes of the ellipsoid correspond to the eigenvectors of C, the squared axes lengths correspond to the eigenvalues. The eigendecomposition is denoted by


- C = B (D)2 BT (see Sect. 0.1). If D = σI, where σ ∈ R>0 and I denotes the identity matrix, C = σ2I and the ellipsoid is isotropic (Fig. 1, left). If B = I, then C = D2 is a diagonal matrix and the ellipsoid is axis parallel oriented (middle). In the coordinate system given by the columns of B, the distribution N (0,C) is always uncorrelated.


The normal distribution N (m,C) can be written in different ways.

N (m,C) ∼ m + N (0,C) ∼ m + C

- 1

- 2


##### N (0,I) ∼ m + BD BTN (0,I)

∼ N(0,I)

, (4)

##### ∼ m + B DN (0,I)

∼ N(0,D2)

- 1

- 2 = BDBT. The last row can be well


where “∼” denotes equality in distribution, and C interpreted, from right to left

N (0,I) produces an spherical (isotropic) distribution as in Fig. 1, left.

- D scales the spherical distribution within the coordinate axes as in Fig. 1, middle. DN (0,I) ∼ N 0,D2 has n independent components. The matrix D can be interpreted as (individual) step-size matrix and its diagonal entries are the standard deviations of the components.


- B deﬁnes a new orientation for the ellipsoid, where the new principal axes of the ellipsoid


2−n

correspond to the columns of B. Note that B has n

2 degrees of freedom.

Equation (4) is useful to compute N (m,C) distributed vectors, because N (0,I) is a vector of independent (0,1)-normally distributed numbers that can easily be realized on a computer.

#### 0.3 Randomized Black Box Optimization

We consider the black box search scenario, where we want to minimize an objective function (or cost function or ﬁtness function)

f : Rn → R

x  → f(x) .

The objective is to ﬁnd one or more search points (candidate solutions), x ∈ Rn, with a function value, f(x), as small as possible. We do not state the objective of searching for a global optimum, as this is often neither feasible nor relevant in practice. Black box optimization refers to the situation, where function values of evaluated search points are the only accessible information on f.4 The search points to be evaluated can be freely chosen. We deﬁne the search costs as the number of executed function evaluations, in other words the amount of information we needed to acquire from f5. Any performance measure must consider the search costs together with the achieved objective function value.6

A randomized black box search algorithm is outlined in Fig. 2. In the CMA Evolution

4Knowledge about the underlying optimization problem might well enter the composition of f and the chosen problem encoding.

- 5Also f is sometimes denoted as cost function, but it should not to be confused with the search costs.
- 6A performance measure can be obtained from a number of trials as, for example, the mean number of function


evaluations to reach a given function value, or the median best function value obtained after a given number of function evaluations.

|Initialize distribution parameters θ(0) For generation g = 0,1,2,...<br><br>Sample λ independent points from distribution P x|θ(g) → x1,...,xλ Evaluate the sample x1,...,xλ on f Update parameters θ(g+1) = Fθ(θ(g),(x1,f(x1)),...,(xλ,f(xλ))) break, if termination criterion met|
|---|


Figure 2: Randomized black box search. f : Rn → R is the objective function

Strategy the search distribution, P, is a multivariate normal distribution. Given all variances and covariances, the normal distribution has the largest entropy of all distributions in Rn. Furthermore, coordinate directions are not distinguished in any way. Both makes the normal distribution a particularly attractive candidate for randomized search.

Randomized search algorithms are regarded to be robust in a rugged search landscape, which can comprise discontinuities, (sharp) ridges, or local optima. The covariance matrix adaptation (CMA) in particular is designed to tackle, additionally, ill-conditioned and nonseparable7 problems.

#### 0.4 Hessian and Covariance Matrices

We consider the convex-quadratic objective function fH : x  → 21xTHx, where the Hessian matrix H ∈ Rn×n is a positive deﬁnite matrix. Given a search distribution N (m,C), there is

a close relation between H and C: Setting C = H−1 on fH is equivalent to optimizing the isotropic function fsphere(x) = 21xTx = 12 i x2i (where H = I) with C = I.8 That is, on convex-quadratic objective functions, setting the covariance matrix of the search distribution to the inverse Hessian matrix is equivalent to rescaling the ellipsoid function into a spherical one. Consequently, we assume that the optimal covariance matrix equals to the inverse Hessian matrix, up to a constant factor.9 Furthermore, choosing a covariance matrix or choosing a respective afﬁne linear transformation of the search space (i.e. of x) is equivalent [14], because for any full rank n × n-matrix A we ﬁnd a positive deﬁnite Hessian such that 21(Ax)TAx =

- 1

- 2xTATAx = 12xTHx. The ﬁnal objective of covariance matrix adaptation is to closely approximate the contour


lines of the objective function f. On convex-quadratic functions this amounts to approximating the inverse Hessian matrix, similar to a quasi-Newton method.

In Fig. 1 the solid-line distribution in the right ﬁgure follows the objective function contours most suitably, and it is easy to foresee that it will aid to approach the optimum the most.

The condition number of a positive deﬁnite matrix A is deﬁned via the Euclidean norm: cond(A) def= A  ×  A−1 , where A = sup x =1 Ax . For a positive deﬁnite (Hessian or covariance) matrix A holds A = λmax and cond(A) = λ

λmin ≥ 1, where λmax and λmin are the largest and smallest eigenvalue of A.

max

- 7An n-dimensional separable problem can be solved by solving n 1-dimensional problems separately, which is a

far easier task.

- 8Also the initial mean value m has to be transformed accordingly. 9Even though there is good intuition and strong empirical evidence for this statement, a rigorous proof is missing.


### 1 Basic Equation: Sampling

In the CMA Evolution Strategy, a population of new search points (individuals, offspring) is generated by sampling a multivariate normal distribution.10 The basic equation for sampling the search points, for generation number g = 0,1,2,..., reads11

|x(kg+1) ∼ m(g) + σ(g)N 0,C(g) for k = 1,...,λ (5)|
|---|


where ∼ denotes the same distribution on the left and right side. N(0,C(g)) is a multivariate normal distribution with zero mean and covariance matrix C(g),

see Sect. 0.2. It holds m(g) + σ(g)N(0,C(g)) ∼ N m(g),(σ(g))2C(g) .

x(kg+1) ∈ Rn, k-th offspring (individual, search point) from generation g + 1. m(g) ∈ Rn, mean value of the search distribution at generation g.

σ(g) ∈ R>0, “overall” standard deviation, step-size, at generation g. C(g) ∈ Rn×n, covariance matrix at generation g. Up to the scalar factor σ(g)2, C(g) is the

covariance matrix of the search distribution.

λ ≥ 2, population size, sample size, number of offspring.

To deﬁne the complete iteration step, the remaining question is, how to calculate m(g+1), C(g+1), and σ(g+1) for the next generation g + 1. The next three sections will answer these questions, respectively. An algorithm summary with all parameter settings and MATLAB source code are given in Appendix A and C, respectively.

### 2 Selection and Recombination: Moving the Mean

The new mean m(g+1) of the search distribution is a weighted average of µ selected points from the sample x(1g+1),...,x(λg+1):

m(g+1) =

µ

wi x(i:gλ+1) (6)

i=1

µ

wi = 1, w1 ≥ w2 ≥ ··· ≥ wµ > 0 (7)

i=1

where

10Recall that, given all (co-)variances, the normal distribution has the largest entropy of all distributions in Rn. 11Framed equations belong to the ﬁnal algorithm of a CMA Evolution Strategy.

µ ≤ λ is the parent population size, i.e. the number of selected points. wi=1...µ ∈ R>0, positive weight coefﬁcients for recombination. For wi=1...µ = 1/µ, Equa-

tion (6) calculates the mean value of µ selected points.

x(i:gλ+1), i-th best individual out of x(1g+1),...,x(λg+1) from (5). The index i : λ denotes the

index of the i-th ranked individual and f(x(1:gλ+1)) ≤ f(x(2:gλ+1)) ≤ ··· ≤ f(x(λg:λ+1)), where f is the objective function to be minimized.

Equation (6) implements truncation selection by choosing µ < λ out of λ offspring points. Assigning different weights wi should also be interpreted as a selection mechanism. Equation (6) implements weighted intermediate recombination by taking µ > 1 individuals into account for a weighted average.

The measure12

2

( µi=1 |wi|)2 µ i=1 wi2

w 21 w 22

1

w 1 w 2

(8)

=

=

=

µeﬀ =

µ i=1 wi2

will be repeatedly used in the following and can be paraphrased as effective sample size of the selected samples or variance effective selection mass. From the deﬁnition of wi in (7) we derive 1 ≤ µeﬀ ≤ µ, and µeﬀ = µ for equal recombination weights, i.e. wi = 1/µ for all i = 1...µ.

The notion of µeﬀ with different recombination weights generalizes the notion of µ with equal recombination weights in several aspects. The number µ (with equal recombination weights) is the amount of information used, expressed as number of independent sources. Taking the weighted average of independent samples reduces the original variance by a factor of µ for equal weights and by a factor of µeﬀ for any weights, hence µeﬀ can be considered as the amount of used information. To keep the variance unchanged, the average must be multiplied by √µeﬀ. However, the optimal step-size (given µ < n) is proportional to µ [6, 33] for equal weights and proportional to 1.25 µeﬀ for optimal recombination weights [4], respectively, see also Section 4.

Usually, µeﬀ ≈ λ/4 indicates a reasonable setting of wi. A simple and reasonable setting is wi ∝ µ − i + 1, and µ ≈ λ/2, where µeﬀ ≈ 3λ/8.

The ﬁnal equation rewrites (6) as an update of m,

|m(g+1) = m(g) + cm<br><br>µ<br><br>i=1<br><br>wi (x(i:gλ+1) − m(g)) (9)|
|---|


where

cm is a learning rate, usually set to 1.13

Equation (9) generalizes (6). If cm µi=1 wi = 1, as it is the case with the default parameter setting (compare Table 1 in Appendix A), −m(g) cancels out m(g), and Equations (9) and (6)

are identical.

- 12Later, the vector w will have λ ≥ µ elements. Here, for computing the norm, we assume that any additional λ − µ elements are zero.
- 13In the literature the notation κ = 1/cm is also common and κ is used as multiplier in (5) instead of in (9).


Choosing cm < 1 can be advantageous on noisy functions. With optimal step-size we have roughly σ ∝ 1/cm, hence the “test steps” in (5) are in effect increased whereas the update step in (9) remains unchanged. However, too large test steps negatively impact the performance because the ranking indices i : λ are determined too far away from the (current) region of relevance. Arbitrary small test steps (when cm → ∞) work generally well, within the limits of numerical precision, on unimodal and noisefree functions [1, 11].

### 3 Adapting the Covariance Matrix

In this section, the update of the covariance matrix, C, is derived. We will start out estimating the covariance matrix from a single population of one generation (Sect. 3.1). For small populations this estimation is unreliable and an adaptation procedure has to be invented (rank-µupdate, Sect. 3.2). In the limit case only a single point can be used to update (adapt) the covariance matrix at each generation (rank-one-update, Sect. 3.3). This adaptation can be enhanced by exploiting dependencies between successive steps applying cumulation (Sect. 3.3.2). Finally we combine the rank-µ and rank-one updating methods (Sect. 3.4).

#### 3.1 Estimating the Covariance Matrix From Scratch

For the moment we assume that the population contains enough information to reliably estimate a covariance matrix from the population.14 For the sake of convenience we assume σ(g) = 1 (see (5)) in this section. For σ(g) = 1 the formulae hold except for a constant factor.

We can (re-)estimate the original covariance matrix C(g) using the sampled population from (5), x(1g+1) ...x(λg+1), via the empirical covariance matrix

 xi(g+1) −

 

 x(ig+1) −

 

T

λ

λ

λ

1 λ − 1

1 λ

1 λ

x(jg+1)

x(jg+1)

C(empg+1) =

. (10)

i=1

j=1

j=1

The empirical covariance matrix C(empg+1) is an unbiased estimator of C(g): assuming the x(ig+1),i = 1...λ, to be random variables (rather than a realized sample), we have that

- E C(empg+1) C(g) = C(g). Consider now a slightly different approach to get an estimator for C(g).


λ

T

1 λ

C(λg+1) =

x(ig+1) − m(g) x(ig+1) − m(g)

(11)

i=1

Also the matrix C(λg+1) is an unbiased estimator of C(g). The remarkable difference between (10) and (11) is the reference mean value. For C(empg+1) it is the mean of the actually realized sample. For C(λg+1) it is the true mean value, m(g), of the sampled distribution (see (5)). Therefore, the estimators C(empg+1) and C(λg+1) can be interpreted differently: while C(empg+1)

14To re-estimate the covariance matrix, C, from a N (0, I) distributed sample such that cond(C) < 10 a sample size λ ≥ 4n is needed, as can be observed in numerical experiments.

estimates the distribution variance within the sampled points, C(λg+1) estimates variances of sampled steps, x(ig+1) − m(g).

A minor difference between (10) and (11) is the different normalizations λ−11 versus λ1 , necessary to get an unbiased estimator in both cases. In (10) one degree of freedom is

already taken by the inner summand. In order to get a maximum likelihood estimator, in both cases λ1 must be used.

Equation (11) re-estimates the original covariance matrix. To “estimate” a “better” covariance matrix, the same, weighted selection mechanism as in (6) is used [21].

C(µg+1) =

µ

wi x(i:gλ+1) − m(g) x(i:gλ+1) − m(g)

i=1

T

(12)

The matrix C(µg+1)is an estimator for the distribution of selected steps, just as C(λg+1) is an estimator of the original distribution of steps before selection. Sampling from C(µg+1) tends to reproduce selected, i.e. successful steps, giving a justiﬁcation for what a “better” covariance matrix means.

Following [15], we compare (12) with the Estimation of Multivariate Normal Algorithm EMNAglobal [30, 31]. The covariance matrix in EMNAglobal reads, similar to (10),

C(EMNAg+1)

=

global

µ

1 µ

i=1

x(i:gλ+1) − m(g+1) x(i:gλ+1) − m(g+1)

T

, (13)

where m(g+1) = µ1 µi=1 xi(:gλ+1). Similarly, applying the so-called Cross-Entropy method to continuous domain optimization [34] yields the covariance matrix µ−µ1 C(EMNAg+1)

, i.e. the unbiased empirical covariance matrix of the µ best points. In both cases the subtle, but most important difference to (12) is, again, the choice of the reference mean value.15 Equation (13) estimates the variance within the selected population while (12) estimates selected steps. Equation (13) reveals always smaller variances than (12), because its reference mean value is the minimizer for the variances. Moreover, in most conceivable selection situations (13) decreases the variances compared to C(g).

global

Figure3 demonstrates the estimation results on a linear objective function for λ = 150, µ = 50, and wi = 1/µ. Equation (12) geometrically increases the expected variance in direction of the gradient (where the selection takes place, here the diagonal), given ordinary settings for parent number µ and recombination weights w1, . . . , wµ. Equation (13) always decreases the variance in gradient direction geometrically fast! Therefore, (13) is highly susceptible to premature convergence, in particular with small parent populations, where the population cannot be expected to bracket the optimum at any time. However, for large values of µ in large populations with large initial variances, the impact of the different reference mean value can become marginal.

In order to ensure with (5), (6), and (12), that C(µg+1) is a reliable estimator, the variance effective selection mass µeﬀ (cf. (8)) must be large enough: getting condition numbers (cf. Sect. 0.4) smaller than ten for C(µg) on fsphere(x) = ni=1 x2i, requires µeﬀ ≈ 10n. The next step is to circumvent this restriction on µeﬀ.

15Taking a weighted sum, µi=1 wi . . . , instead of the mean, µ1 µi=1 . . . , is an appealing, but less important, difference.

| |
|---|


| |
|---|


| |
|---|


| |
|---|


sampling estimation new distribution

C(µg+1)

C(EMNAg+1)

global

- Figure 3: Estimation of the covariance matrix on flinear(x) = − 2i=1 xi to be minimized. Contour lines (dotted) indicate that the strategy should move toward the upper right corner. Above: estimation of C(µg+1) according to (12), where wi = 1/µ. Below: estimation of


C(EMNAg+1)

according to (13). Left: sample of λ = 150 N (0,I) distributed points. Middle: the µ = 50 selected points (dots) determining the entries for the estimation equation (solid straight lines). Right: search distribution of the next generation (solid ellipsoids). Given wi = 1/µ, estimation via C(µg+1) increases the expected variance in gradient direction for all µ < λ/2, while estimation via C(EMNAg+1)

global

decreases this variance for any µ < λ geometrically fast

global

#### 3.2 Rank-µ-Update

To achieve fast search (opposite to more robust or more global search), e.g. competitive performance on fsphere : x  → x2i, the population size λ must be small. Because typically (and ideally) µeﬀ ≈ λ/4 also µeﬀ must be small and we may assume, e.g., µeﬀ ≤ 1 + lnn. Then, it is not possible to get a reliable estimator for a good covariance matrix from (12). As a remedy, information from previous generations is used additionally. For example, after a sufﬁcient number of generations, the mean of the estimated covariance matrices from all generations,

g

1 σ(i)2

1 g + 1

C(µi+1) (14)

C(g+1) =

i=0

becomes a reliable estimator for the selected steps. To make C(µg) from different generations comparable, the different σ(i) are incorporated. (Assuming σ(i) = 1, (14) resembles the covariance matrix from the Estimation of Multivariate Normal Algorithm EMNAi [31].)

In (14), all generation steps have the same weight. To assign recent generations a higher

weight, exponential smoothing is introduced. Choosing C(0) = I to be the unity matrix and a learning rate 0 < cµ ≤ 1, then C(g+1) reads

1 σ(g)2

C(µg+1)

C(g+1) = (1 − cµ)C(g) + cµ

µ

T

wi y(i:gλ+1)y(i:gλ+1)

= (1 − cµ)C(g) + cµ

, (15)

i=1

where

cµ ≤ 1 learning rate for updating the covariance matrix. For cµ = 1, no prior information is

(g)2 C(µg+1). For cµ = 0, no learning takes place and C(g+1) = C(0). Here, cµ ≈ min(1,µeﬀ/n2) is a reasonably choice.

retained and C(g+1) = σ 1

w1...µ ∈ R such that w1 ≥ ··· ≥ wµ > 0 and i wi = 1.

- y(i:gλ+1) = (x(i:gλ+1) − m(g))/σ(g).
- z(i:gλ+1) = C(g)−1/2y(i:gλ+1) is the mutation vector expressed in the unique coordinate system where the sampling is isotropic and the respective coordinate system transformation does not rotate the original principal axes of the distribution.


This covariance matrix update is called rank-µ-update [23], because the sum of outer products in (15) is of rank min(µ,n) with probability one (given µ non-zero weights). This sum can even consist of a single term, if µ = 1.

Finally, we generalize (15) to λ weight values which need neither sum to 1, nor be nonnegative anymore [28, 27],

λ

T

wiy(i:gλ+1)y(i:gλ+1)

C(g+1) = (1 − cµ wi)C(g) + cµ

i=1

λ

T

= C(g)1/2 I + cµ

− I C(g)1/2 ,

wi z(i:gλ+1)z(i:gλ+1)

i=1

(16)

where

w1...λ ∈ R such that w1 ≥ ··· ≥ wµ > 0 ≥ wµ+1 ≥ wλ, and usually µi=1 wi = 1 and λ i=1 wi ≈ 0.

wi = λi=1 wi

The second line of (16) expresses the update in the natural coordinate system, an idea already considered in [12]. The identity covariance matrix is updated and a coordinate system trans-

formation is applied afterwards by multiplication with C(g)1/2 on both sides. Equation (16) uses λ weights, wi, of which about half are negative. If the weights are chosen such that

wi = 0, the decay on C(g) disappears and changes are only made along axes in which samples are realized.

Negative values for the recombination weights in the covariance matrix update have been introduced in the seminal paper of Jastrebski and Arnold [28] as active covariance matrix adaptation. Non-equal negative weight values have been used in [27] together with a rather involved mechanism to make up for different vector lengths. The default recombination weights as deﬁned in Table 1 in Appendix A are somewhere in between these two proposals, but closer to [28]. Slightly deviating from (16) later on, vector lengths associated with negative weights will be rescaled to a (direction dependent) constant, see (46) and (47) in Appendix A. This allows to guaranty positive deﬁniteness of C(g+1). Conveniently, it also alleviates a selection error which usually makes directions associated with longer vectors worse.

The number 1/cµ is the backward time horizon that contributes roughly 63% of the overall information.

Because (16) expands to the weighted sum

C(g+1) = (1 − cµ)g+1C(0) + cµ

g

1 σ(i)2

(1 − cµ)g−i

i=0

###### C(µi+1) , (17)

the backward time horizon, ∆g, where about 63% of the overall weight is summed up, is deﬁned by

g

1 e

(1 − cµ)g−i ≈ 0.63 ≈ 1 −

. (18)

cµ

i=g+1−∆g

Resolving the sum yields

1 e

(1 − cµ)∆g ≈

, (19) and resolving for ∆g, using the Taylor approximation for ln, yields

1 cµ

∆g ≈

. (20)

That is, approximately 37% of the information in C(g+1) is older than 1/cµ generations, and, according to (19), the original weight is reduced by a factor of 0.37 after approximately 1/cµ generations.16

The choice of cµ is crucial. Small values lead to slow learning, too large values lead to a failure, because the covariance matrix degenerates. Fortunately, a good setting seems to be largely independent of the function to be optimized.17 A ﬁrst order approximation for a good choice is cµ ≈ µeﬀ/n2. Therefore, the characteristic time horizon for (16) is roughly n2/µeﬀ.

Experiments suggest that cµ ≈ µeﬀ/n2 is a rather conservative setting for large values of n, whereas µeﬀ/n1.5 appears to be slightly beyond the limit of stability. The best, yet robust choice of the exponent remains to be an open question.

Even for the learning rate cµ = 1, adapting the covariance matrix cannot be accomplished within one generation. The effect of the original sample distribution does not vanish until a sufﬁcient number of generations. Assuming ﬁxed search costs (number of function evaluations), a small population size λ allows a larger number of generations and therefore usually leads to a faster adaptation of the covariance matrix.

- 16This can be shown more easily, because (1 − cµ)g = exp ln(1 − cµ)g = exp(g ln(1 − cµ)) ≈ exp(−gcµ) for small cµ, and for g ≈ 1/cµ we get immediately (1 − cµ)g ≈ exp(−1).
- 17We use the sphere model fsphere(x) = i x2i to empirically ﬁnd a good setting for the parameter cµ, dependent on n and µeﬀ. The found setting was applicable to any non-noisy objective function we tried so far.


#### 3.3 Rank-One-Update

In Section 3.1 we started by estimating the complete covariance matrix from scratch, using all selected steps from a single generation. We now take an opposite viewpoint. We repeatedly update the covariance matrix in the generation sequence using a single selected step only. First, this perspective will give another justiﬁcation of the adaptation rule (16). Second, we will introduce the so-called evolution path that is ﬁnally used for a rank-one update of the covariance matrix.

##### 3.3.1 A Different Viewpoint

We consider a speciﬁc method to produce n-dimensional normal distributions with zero mean. Let the vectors y1,...,yg

0 ∈ Rn, g0 ≥ n, span Rn and let N (0,1) denote independent (0,1)normally distributed random numbers, then

g0

N (0,1)y1 + ··· + N (0,1)yg

0 ∼ N 0,

i=1

yiyTi (21)

is a normally distributed random vector with zero mean and covariance matrix gi=10 yiyTi . The random vector (21) is generated by adding “line-distributions” N (0,1)yi. The singular distribution N (0,1)yi ∼ N(0,yiyTi ) generates the vector yi with maximum likelihood considering all normal distributions with zero mean.

The line distribution that generates a vector y with the maximum likelihood must “live” on a line that includes y, and therefore the distribution must obey N(0, 1)σy ∼ N(0, σ2yyT). Any other line distribution with zero mean cannot generate y at all. Choosing σ reduces to choosing the maximum likelihood of y for the one-dimensional gaussian N(0, σ2 y 2), which is σ = 1.

The covariance matrix yyT has rank one, its only eigenvectors are {αy | α ∈ R\0} with eigenvalue y 2. Using equation (21), any normal distribution can be realized if yi are chosen appropriately. For example, (21) resembles (4) with m = 0, using the orthogonal eigenvectors yi = diibi, for i = 1, . . . , n, where bi are the columns of B. In general, the vectors yi need not to be eigenvectors of the covariance matrix, and they usually are not.

Considering (21) and a slight simpliﬁcation of (16), we try to gain insight into the adaptation rule for the covariance matrix. Let the sum in (16) consist of a single summand only (e.g. µ = 1), and let yg+1 = x

(g+1) 1:λ −m(g)

σ(g) . Then, the rank-one update for the covariance matrix reads

C(g+1) = (1 − c1)C(g) + c1 yg+1yg+1T (22)

The right summand is of rank one and adds the maximum likelihood term for yg+1 into the covariance matrix C(g). Therefore the probability to generate yg+1 in the next generation increases.

An example of the ﬁrst two iteration steps of (22) is shown in Figure 4. The distribution N(0,C(1)) tends to reproduce y1 with a larger probability than the initial distribution N(0,I); the distribution N(0,C(2)) tends to reproduce y2 with a larger probability than N(0,C(1)), and so forth. When y1,...,yg denote the formerly selected, favorable steps, N(0,C(g))

| |
|---|


| |
|---|


| |
|---|


###### N 0,C(0) N 0,C(1) N 0,C(2)

- Figure 4: Change of the distribution according to the covariance matrix update (22). Left:


vectors e1 and e2, and C(0) = I = e1eT1 + e2eT2. Middle: vectors 0.91e1, 0.91e2, and 0.41y1 (the coefﬁcients deduce from c1 = 0.17), and C(1) = (1 − c1)I + c1 y1yT1, where y1 = −−02..592 . The distribution ellipsoid is elongated into the direction of y1, and therefore increases the likelihood of y1. Right: C(2) = (1 − c1)C(1) + c1 y2yT2, where y2 = 01..975 .

tends to reproduce these steps. The process leads to an alignment of the search distribution N(0,C(g)) to the distribution of the selected steps. If both distributions become alike, as under random selection, in expectation no further change of the covariance matrix takes place [13].

##### 3.3.2 Cumulation: Utilizing the Evolution Path

We have used the selected steps, y(i:gλ+1) = (x(i:gλ+1) − m(g))/σ(g), to update the covariance matrix in (16) and (22). Because yyT = −y(−y)T, the sign of the steps is irrelevant for the

update of the covariance matrix—that is, the sign information is lost when calculating C(g+1). To reintroduce the sign information, a so-called evolution path is constructed [24, 26].

We call a sequence of successive steps, the strategy takes over a number of generations, an evolution path. An evolution path can be expressed by a sum of consecutive steps. This summation is referred to as cumulation. To construct an evolution path, the step-size σ is disregarded. For example, an evolution path of three steps of the distribution mean m can be constructed by the sum

m(g) − m(g−1)

m(g−1) − m(g−2)

m(g+1) − m(g) σ(g)

σ(g−2) . (23)

+

σ(g−1) +

In practice, to construct the evolution path, pc ∈ Rn, we use exponential smoothing as in (16), and start with p(0)c = 0.18

|p(cg+1) = (1 − cc)p(cg) + cc(2 − cc)µeﬀ<br><br>m(g+1) − m(g) cmσ(g)<br><br>(24)|
|---|


where

18In the ﬁnal algorithm (24) is still slightly modiﬁed, compare (45).

p(cg) ∈ Rn, evolution path at generation g. cc ≤ 1. Again, 1/cc is the backward time horizon of the evolution path pc that contains

roughly√n and 63%n is effective.of the overall weight (compare derivation of (20)). A time horizon between

The factor cc(2 − cc)µeﬀ is a normalization constant for pc. For cc = 1 and µeﬀ = 1, the factor reduces to one, and p(cg+1) = (x(1:gλ+1) − m(g))/σ(g).

The factor cc(2 − cc)µeﬀ is chosen, such that

pc(g+1) ∼ N (0, C) (25) if

x(i:gλ+1) − m(g)

p(cg) ∼

σ(g) ∼ N (0, C) for all i = 1, . . . , µ . (26) To derive (25) from (26) and (24) remark that

(1 − cc)2 + cc(2 − cc)2 = 1 and

µ

1 √µeﬀ N(0, C) . (27)

wiNi(0, C) ∼

i=1

The (rank-one) update of the covariance matrix C(g) via the evolution path p(cg+1) reads [24]

###### C(g+1) = (1 − c1)C(g) + c1p(cg+1)p(cg+1)T . (28)

An empirically validated choice for the learning rate in (28) is c1 ≈ 2/n2. For cc = 1 and µ = 1, Equations (28), (22), and (16) are identical.

Using the evolution path for the update of C is a signiﬁcant improvement of (16) for

small µeﬀ, because correlations between consecutive steps are heavily exploited. The leading signs of steps, and the dependencies between consecutive steps play a signiﬁcant role for the

resulting evolution path p(cg+1).

We consider the two most extreme situations, fully correlated steps and entirely anticorrelated steps. The summation in (24) reads for positive correlations

g

1 cc

(1 − cc)i →

i=0

and for negative correlations

(for g → ∞) ,

g

(−1)i(1 − cc)i =

i=0

=

= cc

→

(g−1)/2

g/2

(1 − cc)2i −

(1 − cc)2i+1

i=0

i=0

(g−1)/2

g/2

(1 − cc)2i − (1 − cc)

(1 − cc)2i

i=0

i=0

g/2

(1 − cc)2 i + (1 − cc)g((g + 1) mod 2)

i=0

- 1

- 2 − cc


cc 1 − (1 − cc)2

(for g → ∞) .

=

Multipling these by cc(2 − cc), which is applied to each input vector, we ﬁnd that the length of the evolution path is modulated by the factor of up to

2 − cc cc ≈

1 √cc

(29)

due to the positive correlations, or its inverse due to negative correlations, respectively [19, Equations (48) and (49)].

With √n ≤ 1/cc ≤ n/2 the number of function evaluations needed to adapt a nearly optimal covariance matrix on cigar-like objective functions becomes O(n), despite a learning rate of c1 ≈ 2/n2 [19]. A plausible interpretation of this effect is two-fold. First, the desired axis is represented in the path (much) more accurately than in single steps. Second, the learning rate c1 is modulated: the increased length of the evolution path as computed in (29) acts in effect similar to an increased learning rate by a factor of up to c−c 1/2.

As a last step, we combine (16) and (28).

- 3.4 Combining Rank-µ-Update and Cumulation The ﬁnal CMA update of the covariance matrix combines (16) and (28).


|C(g+1) = (1 − c1 − cµ wj<br><br>can be close or equal to 0<br><br>)C(g)<br><br>+ c1 p(cg+1)p(cg+1)T rank-one update<br><br>+ cµ<br><br>λ<br><br>i=1<br><br>wi y(i:gλ+1) y(i:gλ+1)<br><br>T<br><br>rank-µ update<br><br>(30)|
|---|


where c1 ≈ 2/n2. cµ ≈ min(µeﬀ/n2,1 − c1). y(i:gλ+1) = (x(i:gλ+1) − m(g))/σ(g).

wj = λi=1 wi ≈ −c1/cµ, but see also (53) and(46) in Appendix A.

Equation (30) reduces to (16) for c1 = 0 and to (28) for cµ = 0. The equation combines the advantages of (16) and (28). On the one hand, the information from the entire population is used efﬁciently by the so-called rank-µ update. On the other hand, information of correlations between generations is exploited by using the evolution path for the rank-one update. The former is important in large populations, the latter is particularly important in small populations.

### 4 Step-Size Control

The covariance matrix adaptation, discussed in the last section, does not explicitly control the “overall scale” of the distribution, the step-size. The covariance matrix adaptation increases or decreases the scale only in a single direction for each selected step—or it decreases the scale by fading out old information by a given, non-adaptive factor. Less informally, we have two speciﬁc reasons to introduce a step-size control in addition to the adaptation rule (30) for C(g).

- 1. The optimal overall step length cannot be well approximated by (30), in particular if µeﬀ is chosen larger than one.

For example, on fsphere(x) = ni=1 x2i, given C(g) = I and λ ≤ n, the optimal step-size σ equals approximately µ fsphere(x)/n with equal recombination weights [6, 33] and 1.25 µeﬀ fsphere(x)/n with optimal recombination weights [4].19 This dependency on µ or µeﬀ can not be realized by (16) or (30).

- 2. The largest reliable learning rate for the covariance matrix update in (30) is too slow to achieve competitive change rates for the overall step length.


To achieve optimal performance on fsphere with an Evolution Strategy with weighted recombination, the overall step length must decrease by a factor of about exp(0.25) ≈ 1.28 within n function evaluations, as can be derived from progress formulas as in [4] and [6, p.229]. That is, the time horizon for the step length change must be proportional to n or shorter. From the learning rates c1 and cµ in (30) follows that the adaptation is too slow to perform competitive on fsphere whenever µeﬀ n. This can be validated by simulations even for moderate dimensions, n ≥ 10, and small µeﬀ ≤ 1 + ln n.

To control the step-size σ(g) we utilize an evolution path, i.e. a sum of successive steps (see also Sect. 3.3.2). The method can be applied independently of the covariance matrix update and is denoted as cumulative path length control, cumulative step-size control, or cumulative step length adaptation (CSA). The length of an evolution path is exploited, based on the following reasoning, as depicted in Fig. 5.

- • Whenever the evolution path is short, single steps cancel each other out (Fig. 5, left). Loosely speaking, they are anti-correlated. If steps extinguish each other, the step-size should be decreased.
- • Whenever the evolution path is long, the single steps are pointing to similar directions (Fig. 5, right). Loosely speaking, they are correlated. Because the steps are similar, the same distance can be covered by fewer but longer steps into the same directions. In the limit case, when consecutive steps have identical direction, they can be replaced by any of the enlarged single step. Consequently, the step-size should be increased.
- • In the desired situation the steps are (approximately) perpendicular in expectation and therefore uncorrelated (Fig. 5, middle).


19Because recombination then reduces the size of the realized step by a factor of √µ or √µeﬀ (under random selection or in large dimension), the effective optimal steps are proportional to √µ or 1.25√µeﬀ, respectively.

| | | |
|---|---|---|


- Figure 5: Three evolution paths of respectively six steps from different selection situations (idealized). The lengths of the single steps are all comparable. The length of the evolution paths (sum of steps) is remarkably different and is exploited for step-size control


To decide whether the evolution path is “long” or “short”, we compare the length of the path with its expected length under random selection20, where consecutive steps are independent and therefore uncorrelated (uncorrelated steps are the desired situation). If selection biases the evolution path to be longer then expected, σ is increased, and, vice versa, if selection biases the evolution path to be shorter than expected, σ is decreased. In the ideal situation, selection does not bias the length of the evolution path and the length equals its expected length under random selection.

In practice, to construct the evolution path, pσ, the same techniques as in (24) are applied. In contrast to (24), a conjugate evolution path is constructed, because the expected length of the evolution path pc from (24) depends on its direction (compare (25)). Initialized with p(0)σ = 0, the conjugate evolution path reads

|p(σg+1) = (1 − cσ)p(σg) + cσ(2 − cσ)µeﬀ C(g)−<br><br>1<br><br>2<br><br><br>m(g+1) − m(g) cmσ(g)<br><br>(31)|
|---|


where p(σg) ∈ Rn is the conjugate evolution path at generation g. cσ < 1. Again, 1/cσ is the backward time horizon of the evolution path (compare (20)). For

small µeﬀ, a time horizon between √n and n is reasonable. cσ(2 − cσ)µeﬀ is a normalization constant, see (24).

- 1

- 2 def= B(g)D(g)−1B(g)T, where C(g) = B(g) D(g) 2 B(g)T is an eigendecompo-


C(g)−

sition of C(g), where B(g) is an orthonormal basis of eigenvectors, and the diagonal elements of the diagonal matrix D(g) are square roots of the corresponding positive eigenvalues (cf. Sect. 0.1).

20Random selection means that the index i : λ (compare (6)) is independent of the value of xi(:gλ+1) for all i = 1, . . . , λ, e.g. i : λ = i.

- 1

- 2 = I and (31) replicates (24). The transformation C(g)−


- 1

- 2


For C(g) = I, we have C(g)− re-scales the step m(g+1) − m(g) within the coordinate system given by B(g).

- 1

- 2 = B(g)D(g)−1B(g)T can be explained


The single factors of the transformation C(g)− as follows (from right to left):

B(g)T rotates the space such that the columns of B(g), i.e. the principal axes of the distribution N(0, C(g)), rotate into the coordinate axes. Elements of the resulting vector relate to projections onto the corresponding eigenvectors.

D(g)−1 applies a (re-)scaling such that all axes become equally sized. B(g) rotates the result back into the original coordinate system. This last transforma-

tion ensures that the principal axes of the distribution are not rotated by the overall transformation and directions of consecutive steps are comparable.

- 1

- 2 makes the expected length of p(σg+1) independent of


Consequently, the transformation C(g)− its direction, and for any sequence of realized covariance matrices C(gg=0) ,1,2,... we have under random selection p(σg+1) ∼ N (0,I), given p(0)σ ∼ N (0,I) [13].

To update σ(g), we “compare” p(σg+1) with its expected length E N (0,I) , that is

p(σg+1)

cσ dσ

lnσ(g+1) = lnσ(g) +

E N (0,I) − 1 , (32) where

dσ ≈ 1, damping parameter, scales the change magnitude of lnσ(g). The factor cσ/dσ/E N (0,I)

is based on in-depth investigations of the algorithm [13]. E N (0,I) = √2Γ(n+12 )/Γ(n2) ≈

√n + O(1/n), expectation of the Euclidean norm of a N (0,I) distributed random vector.

For p(σg+1) = E N (0,I) the second summand in (32) is zero, and σ(g) is unchanged, while σ(g) is increased for p(σg+1) > E N (0,I) , and σ(g) is decreased for p(σg+1) < E N (0,I) .

Alternatively, we might use the squared norm pσ(g+1) 2 in (32) and compare with its expected value n [5]. In this case (32) would read

cσ 2dσ

ln σ(g+1) = ln σ(g) +

p(σg+1) 2

n − 1 . (33)

This update performs rather similar to (32), while it presumable leads to faster step-size increments and slower step-size decrements.

The step-size change is unbiased on the log scale, because E lnσ(g+1) σ(g) = lnσ(g) for p(σg+1) ∼ N (0,I). The role of unbiasedness is discussed in Sect. 5. Equations (31) and (32) cause successive steps of the distribution mean m(g) to be approximately C(g)−1conjugate.

In order to show that successive steps are approximately C(g)−1-conjugate ﬁrst we remark that (31) and (32) adapt σ such that the length of pσ(g+1) equals approximately E N (0, I) . Starting from (E N (0, I) )2 ≈ p(σg+1) 2 = pσ(g+1)Tp(σg+1) = RHSTRHS of (31) and assuming that the expected squared length of C(g)−

- 1

- 2 (m(g+1) − m(g)) is unchanged by selection (unlike its direction) we get


- 1

- 2 (m(g+1) − m(g)) ≈ 0 , (34) and


p(σg)TC(g)−

T

- 1

- 2 pσ(g)


C(g)−1 m(g+1) − m(g) ≈ 0 . (35)

C(g)

- 1

- 2 (m(g+1) − m(g)) ≈ 0


Given 1/(c1 + cµ) 1 and (34) we assume also p(σg−1)TC(g)− and derive

T

C(g)−1 m(g+1) − m(g) ≈ 0 . (36) That is, the steps taken by the distribution mean become approximately C(g)−1-conjugate.

m(g) − m(g−1)

Because σ(g) > 0, (32) is equivalent to

|σ(g+1) = σ(g) exp<br><br>cσ dσ<br><br>p(σg+1)<br><br>E N (0,I) − 1 (37)|
|---|


The length of the evolution path is an intuitive and empirically well validated goodness measure for the overall step length. For µeﬀ > 1 it is the best measure to our knowledge.21 Nevertheless, it fails to adapt nearly optimal step-sizes on very noisy objective functions [7].

### 5 Discussion

The CMA-ES is an attractive option for non-linear optimization, if “classical” search methods, e.g. quasi-Newton methods (BFGS) and/or conjugate gradient methods, fail due to a non-convex or rugged search landscape (e.g. sharp bends, discontinuities, outliers, noise, and local optima). Learning the covariance matrix in the CMA-ES is analogous to learning the inverse Hessian matrix in a quasi-Newton method. In the end, any convex-quadratic (ellipsoid) objective function is transformed into the spherical function fsphere. This can reduce the number of f-evaluations needed to reach a target f-value on ill-conditioned and/or non-separable problems by orders of magnitude.

The CMA-ES overcomes typical problems that are often associated with evolutionary algorithms.

1. Poor performance on badly scaled and/or highly non-separable objective functions. Equation (30) adapts the search distribution to badly scaled and non-separable problems.

21Recently, two-point adaptation has shown to achieve similar performance [20].

- 2. The inherent need to use large population sizes. A typical, however intricate to diagnose reason for the failure of population based search algorithms is the degeneration of the population into a subspace.22 This is usually prevented by non-adaptive components in the algorithm and/or by a large population size (considerably larger than the problem dimension). In the CMA-ES, the population size can be freely chosen, because the

learning rates c1 and cµ in (30) prevent the degeneration even for small population sizes, e.g. λ = 9. Small population sizes usually lead to faster convergence, large population sizes help to avoid local optima.

- 3. Premature convergence of the population. Step-size control in (37) prevents the population to converge prematurely. It does not prevent the search to end up in a local optimum.


Therefore, the CMA-ES is highly competitive on a considerable number of test functions [13, 21, 23, 25, 26] and was successfully applied to many real world problems.23

Finally, we discuss a few basic design principles that were applied in the previous sections.

Change rates We refer to a change rate as the expected parameter change per sampled search point, given a certain selection situation. To achieve competitive performance on a wide range of objective functions, the possible change rates of the adaptive parameters need to be adjusted carefully. The CMA-ES separately controls change rates for the mean value of the distribution, m, the covariance matrix, C, and the step-size, σ.

- • The change rate for the mean value m, relative to the given sample distribution, is determined by cm, and by the parent number and the recombination weights. The larger µeﬀ, the smaller is the possible change rate of m.24 Similar holds for most evolutionary algorithms.
- • The change rate of the covariance matrix C is explicitly controlled by the learning rates

c1 and cµ and therefore detached from parent number and population size. The learning rate reﬂects the model complexity. In evolutionary algorithms, the explicit control of change rates of the covariances, independently of population size and mean change, is a rather unique feature.

- • The change rate of the step-size σ is explicitly controlled by the damping parameter dσ and is in particular independent from the change rate of C. The time constant 1/cσ ≤ n ensures a sufﬁciently fast change of the overall step length in particular with small population sizes.


- 22The same problem can be observed with the downhill simplex method [32] in dimension, say, larger than ten.
- 23The author stopped to maintain the growing list of (at the time 120) published references to applications in 2009. 24Given λ n, then the mean change per generation is roughly proportional to σ/√µeﬀ, while the optimal


step-size σ is roughly proportional to µeﬀ. Therefore, the net change with optimal step-size is proportional to √µeﬀ per generation. Now considering the effect on the resulting convergence rate, a closer approximation of the gradient

adds another factor of √µeﬀ, such that the generational progress rate is proportional to µeﬀ. Given λ/µeﬀ ≈ 4, we have the remarkable result that the convergence rate per f-evaluation is roughly independent of λ.

Invariance Invariance properties of a search algorithm denote identical behavior on a set, or a class of objective functions. Invariance is an important property of the CMA-ES.25 Translation invariance should be taken for granted in continuous domain optimization. Translation invariance means that the search behavior on the function x  → f(x + a), x(0) = b − a, is independent of a ∈ Rn. Further invariances, e.g. invariance to certain linear transformations of the search space, are highly desirable: they imply uniform performance on classes of functions26 and therefore allow for generalization of empirical results. In addition to translation invariance, the CMA-ES exhibits the following invariances.

- • Invariance to order preserving (i.e. strictly monotonic) transformations of the objective function value. The algorithm only depends on the ranking of function values.
- • Invariance to angle preserving (rigid) transformations of the search space (rotation, reﬂection, and translation) if the initial search point is transformed accordingly.
- • Scale invariance if the initial scaling, e.g. σ(0), and the initial search point, m(0), are chosen accordingly.
- • Invariance to a scaling of variables (diagonal invariance) if the initial diagonal covariance matrix C(0), and the initial search point, m(0), are chosen accordingly.
- • Invariance to any invertible linear transformation of the search space, A, if the initial covariance matrix C(0) = A−1 A−1 T, and the initial search point, m(0), are transformed accordingly. Together with translation invariance, this can also be referred to as afﬁne invariance, i.e. invariance to afﬁne search space transformations.


Invariance should be a fundamental design criterion for any search algorithm. Together with the ability to efﬁciently adapt the invariance governing parameters, invariance is a key to competitive performance.

Stationarity or Unbiasedness An important design criterion for a randomized search procedure is unbiasedness of variations of object and strategy parameters [8, 26]. Consider random selection, e.g. the objective function f(x) = rand to be independent of x. Then the population mean is unbiased if its expected value remains unchanged in the next generation, that is E m(g+1) m(g) = m(g). For the population mean, stationarity under random selection is a rather intuitive concept. In the CMA-ES, stationarity is respected for all parameters that appear in the basic equation (5). The distribution mean m, the covariance matrix C, and lnσ are unbiased. Unbiasedness of lnσ does not imply that σ is unbiased. Under random selection, E σ(g+1) σ(g) > σ(g), compare (32).27

For distribution variances (or step-sizes) a bias toward increase or decrease entails the risk of divergence or premature convergence, respectively, whenever the selection pressure is low or when no improvements are observed. On noisy problems, a properly controlled bias towards increase can be appropriate. It has the non-negligible disadvantage that the decision for termination becomes more difﬁcult.

25Special acknowledgments to Iv´an Santib´a¯nez-Koref for pointing this out to me. 26However, most invariances are linked to a state space transformation. Therefore, uniform performance is only

observed after the state of the algorithm has been adapted.

27Alternatively, if (37) were designed to be unbiased for σ(g+1), this would imply that E ln σ(g+1) σ(g) < ln σ(g), in our opinion a less desirable alternative.

### Acknowledgments

The author wishes to gratefully thank Anne Auger, Christian Igel, Stefan Kern, and Fabrice Marchal for the many valuable comments on the manuscript.

### References

- [1] Akimoto Y, Auger A, Hansen N. Quality gain analysis of the weighted recombination evolution strategy on general convex quadratic functions. In Proceedings of the 14th ACM/SIGEVO Conference on Foundations of Genetic Algorithms (FOGA ’17), pages 111–126. ACM, New York, NY, USA, 2017.
- [2] Akimoto Y, Hansen N. Diagonal acceleration for covariance matrix adaptation evolution strategies. Evolutionary computation, 28(3):405–435, 2020.
- [3] Auger A, Hansen N. A restart CMA evolution strategy with increasing population size. In Proceedings of the IEEE Congress on Evolutionary Computation, 2005.
- [4] Arnold DV. Weighted multirecombination evolution strategies. Theoretical computer science, 361.1:18–37, 2006.
- [5] Arnold DV, Beyer HG. Performance analysis of evolutionary optimization with cumulative step length adaptation. IEEE Transactions on Automatic Control, 49(4):617–622, 2004.
- [6] Beyer HG. The Theory of Evolution Strategies. Springer, Berlin, 2001.
- [7] Beyer HG, Arnold DV. Qualms regarding the optimality of cumulative path length control in CSA/CMA-evolution strategies. Evolutionary Computation, 11(1):19–28, 2003.
- [8] Beyer HG, Deb K. On self-adaptive features in real-parameter evolutionary algorithms. IEEE Transactions on Evolutionary Computation, 5(3):250–270, 2001.
- [9] Collange G, Delattre N, Hansen N, Quinquis I, Schoenauer M. Multidisciplinary optimisation in the design of future space launchers. In Breitkopf and Coelho, editors, Multidisciplinary Design Optimization in Computational Mechanics, chapter 12, pages 487–496. Wiley, 2010.
- [10] Dufoss´e P, Hansen N. Augmented Lagrangian, penalty techniques and surrogate modeling for constrained optimization with CMA-ES. In Proceedings of the Genetic and Evolutionary Computation Conference (GECCO ’21), pages 519–527, 2021.
- [11] Gissler A, Auger A, Hansen N. Learning rate adaptation by line search in evolution strategies with recombination. In Proceedings of the Genetic and Evolutionary Computation Conference (GECCO ’22), pages 630–638. ACM, New York, NY, USA, 2022.
- [12] Glasmachers T, Schaul T, Yi S, Wierstra D, Schmidhuber J. Exponential natural evolution strategies. In Proceedings of the 12th annual Genetic and Evolutionary Computation Conference, GECCO, pages 393–400. ACM, 2010.


- [13] Hansen N. Verallgemeinerte individuelle Schrittweitenregelung in der Evolutionsstrategie. Mensch und Buch Verlag, Berlin, 1998.
- [14] Hansen N. Invariance, self-adaptation and correlated mutations in evolution strategies. In Schoenauer M, Deb K, Rudolph G, Yao X, Lutton E, Merelo JJ, Schwefel HP, editors, Parallel Problem Solving from Nature - PPSN VI, pages 355–364. Springer, 2000.
- [15] Hansen N. The CMA evolution strategy: a comparing review. In Lozano JA, Larranaga P, Inza I, and Bengoetxea E, editors, Towards a new evolutionary computation. Advances on estimation of distribution algorithms, pages 75–102. Springer, 2006.
- [16] Hansen N. Benchmarking a BI-Population CMA-ES on the BBOB-2009 Function Testbed. In the workshop Proceedings of the Genetic and Evolutionary Computation Conference, GECCO, pages 2389–2395. ACM, 2009.
- [17] Hansen N. Variable Metrics in Evolutionary Computation. Habilitation a` diriger des recherches, Universit´e Paris-Sud, 2010.
- [18] Hansen N. Injecting External Solutions Into CMA-ES. CoRR, arXiv:1110.4181, 2011.
- [19] Hansen N, Auger A. Principled design of continuous stochastic search: From theory to practice. In Y Borenstein and A Moraglio, eds.: Theory and Principled Methods for Designing Metaheustics. Springer, pages 145–180, 2014.
- [20] Hansen N, Atamna A, Auger A. How to Assess Step-Size Adaptation Mechanisms in Randomised Search. In Parallel Problem Solving from Nature – PPSN XIII, pages 60–69. Springer, 2014.
- [21] Hansen N, Kern S. Evaluating the CMA evolution strategy on multimodal test functions. In Xin Yao et al., editors, Parallel Problem Solving from Nature – PPSN VIII, pages 282–291. Springer, 2004.
- [22] Hansen N, Niederberger SPN, Guzzella L, Koumoutsakos P. A method for handling uncertainty in evolutionary optimization with an application to feedback control of combustion. IEEE Transactions on Evolutionary Computation, 13(1):180–197, 2009.
- [23] Hansen N, M¨uller SD, Koumoutsakos P. Reducing the time complexity of the derandomized evolution strategy with covariance matrix adaptation (CMA-ES). Evolutionary Computation, 11(1):1–18, 2003.
- [24] Hansen N, Ostermeier A. Adapting arbitrary normal mutation distributions in evolution strategies: The covariance matrix adaptation. In Proceedings of the 1996 IEEE Conference on Evolutionary Computation (ICEC ’96), pages 312–317, 1996.
- [25] Hansen N, Ostermeier A. Convergence properties of evolution strategies with the deran-

domized covariance matrix adaptation: The (µ/µI,λ)-CMA-ES. In Proceedings of the 5th European Congress on Intelligent Techniques and Soft Computing, pages 650–654, 1997.

- [26] Hansen N, Ostermeier A. Completely derandomized self-adaptation in evolution strategies. Evolutionary Computation, 9(2):159–195, 2001.


- [27] Hansen N, Ros R. Benchmarking a weighted negative covariance matrix update on the BBOB-2010 noiseless testbed. In Proceedings companion of the 12th annual Genetic and Evolutionary Computation Conference, GECCO, pages 1673–1680. ACM, 2010.
- [28] Jastrebski G, Arnold DV. Improving evolution strategies through active covariance matrix adaptation. In Proceedings of the 2006 IEEE Congress on Evolutionary Computation, CEC, pages 2814–2821. IEEE, 2006.
- [29] Kern S, M¨uller SD, Hansen N, B¨uche D, Ocenasek J, Koumoutsakos P. Learning probability distributions in continuous evolutionary algorithms – a comparative review. Natural Computing, 3:77–112, 2004.
- [30] Larra˜naga P. A review on estimation of distribution algorithms. In P. Larra˜naga and J. A. Lozano, editors, Estimation of Distribution Algorithms, pages 80–90. Kluwer Academic Publishers, 2002.
- [31] Larra˜naga P, Lozano JA, Bengoetxea E. Estimation of distribution algorithms based on multivariate normal and Gaussian networks. Technical report, Dept. of Computer Science and Artiﬁcial Intelligence, University of the Basque Country, 2001. KZAA-IK1-01.
- [32] Nelder JA, Mead R. A simplex method for function minimization. The Computer Journal 7.4:308-313, 1965.
- [33] Rechenberg I. Evolutionsstrategie ’94. Frommann-Holzboog, Stuttgart, Germany, 1994.
- [34] Rubenstein RY, Kroese DP. The Cross-Entropy Method: a uniﬁed approach to combinatorial optimization, Monte-Carlo simulation, and machine learning. Springer, 2004.
- [35] Suttorp T, Hansen N, Igel C. Efﬁcient Covariance Matrix Update for Variable Metric Evolution Strategies. Machine Learning 75(2): 167–197, 2009.


### A Algorithm Summary: The (µ/µW,λ)-CMA-ES

- Figure 6 outlines the complete algorithm28, summarizing (5), (9), (24), (30), (31), and (37). Used symbols, in order of appearance, are:


yk ∼ N (0,C), for k = 1,...,λ, are realizations from a multivariate normal distribution

with zero mean and covariance matrix C.

B,D result from an eigendecomposition of the covariance matrix C with C = BD2BT = BDDBT (cf. Sect. 0.1). Columns of B are an orthonormal basis of eigenvectors. Diagonal elements of the diagonal matrix D are square roots of the corresponding positive eigenvalues. While (39) can certainly be implemented using a Cholesky decomposition of C, the eigendecomposition is needed to correctly compute C−21 = BD−1BT for (43) and (46).

xk ∈ Rn, for k = 1,...,λ. Sample of λ search points.

y w = µi=1 wi yi:λ, step of the distribution mean disregarding step-size σ. yi:λ = (xi:λ − m)/σ, see xi:λ below. xi:λ ∈ Rn, i-th best point out of x1,...,xλ from (40). The index i : λ denotes the index of

the i-th ranked point, that is f(x1:λ) ≤ f(x2:λ) ≤ ··· ≤ f(xλ:λ).

µ = |{wi |wi > 0}| = λi=1 1(0,inf)(wi) ≥ 1 is the number of strictly positive recombina-

tion weights.

µeﬀ = µi=1 wi2 −1 is the variance effective selection mass, see (8). Because µi=1 |wi| =

1, we have 1 ≤ µeﬀ ≤ µ. C−

- 1

- 2 def= BD−1BT, see B,D above. The matrix D can be inverted by inverting its diagonal elements. From the deﬁnitions we ﬁnd that C− B µi=1 wi zi:λ.


- 1

- 2 y w =


- 1

- 2yi = Bzi, and C−


E N (0,I) = √2Γ(n+12 )/Γ(n2) ≈

√n 1 − 41n + 211n2 . hσ =

1 if p

< (1.4 + n+12 )E N (0,I) 0 otherwise

√

σ

, where g is the generation

1−(1−cσ)2(g+1)

number. The Heaviside function hσ stalls the update of pc in (45) if pσ is large. This prevents a too fast increase of axes of C in a linear surrounding, i.e. when the step-size is far too small. This is useful when the initial step-size is chosen far too small or when the objective function changes in time.

δ(hσ) = (1 − hσ)cc(2 − cc) ≤ 1 is of minor relevance. In the (unusual) case of hσ = 0, it

substitutes for the second summand from (45) in (47).

wj = λi=1 wi is the sum of the recombination weights, see (49)–(53). We have −c1/cµ ≤

wj ≤ 1 and for the default population size λ, we meet the lower bound cµ wj = −c1.

28With negative recombination weights in the covariance matrix, chosen here by default, the algorithm is sometimes denoted as aCMA-ES for active CMA [28].

||Set parameters<br><br>Set parameters λ, wi=1...λ, cm, cσ, dσ, cc, c1, and cµ according to Table 1.<br><br>Initialization Set evolution paths pσ = 0, pc = 0, covariance matrix C = I, and g = 0. Choose distribution mean m ∈ Rn and step-size σ ∈ R>0 problem dependent.1<br><br>Until termination criterion met, g ← g + 1<br><br>Sample new population of search points, for k = 1,...,λ<br><br>zk ∼ N (0,I) (38) yk = BDzk ∼ N (0,C) (39) xk = m + σyk ∼ N m,σ2C (40)<br><br>Selection and recombination<br><br>y w =<br><br>µ<br><br>i=1<br><br>wi yi:λ where<br><br>µ<br><br>i=1<br><br>wi = 1, wi > 0 for i = 1...µ (41)<br><br>m ← m + cmσ y w equals<br><br>µ<br><br>i=1<br><br>wi xi:λ if cm = 1 (42)<br><br>Step-size control<br><br>pσ ← (1 − cσ)pσ + cσ(2 − cσ)µeﬀ C−<br><br>1<br><br>2 y w (43)<br><br><br>σ ← σ × exp<br><br>cσ dσ<br><br>pσ<br><br>E N (0,I) − 1 (44) Covariance matrix adaptation<br><br>pc ← (1 − cc)pc + hσ cc(2 − cc)µeﬀ y w (45) wi◦ = wi × (1 if wi ≥ 0 else n/ C−<br><br>1<br><br>2 yi:λ 2) (46)<br><br><br>C ← (1 + c1δ(hσ) − c1 − cµ wj<br><br>usually equals to 0<br><br>)C + c1pcpTc + cµ<br><br>λ<br><br>i=1<br><br>wi◦ yi:λyTi:λ (47)<br><br>1The optimum should presumably be within the initial cube m ± 3σ(1, . . . , 1)T. If the optimum is expected to be in the initial search interval [a, b]n we may choose the initial search point, m, uniformly randomly in [a, b]n, and σ = 0.3(b − a). Different search intervals ∆si for different variables can be reﬂected by a different initialization of C, in that the diagonal elements of C obey cii = (∆si)2. However, the ∆si should not disagree by several orders of magnitude. Otherwise a scaling of the variables should be applied.|
|---|
|
|---|


###### Figure 6: The (µ/µW,λ)-CMA Evolution Strategy. Symbols: see text

Default Parameters The (external) strategy parameters are λ, wi=1...λ, cm, cσ, dσ, cc, c1, and cµ. Default strategy parameter values are given in Table 1. An in-depth discussion of most parameters is given in [26].

The given setting for the default negative weights was introduced in 2016. The setting is somewhere between uniform weights [28] and mirrors of the positive weight values [4, 27]. The choice is a compromise between avoiding increasingly large negative values which lead to a large variance reduction in a single direction in C while still giving emphasis on the selection differences in particular for weights close to the median rank. We attempt to scale all negative weights such that the factor in front of C in (47) becomes 1. That is, we have by default no decay on C and the variance added to the covariance matrix by the positive updates equals, in expectation, to the variance removed by the negative updates.

Speciﬁcally, we want to achieve c1 + cµ wj = 0, that is

c1 = −cµ wj c1/cµ = − |wj|+ − |wj|− c1/cµ = −1 + |wj|−

1 + c1/cµ = |wj|− ,

hence the multiplier αµ− in (53) is set to 1 + c1/cµ. Choosing |wj|− in the order of 1 is only viable if µeﬀ µ−eﬀ = λi=µ+1 wi

2

/ λi=µ+1 wi2,

that is, if the variance effective update information from positive weights, µeﬀ, is not much larger than that from negative weights, µ−eﬀ. In the default setting, µ−eﬀ is about 1.2 to 1.5 times larger than µeﬀ, because the curve wi versus i ﬂattens out for increasing i. In (53) we use the bound αµ−eff, see (51), to (i) get a meaningful value for any choices of w i, and (ii) preserve the effect from letting cµ go to zero (eventually turning off the covariance matrix adaptation entirely).

The apparent circular dependency between wi, αµ−, cµ, µeﬀ, and again wi can be resolved: the variance effective selection mass µeﬀ depends only on the relative relation between the positive weights, such that µeﬀ(w1...λ) = µeﬀ(w1...µ) = ( µi=1 wi)2/ µi=1 wi2 =

µeﬀ(w 1...µ). That is, µeﬀ and µ−eﬀ can be computed already from w i of (49), from which cµ can be computed, from which αµ− can be computed, from which the remaining negative weights wi can be computed.

Finally, we also bound the negative weights via (53) to guaranty positive deﬁniteness of C via (46), thereby, possibly, re-introducing a decay on C. With the default setting for population size λ and the default raw weight values, αpos def− in Equation (53) leaves the weights unchanged.

Speciﬁcally, to guaranty positive deﬁniteness of the covariance matrix, we can bound the maximal variance subtracted in a single direction by the variance remaining after the decay on C is applied in (47), disregarding any added variance (worst case). Deﬁning

|wi|− = λi=µ+1 |wi| to be the sum of the absolute values of all negative weights, and assuming a (Mahalanobis-)variance of n from each negative summand of the weighted sum in (47), we require

###### ncµ |wi|− < 1 − c1 − wjcµ = 1 − c1 − cµ + cµ |wi|− . (59)

µ i=1 w i)2 µ i=1 wi 2 ∈

Table 1: Default Parameters (in 2016), where µ = |{wi > 0}| = λ/2 , µeﬀ = (

λ i=µ+1 w i)2 λ i=µ+1 wi 2 , µi=1 wi = 1, and |wj|+ is the sum of all positive, and

[1,µ], µ−eﬀ = (

− |wj|− the sum of all negative wj-values, i.e., αµ− = |w j|− ≥ 0. Apart from wi for i > µ, all parameters are taken from [16] with only minor modiﬁcations

|Selection and Recombination:<br><br>λ = 4 + 3 lnn can be increased (48)<br><br>w i = ln<br><br>λ + 1 2 − lni for i = 1,...,λ preliminary convex shape (49)<br><br>αµ− = 1 + c1/cµ let c1 + cµ wi = c1 + cµ − cµ |wi|− be 0 (50) αµ−<br><br>eff<br><br>= 1 +<br><br>2µ−eﬀ µeﬀ + 2<br><br>bound |wi|− to be compliant with cµ(µeﬀ) (51)<br><br>αpos def− =<br><br>1 − c1 − cµ ncµ<br><br>bound |wi|− to guaranty positive deﬁniteness<br><br>(52)<br><br>wi =<br><br> <br><br><br><br>1 |w j|+<br><br>w i if w i ≥ 0 positive weights sum to one min(αµ−,αµ−<br><br>eff<br><br>,αpos def− ) |w j|−<br><br>w i if w i < 0<br><br>negative weights usually sum to −αµ−<br><br>(53)<br><br>cm = 1 (54) Step-size control:<br><br>cσ =<br><br>µeﬀ + 2 n + µeﬀ + 5<br><br>dσ = 1 + 2 max 0,<br><br>µeﬀ − 1 n + 1 − 1 + cσ<br><br>(55)<br><br>Covariance matrix adaptation:<br><br>cc =<br><br>4 + µeﬀ/n n + 4 + 2µeﬀ/n<br><br>(56)<br><br>c1 =<br><br>αcov (n + 1.3)2 + µeﬀ<br><br>with αcov = 2 (57)<br><br>cµ = min 1 − c1,αcov<br><br>1/4 + µeﬀ + 1/µeﬀ − 2 (n + 2)2 + αcovµeﬀ/2<br><br>with αcov = 2 (58)|
|---|


Solving for |wi|− yields

1 − c1 − cµ (n − 1)cµ

|wi|− <

. (60)

###### We use min(. . . , 1−ncc1−cµ

) as multiplier for setting wi=µ+1...λ in (53) and normalize

µ

the variance from each respective summand yi:λyTi:λ via (46) to n, thereby bounding the variance reduction from negative weight values to the factor n−1

n .

- A Python implementation of the slightly intricate computation of the weights (49)–(53) can be found here.

The cumulation parameter cc for (56) is chosen ∝ 1/n. For learning a single direction in (almost) linear time, the setting cc ∝ 1/√n seems sufﬁcient [19]. Larger values are in general more robust to avoid feedback oscillations or instabilities and might allow for more freedom in the setting of c1. However, on the cigar function the relationship between cc times dimension (cc × n) and the evaluations divided by dimension to reach a given target becomes perfectly invariant with increasing dimension.29

Adopting a technique from [35, Eq. (11)], a generalized setting reads

cc =

αc(n) + (µeﬀ/n)β

c

nβc + αc(n) + 2(µeﬀ/n)βc

. (61)

With αc(n) = 101−n

−1/3

and βc = 1, the setting is slightly more robust in larger dimension but remains invariant, see Figure 7. When not all parameters of C are subject to adaptation and 1/c1 = o(n1.5), we suspect that βc < 1 is the reasonable choice. The last summand of the denominator of (61) is chosen such that cc approaches 1/2 when µeﬀ/n approaches inﬁnity.

Similarly, the second summand of the denominator of (58), αcovµeﬀ/2, is chosen such that cµ approaches one when αcovµeﬀ approaches 2 = 2/(2 − 1) times the ﬁrst summand.

Another technique, namely setting parameters depending on the degrees of freedom is developed in [2].

The default parameters of (53)–(58) are in particular chosen to be a robust setting and therefore, to our experience, applicable to a wide range of functions to be optimized. We do not recommend to change this setting, apart from increasing the population size λ in (48),30 and possibly decreasing αcov on noisy functions. If the λ-dependent default values for wi are used as given, the population size λ has a signiﬁcant inﬂuence on the global search performance [21]. Increasing λ usually improves the global search capability and the robustness of the CMA-ES, at the price of a reduced convergence speed. The convergence speed (per function evaluation) decreases at most linearly with λ. Independent restarts with increasing population size [3], automated or manually conducted, are a useful policy to perform well on most problems.

- B Implementational Concerns


We discuss a few implementational questions.

- 29This invariance remains almost perfect when the learning rates c1 and cµ are chosen ∝ n−1.5 instead of ∝ n−2 (∝ n−1.5 is however not a reliable setting). It changes to about cc × n1/2 when only the diagonal elements of the covariance matrix are adapted with a learning rate of ∝ 1/n.
- 30Decreasing λ is not recommended. Too small values have strong adverse effects on the performance.


0.6

n = 5

0.4

n = 10 n = 25 n = 100

recombinationweight

0.2

0.0

17, − 0. 28

0.2

13, − 0. 42

0.4

10, − 0. 63

0.6

8, − 0. 95

0.8

0 2 4 6 8 10 12 14 16 18 index

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |


- 100
- 101
- 102


1/cc

100 101 102 103 dimension

- Figure 7: Left: recombination weights from (53) in Table 1 for n = 5,10,25,100. Also given are the (default) population size λ (corresponding to the last index) and the sum of


weights. Positive weights sum to one. Right: backward time horizon 1/cc according to (56) (blue) and (61) (green), and n/4 and √n (both dashed) plotted against dimension n. The blue line is above the green line by a factor of about 1.5,2,2.5 = 10/4 for n = 100,1000,∞, respectively.

#### B.1 Multivariate normal distribution

Let the vector z ∼ N (0,I) have independent, (0,1)-normally distributed components that can easily be sampled on a computer. To generate a random vector y ∼ N(0,C) for (39), we set y = BDz (see above symbol descriptions of B and D and Sects. 0.1 and 0.2, and compare lines 52–53 and 83–84 in the source code below). Given yk = BDzk and C−12 = BD−1BT we have C−12 y w = B µi=1 wi zi:λ (compare (43) and lines 61 and 64 in the source code below).

#### B.2 Strategy internal numerical effort

In practice, the re-calculation of B and D needs to be done not until about max(1, 1/(10n(c1+

cµ)) ) generations. For reasonable c1 + cµ values, this reduces the numerical effort due to the eigendecomposition from O(n3) to O(n2) per generated search point, that is the effort of a matrix vector multiplication.

On a Pentium 4, 2.5 GHz processor the overall strategy internal time consumption is roughly 3 × (n + 5)2 × 10−8 seconds per function evaluation [29].

Remark that it is not sufﬁcient to compute a Cholesky decomposition of C, because then

(43) cannot be computed correctly.

#### B.3 Termination criteria

In general, the algorithm should be stopped whenever it becomes a waste of CPU-time to continue, and it would be better to restart (eventually with increased population size [3]) or to reconsidering the encoding and/or objective function formulation. We recommend the following termination criteria [3, 16] that are mostly related to numerical stability:

- • NoEffectAxis: stop if adding a 0.1-standard deviation vector in any principal axis direction of C does not change m.31
- • NoEffectCoord: stop if adding 0.2-standard deviations in any single coordinate does not change m (i.e. mi equals mi + 0.2σci,i for any i).
- • ConditionCov: stop if the condition number of the covariance matrix exceeds 1014.
- • EqualFunValues: stop if the range of the best objective function values of the last 10 + 30n/λ generations is zero.
- • Stagnation: we track a history of the best and the median ﬁtness in each iteration over the last 20% but at least 120+30n/λ and no more than 20000 iterations. We stop, if in both histories the median of the last (most recent) 30% values is not better than the median of the ﬁrst 30%.
- • TolXUp: stop if σ×max(diag(D)) increased by more than 104. This usually indicates a far too small initial σ, or divergent behavior.


Two other useful termination criteria should be considered problem dependent:

- • TolFun: stop if the range of the best objective function values of the last 10+ 30n/λ generations and all function values of the recent generation is below TolFun. Choosing TolFun depends on the problem, while 10−12 is a conservative ﬁrst guess.
- • TolX: stop if the standard deviation of the normal distribution is smaller than TolX


in all coordinates and σpc is smaller than TolX in all components. By default we set TolX to 10−12 times the initial σ.

#### B.4 Flat ﬁtness

In the case of equal function values for several individuals in the population, it is feasible to increase the step-size (see lines 92–96 in the source code below). This method can interfere with the termination criterion TolFun. In practice, observation of a ﬂat ﬁtness should be rather a termination criterion and consequently lead to a reconsideration of the objective function formulation.

#### B.5 Boundaries and Constraints

The handling of boundaries and constraints is to a certain extend problem dependent. We discuss a few principles and useful approaches.

Best solution strictly inside the feasible domain If the optimal solution is not too close to the infeasible domain, a simple and sufﬁcient way to handle any type of boundaries and constraints is

31More formally, we terminate if m equals to m + 0.1 σdiibi, where i = (g mod n) + 1, and d2ii and bi are respectively the i-th eigenvalue and eigenvector of C, with bi = 1.

###### 1. setting the ﬁtness as fﬁtness(x) = fmax + x − xfeasible , (62)

where fmax is larger than the worst ﬁtness in the feasible population or in the feasible domain (in case of minization) and xfeasible is a constant feasible point, preferably in the middle of the feasible domain.

###### 2. re-sampling any infeasible solution x until it become feasible.

Repair available as for example with box-constraints.

Simple repair It is possible to simply repair infeasible individuals before the update equations are applied. This is not recommended, because the CMA-ES makes implicit assumptions on the distribution of solution points, which can be heavily violated by a repair. The main resulting problem might be divergence or too fast convergence of the step-size. However, a (re-)repair of changed or injected solutions for their use in the update seems to solve the problem of divergence [18]

(clipping√n+2n/the(n+2)Mahalanobisseems to bedistancesufﬁcient).of theNotestepalsolengththattorepairobeymechanisms x − m σ2mightC ≤ be intricate to implement, in particular if y or z are used for implementing the update equations in the original code.

Penalization We evaluate the objective function on a repaired search point, xrepaired,

and add a penalty depending on the distance to the repaired solution.

fﬁtness(x) = f(xrepaired) + α x − xrepaired 2 . (63) The repaired solution is disregarded afterwards.

In case of box-boundaries, xrepaired is set to the feasible solution with the smallest distance x − xrepaired . In other words, components that are infeasible in x are set to the (closest) boundary value in xrepaired. A similar boundary handling with a component-wise adaptive α is described in [22].

No repair mechanism available The ﬁtness of the infeasible search point x might similarly

compute to

i>0 × ci(x)2 (64)

fﬁtness(x) = foﬀset + α

11c

i

where, w.l.o.g., the (non-linear) constraints ci : Rn → R,x  → ci(x) are satisﬁed for ci(x) ≤ 0 , and the indicator function 11c

i>0 equals to one for ci(x) > 0, zero otherwise, and foﬀset = mediankf(xk) equals, for example, to the median or 25%-tile or best function value of the feasible points in the same generation. If no other information is available, ci(x) might be computed as the squared distance of x to the best or the closest feasible solution in the population or the closest known feasible solution. The latter is reminiscent to the boundary repair above. This approach has not yet been experimentally evaluated by the author. A different, slightly more involved approach is given in [9]. Similar and more recent approaches [10] have already found there way into the Python cma package.

In either case of (63) and (64), α should be chosen such that the differences in f and the differences in the second summand have a similar magnitude.

### C MATLAB Source Code

This code does not implement negative weights, that is, wi = 0 for i > µ in Table 1.

- 1 function xmin=purecmaes
- 2 % CMA-ES: Evolution Strategy with Covariance Matrix Adaptation for
- 3 % nonlinear function minimization.
- 4 %
- 5 % This code is an excerpt from cmaes.m and implements the key parts
- 6 % of the algorithm. It is intendend to be used for READING and
- 7 % UNDERSTANDING the basic flow and all details of the CMA *algorithm*.
- 8 % Computational efficiency is sometimes disregarded.
- 9
- 10 % -------------------- Initialization --------------------------------
- 11
- 12 % User defined input parameters (need to be edited)
- 13 strfitnessfct = ’felli’; % name of objective/fitness function
- 14 N = 10; % number of objective variables/problem dimension
- 15 xmean = rand(N,1); % objective variables initial point
- 16 sigma = 0.5; % coordinate wise standard deviation (step-size)
- 17 stopfitness = 1e-10; % stop if fitness < stopfitness (minimization)
- 18 stopeval = 1e3*Nˆ2; % stop after stopeval number of function evaluations
- 19
- 20 % Strategy parameter setting: Selection
- 21 lambda = 4+floor(3*log(N)); % population size, offspring number
- 22 mu = lambda/2; % lambda=12; mu=3; weights = ones(mu,1); would be (3_I,12)-ES
- 23 weights = log(mu+1/2)-log(1:mu)’; % muXone recombination weights
- 24 mu = floor(mu); % number of parents/points for recombination
- 25 weights = weights/sum(weights); % normalize recombination weights array
- 26 mueff=sum(weights)ˆ2/sum(weights.ˆ2); % variance-effective size of mu
- 27
- 28 % Strategy parameter setting: Adaptation
- 29 cc = (4+mueff/N) / (N+4 + 2*mueff/N); % time constant for cumulation for C
- 30 cs = (mueff+2)/(N+mueff+5); % t-const for cumulation for sigma control
- 31 c1 = 2 / ((N+1.3)ˆ2+mueff); % learning rate for rank-one update of C and
- 32 cmu = min(1-c1, 2*(mueff-2+1/mueff) / ((N+2)ˆ2+2*mueff/2)); % for rank-mu update
- 33 damps = 1 + 2*max(0, sqrt((mueff-1)/(N+1))-1) + cs; % damping for sigma
- 34


- 36 % Initialize dynamic (internal) strategy parameters and constants
- 37 pc = zeros(N,1); ps = zeros(N,1); % evolution paths for C and sigma
- 38 B = eye(N); % B defines the coordinate system
- 39 D = eye(N); % diagonal matrix D defines the scaling
- 40 C = B*D*(B*D)’; % covariance matrix
- 41 eigeneval = 0; % B and D updated at counteval == 0
- 42 chiN=Nˆ0.5*(1-1/(4*N)+1/(21*Nˆ2)); % expectation of
- 43 % ||N(0,I)|| == norm(randn(N,1))
- 44
- 45 % -------------------- Generation Loop --------------------------------
- 46
- 47 counteval = 0; % the next 40 lines contain the 20 lines of interesting code
- 48 while counteval < stopeval
- 49
- 50 % Generate and evaluate lambda offspring
- 51 for k=1:lambda,
- 52 arz(:,k) = randn(N,1); % standard normally distributed vector
- 53 arx(:,k) = xmean + sigma * (B*D * arz(:,k)); % add mutation % Eq. 40
- 54 arfitness(k) = feval(strfitnessfct, arx(:,k)); % objective function call
- 55 counteval = counteval+1;
- 56 end
- 57
- 58 % Sort by fitness and compute weighted mean into xmean
- 59 [arfitness, arindex] = sort(arfitness); % minimization
- 60 xmean = arx(:,arindex(1:mu))*weights; % recombination % Eq. 42
- 61 zmean = arz(:,arindex(1:mu))*weights; % == Dˆ-1*B’*(xmean-xold)/sigma
- 62
- 63 % Cumulation: Update evolution paths
- 64 ps = (1-cs)*ps + (sqrt(cs*(2-cs)*mueff)) * (B * zmean); % Eq. 43
- 65 hsig = norm(ps)/sqrt(1-(1-cs)ˆ(2*counteval/lambda))/chiN < 1.4+2/(N+1);


- 66 pc = (1-cc)*pc + hsig * sqrt(cc*(2-cc)*mueff) * (B*D*zmean); % Eq. 45
- 67
- 68 % Adapt covariance matrix C
- 69 C = (1-c1-cmu) * C ... % regard old matrix % Eq. 47
- 70 + c1 * (pc*pc’ ... % plus rank one update
- 71 + (1-hsig) * cc*(2-cc) * C) ... % minor correction
- 72 + cmu ... % plus rank mu update
- 73 * (B*D*arz(:,arindex(1:mu))) ...
- 74 * diag(weights) * (B*D*arz(:,arindex(1:mu)))’;
- 75
- 76 % Adapt step-size sigma
- 77 sigma = sigma * exp((cs/damps)*(norm(ps)/chiN - 1)); % Eq. 44
- 78
- 79 % Update B and D from C
- 80 if counteval - eigeneval > lambda/(cone+cmu)/N/10 % to achieve O(Nˆ2)
- 81 eigeneval = counteval;
- 82 C=triu(C)+triu(C,1)’; % enforce symmetry
- 83 [B,D] = eig(C); % eigen decomposition, B==normalized eigenvectors
- 84 D = diag(sqrt(diag(D))); % D contains standard deviations now
- 85 end
- 86
- 87 % Break, if fitness is good enough
- 88 if arfitness(1) <= stopfitness
- 89 break;
- 90 end
- 91
- 92 % Escape flat fitness, or better terminate?
- 93 if arfitness(1) == arfitness(ceil(0.7*lambda))
- 94 sigma = sigma * exp(0.2+cs/damps);
- 95 disp(’warning: flat fitness, consider reformulating the objective’);
- 96 end
- 97
- 98 disp([num2str(counteval) ’: ’ num2str(arfitness(1))]);
- 99
- 100 end % while, end generation loop
- 101
- 102 % -------------------- Final Message ---------------------------------
- 103
- 104 disp([num2str(counteval) ’: ’ num2str(arfitness(1))]);
- 105 xmin = arx(:, arindex(1)); % Return best point of last generation.
- 106 % Notice that xmean is expected to be even
- 107 % better.
- 108
- 109 % ---------------------------------------------------------------
- 110 function f=felli(x)
- 111 N = size(x,1); if N < 2 error(’dimension must be greater one’); end
- 112 f=1e6.ˆ((0:N-1)/(N-1)) * x.ˆ2; % condition number 1e6


### D Reformulation of Learning Parameter ccov

For sake of consistency and clarity, we have reformulated the learning coefﬁcients in (47) and replaced

ccov µcov

with c1 (65)

1 µcov

with cµ and (66)

ccov 1 −

1 − ccov with 1 − c1 − cµ , (67) and chosen (in (57) and (58))

2 (n + 1.3)2 + µcov

(68)

c1 =

µcov − 2 + µ1

, 1 − c1 , (69)

cov

cµ = min 2

(n + 2)2 + µcov

The resulting coefﬁcients are quite similar to the previous. In contrast to the previous formulation, c1 becomes monotonic in µ−eﬀ1 and c1 + cµ becomes virtually monotonic in µeﬀ.

Another alternative, depending only on the degrees of freedom in the covariance matrix and additionally correcting for very small λ, reads

min(1,λ/6) m + 2√m + µ

(70)

c1 =

eff

n

αµ0 + µeﬀ − 2 + µ1

(71)

m + 4√m + µ

eff

cµ = min 1 − c1 ,

eff

2

αµ0 = 0.3 , (72) where m = n

2+n

2 is the degrees of freedom in the covariance matrix. For µeﬀ = 1, the coefﬁcient cµ is now chosen to be larger than zero, as αµ0 > 0. Figure 8 compares the new learning rates with the old ones.

- 10−2

- 10−1

100

| | |
|---|---|
| | |


2 4 6 8 10 12 14 16 18 20

10−3

- 10−2




10−3

2 4 6 8 10 12 14 16 18 20

| | |
|---|---|
| | |
| | |


100

10−1

- Figure 8: Learning rates c1,cµ (solid) and ccov (dash-dotted) versus µeﬀ. Above: Equations


(68) etc. for n = 3;10. Below: Equations (70) etc. for n = 2;40. Black: c1 + cµ and ccov; blue: c1 and ccov/µcov; green: cµ and (1 − 1/µcov)ccov; cyan: 2/(n2 + √2); red: (c1 + cµ)/ccov, above divided by ten. For µcov ≈ 2 the difference is maximal, because c1 decreases much slower with increasing µcov and ccov is non-monotonic in µcov (a main reason for the new formulation).

