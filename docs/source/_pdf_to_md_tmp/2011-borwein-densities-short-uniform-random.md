# arXiv:1103.2995v2[math.CA]11Aug2011

## DENSITIES OF SHORT UNIFORM RANDOM WALKS

JONATHAN M. BORWEIN, ARMIN STRAUB, JAMES WAN, AND WADIM ZUDILIN with an appendix by: DON ZAGIER

Abstract. We study the densities of uniform random walks in the plane. A special focus is on the case of short walks with three or four steps and less completely those with ﬁve steps. As one of the main results, we obtain a hypergeometric representation of the density for four steps, which complements the classical elliptic representation in the case of three steps. It appears unrealistic to expect similar results for more than ﬁve steps. New results are also presented concerning the moments of uniform random walks and, in particular, their derivatives. Relations with Mahler measures are discussed.

1. Introduction

An n-step uniform random walk is a walk in the plane that starts at the origin and consists of n steps of length 1 each taken into a uniformly random direction. The study of such walks largely originated with Pearson more than a century ago [Pea05b, Pea05a, Pea06] who posed the problem of determining the distribution of the distance from the origin after a certain number of steps. In this paper, we study the (radial) densities pn of the distance travelled in n steps. This continues research commenced in [BNSW09, BSW11] where the focus was on the moments of these distributions:

n

pn(t)ts dt. The densities for walks of up to 8 steps are depicted in Figure 1. As established

Wn(s) :=

0

by Lord Rayleigh [Ray05], pn quickly approaches the probability density 2nxe−x2/n for large n. This limiting density is superimposed in Figure 1 for n 5.

Closed forms were only known in the cases n = 2 and n = 3. The evaluation, for 0 x 2,

2 π√4 − x2

(1) p2(x) =

2010 Mathematics Subject Classiﬁcation. Primary 60G50; Secondary 33C20, 34M25, 44A10.

1

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0.5 1.0 1.5 2.0 2.5 3.0

(a) p3

0.35

0.30

0.25

0.20

0.15

0.10

0.05

1 2 3 4 5 6

(d) p6

0.5

0.4

0.3

0.2

0.1

1 2 3 4

(b) p4

0.30

0.25

0.20

0.15

0.10

0.05

1 2 3 4 5 6 7

(e) p7

0.35

0.30

0.25

0.20

0.15

0.10

0.05

1 2 3 4 5

#### (c) p5

0.30

0.25

0.20

0.15

0.10

0.05

2 4 6 8

(f) p8

Figure 1. Densities pn with the limiting behaviour superimposed for n 5.

is elementary. On the other hand, the density p3(x) for 0 x 3 can be expressed in terms of elliptic integrals by

- (2) p3(x) = Re

√x π2

K

(x + 1)3(3 − x) 16x

,

see, e.g., [Pea06]. One of the main results of this paper is a closed form evaluation of p4 as a hypergeometric function given in Theorem 8. In (20) we also provide a single hypergeometric closed form for p3 which, in contrast to (2), is real and valid on all of [0,3]. For convenience, we list these two closed forms here:

p3(x) =

2√3 π

x (3 + x2)2

F1

1

3, 32 1

x2 (9 − x2)2 (3 + x2)3

- (3) ,

p4(x) =

2 π2

√16 − x2 x

Re3F2

- 1

- 2, 12, 21


- 5

- 6, 76


(16 − x2)3 108x4

- (4) .


We note that while Maple handled these well to high precision, Mathematica struggled, especially with the analytic continuation of the 3F2 when the argument is greater than 1.

A striking feature of the 3- and 4-step random walk densities is their modularity. It is this circumstance which not only allows us to express them via hypergeometric series, but also makes them a remarkable object of mathematical study.

This paper is structured as follows: In Section 2 we give general results for the densities pn and prove for instance that they satisfy certain linear diﬀerential equations. In Sections 3, 4, and 5 we provide special results for p3, p4, and p5 respectively. Particular interest is taken in the behaviour near the points where the densities fail to be smooth. In Section 6 we study the derivatives of the moment function and make a connection to multidimensional Mahler measures. Finally in Section 7 we provide some related new evaluations of moments and so resolve a central case of an earlier conjecture on convolutions of moments in [BSW11].

The amazing story of the appearance of Theorem 4 is worth mentioning here. The theorem was a conjecture in an earlier version of this manuscript, and one of the present authors communicated it to D. Zagier. That author was surprised to learn that Zagier had already been asked for a proof of exactly the same identities a little earlier, by P. Djakov and B. Mityagin.

Those authors had in fact proved the theorem already in 2004 (see [DM04, Theorem 4.1] and [DM07, Theorem 8]) during their study of the asymptotics of the spectral gaps of a Schr¨odinger operator with a two-term potential — their proof was indirect, so that we should never have come across the identities without the accident of asking the same person the same question! Djakov and Mityagin asked Zagier about the possibility of a direct proof of their identities (the subject of Theorem 4), and he gave a very neat and purely combinatorial answer. It is this proof which is herein presented in the Appendix.

We close this introduction with a historical remark illustrating the fascination arising from these densities and their curious geometric features. H. Fettis devotes the entire paper [Fet63] to proving that p5 is not linear on the initial interval [0,1] as ruminated upon by Pearson [Pea06]. This will be explained in Section 5.

2. The densities pn

It is a classical result of Kluyver [Klu06] that pn has the following Bessel integral representation:

∞

xtJ0(xt)J0n(t)dt. Here Jν is the Bessel function of the ﬁrst kind of order ν.

(5) pn(x) =

0

Remark 1. Equation (5) naturally generalizes to the case of nonuniform step lengths. In particular, for n = 2 and step lengths a and b we record (see [Wat41, p. 411] or

[Hug95, 2.3.2]; the result is attributed to Sonine) that the corresponding density is p2(x;a,b) =

∞

xtJ0(xt)J0(at)J0(bt)dt

0

2x π ((a + b)2 − x2)(x2 − (a − b)2)

=

- (6)

for |a − b| x a + b and p2(x;a,b) = 0 otherwise. Observe how (6) specializes to

(1) in the case a = b = 1.

In the case n = 3 the density p3(x;a,b,c) has been evaluated by Nicholson [Wat41, p. 414] in terms of elliptic integrals directly generalizing (2). The corresponding extensions for four and more variables appear much less accessible. ♦

It is visually clear from the graphs in Figure 1 that pn is getting smoother for increasing n. This can be made precise from (5) using the asymptotic formula for J0 for large arguments and dominated convergence:

Theorem 1. For each integer n 0, the density pn+4 is n/2 times continuously diﬀerentiable.

On the other hand, we note from Figure 1 that the only points preventing pn from being smooth appear to be integers. This will be made precise in Theorem 2.

To this end, we recall a few things about the s-th moments Wn(s) of the density pn which are given by

- (7) Wn(s) =

∞

0

xspn(x)dx =

[0,1]n

n

k=1

e2πx

ki

s

dx.

Starting with the right-hand side, these moments had been investigated in [BNSW09, BSW11]. There it was shown that Wn(s) admits an analytic continuation to all of the complex plane with poles of at most order two at certain negative integers. In particular, W3(s) has simple poles at s = −2,−4,−6,... and W4(s) has double poles at these integers [BNSW09, Thm. 6, Ex. 2 & 3]. Moreover, from the combinatorial evaluation

- (8) Wn(2k) =


2

k a1,...,an

a1+···+an=k

for integers k 0 it followed that Wn(s) satisﬁes a functional equation, as in [BNSW09, Ex. 1], coming from the inevitable recursion that exists for the righthand side of (8) . For instance,

(s + 4)2W3(s + 4) − 2(5s2 + 30s + 46)W3(s + 2) + 9(s + 2)2W3(s) = 0, and equation (9) below.

The ﬁrst part of equation (7) can be rephrased as saying that Wn(s−1) is the Mellin transform of pn ([ML86]). We denote this by Wn(s−1) = M[pn;s]. Conversely, the density pn is the inverse Mellin transform of Wn(s − 1). We intend to exploit this relation as detailed for n = 4 in the following example.

Example 1 (Mellin transforms). For n = 4, the moments W4(s) satisfy the functional equation

