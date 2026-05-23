## Arb: Efﬁcient Arbitrary-Precision Midpoint-Radius Interval Arithmetic

Fredrik Johansson

Abstract—Arb is a C library for arbitrary-precision interval arithmetic using the midpoint-radius representation, also known as ball arithmetic. It supports real and complex numbers, polynomials, power series, matrices, and evaluation of many special functions. The core number types are designed for versatility and speed in a range of scenarios, allowing performance that is competitive with non-interval arbitrary-precision types such as MPFR and MPC ﬂoating-point numbers. We discuss the low-level number representation, strategies for precision and error bounds, and the implementation of efﬁcient polynomial arithmetic with interval coefﬁcients.

Index Terms—Arbitrary-precision arithmetic, interval arithmetic, ﬂoating-point arithmetic, polynomial arithmetic

arXiv:1611.02831v1[cs.MS]9Nov2016

✦

![image 1](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile1.png>)

![image 2](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile2.png>)

- 1 INTRODUCTION


# I

NTERVAL arithmetic allows computing with real numbers in a mathematically rigorous way by automatically track-

We argue that midpoint-radius arithmetic not only is a viable alternative to endpoint-based interval arithmetic, but competitive with ﬂoating-point arithmetic in contexts where arbitrary precision is used, e.g. in computer algebra systems. The small overhead of tracking errors automatically, if not completely negligible, affords us the freedom to use more complex algorithms with conﬁdence in the output.

ing error bounds through the steps of a program [1]. Success stories of interval arithmetic in mathematical research include Hales’s proof of the Kepler conjecture [2], Helfgott’s proof of the ternary Goldbach conjecture [3], and Tucker’s positive solution of Smale’s 14th problem concerning the existence of the Lorenz attractor [4].

Our focus is on “narrow” intervals, say [π ± 2−30]; that is, we are more concerned with bounding arithmetic error starting from precise input than bracketing function images on “wide” intervals, say sin([3,4]). For the latter job, high-degree Taylor approximations are an alternative to direct application of interval arithmetic. Arb has good support for Taylor expansion (automatic differentiation), though presently only in one variable.

The main drawback of interval arithmetic is that the bounds can blow up catastrophically, perhaps only telling us that x ∈ [−∞,∞]. Assuming that all input intervals can be made sufﬁciently precise, increasing the working precision is an effective way to circumvent this problem. One well-known implementation of arbitrary-precision interval arithmetic is MPFI [5], which builds on the MPFR [6] library for arbitrary-precision ﬂoating-point arithmetic with correct rounding. MPFI extends the principles of MPFR to provide a well-deﬁned semantics by guaranteeing that each built-in interval operation produces the smallest possible output interval (of course, composing operations will still generally lead to overestimation). Due to the difﬁculty of computing optimal ﬂoating-point enclosures, MPFR, MPFI and the complex MPFR extension MPC [7] are currently limited to a small set of built-in functions.

We use the ball representation for real numbers, constructing complex numbers, polynomials and matrices out of real balls. This is the most convenient approach, but we note that the concept of ball arithmetic can be generalized directly to normed vector spaces, e.g. giving disks for complex numbers and norm perturbation bounds for matrices, which has some advantages [8]. Ball arithmetic in some form is an old idea, previously used in e.g. Mathemagix [9] and iRRAM [10]. Our contributions include low-level optimizations as well as the scope of high-level features.

In this paper, we present Arb, a C library for arbitraryprecision arithmetic using midpoint-radius intervals. In midpoint-radius arithmetic, or ball arithmetic, a real number is represented by an enclosure [m±r] where the midpoint m and the radius r are ﬂoating-point numbers. The advantage of this representation over the more traditional endpointbased intervals [a,b] used in MPFI is that only m needs to be tracked to full precision; a few digits sufﬁce for r, as in

One of our goals is fast, reliable evaluation of transcendental functions, which are needed with high precision in many scientiﬁc applications [11]. Arb has rigorous implementations of elementary, complete and incomplete gamma and beta, zeta, polylogarithm, Bessel, Airy, exponential integral, hypergeometric, modular, elliptic and other special functions with full support for complex variables. The speed is typically better than previous arbitrary-precision software, despite tracking error bounds. The purpose of this paper is not to describe algorithms for particular mathematical functions (we refer to [12], [13], [14]). Instead, we focus on how the core arithmetic in Arb facilitates implementations.

π ∈ [3.14159265358979323846264338328± 1.07 · 10−30].

At high precision, this costs (1+ε) as much as ﬂoating-point arithmetic, saving a factor two over endpoint intervals.

![image 3](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile3.png>)

A preliminary report about Arb was presented in [15]; however, the core arithmetic has subsequently been rewritten and many features have been added. The present paper offers a more detailed view and covers new developments.

• F. Johansson was with Inria Bordeaux-Sud-Ouest and the University of Bordeaux, 33400 Talence, France. E-mail: fredrik.johansson@gmail.com

### 2 FEATURES AND EXAMPLE APPLICATIONS

Arb is free software distributed under the GNU Lesser General Public License (LGPL). The public git repository is https://github.com/fredrik-johansson/arb/ and documentation is available at http://arblib.org/. The code is threadsafe, written in portable C, and builds in most common environments. An extensive test suite is included.

Arb depends on GMP [16] or the fork MPIR [17] for low-level bignum arithmetic, MPFR for some operations on ﬂoating-point numbers and for testing (MPFR numbers are not used directly), and FLINT [18] for arithmetic over the exact rings Z, Q and Z/nZ and polynomials over these rings. Conceptually, Arb extends FLINT’s numerical tower to the rings R and C, and follows similar coding conventions as FLINT. Arb provides the following core types:

- • arf_t - arbitrary-precision ﬂoating-point numbers
- • mag_t - unsigned ﬂoating-point numbers
- • arb_t - real numbers, represented in midpointradius interval form [m ± r] where m is an arf_t and r is a mag_t
- • acb_t - complex numbers, represented in Cartesian form a + bi where a,b are arb_t real intervals
- • arb_poly_t, acb_poly_t - real and complex dense univariate polynomials
- • arb_mat_t, acb_mat_t - dense matrices


Each type comes with a set of methods. For example, arb_add(z, x, y, prec) sets the arb_t variable z to the sum of the arb_t variables x and y, performing the computation at prec bits of precision.

In the git version as of November 2016, there are around 1850 documented methods in total, including alternative implementations of the same mathematical operation. For example, there are methods for computing the Riemann zeta function ζ(s) using Borwein’s algorithm, the Euler product, Euler-Maclaurin summation, and the Riemann-Siegel formula. The user will most likely only need the “top-level” methods arb_zeta, acb_zeta, arb_poly_zeta_series or acb_poly_zeta_series (the latter two compute series expansions, i.e. derivatives with respect to s) which automatically try to choose the best algorithm depending on s and the precision, but methods for speciﬁc algorithms are available for testing purposes and

- as an option if the default choice is suboptimal. Arb includes some 650 test programs that cover almost


all the methods. Typically, a test program exercises a single method (or variants of the same method) by generating 103 to 106 random inputs, computing the same mathematical quantity in two different ways (by using a functional identity, switching the algorithm, or varying parameters such as the precision), and verifying that the results are consistent, e.g. that two intervals that should represent the same real number overlap. Random intervals are generated non-uniformly to hit corner cases with high probability.

lack of operator overloading and high-level generic data types makes C cumbersome for many potential users. Highlevel interfaces to Arb are available in the Python-based SageMath computer algebra system [19], a separate Python module1, and the Julia computer algebra package Nemo2.

Perhaps the biggest drawback of C as an implementation language is that it provides poor protection against simple programming errors. This makes stringent unit testing particularly important. We have found running unit tests with Valgrind/Memcheck [20] to be indispensable for detecting memory leaks, uses of uninitialized variables, outof-bounds array accesses, and other similar mistakes.

Arb is designed to be thread-safe, and in particular, avoids global state. However, thread-local storage is used for some internal caches. To avoid leaking memory, the user should call flint_cleanup() before exiting a thread, which frees all caches used by FLINT, MPFR and Arb. A few Arb methods (such as matrix multiplication) can use several threads internally, but only one thread is used by default; the user can set the number of threads available for internal use with flint_set_num_threads().

#### 2.2 Numerical evaluation with guaranteed accuracy

We now turn to demonstrating typical use. With arbitraryprecision interval arithmetic, a formula can often be evaluated to a desired tolerance by trying with few guard bits and simply starting over with more guard bits if the resulting interval is too wide. The precision steps can be ﬁne-tuned for a speciﬁc problem, but generally speaking, repeatedly doubling either the total precision or the guard bits tends to give close to optimal performance. The following program computes sin(π + e−10000) to a relative accuracy of 53 bits.

#include "arb.h" int main() {

long prec; arb_t x, y; arb_init(x); arb_init(y); for (prec = 64; ; prec *= 2) { arb_const_pi(x, prec); arb_set_si(y, -10000); arb_exp(y, y, prec); arb_add(x, x, y, prec); arb_sin(y, x, prec); arb_printn(y, 15, 0); printf("\n"); if (arb_rel_accuracy_bits(y) >= 53)

break;

} arb_clear(x); arb_clear(y); flint_cleanup();

}

The output is:

[+/- 6.01e-19]

- [+/- 2.55e-38] [+/- 8.01e-77]

