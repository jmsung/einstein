arXiv:1802.03948v2[cs.NA]17Oct2018

FAST AND RIGOROUS ARBITRARY-PRECISION COMPUTATION OF GAUSS-LEGENDRE QUADRATURE NODES AND WEIGHTS

FREDRIK JOHANSSON∗ AND MARC MEZZAROBBA†

Abstract. We describe a strategy for rigorous arbitrary-precision evaluation of Legendre polynomials on the unit interval and its application in the generation of Gauss-Legendre quadrature rules. Our focus is on making the evaluation practical for a wide range of realistic parameters, corresponding to the requirements of numerical integration to an accuracy of about 100 to 100 000 bits. Our algorithm combines the summation by rectangular splitting of several types of expansions in terms of hypergeometric series with a ﬁxed-point implementation of Bonnet’s three-term recurrence relation. We then compute rigorous enclosures of the Gauss-Legendre nodes and weights using the interval Newton method. We provide rigorous error bounds for all steps of the algorithm. The approach is validated by an implementation in the Arb library, which achieves order-of-magnitude speedups over previous code for computing Gauss-Legendre rules suitable for precisions in the thousands of bits.

Key words. Legendre polynomials, Gauss–Legendre quadrature, arbitrary-precision arithmetic, interval arithmetic

AMS subject classiﬁcations. 65Y99, 65G99, 33C45

1. Introduction. The Legendre polynomials Pn(x) are the sequence of orthogonal polynomials with respect to the unit weight on the interval (−1,1), normalized so that Pn(1) = 1. Like other classical orthogonal polynomials, Legendre polynomials satisfy a three-term recurrence, in this case the relation

- (1) (n + 1)Pn+1(x) − (2n + 1)xPn(x) + nPn−1(x) = 0, n ≥ 1, also known as Bonnet’s formula, and a second order diﬀerential equation, here
- (2) (1 − x2)Pn′′(x) − 2xPn′(x) + n(n + 1)Pn(x) = 0.

The deﬁnition implies that Pn has n roots all located in (−1,1). Perhaps the most important application of Legendre polynomials is the Gauss-Legendre quadrature rule

- (3)


n−1

1

2 (1 − x2i )[Pn′ (xi)]2

,

wif(xi), wi =

f(x)dx ≈

![image 1](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile1.png>)

−1

i=0

where the nodes xi are the roots of Pn. The quantity wi is called the weight associated with the node xi.

For some applications in computer algebra, number theory, mathematical physics, and experimental mathematics, it is necessary to compute integrals to an accuracy of hundreds of digits, and occasionally even tens of thousands of digits [2, 3, 9, 23]. The Gauss-Legendre formula (3) achieves an accuracy of p bits using n = O(p) evaluation points if f is analytic on a neighborhood of (−1,1), and if the neighborhood is large (that is, if the path of integration is well isolated from any singularities of f), then the constants hidden in the O notation are close to the best achievable by any quadrature rule [22]. This quality is related to the fact that (3) maximizes the order of accuracy among n-point quadrature rules for integrating polynomials, being exact when f is

![image 2](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile2.png>)

∗INRIA – LFANT, CNRS – IMB – UMR 5251, Universit´e de Bordeaux, 33400 Talence, France (fredrik.johansson@gmail.com)

†Sorbonne Universit´e, CNRS, Laboratoire d’Informatique de Paris 6, LIP6, F-75005 Paris, France (marc@mezzarobba.net)

1

any polynomial of degree up to 2n − 1; as a result, the accuracy is also excellent for analytic integrands that are well approximated by polynomials.1

In general, the error in (3) can be bounded in terms of supx∈(−1,1) |f(2n)(x)|, or, if f is analytic on an elliptical domain D with foci at ±1, in terms of supz∈D |f(z)| and the semi-axes of the ellipse. Even when the conditions are not ideal for using (3) directly, rapid convergence is often possible by combining (3) with adaptive subdivision of the integration path [28]. We give some elements of comparison between GaussLegendre quadrature and alternative methods, such as Clenshaw-Curtis quadrature, in section 8.

The Gauss-Legendre scheme has the drawback that the quadrature nodes and weights are somewhat inconvenient to compute. Indeed, Pn becomes highly oscillatory for large n and hence presents diﬃculties for naive root-ﬁnding and polynomial evaluation methods. The classical Golub-Welsch algorithm avoids accuracy problems by formulating the task of computing the nodes as ﬁnding the eigenvalues of a tridiagonal matrix [13], but this approach is still too slow to be practical for large n.

In the last decade, several authors have contributed to the development of asymptotic methods that permit computing any individual node and weight for arbitrarily large n in O(1) time, culminating in the 2014 work by Bogaert [6, 15, 5]. For a review of this progress, see Townsend [32]. Of course, the “O(1)” bound assumes that a ﬁxed level of precision is used. In the prevailing literature this generally means 53-bit IEEE 754 ﬂoating-point arithmetic. In addition, the available O(1) implementations rely in part on heuristic error estimates without rigorously proved bounds.

The literature on arbitrary precision or rigorous evaluation is comparatively lim-

ited. Petras [27] gave explicit bounds for the error |xk(i) − xk| when the roots xk of the Legendre polynomial Pn are approximated using Newton iteration

Pn(xk(i)) Pn′(xk(i))

- (4) x(ki+1) = x(ki) −


![image 3](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile3.png>)

provided that the initial values x(0)k are computed by a certain asymptotic formula. However, Petras did not address the numerical evaluation of Pn(x). Fousse [12] discussed the rigorous implementation of Gauss-Legendre quadrature using generic polynomial root isolation methods together with interval Newton iteration for root reﬁnement, but did not study fast methods for large n. Code for high-precision GaussLegendre quadrature rules can also be found in packages such as Pari/GP [31] and ARPREC [4], but without error analysis and without special techniques for large n.

In the present article, we are interested in computing Gauss-Legendre nodes and weights to precisions p signiﬁcantly larger than machine precision typically in the hundreds to thousands of bits , with rigorous error bounds. As mentioned earlier, certain applications require enclosing the values of integrals to accuracies of this order, and it is often reasonable to use quadrature rules of degree n that grows roughly linearly with p for this purpose. For example, Johansson and Blagouchine [20] study the computation of Stieltjes constants to precisions of hundreds of digits using complex integration, building among other things on the work described in the present paper.

If we assume that the precision p varies, basic arithmetic operations are no longer constant-time. It is well-known that addition, multiplication and division of p-bit

![image 4](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile4.png>)

1However, statements about the near-optimality of Gauss-Legendre quadrature must not be overinterpreted. Indeed, the rate of convergence of Gauss-Legendre quadrature is not optimal asymptotically when n → ∞ for analytic f on a ﬁxed neighborhood, being improvable by a small factor [34].

numbers (of bounded exponent) can be performed in O(p) operations [8], where the notation O(·) means that we neglect logarithmic factors. It is then clear that any node and weight can be computed to p-bit accuracy in O(np) time, by performing O(log p) Newton iterations (4) from an appropriate initial value. As a consequence, the full set of nodes and weights for the degree-n quadrature rule can be computed in O(n2p) time. For numerical integration of analytic functions where we typically have p ≈ n, a better (indeed, optimal) estimate than the classical O(n3) bound is possible.

Theorem 1. If p ∼ αn for some ﬁxed α, then the Gauss-Legendre nodes and weights of degree n can be computed to p-bit accuracy in O(n2) (equivalently, O(p2)) bit operations.

Proof sketch. Using the formulae in [27], we can compute good initial values for Newton iteration in O(n) bit operations. The Newton iteration can be performed for all roots simultaneously using fast multipoint evaluation, which costs O(np) bit operations. Fast multipoint evaluation is numerically unstable and generically loses O(n) bits of accuracy, but we can compensate for this loss by using O(n) guard bits [21]. Since p ∼ αn by assumption, this does not change the complexity bound.

![image 5](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile5.png>)

![image 6](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile6.png>)

![image 7](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile7.png>)

![image 8](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile8.png>)

Completing the details of the proof is a technical exercise. Despite being elegant in theory, the algorithm behind Theorem 1 has a high overhead in practice, in large part due to the need to work with greatly increased precision. Working with expanded polynomials and processing all roots simultaneously also results in high memory usage and makes parallelization diﬃcult. As discussed in subsection 5.2 below, an approach based on the “bit-burst” evaluation method for hypergeometric series leads to a similar complexity bound and may prove more practical for extremely large p, but likely not for p ≤ 106. We can achieve a slightly worse but still subcubic complexity of O(n5/2) by employing fast multipoint evaluation in a completely diﬀerent way to compute Pn values in isolation [16], but unfortunately that algorithm also has high overhead.

In this work, we develop rigorous and more practical alternatives to the asymptotically fast algorithm outlined above. Our main contribution is to give a complete evaluation strategy for Legendre polynomials on [−1,1] in ball arithmetic [35, 19]. Computing the Gauss-Legendre nodes, then, is a relatively simple application of the results in [27] together with the interval Newton method [24]. For generating GaussLegendre quadrature rules with n ∼ αp, our algorithm has an asymptotic bit complexity of O(n3) like classical methods, but much lower overhead. For parameters p,n ≤ 105 which are most relevant to applications, the observed running time is eﬀectively subcubic. Our algorithm outperforms that of Theorem 1 for practically any combination of n and p in that range. Furthermore, if p = O(1), the complexity reduces to O(n) as in the machine-precision implementations by Bogaert [5] and others.

The remainder of this paper is organized as follows. Section 2 gives an overview of our algorithm for evaluating Legendre polynomials. This is a hybrid algorithm that switches between diﬀerent methods, detailed in the following sections, depending on the values of n, p, and x. In section 3, we prove practical error bounds for the threeterm recurrence (1), which can be eﬃciently implemented in ﬁxed-point arithmetic. This method is ideal for n and p up to a few hundred. For larger n or p, we use a fast method for evaluation of hypergeometric series. Section 4 discusses the hypergeometric series expansions that are preferable for diﬀerent inputs and precision (including a well-known asymptotic expansion for large n), and section 5 their eﬃcient evaluation. In section 6, we propose a strategy to select the best formula for any combination