- (9) (s + 4)3W4(s + 4) − 4(s + 3)(5s2 + 30s + 48)W4(s + 2) + 64(s + 2)3W4(s) = 0.

Recall the following rules for the Mellin transform: if F(s) = M[f;s] then in the appropriate strips of convergence

- • M[xµf(x);s] = F(s + µ),
- • M[Dxf(x);s] = −(s − 1)F(s − 1).


Here, and below, Dx denotes diﬀerentiation with respect to x, and, for the second rule to be true, we have to assume, for instance, that f is continuously diﬀerentiable.

Thus, purely formally, we can translate the functional equation (9) of W4 into the diﬀerential equation A4 · p4(x) = 0 where A4 is the operator

- (10) A4 = x4(θ + 1)3 − 4x2θ(5θ2 + 3) + 64(θ − 1)3
- (11) = (x − 4)(x − 2)x3(x + 2)(x + 4)Dx3 + 6x4 x2 − 10 Dx2


+ x 7x4 − 32x2 + 64 Dx + x2 − 8 x2 + 8 .

Here θ = xDx. However, it should be noted that p4 is not continuously diﬀerentiable. Moreover, p4(x) is approximated by a constant multiple of √4 − x as x → 4− (see Theorem 5) so that the second derivative of p4 is not even locally integrable. In particular, it does not have a Mellin transform in the classical sense. ♦

Theorem 2. Let an integer n 1 be given.

- • The density pn satisﬁes a diﬀerential equation of order n − 1.
- • If n is even (respectively odd) then pn is real analytic except at 0 and the even (respectively odd) integers m ≤ n.


Proof. As illustrated for p4 in Example 1, we formally use the Mellin transform method to translate the functional equation of Wn into a diﬀerential equation An · y(x) = 0. Since pn is locally integrable and compactly supported, it has a Mellin transform in the distributional sense as detailed for instance in [ML86]. It follows rigorously that pn solves An · y(x) = 0 in a distributional sense. In other words, pn is a weak solution of this diﬀerential equation. The degree of this equation is n − 1 because the functional equation satisﬁed by Wn has coeﬃcients of degree n − 1 as shown in [BNSW09, Thm. 1].

The leading coeﬃcient of the diﬀerential equation (in terms of Dx as in (11)) turns out to be

- (12) xn−1

2|(m−n)

(x2 − m2)

where the product is over the even or odd integers 1 ≤ m ≤ n depending on whether n is even or odd. This is discussed below in Section 2.1.

Thus the leading coeﬃcient of the diﬀerential equation is nonzero on [0,n] except for 0 and the even or odd integers already mentioned. On each interval not containing these points it follows, as described for instance in [Ho¨r89, Cor. 3.1.6], that pn is in fact a classical solution of the diﬀerential equation. Moreover the analyticity of the coeﬃcients, which are polynomials in our case, implies that pn is piecewise real analytic as claimed.

Remark 2. It is one of the basic properties of the Mellin transform, see for instance [FS09, Appendix B.7], that the asymptotic behaviour of a function at zero is determined by the poles of its Mellin transform which lie to the left of the fundamental strip. It is shown in [BNSW09] that the poles of Wn(s) occur at speciﬁc negative integers and are at most of second order. This translates into the fact that pn has an expansion at 0 as a power series with additional logarithmic terms in the presence of double poles. This is made explicit in the case of p4 in Example 4.

2.1. An explicit recursion. We close this section by providing details for the claim made in (12). Recall that the even moments fn(k) := Wn(2k) satisfy a recurrence of order λ := n/2 with polynomial coeﬃcients of degree n − 1 (see [BNSW09]). An entirely explicit formula for this recurrence is given in [Ver04]:

Theorem 3.

- (13)


 kn+1

 fn(k − j) = 0

j

αi−1

k − i k − i + 1

(−αi)(n + 1 − αi)

α1,...,αj

j 0

i=1

where the sum is over all sequences α1,...,αj such that 0 αi n and αi+1 αi−2.

Observe that (12) is easily checked for each ﬁxed n by applying Theorem 3. We explicitly checked the cases n 1000 (using a recursive formulation of Theorem 3 from [Ver04]) while only using this statement for n 5 in this paper. The fact that (12) is true in general is recorded and made more explicit in Theorem 4 below.

For ﬁxed n, write the recurrence for fn(k) in the form j n=0−1 kjqj(K) where qj are polynomials and K is the shift k → k + 1. Then qn−1 is the characteristic polynomial of this recurrence, and, by the rules outlined in Example 1, we ﬁnd that the diﬀerential equation satisﬁed by pn(x) is of the form qn−1(x2)θn−1 + ··· , where θ = xDx and the dots indicate terms of lower order in θ.

We claim that the characteristic polynomial of the recurrence (13) satisﬁed by

fn(k) is 2|(m−n)(x − m2) where the product is over the integers 1 ≤ m ≤ n such that m ≡ n modulo 2. This implies (12). By Theorem 3 the characteristic polynomial is

- (14)

λ

j=0



 α1,...,αj

j

i=1

(−αi)(n + 1 − αi)

 xλ−j

where λ = n/2 and the sum is again over all sequences α1,...,αj such that 0

αi n and αi+1 αi −2. The claimed evaluation is thus equivalent to the following identity, ﬁrst proven by P. Djakov and B. Mityagin [DM04, DM07]. Zagier’s more direct and purely combinatorial proof is given in the Appendix.

- Theorem 4. For all integers n,j 1,


- (15)

0 m1,...,mj<n/2 mi<mi+1

j

i=1

(n − 2mi)2 =

1 α1,...,αj n αi αi+1−2

j

i=1

αi(n + 1 − αi).

3. The density p3

The elliptic integral evaluation (2) of p3 is very suitable to extract information about the features of p3 exposed in Figure 1(a). It follows, for instance, that p3 has a singularity at 1. Moreover, using the known asymptotics for K(x), we may deduce that the singularity is of the form

- (16) p3(x) =

3 2π2

log

4 |x − 1|

+ O(1) as x → 1.

We also recall from [BSW11, Ex. 5] that p3 has the expansion, valid for 0 x 1,

- (17) p3(x) =

2x π√3

∞

k=0

W3(2k)

x 3

2k

where

- (18) W3(2k) =

k

j=0

k j

2 2j j

is the sum of squares of trinomials. Moreover, we have from [BSW11, Eqn. 29] the functional relation

- (19) p3(x) =


4x (3 − x)(x + 1)

p3

3 − x 1 + x

so that (17) determines p3 completely and also makes apparent the behaviour at 3. We close this section with two more alternative expressions for p3.

- Example 2 (Hypergeometric form for p3). Using the techniques in [CZ10] we can deduce from (17) that

- (20) p3(x) =

2√3x π (3 + x2) 2

F1

1 3

,

- 2

- 3


; 1;

x2 (9 − x2)2 (3 + x2)3

which is found in a similar but simpler way than the hypergeometric form of p4 given in Theorem 8. Once obtained, this identity is easily proven using the diﬀerential equation from Theorem 2 satisﬁed by p3. From (20) we see, for example, that p3(√3)2 = 2π3

2

W3(−1). ♦

Example 3 (Iterative form for p3). The expression (20) can be interpreted in terms of the cubic AGM, AG3, see [BB91], as follows. Recall that AG3(a,b) is the limit of iterating

an+1 =

an + 2bn 3

, bn+1 = 3 bn

a2n + anbn + b2n 3

,

beginning with a0 = a and b0 = b. The iterations converge cubically, thus allowing for very eﬃcient high-precision evaluation. On the other hand,

1 AG3(1,s)

= 2F1

1 3

,

- 2

- 3


;1;1 − s3 so that in consequence of (20), for 0 x 3,

- (21) p3(x) =

2√3 π

x AG3(3 + x2,3|1 − x2|2/3)

.

Note that p3(3) =

√3

2π is a direct consequence of the ﬁnal formula.

Finally we remark that the cubic AGM also makes an appearance in the case n = 4. We just mention that the modular properties of p4 recorded in Remark 7 can be stated in terms of the theta functions

- (22) b(τ) =




η(τ)3 η(3τ)

η(3τ)3 η(τ)

