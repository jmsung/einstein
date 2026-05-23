## Lambert W Function for Applications in Physics

Darko Veberiˇc a,b

aLaboratory for Astroparticle Physics, University of Nova Gorica, Slovenia bDepartment of Theoretical Physics, J. Stefan Institute, Ljubljana, Slovenia

##### Abstract

The Lambert W(x) function and its possible applications in physics are presented. The actual numerical implementation in C++ consists of Halley’s and Fritsch’s iterations with initial approximations based on branch-point expansion, asymptotic series, rational ﬁts, and continued-logarithm recursion.

# arXiv:1209.0735v2[cs.MS]7Jan2018

Keywords: Lambert W function, computational physics, numerical methods and algorithms, C++

##### Program summary

Program title: LambertW Catalogue identiﬁer: AENC v1 0 Program summary URL: http://cpc.cs.qub.ac.uk/summaries/AENC v1 0.html Program obtainable from: CPC Program Library, Queen’s University, Belfast, N. Ireland Licensing provisions: GNU General Public License version 3 No. of lines in distributed program, including test data, etc.: 1335 No. of bytes in distributed program, including test data, etc.: 25283 Distribution format: tar.gz Programming language: C++ (with suitable wrappers it can be called from C, Fortran etc.), the supplied command-line

utility is suitable for other scripting languages like sh, csh, awk, perl etc. Computer: All systems with a C++ compiler. Operating system: All Unix ﬂavors, Windows. It might work with others. RAM: Small memory footprint, less than 1MB Classiﬁcation: 1.1, 4.7, 11.3, 11.9. Nature of problem: Find fast and accurate numerical implementation for the Lambert W function. Solution method: Halley’s and Fritsch’s iterations with initial approximations based on branch-point expansion,

asymptotic series, rational ﬁts, and continued logarithm recursion. Additional comments: Distribution ﬁle contains the command-line utility lambert-w. Doxygen comments, included in

the source ﬁles. Makeﬁle. Running time: The tests provided take only a few seconds to run. Source repository: https://github.com/DarkoVeberic/LambertW

Email address: darko.veberic@kit.edu (Darko Veberiˇc ) Preprint submitted to Computer Physics Communications September 5, 2012

##### 1. Introduction

The Lambert W function is deﬁned as the inverse function of the

- x  → x ex (1)

mapping and thus solves the

- y ey = x (2)


equation. This solution is given in the form of the Lambert W function,

y = W(x), (3) and according to Eq. (2) it satisﬁes the following relation,

W(x) eW(x) = x. (4)

Since the mapping in Eq. (1) is not injective, no unique inverse of the x ex function exists (except at the minimum). As can be seen in Fig. 1, the Lambert W function has two real branches with a branching point located at (−e−1, −1). The bottom branch, W−1(x), is deﬁned in the interval x ∈ [−e−1, 0] and has a negative singularity for x → 0−. The upper branch W0(x) is deﬁned for x ∈ [−e−1, ∞].

The earliest mention of the problem of Eq. (2) is attributed to Euler [1]. However, Euler himself credited Lambert for his previous work in this subject, Lambert’s transcendental equation [2]. The W(x) function started to be named after Lambert only recently, in the last 20 years or so; nevertheless, the ﬁrst usage of the letter W appeared much earlier [3].

Recently, the W(x) function amassed quite a following in the mathematical community [4]. Its most faithful proponents are suggesting elevating it among the present set of elementary functions, such as sin(x), cos(x), exp(x), ln(x), etc. The main argument for doing so is the fact that W is the root of the simplest exponential polynomial function given in Eq. (2). We will acknowledge these efforts by strict usage of a roman symbol W as its name.

While the Lambert W function is called LambertW in the mathematics software tool Maple [5] and lambertw in the Matlab programming environment [6], in the Mathematica computer algebra framework this function [7] is implemented under the name ProductLog (in the recent versions an alias LambertW is also supported). In open source format the Lambert W function is available in the special-functions part of the GNU Scientiﬁc Library (GSL) [8], unfortunately implemented using only the slower Halley’s iteration (see discussion in Section 6).