- [+/- 8.64e-154] [+/- 5.37e-308]

[+/- 3.63e-616] [+/- 1.07e-1232]

- [+/- 9.27e-2466] [-1.13548386531474e-4343 +/- 3.91e-4358]




#### 2.1 Software and language issues

C is a suitable language for library development due to its speed, support for ﬁne-grained memory management, fast compilation, portability, and ease of interfacing from other languages. The last point is important, since the

- 1. https://github.com/fredrik-johansson/python-ﬂint
- 2. http://nemocas.org


The Arb repository includes example programs that use similar precision-increasing loops to solve various standard test problems such as computing the n-th iterate of the logistic map, the determinant of the n×n Hilbert matrix, or all the complex roots of a given degree-n integer polynomial.

- 2.2.1 Floating-point functions with guaranteed accuracy

The example program shown above is easily turned into a function that takes double input, approximates some mathematical function to 53-bit accuracy, and returns the interval midpoint rounded to a double. Of course, the precision goal can be changed to any other number of bits, and any other ﬂoating-point type can be used.

We have created a C header ﬁle that wraps Arb to provide higher transcendental functions for the C99 double complex type.3 This code is obviously not competitive with optimized double complex implementations, but few such implementations are available that give accurate results on the whole complex domain. The speed is highly competitive with other arbitrary-precision libraries and computer algebra systems, many of which often give wrong results. We refer to [14] for benchmarks.

We mention a concrete use in computational hydrogeophysics: Kuhlman4 has developed a Fortran program for unconﬁned aquifer test simulations, where one model involves Bessel functions Jν(z) and Kν(z) with fractional ν and complex z. Due to numerical instability in the simulation approach, the Bessel functions are needed with quad-precision (113-bit) accuracy. A few lines of code are used to convert from Fortran quad-precision types to Arb intervals, compute the Bessel functions accurately with Arb, and convert back.

- 2.2.2 Correct rounding We have developed an example program containing Arbbased implementations of all the transcendental functions available in version 3.1.3 of MPFR, guaranteeing correct rounding to a variable number of bits in any of the MPFR supported rounding modes (up, down, toward zero, away from zero, and to nearest with ties-to-even) with correct detection of exact cases, taking mpfr_t input and output variables. This requires approximately 500 lines of wrapper code in total for all functions. The following simple termination test ensures that rounding the midpoint of x to 53 bits in the round-to-nearest mode will give the correct result for this rounding mode:


if (arb_can_round_mpfr(x, 53, MPFR_RNDN))

...

Correct rounding is more difﬁcult than simply targeting a few ulps error, due the table maker’s dilemma. Input where the function value is an exact ﬂoating-point number, such as x = 2n for the function log2(x) = log(x)/ log(2), would cause the precision-increasing loop to repeat forever if the interval evaluation always produced [n±ε] with ε > 0. Such exact cases are handled in the example program. However, this code has not yet been optimized for asymptotic cases where the function value is close to an exact ﬂoatingpoint number. For example, tanh(10000) ≈ 1 to within

- 3. https://github.com/fredrik-johansson/arbcmath
- 4. https://github.com/klkuhlm/unconﬁned


28852 bits. MPFR internally detects such input and quickly returns either 1 or 1−ε according to the rounding mode. To compute tanh(2300), special handling is clearly necessary. With the exception of such degenerate rounding cases, the Arb-based functions generally run faster than MPFR’s builtin transcendental functions. Note that the degenerate cases for correct rounding do not affect normal use of Arb, where correct rounding is not needed.

Testing the Arb-based implementations against their MPFR equivalents for randomly generated inputs revealed cases where MPFR 3.1.3 gave incorrect results for square roots, Bessel functions, and the Riemann zeta function. All cases involved normal precision and input values, which easily could have occurred in real use. The square root bug was caused by an edge case in bit-level manipulation of the mantissa, and the other two involved incorrect error analysis. The MPFR developers were able to ﬁx the bugs quickly, and in response strengthened their test code.

The discovery of serious bugs in MPFR, a mature library used by major applications such as SageMath and the GNU Compiler Collection (GCC), highlights the need for peer review, cross-testing, and ideally, computer-assisted formal veriﬁcation of mathematical software. Automating error analysis via interval arithmetic can eliminate certain types of numerical bugs, and should arguably be done more widely. One must still have in mind that interval arithmetic is not a cure for logical errors, faulty mathematical analysis, or bugs in the implementation of the interval arithmetic itself.

#### 2.3 Exact computing

In ﬁelds such as computational number theory and computational geometry, it is common to rely on numerical approximations to determine discrete information such as signs of numbers. Interval arithmetic is useful in this setting, since one can verify that an output interval contains only points that are strictly positive or negative, encloses exactly one integer, etc., which then must be the correct result. We illustrate with three examples from number theory.

2.3.1 The partition function

Some of the impetus to develop Arb came from the problem of computing the integer partition function p(n), which counts the number of ways n can be written as a sum of positive integers, ignoring order. The famous HardyRamanujan-Rademacher formula (featuring prominently in the plot of the 2015 ﬁlm The Man Who Knew Inﬁnity) expresses p(n) as an inﬁnite series of transcendental terms

∞

Ak(n) k

p(n) = C(n)

I3/2

![image 4](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile4.png>)

k=1

π k

![image 5](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile5.png>)

![image 6](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile6.png>)

1 24

- 2

![image 7](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile7.png>)

- 3


n −

![image 8](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile8.png>)

, (1)

where I3/2(x) = (2/π)1/2x−3/2(xcosh(x) − sinh(x)), C(n) = 2π(24n − 1)−3/4, and Ak(n) denotes a certain complex exponential sum. If a well-chosen truncation of (1) is evaluated using sufﬁciently precise ﬂoating-point arithmetic, one obtains a numerical approximation y ≈ p(n) such that p(n) = ⌊y+1/2⌋. Getting this right is far from trivial, as evidenced by the fact that past versions of Maple computed p(11269),p(11566),... incorrectly [21].

It was shown in [22] that p(n) can be computed in quasioptimal time, i.e. in time essentially linear in log(p(n)), by

careful evaluation of (1). This algorithm was implemented using MPFR arithmetic, which required a laborious ﬂoatingpoint error analysis to ensure correctness. Later reimplementing the algorithm in Arb made the error analysis nearly trivial and allowed improving speed by a factor two (in part because of faster transcendental functions in Arb, and in part because more aggressive optimizations could be made).

Arb computes the 111391-digit number p(1010) in 0.3 seconds, whereas Mathematica 9.0 takes one minute. Arb has been used to compute the record value p(1020) = 1838176508 ...6788091448, an integer with more than 11 billion digits.5 This took 110 hours (205 hours split across two cores) with 130 GB peak memory usage.

Evaluating (1) is a nice benchmark problem for arbitraryprecision software, because the logarithmic magnitudes of the terms follow a hyperbola. For n = 1020, one has to evaluate a few terms to billions of digits, over a billion terms to low precision, and millions of terms to precisions everywhere in between, exercising the software at all scales. For large n, Arb spends roughly half the time on computing π and sinh(x) in the ﬁrst term of (1) to full precision.

The main use of computing p(n) is to study residues p(n) mod m, so getting the last digit right is crucial. Computing the full value of p(n) via (1) and then reducing mod m is the only known practical approach for huge n.

- 2.3.2 Class polynomials

The Hilbert class polynomial HD ∈ Z[x] (where D < 0 is an imaginary quadratic discriminant) encodes information about elliptic curves. Applications of computing the coefﬁcients of HD include elliptic curve primality proving and generating curves with desired cryptographic properties. An efﬁcient way to construct HD uses the factorization

HD =

k

(x − j(τk))

where τk are complex algebraic numbers and j(τ) is a modular function expressible in terms of Jacobi theta functions. Computing the roots numerically via the j-function and expanding the product yields approximations of the coefﬁcients of HD, from which the exact integers can be deduced if sufﬁciently high precision is used. Since HD has degree O( |D|) and coefﬁcients of size 2O(

![image 9](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile9.png>)

√

![image 10](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile10.png>)

|D|), both the numerical evaluation of j(τ) and the polynomial arithmetic needs to be efﬁcient and precise for large |D|. An implementation of this algorithm in Arb is as fast as the stateof-the-art ﬂoating-point implementation by Enge [23], and checking that each coefﬁcient’s computed interval contains a unique integer gives a provably correct result.

- 2.3.3 Cancellation and the Riemann hypothesis


In [13], Arb was used to rigorously determine values of the ﬁrst n = 105 Keiper-Li coefﬁcients and Stieltjes constants, which are certain sequences of real numbers deﬁned in terms of high-order derivatives of the Riemann zeta function. The Riemann hypothesis is equivalent to the statement that all Keiper-Li coefﬁcients λn are positive, and ﬁnding an explicit λn < 0 would constitute a disproof. Unfortunately

5. http://fredrikj.net/blog/2014/03/new-partition-function-record/

for the author, the data agreed with the Riemann hypothesis and other open conjectures.

These computations suffer from severe cancellation in the evaluated formulas, meaning that to compute an n-th derivative to just a few signiﬁcant digits, or indeed just to determine its sign, a precision of n bits has to be used; in other words, for n = 105, Arb was used to manipulate polynomials with 1010 bits of data. Acceptable performance was possible thanks to Arb’s use of asymptotically fast polynomial arithmetic, together with multithreading for parts of the computation that had to use slower algorithms.