of n,p,x. Section 7 presents benchmark results that compare the performance of our algorithm to some previous implementations as well as the asymptotically fast algorithm in Theorem 1. Finally, section 8 reviews the viability of Gauss-Legendre quadrature compared to other methods for extremely high precision integration.

Our code for evaluating Legendre polynomials and computing Gauss-Legendre nodes and weights is freely available as part of the Arb library [19]2.

2. General strategy. We work in the framework of midpoint-radius interval arithmetic, also called ball arithmetic [35, 19]. In general, given an integer n and a ball x = [m±r] = [m−r,m+r], we want to evaluate Pn(x) at x, yielding an enclosure y = [m′ ± r′] such that Pn(ξ) ∈ y holds for all ξ ∈ x.

We restrict our attention to real x ∈ [−1,1], which is the most interesting part of the domain for applications. Since Pn(−x) = (−1)nPn(x), we can further restrict

- to 0 ≤ x ≤ 1. Bogaert [5] suggests working with Pn(cos(θ)) instead of Pn(x) directly to improve numerical stability for x close to ±1. This is not necessary in arbitraryprecision arithmetic since a slight precision increase (of the order of O(log n) bits, since


the distance between two successive roots of Pn close to ±1 is about 1/n2) works as well.

We note that, for rigorous evaluation of Pn(z) with complex z as well as Legendre functions of non-integer order n, generic methods for the hypergeometric 2F1 function are applicable if n is not extremely large; see [18]. Real |x| > 1 can also be handled easily using naive methods.

In view of the use of Newton’s method to compute the roots, we also need to evaluate the derivative Pn′ (x), typically at the same time as Pn(x) itself. A simple option is to deduce Pn′(x) from Pn(x) and Pn−1(x) using

- (5) (x2 − 1)Pn′ (x) = n xPn(x) − Pn−1(x) .


When x is close to ±1, though, this formula involves a cancellation of about |log2(1− x)| bits in the subtraction, followed by a division by x2 − 1. Therefore, a direct

evaluation of Pn′(x) may be preferable to reduce the working precision. We use either of these strategies depending on the values of n, p, and x.

Our evaluation algorithms rely on ball arithmetic internally to propagate the error bounds up to the ﬁnal result. Therefore, to ensure that the enclosure output by our evaluation algorithm contains the image of the input, it is enough to have bounds on the truncation errors associated to each of the approximate expressions of Pn that we use. The corresponding bounds are stated in equations (19), (26), and (29).

To limit overestimation and computational overhead, we deviate from the direct use of ball arithmetic on two occasions. First, Algorithm 1 does not keep track of round-oﬀ errors internally: instead, we prove an a priori bound on the accumulated error (Corollary 6) and add it to the radius of the output ball after calling that algorithm. Second, since some methods would produce unsatisfactorily large enclosures when executed on input balls x = [m ± r] of radius r > 0, we evaluate Pn(m) (with higher internal precision if necessary) and Pn′(x) and use a ﬁrst-order bound

|Pn′(ξ)|

max

|Pn(ξ) − Pn(m)| ≤ r max

ξ∈x

ξ∈x

to separately bound the propagated error. Similarly, we use a bound for Pn′′ to compute a reasonably tight enclosure for Pn′([m ± r]). Suitable bounds are given in

![image 9](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile9.png>)

2http://arblib.org/

Proposition 3. Denote by [zn]f(z) the coeﬃcient of index n in a power series f(z), and write f(z) ≪z fˆ(z) for two power series f,fˆ if fˆ has nonnegative coeﬃcients and |[zn]f(z)| ≤ [zn]fˆ(z) for all n.

Lemma 2. If f, g, fˆ, gˆ are such that f(z) ≪z fˆ(z) and g(z) ≪z gˆ(z), then

z 0 f ≪z 0 z fˆ and f(z)g(z) ≪z fˆ(z)ˆg(z).

Proposition 3. The following bounds hold for −1 ≤ x ≤ 1:

√n (1 − x2)3/4

23/2 √π

![image 10](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile10.png>)

n(n + 1) 2

|Pn′ (x)| ≤ min

- (6) ,

|Pn′′(x)| ≤ min

25/2 √π

![image 11](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile11.png>)

![image 12](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile12.png>)

n3/2 (1 − x2)5/4

![image 13](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile13.png>)

,

(n − 1)n(n + 1)(n + 2) 8

![image 14](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile14.png>)

- (7) .

Proof. It is classical that Legendre polynomials are given by the generating series

- (8) F(x,z) =


,

![image 15](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile15.png>)

![image 16](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile16.png>)

![image 17](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile17.png>)

![image 18](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile18.png>)

∞

1 √1 − 2xz + z2

Pn(x)zn =

.

![image 19](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile19.png>)

![image 20](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile20.png>)

n=0

Diﬀerentiation with respect to x yields

∞

∞

3z2F(x,z) (1 − 2xz + z2)2

zF(x,z) 1 − 2xz + z2

Pn′ (x)zn =

Pn′′(x)zn =

,

.

![image 21](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile21.png>)

![image 22](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile22.png>)

n=0

n=0

Set θ = arccosx, so that the roots of 1 − 2xz + z2 are e±iθ. Then, in the notation of Lemma 2, we have the bound

1 1 − 2xz + z2

=

![image 23](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile23.png>)

1 2i sinθ

![image 24](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile24.png>)

1 z − eiθ −

1 z − e−iθ

![image 25](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile25.png>)

![image 26](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile26.png>)

∞

sin(θ)−1 1 − z

sin (n + 1)θ sin(θ)

zn ≪z

=

.

![image 27](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile27.png>)

![image 28](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile28.png>)

n=0

In addition, Bernstein’s inequality for the Legendre polynomials [37] (see also [10]) combined with the logarithmic convexity of the Gamma function yields

√2 √π

√2 √π

![image 29](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile29.png>)

![image 30](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile30.png>)

1 √

1 √

1 n + 1/2 ≤

Γ(n + 1/2) Γ(n + 1)

,

|Pn(x)| ≤

![image 31](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile31.png>)

![image 32](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile32.png>)

![image 33](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile33.png>)

![image 34](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile34.png>)

![image 35](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile35.png>)

![image 36](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile36.png>)

![image 37](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile37.png>)

![image 38](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile38.png>)

![image 39](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile39.png>)

![image 40](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile40.png>)

![image 41](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile41.png>)

sinθ

sinθ

and hence

√2 √

√2 √

∞

![image 42](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile42.png>)

![image 43](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile43.png>)

Γ(n + 1/2) Γ(n + 1)

1 √1 − z

1 √π

zn =

F(x,z) ≪z

.

![image 44](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile44.png>)

![image 45](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile45.png>)

![image 46](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile46.png>)

![image 47](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile47.png>)

![image 48](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile48.png>)

![image 49](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile49.png>)

![image 50](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile50.png>)

![image 51](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile51.png>)

![image 52](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile52.png>)

sinθ

sinθ

n=0

By Lemma 2, these bounds combine into

√2 sin(θ)5/2

√2 sin(θ)3/2

d2F dx2 ≪z

3z2 (1 − z)5/2

![image 53](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile53.png>)

![image 54](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile54.png>)

1 (1 − z)3/2

dF dx ≪z

,

.

![image 55](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile55.png>)

![image 56](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile56.png>)

![image 57](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile57.png>)

![image 58](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile58.png>)

![image 59](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile59.png>)

![image 60](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile60.png>)

Since [zn](1 − z)−k−1/2 = Γ(n + 1/2)/(Γ(k + 1/2)Γ(n − k + 1)) and using again the logarithmic convexity of Γ, we conclude that

√2 sin(θ)3/2

√n sin(θ)3/2

25/2 √π

n3/2 (1 − x2)5/4

23/2 √π

![image 61](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile61.png>)

![image 62](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile62.png>)

2 √π

Γ(n + 1/2) Γ(n) ≤

, |Pn′′(x)| ≤

|Pn′(x)| ≤

.

![image 63](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile63.png>)

![image 64](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile64.png>)

![image 65](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile65.png>)

![image 66](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile66.png>)

![image 67](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile67.png>)

![image 68](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile68.png>)

![image 69](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile69.png>)

![image 70](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile70.png>)

![image 71](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile71.png>)

![image 72](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile72.png>)

The result follows since all derivatives of Legendre polynomials reach their maximum at x = 1 (or by using the bounds (z−e±iθ)−1,F(x,z) ≪z (1−z)−1 and Lemma 2).

![image 73](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile73.png>)

![image 74](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile74.png>)

![image 75](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile75.png>)

![image 76](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile76.png>)

Remark 4. By the same reasoning, the inequality

nk−1/2 (1 − x2)(2n+1)/4

2k+1/2 √π

|Pn(k)(x)| ≤

![image 77](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile77.png>)

![image 78](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile78.png>)

![image 79](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile79.png>)

actually holds for all k. Unfortunately, it seems to overestimate the envelope of |Pn(k)| by a factor about 2k in the region where it is smaller than Pn(k)(1).

Based on these reductions, we assume from now on that x is a ﬂoating-point number with 0 ≤ x ≤ 1. Our main algorithm for evaluating Pn at x combines the following methods:

- • the iterative computation of Pn(x) via the three-term recurrence (1),
- • the asymptotic expansion (17) of Pn(x) as n → ∞,
- • the usual expanded expression (23), (24) of Pn in the monomial basis,
- • the analogous terminating expansion (27) at 1.


All three expansions can be written as hypergeometric series, i.e., sums of the form k ckξk where ck/ck−1 is a rational function of k.

The constraints and heuristics used to select between these methods are described in detail below. Roughly speaking, the three-term recurrence is used for small index n and precision p, when x is not too close to 1; the asymptotic series when n is large enough, again with x not too close to 1; the expansion at 0 for large p unless x is close