There are numerous, well documented applications of W(x), certainly abundant in mathematics (like linear delay-differential equations [9]), numerics [10], computer science [11] and engineering [12], but surprisingly many also in physics, just to mention a few (without preference): quantum mechanics (solutions for doublewell Dirac-delta potentials [13]), quantum statistics [14], general relativity (solutions to (1+1)-gravity problem [15],

0

W0

- 0.4 0.2 0.0 0.2 0.4 0.6 0.8 1.0

4

3

2

- 1


W x

W 1

x

Figure 1: The two branches of the Lambert W function, W−1(x) in blue and W0(x) in red. The branching point at (−e−1, −1) is indicated with a green dash.

inverse of Eddington-Finkelstein (tortoise) coordinates [16]), statistical mechanics [17], ﬂuid dynamics [18], optics [19] etc.

The main motivation for the implementation in this work comes from the research in cosmic ray physics where it has been in use already for several years [20] and new interesting applications are appearing frequently [21]. In the next sections let us describe two new examples that arise from this ﬁeld of astrophysics.

- 1.1. Inverse of the Moyal function The Moyal function and the related distribution was

proposed as a good approximation for the more complicated Landau distribution [22] used in descriptions of energy loss of charged particles passing through matter [23]. The un-normalized Moyal function is deﬁned as

M(x) = exp −12 x + e−x (5) and can be seen in Fig. 2 (top).

Its inverse can be written in terms of the two branches of the Lambert W function,

M−1

± (x) = W0,−1(−x2) − 2ln x. (6)

In experimental astrophysics the Moyal function is used for phenomenological recovery of the saturated signals from photomultipliers [24], where the largest parts of the saturated signals are obscured by the limited range of the analog-to-digital converters.

- 1.2. Inverse of the Gaisser-Hillas function In astrophysics the Gaisser-Hillas function is used to


model the longitudinal particle density in a cosmic-ray air shower [25]. We can show that the inverse of the three-parametric Gaisser-Hillas function,

G(X; X0, Xmax, λ) =

X − X0 Xmax − X0

Xmax−X0 λ

exp

Xmax − X λ

(7)

,

0.6

0.5

0.4

M x

0.3

0.2

0.1

0.0

2 0 2 4 6 8

x

1.0

0.8

;g xxmax

0.6

0.4

0.2

0.0

0 5 10 15 20 25 30

x

- Figure 2: Top: The Moyal function M(x). Bottom: A family of one-


parametric Gaisser-Hillas functions g(x; xmax) for xmax in the range from 1 to 10 with step 1.

is intimately related to the Lambert W function. Using rescale substitutions,

X − X0 λ

x =

Xmax − X0 λ

and xmax =

, (8)

the Gaisser-Hillas function is modiﬁed into a function of one parameter only,

g(x; xmax) =

x xmax

xmax

exp(xmax − x). (9)

The family of one-parametric Gaisser-Hillas functions is shown in Fig. 2 (bottom). The problem of ﬁnding an inverse,

g(x; xmax) ≡ y (10) for 0 < y 1, can be rewritten into

x xmax

x xmax

exp −

−

= −y1/xmax e−1. (11)

According to the deﬁnition (2), the two (real) solutions for x are obtained from the two branches of the Lambert W function,

x1,2 = −xmax W0,−1(−y1/xmax e−1). (12)

Note that the branch −1 or 0 simply chooses the right or left side relative to the maximum, respectively.

The Gaisser-Hillas function is intimately related to the gamma distribution which was successfully used somewhat earlier [26] in an approximate description of the mean longitudinal proﬁle of the energy deposition in electromagnetic cascades. It is trivial to show that the inverses of the gamma and inverse-gamma distributions [27] are expressible in terms of the Lambert W function as well.

##### 2. Numerical methods

Before describing the actual implementation let us review some of the possible numerical and analytical approaches to ﬁnd W(x).

2.1. Recursion