More recently, Arb has been used to study generalizations of the Keiper-Li coefﬁcients [24]. Related to this example, Matiyasevich and Beliakov have also performed investigations of Dirichlet L-functions that involved using Arb to locate zeros to very high precision [25], [26].

### 3 LOW-LEVEL NUMBER TYPES

In Arb version 1.0, described in [15], the same ﬂoatingpoint type was used for both the midpoint and radius of an interval. Since version 2.0, two different types are used. An arf_t holds an arbitrary-precision ﬂoating-point number (the midpoint), and a mag_t represents a ﬁxed-precision error bound (the radius). This specialization requires more code, but enabled factor-two speedups at low precision, with clear improvements up to several hundred bits. The organization of the data types is shown in Table 1. In this section, we explain the low-level design of the arf_t and mag_t types and how they inﬂuence arb_t performance.

3.1 Midpoints An arf_t represents a dyadic number

a · 2b, a ∈ Z[21] \ {0}, 12 ≤ |a| < 1, b ∈ Z, or one of the special values {0,−∞,+∞,NaN}. Methods are provided for conversions, comparisons, and arithmetic operations with correct directional rounding. For example,

![image 11](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile11.png>)

![image 12](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile12.png>)

c = arf_add(z, x, y, 53, ARF_RND_NEAR);

sets z to the sum of x and y, correctly rounded to the nearest ﬂoating-point number with a 53-bit mantissa (with roundto-even on a tie). The returned int ﬂag c is zero if the operation is exact, and nonzero if rounding occurs.

An arf_t variable just represents a ﬂoating-point value, and the precision is considered a parameter of an operation. The stored mantissa a can have any bit length, and uses dynamic allocation, much like GMP integers. In contrast, MPFR stores the precision to be used for a result as part of each mpfr_t variable, and always allocates space for full precision even if only a few bits are used.

The arf_t approach is convenient for working with exact dyadic numbers, in particular integers which can grow dynamically from single-word values until they reach the precision limit and need to be rounded. This is particularly useful for evaluation of recurrence relations, in calculations with polynomials and matrices, and in any situation where the inputs are low-precision ﬂoating-point values but much higher precision has to be used internally. The working precision in an algorithm can also be adjusted on the ﬂy without changing each variable.

TABLE 1 Data layout of Arb ﬂoating-point and interval types.

![image 13](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile13.png>)

Exponent (fmpz_t) 1 word Limb count + sign bit 1 word

![image 14](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile14.png>)

![image 15](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile15.png>)

![image 16](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile16.png>)

![image 17](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile17.png>)

![image 18](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile18.png>)

![image 19](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile19.png>)

![image 20](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile20.png>)

- Limb 0 Allocation count 1 word

![image 21](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile21.png>)

![image 22](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile22.png>)

![image 23](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile23.png>)

- Limb 1 Pointer to ≥3 limbs 1 word arf_t = 4 words


![image 24](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile24.png>)

![image 25](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile25.png>)

![image 26](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile26.png>)

![image 27](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile27.png>)

![image 28](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile28.png>)

Exponent (fmpz_t) 1 word Limb 1 word mag_t = 2 words

![image 29](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile29.png>)

![image 30](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile30.png>)

![image 31](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile31.png>)

![image 32](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile32.png>)

![image 33](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile33.png>)

![image 34](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile34.png>)

![image 35](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile35.png>)

![image 36](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile36.png>)

![image 37](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile37.png>)

Midpoint (arf_t) 4 words Radius (mag_t) 2 words arb_t = 6 words

![image 38](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile38.png>)

![image 39](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile39.png>)

![image 40](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile40.png>)

![image 41](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile41.png>)

![image 42](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile42.png>)

![image 43](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile43.png>)

![image 44](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile44.png>)

![image 45](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile45.png>)

![image 46](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile46.png>)

Real part (arb_t) 6 words Imaginary part (arb_t) 6 words acb_t = 12 words

![image 47](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile47.png>)

![image 48](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile48.png>)

![image 49](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile49.png>)

![image 50](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile50.png>)

![image 51](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile51.png>)

![image 52](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile52.png>)

![image 53](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile53.png>)

![image 54](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile54.png>)

- 3.1.1 Mantissas


The mantissa 21 ≤ |a| < 1 is stored as an array of words (limbs) in little endian order, allowing GMP’s mpn

![image 55](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile55.png>)

methods to be used for direct manipulation. Like MPFR’s mpfr_t, the mantissa is always normalized so that the top bit of the top word is set. This normalization makes addition slower than the unnormalized representation used by GMP’s mpf_t, but it is more economical at low precision and allows slightly faster multiplication. For error bound calculations, it is also extremely convenient that the exponent gives upper and lower power-of-two estimates.

The second word in the arf_t struct encodes a sign bit and the number of words n in the mantissa, with n = 0 indicating a special value. The third and fourth words encode the mantissa. If n ≤ 2, the these words store the limbs directly. If n > 2, the third word speciﬁes the number m ≥ n of allocated limbs, and the fourth word is a pointer

- to m limbs, with the lowest n being in use. The mantissa is always normalized so that its least signiﬁcant limb is nonzero, and new space is allocated dynamically if n > m limbs need to be used. If the number of used limbs shrinks
- to n ≤ 2, the heap-allocated space is automatically freed. On a 64-bit machine, an arf_t with at most a 128-bit


mantissa (and a small exponent) is represented entirely by a 256-bit struct without separate heap allocation, thereby improving memory locality and speeding up creation and destruction of variables, and many operations use fast inlined code speciﬁcally for the n ≤ 2 cases. When working

- at p ≥ 129-bit precision, this design still speeds up common special values such as all integers |x| < 2128 and double constants, including the important special value zero.


In contrast, an mpfr_t consists of four words (256 bits), plus ⌈p/64⌉ more words for the mantissa at p-bit precision which always need to be allocated. The MPFR format has the advantage of being slightly faster for generic fullprecision ﬂoating-point values, especially at precision just over 128 bits, due to requiring less logic for dealing with different lengths of the mantissa.

3.1.2 Exponents

The ﬁrst word in the arf_t struct represents an arbitrarily large exponent as a FLINT integer, fmpz_t. An fmpz_t

with absolute value at most 262 − 1 (230 − 1 on a 32-bit system) is immediate, and a larger value encodes a pointer to a heap-allocated GMP bignum. This differs from most other ﬂoating-point implementations, including MPFR, where an exponent is conﬁned to the numerical range of one word.

Since exponents almost always will be small in practice, the only overhead of allowing bignum exponents with this representation comes from an extra integer comparison (followed by a predictable branch) every time an exponent is accessed. In fact, we encode inﬁnities and NaNs using special exponent values in a way that allows us to combine testing for large exponents with testing for inﬁnities or NaNs, which often must be done anyway. In performance-critical functions where an input is used several times, such as in a ball multiplication [a±r][b±s] = [ab±(|as|+|br|+rs)], we only inspect each exponent once, and use optimized code for the entire calculation when all inputs are small. The fallback code does not need to be optimized and can deal with all remaining cases in a straightforward way by using FLINT fmpz_t functions to manipulate the exponent values.

Using arbitrary-size exponents has two advantages. First, since underﬂow or overﬂow cannot occur, it becomes easier to reason about ﬂoating-point operations. For example, no rewriting is needed to evaluate x2 + y2 correctly. It is arguably easier for the user to check the exponent range a posteriori if the applications demands that it be bounded (e.g. if the goal is to emulate a hardware type) than to work around underﬂow or overﬂow when it is unwanted. Anecdotally, edge cases related to the exponent range have been a frequent source of (usually minor) bugs in MPFR.

![image 56](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile56.png>)

Second, arbitrary-size exponents become very useful when dealing with asymptotic cases of special functions and combinatorial numbers, as became clear while developing [27]. Typical quotients of large exponentials or gamma functions can be evaluated directly without the need to make case distinctions or rewrite formulas in logarithmic form (which can introduce extra branch cut complications). Such rewriting may still be required for reasons of speed or numerical stability (i.e. giving tight intervals), but in some cases simply becomes an optional optimization.

Exponents can potentially grow so large that they slow down computations or use more memory than is available. We avoid this problem by introducing precision-dependent exponent limits in relevant interval (arb_t and acb_t) functions, where the information loss on underﬂow or overﬂow gets absorbed by the error bound, as we discuss later.

3.1.3 Feature simpliﬁcations The arf_t type deviates from the IEEE 754 standard and MPFR in a few important respects.

There is no global or thread-local state for exception ﬂags, rounding modes, default precision, exponent bounds, or other settings. Methods that might round the output return a ﬂag indicating whether the result is exact. Domain errors such as division by zero or taking the square root of a negative number result in NaNs which propagate through a computation to allow detection at any later point. Since underﬂow and overﬂow cannot occur at the level of ﬂoating-point arithmetic, they do not need to be handled. Memory allocation failure is considered fatal, and presumably raises the process abort signal (provided that

the system’s malloc allows catching failed allocations). We claim that statelessness is a feature of good library design. This allows referential transparency, and it is arguably easier for the user to implement their own state than to be sure that a library’s state is in the wanted conﬁguration at all times (particularly since the library’s state could be mutated by calls to external code that uses the same library).