- to 1; and ﬁnally the expansion at 1 in the remaining cases when x is close to 1. For an evaluation at p-bit precision, we choose parameters such as truncation


′

orders and internal working precision to target an absolute error of 2−p−p

for some p′ = O(log n), corresponding to a relative error of about 2−p measured with respect to monotone envelopes for Pn(x) and Pn′(x) as in [6]. The relative error of a computed ball for Pn(x) where x is near a zero xk can be arbitrarily large, but the relative error of Pn′ (x) near xk will be small, which is suﬃcient for the Newton iteration method. Since the output consists of a ball, we also have the option of catching a result with large relative error and repeating the evaluation with a higher precision as needed.

3. Basecase recurrence. For small n, a straightforward way to compute Pn(x) is to apply the three-term recurrence (1), starting from P0(x) = 1 and P1(x) = x. Computing Pn(x) by this method takes about (M(t) + O(t))n bit operations, where t is the working precision and M(t) denotes the cost of t-bit multiplication. It is thus attractive for small n and t, especially when both Pn(x) and Pn′(x) are needed, since we can get Pn−1(x) at no additional cost.

Fix x ∈ [−1,1], and let pn = Pn(x). Bonnet’s formula (1) gives

1 n + 1

- (9) pn+1 =


(2n + 1)xpn − npn−1 , n ≥ 0.

![image 80](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile80.png>)

In a direct implementation of this recurrence in ball arithmetic, the width of the enclosures would roughly double at every iteration, requiring to increase the internal working precision by O(n) bits. We avoid this issue by performing an a priori round-

- oﬀ error analysis (to be presented now) of the evaluation that yields a less pessimistic bound on the accumulated error. Additionally, the static error bound allows us to implement the recurrence in ﬁxed-point arithmetic, avoiding the overhead of ﬂoatingpoint and interval operations.


Suppose x = xˆ 2−t with xˆ ∈ Z is a given ﬁxed-point number. Let ⌈u⌋ denote the integer truncation of a real number u (note that this is not the same thing as

rounding to the nearest integer; however, any rounding function would do). The integer sequence (ˆpn) deﬁned by

- (10) pˆ0 = 2t, pˆ1 = x,ˆ pˆn+1 =

1 n + 1

![image 81](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile81.png>)

(2n + 1)⌈xˆpˆn2−t⌋ − npˆn−1

is easy to compute using only integer arithmetic, and pˆn 2−t is an approximation of pn. Algorithm 1 provides a complete C implementation using GMP [14]. As a small optimization, we delay the division by n + 1 until we have accumulated a denominator of the size of a machine word.

![image 82](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile82.png>)

- Algorithm 1 Evaluation of Legendre polynomials in GMP ﬁxed-point arithmetic Input: An integer x and t ≥ 0 such that |2−tx| ≤ 1, and n ≥ 1 Output: p, q such that |2−tp−Pn−1(2−tx)|, |2−tq−Pn(2−tx)| ≤ (0.75 (n+1)(n+2)+1) 2−t


![image 83](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile83.png>)

- 1: void legendre(mpz_t p, mpz_t q, int n, const mpz_t x, int t) {
- 2: mpz_t tmp; int k; mpz_init(tmp); ⊲ Comments use the notation of
- 3: mp_limb_t denlo, den = 1; ⊲ the proof of Corollary 6
- 4: mpz_set_ui(p, 1); mpz_mul_2exp(p, p, t); ⊲ p0 = 2t
- 5: mpz_set(q, x); ⊲ q0 = xˆ
- 6: for (k = 1; k < n; k++) {
- 7: mpz_mul(tmp, q, x); mpz_tdiv_q_2exp(tmp, tmp, t); ⊲ ⌈xˆqk−1 2−t⌋
- 8: mpz_mul_si(p, p, -k*k)
- 9: mpz_addmul_ui(p, tmp, 2*k+1); ⊲ −k2pk−1 + (2k + 1) tmp
- 10: mpz_swap(p, q);
- 11: if (mpn_mul_1(&denlo, &den, 1, k+1)) { ⊲ If multiplication overﬂows
- 12: mpz_tdiv_q_ui(p, p, den); ⊲ ⌈p/dk−1⌋
- 13: mpz_tdiv_q_ui(q, q, den);
- 14: den = k+1; ⊲ dk = k + 1
- 15: } else den = denlo; ⊲ dk = (k + 1) dk−1
- 16: }
- 17: mpz_tdiv_q_ui(p, p, den/n); mpz_tdiv_q_ui(q, q, den);
- 18: mpz_clear(tmp);
- 19: }


![image 84](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile84.png>)

To bound the diﬀerence |pˆn 2−t − pn|, we analyze the eﬀect on the result of a small perturbation in each iteration of (9). The bound is based on a classical linearity argument (compare, e.g., [36]) combined with majorant series techniques.

Proposition 5. Suppose that a real sequence (˜pn)n≥−1 satisﬁes p˜0 = 1 and

- (11) p˜n+1 =

1 n + 1

![image 85](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile85.png>)

(2n + 1)xp˜n − np˜n−1 + εn, n ≥ 0.

for arbitrary real numbers εn with |εn| ≤ ε¯ for all n. Then we have

|p˜n − Pn(x)| ≤

(n + 1)(n + 2) 4

![image 86](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile86.png>)

ε¯

for all n ≥ 0. Proof. Let δn = p˜n − pn and ηn = (n + 1)εn. Subtracting (9) from (11) gives

- (12) (n + 1)δn+1 = (2n + 1)xδn − nδn−1 + ηn,


with δ0 = 0. Consider the formal generating series δ(z) = n≥0 δnzn and η(z) =

n≥0 ηnzn. Noting that (12) holds for all n ∈ Z if the sequences (δn) and (ηn) are extended by 0 for n < 0 and using the relations

∞

∞

fnzn,

fn−1zn = z

n=−∞

n=−∞

∞

d dz

nfnzn = z

![image 87](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile87.png>)

n=−∞

∞

fnzn,

n=−∞

we see that (12) translates into

d dz

(1 − 2xz + z2)z

δ(z) = z(x − z)δ(z) + zη(z). The solution of this diﬀerential equation with δ(0) = 0 reads, cf. (8), δ(z) = p(z)

![image 88](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile88.png>)

∞

z

1 √1 − 2xz + z2

pnzn = F(x,z) =

.

η(w)p(w)dw, p(z) =

![image 89](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile89.png>)

![image 90](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile90.png>)

0

n=0

This is an exact expression of the “global” error δ in terms of the “local” errors εn. Since |pn| = |Pn(x)| ≤ 1 and |ηn| ≤ (n + 1)¯ε, it follows by Lemma 2 that

z

z

1 1 − w

ε¯ (1 − w)2

1 1 − z

|δn| = [zn] p(z)

η(w)p(w)dw ≤ [zn]

dw

![image 91](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile91.png>)

![image 92](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile92.png>)

![image 93](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile93.png>)

0

0

and therefore

- 1

![image 94](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile94.png>)

- 2


(n + 1)(n + 2) 4

ε¯ (1 − z)3

|δn| ≤ [zn]

=

ε.¯

![image 95](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile95.png>)

![image 96](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile96.png>)

![image 97](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile97.png>)

![image 98](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile98.png>)

![image 99](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile99.png>)

![image 100](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile100.png>)

Corollary 6. Suppose that x = xˆ 2−t for some t ≥ 0 and xˆ ∈ Z. The sequence (ˆpn)n≥0 deﬁned by (10) satisﬁes

- (13) |pˆn2−t − pn| ≤ 0.75 (n + 1)(n + 1)2−t, n ≥ 0. Furthermore, the quantities p, q returned by Algorithm 1 are such that
- (14) |p − 2tPn−1(x)|,|q − 2tPn(x)| ≤ 0.75(n + 1)(n + 2) + 1. Proof. We can write

pˆn+1 =

1 n + 1

![image 101](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile101.png>)

(2n + 1)(ˆx pˆn 2−t + αn) − n pˆn−1 + βn for some αn, βn of absolute value at most one, and hence

pˆn+1 =

1 n + 1

![image 102](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile102.png>)

(2n + 1)xˆ pˆn 2−t − n pˆn−1 + εn, εn =

2n + 1 n + 1

![image 103](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile103.png>)

αn + βn. where |εn| ≤ 3. Proposition 5 applied to p˜n = pˆn 2−t then provides the bound (13).

Turning to Algorithm 1, let p0, q0, d0 denote the values of the variables p, q, den before the loop, and pk, qk, dk their values at the end of iteration k. Consider the sequence p˜k = 2−tqk−1/dk−1, k ≥ 1, extended by p˜0 = 1 and an arbitrary (ﬁnite) p˜−1. For all k ≥ 1, depending whether the conditional branch is taken, we have one of the systems of equations

- (15) pk = qk−1, qk = (2k + 1)⌈xˆqk−12−t⌋ − k2pk−1, dk = (k + 1)dk−1

pk =

qk−1 dk−1

![image 104](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile104.png>)

, qk =

(2k + 1)⌈xˆqk−12−t⌋ − k2pk−1 dk−1

![image 105](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile105.png>)

- (16) , dk = k + 1.


In both cases, we can write

pk dk

=

![image 106](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile106.png>)

qk−1 (k + 1)dk−1

+

![image 107](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile107.png>)

αk k + 1

,

![image 108](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile108.png>)

(2k + 1)(xqk−1 + βk) − k2pk−1 (k + 1)dk−1

qk dk

=

+

![image 109](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile109.png>)

![image 110](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile110.png>)

γk k + 1

![image 111](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile111.png>)

with |αk|,|βk|,|γk| ≤ 1. The ﬁrst equation implies 2−tk pk−1/dk−1 = p˜k−1 + αk−12−t for k ≥ 2. Since the latter equality also holds for k = 1 with α0 = 0, we can substitute it in the second equation, yielding

+ 2−t −kαk−1 k + 1

(2k + 1)xp˜k − kp˜k−1 k + 1

+