For x > 0 and W(x) > 0 we can take the natural logarithm of Eq. (4) and rearrange it into

W(x) = ln x − lnW(x). (13)

From here it is clear that an analytical expression for W(x) will exhibit a certain degree of self similarity. The W(x) function has multiple branches in the complex domain. Due to the x > 0 and W(x) > 0 conditions, Eq. (13) represents the positive part of the W0(x) principal branch and in this form it is suitable for evaluation when W0(x) > 1, i.e. when x > e.

Unrolling the self-similarity in Eq. (13) as a recursive

relation, the following curious expression for W0(x) is obtained,

W0(x) = ln x − ln(ln x − ln(ln x − . . . )), (14) or in the shorthand of a continued logarithm,

x ln lnxx

. (15)

W0(x) = ln

···

The above expression clearly has the form of successive approximations, the ﬁnal result given by the limit, if it exists.

For x < 0 and W(x) < 0 we can multiply both sides of Eq. (4) with −1, take logarithm, and rewrite it into a similar expansion for the W−1(x) branch,

W(x) = ln(−x) − ln(− W(x)). (16) Again, this leads to the similar recursion,

W−1(x) = ln(−x) − ln(−(ln(−x) − ln(− . . .))), (17) or as a continued logarithm,

W−1(x) = ln −x

. (18)

− ln −x

− ln −x

···

For this continued logarithm we will use the symbol R[−n1](x) where n denotes the depth of the recursion in Eq. (18).

Starting from yet another rearrangement of Eq. (4),

x expW(x)

, (19)

W(x) =

we can obtain a recursion relation for the −e−1 < x < e part of the principal branch W0(x) < 1,

x exp expx x

. (20)

W0(x) =

...

- 2.2. Halley’s iteration

We can apply Halley’s root-ﬁnding method [28] to derive an iteration scheme for f(y) = W(y) − x by writing the second-order Taylor series

f(y) = f(yn) + f (yn) (y − yn) + 12 f (yn) (y − yn)2 + · · ·

(21) Since root y of f(y) satisﬁes f(y) = 0 we can approximate the left-hand side of Eq. (21) with 0 and replace y with yn+1. Rewriting the obtained result into

yn+1 = yn −

f(yn) f (yn) + 12 f (yn) (yn+1 − yn)

(22)

and using Newton’s method yn+1 −yn = −f(yn)/f (yn) on the last bracket, we arrive at the expression for Halley’s iteration for the Lambert W function

Wn+1 = Wn +

tn tn sn − un

, (23)

where

tn = Wn eWn − x, (24) sn =

Wn + 2 2(Wn + 1)

, (25) un = (Wn + 1) eWn. (26)

This method is of the third order, i.e. having Wn = W(x) + O(ε) will produce Wn+1 = W(x) + O(ε3). Supplying this iteration with a sufﬁciently accurate ﬁrst approximation of the order of O(10−4) will thus give a machine-size ﬂoating point precision O(10−16) in at least two iterations.

- 2.3. Fritsch’s iteration


For both branches of the Lambert W function a more efﬁcient iteration scheme exists [29],

Wn+1 = Wn(1 + εn), (27)

where εn is the relative difference of successive approximations at iteration n,

Wn+1 − Wn Wn

. (28)

εn =

The relative difference can be expressed as

zn 1 + Wn

qn − zn qn − 2zn

, (29)

εn =

where

x

zn = ln

Wn − Wn, (30)

qn = 2(1 + Wn) 1 + Wn + 32zn . (31) The error term in this iteration is of a fourth order, i.e. with Wn = W(x) + O(εn) we obtain Wn+1 = W(x) + O(ε4n).

Supplying this iteration with a sufﬁciently reasonable ﬁrst guess, accurate to the order of O(10−4), will therefore deliver machine-size ﬂoating point precision O(10−16) in only one iteration and excessive O(10−64) in two! The main goal now is to ﬁnd reliable ﬁrst order approximations that can be fed into Fritsch’s iteration. Due to the lively landscape of the Lambert W function properties, the approximations will have to be found in all the particular ranges of the function’s behavior.