The set of methods for the arf_t type is deliberately kept small. The most complicated methods are arf_sum, which adds a vector of ﬂoating-point numbers without intermediate rounding or overﬂow (this is necessary for correct implementation of interval predicates), and arf_complex_mul which computes (e + fi) = (a + bi)(c + di) with correct rounding. Mathematical operations beyond addition, multiplication, division and square roots of real numbers are only implemented for the arb_t type, where correct rounding becomes unnecessary and interval operations can be used internally to simplify the algorithms.

The arf_t type does not distinguish between positive and negative zero. Signed zero is probably less useful in ball arithmetic than in raw ﬂoating-point arithmetic. Signed zero allows distinguishing between directional limits when evaluating functions at discontinuities or branch cuts, but such distinctions can be made at a higher level without complicating the semantics of the underlying number type.

With these things said, support for omitted IEEE 754 or MPFR features could easily be accommodated by the arf_t data structure together with wrapper methods.

### 4 ARITHMETIC BENCHMARKS

Table 2 compares the performance of Arb intervals (arb_t), MPFR 3.1.5 ﬂoating-point numbers (mpfr_t) and MPFI 1.5.1 intervals (mpfi_t) for basic operations on real numbers. Table 3 further compares Arb complex intervals (acb_t) and MPC 1.0.3 complex ﬂoating-point numbers (mpc_t). An Intel i5-4300U CPU was used.

TABLE 2 Time to perform a basic operation on intervals with MPFI and Arb, normalized by the time to perform the same operation on ﬂoating-point numbers (i.e. just the midpoints) with MPFR. As operands, we take intervals for x = √3, y = √5 computed to full precision.

![image 57](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile57.png>)

![image 58](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile58.png>)

![image 59](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile59.png>)

![image 60](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile60.png>)

![image 61](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile61.png>)

prec MPFI Arb MPFI Arb MPFI Arb add mul fma

![image 62](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile62.png>)

![image 63](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile63.png>)

![image 64](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile64.png>)

![image 65](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile65.png>)

![image 66](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile66.png>)

![image 67](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile67.png>)

![image 68](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile68.png>)

![image 69](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile69.png>)

64 2.58 1.08 2.06 1.03 1.42 0.56 128 2.15 1.03 2.16 1.09 1.62 0.68 256 2.20 1.48 2.14 1.23 1.65 0.70

![image 70](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile70.png>)

![image 71](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile71.png>)

![image 72](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile72.png>)

![image 73](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile73.png>)

![image 74](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile74.png>)

![image 75](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile75.png>)

- 1024 2.22 1.39 2.05 0.99 1.49 0.76 4096 2.10 1.70 2.02 1.05 1.63 0.95

![image 76](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile76.png>)

![image 77](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile77.png>)

![image 78](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile78.png>)

![image 79](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile79.png>)

![image 80](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile80.png>)

![image 81](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile81.png>)

32768 2.11 1.65 2.02 1.02 1.78 1.00 div sqrt pow

![image 82](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile82.png>)

![image 83](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile83.png>)

![image 84](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile84.png>)

![image 85](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile85.png>)

![image 86](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile86.png>)

![image 87](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile87.png>)

![image 88](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile88.png>)

![image 89](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile89.png>)

64 2.96 1.72 2.02 1.78 0.97 0.09 128 2.81 1.79 2.01 1.50 1.21 0.11 256 2.56 1.38 2.15 1.31 1.40 0.13

![image 90](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile90.png>)

![image 91](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile91.png>)

![image 92](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile92.png>)

![image 93](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile93.png>)

![image 94](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile94.png>)

![image 95](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile95.png>)

![image 96](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile96.png>)

![image 97](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile97.png>)

![image 98](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile98.png>)

- 1024 2.23 0.92 2.03 1.09 1.68 0.29 4096 2.09 0.82 2.03 1.04 1.94 0.67


![image 99](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile99.png>)

![image 100](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile100.png>)

![image 101](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile101.png>)

![image 102](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile102.png>)

![image 103](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile103.png>)

![image 104](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile104.png>)

![image 105](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile105.png>)

![image 106](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile106.png>)

![image 107](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile107.png>)

32768 1.98 1.01 2.02 1.04 1.95 0.79

#### 3.2 Radii and magnitude bounds

The mag_t type represents an unsigned ﬂoating-point number a · 2b, 12 ≤ a < 1, or one of the special values {0,+∞}. The mantissa a has a ﬁxed precision of 30 bits in order to allow fast fused multiply-add operations on either 32-bit or 64-bit CPUs. The arbitrary-size exponent b is represented the same way as in the arf_t type. Methods for the mag_t type are optimized for speed, and may compute bounds that are a few ulps larger than optimally rounded upper bounds. Besides being faster than an arf_t, the mag_t type allows cleaner code by by making upward rounding automatic and removing the need for many sign checks.

![image 108](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile108.png>)

A double could have been used instead of an integer mantissa. This might be faster if coded carefully, though the need to normalize exponents probably takes away some of the advantage. We do some longer error bound calculations by temporarily converting to double values, scaled so that overﬂow or underﬂow cannot occur. When using double arithmetic, we always add or multiply the ﬁnal result by a small perturbation which can be proved to give a correct upper bound in IEEE 754 ﬂoating-point arithmetic regardless of the CPU rounding mode or doublerounding on systems that use extended precision, such at x86 processors with the historical x87 ﬂoating-point unit. For correctness, we assume that unsafe rewriting of ﬂoatingpoint expressions (e.g. assuming associativity) is disabled in the compiler, and and we assume that certain double operations such as ldexp and sqrt are correctly rounded. As a side note, Arb sometimes uses the libm transcendental functions in heuristics (typically, for tuning parameters), but never directly for error bounds.

MPFI lacks fused multiply-add (fma) and pow operations, so we timed fma using a mul followed by an add, and pow via log, mul and exp. Unlike MPFI’s built-in functions, these naive versions do not give optimal enclosures.

Multiplication in Arb is about as fast as in MPFR, and twice as fast as in MPFI. Ball multiplication [a ± r][b ± s] = [ab±(|as|+|br|+rs)] requires four multiplications and two additions (plus one more addition bounding the rounding error in the midpoint multiplication ab), but all steps except ab are done with cheap mag_t operations.

Addition alone in Arb is slower than MPFR at high precision since arf_add is not as well optimized. However, addition is not usually a bottleneck at high precision. The fused multiply-add operation in Arb is optimized to be about as fast as a multiplication alone at low to medium precision. This is important for matrix multiplication and basecase polynomial multiplication. In the tested version of MPFR, a fused multiply-add is somewhat slower than two separate operations, which appears to be an oversight and low-hanging fruit for improvement.

Division and square root in Arb have high overhead at low precision compared to MPFR, due to the relatively complicated steps to bound the propagated error. However, since the precision in these steps can be relaxed, computing the bounds using mag_t is still cheaper than the doubled work to evaluate at the endpoints which MPFI performs.

The large speedup for the transcendental pow operation up to about 4600 bits is due to the fast algorithm for elementary functions described in [12]. At higher precision, Arb remains around 20% faster than MPFR and MPC due to a more optimized implementation of the binary splitting

TABLE 3 Time to perform a basic operation on complex intervals with Arb, normalized by the time to perform the same operation on complex ﬂoating-point numbers with MPC. As operands, we take x = √3 + √5i, y = √7 + √11i.

![image 109](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile109.png>)

![image 110](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile110.png>)

![image 111](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile111.png>)

![image 112](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile112.png>)

![image 113](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile113.png>)

![image 114](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile114.png>)

![image 115](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile115.png>)

![image 116](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile116.png>)

![image 117](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile117.png>)

![image 118](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile118.png>)

prec add mul fma div sqrt pow

![image 119](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile119.png>)

![image 120](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile120.png>)

![image 121](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile121.png>)

![image 122](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile122.png>)

![image 123](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile123.png>)

![image 124](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile124.png>)

![image 125](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile125.png>)

64 1.13 0.24 0.41 0.35 0.66 0.11 128 1.50 0.29 0.41 0.34 0.77 0.11 256 1.71 0.32 0.47 0.63 0.81 0.13

![image 126](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile126.png>)

![image 127](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile127.png>)

![image 128](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile128.png>)

![image 129](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile129.png>)

![image 130](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile130.png>)

![image 131](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile131.png>)

![image 132](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile132.png>)

![image 133](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile133.png>)

![image 134](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile134.png>)

![image 135](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile135.png>)

![image 136](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile136.png>)

![image 137](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile137.png>)

![image 138](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile138.png>)

![image 139](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile139.png>)

![image 140](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile140.png>)

![image 141](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile141.png>)

![image 142](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile142.png>)

![image 143](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile143.png>)

1024 1.67 0.48 0.58 0.70 0.84 0.21 4096 1.51 0.93 0.98 0.89 0.91 0.44

![image 144](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile144.png>)

![image 145](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile145.png>)

![image 146](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile146.png>)

![image 147](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile147.png>)

![image 148](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile148.png>)

![image 149](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile149.png>)

![image 150](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile150.png>)

![image 151](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile151.png>)