p˜k+1 =

![image 112](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile112.png>)

![image 113](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile113.png>)

(2k + 1)βk (k + 1)dk−1

![image 114](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile114.png>)

γk k + 1

+

![image 115](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile115.png>)

.

This relation holds for k ≥ 1, and we extend it to k = 0 by setting β0 = γ0 = 0. Thus, p˜k also satisﬁes (11) with |εn| ≤ 3 · 2−t, and Proposition 5 applies. The ﬁnal values of q and p are respectively ⌈2tp˜n⌋ and ⌈npn−1/dn−1⌋ = ⌈2tp˜n−1 + αn−1⌋, whence the bound (14).

![image 116](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile116.png>)

![image 117](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile117.png>)

![image 118](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile118.png>)

![image 119](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile119.png>)

We do not use asymptotically faster evaluation techniques for large n in combination with this recurrence, since the series expansions to be presented next perform very well in this case.

4. Series expansions. For large n or p, we employ series expansions of Pn(x) with respect to either n or x rather than the algorithm from the previous section. The coeﬃcients of the series are also computed by recurrence, but fewer than n terms will typically be required. Let us now review the various series expansions that we are using (an asymptotic expansion as n → ∞, series expansions at x = 0 and x = 1), before discussing their eﬃcient evaluation in the next section.

4.1. Asymptotic series. For ﬁxed |x| < 1 or equivalently x = cos(θ) with

- 0 < θ < π, an asymptotic expansion for Pn(x) as n → ∞ can be given as [6, Eq. 3.4]


- (17) Pn(cos(θ)) =

2 π sin(θ)

![image 120](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile120.png>)

1/2 K−1

k=0

Cn,k

cos(αn,k(θ)) sink(θ)

![image 121](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile121.png>)

+ ξn,K(θ)

(for arbitrary K ≥ 1), where

- (18) Cn,k =

[Γ(k + 1/2)]2Γ(n + 1) π2kΓ(n + k + 3/2)Γ(k + 1)

![image 122](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile122.png>)

,

αn,k(θ) = (n + k + 1/2)θ − (k + 1/2)π/2, and the error term satisﬁes

- (19) |ξn,K(θ)| < 2

2 π sin(θ)

![image 123](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile123.png>)

1/2 Cn,K sinK(θ)

![image 124](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile124.png>)

.

The coeﬃcients Cn,k are a hypergeometric sequence with

- (20)

Cn,k Cn,k−1

![image 125](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile125.png>)

=

(2k − 1)2 4k(2n + 2k + 1)

![image 126](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile126.png>)

, Cn,0 =

1 √π

![image 127](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile127.png>)

![image 128](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile128.png>)

4n (n + 21) 2nn

![image 129](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile129.png>)

![image 130](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile130.png>)

.

To evaluate the error bound, we can use the following inequality deduced from (18):

- (21) Cn,k ≤


1 πn1/2

k!n! 2k(n + k)! ≤

1 πn1/2

![image 131](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile131.png>)

![image 132](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile132.png>)

![image 133](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile133.png>)

k! (2n)k

, n,k ≥ 1.

![image 134](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile134.png>)

The condition |ξn,K(θ)| ≤ 2−p is satisﬁable as soon as sin(θ) ≥ (p + 3)ln(2)/(2n),

- as we can see by choosing K = ⌊2n sin(θ)⌋ and using the inequality k! ≤ kk+1/2e1−k. Since the Gauss-Legendre nodes are distributed linearly in θ, the asymptotic expansion gives a candidate algorithm for all but about (log(2)/π)p/n of the nodes as p/n → 0. It is in fact a convergent series when 2 sin(θ) > 1, which allows evaluating Pn(x) to


unbounded accuracy for ﬁxed n when 16π < θ < 65π. The particular form (17) must be used for this purpose; there is a slightly diﬀerent version of the expansion which

![image 135](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile135.png>)

![image 136](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile136.png>)

is asymptotic to Pn(x) (for ﬁxed K when n → ∞) but paradoxically converges to 2Pn(x) (for ﬁxed n when K → ∞); see [25, Section 10.3] and [26, Section 18.15(iii)].

We can restate (17) as a hypergeometric series by working with complex numbers. Letting ω = 1 − (x/y)i, with x = cos(θ) and y = sin(θ) as usual, we have

√

√

exp(i αn,k(θ)) sink(θ)

π

(1 − i)(x + iy)n+1/2ωk =

4 ei(n+1/2)θ eik(θ−π/2) y−k =

2 e−i

![image 137](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile137.png>)

![image 138](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile138.png>)

2

,

![image 139](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile139.png>)

![image 140](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile140.png>)

and hence

- (22) Pn(x) =

1 √πy

![image 141](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile141.png>)

![image 142](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile142.png>)

Re (1 − i)(x + yi)n+1/2

K−1

k=0

Cn,kωk + ξn,K(θ).

This eliminates the explicit trigonometric functions and permits using Algorithm 2 below to evaluate the series.

The evaluation of (22) in ball arithmetic is numerically stable, and we therefore only need to add a few guard bits to the working precision.

4.2. Expansion at zero. If n = 2d is even, the expansion of Pn(x) in the monomial basis reads

P2d(x) = (−1)d

d

k=0

(−1)k 2n

![image 143](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile143.png>)

n d − k

n + 2k n

x2k

=

(−1)d 22d

![image 144](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile144.png>)

2d d

d

k=0

A−1(d,k)(−x2)k,

- (23)

and if n = 2d + 1 is odd, we have

P2d+1(x) = (−1)dx

d

k=0

(−1)k 2n

![image 145](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile145.png>)

n d − k

n + 2k + 1 n

x2k

=

(−1)d(d + 1) 22d+1

![image 146](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile146.png>)

2d + 2 d + 1

x

d

k=0

A+1(d,k)(−x2)k

- (24)

where the hypergeometric sequences A±1 can be deﬁned by A±1(d,0) = 1 and

- (25)


Aσ(d,k) Aσ(d,k − 1)

(d − k + 1)(2d + 2k + σ) k(2k + σ)

=

, σ ∈ {−1,+1}.

![image 147](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile147.png>)

![image 148](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile148.png>)

At very high precision, we evaluate the full polynomials, where (23) and (24) have the advantage compared to other expansions of requiring only n/2 terms due to the odd-even form. At lower precision p, the high order terms will be smaller than 2−p when |x| is small, and we can truncate the series accordingly and add a bound for the omitted terms to the radius of the computed ball. When the series are truncated after the k = K − 1 term (for any K < d + 1), comparison with a geometric series shows that the error is bounded by the ﬁrst omitted term times a simple factor.

Proposition 7. For σ ∈ {−1,+1}, the error when truncating the bottom sum in

(23) or (24) (with prefactors removed) after the k = K − 1 term satisﬁes

- (26)

d

k=K

Aσ(d,k)(−x2)k ≤

Aσ(d,K)|x|2K 1 − α

![image 149](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile149.png>)

, α = |x|2

(d − K + 1)(2d + 2K + σ) K(2K + σ) provided that α < 1.

![image 150](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile150.png>)

For bounding Aσ(d,K) in this expression, and for selecting an appropriate truncation point K, we use the binomial closed forms (23), (24) together with the remarks in subsection 5.3.

The alternating series (23) and (24) may suﬀer from signiﬁcant cancellation, which requires use of increased precision. We can estimate the magnitude by noting that no cancellation occurs if x is an imaginary number. Solving the majorizing recurrence fn = 2|z|fn−1 + fn−2 with f0 = 1, f1 = |z| shows that

|Pn(z)| ≤ |Pn(i|z|)| ≤ |z| + 1 + |z|2

![image 151](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile151.png>)

n

.

Therefore, the possible cancellation assuming that |Pn(x)| ≈ 1 is about

pA = n log2 |x| + 1 + |x|2 bits (which is at most n log2(1 + √2) ≈ 1.27 n), so using ball arithmetic with about

![image 152](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile152.png>)

![image 153](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile153.png>)

- p + pA bits of working precision for the series evaluation gives p-bit accuracy. 4.3. Expansion at one. Expanding at x = 1 yields


- (27) Pn(x) =

n

k=0

cn,kuk, cn,k =

n k

n + k k

where u = (x − 1)/2. The coeﬃcients cn,k are hypergeometric with initial value cn,0 = 1 and term ratio

- (28)

cn,k cn,k−1

![image 154](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile154.png>)

=

(n − k + 1)(n + k) k2

![image 155](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile155.png>)

.

As in the previous section, we can truncate (27) and bound the error by comparison with a geometric series.

Proposition 8. The error when truncating (27) after the k = K−1 term satisﬁes

- (29)


n

cn,K|u|K 1 − α

(n − K)(n + K + 1) (K + 1)2 provided that α < 1.

cn,kuk ≤

, α = |u|

![image 156](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile156.png>)

![image 157](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile157.png>)

k=K

For u ≥ 0, (27) does not suﬀer from cancellation. For u < 0, we can estimate the amount of cancellation from the magnitude of Pn(x′) where |u| = (x′ − 1)/2. For not too large x′ ≥ 1, a very good approximation is

√

∞

n2k k!2 |u|k = 2 I0(2n |u|) ≤ 2 e2n

![image 158](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile158.png>)

![image 159](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile159.png>)

|u|.

Pn(x′) ≤ 2

![image 160](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile160.png>)

k=0

![image 161](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile161.png>)

We therefore need about 2n max(0,−u)/ ln(2) bits of increased precision.

We can compute Pn′ from Pn and Pn−1, but since this involves a division by 1−x2, it is better to evaluate Pn′ directly when x is close to 1. We have Pn′ (x) = k n=0−1 c′n,kuk where c′n,k = (k + 1)cn,k+1/2 satisﬁes

- (30) c′n,0 =

n(n + 1) 2

![image 162](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile162.png>)

,

c′n,k c′n,k−1

![image 163](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile163.png>)

=

(n − k)(n + k + 1) k(k + 1)