, c(τ) = 3

where η is the Dedekind eta function deﬁned in (42). For more information and proper deﬁnitions of the functions b, c as well as a, which is related by a3 = b3 + c3, we refer to [BBG94]. Ultimately we are hopeful that, in search for an analogue of (19) for p4, this may lead to an algebraic relation between algebraically related arguments of p4. ♦

4. The density p4

The densities pn are recursively related. As in [Hug95], setting φn(x) = pn(x)/(2πx), we have that for integers n 2

- (23) φn(x) =

- 1

- 2π


2π

0

φn−1

√

x2 − 2xcosα + 1 dα.

We use this recursive relation to get some quantitative information about the behaviour of p4 at x = 4. Theorem 5. As x → 4−,

p4(x) =

√2 π2

√4 − x −

3√2 16π2

(4 − x)3/2 +

23√2 512π2

(4 − x)5/2 + O (4 − x)7/2 . Proof. Set y = √x2 − 2xcosα + 1. For 2 < x < 4,

φ4(x) =

1 π

π

0

φ3(y)dα =

1 π

arccos(x22−x8)

0

φ3(y)dα

since φ3 is only supported on [0,3]. Note that φ3(y) is continuous and bounded in the domain of integration. By the Leibniz integral rule, we can thus diﬀerentiate under the integral sign to obtain

- (24) φ 4(x) = −


arccos(x22−x8)

(x2 + 8)φ3(3) x (16 − x2)(x2 − 4)

1 π

φ 3(y) y

1 π

(x − cos(α))

+

dα.

0

This shows that φ 4, and hence p 4, have a singularity at x = 4. More speciﬁcally, φ 4(x) = −

1 8√2π3√4 − x

+ O(1) as x → 4−.

√3

Here, we used that φ3(3) =

12π2. It follows that p 4(x) = −

1 √2π2√4 − x

+ O(1)

which, upon integration, is the claim to ﬁrst order. Diﬀerentiating (24) twice more proves the claim.

- Remark 3. The situation for the singularity at x = 2+ is more complicated since in


(24) both the integral (via the logarithmic singularity of φ3 at 1, see (16)) and the boundary term contribute. Numerically, we ﬁnd, as x → 2+,

2 π2√x − 2

p 4(x) = −

+ O(1).

On the other hand, the derivative of p4 at 2 from the left is given by p 4(2−) =

√3 π 3

F2 −12, 13, 32 1,1

- 2

- 3


1 −

p4(2). These observations can be proven in hindsight from Theorem 7. ♦

We now turn to the behaviour of p4 at zero which we derive from the pole structure of W4 as described in Remark 2.

- 1

- 2

- 3

- 4


6 4 2 2

1

2

3

(a) W4

- 1

- 2

- 3

- 4


6 4 2 2

1

2

3

(b) W5

Figure 2. W4 and W5 analytically continued to the real line.

Example 4. From [BSW11], we know that W4 has a pole of order 2 at −2 as illustrated in Figure 2(a). More speciﬁcally, results in Section 6 give

1 (s + 2)2

9 2π2

1 s + 2

3 2π2

+ O(1) as s → −2. It therefore follows that

+

log(2)

W4(s) =

9 2π2

3 2π2

log(2)x + O(x3) as x → 0. ♦

p4(x) = −

xlog(x) +

More generally, W4 has poles of order 2 at −2k for k a positive integer. Deﬁne s4,k and r4,k by

s4,k−1 (s + 2k)2

r4,k−1 s + 2k

(25) W4(s) =

+

+ O(1) as s → −2k. We thus obtain that, as x → 0+,

K−1

x2k+1 (r4,k − s4,k log(x)) + O(x2K+1).

p4(x) =

k=0

In fact, knowing that p4 solves the linear Fuchsian diﬀerential equation (10) with a regular singularity at 0 we may conclude:

- Theorem 6. For small values x > 0,


- (26) p4(x) =

∞

k=0

(r4,k − s4,k log(x)) x2k+1.

Note that

s4,k =

3 2π2

W4(2k) 82k

as the two sequences satisfy the same recurrence and initial conditions. The numbers W4(2k) are also known as the Domb numbers ([BBBG08]), and their generating function in hypergeometric form is given in [Rog09] and has been further studied in [CZ10]. We thus have

- (27)

∞

k=0

s4,k x2k+1 =

6x π2 (4 − x2) 3

F2

1

3, 21, 23 1,1

108x2 (x2 − 4)3 which is readily veriﬁed to be an analytic solution to the diﬀerential equation satisﬁed by p4. Remark 4. For future use, we note that (27) can also be written as

- (28)

∞

k=0

s4,k x2k+1 =

24x π2 (16 − x2) 3

F2

1

3, 21, 23 1,1

108x4 (16 − x2)3 which follows from the transformation

- (29) (1 − 4x)3F2

1

3, 12, 23 1,1 −

108x (1 − 16x)3

= (1 − 16x)3F2

1

3, 12, 23 1,1

108x2 (1 − 4x)3

given in [CZ10, (3.1)]. ♦

On the other hand, as a consequence of (25) and the functional equation (9) satisﬁed by W4, the residues r4,k can be obtained from the recurrence relation

128k3r4,k = 4(2k − 1)(5k2 − 5k + 2)r4,k−1 − 2(k − 1)3r4,k−2

- (30) + 3 64k2s4,k − (20k2 − 20k + 6)s4,k−1 + (k − 1)2s4,k−2


with r4,−1 = 0 and r4,0 = 2π9

log(2).

2

- Remark 5. In fact, before realizing the connection between the Mellin transform


and the behaviour of p4 at 0, we empirically found that p4 on (0,2) should be of the form r(x) − s(x)log(x) where a and r are odd and analytic. We then numerically

determined the coeﬃcients and observed the relation with the residues of W4 as given in Theorem 6. ♦

The diﬀerential equation for p4 has a regular singularity at 0. A basis of solutions at 0 can therefore be obtained via the Frobenius method, see for instance [Inc26]. Since the indicial equation has 1 as a triple root, the solution (27) is the unique analytic solution at 0 while the other solutions have a logarithmic or double logarithmic singularity. The solution with a logarithmic singularity at 0 is explicitly given in (34), and, from (26), it is clear that p4 on (0,2) is a linear combination of the analytic and the logarithmic solution.

Moreover, the diﬀerential equation for p4 is a symmetric square. In other words, it can be reduced to a second order diﬀerential equation, which after a quadratic substitution, has 4 regular singularities and is thus of Heun type. In fact, a hypergeometric representation of p4 with rational argument is possible.

## Theorem 7. For 2 < x < 4,

- (31) p4(x) =

2 π2

√16 − x2 x 3

F2

- 1

- 2, 12, 21


- 5

- 6, 76


(16 − x2)3 108x4

.

Proof. Denote the right-hand side of (31) by q4(x) and observe that the hypergeometric series converges for 2 < x < 4. It is routine to verify that q4 is a solution of the diﬀerential equation A4 · y(x) = 0 given in (10) which is also satisﬁed by p4 as proven in Theorem 2. Together with the boundary conditions supplied by Theorem 5 it follows that p4 = q4.

We note that Theorem 7 gives 2√16 − x2/(π2x) as an approximation to p4(x) near x = 4, which is much more accurate than the elementary estimates established in Theorem 5.

Corollary 1. In particular,

- (32) p4(2) =

27/3π 3√3

Γ

2 3

−6

=

√3 π

W3(−1). Quite marvelously, as ﬁrst discovered numerically:

Theorem 8. For 0 < x < 4,

- (33) p4(x) =


√16 − x2 x

2 π2

Re3F2

- 1

- 2, 12, 21


- 5

- 6, 76


(16 − x2)3 108x4

.

### Proof. To obtain the analytic continuation of the 3F2 for 0 < x < 2 we employ the formula [Luk69, 5.3], valid for all z,

q+1

Γ(ak) j =k Γ(aj − ak) j Γ(bj − ak)

Γ(bj) j Γ(aj)

- a1,...,aq+1
- b1,...,bq


z = j

(−z)−a

q+1Fq

k

k=1

ak,{ak − bj + 1}j {ak − aj + 1}j =k