##### 3. Initial approximations

The following section deals with ﬁnding the appropriate initial approximations in the whole deﬁnition range of the two branches of the Lambert W function.

3.1. Branch-point expansion

The inverse of the Lambert W function, W−1(y) = y ey, has two extrema located at W−1(−1) = −e−1 and W−1(−∞) = 0−. Expanding W−1(y) to the second order around the minimum at y = −1 we obtain

(y + 1)2 2e

1 e

W−1(y) ≈ −

. (32)

+

The inverse W−1(y) is thus approximated in the lowest order by a parabolic term implying that the Lambert W function will have square-root behavior in the vicinity of the branch point x = −e−1,

W−1,0(x) ≈ −1 ∓ 2(1 + ex). (33)

To obtain the additional terms in Eq. (33) we proceed by deﬁning an inverse function, centered and rescaled around the minimum, i.e. f(y) = 2(e W−1(y − 1) + 1). Due to this centering and rescaling, the Taylor series around

y = 0 becomes particularly neat,

f(y) = y2 + 32y3 + 14y4 + 151 y5 + · · · (34) Using this expansion we can derive coefﬁcients [30] of the corresponding inverse function

z − 2 2e

f−1(z) = 1 + W

= (35)

= z1/2 − 13z + 7211z3/2 − 54043 z2 + · · · (36)

W0

1

2

3

W x

4

5

6

W 1

7

0.3 0.2 0.1 0.0

x

W0

0.0

W x

0.5

1.0

W 1

0.3 0.2 0.1 0.0 0.1 0.2

x

- Figure 3: Successive orders of the branch-point expansion for W−1(x) on the top and W0(x) on the bottom.


From Eq. (35) we see that z = 2(1 + ex). Using p±(x) = ± 2(1 + ex) as an independent variable we can write this series expansion as

W−1,0(x) ≈ B−[n1,0] (x) =

n

bipi∓(x), (37)

### ∑

i=0

where the lowest few coefﬁcients bi are

i 0 1 2 3 4 5 6 7 bi -1 1 −13

11 72 −54043

17280 −8505221

769

680863 43545600

and more of them are given in the accompanying code (see Fig. 3 for succesive orders of the series).

- 3.2. Asymptotic series Another useful tool is the asymptotic expansion [31].


Using

A(a,b) = a−b+∑

k

Ckma−k−m−1bm+1, (38)

### ∑

m

with Ckm related to the Stirling numbers of the ﬁrst kind, the Lambert W function can be expressed as

W−1,0(x) = A(ln(∓x), ln(∓ ln(∓x))), (39)

with a = ln x, b = lnln x for the W0 branch and a = ln(−x), b = ln(− ln(−x)) for the W−1 branch. The ﬁrst few terms are

b(6 − 9b + 2b2) 6a3

b(−2 + b) 2a2

b a

A(a, b) = a − b +

+

+

+

b(−12 + 36b − 22b2 + 3b3) 12a4

+ (40)

+

b(60 − 300b + 350b2 − 125b3 + 12b4) 60a5

#### + · · ·

+

3.3. Rational ﬁts

A useful quick-and-dirty approach to the functional approximation is to generate a large enough sample of data points {wi ewi, wi}, which evidently lie on the Lambert W function. Within some appropriately chosen range of wi values, the points are ﬁtted with a rational approximation

∑i aixi ∑i bixi

, (41)

Q(x) =

varying the order of the polynomials in the nominator and denominator, and choosing the one that has the lowest maximal absolute residual in a particular interval of interest.

For the W0(x) branch, the ﬁrst set of equally-spaced wi components was chosen in a range that produced wi ewi values in an interval [−0.3, 0]. The optimal rational ﬁt turned out to be

- 1 + a1x + a2x2 + a3x3 + a4x4

- 1 + b1x + b2x2 + b3x3 + b4x4


(42)

Q0(x) = x

