# arXiv:1708.04122v2[math.NT]14Sep2018

## FOURIER OPTIMIZATION AND PRIME GAPS

EMANUEL CARNEIRO, MICAH B. MILINOVICH, AND KANNAN SOUNDARARAJAN

Abstract. We investigate some extremal problems in Fourier analysis and their connection to a problem in prime number theory. In particular, we improve the current bounds for the largest possible gap between consecutive primes assuming the Riemann hypothesis.

1. Introduction

In this paper we study a new set of extremal problems in Fourier analysis, motivated by a problem in prime number theory. These problems (which will be described shortly) are of the kind where one prescribes some constraints for a function and its Fourier transform, and then wants to optimize a certain quantity. When available, a solution to such a problem usually requires two main ingredients: a tool to prove optimality and a tool to construct an extremal function. A classical example in approximation theory is the problem of ﬁnding the best L1(R)-approximation of real-valued functions by bandlimited functions (i.e. functions with compactly supported Fourier transforms). For the two-sided problem (i.e. unrestricted approximation), one usually works with the so called extremal signatures to establish optimality, whereas for the one-sided problem (in which one is interested in majorizing or minorizing a given function) the Poisson summation formula is useful as a tool to prove optimality. For an account of such methods see, for instance, [10, 36, 41] and the references therein. Optimal bandlimited majorants and minorants have several applications to inequalities in analysis and number theory, for instance in connection to the theory of the Riemann zeta-function, e.g. [6, 7, 8, 11]. Slightly diﬀerent extremal problems appear in the work [32], in connection with the question of bounding the least quadratic nonresidue modulo a prime. Another example of a Fourier optimization problem was proposed by Cohn and Elkies [12], in connection to the sphere packing problem. This recently attracted considerable attention with its resolution in dimensions 8 and 24 (see [13, 42]).

As we see below, the Fourier optimization problems considered here are simple enough to be stated in very accessible terms but rather delicate in the sense that the usual tools in the literature to prove optimality and construct extremal functions are not particularly helpful. While we have been unable to determine explicitly the solutions to our optimization problems, we are able to make progress on the existence and uniqueness of extremizers, and to establish good upper and lower bounds for the values of the sharp constants. In addition, we establish a connection between these

Date: September 17, 2018. 2010 Mathematics Subject Classiﬁcation. 41A30, 11M06, 11M26, 11N05. Key words and phrases. Bandlimited functions, Fourier uncertainty, prime gaps, Riemann hypothesis.

1

extremal problems in Fourier analysis and the problem of bounding the largest possible gap between consecutive primes (assuming the Riemann hypothesis).

## 1.1. Fourier optimization problems. For F ∈ L1(R), we let

∞

e−2πixt F(x)dx

F(t) =

−∞

denote the Fourier transform of F. We also let x+ := max{x,0} and 1 ≤ A ≤ ∞ be a given parameter (note that we include the possibility that A = ∞), and we consider the following problems.

## Extremal problem 1: Given 1 ≤ A < ∞, ﬁnd

1 F 1 |F(0)| − A

C(A) := sup

F(t) dt , (1.1)

F∈A F =0

[−1,1]c

where the supremum is taken over the class A of continuous functions F : R → C, with F ∈ L1(R). In the case A = ∞, determine

|F(0)| F 1

C(∞) = sup

, (1.2)

F∈E F =0

where the supremum is over the subclass E ⊂ A of continuous functions F : R → C, with F ∈ L1(R) and supp F ⊂ [−1,1].

## Extremal problem 2: Given 1 ≤ A < ∞, ﬁnd

1 F 1

C+(A) := sup

F(0) − A

F(t) + dt , (1.3)

F∈A+ F =0

[−1,1]c

where the supremum is taken over the class A+ of even and continuous functions F : R → R, with

- F ∈ L1(R). In the case A = ∞, determine


F(0) F 1

C+(∞) = sup

, (1.4)

F∈E+ F =0

where the supremum is over the subclass E+ ⊂ A+ of even and continuous functions F : R → R, with F ∈ L1(R) and F(t) ≤ 0 for |t| ≥ 1.

There has been some previous works in connection to problem (1.2) and its analogue for trigonometric polynomials, see for instance [2, 24, 39]. The current best numerical upper and lower bounds for C(∞), reviewed in (1.5) below, are due to Gorbachev [25, Theorem 3]. We were not able to ﬁnd any mention to the other problems in the literature. If one further imposes the condition that

- F is nonnegative on R, then (1.2) reduces to a folkloric problem for bandlimited functions while (1.4) reduces to the Cohn-Elkies problem [12, Theorem 3.1] in dimension 1. In both cases Poisson summation shows that the required maximum is 1, being attained by any constant multiple of the Fej´er kernel F(x) = sin(πx)/(πx) 2. Classical interpolation formulas of Vaaler [41, Theorem 9] show that these are indeed the unique extremizers for this simpliﬁed version of (1.2), whereas this simpliﬁed version of (1.4) admits other extremizers (see [12, Section 5]).


We restricted the parameter A to the range 1 ≤ A ≤ ∞ because in the range 0 < A < 1 the corresponding problems (1.1) and (1.3) are trivial in the sense that C(A) = C+(A) = ∞. This can be seen by taking Fε(x) = √1ε e−πx

2/ε with ε → 0+. It is also clear that the mappings A  → C(A) and A  → C+(A) are non-increasing for 1 ≤ A ≤ ∞.

The extremal problems presented here are certainly related to the phenomenon of Fourier uncertainty, and works like [17, 18], that discuss L1-uncertainty principles, provide interesting insights. The recent works [3, 23] on the “root-uncertainty principle” for the Fourier transform also consider interesting extremal problems related to the theory of zeta-functions in number ﬁelds. Toward the problems of determining the exact values of the sharp constants C(A) and C+(A) we establish the following results.

- Theorem 1. Let 1 ≤ A ≤ ∞. With respect to problems (1.1) and (1.2), the following propositions hold:


- (a) If A = ∞, then:

- (a.1) There exists an even and real-valued function G ∈ E, with G(0) = 1, that extremizes (1.2).
- (a.2) All the extremizers of (1.2) are of the form F(x) = cG(x), where c ∈ C with c = 0.
- (a.3) The extremal function G veriﬁes the identity

C(∞)

∞

−∞

sgn(G(x))F(x)dx = F(0) for any F ∈ E.

- (a.4) (cf. [25]) The sharp constant C(∞) veriﬁes the inequality 1.08185... ≤ C(∞) ≤ 1.09769.... (1.5)


- (b) If A = 1 then C(1) = 2, but there are no extremizers for (1.1).
- (c) If 1 < A < ∞, then:


- (c.1) There exists an even and real-valued function G ∈ A that extremizes (1.1).
- (c.2) Let c0 = π4 − 11 sinπtπtdt


−1

= 1.07995... and d0 = 1.09769... be the constant on the right-hand side of (1.5). Let λ = λ(A) be the unique solution of

πλ 2 with 0 < λ < 1. Then

πλ 2 −

πλ 2

1 A

1 −

= sin

cos

πAc0 2

πλ(A) 2 ≤ C(A) ≤ min

d0 1 − (A0−.32)

max 2A − 2 A(A − 1) ,

cos

, 2 , (1.6)

where the ﬁrst upper bound on the right-hand side of (1.6) is only available in the range 2.6 ≤ A < ∞.

Remark: The function

cos2πx 1 − 16x2

H(x) =

(1.7)

belongs to the class E and veriﬁes H 1 = 1/c0. We then have H(0)/ H 1 = c0 = 1.07995..., and this yields a slightly inferior lower bound for C(∞) when compared to the one in (1.5) (which is obtained in [25] by means of more complicated numerical examples). Due to its simplicity, this particular function H(x) plays an important role in our work, being used in the proof of the lower bound in (1.6) and in the proof of Theorem 5.

- Theorem 2. Let 1 ≤ A ≤ ∞. With respect to problems (1.3) and (1.4), the following propositions hold:


- (a) If A = ∞, then:

- (a.1) There exists a function G ∈ E+ that extremizes (1.4).
- (a.2) The sharp constant C+(∞) veriﬁes the inequality C(∞) ≤ C+(∞) < 1.2.


- (b) If A = 1 then C+(1) = 2, but there are no extremizers for (1.3).
- (c) If 1 < A < ∞, then:


- (c.1) There exists an even and real-valued function G ∈ A+ that extremizes (1.3).
- (c.2) The sharp constant C+(A) veriﬁes the inequality

C(A) ≤ C+(A) ≤ min

1.2 1 − (0A.222−1)

, 2 , (1.8)

where the ﬁrst upper bound on the right-hand side of (1.8) is only available in the range 1.222 < A < ∞.

- (c.3) In particular, if A = 36/11 a numerical example yields the lower bound


25 21

< C+

36 11

. (1.9)

Remark: Note that for small values of A, the right-hand side of (1.8) gives a better bound than the right-hand side of (1.6), and can be used instead. The reason, as we shall see, is that such bounds come from modifying the test functions in the dual problem for the case A = ∞. In our construction, these modiﬁcations do not necessarily maintain the hierarchy as A approaches 1.

- 1.2. Bounds for prime gaps on RH. Let pn denote the nth prime. Assuming the Riemann hypothesis (RH), a classical result of Cram´er [14] yields the bound


pn+1 − pn

√pn log pn ≤ c, (1.10) where c is a universal constant. Building upon the works of Goldston [21] and of Ramar´e and Saouter [38], the current best form of this bound is due to Dudek [19, Theorem 1.3], who obtained

limsup

n→∞

- (1.10) with constant c = 1. Here we improve this and other bounds in this theory by establishing an interesting connection with the extremal problems presented in the previous section.


Our strategy consists of three main ingredients: (i) the explicit formula, (ii) the Brun-Titchmarsh inequality, and (iii) the derived extremal problems in Fourier analysis. Letting π(x) denote the