1 z

× q+1Fq

,

which requires the aj to not diﬀer by integers. Therefore we apply it to

3F2

- 1

- 2 + ε, 12, 12 − ε


- 5

- 6, 76


z .

and take the limit as ε → 0. This ultimately produces, for z > 1,

- 1

- 2, 12, 12


3, 12, 23 1,1

1

log(108z) 2√3z 3

1 z

- (34)

+

- 1

- 2√3z


∞

n=0

(13)n(12)n(23)n n!3

1 z

n

(5Hn − 2H2n − 3H3n).

Here Hn = nk=1 1/k is the n-th harmonic number. Now, insert the appropriate argument for z and the factors so the left-hand side corresponds to the claimed

closed form. Observing that

1 3 n

- 1

- 2 n


- 2

- 3 n =


(2n)!(3n)! 108n(n!)2

,

we thus ﬁnd that the right-hand side of (33) is given by −log(x)S4(x) plus

6 π2

∞

n=0

(2n)!(3n)! (n!)5

x4n+1 (16 − x2)3n

5Hn − 2H2n − 3H3n + 3log(16 − x2)

where S4 is the solution (analytic at 0) to the diﬀerential equation for p4 given in (28). This combination can now be veriﬁed to be a formal and hence actual solution of the diﬀerential equation for p4. Together with the boundary conditions supplied by Theorem 6 this proves the claim.

Remark 6. Let us indicate how the hypergeometric expression for p4 given in Theorem 7 was discovered. Consider the generating series

- (35) y0(z) =


Re3F2

z =

F2

- 5

- 6, 76


∞

W4(2k)zk

k=0

of the Domb numbers which is just a rescaled version of (27). Corresponding to (28), the hypergeometric form for this series given in [Rog09] is

- (36) y0(z) =

1 1 − 4z 3

F2

1

3, 21, 23 1,1

108z2 (1 − 4z)3

which converges for |z| < 1/16. y0 satisﬁes the diﬀerential equation B4 · y0(z) = 0 where

- (37) B4 = 64z2(θ + 1)3 − 2z(2θ + 1)(5θ2 + 5θ + 2) + θ3 and θ = zddz. Up to a change of variables this is (10); y0 is the unique solution which is analytic at zero and takes the value 1 at zero; the other solutions which are not a

multiple of y0 have a single or double logarithmic singularity. Let y1 be the solution characterized by

- (38) y1(z) − y0(z)log(z) ∈ zQ[[z]]. Note that it follows from (38) as well as Theorem 6 together with the initial values s4,0 = 2π3

2

and r4,0 = s4,0 log(8) that p4, for small positive argument, is given by

- (39) p4(x) = −

3x 4π2

y1

x2 64

.

If x ∈ (2,4) and z = x2/64 then the argument t = (1108−4zz2)

3

of the hypergeometric function in (36) takes the values (1,∞). We therefore consider the solutions of the corresponding hypergeometric equation at inﬁnity. A standard basis for these is

t−1/33F2

- 1

3, 13, 13

- 2

- 3, 56


1 t

, t−1/23F2

- 1

- 2, 21, 12


- 5

- 6, 76


1 t

, t−2/33F2

- 2

- 3, 23, 23

- 4


3, 76

1 t

- (40) .

In fact, the second element suﬃces to express p4 on the interval (2,4) as shown in Theorem 7. ♦

We close this section by showing that, remarkably, p4 has modular structure.

Remark 7. As shown in [CZ10] the series y0 deﬁned in (35) possesses the modular parameterization

- (41) y0 −

η(2τ)6η(6τ)6 η(τ)6η(3τ)6

=

η(τ)4η(3τ)4 η(2τ)2η(6τ)2

. Here η is the Dedekind eta function deﬁned as

- (42) η(τ) = q1/24


∞

∞

(−1)nqn(3n+1)/2,

(1 − qn) = q1/24

n=−∞

n=1

where q = e2πiτ. Moreover, the quotient of the logarithmic solution y1 deﬁned in

(38) and y0 is related to the modular parameter τ used in (41) by

- (43) exp

y1(z) y0(z)

= e(2τ+1)πi = −q.

Combining (41), (43) and (39) one obtains the modular representation

- (44) p4 8i

η(2τ)3η(6τ)3 η(τ)3η(3τ)3

=

6(2τ + 1) π

η(τ)η(2τ)η(3τ)η(6τ)

valid when the argument of p4 is small and positive. This is the case for τ = −1/2+iy when y > 0. Remarkably, the argument attains the value 1 at the quadratic irrationality τ = ( −5/3 − 1)/2 (the 5/3rd singular value of the next section). As a consequence, the value p4(1) has a nice evaluation which is given in Theorem 9. ♦

5. The density p5

As shown in [BSW11], W5(s) has simple poles at −2,−4,..., compare Figure 2(b). We write r5,k = Res−2k−2 W5 for the residue of W5 at s = −2k − 2. A surprising bonus is an evaluation of r5,0 = p4(1) ≈ 0.3299338011, the residue at s = −2. This is because in general for n 4, one has

Res−2 Wn+1 = p n+1(0) = pn(1),

as follows from [BSW11, Prop. 1(b)]; here p n+1(0) denotes the derivative from the right at zero.

Explicitly, using Theorem 8, we have,

- (45) r5,0 = p 5(0) =

2√15 π2

Re3F2

- 1

- 2, 21, 12


- 5

- 6, 76


125 4

.

In fact, based on the modularity of p4 discussed in Remark 7 we ﬁnd: Theorem 9.

- (46) r5,0 =


- 1

- 2π2


Γ(151 )Γ(152 )Γ(154 )Γ(158 ) 5Γ(157 )Γ(1115)Γ(1315)Γ(1415)

.

Proof. The value τ = ( −5/3 − 1)/2 in (44) gives the value p4(1) = r5,0. Applying the Chowla–Selberg formula [SC67, BB98] to evaluate the eta functions yields the claimed evaluation.

Using [BZ92, Table 4, (ii)], (46) may be simpliﬁed to

√5 40

Γ(151 )Γ(152 )Γ(154 )Γ(158 ) π4

r5,0 =

- (47)

=

3√5 π3

√5 − 1 2

K152 =

√15 π3

- (48) K5/3K15,

where K15 and K5/3 are the complete elliptic integral at the 15th and 5/3rd singular values [BB98].

Remarkably, these evaluations appear to extend to r5,1 ≈ 0.006616730259, the residue at s = −4. Resemblance to the tiny nome of Bologna [BBBG08] led us to discover — and then check to 400 places using (55) and (56) — that

r5,1 =?

13 1800√5

Γ(151 )Γ(152 )Γ(154 )Γ(158 ) π4 −

1 √5

Γ(157 )Γ(1115)Γ(1315)Γ(1415) π4

- (49) . Using (47) this evaluation can be neatly restated as

r5,1 =?

13 225

r5,0 −

2 5π4

1 r5,0

- (50) . We summarize our knowledge as follows:

Theorem 10. The density p5 is real analytic on (0,5) except at 1 and 3 and satisﬁes the diﬀerential equation A5 · p5(x) = 0 where A5 is the operator

- (51) A5 = x6(θ + 1)4 − x4(35θ4 + 42θ2 + 3)

+ x2(259(θ − 1)4 + 104(θ − 1)2) − (15(θ − 3)(θ − 1))2 and θ = xDx. Moreover, for small x > 0,

- (52) p5(x) =

∞

k=0

r5,k x2k+1

where (15(2k + 2)(2k + 4))2 r5,k+2 = 259(2k + 2)4 + 104(2k + 2)2 r5,k+1

- (53) − 35(2k + 1)4 + 42(2k + 1)2 + 3 r5,k + (2k)4r5,k−1 with explicit initial values r5,−1 = 0 and r5,0, r5,1 given by (47) and (49) above.


Proof. First, the diﬀerential equation (51) is computed as was that for p4, see (10). Next, as detailed in [BSW11, Ex. 3] the residues satisfy the recurrence relation (53) with the given initial values. Finally, proceeding as for (26), we deduce that (52) holds for small x > 0.

Numerically, the series (52) appears to converge for |x| < 3 which is in accordance with 91 being a root of the characteristic polynomial of the recurrence (53); see also