![image 152](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile152.png>)

![image 153](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile153.png>)

![image 154](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile154.png>)

![image 155](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile155.png>)

32768 1.18 0.99 1.00 1.02 0.99 0.82

algorithm to compute exp and atan. Arb currently depends on MPFR for computing log, sin and cos above 4600 bits, reimplementation of these functions being a future possibility.

As one more test of basic arithmetic, we consider the following function that computes N! given a = 0,b = N.

void fac(arb_t res, int a, int b, int prec) {

if (b - a == 1) arb_set_si(res, b);

else { arb_t tmp1, tmp2; arb_init(tmp1); arb_init(tmp2);

- fac(tmp1, a, a + (b - a) / 2, prec);
- fac(tmp2, a + (b - a) / 2, b, prec); arb_mul(res, tmp1, tmp2); arb_clear(tmp2); arb_clear(tmp2);


} }

Table 4 compares absolute timings for this code and the equivalent code using MPFR and MPFI.

TABLE 4 Time in seconds to compute recursive factorial product with N = 105.

![image 156](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile156.png>)

![image 157](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile157.png>)

![image 158](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile158.png>)

prec MPFR MPFI Arb

![image 159](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile159.png>)

![image 160](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile160.png>)

![image 161](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile161.png>)

![image 162](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile162.png>)

64 0.0129 0.0271 0.00315 128 0.0137 0.0285 0.00303 256 0.0165 0.0345 0.00396

![image 163](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile163.png>)

![image 164](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile164.png>)

![image 165](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile165.png>)

![image 166](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile166.png>)

![image 167](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile167.png>)

![image 168](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile168.png>)

![image 169](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile169.png>)

![image 170](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile170.png>)

![image 171](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile171.png>)

1024 0.0417 0.0852 0.00441 4096 0.0309 0.0617 0.00543

![image 172](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile172.png>)

![image 173](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile173.png>)

![image 174](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile174.png>)

![image 175](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile175.png>)

![image 176](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile176.png>)

![image 177](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile177.png>)

32768 0.109 0.234 0.00883

In this benchmark, we deliberately allocate two temporary variables at each recursion step. The temporary variables could be avoided with a minor rewrite of the algorithm, but they are typical of real-world code. Since most intermediate results are small integers, we also see the beneﬁt of allocating mantissas dynamically to optimize for short partial results. Computing N! recursively is a model problem for various divide-and-conquer tasks such as binary splitting evaluation of linearly recurrent sequences. The MPFR and MPFI versions could be optimized by manually varying the precision or switching to integers at a certain recursion depth (in fact, Arb does this in the computation of exp and atan mentioned earlier), but this

becomes inconvenient in more complicated problems, such as the evaluation of the generalized hypergeometric series pFq(a1,...,ap;b1,...,bq;z) where the parameters (which may be complex numbers and even truncated power series) can have mixed lengths and sizes.

### 5 PRECISION AND BOUNDS

By deﬁnition, interval arithmetic must preserve set inclusions. That is, if f is a point-valued function, F is a valid interval extension of f if for any set X and any point x ∈ X, the inclusion f(x) ∈ F(X) holds. This leaves considerable freedom in choosing what set F(X) to compute.

For basic arb_t arithmetic operations, we generally evaluate the ﬂoating-point operation on the midpoint at pbit precision, bound the propagated error, and add a tight bound for the result of rounding the midpoint. For example, addition becomes [m1±r1]+[m2±r2] = [roundp(m1+m2)± (r1 + r2 + εround)] where the radius operations are done with upward rounding. In this case, the error bounds are essentially the best possible, up to order 2−30 perturbations in the mag_t radius operations.

For more complicated operations, the smallest possible enclosure can be very difﬁcult to determine. The design of interval functions F in Arb has largely been dictated by evaluation speed and convenience, following the philosophy that “good enough” error bounds can serve until a concrete application is found that mandates optimization.

#### 5.1 Generic error bounds

Since the user inputs the precision p as a parameter, we can think of Fp as a sequence of functions, and formulate some useful properties that should hold. Clearly, if x is a single point, then Fp(x) should converge to f(x) when p → ∞, preferably with error 2O(1)−p. It is also nice to ensure Fp({x}) = {f(x)} for all sufﬁciently large p if f(x) is exactly representable. If f is continuous near the point x and the sequence of input sets Xp converge to x sufﬁciently rapidly, then Fp(Xp) should converge to f(x) when p → ∞. In particular, if f is Lipschitz continuous and Xp has radius 2O(1)−p, then Fp(X) should preferably have radius 2O(1)−p.

Let X = [m ± r] and assume that f is differentiable. A reasonable compromise between speed and accuracy is to evaluate f(m) to p-bit accuracy and use a ﬁrst-order error propagation bound:

sup

|f(m + t) − f(m)| ≤ C1|r|, C1 = sup

|t|≤r

|t|≤|r|

|f′(m + t)|.

Of course, this presumes that a good bound for |f′| is available. A bound on |f| can be included if r is large. For example, for m,r ∈ R, sup|t|≤|r| |sin(m+t)−sin(t)| ≤ min(2,|r|).

In practice, we implement most operations by composing simpler interval operations; either because derivative bounds would be difﬁcult to compute accurately and quickly, or because the function composition is numerically stable and avoids inﬂating the error bounds too much. Ideally, asymptotic ill-conditioning is captured by an elementary prefactor such as ez or sin(z), whose accurate evaluation is delegated to the corresponding arb_t or acb_t method. Some case distinctions may be required for

different parts of the domain. For instance, Arb computes the complex tangent as



sin(z) cos(z)

if |mid(im(z))| < 1

![image 178](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile178.png>)

2i exp(2iz) 1 + exp(2iz)



tan(z) =

i −

if mid(im(z)) ≥ 1

![image 179](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile179.png>)

2i exp(−2iz) 1 + exp(−2iz)

if mid(im(z)) ≤ 1

−i +

![image 180](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile180.png>)



When |im(z)| is large, the ﬁrst formula is a quotient of two large exponentials. This causes error bounds to blow up in interval arithmetic, and for sufﬁciently large |im(z)|, overﬂow occurs. The alternative formulas only compute small exponentials and add them to numbers of unit magnitude, which is numerically stable and avoids overﬂow problems.

In general, transcendental functions are computed from some combination of functional equations and ﬁnite approximations (e.g. truncated Taylor and asymptotic series), using most of the “tricks from the book”. There are usually three distinct steps. Evaluation parameters (e.g. the series truncation order; working precision to compensate for cancellation) are ﬁrst chosen using fast heuristics. The ﬁnite approximation formula is then evaluated using interval arithmetic. Finally, a rigorous bound for the truncation error is computed using interval or mag_t operations.

#### 5.2 Large values and evaluation cutoffs

If x is a ﬂoating-point number of size |x| ≈ 2n, then computing sin(x) or exp(x) to p-bit accuracy requires n + p bits of internal precision for argument reduction, i.e. subtracting a multiple of π or log(2) from x (the ﬂoating-point approximation of exp(x) will also have an n-bit exponent). This is clearly futile if x = 22

35, but in practice computing billions of digits of π is likely to be a waste of time. For example, when evaluating the formula

100. It is feasible if x = 22

log(x) + sin(x)exp(−x) (2)

we only need a crude bound for the sine and exponential to get an accurate result if x ≫ 0. To handle different ranges of x and p, the user could make case distinctions, but automatic cutoffs are useful when calculations become more complex.

As a general rule, Arb restricts internal evaluation parameters so that a method does at most O(poly(p)) work, independent of the input value. This prevents too much time from being spent on branches in an evaluation tree that may turn out not to be needed for the end result. It allows a simple precision-increasing loop to be used for “black box” numerical evaluation that can be terminated at any convenient point if it fails to converge rapidly enough. In other words, the goal is not to try to solve the problem at any cost, but to fail gracefully and allow the user to try an alternative approach.

The cutoffs should increase in proportion to the precision so that not too much time is wasted at low precision on subexpressions that may turn out not to be needed, but so that the precise values still can be computed by setting the precision high enough.

For real trigonometric functions and exponentials, Arb effectively computes

sin(x) =

[sin(x) ± ε] if n ≤ max(65536,4p) [±1] if n > max(65536,4p),

 

[ex ± ε] if n ≤ max(128,2p) [0,2−2

max(128,2p)

ex =

] if n > max(128,2p) and x < 0 [±∞] if n > max(128,2p) and x > 0.



The automatic overﬂow and underﬂow for exp(x) is certainly necessary with arbitrary-size exponents, but arbitrarily bad slowdown for a function such as sin(x) is a concern even with single-word exponents, e.g. with MPFR and MPFI. Evaluation cutoffs are useful even if the user only intends to work with modest numbers, one reason being that extremely large values can result when some initial rounding noise gets ampliﬁed by a sequence of ﬂoating-point operations. It is better to pass such input through quickly than to stall the computation. Exponential or trigonometric terms that become irrelevant asymptotically also appear in connection with special functions. For example, the righthand side in the digamma function reﬂection formula

ψ(1 − z) = ψ(z) + π cot(πz)

with z ∈ C has the same nature as (2). In Pari/GP 2.5.5 and Mathematica 9.0, numerically evaluating ψ(−10+2100i) results in an overﬂow (Maple 18 succeeds, however). Version 0.19 of mpmath manages by using arbitrary-precision exponents, but is unable to evaluate ψ(−10 + 22

100

i). With Arb, computing at 53-bit precision gives