![image 164](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile164.png>)

.

Since c′n,k ≤ ncn,k+1, the analog

- (31)


n

1 1 − α of Proposition 8 holds with u and α as above.

n K + 1

n + K + 1 K + 1 |u|K

c′n,kuk ≤ n

![image 165](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile165.png>)

k=K

5. Fast evaluation of series expansions. All these series expansions are amenable to fast evaluation techniques speciﬁc to multiple-precision arithmetic. Using such fast summation algorithms is critical for achieving good performance at high precision. We now discuss the algorithm that we use for evaluating the series of the previous section.

5.1. Rectangular splitting. We use rectangular splitting [29, 16] to evaluate hypergeometric series with rational parameters where the argument x is a highprecision number. This reduces evaluating a K-term series to O(K) cheap scalar operations (additions and multiplications or divisions by small integer coeﬃcients) and about 2

√

![image 166](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile166.png>)

K expensive nonscalar operations (general multiplications), whereas direct evaluation of the hypergeometric recurrence uses O(K) expensive operations.

Algorithm 2 presents our version of rectangular splitting for the present application. We implement the various series expansions by deﬁning the functions p(k),q(k) used in steps 6 and 17 according to formulae (20), (25), (28), (30).

This algorithm is a generalization of the method for evaluating Taylor series of elementary functions given in [17], which combines rectangular splitting with partially unrolling the recurrence to reduce the number of scalar divisions (which in practice are more costly than scalar multiplications). The terms are computed in the reverse direction to allow using Horner’s rule for the outer multiplications.

Our code uses ball arithmetic for x and s so that no error analysis is needed, and we use a bignum type for c (so no overﬂow can occur regardless of u). For low precision a faster implementation would be possible using ﬁxed-point arithmetic with tight control of the word-level operations as was done for elementary functions in [17].

The algorithm contains two tuning parameters3. The splitting parameter m controls the number m of multiplications for powers versus the number K/m of multiplications for Horner’s rule. The choice m ≈

√

![image 167](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile167.png>)

K is optimal, but when evaluating two

series for the same x (in our case, to compute both Pn(x) and Pn′(x)), the table of powers can be reused, and then m ≈

√

![image 168](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile168.png>)

2K minimizes the total cost.

The unrolling parameter u controls the number of coeﬃcients to collect on a single denominator, reducing the number of divisions to N/u. Ideally, u should be chosen so that bj=a p(j) and bj=a q(j) ﬁt in 1 or 2 machine words. The example value u = 4 is a reasonable default, but as an optimization, one might vary u for each iteration of the main loop to ensure that c always ﬁts in a speciﬁc number of words.

![image 169](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile169.png>)

3Let us stress that the choice of these parameters only aﬀects the performance of the algorithm, not its correctness. The same remark holds every other time we resort to heuristics in this article.

![image 170](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile170.png>)

- Algorithm 2 Evaluation of hypergeometric series using rectangular splitting Input: An arbitrary x, recurrence data p,q ∈ Z[k], integer K ≥ 0, oﬀset Ω ∈ {0, 1}. Output: s = Kk=Ω−1 xk kj=Ω p(j)/q(j)


![image 171](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile171.png>)

- 1: m ← ⌊

√K⌋; precompute [1, x, x2, . . . , xm] ⊲ Tuning parameter: any m ≥ 1 can be used

![image 172](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile172.png>)

- 2: s ← 0; k ← K − 1
- 3: while k ≥ Ω do
- 4: u ← min(4, k + 1 − Ω) ⊲ Tuning parameter: any 1 ≤ u ≤ k + 1 − Ω can be used
- 5: (a,b) ← (k − u + 1, k) ⊲ Unrolled range
- 6: c ← bj=a p(j) ⊲ Small integer coeﬃcient
- 7: while k ≥ a do
- 8: r ← k mod m
- 9: if k = b then
- 10: s ← c · (s + xr) ⊲ Using precomputed power of x
- 11: else
- 12: s ← s + c · xr ⊲ Using precomputed power of x
- 13: end if
- 14: if r = 0 and k = 0 then
- 15: s ← s · xm ⊲ Using precomputed power of x
- 16: end if
- 17: c ← (c/p(k))q(k) ⊲ Exact small integer division
- 18: k ← k − 1
- 19: end while
- 20: s ← s/c
- 21: end while
- 22: return s


![image 173](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile173.png>)

The redundant parameter Ω is a small convenience in the pseudocode. Setting Ω = 1 and adding the constant term separately avoids having to make a special case to prevent division by zero when q(0) = 0.

Due to the scalar operations, rectangular splitting ultimately requires O(K) arithmetic operations with O(p) bit complexity each just like straightforward evaluation of the recurrence, so it is not a genuine asymptotic improvement, but it is an improvement in practice and can give more than a factor 100 speedup at very high precision. It is possible to genuinely reduce the complexity of evaluating a hypergeometric sequence to O(√K log(K)) arithmetic operations using a baby-step giant-step method that employs fast multipoint evaluation, but in practice rectangular splitting performs better until both K and p exceed 106 (see [16]).

![image 174](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile174.png>)

5.2. A note on the bit-burst method. Another technique for fast evaluation of hypergeometric series, called binary splitting, would be useful when p is large and the argument x is a rational number with small numerator and denominator, but this case is not relevant for our application. Binary splitting also forms the basis of the bit-burst method [11, Section 4], which permits evaluating any ﬁxed hypergeometric series at any ﬁxed point without the restriction to simple rational numbers of plain binary splitting to absolute precision p in only O(p) bit operations. Yet, we do not use this method either in our implementation, due to its large overhead.

Indeed, computing Pn(x) by the bit-burst method method requires O(log p) analytic continuation steps, each of which entails two evaluations of general solutions of the Legendre diﬀerential equation (2). These solutions are deﬁned by unit initial values at some intermediate point x0, and can be represented as a power series of radius of convergence 1 − |x| whose coeﬃcients obey recurrences of order two. This

is to be compared with a single series, given by a ﬁrst-order recurrence and typically converging faster, for the expansions considered in subsection 4.1 to subsection 4.3. Thus, the bit-burst method is unlikely to be competitive in the range of precision we are interested in, especially when the asymptotic series can be used.

Nevertheless, it can be shown that the solutions with unit initial values at x0 of (2) occuring at intermediate analytic continuation steps have Taylor coeﬃcients ck

- at x0 bounded by (n2/(1 − |x0|))O(k) uniformly in n and x0. As a consequence, the asymptotic cost of computing any individual root of Pn(x) by the bit-burst method and Newton iteration is O(p) log(n)O(1). For computing all the roots, this approach matches the O(np) estimate of Theorem 1, while allowing for parallelization and requiring less memory. It may hence provide an alternative to multipoint evaluation worth investigating for precisions in the millions of bits.


5.3. Binomial coeﬃcients. The prefactors of both the series expansion at x = 0 and the asymptotic series contain the central binomial coeﬃcient 2nn . We need to compute this factor eﬃciently for any n and precision p. Since 2nn ≈ 4n, it is best to use an exact algorithm when n < Cp for some small constant C > 1/2. We use the binomial function provided by GMP for n < 6p + 200 and otherwise use an asymptotic series for 2nn with error bounds given in [7, Corollaries 1 and 2].

We also need to quickly estimate the magnitude of binomial coeﬃcients for error bounds of series truncations. We have the binary entropy estimate

log2

n k ≤ nG(k/n), G(x) = −xlog2(x) − (1 − x)log2(1 − x)

and the equivalent form

n−k n k

nn kk(n − k)n−k

k

n k ≤

n n − k

- (32)


=

.

![image 175](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile175.png>)

![image 176](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile176.png>)

![image 177](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile177.png>)

The function G(x) can be evaluated cheaply with a precomputed lookup table. A coarse estimate is suﬃcient, since overestimating log2 nk by a few percent only adds a few percent to the running time.

6. Algorithm selection. We ﬁrst use a set of cutoﬀs found experimentally to decide whether to use the basecase recurrence or one of the series expansions. The recurrence is mainly faster for some combinations of p < 1 000, n < 400 when computing (Pn(x),Pn′ (x)) simultaneously and for some combinations of p < 500, n < 100 when computing Pn(x) alone (in all cases subject to some boundaries ε < x <

- 1 − ε); the actual optimal regions are complicated due to diﬀerences in overhead between ﬁxed-point integer arithmetic and ball arithmetic for the respective algorithm implementations. For the actual cutoﬀs used, we refer to the source code.


To select between the series expansion at x = 0, the expansion at x = 1, and the asymptotic series, the following heuristic is used. For each algorithm A, we estimate the evaluation cost as CA = KA(p + pA) where KA is the number of terms required by algorithm A (KA = ∞ if A is the asymptotic series and it does not converge to the required accuracy), p is the precision goal, and pA is the extra precision required by algorithm A due to internal cancellation. For the asymptotic series, we multiply the cost by an extra factor 2 as a penalty for using complex numbers. In the end, we select the algorithm with the lowest CA.

We select KA and estimate pA heuristically using machine precision ﬂoating-point computations, working with logarithmic magnitudes to avoid underﬂow and overﬂow.

0.0010 p = 1000

0.0005

![image 178](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile178.png>)

0.0000

p = 20000

0.04

Time(s)

0.02

0.00

0 θ = π/4 π/2

Fig. 1. Time to evaluate (Pn(x), Pn′ (x)) as the argument x = cos(θ) varies (x = 1 at θ = 0 and x = 0 at θ = π/2), here with n = 10 000, for precision p somewhat smaller than n (top plot) and somewhat larger (bottom plot). The variable θ is used for the horizontal scale in this picture to follow the distribution of the roots (which are clustered near x = 1) linearly.

For example, when A is the asymptotic series, we search for a small KA such that log(KA!/(2n sinθ)K

) ≤ −(p+pA) for some small pA, in accordance with (21). During the actual evaluation of the series expansions, KA and pA are then given; we compute rigorous upper bounds for the truncation error via (19), (21), (26), (29), (31), (32) using ﬂoating-point arithmetic with directed rounding, while additional rounding errors are tracked by the ball arithmetic.