(12). The series (52) is depicted in Figure 3.

0.8

0.6

0.4

0.2

0.5 1.0 1.5 2.0 2.5

Figure 3. The series (52) (dotted) and p5.

Since the poles of W5 are simple, no logarithmic terms are involved in (52) as opposed to (26). In particular, by computing a few more residues from (53),

p5(x) = 0.329934x + 0.00661673x3 + 0.000262333x5 + 0.0000141185x7 + O(x9) near 0 (with each coeﬃcient given to six digits of precision only), explaining the strikingly straight shape of p5(x) on [0,1]. This phenomenon was observed by Pearson [Pea06] who stated that for p5(x)/x between x = 0 and x = 1,

“the graphical construction, however carefully reinvestigated, did not permit of our considering the curve to be anything but a straight line...Even if it is not absolutely true, it exempliﬁes the extraordinary power of such integrals of J products [that is, (5)] to give extremely close approximations to such simple forms as horizontal lines.”

This conjecture was investigated in detail in [Fet63] wherein the nonlinearity was ﬁrst rigorously established. This work and various more recent papers highlight the diﬃculty of computing the underlying Bessel integrals.

Remark 8. Recall from Example 4 that the asymptotic behaviour of pn at zero is determined by the poles of the moments Wn(s). To obtain information about the behaviour of pn(x) as x → n−, we consider the “reversed” densities p˜n(x) = pn(n−x) and their moments W˜n(s). For non-negative integers k,

W˜n(k) =

n

xkp˜n(x)dx =

0

k

n

(n − x)kpn(x)dx =

0

j=0

k j

(−1)jnk−jWn(j)

On the other hand, we can ﬁnd a recurrence satisﬁed by the W˜n(s) as follows: a diﬀerential equation for the densities p˜n(x) is obtained from Theorem 2 by a change of variables. The Mellin transform method as described in Example 1 then provides a recurrence for the moments W˜n(s). We next apply the same reasoning as in [BSW11] to obtain information about the pole structure of W˜n(s). It should be emphasized that this involves knowledge about initial conditions in term of explicit values of initial moments Wn(2k).

For instance, in the case n = 4, we ﬁnd that the moments W˜4(s) have simple poles at −23,−52,−72,... which predicts an expansion of p4(x) as given in Theorem 5.

For n = 5, we learn that W˜5(s) has simple poles at s = −2,−3,−4,.... It then follows, as for (52), that p5(x) = ∞k=0 r˜5,k (x − 5)k+1 for x 5 and close to 5. The r˜5,k are the residues of W˜5(s) at s = −k − 2. ♦

6. Derivative evaluations of Wn

As illustrated by Theorem 6, the residues of Wn(s) are very important for studying the densities pn as they directly translate into behaviour of pn at 0. The residues may be obtained as a linear combination of the values of Wn(s) and W n(s).

Example 5 (Residues of Wn). Using the functional equation for W3(s) and L’Hˆopital’s rule we ﬁnd that the residue at s = −2 can be expressed as

- (54) Res−2(W3) =

8 + 12W 3(0) − 4W 3(2) 9

. This is a general principle and we likewise obtain for instance: Res−2(W5) =

16 + 1140W 5(0) − 804W 5(2) + 64W 5(4) 225

- (55) ,

Res−4(W5) =

26Res−2(W5) − 16 − 20W 5(0) + 4W 5(2) 225

- (56) . In the presence of double poles, as for W4,
- (57) lim

s→−2

(s + 2)2W4(s) =

3 + 4W 4(0) − W 4(2) 8 and for the residue:

- (58) Res−2(W4) =


9 + 18W 4(0) − 3W 4(2) + 4W 4 (0) − W 4 (2) 16

. Equations (57, 58) are used in Example 4 and each unknown is evaluated below. ♦

We are therefore interested in evaluations of the derivatives of Wn for even arguments.

Example 6 (Derivatives of W3 and W4). Diﬀerentiating the double integral for

- W3(s) (7) under the integral sign, we have


1

1

- 1

- 2


log(4sin(πy)cos(2πx) + 3 − 2cos(2πy))dxdy. Then, using

W 3(0) =

0

0

√

1

- 1

- 2


a2 − b2 for a > b > 0, we deduce

log(a + bcos(2πx))dx = log

a +

0

### (59) W 3(0) =

5/6

1 π

log(2sin(πy))dy =

1/6

Cl

π 3

,

where Cl denotes the Clausen function. Knowing as we do that the residue at s = −2 is 2/(√3π), we can thus also obtain from (54) that

3√3 2π

3 π

π 3 −

. In like fashion,

Cl

W 3(2) = 2 +

π

π

3 8π2

log (3 + 2 cosx + 2 cosy + 2 cos(x − y)) dxdy

W 4(0) =

0

0

7 2

ζ(3) π2

### (60) . The ﬁnal equality will be shown in Example 8. Note that we may also write

=

1 8π2

W 3(0) =

2π

0

2π

log(3 + 2cosx + 2cosy + 2cos(x − y))dxdy.

0

The similarity between W 3(0) and W 4(0) is not coincidental, but comes from applying

1

log (a + cos2πx)2 + (b + sin2πx)2 dx =

0

log(a2 + b2) if a2 + b2 > 1, 0 otherwise

to the triple integral of W 4(0). As this reduction breaks the symmetry, we cannot apply it to W 5(0) to get a similar integral. ♦

In general, diﬀerentiating the Bessel integral expression

Γ(1 + 2s) Γ(k − 2s)

### (61) Wn(s) = 2s+1−k

∞

1 x

x2k−s−1 −

0

d dx

k

J0n(x)dx,

obtained by David Broadhurst [Bro09] and discussed in [BSW11], under the integral sign gives

∞

2 x − γ J0n−1(x)J1(x)dx

W n(0) = n

log

0

∞

### (62) log(x)J0n−1(x)J1(x)dx, where γ is the Euler-Mascheroni constant, and

= log(2) − γ − n

0

2

∞

2 x − γ

J0n−1(x)J1(x)dx. Likewise

log

W n(0) = n

0

∞

log(x)J0n(x)dx, and

W n(−1) = (log(2) − γ)Wn(−1) −

0

∞

n x

J0n−1(x)J1(x)(1 − γ − log(2x)) dx.

W n(1) =

0

Remark 9. We may therefore obtain many identities by comparing the above equations to known values. For instance,

∞

1 π

π 3

log(x)J02(x)J1(x)dx = log(2) − γ −

3

Cl

.

♦ Example 7 (Derivatives of W5). In the case n = 5,

0

∞

2 t − γ J04(t)J1(t)dt ≈ 0.54441256

W 5(0) = 5

log

0

with similar but more elaborate formulae for W 5(2) and W 5(4). Observe that in general we also have

∞

1

dx x −

dx x

(J0n(x) − 1)

J0n(x)

### (63) W n(0) = log(2) − γ −

, which is useful numerically. ♦

0

1

In fact, the hypergeometric representation of W3 and W4 ﬁrst obtained in [Cra09] and recalled below also makes derivation of the derivatives of W3 and W4 possible. Corollary 2 (Hypergeometric forms). For s not an odd integer, we have

### (64)

1 22s+1

W3(s) =

tan

πs 2

s

s−1 2

- 2
- 3F2


- 1

- 2, 21, 12


s+3

2 , s+32

1 4

+

- 2
- 3F2 −2s,−2s,−2s 1,−s−21


s

s

1 4

,

and, if also Res > −2, we have

- (65)

Example 8 (Evaluation of W 3(0) and W 4(0)). If we write (64) or (65) as Wn(s) = f1(s)F1(s)+f2(s)F2(s), where F1,F2 are the corresponding hypergeometric functions, then it can be readily veriﬁed that f1(0) = f 2(0) = F 2(0) = 0. Thus, diﬀerentiating (64) by appealing to the product rule we get:

W 3(0) =

1 π3

F2

- 1

- 2, 12, 12

- 3


2, 23

1 4

=

1 π

Cl

π 3

.

The last equality follows from setting θ = π/6 in the identity

2sin(θ)3F2

- 1

- 2, 12, 12