ψ(−10 + 2100i) = [69.3147180559945± 3.12 · 10−14]

+ [1.57079632679490± 3.40 · 10−15]i

and

100

ψ(−10 + 22

i) = [8.78668439483320· 1029 ± 4.35 · 1014]

+ [1.57079632679490± 3.40 · 10−15]i.

This works automatically since a numerically stable formula is used to compute cot(πz) (like the formula for tan(z)), and in that formula, the tiny exponential automatically evaluates to a power-of-two bound with a clamped exponent.

#### 5.3 Branch cuts

Arb works with principal branches, following conventions most common in computer algebra systems. In particular, the complex logarithm satisﬁes −π < im(log(z)) ≤ π, and the phase of a negative real number is +π. A convenience of using rectangular complex intervals instead of disks is that it allows representing line segments along branch cuts without crossing the cuts. When intervals do cross branch cuts, the image of the principal branch includes the jump discontinuity. For example,

log(−100 + [±1]i) = [4.6052 ± 7.99 · 10−5] + [±3.15]i.

It would be tempting to pick an arbitrary branch, e.g. that of the midpoint, to avoid the discontinuity. However, this would break formulas where the same branch choice is

assumed in two subexpressions and rounding perturbations could place the midpoints on different sides of the cut.

It is up to the user to rewrite formulas to avoid branch cuts when preserving continuity is necessary. For example, to compute both square roots of a complex number (in undeﬁned order), one can use (√z,−

√z) if re(mid(z)) ≥ 0 and (i√

![image 181](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile181.png>)

![image 182](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile182.png>)

−z,−i√

![image 183](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile183.png>)

![image 184](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile184.png>)

−z) if re(mid(z)) < 0. Arb has limited support for working with non-principal branches of higher special functions: the Gauss hypergeometric function 2F1 has a branch cut on (1,∞), which is used by default, but a method is available for continuous analytic continuation of 2F1 along an arbitrary path, which may cross the normal placement of the branch cut.

#### 5.4 Decimal conversion

While computations are done in binary and binary is recommended for serialization, human-readable decimal output is important for user interaction. The method arb_printn(x, d, flags), given an arb_t x = [m±r], a decimal precision d ≥ 1, and default ﬂags 0, prints a decimal interval of the form [m′ ± r′] where:

- • m′ and r′ are exact decimal ﬂoating-point numbers,
- • m′ has at most d-digit mantissa; r′ has three digits,
- • m′ is nearly a correctly rounded representation of x: it is allowed to differ from x by at most one unit in the last place (if x is accurate to fewer than d digits, m′ is truncated accordingly),
- • x ⊆ [m′ ±r′] (the output radius r′ takes into account both the original error r and any error resulting from the binary-to-decimal conversion).


For example, x = [884279719003555·2−48±536870913· 2−80] (a 53-bit accurate enclosure of π) is printed as [3.141592653589793 ± 5.61 · 10−16] with d = 30 and as [3.14 ± 1.60 · 10−3] with d = 3. The brackets and ±r′ are omitted if m′ = x. If less than one digit of x can be determined, m′ is omitted, resulting in a magnitudebound output such as [±1.23 · 10−8]. (The typesetting in conventional mathematical notation is a liberty taken in this paper; the verbatim output is an ASCII string with C-style ﬂoating-point literals such as [3.14 +/- 1.60e-3].)

A method is also provided for parsing back from a string. In general, a binary-decimal-binary or decimalbinary-decimal roundtrip enlarges the interval. However, conversions in either direction preserve exact midpoints (such as x = 0.125 with d ≥ 3) whenever possible.

The implementations are simple: interval arithmetic is used to multiply or divide out exponents, and the actual radix conversions are performed on big integers, with linear passes over the decimal strings for rounding and formatting.

### 6 POLYNOMIALS, POWER SERIES AND MATRICES

Arb provides matrices and univariate polynomials with an eye toward computer algebra applications. Polynomials are also used extensively within the library for algorithms related to special functions.

Matrices come with rudimentary support for linear algebra, including multiplication, powering, LU factorization, nonsingular solving, inverse, determinant, characteristic

polynomial, and matrix exponential. Most matrix operations currently use the obvious, naive algorithms (with the exception of matrix exponentials, details about which are beyond the scope of this paper). Support for ﬁnding eigenvalues is notably absent, though computing roots of the characteristic polynomial is feasible if the matrix is not too large.

Polynomials support all the usual operations including arithmetic, differentiation, integration, evaluation, composition, Taylor shift, multipoint evaluation and interpolation, complex root isolation, and reconstruction from given roots. The polynomial types are also used to represent truncated power series, and methods are provided for truncated arithmetic, composition, reversion, and standard algebraic and transcendental functions of power series.

Arb automatically switches between basecase algorithms for low degree and asymptotically fast algorithms based on polynomial multiplication for high degree. For example, division, square roots and elementary transcendental functions of power series use O(n2) coefﬁcient recurrences for short input and methods based on Newton iteration that cost O(1) multiplications for long input. Polynomial composition uses the divide-and-conquer algorithm [28], and power series composition and reversion use baby-step giant-step algorithms [29], [30]. Monomials and binomials are also handled specially in certain cases.

#### 6.1 Polynomial multiplication

Since polynomial multiplication is the kernel of many operations, it needs to be optimized for both speed and accuracy, for input of all sizes and shapes.

When multiplying polynomials with interval coefﬁcients, the O(n2) schoolbook algorithm essentially gives the best possible error bound for each coefﬁcient in the output (up to rounding errors in the multiplication itself and under generic assumptions about the coefﬁcients).

The O(n1.6) Karatsuba and O(n log n) FFT multiplication algorithms work well when all input coefﬁcients and errors have the same absolute magnitude, but they can give poor results when this is not the case. The effect is pronounced when manipulating power series with decaying coefﬁcients such as exp(x) = k xk/k!. Since the FFT gives error bounds of roughly the same magnitude for all output coefﬁcients, high precision is necessary to produce accurate high-order coefﬁcients. Karatsuba multiplication also effectively adds a term and then subtracts it again, doubling the initial error, which leads to exponentially-growing bounds for instance when computing the powers A,A2,A3,... of a polynomial via the recurrence Ak+1 = Ak · A.

We have implemented a version of the algorithm proposed by van der Hoeven [31] to combine numerical stability with FFT performance where possible. This rests on several techniques:

- 1) Rather than directly multiplying polynomials with interval coefﬁcients, say A ± a and B ± b where A,a,B,b ∈ Z[21][x], we compute AB ± (|A|b + a(|B|+b)) using three multiplications of polynomials with ﬂoating-point coefﬁcients, where |·| denotes the per-coefﬁcient absolute value.

![image 185](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile185.png>)

- 2) (Trimming: bits in the input coefﬁcients that do not contribute signiﬁcantly can be discarded.)




6000

0

5000

−20000

4000

−40000

log()ck2

log()ck2

3000

−60000

2000

−80000

1000

−100000

0

−120000

−1000

0 2000 4000 6000 8000 10000 k

0 2000 4000 6000 8000 10000 k

10

Fig. 1. Transformation used to square exp(x) = k xk/k! ∈ R[x]/ xn with n = 104 at p = 333 bits of precision. The original polynomial, shown on the left, has an effective height of log2(n!) + p ≈ 119 000 bits. Scaling x → 212x gives the polynomial on the right which is split into 8 blocks of height at most 1511 bits, where the largest block has a width of 5122 coefﬁcients.

- 3) Scaling: a substitution x → 2cx is made to give polynomials with more slowly changing coefﬁcients.
- 4) Splitting: if the coefﬁcients still vary too much, we write the polynomials as block polynomials,

say A = A0 + xr

1

A1 + ...xr

K−1

AK−1 and B = B0 + xs

1

B1 + ...xs

L−1

BL−1, where the coefﬁcients in each block have similar magnitude. The block polynomials are multiplied using KL polynomial multiplications. Ideally, we will have K = L = 1.

- 5) Exact multiplication: we ﬁnally use a fast algo-


rithm to multiply each pair of blocks AiBj. Instead of using ﬂoating-point arithmetic, we compute 2eAiBj ∈ Z[x] exactly using integer arithmetic. The product of the blocks is added to the output interval polynomial using a single addition rounded to the target precision.

For degrees n < 16, we use the O(n2) schoolbook algorithm. At higher degree, we combine techniques 1 and 3-5 (technique 2 has not yet been implemented). We perform a single scaling x → 2cx, where c is chosen heuristically by looking at the exponents of the ﬁrst and last nonzero coefﬁcient in both input polynomials and picking the weighted average of the slopes (the scaling trick is particularly effective when both A and B are power series with the same ﬁnite radius of convergence). We then split the inputs into blocks of height (the difference between the highest and lowest exponent) at most 3p+512 bits, where p is the target precision. The scaling and splitting is illustrated in Figure 1.

The exact multiplications in Z[x] are done via FLINT. Depending on the input size, FLINT in turn uses the schoolbook algorithm, Karatsuba, Kronecker segmentation, or a Sch¨onhage-Strassen FFT. The latter two algorithms have quasi-optimal bit complexity O˜(np).