where the coefﬁcients1 for this ﬁrst approximation Q0[1](x) are

i 1 2 3 4 ai 5.931375’ 11.392205’ 7.338883’ 0.653449’ bi 6.931373’ 16.823494’ 16.430723’ 5.115235’

For the second ﬁt of the W0(x) branch a wi range was chosen so that the wi ewi values were produced in the interval [0.3, 2e], giving rise to the second optimal

rational ﬁt Q0[2](x) of the same form as in Eq. (42) but with coefﬁcients

i 1 2 3 4 ai 2.445053’ 1.343664’ 0.148440’ 0.000804’ bi 3.444708’ 3.292489’ 0.916460’ 0.053068’

For the W−1(x) branch a single rational approximation of the form

a0 + a1x + a2x2 1 + b1x + b2x2 + b3x3 + b4x4 + b5x5

(43) with the coefﬁcients

Q−1(x) =

1The ’ symbol in coefﬁcient values denotes truncation in this presentation; the full machine-size sets of decimal places are given in the accompanying code.

i 0 1 2 ai -7.814176’ 253.888101’ 657.949317’ bi -60.439587’ 99.985670’ i 3 4 5 bi 682.607399’ 962.178439’ 1477.934128’

is enough.

##### 4. Implementation

To quantify the accuracy of a particular approximation W(x) of the Lambert function W(x) we can introduce a quantity ∆(x) deﬁned as

∆(x) = log10 | W(x)| − log10 | W(x) − W(x)|, (44) so that it gives us a number of correct decimal places the approximation W(x) is producing for some value of the parameter x.

In Fig. 4 all approximations for the W0(x) mentioned above are shown in the linear interval [−e−1, 0.3] on the left and the logarithmic interval [0.3, 105] on the right. For each of the approximations an optimal interval is chosen so that the number of accurate decimal places is maximized over the whole deﬁnition range. For the W0(x) branch the resulting piecewise approximation

 

B0[9](x) ; −e−1 x < a

- Q0[1](x) ; a x < b
- Q0[2](x) ; b x < c A0(x) ; c x < ∞


(45)

W0(x) =



with a = −0.323581 , b = 0.145469 , and c = 8.706658 , is accurate in the deﬁnition range [−e−1, 7] to at least 5 decimal places and to at least 3 decimal places in the whole

deﬁnition range [−e−1, ∞]. Note that B0[9](x) comes from Eq. (37), Q0[1](x) and Q0[2](x) are from Eq. (42), and A0(x) is from Eq. (40).

The accuracy of the ﬁnal piecewise approximation W0(x) is shown in Fig. 5 (black line). Using this approximation, a single step of Halley’s iteration (red) and Fritsch’s iteration (blue) is performed and the resulting number of accurate decimal places is shown. As can be seen from the plots, both iterations produce machinesize accurate ﬂoating point numbers in the whole deﬁnition interval except for the interval between 6.5 and 190 where the Halley’s method requires another step of the iteration. For that reason we have decided to use only (one step of) Fritsch’s iteration in the C++ implementation of the Lambert W function.

In Fig. 6 (top) the same procedure is shown for the W−1(x) branch. The ﬁnal approximation

 

B−[91] (x) ; −e−1 x < a

W−1(x) =

(46)

- Q−1(x) ; a x < b
- R−[9]1(x) ; b x < 0




20

15

10

5

0

0.3 0.2 0.1 0.0 0.1 0.2 0.3

x

20

15

10

5

0

1 10 100 1000 104 105

x

Figure 4: Combining different approximations of W0(x) into a ﬁnal piecewise function. The number of accurate decimal places ∆(x) is shown for two ranges, linear interval [−e−1, 0.3] (top) and logarithmic interval [0.3, 105] (bottom). The approximations are branch-point

expansion B0[9](x) from Eq. (37) (blue), rational ﬁts Q0[1](x) and Q0[2](x) from Eq. (42) in black and red, respectively, and asymptotic series A0(x) from Eq. (40) (green).