- 3


2, 32

sin2 θ = Cl(2θ) + 2θ log (2sinθ).

Likewise, diﬀerentiating (65) gives

- (66) W 4(0) =

4 π24

F3

- 1

- 2, 12, 21,1

- 3


2, 32, 32

1 =

7ζ(3) 2π2

,

thus verifying (60). In this case the hypergeometric evaluation

4F3

- 1

- 2, 12, 12,1

- 3


2, 32, 32

1 =

∞

n=0

1 (2n + 1)3

=

- 7

- 8


ζ(3),

is elementary. ♦

Diﬀerentiating (64) at s = 2 leads to the evaluation

3F2

- 1

- 2, 12, 12


5

2, 52

1 4

=

27 4

Cl

π 3 −

√3 2

,

while from (65) at s = 2 we obtain

- (67) W 4(2) = 3 +


- 3
- 4F3


- 1

- 2, 21, 12, 2s + 1


- 1

- 2,−2s,−2s,−2s


1 22s

s

s

πs 2

- W4(s) =


1 +

1 .

tan

4F3

s−1 2

s 2

1,1,−s−21

s+3

2 , s+32 , s+32

14ζ(3) − 12 π2

. Thus we have enough information to evaluate (57) (with the answer 3/(2π2)).

Note that with two such starting values, all derivatives of W3(s) or W4(s) at even s may be computed recursively.

We also note here that the same technique yields

∞

2n n

π2 12 −

Hn+1/2 (2n + 1)2

2 π

W 3 (0) =

- (68)

=

π2 12

+

4log(2) π

Cl

π 3 −

4 π

∞

n=0

2n n

42n

n k=0

- 1

- 2k+1


(2n + 1)2

- (69) ,

and, quite remarkably,

W 4 (0) =

π2 12

+

7ζ(3)log(2) π2

+

4 π2

∞

n=0

Hn − 3Hn+1/2 (2n + 1)3

- (70)


42n

n=0

24Li4 12 − 18ζ(4) + 21ζ(3)log(2) − 6ζ(2)log2(2) + log4(2) π2

=

,

where the very ﬁnal evaluation is obtained from results in [BZB08, §5]. Here Li4(1/2) is the polylogarithm of order 4, while Hn := γ + Ψ(n + 1) denotes the nth harmonic number, where Ψ is the digamma function. So for non-negative integers n, we have explicitly Hn = nk=1 1/k, as before, and

n+1

- 1

- 2k − 1 − 2log(2).


Hn+1/2 = 2

k=1

An evaluation of W 3 (0) in terms of polylogarithmic constants is given in [BS11]. In particular, this gives an evaluation of the sum on the right-hand side of (68).

Finally, the corresponding sum for W 4 (2) may be split into a telescoping part and a part involving W 4 (0). Therefore, it can also be written as a linear combination of the constants used in (70). In summary, we have all the pieces to evaluate (58), obtaining the answer 9log(2)/(2π2).

6.1. Relations with Mahler measure. For a (Laurent) polynomial f(x1,...,xn), its logarithmic Mahler measure, see for instance [RVTV04], is deﬁned as

1

1

log f e2πit

### ,...,e2πit

dt1 ···dtn. Recall that the sth moments of an n-step random walk are given by

m(f) =

...

n

1

0

0

s

n

1

1

e2πit

dt1 ···dtn = x1 + ... + xn ss

Wn(s) =

...

k

0

0

k=1

where · p denotes the p-norm over the unit n-torus, and hence W n(0) = m(x1 + ... + xn) = m(1 + x1 + ... + xn−1).

Thus the derivative evaluations in the previous sections are also Mahler measure evaluations. In particular, we rediscovered

1 π

π 3

= L (χ−3,−1) = m(1 + x1 + x2), along with

W 3(0) =

Cl

7ζ(3) 2π2

W 4(0) =

= m(1 + x1 + x2 + x3)

which are both due to C. Smyth [RVTV04, (1.1) and (1.2)] with proofs ﬁrst published in [Boy81, Appendix 1].

With this connection realized, we ﬁnd the following conjectural expressions put forth by Rodriguez-Villegas, mentioned in diﬀerent form in [Fin05],

5/2 ∞

15 4π2

### (71) W 5(0) =?

η3(e−3t)η3(e−5t) + η3(e−t)η3(e−15t) t3 dt and

0

3 ∞

3 π2

### (72) W 6(0) =?

η2(e−t)η2(e−2t)η2(e−3t)η2(e−6t)t4 dt,

0

where η was deﬁned in (42). We have conﬁrmed numerically that the evaluation of W 5(0) in (71) holds to 600 places. Likewise, we have conﬁrmed that (72) holds to 80 places. Details of these somewhat arduous conﬁrmations are given in [BB10].

Diﬀerentiating the series expansion for Wn(s) obtained in [BNSW09] term by term, we obtain

∞

m

(−1)kWn(2k) n2k

- 1

- 2m


m k

### (73) W n(0) = log(n) −

.

m=1

k=0

On the other hand, from [RVTV04] we ﬁnd the strikingly similar

### (74) W n(0) =

∞

m

- 1

- 2


γ 2 −

- 1

- 2m


log(n) −

m=2

k=0

m k

(−1)kWn(2k) k!nk

.

Finally, we note that Wn(s) itself is a special case of zeta Mahler measure as introduced recently in [Aka09].

7. New results on the moments Wn From [BBBG08] equation (23), we have for k > 0 even,

3k+3/2 π 2k Γ(k/2 + 1)2

### (75) W3(k) =

∞

tk+1K0(t)2I0(t)dt,

0

where I0(t),K0(t) denote the modiﬁed Bessel functions of the ﬁrst and second kind, respectively.

Similarly, [BBBG08] equation (55) states that for k > 0 even,

- (76) W4(k) =

4k+2 π2 Γ(k/2 + 1)2

∞

0

tk+1K0(t)3I0(t)dt.

Equation (75) can be formally reduced to a closed form as a 3F2 (for instance by Mathematica). At k = ±1, the closed form agrees with W3(±1). As both sides of (75) satisfy the same recursion ([BBBG08] equation (8)), we see that it in fact holds for all integers k > −2.

In the following we shall use Carlson’s theorem ([Tit39]) which states: Let f be analytic in the right half-plane Rez 0 and of exponential type with the

additional requirement that

|f(z)| Med|z| for some d < π on the imaginary axis Rez = 0. If f(k) = 0 for k = 0,1,2,... then f(z) = 0 identically. We then have the following:

Lemma 1. Equation (75) holds for all k with Rek > −2.

Proof. Both sides of (75) are of exponential type and agree when k = 0,1,2,.... The standard estimate shows that the right-hand side grows like e|y|π/2 on the imaginary axis. Therefore the conditions of Carlson’s theorem are satisﬁed and the identity holds whenever the right-hand side converges.

Using the closed form given by the computer algebra system, we thus have:

Theorem 11 (Single hypergeometric for W3(s)). For s not a negative integer < −1,

- (77) W3(s) =

3s+3/2 2π

Γ(1 + s/2)2 Γ(s + 2) 3

F2

s+2

2 , s+22 , s+22 1, s+32

1 4

.

Turning our attention to negative integers, we have for k 0 an integer:

- (78) W3(−2k − 1) =


4 π3

2kk! (2k)!

2 ∞

t2kK0(t)3dt,

0

because the two sides satisfy the same recursion ([BBBG08, (8)]), and agree when k = 0,1 ([BBBG08, (47) and (48)]).

Remark 10. Equation (78) however does not hold when k is not an integer. Also, combining (78) and (75) for W3(−1), we deduce

∞

∞

∞

π2 2√3

2 √3π

K0(t)2I0(t)dt =

K0(t)3 dt =

J0(t)3 dt.

0

0

0

From (78), we experimentally determined a single hypergeometric for W3(s) at negative odd integers: Lemma 2. For k 0 an integer,

√3 2kk 2 24k+132k 3

- 1

- 2, 12, 12


1 4

W3(−2k − 1) =

.

F2

k + 1,k + 1