number of primes less than or equal to x, we deﬁne the Brun-Titchmarsh constant B in our desired scale by

π(x + √x) − π(x) √x/log x

B := limsup

(1.11) and we observe that

x→∞

36 11

1 ≤ B ≤

. (1.12) The lower bound in (1.12) follows from the prime number theorem π(x) ∼ x/log x as x → ∞ and the upper bound on B follows from the work of Iwaniec [29, Theorem 14].

We prove the following general result.

- Theorem 3. Assume the Riemann hypothesis. Let C+(·) be deﬁned in (1.3) and B be deﬁned in


- (1.11). Then, for any α ≥ 0, we have


π x + c√xlog x − π(x) √x

21 25

(1 + 2α) C+(B)

> α ≤

inf c > 0; liminf

<

(1 + 2α). (1.13)

x→∞

The last inequality comes from (1.9) and (1.12).

The case α = 0 in Theorem 3 yields an aﬃrmative answer for a question posed in [19], on whether one could establish (1.10) with a constant c < 1. Corollary 4. Assume the Riemann hypothesis. Let C+(·) be deﬁned in (1.3) and B be deﬁned in (1.11). Then

pn+1 − pn √pn log pn ≤

21 25

1 C+(B)

<

. (1.14)

limsup

n→∞

We note from (1.12) and Theorem 2 (b) that the limit of this method would yield a constant 12 on the right-hand side of (1.14). On the other hand, under stronger assumptions, namely the Riemann hypothesis and Montgomery’s pair correlation conjecture, it is known that the limit supremum in

- (1.14) is actually zero (see, for instance, [26, 27, 35]). The case α = 1 in Theorem 3 yields the constant


63 25

3 C+(B)

<

c =

on the right-hand side of (1.13). This also sharpens the previous best result, due to Dudek [19], who had obtained this inequality with constant c = 3.

By working with a particular dilation of the bandlimited function (1.7) and an explicit version of the Brun-Titchmarsh inequality due to Montgomery and Vaughan [34], we are able to make all of our error terms eﬀective and, assuming the Riemann hypothesis, prove that

√pn log pn

22 25

pn+1 − pn ≤

for all primes pn > 3. Theorem 5. Assume the Riemann hypothesis. Then, for x ≥ 4, there is always a prime number in the interval [x, x + 2522√xlog x].

This theorem improves a result of Dudek, Greni´e, and Molteni [20, Theorem 1.1], who had

previously reached a similar conclusion with c = 2522 replaced by c = c(x) = 1 + log4x. Crame´r [15] has conjectured that

pn+1 − pn = O(log2 pn), and this problem remains open to this date. It has been veriﬁed by Oliveira e Silva, Herzog, and Pardi [37, Section 2.2] that

pn+1 − pn < log2 pn (1.15)

for all primes 11 ≤ pn ≤ 4 · 1018. Estimate (1.15) plainly implies the conclusion of Theorem 5 for all 4 ≤ x ≤ 4 · 1018. Therefore, in our proof, we assume that x ≥ 4 · 1018.

We now proceed to the proofs of the main results stated in this introduction. This is carried out in Sections 2 – 6. In Section 7 we have a general discussion on some related extremal problems in Fourier analysis, which includes for example the existence of extremizers for the Fourier optimization problem of Cohn and Elkies [12] related to sphere packing. Some of this material may be of independent interest.

2. Existence of extremizers

In this section we discuss the existence of extremizers for the extremal problems (1.1) – (1.4). We prove here parts (a.1), (b), and (c.1) of Theorems 1 and 2. We begin by making some simplifying observations, that will be helpful for the rest of the paper. Note that we may restrict ourselves to the situation when F ∈ L1(R) (otherwise the quotients on right-hand sides of (1.1), (1.3), and (1.4) yield −∞), and we assume this throughout the rest of the paper. In particular, F decays at inﬁnity and F ∞ is attained at some point.

The class A in Theorem 1 includes complex-valued functions, but for our extremal problems we can restrict attention to even, real-valued functions. Indeed, given a non-identically zero F ∈ A, the following steps either increase the quotients on the right-hand sides of (1.1) – (1.2) or leave them unaltered:

- • by translating F over R, we may assume that |F(0)| = F ∞;
- • by dilating F, we may assume that F 1 = 1;
- • by multiplying F by a unimodular complex number, we may assume that F(0) > 0;
- • by replacing F(x) by F(x) + F(x) /2 we may assume that F is real-valued;

- • by replacing F(x) by F(x) + F(−x) /2 we may assume that F is even.


From the deﬁnitions it is clear that C(A) and C+(A) are non-increasing functions of A. The observations above show that in (1.1) – (1.2) we can restrict attention to even, real-valued functions, so that C(A) ≤ C+(A). The Fej´er kernel F(x) = sin(πx)/(πx) 2 reveals that C(∞) ≥ 1. For every

- F ∈ A we have


1

|F(0)| −

F(t) dt ≤ 2 F 1, (2.1)

F(t) dt ≤

[−1,1]c

−1

so that C(1) ≤ 2. A similar argument gives C+(1) ≤ 2. Putting together all of these observations, for 1 ≤ A ≤ ∞, we obtain the chain of inequalities

1 ≤ C(∞) ≤ C(A) ≤ C+(A) ≤ C+(1) ≤ 2.

- 2.1. Proof of Theorem 1 (a.1). This is the case A = ∞ and we are restricted to the class E ⊂ A of continuous functions F : R → C, with F ∈ L1(R) and supp F ⊂ [−1,1]. Let {Fn}n≥1 be an extremizing sequence verifying the conditions above, i.e. a sequence {Fn}n≥1 ⊂ E of even and real-valued functions, with Fn 1 = 1, Fn ∞ = Fn(0) > 0, and

lim

n→∞

Fn(0) = C(∞).

Since C(∞) ≤ 2, it follows that {Fn}n≥1 is a bounded sequence in L2(R). Hence, there exists G ∈ L2(R) such that (after passing to a subsequence, if necessary) Fn G weakly in L2(R). In this case, supp G ⊂ [−1,1] and by Fourier inversion G can be taken continuous. For any y ∈ R, we have

Fn(y) =

1

−1

e2πiyt Fn(t)dt =

∞

−∞

sin2π(x − y) π(x − y)

Fn(x)dx →

∞

−∞

sin2π(x − y) π(x − y)

G(x)dx

=

1

−1

e2πiyt G(t)dt = G(y),

as n → ∞. It follows that G is even, real-valued and G(0) = C(∞). Moreover, by Fatou’s lemma, we have G 1 ≤ 1. Hence G ∈ E, and from the deﬁnition of C(∞) we must have G 1 = 1 which makes G an extremizer. Multiplying this G by the constant factor C(∞)−1 we arrive at the extremizer stated in the theorem (that assumes the value 1 at x = 0).

- 2.2. Proof of Theorem 1 (b). We already observed in (2.1) that C(1) ≤ 2. By taking Fε(x) = √1ε e−πx

2/ε with ε → 0+ we see that C(1) = 2. In order to obtain equality in (2.1) we must have

F(t) = c F 1 for all t ∈ [−1,1], for some constant c ∈ C with |c| = 1. This is not possible, and hence there are no extremizers in this case.

- 2.3. Proof of Theorem 1 (c.1). Here 1 < A < ∞. Suppose F ∈ A is non-identically zero, with


|F(0)| − A [−1,1]

F(t) dt F 1

- 1

- 2 ≤


c

. (2.2) Since

1

F(t) dt ≥ F(0) −

F(t)dt ≥ |F(0)| − 2 F 1 , we may use (2.2) to see that

[−1,1]c

−1

2A − 21 A − 1

|F(0)| ≤

F 1. (2.3) Inserting this estimate into (2.2), we also have

3 2(A − 1)

| F(t)|dt ≤

[−1,1]c

F 1. (2.4)

Let {Fn}n≥1 ⊂ A be an extremizing sequence of even and real-valued functions, with Fn 1 = 1, Fn ∞ = Fn(0) > 0, and Fn ∈ L1(R). Thus

Fn(0) − A

Fn(t) dt = C(A).

lim

n→∞

[−1,1]c

Since C(A) ≥ 1, from our observation in (2.3) we see that {Fn(0)}n≥1 is a bounded sequence, and from (2.4) that Fn 1 n≥1 is also bounded.

- 2.3.1. Step 1. Since Fn ∞ = Fn(0), the sequence {Fn}n≥1 is bounded in L2(R). Passing to a subsequence, if necessary, we may assume that Fn(0) → c, for some constant c ≥ C(A), and that Fn G weakly in L2(R) for some G ∈ L2(R). By Mazur’s lemma [4, Corollary 3.8 and Exercise
- 3.4], there exists a sequence Hk → G strongly in L2(R), with Hk ∈ Conv {Fn}n≥k} (i.e. each Hk is a ﬁnite linear convex combination of functions Fn with n ≥ k). Note that Hk is even and


real-valued, Hk ∞ = Hk(0) → c, Hk 1 ≤ 1, and Hk 1 k≥1 remains bounded. By passing to a further subsequence, we may also assume that Hk → G and Hk → G, pointwise almost everywhere. Hence G is also even and real-valued. Note that {Hk}k≥1 is also an extremizing sequence.

- 2.3.2. Step 2. By Fatou’s lemma G 1 ≤ liminfk→∞ Hk 1 ≤ 1 and G 1 ≤ liminfk→∞ Hk 1 < ∞. By Fourier inversion, we may assume that G is continuous (after eventually modifying it on a set of measure zero), hence G ∈ A. First we claim that G is nonzero. In fact, since {Hk}k≥1 is an extremizing sequence and Hk(0) → c ≥ C(A), from (2.3) we ﬁnd that liminfk→∞ Hk 1 ≥ c1 > 0. From the L2-convergence (applied below just in the interval [−1,1]) and Fatou’s lemma, we have

G(0) − A

[−1,1]c

G(t) dt =

1

−1