For the multiplications |A|b and a(|B| + b) involving radii, blocks of width n < 1000 are processed using schoolbook multiplication with hardware double arithmetic. This has less overhead than working with big integers, and guaranteeing correct and accurate error bounds is easy since all coefﬁcients are nonnegative.

Our implementation follows the principle that polynomial multiplication always should give error bounds of the same quality as the schoolbook algorithm, sacriﬁcing speed if necessary. As a bonus, it preserves sparsity (e.g. even or

odd polynomials) and exactness of individual coefﬁcients.

In practice, it is often the case that one needs O(n) bits of precision to compute with degree-n polynomials and power series regardless of the multiplication algorithm, because the problems that lead to such polynomials are inherently ill-conditioned. In such cases, a single block will typically be used, so the block algorithm is almost as fast as a “lossy” FFT algorithm that discards information about the smallest coefﬁcients. On the other hand, whenever low precision is sufﬁcient with the block algorithm and a “lossy” FFT requires much higher precision for equivalent output accuracy, the “lossy” FFT is often even slower than the schoolbook algorithm.

Complex multiplication is reduced to four real multiplication in the obvious way. Three multiplications would be sufﬁcient using the Karatsuba trick, but this suffers from the instability problem mentioned earlier. Karatsuba multiplication could, however, be used for the exact stage.

#### 6.2 Polynomial multiplication benchmark

Enge’s MPFRCX library [32] implements univariate polynomials over MPFR and MPC coefﬁcients without control over the error. Depending on size, MPFRCX performs polynomial multiplication using the schoolbook algorithm, Karatsuba, Toom-Cook, or a numerical FFT.

Table 5 compares MPFRCX and Arb for multiplying real and complex polynomials where all coefﬁcients have roughly the same magnitude (we use the real polynomials f = k n=0−1 xk/(k + 1), g = k n=0−1 xk/(k + 2) and complex polynomials with similar real and imaginary parts). This means that MPFRCX’s FFT multiplication computes all coefﬁcients accurately and that Arb can use a single block.

The results show that multiplying via FLINT generally performs signiﬁcantly better than a numerical FFT with high-precision coefﬁcients. MPFRCX is only faster for small n and very high precision, where it uses Toom-Cook while Arb uses the schoolbook algorithm.

Complex coefﬁcients are about four times slower than real coefﬁcients in Arb (since four real polynomial multiplications are used) but only two times slower in MPFRCX (since a real FFT takes half the work of a complex FFT). A factor two could theoretically be saved in Arb’s complex multiplication algorithm by recycling the integer transforms, but this would be signiﬁcantly harder to implement.

TABLE 5 Time in seconds to multiply polynomials of length n with p-bit coefﬁcients having roughly unit magnitude.

Real Complex n p MPFRCX Arb MPFRCX Arb

![image 187](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile187.png>)

![image 188](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile188.png>)

![image 189](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile189.png>)

![image 190](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile190.png>)

![image 191](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile191.png>)

10 100 1.3e-5 6.9e-6 6.4e-5 3.5e-5 10 1000 3.1e-5 2.1e-5 1.8e-4 9.4e-5

![image 192](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile192.png>)

![image 193](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile193.png>)

- 10 104 3.6e-4 4.4e-4 0.0015 0.0021

![image 194](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile194.png>)

![image 195](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile195.png>)

- 10 105 0.0095 0.012 0.034 0.055 100 100 6.0e-4 1.3e-4 0.0020 5.6e-4 100 1000 0.0012 4.5e-4 0.0042 0.0019


![image 196](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile196.png>)

![image 197](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile197.png>)

![image 198](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile198.png>)

![image 199](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile199.png>)

![image 200](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile200.png>)

![image 201](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile201.png>)

![image 202](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile202.png>)

- 100 104 0.012 0.0076 0.043 0.031

![image 203](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile203.png>)

![image 204](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile204.png>)

- 100 105 0.31 0.11 0.98 0.42


![image 205](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile205.png>)

![image 206](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile206.png>)

![image 207](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile207.png>)

- 103 100 0.015 0.0022 0.025 0.0091

![image 208](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile208.png>)

![image 209](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile209.png>)

- 103 1000 0.029 0.0061 0.049 0.026

![image 210](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile210.png>)

![image 211](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile211.png>)

- 103 104 0.36 0.084 0.59 0.34

![image 212](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile212.png>)

![image 213](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile213.png>)

- 103 105 9.3 1.2 16 4.4


![image 214](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile214.png>)

![image 215](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile215.png>)

![image 216](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile216.png>)

- 104 100 0.30 0.034 0.55 0.14

![image 217](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile217.png>)

![image 218](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile218.png>)

- 104 1000 0.63 0.19 1.1 0.82

![image 219](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile219.png>)

![image 220](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile220.png>)

- 104 104 8.0 1.2 14 4.6

![image 221](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile221.png>)

![image 222](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile222.png>)

- 104 105 204 13 349 50


![image 223](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile223.png>)

![image 224](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile224.png>)

![image 225](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile225.png>)

- 105 100 2.9 0.54 5.4 2.0


![image 226](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile226.png>)

![image 227](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile227.png>)

- 105 1000 6.3 2.5 11 10

![image 228](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile228.png>)

![image 229](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile229.png>)

- 105 104 77 23 142 96

![image 230](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile230.png>)

![image 231](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile231.png>)

![image 232](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile232.png>)

- 106 100 553 6.3 1621 23


![image 233](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile233.png>)

![image 234](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile234.png>)

- 106 1000 947 28 3311 103




TABLE 6 Time in seconds to expand falling factorial polynomial.

![image 235](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile235.png>)

![image 236](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile236.png>)

![image 237](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile237.png>)

![image 238](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile238.png>)

![image 239](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile239.png>)

![image 240](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile240.png>)

n FLINT MPFRCX MPFRCX Arb Arb Arb

![image 241](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile241.png>)

![image 242](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile242.png>)

![image 243](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile243.png>)

![image 244](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile244.png>)

![image 245](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile245.png>)

![image 246](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile246.png>)

exact, 64-bit, P-bit, 64-bit 64-bit, exact, tree iter. tree iter. tree tree

![image 247](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile247.png>)

![image 248](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile248.png>)

![image 249](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile249.png>)

![image 250](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile250.png>)

![image 251](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile251.png>)

![image 252](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile252.png>)

![image 253](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile253.png>)

![image 254](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile254.png>)

![image 255](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile255.png>)

![image 256](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile256.png>)

![image 257](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile257.png>)

![image 258](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile258.png>)

![image 259](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile259.png>)

10 4.8e-7 1.8e-5 1.8e-5 4.6e-6 2.7e-6 2.7e-6

- 102 1.2e-4 1.1e-3 9.0e-4 4.8e-4 2.0e-4 2.4e-4

![image 260](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile260.png>)

![image 261](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile261.png>)

![image 262](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile262.png>)

![image 263](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile263.png>)

![image 264](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile264.png>)

![image 265](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile265.png>)

- 103 0.030 0.10 0.35 0.049 0.0099 0.032

![image 266](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile266.png>)

![image 267](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile267.png>)

![image 268](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile268.png>)

![image 269](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile269.png>)

![image 270](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile270.png>)

![image 271](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile271.png>)

- 104 5.9 10 386 4.8 0.85 5.9

![image 272](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile272.png>)

![image 273](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile273.png>)

![image 274](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile274.png>)

![image 275](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile275.png>)

![image 276](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile276.png>)

![image 277](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile277.png>)

- 105 1540 515 85

![image 278](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile278.png>)

![image 279](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile279.png>)

![image 280](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile280.png>)

![image 281](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile281.png>)

![image 282](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile282.png>)

![image 283](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile283.png>)

- 106 8823


![image 284](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile284.png>)

![image 285](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile285.png>)

![image 286](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile286.png>)

![image 287](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile287.png>)

![image 288](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile288.png>)

![image 289](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile289.png>)

is about as fast as FLINT for exact computation when n is large, and can transition seamlessly between the extremes. For example, 4096-bit precision takes 1.8 s at n = 104 and 174 s at n = 105, twice that of 64-bit precision.

![image 290](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile290.png>)

![image 291](<2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra_images/imageFile291.png>)

We show one more benchmark in Table 6. Deﬁne

n

s(n,k)xk.

fn = x(x − 1)(x − 2)···(x − n + 1) =

k=0

Similar polynomials appear in series expansions and in manipulation of differential and difference operators. The coefﬁcients s(n,k) are the Stirling numbers of the ﬁrst kind, which fall of from size about |s(n,1)| = (n − 1)! to s(n,n) = 1. Let P = maxk log2 |s(n,k)| + 64. Using a tree (binary splitting) to expand the product provides an asymptotically fast way to generate s(n,0),...,s(n,n). We compare expanding fn from the linear factors using:

- • FLINT integer polynomials, with a tree.
- • MPFRCX, at 64-bit precision multiplying out one factor at a time, and at P-bit precision with a tree.
- • Arb, one factor at a time at 64-bit precision, and then at 64-bit precision and exactly (using ≥ P-bit precision) with a tree.