Proof. It is easy to check that both sides agree at k = 0,1. Therefore we need only to show that they satisfy the same recursion. The recursion for the left-hand side implies a contiguous relation for the right-hand side, which can be veriﬁed by extracting the summand and applying Gosper’s algorithm ([PWZ06]).

The integral in (78) shows that W3(−2k − 1) decays to 0 rapidly – very roughly like 9−k as k → ∞ – and so is never 0 when k is an integer.

To show that (76) holds for more general k required more work. Using Nicholson’s integral representation in [Wat41],

π/2

2 π

I0(t)K0(t) =

K0(2tsina)da, the integral in (76) simpliﬁes to

0

- (79)

2 π

π/2

0

∞

0

tk+1K0(t)2K0(2tsina)dtda. The inner integral in (79) simpliﬁes in terms of a Meijer G-function; Mathematica is able to produce √π

8sink+2 a

G33,,23 −12,−21, 21

0,0,0

1 sin2 a

,

which transforms to √π 8sink+2 a

G32,,33

- 1,1,1

3

- 2, 32, 21


sin2 a . Let t = sin2 a in the above, so the outer integral in (79) transforms to

- (80)

√π 16

1

0

t−

k+3

2 (1 − t)−

- 1

- 2 G23,,33


- 1,1,1

3

- 2, 23, 12


t dt. We can resolve this integral by applying the Euler-type integral

- (81)


1

t−a(1 − t)a−b−1 Gm,np,q

0

c d

zt dt = Γ(a − b)Gm,np+1+1,q+1

a,c d,b

z .

Indeed, when k = −1, the application of (81) recovers the Meijer G representation of W4(−1) ([BSW11]); that is, (76) holds for k = −1.

When k = 1, the resulting Meijer G-function is

G42,,44

- 2,1,1,1
- 3


2, 32, 21, 32

1 ,

to which we apply Nesterenko’s theorem ([Nes03]), deducing a triple integral (up to a constant factor) for it:

1

1

1

x(1 − x)z y(1 − y)(1 − z)(1 − x(1 − yz))3

dxdydz.

0

0

0

We can reduce the triple integral to a single integral,

8E (t) (1 + t2)K (t) − 2E (t) (1 − t2)2

1

dt.

0

Now applying the change of variable t  → (1 − t)/(1 + t), followed by quadratic transformations for K and E, we ﬁnally get

2√t 1 + t

1

4(1 + t) t2

K(t) − E(t) dt,

E

0

which is, indeed, (a correct constant multiple times) the expression for W4(1) which follows from Section 3.1 in [BSW11].

We ﬁnally observe that both sides of (76) satisfy the same recursion ([BBBG08] equation (9)), hence they agree for k = 0,1,2,.... Carlson’s theorem applies with the same growth on the imaginary axis as in (75) and we have proven the following:

Lemma 3. Equation (76) holds for all k with Rek > −2. Theorem 12 (Alternative Meijer G representation for W4(s)). For all s,

22s+1 π2 Γ(12(s + 2))2

G24,,44

(82) W4(s) =

- 1,1,1, s+32

s+2

- 2 , s+22 , s+22 , 12


1 .

Proof. Apply (81) to (80) for general k, and equality holds by Lemma 3.

Note that Lemma 3 combined with the known formula for W4(−1) in [BSW11] gives

∞

∞

4 π3

K0(t)3I0(t)dt =

J0(t)4 dt.

0

0

Armed with the knowledge of Lemma 3, we may now resolve a very special but central case (corresponding to n = 2) of Conjecture 1 in [BSW11].

## Theorem 13. For integer s,

∞

(83) W4(s) =

j=0

s/2 j

2

W3(s − 2j).

Proof. In [BNSW09] it is shown that both sides satisfy the same three term recurrence, and agree when s is even. Therefore, we only need to show that the identity holds for two consecutive odd values of s.

For s = −1, the right-hand side of (83) is

∞

∞

2

∞

22−2j π3j!2

−1/2 j

t2jK0(t)3 dt

W3(−1 − 2j) =

0

j=0

j=0

upon using (78), and after interchanging summation and integration (which is justiﬁed as all terms are positive), this reduces to

4 π3

∞

K0(t)3I0(t)dt,

0

which is the value for W4(−1) by Lemma 3. We note that the recursion for W4(s) gives the pleasing reﬂection property

W4(−2k − 1)26k = W4(2k − 1).

In particular, W4(−3) = 641 W4(1). Now computing the right-hand side of (83) at s = −3, and interchanging summation and integration as before, we obtain

∞

2

∞

−3/2 j

4 π3

1 64

t2K0(t)3I0(t)dt =

W3(−3 − 2j) =

W4(1) = W4(−3).

0

j=0

Therefore (83) holds when s = −1,−3, and thus holds for all integer s.

Acknowledgments. We are grateful to David Bailey for signiﬁcant numerical assistance, Michael Mossinghoﬀ for pointing us to the Mahler measure conjectures via [RVTV04], and Plamen Djakov and Boris Mityagin for correspondence related to Theorem 4 and the history of their proof. We are specially grateful to Don Zagier for not only providing us with his proof of Theorem 4 but also for his enormous amount of helpful comments and improvements. We also thank the reviewer for helpful suggestions.

The ﬁrst and the last authors thankfully acknowledge support by the Australian Research Council.

## Appendix. A family of combinatorial identities

DON ZAGIER1

The “collateral result” of Djakov and Mityagin, [DM04, DM07], is the pair of identities

−m<i1<···<ik<m i2−i1,...,ik−ik−1 2

1−m<i1<···<ik<m i2−i1,...,ik−ik−1 2

k

(m2 − i2s) = σk(12,32,...,(2m − 1)2),

s=1

k

(m − is)(m + is − 1) = σk(22,42,...,(2m − 2)2),

s=1

where m and k are integers with m k 0 and σk denotes the kth elementary symmetric function. By setting js = is + m in the ﬁrst sum and js = is + m − 1 in the second, we can rewrite these formulas more uniformly as2

σk(12,32,...,(M − 1)2) if M is even, σk(22,42,...,(M − 1)2) if M is odd,

FM,k(M) =

- (84)

where FM,k(X) is the polynomial in X (non-zero only if M 2k 0) deﬁned by

FM,k(X) =

0<j1<···<jk<M j2−j1,...,jk−jk−1 2

k

s=1

- (85) js(X − js) .

The advantage of introducing the free variable X in (85) is that the functions FM,k(X) satisfy the recursion

- (86) FM+1,k+1(X) − FM,k+1(X) = M (X − M)FM−1,k(X),


because the only paths that are counted on the left are those with 0 < j1 < ··· < jk < jk+1 = M.

It is also advantageous to introduce the polynomial generating function ΦM = ΦM(X,u) =

(−1)k FM,k(X)uM−2k ,

0 k M/2

1The original note is unchanged. 2Note that (84) is precisely Theorem 4.

the ﬁrst examples being Φ0 = 1, Φ1 = u, Φ2 = u2 − (X − 1), Φ3 = u3 − (3X − 5)u,

- Φ4 = u4 − (6X − 14)u2 + (3X2 − 12X + 9),
- Φ5 = u5 − (10X − 30)u3 + (15X2 − 80X + 89),
- Φ6 = u6 − (15X − 55)u4 + (45X2 − 300X + 439)u2 − (15X3 − 135X2 + 345X − 225). In terms of this generating function, the recursion (86) becomes


- (87) ΦM+1 = uΦM − M(X − M)ΦM−1 and the identity (84) to be proved can be written succinctly as

ΦM(M,u) =

|λ|<M λ ≡M (mod 2)

- (88) (u − λ) .

Denote by PM(u) the polynomial on the right-hand side of (88). Looking for other pairs (M,X) where ΦM(X,u) has many integer roots, we ﬁnd experimentally that this happens whenever M −X is a non-negative integer, and studying the data more closely we are to conjecture the two formulas

ΦM(M − n,u) =

- 1

- 2n


n

j=0

n j

- (89) PM(u − n + 2j) (M, n 0)

(a generalization of (88)) and

- (90) ΦM+n(M,u) = ΦM(M,u)Φn(−M,u) (M, n 0).