A

The assumption that the running time is a bilinear function of KA and p + pA is not completely realistic, but this cost estimate nonetheless captures the correct asymptotics when

x → 0, x → 1, n → ∞, p → ∞

separately, and hopefully will not be too inaccurate in the transition regions. This is veriﬁed empirically.

Figure 1 illustrates how the time to evaluate (Pn(x),Pn′ (x)) varies with x when the automatic algorithm selection is used. Here, we have timed the case n = 10 000 for two diﬀerent p. For large n and p ≪ n (top plot), a sharp peak appears at the transition between the series expansion at x = 1 and the asymptotic expansion which is used for most x. This peak tends to become taller but narrower for larger n. We could presumably get rid of the peak by implementing another algorithm speciﬁcally for the transition region, but the area under the peak is so small compared to the median baseline that computing all the roots would not be sped up much. For p somewhat larger than n (bottom plot), we observe a smooth transition between the series at x = 1 near the left of the picture and the series at x = 0 used over the most of the range.

7. Benchmarks. As already mentioned, our code for computing values and

roots of Legendre polynomials is part of the Arb library, available from http://arblib. org/. The benchmark results given in this section were obtained using prerelease builds of version 2.13 of Arb. The implementation of the algorithms of this article is located in the ﬁles arb_hypgeom/legendre_p_ui_* of the Arb source tree. In subsection 7.1, we also use some ad hoc code available from this paper’s public git repository4 when comparing the main algorithm with variants absent from the Arb

![image 179](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile179.png>)

4https://github.com/fredrik-johansson/legendrepaper/



# 16 FREDRIK JOHANSSON, MARC MEZZAROBBA

- 100
- 101 p = n/10


p = 64

- 100
- 101


Relativetime

10−1

10−1

10−2

10−2

101 102 103 104 105

101 102 103 104 105

- 100
- 101 p = 10n


p = n

- 100
- 101


Relativetime

10−1

10−1

10−2

10−2

101 102 103 104 105 n

101 102 103 104 105 n

|Fast multipoint evaluation Main algorithm Main algorithm without recurrence|
|---|


Fig. 2. Performance comparison of various methods to evaluate (Pn(x), Pn′ (x)) to p-bit precision for a set of n/2 points 0 < x < 1 distributed like the roots of Pn. The y axis (relative time) shows the time divided by the time using the three-term recurrence in ﬁxed-point arithmetic.

implementation. The source code for the experiments themselves can be found in the same git repository. Except where otherwise noted, we ran the programs under 64-bit Linux on a laptop with a 1.90 GHz Intel Core i5-4300U CPU using a single core.

7.1. Polynomial evaluation. Figure 2 compares the performance of diﬀerent methods for evaluating (Pn(x),Pn′ (x)) on a set of n/2 points distributed like the positive roots of Pn(x) to simulate one stage of Newton iteration at p-bit precision. The time for the three-term recurrence is set to 1, i.e., we divide the other timings by this measurement. The following methods are timed:

- • Our hybrid method (from here on called the “main algorithm”) with automatic selection between the three-term recurrence and diﬀerent series expansions.
- • The main algorithm without the three-term recurrence as the basecase, i.e., using series expansions even for very small n.
- • Fast multipoint evaluation of the expanded polynomials Pn(x) and Pn′ (x). As in subsection 4.2, we expand Pn(√x) for even n and Pn(√x)/√x for odd n and evaluate at x2 since this halves the amount of work. The polynomial coeﬃcients are generated using the hypergeometric recurrence and the fast multipoint evaluation is done using _arb_poly_evaluate_vec_fast_precomp (where the “precomp” suﬃx indicates that the same product tree is used for


![image 181](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile181.png>)

![image 182](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile182.png>)

![image 183](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile183.png>)

both Pn and Pn′ ). The fast multipoint evaluation is done with 2.9n guard bits, which was found experimentally to be suﬃcient for full accuracy.

The crossover point between the three-term recurrence and series expansions usually occurs around n ≈ 102 − 103 (it can be as low as n ≈ 10 if p is much larger). For modest n, the three-term recurrence is much faster than the hypergeometric series (typically by a factor 3-4) due to working with negligible extra precision and thanks to

Time in seconds to compute the degree-n Gauss-Legendre rules with p-bit precision using our code. (For large n and p, the time was estimated by computing a subset of the nodes and weights.)

![image 184](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile184.png>)

n \ p 64 256 1 024 3 333 33 333

![image 185](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile185.png>)

![image 186](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile186.png>)

20 0.000133 0.000229 0.000510 0.00121 0.0198 50 0.000450 0.000870 0.00212 0.00520 0.0710

![image 187](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile187.png>)

![image 188](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile188.png>)

100 0.00138 0.00310 0.00720 0.0163 0.191 200 0.00550 0.0111 0.0267 0.0550 0.589 500 0.0236 0.0610 0.164 0.325 2.61

![image 189](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile189.png>)

![image 190](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile190.png>)

- 1 000 0.0530 0.145 0.584 1.238 9.21

![image 191](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile191.png>)

- 2 000 0.0860 0.298 1.12 4.20 32.6 5 000 0.191 0.665 2.67 14.3 181


![image 192](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile192.png>)

![image 193](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile193.png>)

![image 194](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile194.png>)

10 000 0.350 1.26 4.93 26.6 674 100 000 3.60 12.2 41.3 212 13 637 1 000 000 58.0 146 411 1 850 103 960

![image 195](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile195.png>)

![image 196](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile196.png>)

the low overhead of ﬁxed-point arithmetic. This low overhead is very useful for typical evaluation of Legendre polynomials and generation of quadrature nodes for one or a few machine words of precision. The crossover point could be lowered slightly if we used a similarly optimized ﬁxed-point implementation for the hypergeometric series.

When p is ﬁxed (top left in Figure 2), the main algorithm is a factor O(n) faster than the three-term recurrence since the asymptotic expansion converges to suﬃcient accuracy after O(1) terms for all suﬃciently large n. With the constant precision p = 64, the main algorithm is 3.0 times faster for n = 103 and 30 times faster for n = 104. Conversely, fast multipoint evaluation with constant p is a factor O(n) slower than our algorithm due to the higher internal precision.

When p ∝ n (the three remaining plots in Figure 2), the main algorithm appears to show the same O(n) speedup over the three-term recurrence after the crossover point, at least initially. This speedup should level oﬀ asymptotically, but in practice this only occurs for n larger than 104 where we have already gained a factor 10 or more. The leveling oﬀ is visible in the bottom right ﬁgure (p = 10n).

Fast multipoint evaluation gives a true asymptotic O(n) speedup, but since it has much higher overhead, it only starts to give an improvement over the main algorithm from n ≈ 104 and for p larger than n. When p = n/10, it appears that fast multipoint evaluation will only break even for n much larger than 105. We conclude that fast multipoint evaluation would be worthwhile only for the last few Newton iterations when computing quadrature nodes for exceptionally high precision. Since independent evaluations are more convenient and easy to parallelize, the fast multipoint evaluation method currently seems to have limited practical value for this application.

7.2. Quadrature nodes. The function arb_hypgeom_legendre_p_ui_root(x,

w, n, k, p) sets the output variable x to a ball containing the root of Pn with index k (we use the indexing 0 ≤ k < n, with k = 0 giving the root closest to 1), computed to p-bit precision. It also sets w to the corresponding quadrature weight. We use the formulae in [27, Theorem 1(c)] to compute an initial enclosure with roughly machine precision, followed by reﬁnements with the interval Newton method at doubling precision steps for very high precision. We deduce the quadrature weights thanks to the classical expression as functions of the nodes recalled in equation (3).

Table 1 shows timings for computing degree-n Gauss-Legendre rules to p-bit preci-

Time in seconds for Pari/GP to compute the degree-n Gauss-Legendre quadrature rules with p-bit precision. The numbers in parentheses show the speedup of our code compared to Pari/GP.

![image 197](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile197.png>)

n \ p 64 256 1 024 3 333 33 333

![image 198](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile198.png>)

![image 199](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile199.png>)

20 0.00059 (×4.4) 0.00070 (×3.1) 0.0015 (×2.9) 0.0035 (×2.9) 0.078 (×3.9) 50 0.0043 (×9.6) 0.0050 (×5.8) 0.010 (×4.9) 0.022 (×4.1) 0.43 (×6.0)

![image 200](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile200.png>)

![image 201](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile201.png>)

100 0.020 (×15) 0.023 (×7.4) 0.045 (×6.3) 0.089 (×5.5) 1.5 (×8.1) 200 0.11 (×20) 0.13 (×11) 0.24 (×9.1) 0.45 (×8.1) 6.5 (×11) 500 2.0 (×86) 2.1 (×35) 2.9 (×18) 5.1 (×16) 58 (×22)

![image 202](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile202.png>)

![image 203](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile203.png>)

![image 204](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile204.png>)

1 000 25 (×477) 26 (×180) 29 (×49) 39 (×32) 300 (×33) 2 000 496 (×5 767) 478 (×1 604) 474 (×423) 532 (×127) 1 880 (×58)

![image 205](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile205.png>)

sion by calling this function repeatedly with 0 ≤ k < n/2. Table 2 compares our code to the intnumgaussinit function in Pari/GP which uses a generic polynomial root isolation strategy followed by Newton iteration for high precision reﬁnement. The improvement is most dramatic for small p and large n where we beneﬁt from using asymptotic expansions, but we also obtain a consistent speedup for large p.

For low precision and large n, our implementation is about three orders of magnitude slower than the machine precision code by Bogaert [5] which is reported to compute the nodes and weights for n = 106 in 0.02 seconds on four cores. This diﬀerence is reasonable since we use arbitrary-precision arithmetic, compute rigorous error bounds, and evaluate the Legendre polynomials explicitly whereas Bogaert uses a more sophisticated asymptotic development for both the nodes and the weights.