Multiplying out iteratively one factor at a time is numerically stable, i.e. we get nearly 64-bit accuracy for all coefﬁcients with both MPFRCX and Arb at 64-bit precision. Using a tree, we need P-bit precision to get 64-bit accuracy for the smallest coefﬁcients with MPFRCX, since the error in the FFT multiplication depends on the largest term. This turns out to be slower than exact computation with FLINT, in part since the precision in MPFRCX does not automatically track the size of the intermediate coefﬁcients.

With Arb, using a tree gives nearly 64-bit accuracy for all coefﬁcients at 64-bit precision, thanks to the block multiplication algorithm. The multiplication trades speed for accuracy, but when n ≫ 102, the tree is still much faster than expanding one factor at a time. At the same time, Arb

#### 6.3 Power series and calculus

Automatic differentiation together with fast polynomial arithmetic allows computing derivatives that would be hard to reach with numerical differentiation methods. For example, if f1 = exp(x), f2 = exp(exp(x)), f3 = Γ(x), f4 = ζ(x), Arb computes {fk(i)(0.5)}1000i=0 to 1000 digits in 0.0006, 0.2, 0.6 and 1.9 seconds respectively.

Series expansions of functions can be used to carry out analytic operations such as root-ﬁnding, optimization and integration with rigorous error bounds. Arb includes code for isolating roots of real analytic functions using bisection and Newton iteration. To take an example from [14], Arb isolates the 6710 roots of the Airy function Ai(x) on [−1000,0] in 0.4 s and reﬁnes all roots to 1000 digits in 16 s.

Arb also includes code for integrating complex analytic functions using the Taylor method, which allows reaching 100 or 1000 digits with moderate effort. This code is intended more as an example than for serious use.

### 7 CONCLUSION

We have demonstrated that midpoint-radius interval arithmetic can be as performant as ﬂoating-point arithmetic in an arbitrary-precision setting, combining asymptotic efﬁciency with low overhead. It is also often easier to use. The efﬁciency compared to non-interval software is maintained or even improves when we move from basic arithmetic to some higher operations such as evaluation of special functions and polynomial manipulation, since the core arithmetic enables using advanced algorithms for such tasks.

There is currently no accepted standard for how midpoint-radius interval arithmetic should behave. In Arb, we have taken a pragmatic approach which seems to work very well in practice. Arguably, ﬁne-grained determinism (e.g. bitwise reproducible rounding for individual arithmetic operations) is much less important in interval arithmetic than in ﬂoating-point arithmetic since the quality of an interval result can be validated after it has been computed. This opens the door for many optimizations. Implementing algorithms that give better error bounds efﬁciently can itself be viewed as a performance optimization, and should be one of the points for further study.

### ACKNOWLEDGMENTS

The research was partially funded by ERC Starting Grant ANTICS 278537 and Austrian Science Fund (FWF) grant Y464-N18. Special thanks go to the people who have made contributions to Arb: Bill Hart, Alex Grifﬁng, Pascal Molin, and many others who are credited in the documentation.

### REFERENCES

- [1] W. Tucker, Validated numerics: a short introduction to rigorous computations. Princeton University Press, 2011.
- [2] T. C. Hales, J. Harrison, S. McLaughlin, T. Nipkow, S. Obua, and R. Zumkeller, “A revision of the proof of the Kepler conjecture,” in The Kepler Conjecture. Springer, 2011, pp. 341–376.
- [3] H. A. Helfgott, “The ternary Goldbach problem,” http://arxiv.org/abs/1501.05438, 2015.
- [4] W. Tucker, “A rigorous ODE solver and Smale’s 14th problem,” Foundations of Computational Mathematics, vol. 2, no. 1, pp. 53–117, 2002.
- [5] N. Revol and F. Rouillier, “Motivations for an arbitrary precision interval arithmetic library and the MPFI library,” Reliable Computing, vol. 11, no. 4, pp. 275–290, 2005, http://perso.ens-lyon.fr/nathalie.revol/software.html.
- [6] L. Fousse, G. Hanrot, V. Lefe`vre, P. Pe´lissier, and P. Zimmermann, “MPFR: A multiple-precision binary ﬂoating-point library with correct rounding,” ACM Transactions on Mathematical Software, vol. 33, no. 2, pp. 13:1–13:15, Jun. 2007, http://mpfr.org.
- [7] A. Enge, P. The´veny, and P. Zimmermann, “MPC: a library for multiprecision complex arithmetic with exact rounding,” http://multiprecision.org/, 2011.
- [8] J. van der Hoeven, “Ball arithmetic,” HAL, Tech. Rep., 2009, http://hal.archives-ouvertes.fr/hal-00432152/fr/.
- [9] J. van der Hoeven, G. Lecerf, B. Mourrain, P. Tre´buchet, J. Berthomieu, D. N. Diatta, and A. Mantzaﬂaris, “Mathemagix: the quest of modularity and efﬁciency for symbolic and certiﬁed numeric computation?” ACM Communications in Computer Algebra, vol. 45, no. 3/4, pp. 186–188, Jan. 2012, http://mathemagix.org. [Online]. Available: http://doi.acm.org/10.1145/2110170.2110180
- [10] N. Mu¨ller, “The iRRAM: Exact arithmetic in C++,” in Computability and Complexity in Analysis. Springer, 2001, pp. 222–252, http://irram.uni-trier.de.
- [11] D. H. Bailey and J. M. Borwein, “High-precision arithmetic in mathematical physics,” Mathematics, vol. 3, no. 2, pp. 337–367, 2015.
- [12] F. Johansson, “Efﬁcient implementation of elementary functions in the medium-precision range,” in 22nd IEEE Symposium on Computer Arithmetic, ser. ARITH22, 2015, pp. 83–89.
- [13] ——, “Rigorous high-precision computation of the Hurwitz zeta function and its derivatives,” Numerical Algorithms, vol. 69, no. 2, pp. 253–270, June 2015.
- [14] ——, “Computing hypergeometric functions rigorously,” https://arxiv.org/abs/1606.06977, 2016.
- [15] ——, “Arb: a C library for ball arithmetic,” ACM Communications in Computer Algebra, vol. 47, no. 4, pp. 166–169, 2013.
- [16] The GMP development team, “GMP: The GNU Multiple Precision Arithmetic Library,” http://gmplib.org.
- [17] The MPIR development team, “MPIR: Multiple Precision Integers and Rationals,” http://www.mpir.org.
- [18] W. B. Hart, “Fast Library for Number Theory: An Introduction,” in Proceedings of the Third international congress conference on Mathematical software, ser. ICMS’10. Berlin, Heidelberg: Springer-Verlag, 2010, pp. 88–91, http://ﬂintlib.org.
- [19] Sage developers, SageMath, the Sage Mathematics Software System (Version 7.2.0), 2016, http://www.sagemath.org.
- [20] N. Nethercote and J. Seward, “Valgrind: a framework for heavyweight dynamic binary instrumentation,” in ACM Sigplan notices, vol. 42, no. 6. ACM, 2007, pp. 89–100.
- [21] N. J. A. Sloane, “OEIS A110375,” http://oeis.org/A110375, 2008.
- [22] F. Johansson, “Efﬁcient implementation of the Hardy-RamanujanRademacher formula,” LMS Journal of Computation and Mathematics, vol. 15, pp. 341–359, 2012. [Online]. Available: http://dx.doi.org/10.1112/S1461157012001088
- [23] A. Enge, “The complexity of class polynomial computation via ﬂoating point approximations,” Mathematics of Computation, vol. 78, no. 266, pp. 1089–1107, 2009.


- [24] A. Bucur, A. M. Ernvall-Hyt¨onen, A. Odzak,ˇ and L. Smajlovic´, “On a Li-type criterion for zero-free regions of certain Dirichlet series with real coefﬁcients,” LMS Journal of Computation and Mathematics, vol. 19, no. 1, pp. 259–280, 2016.
- [25] G. Beliakov and Y. Matiyasevich, “Zeros of Dirichlet L-functions on the critical line with the accuracy of 40000 decimal places,” http://dx.doi.org/10.4225/16/5382D9A62073E, 2014.
- [26] ——, “Approximation of Riemann’s zeta function by ﬁnite Dirichlet series: A multiprecision numerical approach,” Experimental Mathematics, vol. 24, no. 2, pp. 150–161, 2015.
- [27] F. Johansson, “mpmath: a Python library for arbitrary-precision ﬂoating-point arithmetic,” http://mpmath.org, 2015.
- [28] W. B. Hart and A. Novocin, “Practical divide-and-conquer algorithms for polynomial arithmetic,” in Computer Algebra in Scientiﬁc Computing. Springer, 2011, pp. 200–214.
- [29] R. P. Brent and H. T. Kung, “Fast algorithms for manipulating formal power series,” Journal of the ACM, vol. 25, no. 4, pp. 581– 595, 1978.
- [30] F. Johansson, “A fast algorithm for reversion of power series,” Mathematics of Computation, vol. 84, pp. 475–484, 2015. [Online]. Available: http://dx.doi.org/10.1090/S0025-5718-2014-02857-3
- [31] J. van der Hoeven, “Making fast multiplication of polynomials numerically stable,” Universite´ Paris-Sud, Orsay, France, Tech. Rep. 2008-02, 2008.
- [32] A. Enge, “MPFRCX: a library for univariate polynomials over arbitrary precision real or complex numbers,” 2012, http://www.multiprecision.org/index.php?prog=mpfrcx.