G(t)dt −

[−1,1]c

G(t) − G(t) dt − (A − 1)

[−1,1]c

G(t) dt

≥ limsup

k→∞

1

−1

Hk(t)dt −

[−1,1]c

Hk(t) − Hk(t) dt − (A − 1)

[−1,1]c

Hk(t) dt

= limsup

k→∞

Hk(0) − A

[−1,1]c

Hk(t) dt

≥ c1 C(A). This shows that G is nonzero. The same computation above (up to its third line) shows that G is indeed an extremizer, since G 1 ≤ liminfk→∞ Hk 1.

- 2.4. Proof of Theorem 2 (a.1), (b), and (c.1). The proof of part (b) follows along the same lines as the argument in §2.2 (with the same extremizing family). The proofs of parts (a.1) and (c.1) follow the outline of §2.3 and we simply indicate the minor modiﬁcations needed.


In seeking extremizers when 1 < A < ∞, we may assume that F(0) > 0 and that F ∈ L1(R) (recall that here we are already working within the class of even and real-valued functions). Suppose

that F ∈ A+ is non-identically zero, with F(0) − A [−1,1]

F(t) + dt F 1

- 1

- 2 ≤


c

. (2.5) Since

1

F(t)dt ≥ F(0) − 2 F 1 , we may use (2.5) to see that

F(t) + dt ≥ F(0) −

[−1,1]c

−1

2A − 21 A − 1

F(0) ≤

F 1. (2.6) As before, inserting this estimate into (2.5) we obtain

[−1,1]c

3 2(A − 1)

F(t) +dt ≤

F 1. (2.7)

Let {Fn}n≥1 ⊂ A+ be an extremizing sequence with Fn 1 = 1, Fn(0) > 0, and Fn ∈ L1(R). Note that, in principle, we do not necessarily have Fn ∞ = Fn(0). Since C+(A) ≥ 1, from (2.6) we see that {Fn(0)}n≥1 is a bounded sequence, and from (2.7) we see that Fn 1 n≥1 is also bounded.

The rest of the proof follows as in Steps 1 and 2 of §2.3. Note that the corresponding sequence {Hk}k≥1 will be extremizing, due to the general property that (f + g)+ ≤ f+ + g+, and inequality

- (2.6) shows that liminfk→∞ Hk 1 ≥ c1 > 0. For the ﬁnal computation, one uses the identity

G(0) − A

[−1,1]c

G(t) + dt =

1

−1

G(t)dt −

[−1,1]c

− G(t) −dt − (A − 1)

[−1,1]c

G(t) + dt.

For the case A = ∞ (part (a.1)), the required modiﬁcations are similar and we omit the details.

3. Uniqueness of extremizers

In this section we continue the study of the extremal problem (1.2). We prove the uniqueness of a bandlimited extremizer (up to multiplication by a complex scalar) and provide its variational characterization as described in parts (a.2) and (a.3) of Theorem 1.

- 3.1. Proof of Theorem 1 (a.2). Let G ∈ E ⊂ A be an even and real-valued extremizer of (1.2) with G(0) = 1. Let G1 ∈ E be another extremizer of (1.2), with G1(0) = 1. It suﬃces to show that


- G1 = G.


Let F = (G + G1)/2. Then, by the triangle inequality, we have

∞

∞

- 1

- 2


|G(x)| + |G1(x)| dx =

|F(x)|dx ≤

−∞

−∞

and F(0) = 1. To avoid strict inequality in (3.1) we must have |G(x) + G1(x)| = |G(x)| + |G1(x)|

1 C(∞)

, (3.1)

for all x ∈ R. In particular, this shows that G1 : R → C is real-valued and that G(x)G1(x) ≥ 0

for all x ∈ R. Let R = G · G1. Then R is a nonnegative and integrable function with supp R ⊂ [−2,2]. By a classical result of Krein [1, p. 154], we have R(x) = |S(x)|2, for some S ∈ L2(R) with supp S ⊂ [−1,1]. Observe that |S(0)| = 1 and that

∞

∞

∞

1 C(∞)

- 1

- 2


|G(x)| + |G1(x)| dx =

|S(x)|dx =

G(x)G1(x)dx ≤

. (3.2)

−∞

−∞

−∞

In particular S ∈ L1(R). To avoid strict inequality in (3.2) we must have G(x) = G1(x) for all x ∈ R, completing the proof.

- 3.2. Proof of Theorem 1 (a.3). Let G be the unique extremal function of (1.2) with G(0) = 1. Let F ∈ E be a real-valued function with F(0) = 0 and deﬁne, for ε ∈ R,

Φ(ε) :=

∞

−∞

|G(x) + εF(x)|dx =

∞

−∞

(G(x) + εF(x))2 1/2 dx. This is a diﬀerentiable function of the variable ε and, since G is an extremizer, we must have 0 =

∂Φ ∂ε

(0) =

∞

−∞

sgn(G(x))F(x)dx. (3.3)

If F1 ∈ E is a generic real-valued function (not necessarily with F1(0) = 0), by (3.3) we obtain that C(∞)

∞

−∞

sgn(G(x))F1(x)dx = C(∞)

∞

−∞

sgn(G(x)) F1(x) − F1(0)G(x) dx

+ C(∞)

∞

−∞

sgn(G(x))F1(0)G(x)dx

= F1(0).

(3.4)

Finally, if F2 ∈ E is a generic complex-valued function, we may write F2(x) = A(x) − iB(x), where A(x) = (F2(x) + F2(x))/2 and B(x) = i(F2(x) − F2(x))/2 are real-valued functions in E, and use

- (3.4) to arrive at


C(∞)

∞

−∞

sgn(G(x))F2(x)dx = F2(0).

4. Upper and lower bounds

In this section we conclude the proofs of Theorems 1 and 2 by establishing the proposed upper and lower bounds for the sharp constants C(A) and C+(A).

- 4.1. Approximations. For the purpose of ﬁnding the values of the sharp constants C(A) and C+(A) in problems (1.1) – (1.4), without loss of generality we may work with smooth functions. For


instance, let us show that we can simply consider F ∈ Cc∞(R). This observation is useful in some passages later in the paper.

Starting with 0 = F ∈ A (or 0 = F ∈ A+ in the case of (1.3)), we write

|F(0)| − A [−1,1]

F(0) − A [−1,1]

F(t) dt F 1

F(t) + dt F 1

c

c

and J+(F) :=

J(F) :=

.

In either situation we may also assume that F ∈ L1(R) and that J(F) and J+(F) are positive. Let K(x) = sin(πx)/(πx) 2 be the Feje´r kernel and, for λ > 0, deﬁne Kλ(x) = λ−1K(x/λ). By Young’s inequality we have F ∗ Kλ 1 ≤ F 1, and using dominated convergence it follows that limsupλ→0 J(F ∗ Kλ) ≥ J(F) and limsupλ→0 J+(F ∗ Kλ) ≥ J+(F). Hence we may assume that our test function F is bandlimited.

Let η ∈ Cc∞(R) be an even, nonnegative, and radially non-increasing function such that η(0) = 1, supp(η) ⊂ [−1,1], and − 11 η(x)dx = 1. Again, let ηλ(x) = λ−1η(x/λ). If supp( F) ⊂ [−Λ,Λ], then F ∗ ηλ ∈ Cc∞(R) and supp( F ∗ ηλ) ⊂ [−Λ − λ,Λ + λ]. By dominated convergence, we have limλ→0 J(F · ηλ) = J(F) and limλ→0 J+(F · ηλ) = J+(F). This veriﬁes our claim in the cases 1 ≤ A < ∞. In the cases A = ∞ one has to slightly dilate F beforehand in order to apply the procedure above and arrive at a function in the class E ⊂ A for (1.2) and E+ ⊂ A+ for (1.4).

- 4.2. Proof of Theorem 1 (a.4). The bounds 1.08185... ≤ C(∞) ≤ 1.09769... (4.1)


were proved in the very interesting work of Gorbachev [25, Theorem 3], to which we refer the reader for details. These bounds improved upon the work of Andreev, Konyagin, and Popov [2], who had previously obtained

c0 = 1.07995... ≤ C(∞) ≤ 1.17898. (4.2) As already pointed out in the introduction, the lower bound in (4.2) comes from the simple

example

cos(2πx) 1 − 16x2

H(x) =

.

The Fourier transform of H is H(t) = π4 cos(πt/2)χ[−1,1](t), which may be veriﬁed by starting with our expression for H(t) and computing its Fourier transform to recover H. Thus H belongs to the class E, and H(0) is clearly 1. To compute the L1-norm of H we observe that sgn(H(x)) = 2χ[−1

4,41](x)−sgn(cos2πx), and use Plancherel’s theorem and the fact that sgn(cos2πx) has distributional Fourier transform supported outside (−1,1) to get1

∞

∞

∞

4,14](x) − sgn(cos2πx) H(x)dx =

|H(x)|dx =

2χ[−1

4,14](x)H(x)dx

H 1 =