with a = −0.302985 and b = −0.051012 , is accurate to at least 5 decimal places in the whole deﬁnition range

[−e−1, 0]. Note that B−[91] (x) is taken from Eq. (37), Q−1(x) is from Eq. (43), and R[−9]1(x) is from Eq. (18).

In Fig. 6 (bottom) the combined approximation W−1(x)

is shown (black line). The values after one step of Halley’s iteration are shown in red and after one step of Fritsch’s iteration in blue. Similarly as for the previous branch, Fritsch’s iteration turns out to be superior, yielding machine-size accurate results in the whole deﬁnition range, while Halley’s iteration is accurate to at least 13 decimal places.

##### 5. Source availability, installation and usage

The most recent version of the sources of this implementation with some additional material and examples are available from

20

20

15

15

10

10

5

5

0

0

0.35 0.30 0.25 0.20 0.15 0.10 0.05 0.00

0.3 0.2 0.1 0.0 0.1 0.2 0.3

x

x

20

20

15

15

10

10

5

5

0

0.35 0.30 0.25 0.20 0.15 0.10 0.05 0.00

0

1 10 100 1000 104 105

x

x

Figure 6: Top: Approximations of the W−1(x) branch. The branchpoint expansion B−[91] (x) is shown in blue, the rational approximation Q−1(x) in black, and the logarithmic recursion R[−9]1 in red. Bottom: The combined approximation is accurate to at least 5 decimal places in the whole deﬁnition range. The results after applying one step of Halley’s iteration are shown in red and after one step of Fritsch’s iteration in blue.

Figure 5: Final values of the combined approximation W0(x) (black) from Fig. 4 after one step of Halley’s iteration (red) and one step of Fritsch’s iteration (blue).

###### https://github.com/DarkoVeberic/LambertW and are released under the dual GPL/BSD license.

Apart from the special functions in GSL [8], this is the only freely available implementation of the Lambert W function in C++ and to the best of our knowledge the only implementation using the superior Fritsch’s version of the iteration.

is to force the users to think about the two possible solutions to the problem in Eq. (2). Just as for solutions to the quadratic equation where the ± sign has to be chosen based on the desired solution, the Lambert W function offers two possibilities that need careful consideration.

The supplied C++ code implements the following set of functions2

The initial approximations Wb(x) from Eqs. (46) and (45), that are used to kick-start the iterations, are also directly available as LambertWApproximation<b>(x), as they might be useful in applications for which it is sufﬁcient to have a limited number of accurate decimal places (see the discussion above).

- • double LambertWApproximation<b>(double x);
- • double LambertW<b>(double x);
- • double LambertW(int branch, double x);


The supplied code does not need any kind of special installation procedures. In the case that your analysis needs an evaluation of the Lambert W function, the two source ﬁles, LambertW.h and LambertW.cc, should be simply bundled with your project structure and compiled with a suitable C++ compiler.

where b in the ﬁrst two functions should be replaced with the compile-time branch integer value, e.g. LambertW<-1>(x) or LambertW<0>(x). Apart from the slightly increased efﬁciency, the main reason for implementing the ﬁrst two functions with the branch b as a compile time parameter

The source distribution also includes a command-line utility implemented by the lambert-w.cc source ﬁle. The included Makefile can, with the request make lambert-w,

2Which can be found in the ﬁles LambertW.h and LambertW.cc.

- 0

- 1

- 2

- 3

- 4

- 5

- 6


by the pure function call, t = t − toverhead. The ratio t gsl/t is then plotted in Fig. 7.

As can be clearly seen from Fig. 7, our implementation is at least 2× faster than GSL for a broad range of input parameters x, but the largest efﬁciency gains (up to 5×) are observed in the ranges where rational ﬁts Qb from Eqs. (45) and (46) are used. Although Fritsch’s iteration is in general more complex than Halley’s, at the end it pays off, yielding machine-size accuracy with a single step where Halley’s might need more, also due to poor initial approximations used in GSL. GSL performs better only in the small regions where branch-point and asymptotic expansions are used without the consequent Halley’s iteration reﬁnements. The comparisons were made on the Ubuntu 12.04 x86 64 Linux operating system running on a 2.2GHz AMD Opteron 275 processor, using the GCC 4.6.3 compiler with optimization option -O2.