We also note that we can compute 53-bit ﬂoating-point values with provably correct rounding in about the same time as the 64-bit values, using Ziv’s strategy of increasing the precision. For a ball with relative radius just larger than 2−64, there is less than a 1% probability that the correct 53-bit rounding cannot be determined, in which case that particular node can be recomputed with a few more bits.

Fousse [12] reports a few timings for smaller n and high precision obtained on a 2.40 GHz AMD Opteron 250 CPU. For example, n = 80,p = 500 takes 0.14 seconds (our implementation takes 0.029 seconds) and n = 556,p = 5 000 takes 17 seconds (our implementation takes 0.53 seconds). Of course, these timings are not directly comparable since diﬀerent CPUs were used.

The mathinit program included with version 2.2.19 of D. H. Bailey’s ARPREC library generates Gauss-Legendre quadrature nodes using Newton iteration together with the three-term recurrence for evaluating Legendre polynomials [4, 2]. With default parameters, this program computes the rules of degree n = 3 · 2i+1 for 1 ≤ i ≤ 10 at 3 408 bits of precision, intended as a precomputation for performing degreeadaptive numerical integrations with up to 1 000 decimal digit accuracy. This takes about 1 300 seconds in total (our implementation takes 32 seconds). A breakdown for each degree level is shown in Table 3.

Table 3 also shows the approximation error and the evaluation time (not counting the computation of the nodes and weights) for the degree-n approximations of three diﬀerent integrals, illustrating the relative costs and realistic requirements for n. As motivation for the third integral, we might think of a segment of a Mellin-Barnes integral. The log, Airy and gamma function implementations in Arb are used.

The last few degree levels (with n roughly larger than the number of decimal digits) used by ARPREC tend to be dispensable for well-behaved integrands. A

Left columns: time in seconds to generate 1 000-digit quadrature rules for the degrees n used

by ARPREC. Right columns: for three diﬀerent integrals, the error | − 11 f(x)dx − nk=0−1 wkf(xk)| of the degree-n quadrature rule, and the time to evaluate this degree-n approximation of the integral

at 1 000-digit precision in Arb given the nodes and weights (xk, wk).

n ARPREC Our code − 11log(2+x)dx − 11Ai(10x)dx − 11Γ(1+ix)dx Error Time Error Time Error Time

![image 206](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile206.png>)

![image 207](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile207.png>)

![image 208](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile208.png>)

![image 209](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile209.png>)

![image 210](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile210.png>)

![image 211](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile211.png>)

![image 212](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile212.png>)

![image 213](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile213.png>)

![image 214](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile214.png>)

![image 215](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile215.png>)

![image 216](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile216.png>)

![image 217](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile217.png>)

![image 218](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile218.png>)

![image 219](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile219.png>)

![image 220](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile220.png>)

![image 221](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile221.png>)

12 0.00520 0.000592 10−14 10−1 10−8 24 0.0189 0.00171 10−28 10−9 10−17 48 0.0629 0.00507 10−56 10−34 10−36 96 0.251 0.0163 10−111 10−105 10−73

![image 222](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile222.png>)

![image 223](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile223.png>)

![image 224](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile224.png>)

![image 225](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile225.png>)

![image 226](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile226.png>)

![image 227](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile227.png>)

![image 228](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile228.png>)

![image 229](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile229.png>)

![image 230](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile230.png>)

![image 231](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile231.png>)

![image 232](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile232.png>)

![image 233](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile233.png>)

192 0.974 0.0532 10−222 10−284 0.075 10−146 384 3.83 0.195 10−441 0.023 10−721 0.15 10−293 1.3 768 15.2 0.763 10−881 0.045 < ε 0.29 10−588 2.5

![image 234](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile234.png>)

![image 235](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile235.png>)

![image 236](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile236.png>)

![image 237](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile237.png>)

![image 238](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile238.png>)

![image 239](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile239.png>)

![image 240](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile240.png>)

![image 241](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile241.png>)

![image 242](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile242.png>)

![image 243](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile243.png>)

![image 244](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile244.png>)

![image 245](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile245.png>)

![image 246](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile246.png>)

![image 247](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile247.png>)

![image 248](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile248.png>)

![image 249](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile249.png>)

1 536 60.9 2.82 < ε 0.091 < ε 5.0 3 072 241 9.55 6 144 1 013 18.3

![image 250](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile250.png>)

![image 251](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile251.png>)

![image 252](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile252.png>)

![image 253](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile253.png>)

![image 254](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile254.png>)

![image 255](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile255.png>)

![image 256](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile256.png>)

![image 257](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile257.png>)

Table 4

Left columns: step sizes h, number of evaluation points, and time to compute nodes for double exponential quadrature with Arb at 1 000-digit precision. Right columns: error and evaluation time given precomputed nodes.

h 2n + 1 Time − 11log(2+x)dx − 11Ai(10x)dx − 11Γ(1+ix)dx Error Time Error Time Error Time

![image 258](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile258.png>)

![image 259](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile259.png>)

![image 260](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile260.png>)

![image 261](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile261.png>)

![image 262](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile262.png>)

![image 263](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile263.png>)

![image 264](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile264.png>)

![image 265](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile265.png>)

![image 266](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile266.png>)

![image 267](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile267.png>)

- 2−7 1 989 0.07 10−407 0.12 10−423 0.93 10−314 6.3

![image 268](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile268.png>)

![image 269](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile269.png>)

![image 270](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile270.png>)

- 2−8 3 977 0.14 10−814 0.25 10−909 1.75 10−630 13.0

![image 271](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile271.png>)

![image 272](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile272.png>)

![image 273](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile273.png>)

- 2−9 7 955 0.27 < ε 0.55 < ε 3.49 < ε 25.1


![image 274](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile274.png>)

![image 275](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile275.png>)

![image 276](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile276.png>)

larger n is needed if the path of integration is close to a singularity or if the integrand is highly oscillatory. In such cases, bisecting the interval a few times to reduce the necessary n is often a better tradeoﬀ. On the other hand, since the time to generate nodes with our code only grows linearly with n beyond n ≈ p, increasing the degree further is viable, and potentially useful if the integrand is expensive to evaluate.

In the present work, we refrain from a more detailed discussion of adaptive integration strategies and the computation of error bounds for the integral itself. However, we mention that Arb contains an implementation of a version of the Petras algorithm [28] for rigorous integration. This code uses both adaptive path subdivision and GaussLegendre quadrature with an adaptive choice of n up to n ≈ 0.5p by default, with degree increments n ≈ 2k/2 and automatic caching of the nodes for fast repeated integrations. Node generation takes at most a few seconds for a ﬁrst integration at 1 000-digit precision and a few milliseconds for 100-digit precision.

8. Gauss-Legendre versus Clenshaw-Curtis and the double exponential method. The Clenshaw-Curtis and double exponential (tanh-sinh) quadrature schemes have received much attention as alternatives to Gauss-Legendre quadrature for numerical integration with very high precision [30, 2, 33]. Both schemes typically require a constant factor more evaluation points than Gauss-Legendre rules for equivalent accuracy, but the nodes and weights are easier to compute. Gauss-Legendre quadrature is therefore the best choice when the integrand is expensive to evaluate

or when nodes can be precomputed for several integrations. It is of some interest to compare the relative costs empirically.

Here we assume an analytic integrand with singularities well isolated from the ﬁnite path of integration so that Gauss-Legendre quadrature is a good choice to begin with. As observed in [33], Clenshaw-Curtis often converges with identical rate to Gauss-Legendre for less well-behaved integrands, and the double exponential method is far superior to either Clenshaw-Curtis or Gauss-Legendre for analytic integrands with endpoint singularities.

Clenshaw-Curtis quadrature uses the Chebyshev nodes cos(πk/n),0 ≤ k ≤ n, and the corresponding weights can be expressed by a discrete cosine transform which takes O(n log n) arithmetic operations to compute by an FFT. As a rule of thumb, 2npoint Clenshaw-Curtis quadrature gives the same accuracy as n-point Gauss-Legendre quadrature (for instance, the 384-point Clenshaw-Curtis rule gives errors of 10−229, 10−294 and 10−154 for the three integrals in Table 3). As a point of comparison with Tables 1 and 3, Arb computes a length-2 048 FFT with 1 000-digit precision in 0.09 seconds and a length-32 768 FFT with 10 000-digit precision in 36 seconds. The precomputation for Clenshaw-Curtis quadrature is therefore roughly a factor 20 cheaper than for Gauss-Legendre quadrature with our algorithm, while subsequent integration with cached weights is twice as expensive for Clenshaw-Curtis.

Double exponential quadrature uses the change of variables x = tanh(12π sinht) to convert an integral on (−1,1) to the interval (−∞,+∞) in such a way that the trapezoidal rule −∞ ∞ f(t)dt ≈ h nk=−n f(hk) converges exponentially fast. One generally chooses the discretization parameter as h = 2−j so that both the evaluation points and weights can be recycled for successive levels j = 1,2,3 ..., and n is chosen so that the tail of the inﬁnite series is smaller than 2−p. The 2n + 1 nodes and weights can be computed with n + O(1) exponential function evaluations and O(n) arithmetic operations. Double exponential quadrature with Cn evaluation points typically achieves the same accuracy as n-point Gauss-Legendre quadrature, where C is slightly larger than for Clenshaw-Curtis, e.g. C ≈ 5; see Table 4. The time to compute nodes and weights is comparable to Clenshaw-Curtis quadrature (around 0.2 seconds for 1 000-digit precision and two minutes for 10 000-digit precision).

![image 277](<2018-johansson-fast-rigorous-arbitrary-precision-computation_images/imageFile277.png>)

In summary, for integration with precision in the neighborhood of 103 to 104 digits, computing n nodes with our algorithm is about an order of magnitude more expensive than performing n elementary function (e.g. exp or log) evaluations or computing an FFT of length n. This makes Gauss-Legendre quadrature competitive for computing more than m integrals (assuming that nodes and weights are cached), for a single integral requiring splitting into m subintervals, or for a single integral when the integrand costs more than m elementary function evaluations, where m ≈ 101.