2χ[−1

−∞

−∞

−∞

1

1

2sin(πt/2) πt

π 4

π 4

sinπt πt

=

cos(πt/2) dt =

dt = 1/c0.

−1

−1

This example will be useful later on to generate lower bounds for C(A) in the general case 1 < A < ∞. The lower bound of Gorbachev [25] in (4.1) comes from more complicated numerical examples.

1The function x  → sgn(cos 2πx) is an example of a high pass function, as studied in [33].

The upper bound in (4.1) comes from a dual formulation of the problem. Suppose that ψ ∈ L∞(R) is such that its distributional Fourier transform is identically equal to 1 on the interval (−1,1). Let S(R) denote the Schwartz class. Then, for F ∈ E ∩ S(R) (as discussed in §4.1), we have

∞

∞

1

F(t) ψ(t)dt = |F(0)|, which implies that

|F(x)|dx ≥

F(x)ψ(x)dx =

ψ ∞

−1

−∞

−∞

C(∞) ≤ ψ ∞. With this dual formulation, it suﬃces to exhibit a nice test function ψ.

We now brieﬂy describe the construction of Gorbachev [25, Lemma 9]. To simplify the notation (and align with the terminology of [25] to facilitate the references) we let

sin(2πx) 2πx in what follows. For τ = 29289/100000 = 0.29289 we deﬁne a continuous and piecewise linear function α : [0,1/2] → R by

j(x) =



2x − 1, 0 ≤ x ≤ τ; 2τ − 1 + 2(1 − τ)(x − τ)/ε, τ ≤ x ≤ τ + ε; 1, τ + ε ≤ x ≤ 1/2 − 2ε; 1 − y(x − 1/2 + 2ε)/ε, 1/2 − 2ε ≤ x ≤ 1/2 − ε; 1 − y + y(x − 1/2 + ε)/ε, 1/2 − ε ≤ x ≤ 1/2,



(4.3)

α(x) =



where

τ2 − 2τ + 1/2 1 + y − 2τ

ε =

> 0, (4.4) and, having deﬁned (4.3) and (4.4), y is ﬁnally chosen so that

1/2

(1 − α(x)) j(x)

cos(2πx)dx = 0. One arrives at the values y = 0.43056... and ε = 0.0000053884.... Let d0 =

0

−1

1/2

1 − α(x) j(x)

dx

= 1.09769...

0

and deﬁne 1−periodic even functions a(x) and b(x) by

d0 − a(x) 2j(x) − 1, for x ∈ [0,1/2].

a(x) = d0 α(x) and b(x) =

As observed in [25], with this construction the functions a and b have Fourier series expansions

a(x) =

∞

2an cos(2πnx), b(x) =

n=1

∞

2bn cos(2πnx),

n=2

∞

|an| < ∞, and

n=1

∞

|bn| < ∞.

n=2

(notice that the ﬁrst Fourier coeﬃcients verify a0 = b0 = b1 = 0). A numerical evaluation leads to

a1 = −0.5622..., a2 = 0.0684..., a3 = 0.1005..., and since a 2L

2[−21,21] = 0.7238... and 2a21 = 0.6321..., an application of Plancherel’s theorem gives us that |an| ≤ |a1| for all n. For the function b we adopt a slightly diﬀerent approach to bounding the Fourier coeﬃcients bn (since b L2[−12,21] is very large). A numerical integration yields

1/2

|b(x)|dx = 0.8283...

|bn| ≤

−1/2

for all n ≥ 2. Finally, let φ(x) = 2j(x)(1 + b(x)), and deﬁne ψ(x) = φ(x) + a(x). (4.5)

This is the test function constructed by Gorbachev [25], which veriﬁes ψ ∞ = d0 and has distributional Fourier transform identically equal to 1 on the interval (−1,1). In fact, we have

∞

an δ(t − n) + δ(t + n)

ψ(t) = φ(t) +

n=1

(4.6)

∞

∞

an δ(t − n) + δ(t + n) ,

bn χ[−1,1](t − n) + χ[−1,1](t + n) +

= χ[−1,1](t) +

n=1

n=2

where δ is the Dirac delta distribution. We shall use this construction to generate upper bounds for C(A) in the general case 1 < A < ∞. The observation that φ ∞ = 1 will be relevant later on.

Remark: In an earlier version of this manuscript, without being aware of the references [2] and [25], we had initially arrived at the test function

ψ(x) = 2 a0χ[−1

4,41](x) +

∞

4,41](x − n2) + χ[−1

4,14](x + n2) − a0 sgn(cos(2πx)),