relativespeedup,t tgsl

0.0 0.5 1.0 1.5 2.0 x

Figure 7: Execution speedup t gsl/t , relative to the GSL implementation [8] for the W0(x) branch (red) and the W−1(x) branch (blue). For x > 2 the ratio slowly decreases and is ∼ 2 for x > 8. Time of the respective driver loops and function calls was subtracted in order to measure only differences between the pure numerical parts of the two implementations (see text for details).

##### 7. Conclusions

build an executable command. It can be invoked through a shell as ./lambert-w [branch] x, taking an optional branch number (0 by default) and a parameter x. The output of the command is equivalent to the Wbranch(x) return value and can thus be simply used in shell scripts (sh, bash, or csh) or other programming languages with easy access to shell invocations (awk, perl etc.).

Also included in the distribution is a test suite which can perform a correctness check on your build by comparing obtained and expected return values of the Lambert W function on your system. It is invoked by the command make tests. Any potential discrepancies larger than the double machine precision ( 10−14) will be reported in the output.

We have shown that Fritsch’s iteration scheme coupled with accurate initial approximations can deliver signiﬁcant efﬁciency gains in the numerical evaluation of the real branches of the Lambert W function. The opensource release of our C++ implementation is suitable for inclusion in various analysis packages used in all ﬁelds of physics.

##### Acknowledgments

The author wishes to thank Matej Horvat, Michael Unger, Martin O’Loughlin, and Amir Malekpour for useful discussions and suggestions. This work was partially supported by the Slovenian Research Agency.

##### 6. Timing

We have decided to compare the execution time of our code relative to the GNU GSL library (implemented in the C language) since comparisons to interpreted code (like Maple, Matlab or Mathematica) would, besides common availability problems, not be fair in terms of speed.

In Fig. 7 relative speedup, tgsl/t, is shown as a function of the Lambert W parameter x. Timing accuracy of several % was achieved by running 3000000 function calls in a loop, taking special care that the compiler did not optimize code away by slightly modifying x on each call and then gathering all results into a summed variable reported at the end. For each of the two implementations an identical code was also run with the Lambert W function call replaced with a simple identity function (just returning its input parameter) in order to estimate the overhead of the surrounding timing code. This toverhead is then consequently subtracted from the time of the Lambert W runs t, giving an approximation to the time taken

##### References

- [1] L. Euler, Acta Acad. Scient. Petropol. 2 (1783) 29–51.
- [2] J.H. Lambert, Acta Helvitica 3 (1758) 128–168.
- [3] G. P´olya and G. Szeg¨o, Aufgaben und Lehrs¨atze aus der Analysis, J. Springer, Berlin, 1925.
- [4] http://www.orcca.on.ca/LambertW/.
- [5] R.M. Corless, G.H. Gonnet, D.E.G. Hare, and D.J. Jeffrey, Maple Technical Newsletter 9 (1993) 12.
- [6] http://www.mathworks.com/help/toolbox/symbolic/ lambertw.html; some open source versions for Matlab: P. Getreuer and D. Clamond, http://www.getreuer.info/home/ lambertw; N.N. Schraudolph and D. Ross, http://www.cs.toronto.edu/˜dross/code/LambertW.m.
- [7] E.W. Weisstein, Lambert W-Function, MathWorld Wolfram Web Resource, http://mathworld.wolfram.com/LambertW-Function.html.
- [8] G. Jungman and K. Briggs, GNU Scientiﬁc Library, gsl-1.15, specfunc/lambert.c, http://www.gnu.org/software/gsl/.
- [9] F.M. Asl and A.G. Ulsoy, J. Dyn. Sys. Meas. Control 125 (2003) 215; S. Yi, P.W. Nelson, and A.G. Ulsoy, IEEE Trans. Autom. Control 53 (2008) 854–860.
- [10] R.M. Corless, G.H. Gonnet, D.E.G. Hare, D.J. Jeffrey, and D.E. Knuth, Adv. Comput. Math. 5 (1996) 329; R.M. Corless, D.J. Jeffrey, and D.E. Knuth, 1997, A Sequence of Series for the Lambert Function, in: Proc. ISSAC ’97, Maui, (1997) 197–204;