Formula (90) is easy to prove, since it holds for n = 0 trivially and for n = 1 by (87) and since both sides satisfy the recursion yn+1 = uyn+n(M +n)yn−1 for n = 1,2,... by (87). On the other hand, combining (88), (89) and (90) leads to the conjectural formula

Φn(−M,u) =

1 2n

n

j=0

n j

PM+n(u − n + 2j) Pn(u)

= n!

n

j=0

(−1)j

−u−M−1 2

j

u−M−1 2

n − j or, renaming the variables,

1 M!

ΦM(x + y + 1,y − x) =

M

j=0

(−1)j

x j

y M − j

- (91) .


To prove this, we see by (87) that, denoting by GM = GM(x,y) the expression on the right, it suﬃces to prove the recursion (M + 1)GM+1 = (y − x)GM + (M − x −

y − 1)GM−1. This is an easy binomial coeﬃcient identity, but once again it is easier to work with generating functions: the sum

∞

(92) GM(x,y)Tm = (1 − T)x (1 + T)y satisﬁes the diﬀerential equation

G(x,y;T) :=

M=0

∂G ∂T

1 G

x 1 − T or

y 1 + T −

=

∂G ∂T

∂

∂T − x − y G, and this is equivalent to the desired recursion.

= (y − x)G + T

We can now complete the proof of (84). Rewriting (92) in the form

1 M!

X+u−1

X−u−1

ΦM(X,u) = coeﬀTM (1 − T)

2 (1 + T)

2 , we ﬁnd that, for 1 j M,

1 M!

ΦM(M,M + 1 − 2j) = coeﬀTM (1 − T)j−1 (1 + T)M−j = 0

and hence that the polynomial on the left-hand side of (88) is divisible by the polynomial on the right, which completes the proof since both are monic of degree M in u.

References

[Aka09] Hirotaka Akatsuka. Zeta Mahler measures. Journal of Number Theory, 129(11):2713– 2734, 2009. [BB91] J. M. Borwein and P. B. Borwein. A cubic counterpart of Jacobi’s identity and the AGM. Transactions of the American Mathematical Society, 323(2):691–701, 1991. [BB98] Jonathan M. Borwein and Peter B. Borwein. Pi and the AGM: A Study in Analytic Number Theory and Computational Complexity. Wiley, 1998.

[BB10] Jonathan M. Borwein and David H. Bailey. Hand-to-hand combat: Experimental mathematics with multi-thousand-digit integrals. Journal of Computational Science, 2010. In press, available at: http://www.carma.newcastle.edu.au/~jb616/combat.pdf.

[BBBG08] D. H. Bailey, J. M. Borwein, D. J. Broadhurst, and M. L. Glasser. Elliptic integral evaluations of Bessel moments and applications. Phys. A: Math. Theor., 41:5203–5231, 2008.

[BBG94] J.M. Borwein, P.B. Borwein, and F. Garvan. Some cubic modular identities of ramanujan. Trans. Amer. Math. Soc., 343:35–48, 1994.

[BNSW09] Jonathan M. Borwein, Dirk Nuyens, Armin Straub, and James Wan. Random walk integrals. The Ramanujan Journal, 2009. Submitted, available at: http://www.carma. newcastle.edu.au/~jb616/walks.pdf.

[Boy81] David W. Boyd. Speculations concerning the range of Mahler’s measure. Canad. Math. Bull., 24:453–469, 1981. [Bro09] D. J. Broadhurst. Bessel moments, random walks and Calabi-Yau equations. Preprint, 2009. [BS11] Jonathan M. Borwein and Armin Straub. Log-sine evaluations of Mahler measures. J. Aust Math. Soc., 2011. In press, arXiv:1103.3893.

[BSW11] Jonathan M. Borwein, Armin Straub, and James Wan. Three-step and four-step random walk integrals. Experimental Mathematics, 2011. In press, available at: http://www. carma.newcastle.edu.au/~jb616/walks2.pdf.

[BZ92] J. M. Borwein and I. J. Zucker. Fast evaluation of the gamma function for small rational fractions using complete elliptic integrals of the ﬁrst kind. IMA J. Numer. Anal., 12(4):519–526, 1992.

[BZB08] J. M. Borwein, I. J. Zucker, and J. Boersma. The evaluation of character Euler double sums. The Ramanujan Journal, 15(3):377–405, 2008. [Cra09] R. E. Crandall. Analytic representations for circle-jump moments. PSIpress,

2009. Preprint, available at: http://www.perfscipress.com/papers/analyticWn_ psipress.pdf.

[CZ10] H. H. Chan and W. Zudilin. New representations for Ap´ery-like sequences. Mathematika, 56:107–117, 2010. [DM04] Plamen Djakov and Boris Mityagin. Asymptotics of instability zones of Hill operators with a two term potential. C. R. Math. Acad. Sci. Paris, 339(5):351–354, 2004. [DM07] Plamen Djakov and Boris Mityagin. Asymptotics of instability zones of the Hill operator with a two term potential. J. Funct. Anal., 242(1):157–194, 2007. [Fet63] H. E. Fettis. On a conjecture of Karl Pearson. Rider Anniversary Volume, pages 39–54,

1963. [Fin05] S. Finch. Modular forms on SL2(Z). Preprint, 2005. [FS09] P. Flajolet and R. Sedgewick. Analytic Combinatorics. Cambridge University Press,

2009. [H¨r89] L. H¨rmander. The Analysis of Linear Partial Diﬀerential Operators I. Springer, 2nd edition, 1989. [Hug95] Barry D. Hughes. Random Walks and Random Environments, volume 1. Oxford Uni-

versity Press, 1995. [Inc26] Edward L. Ince. Ordinary Diﬀerential Equations. Green and Co., London, 1926. [Klu06] J. C. Kluyver. A local probability problem. Nederl. Acad. Wetensch. Proc., 8:341–350,

1906. [Luk69] Y. L. Luke. The Special Functions and Their Approximations, volume 1. Academic Press, 1969. [ML86] O. P. Misra and Jean L. Lavoine. Transform Analysis of Generalized Functions. Elsevier, Amsterdam, 1986. [Nes03] Y. V. Nesterenko. Integral identities and constructions of approximations to zeta-values. J. Th´eor. Nombres Bordeaux, 15(2):535–550, 2003.

- [Pea05a] K. Pearson. The problem of the random walk. Nature, 72:342, 1905.
- [Pea05b] K. Pearson. The random walk. Nature, 72:294, 1905. [Pea06] K. Pearson. A mathematical theory of random migration. In Drapers Company Research


Memoirs, number 3 in Biometric Series. Cambridge University Press, 1906. [PWZ06] M. Petkovsek, H. Wilf, and D. Zeilberger. A=B. A. K. Peters, 2006.

[Ray05] Lord Rayleigh. The problem of the random walk. Nature, 72:318, 1905. [Rog09] M. D. Rogers. New 5F4 hypergeometric transformations, three-variable Mahler mea-

sures, and formulas for 1/π. Ramanujan Journal, 18(3):327–340, 2009. [RVTV04] F. Rodriguez-Villegas, R. Toledano, and J. D. Vaaler. Estimates for Mahler’s measure of

a linear form. Proceedings of the Edinburgh Mathematical Society, 2(47):473–494, 2004. [SC67] Atle Selberg and S. Chowla. On epstein’s zeta-function. J. Reine Angew. Math., 227:86–

110, 1967. [Tit39] E. Titchmarsh. The Theory of Functions. Oxford University Press, 2nd edition, 1939. [Ver04] H. A. Verrill. Sums of squares of binomial coeﬃcients, with applications to Picard-Fuchs

equations. Preprint, 2004. [Wat41] G. N. Watson. A Treatise on the Theory of Bessel Functions. Cambridge University Press, 2nd edition, 1941.

CARMA, University of Newcastle, Australia E-mail address: jonathan.borwein@newcastle.edu.au

Tulane University, USA E-mail address: astraub@tulane.edu

CARMA, University of Newcastle, Australia E-mail address: james.wan@newcastle.edu.au

CARMA, University of Newcastle, Australia E-mail address: wadim.zudilin@newcastle.edu.au

Max-Planck-Institut fur¨ Mathematik, Bonn, Germany E-mail address: don.zagier@mpim-bonn.mpg.de