2 an χ[−1

n=1

j

where an = π4 ∞j=n (−1)

(2j+1)2 are the Fourier coeﬃcients in the expansion

∞

(πt/2) sin(πt/2)

= a0 + 2

an cos(nπt)

n=1

for −1 ≤ t < 1. This leads to the bound C(∞) ≤ ψ ∞ = a0 = 1.16624..., which is intermediate between (4.1) and (4.2).

## 4.3. Proof of Theorem 1 (c.2).

- 4.3.1. Lower bounds. As before, let H(x) = (cos2πx)/(1 − 16x2). Take F(x) = H(x/λ) for a suitable parameter λ ∈ (0,1] to be optimized. Then F(0) = 1 and F 1 = λ H 1 = λ/c0 with


c0 = 1.079950.... The ratio to be maximized is

c0 λ

π 4 1≤|t|≤1

πλt 2

c0 λ

πλ 2

1 − Aλ

1 − A 1 − sin

cos

dt =

.

λ

Calculus shows that this is maximized by choosing λ such that 1 −

1 A

πλ 2 −

πλ 2

πλ 2

= sin

cos

. (4.7)

For λ = λ(A) verifying (4.7), this examples demonstrates that

πAc0 2

C(A) ≥

cos

πλ(A) 2

.

Note that as A → 1+, this lower bound goes to πc0/2 and is not very eﬀective. Alternatively, we can then use a dilation of the Fej´er kernel K(x) = (sin(πx)/(πx))2 (note that K(t) = (1 − |t|)+). Again we consider F(x) = K(x/λ) and optimize the dilation parameter λ ∈ (0,1]. The ratio we seek to maximize is

1 λ − A

1 λ

1 λ

1 − Aλ

(1 − |λt|)+ dt =

+ λ − 2 .

1≤|t|≤ λ1

The optimal choice is λ = (A − 1)/A, which leads to the bound C(A) ≥ 2A − 2 A(A − 1).

- 4.3.2. Upper bounds. We already know that C(A) ≤ C(1) = 2. The other upper bound comes from duality considerations. Suppose that ϕ ∈ L∞(R) is such that its distributional Fourier transform is identically equal to 1 on the interval (−1,1) and ϕ(t)−1 ≤ A for all t ∈ R. Then, for F ∈ A∩S(R)


- (as discussed in §4.1), we have


∞

∞

∞

F(t) ϕ(t)dt ≥ |F(0)| − A

|F(x)|dx ≥

F(t) dt.

ϕ ∞

F(x)ϕ(x)dx =

[−1,1]c

−∞

−∞

−∞

This leads to C(A) ≤ ϕ ∞.

Let ψ be deﬁned by (4.5). The idea is to mollify this function (used in the case A = ∞) in order to “bring down the delta functions” in its Fourier transform into the acceptable range ϕ(t)−1 ≤ A for all t ∈ R. First we dilate ψ deﬁned by (4.6) to push the delta functions away from the interval [−1,1], in other words, for γ > 1, we observe that

∞

γan δ(t − γn) + δ(t + γn) .

ψ(t/γ) = φ(t/γ) +

n=1

Let R(t) = χ[−1/2,1/2](t). For λ > 0, we write Rλ(t) = λ−1R(t/λ) and deﬁne ϕ(t) := ψ(·/γ) ∗ Rλ (t)

∞

γan λ

= φ(·/γ) ∗ Rλ (t) +

2,λ2](t − γn) + χ[−λ

χ[−λ

2,λ2](t + γn) .

n=1

(4.8)

Recall that |an| ≤ |a1| < 0.6 for all n ≥ 1. Let c = 0.6, so that all the delta functions in (4.6) have coeﬃcients at most c. Let us assume that A ≥ 2+c (so that our particular choices of λ and γ below

verify 0 < λ ≤ γ). We choose γ − 1 = λ2 (so that the support of the molliﬁed delta functions in

- (4.8) stay away from the interval (−1,1)) and cγλ = A − 2 (so that the height of the molliﬁed delta functions in (4.8) is at most A − 2). This leads to the explicit forms


2

1 1 − 2(Ac−2)

λ =

and γ =

.

2 c(A − 2) − 1

From (4.8) we conclude that ϕ(t) = 1 for t ∈ (−1,1) and, since φ ∞ = 1, we also have | ϕ(t)| ≤ A−1 for all t ∈ R, which in particular implies that ϕ(t) − 1 ≤ A for all t ∈ R (note that the molliﬁed

delta functions on the right-hand side of (4.8) have disjoint supports due to the fact that λ ≤ γ). Since ϕ(x) = γ ψ(γx) R(x/λ), our upper bound is then ϕ ∞ = γ ψ ∞ = γ d0.

- 4.4. Proof of Theorem 2 (a.2). We proceed again via duality considerations. Suppose that Ψ ∈ L∞(R) is a real-valued function such that its distributional Fourier transform is identically equal to 1 on the interval (−1,1) and Ψ(t) − 1 ≤ 0 for all t ∈ R. Then, for F ∈ E+ ∩ S(R) (as discussed in §4.1), we have

Ψ ∞

∞

−∞

|F(x)|dx ≥

∞

−∞

F(x)Ψ(x)dx =

∞

−∞

F(t) Ψ(t)dt ≥ F(0), which implies that

C+(∞) ≤ Ψ ∞. Experimentation gave the following numerical example. Let a = 0.018, b = 0.027, and c = 0.002, and consider

Ψ(x) =

sin(2πx) πx

+

2sin(aπx) πx

cos(3πx) +

2sin(bπx) πx

cos(4πx) +

2sin(cπx) πx

cos(10πx) − 0.888cos(2πx) − 0.01cos(6πx),

(4.9)

which has Fourier transform Ψ(t) = χ[−1,1](t) + χ[−a/2,a/2](t − 23) + χ[−a/2,a/2](t + 32)

- + χ[−b/2,b/2](t − 2) + χ[−b/2,b/2](t + 2)
- + χ[−c/2,c/2](t − 5) + χ[−c/2,c/2](t + 5) − 0.444(δ(t + 1) + δ(t − 1)) − 0.005(δ(t + 3) + δ(t − 3)).


(4.10)

For this test function we have Ψ ∞ < 1.2.

- 4.5. Proof of Theorem 2 (c.2). We have already seen that C+(A) ≤ C+(1) = 2. The other upper bound comes from the following dual formulation. Suppose that Φ ∈ L∞(R) is a real-valued function such that its distributional Fourier transform is identically equal to 1 on the interval (−1,1) and −A ≤ Φ(t) − 1 ≤ 0 for all t ∈ R. Then, for F ∈ A+ ∩ S(R) (as discussed in §4.1), we have


∞

∞

∞

|F(x)|dx ≥

F(t) Φ(t)dt ≥ F(0) − A

F(x)Φ(x)dx =

Φ ∞

F(t) + dt,

[−1,1]c

−∞

−∞

−∞

1.0

0.5

-3 -2 -1 1 2 3

- -1.0

- -0.5


1.200

1.195

1.190

1.185

-0.4 -0.2 0.0 0.2 0.4

Figure 1. Graph of the function Ψ in (4.9) in two diﬀerent scales.

which leads to

C+(A) ≤ Φ ∞. The idea is to mollify the test function in (4.9) to bring down the delta functions to the required range, as done in §4.3.2. Let c = 0.444 be the largest coeﬃcient of a delta function in (4.10) and assume a priori that A > 1 + 2c (so that our choice of λ below is in fact positive). With the same notation as in (4.8) we choose γ − 1 = λ2 and cγλ = A − 1. Note that the four delta functions in (4.10) have negative coeﬃcients, while the rest of the Fourier transform lies between 0 and 1, so we may take A − 1 here instead of A − 2. Moreover, since these delta functions are supported in non-consecutive integers, the condition γ − 1 = λ2 already guarantees that the molliﬁed delta functions will not overlap (hence we do not need to assume here that λ ≤ γ). This yields

1 1 − 2(Ac−1)

2

and γ =

.

λ =

2 c(A − 1) − 1

Since Φ(x) = γ Ψ(γx) R(x/λ), our upper bound is Φ ∞ ≤ γ Ψ ∞ < γ × 1.2.

- 4.6. Proof of Theorem 2 (c.3). For the speciﬁc value of A = 3611, the lower bound described in


(1.8) and (1.6) yields C+(3611) ≥ 1.1569.... We found a better example through experimentation. The function

2

2

2

2

2

F(x) = −4.8x2e−3.3x

+ 1.5x2e−7.4x

+ 520x24e−9.7x

+ 1.3e−2.8x

+ 0.18e−2x

(4.11) gives

F(0) − A [−1,1]

F(t) + dt F 1

25 21

c

. We have found more complicated examples that do slightly better.

= 1.1943... >

1.5

1.0

0.5

-2 -1 1 2

1.0

0.8

0.6

0.4

0.2

-2 -1 1 2

Figure 2. Graph of the function F in (4.11) on the left, and graph of F on the right.

5. Prime gaps — asymptotic version

In this section we prove Theorem 3. The proof uses two main tools: the explicit formula connecting the prime numbers and the zeros of the Riemann zeta-function, and the Brun-Titchmarsh inequality as expressed in (1.11) and (1.12).

- Lemma 6 (Guinand-Weil explicit formula). Let h(s) be analytic in the strip |Ims| ≤ 12 +ε for some ε > 0, and assume that |h(s)| (1 + |s|)−(1+δ) for some δ > 0 when |Res| → ∞. Then


∞

ρ − 21 i

- 1

- 2i


- 1

- 2i −


- 1

- 2π


- 1

- 2π


Γ Γ

1 4

iu 2

+ h −

h

= h

h(0)log π +

h(u)Re

+

du

−∞

ρ

+ h −log n 2π

- 1

- 2π n≥2


Λ(n) √n

log n 2π

−

h

,

where ρ = β + iγ are the non-trivial zeros of ζ(s), Γ /Γ is the logarithmic derivative of the Gamma function, and Λ(n) is the Von-Mangoldt function deﬁned to be log p if n = pm with p a prime number and m ≥ 1 an integer, and zero otherwise.

Proof. The proof follows from [30, Theorem 5.12].

- 5.1. Set-up. Motivated by the discussion in §4.1, throughout this section we ﬁx F : R → R to be an even and bandlimited Schwartz function, with F(0) > 0. Let us assume that supp( F) ⊂ [−N,N] for some parameter N ≥ 1. It then follows that F extends to an entire function (which we continue calling F) and the fact that x2F(x) ∈ L∞(R) implies, via the Phragme´n-Lindel¨f principle, that |F(s)| (1 + |s|)−2 when |Res| → ∞. We may therefore apply the explicit formula (Lemma 6).


Our idea to approach this problem can be summarized as follows. We use the explicit formula above to measure the size of an interval that does not contain too many primes. Note that the information about the primes is on the right-hand side of the formula, while on the left-hand side we have information on the zeros of ζ(s). We modify our test function F in such a way that F emphasizes the information on said interval, translating and rescaling F to concentrate the mass of F on this interval. We then try to understand the eﬀect of this localization in all the terms of the

formula through an asymptotic analysis. Since the function F must be small near its endpoints, it is advantageous to use the Brun-Titchmarsh inequality to (over) estimate the contribution from the primes on the edges of the interval.

Let 0 < ∆ ≤ 1 and 1 < a be free parameters to be chosen later. We anticipate that we will be choosing ∆ → 0+ and a → ∞, so it is not harmful to further assume that

2π∆N ≤ log a. (5.1)

Deﬁne f(z) := ∆F(∆z) and note that supp( f) ⊂ [−∆N,∆N]. Assuming RH, an application of the explicit formula (Lemma 6) to the entire function h(z) = f(z)aiz yields the following inequality:

- 1

- 2i


- 1

- 2i


- 1

- 2π


log a 2π

a−1/2 ≤

a1/2 + f −

|f(γ)| +

f −

log π

f

γ

∞

- 1

- 2π


Γ Γ

iu 2

1 4

f(u)aiu Re

+

+

du

(5.2)

−∞

Λ(n) √n

log(n/a) 2π +

log na 2π +

1 2π n≥2

+ f −

f

.

+

- 5.2. Proof of Theorem 3. The idea is to proceed with an asymptotic evaluation of both sides of (5.2). We start with its left-hand side. Note that


N

- 1

- 2i


∆ 2i

f

= ∆F

= ∆

−N

N

= ∆

F(t)dt + ∆

−N

= ∆F(0) + O(∆2). Therefore, the left-hand side of (5.2) equals

eπt∆ F(t)dt

N

−N

eπt∆ − 1 F(t)dt

f

- 1

- 2i


- 1

- 2i


a1/2 + f −

a−1/2 = ∆F(0) a1/2 + a−1/2 + O(∆2a1/2).

For the right-hand side of (5.2), we ﬁrst consider the error terms. From (5.1) we have

log a 2π

- 1

- 2π


f −

- 1

- 2π


log a 2π∆

F −

log π =

log π = 0.

Also, using Stirling’s formula ΓΓ (s) = log s + O(|s|−1) and (5.1), we get

∞

∞

Γ Γ

1 4

iu 2

1 4

log a

f(u)aiu Re

2π∆) log

F(y)e2πiy(

+

du =

+

−∞

−∞

∞

2π∆) 1 2

1 4∆

log a

log(∆2 + 4y2) + log