The picture becomes more complicated when accounting for the method used to estimate errors in an adaptive integration algorithm. One drawback of the GaussLegendre scheme is that the nodes are not nested, so that an adaptive strategy that repeatedly doubles the quadrature degree requires twice as many function evaluations as the degree of the ﬁnal level. This drawback disappears if the error is estimated by extrapolation or if an error bound is computed a priori as in the Petras algorithm [28].

9. Conclusion. In [2], it was claimed that “There is no known scheme for generating Gaussian abscissa–weight pairs that avoids [the] quadratic dependence on n. High-precision abscissas and weights, once computed, may be stored for future use. But for truly extreme-precision calculations – i.e., several thousand digits or more – the cost of computing them even once becomes prohibitive”.

In this quote, “quadratic dependence” refers to the number of arithmetic operations. We may remark that using asymptotic expansions in the evaluation of Legendre polynomials avoids the quadratic dependence on n for ﬁxed precision p, and Theorem 1 avoids the implied cubic time dependence on n when n = O(p). In fact, Theorem 1 implies that Gauss-Legendre, Clenshaw-Curtis and double exponential quadrature have the same quasi-optimal asymptotic bit complexity, up to logarithmic factors.

Our experiments show that the algorithm in Theorem 1 hardly is worthwhile. However, the hybrid method described in sections 2 to 5 does achieve a signiﬁcant speedup for practical p and n which allows us to compute Gauss-Legendre quadrature rules for 1 000-digit integration in 1-2 seconds and for 10 000-digit integration in 1020 minutes on a single core. This is not prohibitively expensive compared to the repeated evaluation of typical integrands, especially if several integrations are needed. Parallelization is also trivial since all roots are computed independently.

A natural extension of this work would be to consider Gaussian quadrature rules for diﬀerent weight functions. The techniques should transfer to other classical orthogonal polynomials (Jacobi, Hermite, Laguerre, etc.) which likewise have hypergeometric expansions and satisfy three-term recurrence relations. The main obstacle might be to obtain large-n asymptotic expansions with suitable error bounds.

Acknowledgements. We are indebted to Nick Trefethen and two anonymous referees for their useful comments. We also thank Bruno Salvy for pointing out Petras’ paper [27]. Marc Mezzarobba was supported in part by ANR grant ANR-14-CE250018-01 (FastRelax).

REFERENCES

- [1] V. Antonov and K. Holsevnikovˇ , An estimate of the remainder in the expansion of the generating function for the Legendre polynomials (generalization and improvement of Bernstein’s inequality), Vestnik Leningrad Univ. Mat., 13 (1981), pp. 163–166. English translation of [37] by H. H. McFadden.
- [2] D. H. Bailey and J. M. Borwein, High-precision numerical integration: Progress and challenges, J. Symbolic Comput., 46 (2011), pp. 741–754, http://dx.doi.org/10.1016/j.jsc.2010. 08.010.
- [3] D. H. Bailey, J. M. Borwein, and R. E. Crandall, Integrals of the Ising class, J. Phys. A, 39 (2006), p. 12271, http://dx.doi.org/10.1088/0305-4470/39/40/001.
- [4] D. H. Bailey, H. Yozo, X. S. Li, and B. Thompson, ARPREC: An arbitrary precision computation package, 2002.
- [5] I. Bogaert, Iteration-free computation of Gauss–Legendre quadrature nodes and weights, SIAM J. Sci. Comput., 36 (2014), pp. A1008–A1026, http://dx.doi.org/10.1137/140954969.
- [6] I. Bogaert, B. Michiels, and J. Fostier, O(1) computation of Legendre polynomials and Gauss–Legendre nodes and weights for parallel computing, SIAM J. Sci. Comput., 34 (2012), pp. C83–C101, http://dx.doi.org/10.1137/110855442.
- [7] R. P. Brent, Asymptotic approximation of central binomial coeﬃcients with rigorous error bounds, 2016, http://arxiv.org/abs/1608.04834.
- [8] R. P. Brent and P. Zimmermann, Modern Computer Arithmetic, Cambridge University Press, 2010, http://www.loria.fr/~zimmerma/mca/mca-cup-0.5.7.pdf.
- [9] D. Broadhurst, Feynman integrals, L-series and Kloosterman moments, Feb. 2016, http:// arxiv.org/abs/1604.03057.
- [10] Y. Chow, L. Gatteschi, and R. Wong, A Bernstein-type inequality for the Jacobi polynomial, Proc. Amer. Math. Soc., 121 (1994), pp. 703–709, http://dx.doi.org/10.2307/2160265.
- [11] D. V. Chudnovsky and G. V. Chudnovsky, Computer algebra in the service of mathematical physics and number theory, in Computers in Mathematics, D. V. Chudnovsky and R. D. Jenks, eds., vol. 125 of Lecture Notes in Pure and Applied Mathematics, Dekker, 1990, pp. 109–232. Talks from the International Conference on Computers and Mathematics, Stanford University, 1986.
- [12] L. Fousse, Accurate multiple-precision Gauss–Legendre quadrature, in 18th IEEE Symposium


- on Computer Arithmetic, ARITH’07, IEEE, 2007, pp. 150–160.
- [13] G. H. Golub and J. H. Welsch, Calculation of Gauss quadrature rules, Math. Comp., 23

(1969), pp. 221–230, http://dx.doi.org/10.1007/BF01389877.

- [14] T. Granlund and the GMP development team, GNU MP: The GNU Multiple Precision Arithmetic Library, 6.1.2 ed., 2017, https://gmplib.org/.
- [15] N. Hale and A. Townsend, Fast and accurate computation of Gauss–Legendre and Gauss– Jacobi quadrature nodes and weights, SIAM J. Sci. Comput., 35 (2013), pp. A652–A674, http://dx.doi.org/10.1137/120889873.
- [16] F. Johansson, Evaluating parametric holonomic sequences using rectangular splitting, in Proceedings of the 39th International Symposium on Symbolic and Algebraic Computation, ISSAC ’14, New York, NY, USA, 2014, ACM, pp. 256–263, http://dx.doi.org/10.1145/ 2608628.2608629.
- [17] F. Johansson, Eﬃcient implementation of elementary functions in the medium-precision range, in 22nd IEEE Symposium on Computer Arithmetic, ARITH22, 2015, pp. 83–89, http://dx.doi.org/10.1109/ARITH.2015.16.
- [18] F. Johansson, Computing hypergeometric functions rigorously, 2016, http://arxiv.org/abs/ 1606.06977.
- [19] F. Johansson, Arb: eﬃcient arbitrary-precision midpoint-radius interval arithmetic, IEEE Trans. Comput., 66 (2017), pp. 1281–1292, http://dx.doi.org/10.1109/TC.2017.2690633.
- [20] F. Johansson and I. V. Blagouchine, Computing Stieltjes constants using complex integration, June 2018, http://arxiv.org/abs/1804.01679.
- [21] A. Kobel and M. Sagraloff, Fast approximate polynomial multipoint evaluation and applications, 2013, https://arxiv.org/abs/1304.8069.
- [22] M. A. Kowalski, A. G. Werschulz, and H. Wozniakowski´ , Is Gauss quadrature optimal for analytic functions?, Numer. Math., 47 (1985), pp. 89–98.
- [23] P. Molin, Numerical Integration and L-Functions Computations, theses, Universit´e Sciences et Technologies - Bordeaux I, Oct. 2010.
- [24] R. E. Moore, Methods and applications of interval analysis, SIAM, 1979.
- [25] F. W. J. Olver, Asymptotics and Special Functions, A K Peters, Wellesley, MA, 1997.
- [26] F. W. J. Olver, D. W. Lozier, R. F. Boisvert, and C. W. Clark, NIST Handbook of Mathematical Functions, Cambridge University Press, New York, 2010.
- [27] K. Petras, On the computation of the Gauss–Legendre quadrature formula with a given precision, J. Comput. Appl. Math., 112 (1999), pp. 253–267, http://dx.doi.org/10.1016/ S0377-0427(99)00225-3.
- [28] K. Petras, Self-validating integration and approximation of piecewise analytic functions, J. Comput. Appl. Math., 145 (2002), pp. 345–359, http://dx.doi.org/10.1016/ S0377-0427(01)00586-6.
- [29] D. M. Smith, Eﬃcient multiple-precision evaluation of elementary functions, Math. Comp., 52 (1989), pp. 131–134, http://myweb.lmu.edu/dmsmith/MComp1989.pdf.
- [30] H. Takahasi and M. Mori, Double exponential formulas for numerical integration, Publ. Res. Inst. Math. Sci., 9 (1974), pp. 721–741, http://dx.doi.org/10.2977/prims/1195192451.
- [31] The PARI Group, PARI/GP version 2.9.4, Univ. Bordeaux, 2017, http://pari.math. u-bordeaux.fr/.
- [32] A. Townsend, The race for high order Gauss–Legendre quadrature, SIAM News, (2015), pp. 1– 3, http://math.mit.edu/~ajt/papers/QuadratureEssay.pdf.
- [33] L. N. Trefethen, Is Gauss quadrature better than Clenshaw–Curtis?, SIAM Rev., 50 (2008), pp. 67–87, http://dx.doi.org/10.1137/060659831.
- [34] L. N. Trefethen, Six myths of polynomial interpolation and quadrature, 2011, https://people. maths.ox.ac.uk/trefethen/mythspaper.pdf.
- [35] J. van der Hoeven, Ball arithmetic, tech. report, HAL, 2009, http://hal.archives-ouvertes.fr/ hal-00432152/fr/.
- [36] J. Wimp, Computation with Recurrence Relations, Pitman, Boston, 1984.
- [37] В. А. Антонов and К. В. Холшевников, Оценка остатка разложения производящей функции полиномов Лежандра (обобщение и уточнение неравенства Бернштейна), Вестник Ленинградского университета (Математика), no. 13 (1980), pp. 5–7. English translation in [1].