R.M. Corless and D.J. Jeffrey, The Wright ω function, in: J. Calmet, B. Benhamou, O. Caprotti, L. Henocque, V. Sorge (Eds.), Artiﬁcial Intelligence, Automated Reasoning, and Symbolic Computation, in:

Proc. AISC-Calculemus 2002, Springer (2002) 76–89.

- [11] J. Bustos-Jimenez, N. Bersano, S.E. Schaeffer, J.M. Piquer, A. Iosup, and A. Ciuffoletti, in Grid Computing: Achievements and Prospects, eds. S. Gorlatch, P. Fragopoulou, and T. Priol, Springer

(2008); doi:10.1007/978-0-387-09457-1 6.

- [12] S. Yi, P.W. Nelson, and A.G. Ulsoy, Math. Biosci. Engrg. 4 (2007) 355–368.
- [13] T.C. Scott, M. Aubert-Fr´econ, and J. Grotendorst, Chem. Phys. 324 (2006) 323–338; T.C. Scott, A. Luchow,¨ D. Bressanini, and J.D. Morgan III, Phys. Rev. A 75 (2007) 060101R; T.C. Scott, J.F. Babb, A. Dalgamo, and J.D. Morgan III, Chem. Phys. Lett. 203

(1993) 175–183.

- [14] S.R. Valluri, M. Gil, D.J. Jeffrey, and S. Basu, J. Math. Phys. 50

(2009) 102103.

- [15] T.C. Scott, R. Mann, and R.E. Martinez II, Appl. Algebra Engrg. Comm. Comput. 17 (2006) 41–47.
- [16] A.S. Eddington, Nature 113 (1924) 192; T. Regge and J.A. Wheeler, Phys. Rev. 108 (1957) 1063–1069.
- [17] J.-M. Caillol, J. Phys. A 36 (2003) 10431–10442.
- [18] S.P. Pudasaini, Phys. Fluids 23 (2011) 043301.


- [19] O. Steinvall, Appl. Optics 48 (2009) B1–B7.
- [20] S. Argir`o et al., Nucl. Instr. and Meth. A 580 (2007) 1485.
- [21] K.-H. Kampert and M. Unger, Astropart. Phys. 35 (2012) 660–678; arXiv:1201.0018.
- [22] J.E. Moyal, Phil. Mag. 46 (1955) 263.
- [23] L.D. Landau, J. Phys. USSR 8 (1944) 201–205.
- [24] I.C. Maris¸, M. Roth, and T. Schmidt, A Phenomenological Method to Recover the Signal from Saturated Stations, P. Auger Collaboration internal note GAP-2006-012.
- [25] T.K. Gaisser and A.M. Hillas, Proc. of the 15th Internation Cosmic-Ray Conference, Plavdiv, 8 (1977) 353.
- [26] E. Longo and I. Sestili, Nucl. Instrum. Methods 128 (1975) 283.
- [27] C. Walck, Hand-book on statistical distributions for experimentalists, Stockholms Universitet, Internal Report SUF-PFY/96-01, 10 September 2007, pp. 69–74.
- [28] T.R. Scavo and J.B. Thoo, Amer. Math. Monthly 102 (1995) 417.
- [29] F.N. Fritsch, R.E. Shafer, and W.P. Crowley, Commun. ACM 16

(1973) 123.

- [30] P.M. Morse and H. Feshbach, Methods of Theoretical Physics, Part I, McGraw-Hill, New York (1953) 411.
- [31] N.G. de Bruijn, Asymptotic Methods in Analysis, New York, Dover


(1981) 27.