F(y)e2πiy(

=

−∞

1 4∆

log a 2π∆

F −

= log

+ O(1) = O(1).

iy 2∆

dy + O(1)

dy + O(1)

Thus, we have deduced that

∆F(0) a1/2 + a−1/2 ≤

- 1

- 2π n≥2


Λ(n) √n

|f(γ)| +

γ

+ O(∆2a1/2) + O(1).

f

log(n/a) 2π +

log na 2π +

+ f −

It remains to estimate the two remaining sums on right-hand side of this inequality.

(5.3)

- 5.2.1. The sum over zeros. Let N(x) denote the number of zeros ρ = β +iγ of ζ(s) with 0 < γ ≤ x.


Using the fact that N(x) = 2xπ log 2xπ−2xπ+O(log x), we evaluate the sum γ |f(γ)| using summation by parts to get

∞

|f(x)| log+ |x| 2π

- 1

- 2π


dx + O f ∞ + f (x) log+|x| 1 ,

|f(γ)| =

−∞

γ

where log+x = max{log x,0} for x > 0. Recalling that f(x) = ∆F(∆x), this yields

∞

- 1

- 2π


|F(y)| log+|y/2π∆|dy + O(1)

|f(γ)| =

−∞

γ

(5.4)

log(1/2π∆) 2π

F 1 + O(1).

=

- 5.2.2. The sum over primes and the choice of parameters. Fix α ≥ 0 and assume that c is a ﬁxed positive constant such that


π x + c√xlog x − π(x)

√x ≤ α. Then, given ε > 0, there exists a sequence of x → ∞ such that

liminf

x→∞

π x + c√xlog x − π(x)

√x ≤ α + ε (5.5) along this sequence. For each such x, we choose a and ∆ such that

[x,x + c√xlog x] = ae−2π∆,ae2π∆ . (5.6) Then (allowing the implicit constants in the big-O notation here to depend on c) we have

log2 x x

log x √x

log x √x

(5.7) and

= c

+ O

4π∆ = log 1 + c

1/2

= x + O(√xlog x). (5.8)

log x √x

a = x 1 + c

By (5.1), the sum we want to evaluate is

Λ(n) √n

n≥2

f

log(n/a) 2π +

log na 2π +

+ f −

Λ(n) √n

=

F

n≥2

log(n/a) 2π∆ +

. (5.9)

Note that the last sum is supported on n with ae−2π∆N ≤ n ≤ ae2π∆N. The contribution of the

- (at most) (α + ε)√x primes in the interval (x,x + c√xlog x] = (ae−2π∆,ae2π∆] to the sum (5.9) is bounded above by (using the trivial bound ( F(t))+ ≤ F 1)


log p √p ≤ F 1 (α + ε)√x

log x √x

≤ F 1

= F 1 (α + ε) log x.

p∈(a e−2π∆,a e2π∆]

It is not hard to show that the contribution of the prime powers n = pk with k ≥ 2 in the full interval [ae−2π∆N,ae2π∆N] to the sum (5.9) is O(1). It remains to estimate the contribution of the primes in the intervals [ae−2π∆N,ae−2π∆] and [ae2π∆,ae2π∆N], and for this we use the Brun-Titchmarsh inequality. Let B be deﬁned by (1.11) and let B > B. For x suﬃciently large we have

log p √p

log(p/a) 2π∆ + ≤ B

log(t/a) 2π∆ +

dt √t

+ O(1)

F

F

1≤| log(2πt/a∆ ) |≤N

1≤| log(2πp/a∆ ) |≤N

= B √a(2π∆)

F(t) + dt + O(1).

[−1,1]c

The inequality above can be seen by covering the intervals [ae−2π∆N,ae−2π∆] and [ae2π∆,ae2π∆N] by subintervals of size √a, and applying the Brun-Titchmarsh inequality in each summand of the corresponding Riemann-Stieltjes sum associated to this partition (the details of this argument are carried out in §6.2 for a speciﬁc function and can be modiﬁed to handle the general case). Combining estimates, we see that

Λ(n) √n

log(n/a) 2π +

log na 2π +

+ f −

f

n≥2

(5.10)

≤ F 1 (α + ε) log x + B √a(2π∆)

F(t) + dt + O(1).

[−1,1]c

- 5.2.3. Conclusion. Inserting the estimates in (5.4) and (5.10) into (5.3) and then rearranging terms, it follows that


∆√a F(0) − B

log(1/2π∆) 2π

- 1

- 2π


F(t) + dt ≤

F 1 +

F 1 (α + ε) log x + O(1),

[−1,1]c

where we have used (5.7) and (5.8) to combine the error terms. Sending x → ∞ along the sequence

- (5.5), we conclude that


F 1 F(0) − B [−1,1]

c ≤ (1 + 2α + 2ε)

,

F(t) + dt

c

where we naturally assume that the denominator above is positive. Since this holds for all ε > 0 and B > B we ﬁnally arrive at

F 1 F(0) − B [−1,1]

c ≤ (1 + 2α)

. (5.11)

F(t) + dt

c

This is the connection to our extremal problem (1.3) and the discussion in §4.1 leads to the desired conclusion, since we may now optimize (5.11) over such bandlimited F.

6. Prime gaps — explicit version

We now move on to the proof of Theorem 5. Instead of initially following the proof outlined in Section 5 with a particular choice of test function F in the Guinand-Weil explicit formula (and carefully estimating the error terms), we start oﬀ slightly diﬀerently using a Mellin transform approach to the problem. For our ﬁxed choice of test function, this approach simpliﬁes some of our calculations. Moreover, it may be the case that the kernel we are using will be helpful in other applications. For a generic choice of test function, however, the Fourier transform approach to the problem used in the previous section is perhaps more illuminating.

- Lemma 7. Let ϑ and δ be positive numbers satisfying ϑδ = π/2. Then, for a > eδ and ϑ not an ordinate of a zero of ζ(s), we have


ϑ√a

aiγ cos(δγ) ϑ2 − γ2

Λ(n) √n

a n

eδ/2 + e−δ/2 − 2ϑ

cos ϑlog

=

1 4 + ϑ2

γ

ae−δ≤n≤aeδ

(6.1)

∞

ϑa−2n−1/2 (2n+ 12)2 + ϑ2

e(2n+1/2)δ + e−(2n+1/2)δ .

−

n=1

Here the ﬁrst sum on the right-hand side runs over the nontrivial zeros ρ = 1/2 + iγ of ζ(s) where γ ∈ C with |Re(γ)| < 1/2.

Proof. For any c > 0, δ > 0 and ξ > 0 we have

 

1, if e−δ < ξ < eδ, 1/2, if ξ = e±δ, 0, otherwise.

c+i∞

eδs − e−δs s

- 1

- 2πi


ξs

ds =

c−i∞



It then follows, for any c > 1/2, a > 0, δ > 0 (assuming ae±δ  ∈ N), and any real number ϑ, that

c+i∞

eδs − e−δs s

iϑ

- 1

- 2πi


ζ ζ

a n

Λ(n) √n

(s + 12 + iϑ)as+iϑ

−

ds =

.

c−i∞

ae−δ≤n≤aeδ

For details on this calculation we refer to [16, Chapter 17]. Applying this formula at ϑ and −ϑ and then adding, we deduce that

a n

Λ(n) √n

2

cos ϑlog

ae−δ≤n≤aeδ

c+i∞

- 1

- 2πi


ζ ζ

(w + 12)aw

−

=

c−i∞

eδ(w−iϑ)−e−δ(w−iϑ) w − iϑ

+

eδ(w+iϑ)−e−δ(w+iϑ) w + iϑ

dw.

(6.2)

### In the case ϑδ = π/2, after dividing by 2, this formula simpliﬁes to

c+i∞

- 1

- 2πi


ζ ζ

Λ(n) √n

a n

ϑ w2 + ϑ2

eδw + e−δw dw; (6.3)

(w + 21)aw

−

=

cos ϑlog

c−i∞

ae−δ≤n≤aeδ

note the removable singularities of the integrand at w = ±iϑ and that the formula now holds when ae±δ ∈ N, as well. Since a > eδ, we can shift the line of integration left from Re(w) = c to Re(w) = −∞ and, using the calculus of residues, the integral in (6.3) equals

ϑ√a

∞

ϑa−2n−1/2 (2n + 12)2 + ϑ2

aiγ cos(δγ) ϑ2 − γ2 −

eδ/2 + e−δ/2 − 2ϑ

e(2n+1/2)δ + e−(2n+1/2)δ .

1 4 + ϑ2

γ

n=1

Combining estimates, the lemma follows.

Remark 8. Slightly more generally, if ϑδ ≡ π2 (mod π), then we can also evaluate the integral in

- (6.2) in terms of an absolutely convergent sum over the nontrivial zeros of ζ(s) (but not otherwise).


Since ϑδ = π/2, the ﬁrst term on the right-hand side of (6.1) is ϑ√a

4δ√a π

δ (eδ/2+e−δ/2) π2 + δ2 ≥ 2π√a

(eδ/2+e−δ/2) = 2π√a

2δ π2

.

=

1 4 + ϑ2

Our assumptions below imply that eδ/a ≤ 1/√3, so the third term on the right-hand side of (6.1) is bounded in absolute value by

2 ϑ

eδ a

5/2 ∞

n=0

eδ a

2n

2 ϑ

≤

eδ a

5/2 ∞

n=0

1 3

n

3 ϑ

=

eδ a

5/2

.

Hence, taking absolute values in (6.1) and using the previous two estimates, it follows that 4δ√a π ≤

5/2

eδ a

Λ(n) √n

a n

cos(δγ) ϑ2 − γ2

3 ϑ

cos ϑlog

+ 2ϑ

+

. (6.4)

γ

ae−δ≤n≤aeδ

At this point, it is convenient to make a change of variables so that we can retrace our steps from the proof of Theorem 3 in Section 5 using a dilation of the Fourier transform pair

π 4

πt 2

cos(2πx) 1 − 16x2

cos

χ[−1,1](t).

and H(t) =

H(x) =

We set f(x) = ∆F(∆x) where F(x) = H(x/λ) so that F(t) = λ H(λt). Then, letting δ =

2π∆ λ

λ 4∆

and ϑ =

in (6.4) (note that ϑδ = π/2), after a little rearranging it follows that

e2π∆/λ a

∆√a ≤

- 1

- 2π n≥2


Λ(n) √n

log(n/a) 2π∆

3 2

|f(γ)| +

F

+

∆

γ

Note that the sum over n is supported on the interval ae−2π∆/λ,ae2π∆/λ .

5/2

. (6.5)

We assume that there are no primes in the interval [x,x+c√xlog x] for 21 ≤ c ≤ 1, and we choose a and ∆ to satisfy (5.6). In particular, the equalities in (5.7) and (5.8) still hold. As mentioned at the end of the introduction, we may assume that x ≥ 4·1018. Using the fact that log(1+y) ≤ y for y ≥ 0 in (5.7), we note that ∆ ≤ 41π log√xx < 10−8.

- 6.1. Sum over zeros. We now explicitly estimate the sum over the zeros of the zeta function on the right-hand side of (6.5). Lemma 9. Let N(x) denote the number of zeros ρ = β + iγ of ζ(s) with 0 < γ ≤ x. Then


x 2π

x 2πe −

- 7

- 8 ≤ 0.15log x + 3


N(x) −

log

- for x ≥ e. Proof. The result holds for e ≤ x ≤ 10, since N(10) = 0. From [40, Corollary 1] we have


x 2π

x 2πe −

- 7

- 8 ≤ 0.112log x + 0.278log log x + 2.51 +


0.2 x

N(x) −

, (6.6) which holds for all x ≥ e. The estimate

log

0.278log log x ≤ 0.038log x + 0.28 (6.7) holds for all x ≥ e, while

0.2

x ≤ 0.02 (6.8) holds for x ≥ 10. Combining (6.6), (6.7), and (6.8), we arrive at our desired bound for x ≥ 10.

Write

x 2πe

- 7

- 8


x 2π

+ R(x) and let x0 = 9.676... be such that

log

+

N(x) =

x0 2π

x0 2πe

- 7

- 8


= 0. Then, assuming the Riemann hypothesis and using summation by parts and Lemma 9, we have

log

+

∞

∞

- 1

- 2π


x 2π |f(x)|dx −

|f(γ)| =

R(x)|f| (x)dx

log

x0

x0

γ>0

∞

∞

x 2π |f(x)|dx +

- 1

- 2π


(0.15log x + 3)|f (x)|dx

≤

log

x0

x0

∞

∞

- 1

- 2π


y 2π∆ |F(y)|dy + ∆

(0.15log ∆y + 3)|F (y)|dy Therefore

=

log

∆x0

∆x0

∞

∞

- 1

- 2π


- 1

- 2π


log+y |F(y)|dy +

|f(γ)| ≤

|F(y)|dy

log(1/2π∆)

0

0

γ>0

∞

∞

log+ y |F (y)|dy + (0.15)∆log(1/∆)

|F (y)|dy

+ (0.15)∆

0

0

∞

|F (y)|dy.

+ 3∆

0

The same bound holds for the zeros with γ < 0. Since ∆ < 10−8 implies that ∆log(1/∆) ≤ 2×10−7, we conclude that

log(1/2π∆) 2π

1 2π

log+|y|F(y) 1 + (0.15) × 10−8 × log+|y|F (y) 1

|f(γ)| ≤

F 1 +

γ

(6.9)

+ (3 × 10−8 + (0.15) × 2 × 10−7) F 1 <

0.070 2π

log(1/2π∆) 2π

F 1 +

.

- 6.2. Sum over prime powers. We use a version of the Brun-Titchmarsh inequality due to Montgomery and Vaughan [34, Theorem 2] which states that


2y log y

π(x + y) − π(x) <

, (6.10) for all x,y > 1. For us, the relevant range is y ≥

√x, so that (6.10) corresponds to an application of the Brun-Titchmarsh inequality with the bound B ≤ 4. This is slightly worse than Iwaniec’s bound (1.12) but is completely explicit. With A = 4, the lower bound in (1.6) was established in §4.3.1 with a dilation of the function H(x) with dilation parameter λ = λ(4) = 0.892422...., leading to the bound C(4) ≥ 1.141186... = (0.8762...)−1. For the sake of simplicity, we work instead with the dilation parameter λ = 0.9 and note that for F(x) = H(x/λ) we have

F(0) − 4 [−1,1]

F(t) dt F 1

25 22

c

. (6.11) With a and ∆ chosen as in (5.6), we need to estimate the contribution of the primes p such

= 1.1405... >

J(F) =

−1

that 1 < |log2πp/a∆ | ≤ λ−1 to the sum over n in (6.5). We cover the interval (ae2π∆,ae2π∆λ

] ⊂

∪Jj=0−1(xj,xj+1], with x0 = ae2π∆ and xj+1 = xj + √xj. Using (6.10) in each subinterval (xj,xj+1] and the fact that F is decreasing on [0,λ−1] we obtain

4√xj log xj

J−1

log p √p

log(p/a) 2π∆ ≤

log xj √xj

log(xj/a) 2π∆

F

F

j=0

1< log2πp/a∆ ≤λ−1

J−1

log(xj/a) 2π∆

4 √a

√xj−1

≤ 4 F(1) +

F

j=1

xJ

4 √a

log(t/a) 2π∆

≤ 4 F(1) +

dt (6.12)

F

x0

λ−1

= 4 F(1) + 4√a(2π∆)

F(y)e2π∆y dy

1

λ−1

λ−1

= 4 F(1) + 4√a(2π∆)

F(y)dy + 4√a(2π∆)

F(y) e2π∆y − 1 dy

1

1

≤ 4 F(1) + 4√a(2π∆)

λ−1

F(y)dy + 4√a(4π∆)2 F(1)(λ−1 − 1),

1

where we have used the basic estimate ex − 1 ≤ 2x, for x ≤ 1, in the last passage. We treat the other interval in a similar way, covering [ae−2π∆λ

−1

,ae−2π∆) ⊂ ∪jL=0−1[xj+1,xj), with x0 = ae−2π∆ and xj = xj+1 +√xj+1. Using (6.10) in each subinterval [xj+1,xj) and the fact that F is increasing on [−λ−1,0] we obtain

4√xj+1 log xj+1

L−1

log p √p

log(p/a) 2π∆ ≤

log(xj/a) 2π∆

log xj+1 √xj+1

F

F

j=0

−λ−1< log2πp/a∆ ≤−1

L−1

4 a/(e4π∆)

log(xj/a) 2π∆

√xj

≤ 4 F(−1) +

F

j=1

x0

4e2π∆ √a

log(t/a) 2π∆

≤ 4 F(−1) +

F

dt (6.13)

xL

−1

≤ 4 F(−1) + 4√ae2π∆ (2π∆)

F(y)dy

−λ−1

−1

≤ 4 F(−1) + 4√a(2π∆)

F(y)dy + 8√a(2π∆)2 F(−1)(λ−1 − 1).

−λ−1

Combining (6.12) and (6.13) we conclude that

log(p/a) 2π∆

log p √p

F

1<| log2πp/a∆ |≤λ−1

≤ 8 F(1) + 4√a(2π∆)

F(y)dy + 24√a(2π∆)2 F(1)(λ−1 − 1)

(6.14)

[−1,1]c

≤ 0.886 + 4√a(2π∆)

F(y)dy.

[−1,1]c

Here we have used the estimate 8 F(1) ≤ 0.885 along with the inequalities a ≤ 4x and log(1+y) ≤ y

- for y ≥ 0 in (5.7) and (5.8) to see that √a(2π∆)2 ≤ c


2 log√x2 x ≤ 10−7 for c ≤ 1 and x ≥ 4 · 1018 and thus that 24√a(2π∆)2 F(1)(λ−1 − 1) ≤ 0.001.

Since supp( F) ⊂ [−λ−1,λ−1] ⊂ [−2,2] and | F(y)| ≤ πλ/4 < 1, the contribution from the prime powers n = pk with k ≥ 2 to the sum over n in (6.5) is

log(ae−4π∆) 2

log p √n ≤

1

k (e4π∆/k − e−4π∆/k) ,

√

≤

1 + a

ae−4π∆

k≥2 ae−4π∆≤n≤ae4π∆ n=pk

k≥2 k≤log(ae4π∆)/ log 2

where we used a trivial estimate for the total number of kth powers that can lie in the interval [ae−4π∆,ae4π∆]. This is readily bounded by

log(ae−4π∆) 2

√

≤

ae−4π∆

2√a e2π∆ − e−2π∆

log(ae4π∆) log 2

=

log(ae−4π∆)log(ae4π∆) ae−2π∆ log 2

ae2π∆ − ae−2π∆

log(ae−4π∆)log(ae4π∆) ae−2π∆ log 2

2(log a + 1)3 log 2√a

c√xlog x <

=

< 0.001. (6.15)

- 6.3. Finishing the proof. Note that ae−2π∆/λ ≥ x/2 ≥ 2 · 1018 and thus


5/2

e2π∆/λ a

3 2

0.001 2π

≤

∆

.

Combining this estimate with (6.5), (6.9), (6.14), and (6.15), (after multiplying both sides by 2π) we derive that

√a(2π∆) ≤ log

F 1 + 4√a(2π∆)

- 1

- 2π∆


F(y)dy + 0.958.

[−1,1]c

Rearranging and dividing by F 1 = λ H 1 = 0.83337... we obtain (with J(F) deﬁned in (6.11)) J(F)√a(2π∆) ≤ log

- 1

- 2π∆


+ 1.16. (6.16)

2

Since a ≥ x, 1 ≥ c ≥ 12, and log(1 + y) ≥ y − y

2 for y ≥ 0, we derive from (5.7) and (5.8) that √a(2π∆) ≥

c2 log2 x 4√x ≥

c 2

c 2

log x −

log x − 0.001.

Using the inequalities c ≥ 21 and log(1 + y) ≥ y log 2, which holds for 0 ≤ y ≤ 1, it follows that 2π∆ = 21 log 1 + clog√xx ≥ clog2 2 log√xx and therefore

√x log x ≤

2 clog 2

1 2π∆ ≤ log

log

- 1

- 2


log 2 4

1 2

log(4 · 1018) ≤

log x − log

log x − 2.

Inserting these estimates into (6.16), we derive that

cJ(F) 2

1 2

1 2

log x ≤

log x −

.

This is not possible if c = J(1F) < 2225. Hence there must be a prime in the interval [x,x+ 2225√xlog x].

7. Concluding remarks

There are several related extremal problems in Fourier analysis that could be the sources of further investigation. We brieﬂy discuss a few of these here.

- 7.1. Multidimensional analogues. The corresponding versions of the extremal problems (1.1) – (1.4) in Rd arise as natural generalizations. The compact interval [−1,1] ⊂ R could be replaced by any convex, compact, and symmetric set K ⊂ Rd, for instance. Of those, the most basic ones are certainly the cube Q = [−1,1]d and the unit Euclidean ball B = {x ∈ Rd;|x| ≤ 1}. The same ideas used here could be applied to show the existence of extremizers in this general situation. By averaging over the group of symmetries of K, one can show that extremizers admit, without loss of generality, these symmetries. Note that a crucial step in our proof of the uniqueness of extremizers


in Section 3 (for the bandlimited problem (1.2)) was the ability to write a nonnegative function with Fourier transform supported in 2K as the square of a function whose Fourier transform is supported in K. In general, this decomposition is not available for any given K, but in the case of the unit ball B, with respect to radial functions, this statement holds. This was proved, for instance, in [9, 28], exploring the connection with the theory of Hilbert spaces of entire functions of L. de Branges. Hence, in dimension d ≥ 1 and for K = B, one has indeed the uniqueness of radial extremizers (up to multiplication by a complex scalar) for the multidimensional version of (1.2). Letting Cd,K(A) denote the sharp constant in the multidimensional version of (1.1) – (1.2), one can show that Cd,Q(∞) = C(∞)d, and a tensor product of one-dimensional extremizers is an extremizer for the multivariable problem. In the general case, one has Cd,K(∞) ≤ vol(K). A lower bound for Cd,K(∞) may come, for instance, from the solution of the “one-delta problem for K”, which is the same problem as (1.2) with the additional constraint that F ≥ 0. Such problem is also vastly open, having been solved only in a few particular cases such as the cube Q and the ball B (see the discussion in [5, 22, 31]). It would be interesting to have reﬁned upper and lower bounds for all of these extremal problems, as we have here in our Theorems 1 and 2.

7.2. Sphere packing. The following extremal problem in Fourier analysis was proposed by Cohn and Elkies [12] in connection to the sphere packing problem. Find

C = sup

F∈Ed+ F =0

F(0) F(0)

, (7.1)

where the supremum is taken over the class Ed+ of real-valued, continuous, and integrable functions F : Rd → R with F ≥ 0 and F(y) ≤ 0 for |y| ≥ 1. This is the multidimensional analogue of our extremal problem (1.4) with the additional constraint that F ≥ 0. By averaging over the group of rotations SO(d) we may restrict the search to radial functions and by following the outline of §2.3 and §2.4 we obtain the next result.2

Proposition 10. There exists a radial extremizer for (7.1).

As a matter of fact, Cohn and Elkies [12] proposed this optimization problem over the more restrictive class of admissible functions F : Rd → R such that |F| and | F| are bounded above by constant times (1 + |x|)−d−δ for some δ > 0. Standard approximation arguments show that the sharp constant over this restricted class is the same C in (7.1), although extremizers of (7.1), in principle, need not have this particular decay. In addition to dimension d = 1, the value of the sharp constant in (7.1) is known only in dimensions d = 8 and 24 (see [42] and [13], respectively). The extremizers found by Viazovska in [42] and by Cohn, Kumar, Miller, Radchenko, and Viazovska in [13] are indeed radial Schwartz functions.

2This result has been previously communicated by E. Carneiro and Alvaro A. Gomez (with a slightly diﬀerent proof than the one presented here), as part of the M.Sc. thesis of the latter under the supervision of the former.

Acknowledgments

The authors are thankful to Andr´es Chirre for very helpful discussions during the preparation of this work, to Dan Goldston for encouragement, and to Dimitar Dimitrov for bringing references [2, 24, 25, 39] to our attention. E.C. acknowledges support from CNPq-Brazil, FAPERJ-Brazil, and the Fulbright Junior Faculty Award, and is also thankful to Stanford University for the support and warm hospitality. M.B.M. was supported in part by NSA Young Investigator Grants H98230-15-10231 and H98230-16-1-0311, and thanks Stanford University for hosting him on two research visits. K.S. was partially supported by NSF grant DMS 1500237, and a Simons Investigator grant from the Simons Foundation.

References

- [1] N. I. Achieser, Theory of Approximation, New York, 1956.
- [2] N. N. Andreev, S. V. Konyagin, and A. Yu. Popov, Extremum problems for functions with small support, Mathematical Notes, Vol. 60, No. 3, 1996 (translated from Mat. Zametki).
- [3] J. Bourgain, L. Clozel, and J.P. Kahane, Principe d’Heisenberg et fonctions positives. (French) [The Heisenberg principle and positive functions], , Ann. Inst. Fourier (Grenoble) 60 (2010), no. 4, 1215–1232.
- [4] H. Brezis, Functional Analysis, Sobolev Spaces and Partial Diﬀerential Equations, Springer, 2011.
- [5] G. Bianchi and M. Kelly, A Fourier analytic proof of the Blaschke-Santal´o inequality, Proc. Amer. Math. Soc. 143 (2015), no. 11, 4901–4912.
- [6] E. Carneiro, V. Chandee, F. Littmann, and M. B. Milinovich, Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function, J. Reine Angew. Math. 725 (2017), 143–182.
- [7] E. Carneiro, V. Chandee, and M. B. Milinovich, Bounding S(t) and S1(t) on the Riemann hypothesis, Math. Ann. 356 (2013), no. 3, 939–968.
- [8] E. Carneiro and A. Chirre, Bounding Sn(t) on the Riemann hypothesis, Math. Proc. Cambridge Philos. Soc. 164 (2018), no. 2, 259–283.
- [9] E. Carneiro and F. Littmann, Extremal functions in de Branges and Euclidean spaces, Adv. Math. 260 (2014), 281–349.
- [10] E. Carneiro, F. Littmann, and J. D. Vaaler, Gaussian subordination for the Beurling-Selberg extremal problem, Trans. Amer. Math. Soc. 365 (2013), 3493–3534.
- [11] V. Chandee and K. Soundararajan, Bounding |ζ(12 +it)| on the Riemann hypothesis, Bull. London Math. Soc. 43 (2011), no. 2, 243–250.

- [12] H. Cohn and N. Elkies, New upper bounds on sphere packings. I. Ann. of Math. (2) 157 (2003), no. 2, 689–714.
- [13] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska, The sphere packing problem in dimension 24, Ann. Math. 185 (2017), 1017–1033.
- [14] H. Crame´r, Some theorems concerning prime numbers, Ark. Mat. Astron. Fysik. 15 (5) (1920), 1–32.
- [15] H. Crame´r, On the order of magnitude of the diﬀerence between consecutive prime numbers, Acta Arith. 2

(1) (1936) 23–46.

- [16] H. Davenport, Multiplicative number theory, Third edition, Graduate Texts in Mathematics 74, SpringerVerlag, New York (2000).
- [17] D. L. Donoho and B. F. Logan, Signal recovery and the large sieve, SIAM J. Appl. Math. 52 (1992), no. 2, 577–591.
- [18] D. L. Donoho and P. Stark, Uncertainty principles and signal recovery, SIAM J. Appl. Math 49 (1989), 906–931.
- [19] A. Dudek, On the Riemann hypothesis and the diﬀerence between primes, Int. J. Number Theory 11 (2015), no. 3, 771–778.


- [20] A. Dudek, L. Greni´e, and G. Molteni, Primes in explicit short intervals on RH, Int. J. Number Theory 12

(2016), no. 5, 1391–1407.

- [21] D. A. Goldston, On a result of Littlewood concerning prime numbers, Acta Arith. 43 (1) (1983) 49–51.
- [22] F. Gonc¸alves, M. Kelly, and J. Madrid, One-sided band-limited approximations of some radial functions, Bull. Braz. Math. Soc. (N.S.) 46 (2015), no. 4, 563–599.
- [23] F. Gon¸calves, D. Oliveira e Silva, and S. Steinerberger, Hermite polynomials, linear ﬂows on the torus, and an uncertainty principle for roots, J. Math. Anal. Appl. 451 (2017), no. 2, 678–711.
- [24] D. V. Gorbachev, A Sharpening of the Taikov lower bound in the inequality between the C- and L- norms for trigonometric polynomials, Mat. Zametki, 74:1 (2003), 132–134.
- [25] D. V. Gorbachev, An integral problem of Konyagin and the (C,L)-constants of Nikol’skii, Trudy Inst. Mat. i Mekh. UrO RAN, Volume 11, Number 2 (2005), 72–91.
- [26] D. R. Heath-Brown, Gaps between primes, and the pair correlation of zeros of the zeta function, Acta Arith. 41 (1982), no. 1, 85–99.
- [27] D.R. Heath-Brown and D. A. Goldston, A note on the diﬀerences between consecutive primes, Math. Ann. 266 (1984), no. 3, 317–320.
- [28] J. Holt and J. D. Vaaler, The Beurling-Selberg extremal functions for a ball in the Euclidean space, Duke Math. Journal 83 (1996), 203–247.
- [29] H. Iwaniec, On the Brun-Titchmarsh theorem, J. Math. Soc. Japan 34 (1982), no. 1, 95–123.
- [30] H. Iwaniec and E. Kowalski, Analytic Number Theory, American Mathematical Society Colloquium Publications, vol. 53 (2004).
- [31] M. Kelly, Some Inequalities in Fourier Analysis and Applications, Ph.D. dissertation, The University of Texas at Austin, 2013.
- [32] Y. Lamzouri, X. Li, Xiannan, and K. Soundararajan, Conditional bounds for the least quadratic non-residue and related problems. Math. Comp. 84 (2015), no. 295, 2391–2412.
- [33] B. Logan, Properties of high-pass signals, Ph.D. dissertation, Columbia University, New York, 1965.
- [34] H. L. Montgomery and R. C. Vaughan, The large sieve, Mathematika 20 (1973), 119–134.
- [35] J. H. Mueller, On the diﬀerence between consecutive primes, Recent progress in analytic number theory, Vol. 1 (Durham, 1979), pp. 269–273, Academic Press, London-New York, 1981.
- [36] B. Sz.-Nagy, Uber¨ gewisse Extremalfragen bei transformierten trigonometrischen Entwicklungen. II. Nichtperiodischer Fall, Ber. Math.-Phys. Kl. Sachs Akad. Wiss. Leipzig 91 (1939).
- [37] T. Oliveira e Silva, S. Herzog, and S. Pardi, Empirical veriﬁcation of the even Goldbach conjecture and computation of prime gaps up to 4 · 1018, Math. Comp. 83 (288) (2014) 2033–2060.
- [38] O. Ramare´ and Y. Saouter, Short eﬀective intervals containing primes, J. Number Theory 98 (1) (2003) 10–33.
- [39] L. V. Taikov, One scope of extremal problems for trigonometric polynomials, Uspekhi Mat. Nauk 20 (1965), 205–211.
- [40] T. Trudgian, An improved upper bound for the argument of the Riemann zeta-function on the critical line II, J. Number Theory 134 (2014), 280–292.
- [41] J. D. Vaaler, Some extremal functions in Fourier analysis, Bull. Amer. Math. Soc. 12 (1985), 183–215.
- [42] M. Viazovska, The sphere packing problem in dimension 8, Ann. Math. 185 (2017), 991–1015.


IMPA - Instituto Nacional de Matematica´ Pura e Aplicada - Estrada Dona Castorina, 110, Rio de Janeiro, RJ 22460-320, Brazil.

E-mail address: carneiro@impa.br

Department of Mathematics, University of Mississippi, University, MS 38677, USA. E-mail address: mbmilino@olemiss.edu

#### Department of Mathematics, Stanford University, Stanford, CA 94305, USA. E-mail address: ksound@stanford.edu

