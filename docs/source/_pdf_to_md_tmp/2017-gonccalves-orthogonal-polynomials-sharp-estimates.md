arXiv:1702.08510v2[math.CA]24Aug2017

ORTHOGONAL POLYNOMIALS AND SHARP ESTIMATES FOR THE SCHRODINGER¨ EQUATION

FELIPE GONC¸ALVES

Abstract. In this paper we study sharp estimates for the Schro¨dinger operator via the framework of orthogonal polynomials. We use Hermite and Laguerre polynomial expansions to produce sharp Strichartz estimates for even exponents. In particular, for radial initial data in dimension 2, we establish an interesting connection of the Strichartz norm with a combinatorial problem about words with four letters. We use spherical harmonics and Gegenbauer polynomials to prove a sharpened weighted inequality for the Schro¨dinger equation that is maximized by radial functions.

1. Introduction Let 2 ≤ p,q ≤ ∞. The Strichartz estimate for the Schr¨odinger equation (see [19,

- Theorem 2.3]) states that there exists a constant C such that eit∆f(x) Lp(dx) Lq(dt) ≤ C f(x) L2(dx), (1.1)


- for all f ∈ L2(Rd,dx), where ∆ is the Laplacian in Rd and eit∆f(x) denotes


the solution of the Schr¨odinger equation ∂tu(x,t) = i∆u(x,t) with initial data u(x,0) = f(x). The exponents above satisfy the following relation

d p

2 q

d 2

+

=

, (p,q,d) = (∞,2,2).

![image 1](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile1.png>)

![image 2](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile2.png>)

![image 3](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile3.png>)

Since Strichartz’s original work [15] in 1977, the search for maximizers of this spacetime estimate was launched and it is conjectured that a function f(x) maximizes the above inequality if and only if f(x) is a Gaussian.

Conjecture 1. A function f(x) maximizes (1.1) if and only if it has the form Ae−B x

2+u·x, where A,B ∈ C, ReB > 0 and u ∈ Cd.

Remark. We note that Gaussian functions maximize (1.1) if and only if it holds with C = C(p,d) given by

C(p,d) = (p−1/2p21/p−1/4)d. (1.2)

The ﬁrst to prove this conjecture for (p,q,d) ∈ {(6,6,1);(4,4,2)} was Foschi [8] in 2004. In 2005, Hundertmark and Zharnitsky [13] gave an alternative proof for

![image 4](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile4.png>)

Date: September 17, 2018. 2010 Mathematics Subject Classiﬁcation. 42B37, 41A44, 33C45. Key words and phrases. Strichartz estimates, sharp estimates, Schro¨dinger equation, orthogo-

nal polynomials.

1

these two cases. Later on, in 2008, Carneiro [5] and Bennett, Bez, Carbery and Hundertmark [3] gave alternative proofs for these cases, including in addition the new case (p,q,d) = (4,8,1). All these proofs, although shedding new light at the problem via diﬀerent angles, heavily rely on the crucial fact that p = 2k and q = 2kℓ for some integers k ≥ 2 and ℓ ≥ 1. This vital property opens several doors to approach the problem (and we intend to open another one with this article), but the general case for non-even exponents still remains unsolved, although maximizers are known to exist (see [16]).

The main goal of this paper is to demonstrate how orthogonal polynomials can be used to prove sharp space-time estimates related to the Schr¨odinger operator. The novelty of the present work lies in the use of techniques associated with the theory of orthogonal polynomials (in the sense of [18, Chapter 2]) to attack these problems and which ultimately allows us to: (i) Prove a sharpened weighted inequality for the Schr¨odinger operator (Theorem 9 and Corollary 10); (ii) Develop a new way of attacking Conjecture (1) (Theorems 1 and 5); (iii) Produce alternative proofs for the fact that Gaussians maximize the Strichartz estimate (1.1) in the case of even exponents (Theorems 3 and 6 and Corollaries 4 and 7). Moreover, for the case (p,q,d) = (4,4,2) in (1.1), we establish an interesting and unexpected connection with a combinatorial problem about counting words with four letters that dates back to the time of Strichartz’s original work (see Appendix 4).

2. Main Results

The main abstract method underlying all the following results is to break the desired estimate into several simpler pieces, prove a sharp estimate for each piece and then obtain a sharp inequality for the full object. For the trained analyst, this strategy is most likely doomed to failure, but in our particular scenario the pieces are mutually orthogonal (and of ﬁnite dimension in most cases) and this allows us to avoid any loss of sharpness. This will become clear in the next sections.

- 2.1. The Hermite Polynomial Approach. Let {Hm(x)}m≥0 be the Hermite


2/2dx. In the sense of [18, Chapters 2 and 5], these are the orthogonal polynomials associated with the measure dγ(x) and normalized by the condition that each Hm(x) is monic. For a given dimension d and a given vector m ∈ Zd+ (Z+ = {0,1,2,...}) we write

polynomials associated with the normal distribution dγ(x) = (2π)−1/2e−x

(xd), where x = (x1,...,xd) ∈ Rd. We also write

(x1)...Hm

Hm(x) = Hm

1

d

2/2dx, to denote the normal distribution in Rd where x = x21 + ... + x2d.

dγd(x) = (2π)−d/2e− x

![image 5](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile5.png>)

It is known (see [18, Chapter 5]) that the multi-variate Hermite polynomials {Hm(x)} form an orthogonal basis of L2(Rd,dγd(x)) and that

|Hm(x)|2dγd(x) = m! := m1!...md!.

Rd

As a consequence, it can be shown that the functions Φm(x) = Hm(

√

2

4π x)e−π x

![image 6](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile6.png>)

(2.1)

form an orthogonal basis of L2(Rd,dx). Thus, any function f ∈ L2(Rd,dx) can be uniquely written in the following form

α(m)Φm(x).

f(x) =

m∈Zd+

We can now state our ﬁrst main result. In what follows we deﬁne |m| = m1 +m2 +

... + md, for any m = (m1,...,md) ∈ Zd+. Theorem 1. For any given t ∈ R deﬁne the following operator over L2(Rd,dγd)

![image 7](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile7.png>)

Ht : Hm(x)  → e2π|m|itHm( 2/px); x = (x1,...,xd). (2.2)

Let 2 ≤ p,q < ∞ satisfy pd + 2q = d2 and let f ∈ L2(Rd,dx) have the following expansion f(x) = m∈Zd

![image 8](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile8.png>)

![image 9](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile9.png>)

![image 10](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile10.png>)

α(m)Φm(x). Then we have

+

eit∆f(x) Lp(dx) Lq(dt) (p−1/2p21/p−1/2)d

=

![image 11](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile11.png>)

1/2

|HtT−ig(x)|pdγd(x)

−1/2 Rd

q/p

dt

1/q

and

C(p,d) (p−1/2p21/p−1/2)d

![image 12](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile12.png>)

f(x) L2(dx) =

|g(x)|2dγd(x)

Rd

1/2

,

where g(x) = m∈Zd

α(m)Hm(x), C(p,d) is given in (1.2) and T−i is the operator

+

deﬁned in (3.9). Corollary 2. Gaussians maximize the Strichartz estimate (1.1) if and only if

1/2

|Htg(x)|pdγd(x)

−1/2 Rd

q/p

dt

1/q

≤

|g(x)|2dγd(x)

Rd

1/2

, (2.3)

- for all g ∈ L2(Rd,dγd). Remarks.


- (1) Since the operator T−i is isometric and invertible on L2(Rd,dγd), the corollary above easily follows from Theorem 1. The factor e2π|m|it in the deﬁnition of the operator Ht introduces the possibility of using all the machinery from Fourier series to prove Conjecture 1 for all exponents. Unfortunately, the author was not able to achieve any satisfactory result with the mentioned approach for non-even exponents. Nevertheless, we were able to exploit this approach in the known cases of even exponents and to give a new way to understand Conjecture 1.
- (2) Theorem 1 was inspired by Beckner’s approach for the sharp HausdorﬀYoung inequality (see [2]). Roughly speaking, the heart of Beckner’s proof relies on an application of the Central Limit Theorem to approximate the


Hermite semi-group operator Hn  → ωnHn by normalized tensor products of a discrete version of the same operator in the two-point space. This strategy

was generalized by the present author in [10], where we showed that not only the Hermite semi-group can be approximated, but any operator given by a Gaussian kernel can be approximated by tensor products of any operator (not only Beckner’s discrete operator in the two-point space) satisfying the right compatibility conditions. In the eyes of the author, the challenge presented by Conjecture 1, within this framework, is to ﬁnd a special way of discretizing the time variable.

As explained in the introduction, the known cases where the Strichartz inequality (1.1) is maximized by Gaussians are (p,q,d) ∈ {(6,6,1);(4,8,1);(4,4,2)} and they all share the following property: p = 2k and q = 2kℓ, for positive integers k ≥ 2 and ℓ ≥ 1. In these situations, this relation allows us to use Theorem 1 and the orthogonality of Fourier series to transform the problem into an (ℓ2 → ℓ2)–estimate on a suitable space of sequences indexed by certain matrices. In what follows, we deﬁne the required mathematical objects and spaces for any given k ≥ 2 and ℓ ≥ 1 and we explicitly calculate the resulting operators that naturally emerge when one tries to compute the left hand side of inequality (2.3).

α(m)Hm(x) be a function in L2(Rd,dγd). Let I = (−1/2,1/2) and λ = 2/p = 1/k. We have

Let g(x) = m∈Zd

+

![image 13](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile13.png>)

![image 14](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile14.png>)

|Htg(x)|2kdγd(x)

I Rd

k

=

I Rd

j=1

m1,...,mk∈Zd+

=

I (Rd)ℓ S≥0 i,j |mi,j|=S mi,j∈Zd+

=

S≥0 (Rd)ℓ

ℓ

i=1

i,j |mi,j|=S mi,j∈Zd+

ℓ

dt

1|+...+|mk|)it

α(mj)Hmj(λx)e2π(|m

2

dγd(x)

ℓ

dt

k

ℓ

α(mi,j)Hmi,j(λxi)e2πSit

j=1

i=1

2

dγd(x1)...dγd(xℓ)dt

k

α(mi,j)Hmi,j(λxi)

j=1

2

dγd(x1)...dγd(xℓ)

=

∗ ℓ

k

α(mi,j)α(ni,j)

![image 15](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile15.png>)

i=1

j=1

k

ℓ

Hmi,j(λxi)Hni,j(λxi)dγd(x1)...dγd(xℓ), (2.4)

(Rd)ℓ

i=1

j=1

where the summation ∗ is taken over all mi,j,ni,j ∈ Zd+ for i = 1,...,ℓ and j = 1,...,k such that i,j |mi,j| = i,j |ni,j|. The third identity above is due to the orthogonality of Fourier series {e2πiSt}S∈Z. In an analogous way, we also have

ℓ

k

ℓk

|α(mi,j)|2M!, (2.5)

|g(x)|2dγd(x)

=

Rd

i=1

j=1

mi,j∈Zd+

where M! = ℓi=1 kj=1 mi,j! (recall that (m1,...,md)! := m1!...md!).

To be able to clearly analyze the resulting operator that appears in the last line

of (2.4) we need to make some deﬁnitions ﬁrst. Deﬁne M = Mℓ,kd as the space of ℓ × k matrices M = [mi,j] for i = 1,...,ℓ and j = 1,...,k where each entry is a

vector mi,j ∈ Zd+. Next, deﬁne F = Fdℓ,k as the space of functions ϕ : M → C such that

|ϕ(M)|2M! < ∞.

M∈M

The space F is a Hilbert space of sequences indexed by the matrices in M and endowed with the following inner product

ϕ,ψ F =

![image 16](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile16.png>)

ϕ(M)ψ(M)M!. (2.6)

M∈M

We deﬁne an operator P = Pdℓ,k that maps a function ϕ : M → C into a function ψ : M → C by

P(M,N) M!

,

ψ(M) = Pϕ(M) =

ϕ(N)

![image 17](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile17.png>)

(2.7)

N∈M

|N|=|M|

where M = [mi,j] ∈ M and |M| = i,j |mi,j|. The coeﬃcients above are given by

ℓ

k

Hmi,j(λxi)Hni,j(λxi) dγd(x1)...dγd(xℓ) (2.8)

P(M,N) =

(Rd)ℓ

i=1

j=1

for all M = [mi,j] and N = [ni,j]. For each S ≥ 0, let FS denote the closed subspace of functions ϕ : M → C such that ϕ(M) = 0 for any matrix M ∈ M such that |M| = S. Note that dim(FS) < ∞ and P(FS) ⊂ FS. Also, the spaces FS are orthogonal to each other with respect to the inner product (2.6) and

![image 18](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile18.png>)

F =

FS.

S≥0

Our next main result concerns the operator P, its norm over the space F and the its relation with estimate (2.3). Since the coeﬃcients P(M,N) are real, clearly

- P is always symmetric. Depending on the exponents ℓ,k and d, the operator P may be unbounded (hence, not deﬁned in the whole F). It is the goal of our next result to give a full description of these scenarios.


- Theorem 3. Let ℓ ≥ 1, k ≥ 2 and d ≥ 1 be integers and consider the operator P


deﬁned in (2.7) acting on the space F. Then

 

ℓ

|Htg(x)|2kdγd(x)

dt = ϕ,Pϕ F

I Rd

(2.9)

kℓ



Rd |g(x)|2dγd(x)

= ϕ 2F,

if g(x) = m α(m)Hm(x) and if ϕ : M → C is deﬁned by ϕ(M) = i,j α(mi,j) for any M = [mi,j] ∈ M. Let S ≥ 0 be an integer and let PS be the restriction to FS of the operator P (recall that P(FS) ⊂ FS). Then PS2 = PS (hence PS is a projection) if and only if (k − 1)ℓd/2 = 1. In this case, P is well-deﬁned in the

whole F and it is also a projection. In general, if µ := (k − 1)ℓd/2 > 1 we have

Sµ−1 2µ−1Γ(µ)

µ(µ + 1)...(µ + ⌊S/2⌋ − 1) ⌊S/2⌋! ∼

 PS FS→FS =

, S → ∞. In particular, P is not bounded in F for µ > 1.

![image 19](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile19.png>)

![image 20](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile20.png>)

Remark. For k ≥ 2, the only case where 0 < µ < 1 is (k,ℓ,d) = (2,1,1). This is a pathological case that appears due to the presence of probability measures and the possibility of using Jensen’s inequality, and that is why we exclude it from our analysis. Considering the situation p = 2k and q = 2kℓ, where k ≥ 2 and ℓ ≥ 1 are integers, the three cases where Conjecture 1 is known to be true (p,q,d) ∈ {(6,6,1);(4,8,1);(4,4,2)} match exactly with those where µ = (k − 1)ℓd/2 = 1.

Corollary 4. Gaussians maximize the Strichartz inequality (1.1) for (p,q,d) ∈ {(6,6,1);(4,8,1);(4,4,2)}.

- 2.2. The Laguerre Polynomial Approach. For any ν > −1 we denote by


{Ln(ν)(x)}n≥0 the generalized Laguerre polynomials associated with the parameter ν. In the sense of [18, Chapters 2 and 5], these are the orthogonal polynomials associated with the measure e−xxνdx (x > 0) and normalized by the condition

∞

Γ(n + ν + 1) n!

|Ln(ν)(x)|2e−xxνdx =

.

![image 21](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile21.png>)

0

They are also known to form an orthogonal basis in the space L2(R+,e−xxνdx). In analogy with the Hermite polynomials, it can be shown that for a given dimension d the functions

Ψn(x) = Ln(ν)(2π x 2)e−π x

2

, (2.10)

with ν = d/2 − 1 form an orthogonal basis of the space of radial functions in L2(Rd,dx). Thus, any radial function f ∈ L2(Rd,dx) can be uniquely written in the form

f(x) =

α(n)Ψn(x).

n≥0

Our next main result shows an analogue of Theorem 1 but only for radial initial data.

- Theorem 5. Let d be a given dimension and set ν = d/2 − 1. For any given t ∈ R


νe−x

deﬁne the following operator on L2 R+, x

Γ(ν+1)dx Lt : Ln(ν)(x)  → e2πnitLn(ν) p 2 x .

![image 22](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile22.png>)

![image 23](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile23.png>)

Let 2 ≤ p,q < ∞ satisfy pd + 2q = d2 and let f ∈ L2(Rd,dx) be a radial function having the following expansion f(x) = n≥0 α(n)Ψn(x). Then we have

![image 24](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile24.png>)

![image 25](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile25.png>)

![image 26](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile26.png>)

eit∆f(x) Lp(dx) Lq(dt) (p−1/2p21/p−1/2)d

=

![image 27](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile27.png>)

1/2

−1/2

∞

e−xxν Γ(ν + 1)

|Ltg(x)|p

![image 28](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile28.png>)

0

q/p

dt

1/q

(2.11)

and

∞

e−xxν Γ(ν + 1)

C(p,d) (p−1/2p21/p−1/2)d

|g(x)|2

dx

f(x) L2(dx) =

![image 29](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile29.png>)

![image 30](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile30.png>)

0

where g(x) = n≥0 α(n)Ln(ν)(x) and C(p,d) is given in (1.2).

1/2

,

Remark. The above result allows us to explore again the cases where the exponents are even, giving us the opportunity of replicating the results of the Hermite case. However, the resulting operators are not projections any more and the methods used to analyze the Hermite case (see the proof of Theorem 3) do not work. Roughly speaking, the main reason why they do not work is that the Poisson Kernel associated with Laguerre polynomials is given by the Bessel functions Iν(z), which are wild creatures that do not enjoy being handled.

- 2.2.1. The Case (p,q,d) = (4,4,2). We start by calculating the resulting operator that arises from the right hand side term of (2.11). For d = 2 we have ν = d/2−1 =


0 and we write Ln(x) = L(0)n (x) to simplify notation. If g(x) = n≥0 α(n)Ln(x) we deduce that

1/2

∞

|Ltg(x)|4e−xdxdt

−1/2

0

∞

La(x/2)Lb(x/2)Lc(x/2)Ld(x/2)e−xdx

![image 31](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile31.png>)

![image 32](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile32.png>)

=

α(a)α(b)

α(c) α(d)

0

a,b≥0

c,d≥0

c+d=a+b

(2.12) and

2

∞

|g(x)|2e−xdx

|α(n)α(m)|2. (2.13)

=

0

n,m≥0

The above calculations suggest the following deﬁnitions. Let G = ℓ2(Z2+) be the standard Hilbert space of complex-valued sequences {ϕ(a,b)}(a,b)∈Z2

such that ϕ 2G :=

+

|ϕ(a,b)|2 < ∞.

a,b≥0

The inner product in G is given by ϕ,ψ G =

![image 33](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile33.png>)

ϕ(a,b)ψ(a,b).

a,b≥0

Next, we deﬁne an operator Q for any given ϕ ∈ G by Qϕ(a,b) =

ϕ(c,d)Q(a,b,c,d),

c,d≥0

c+d=a+b

where

∞

La(x/2)Lb(x/2)Lc(x/2)Ld(x/2)e−xdx. (2.14) In analogy with the Hermite polynomial approach, we can analyze the operator

Q(a,b,c,d) =

0

- Q by its action in certain orthogonal invariant subspaces of ﬁnite dimension. For


any integer S ≥ 0, let GS denote the subspace of sequences ϕ : Z2+ → C such that ϕ(a,b) = 0 if a + b = S. Clearly, the collection {GS}S≥0 is orthogonal and

![image 34](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile34.png>)

GS.

G =

S≥0

We also have that dim(GS) = S + 1 and Q(GS) ⊂ GS. Letting QS denote the restriction of Q to the subspace GS, we conclude that the operator QS can be represented by the following matrix

QS = [Q(a,S − a,c,S − c)]a,c=0,...,S. (2.15)

- Theorem 6. For any radial f(x) = n≥0 α(n)Ψn(x) ∈ L2(R2,dx) we have


1 16

eit∆f(x) 4L4(R3,dxdt) =

ϕ,Qϕ G (2.16) and

![image 35](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile35.png>)

1 16

4 =

ϕ 2G, (2.17)

2−1/2 f(x) L2(R2,dx)

![image 36](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile36.png>)

where ϕ(a,b) = α(a)α(b) for all a,b ≥ 0. For any S ≥ 0 the matrix QS at (2.15) is a positive semi-deﬁnite doubly stochastic matrix with strictly positive entries. We conclude that  Q G→G = 1. Furthermore, a function ϕ ∈ G satisﬁes

ϕ,Qϕ G = ϕ 2G if and only if it has the property that ϕ(a,b) = ϕ(c,d) whenever a + b = c + d. Corollary 7. For any radial f(x) ∈ L2(R2,dx) we have

eit∆f(x) L4(R3,dxdt) ≤ 2−1/2 f(x) L2(R2,dx), (2.18) and equality is attained if and only if f(x) = Ae−B x

2

, where A,B ∈ C and ReB > 0.

- 2.3. Spherical Harmonics and Gegenbauer Polynomials. In this part we make use of the special connection between spherical harmonics and Gegenbauer polynomials given by the Funk-Hecke formula (3.24) to prove a sharpened inequality for the Schr¨odinger operator that is maximized by radial functions. We perform a diagonalization process in an operator over L2(Sd−1) that naturally emerges from our approach and which ultimately allows us to perform a near-extremizer analysis.


For any d ≥ 3 deﬁne the following operator R(g)(ξ) =

dζ ξ − ζ d−2

g(ζ)

(2.19)

![image 37](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile37.png>)

Sd−1

for g ∈ L2(Sd−1). Above, Sd−1 represents the unit sphere in Rd,   ·  the Euclidean norm in Rd and dζ (and dξ below) the natural surface measure over Sd−1.

- Theorem 8. Let d ≥ 3. Let f ∈ L2(Rd,dx) be a function of Schwartz class and deﬁne g(r,ξ) = f(rξ) for any r > 0 and ξ ∈ Sd−1. We obtain


∞

dx x 2

π (d − 2)|Sd−1|

g(r,ξ)R(g(r,·))(ξ)dξrd−1dr. (2.20)

|eit∆f(x)|2

![image 38](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile38.png>)

dt =

![image 39](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile39.png>)

![image 40](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile40.png>)

R Rd

0 Sd−1

Moreover, the operator R is bounded over L2(Sd−1) and for all g ∈ L2(Sd−1) we have

2 d

Dist(g,Const)2 , (2.21)

g(ξ)R(g)(ξ)dξ ≤ |Sd−1|

|g(ξ)|2dξ −

![image 41](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile41.png>)

![image 42](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile42.png>)

Sd−1

Sd−1

where Dist(g,Const) denotes the distance in the L2(Sd−1)-norm of g(ξ) to the subspace of constant functions.

- Theorem 9. Let d ≥ 3. Then for all f ∈ L2(Rd,dx) we have


dx x 2

π d − 2 Rd

2 d

|eit∆f(x)|2

|f(x)|2dx −

Dist(f, Radial)2 , (2.22)

dt ≤

![image 43](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile43.png>)

![image 44](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile44.png>)

![image 45](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile45.png>)

R Rd

where Dist(f, Radial) denotes the distance in the L2(Rd,dx)-norm of f(x) to the subspace of radial functions. In particular, we have

π d − 2 Rd

dx x 2

|eit∆f(x)|2

|f(x)|2dx, (2.23) and equality is attained if and only if f(x) is a radial function. Corollary 10. Let d ≥ 3 and 2 ≤ p ≤ 2 + 4/d. There exists C > 0 such that for all f ∈ L2(Rd,dx) we have

dt ≤

![image 46](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile46.png>)

![image 47](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile47.png>)

R Rd

1/p

1/2

dx x d+2−pd/2

|eit∆f(x)|p

|f(x)|2dx

dt

≤ C

.

![image 48](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile48.png>)

R Rd

Rd

Remark.

- (1) The above corollary is a straightforward consequence of Stein and Weiss interpolation result with change of measures [17, Theorem 2.11] (which works very well for homogeneous weights) in conjunction with Theorem 9 and the Strichartz estimate (1.1) for p = q = 2 + 4/d. To the best of our knowledge the ﬁrst time that inequality (2.23) appeared was in [14]. In [20], Watanabe identiﬁed the extremizers as radial functions (and also for related inequalities for the fractional laplacian). This fact was later rediscovered (in a much general framework) by Bez and Sugimoto in [4]. Our improvement here lies in the near extremizer analysis of (2.22).
- (2) The fact that (2.23) is attained for any radial function is a direct consequence of (2.20) and the fact that R(1) ≡ |Sd−1|1 (this can be shown using (3.24) and (3.26) for n = 0 and a = ν). We also note that the proofs of Theorems 8 and 9 actually show that the diﬀerence between the left and right hand side in (2.23) is proportional to Dist(f, Radial)2.


3. Proofs for the Main Results

Throughout this paper we use the following deﬁnition for the Fourier Transform of a function f(x)

f(y) =

f(x)e−2πix·ydx. (3.1)

Rd

- 3.1. The Hermite and Laguerre Polynomials Part. To prove Theorems 1 and 5 we start by calculating the solution of the Schr¨odinger equation for the functions Φm(x) and Ψn(x) deﬁned in (2.1) and (2.10) respectively.


- Lemma 11. For all m ∈ Zd+ we have ei∆t(Φm)(x)


|m|

![image 49](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile49.png>)

4π2it 1 + 16π2t2

1 − 4πit 1 + 4πit

x √1 + 16π2t2

x 2 .

= (1 + 4πit)−d/2

exp

Φm

![image 50](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile50.png>)

![image 51](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile51.png>)

![image 52](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile52.png>)

![image 53](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile53.png>)

(3.2) Also, for all n ≥ 0 we have

ei∆t(Ψn)(x)

n

(3.3)

4π2it 1 + 16π2t2

1 − 4πit 1 + 4πit

x √1 + 16π2t2

= (1 + 4πit)−d/2

x 2 .

exp

Ψn

![image 54](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile54.png>)

![image 55](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile55.png>)

![image 56](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile56.png>)

![image 57](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile57.png>)

Proof. We prove ﬁrst the second identity. Firstly, if f(x) = f( x ) is a radial function, then its Fourier transform f(y) = f( y ) is also radial and we have

∞

f(r)Jν(2πrs)rν+1dr, (3.4)

sν f(s) = 2π

0

for every s > 0, where ν = d/2−1 and Jν(z) is the Bessel function of the ﬁrst kind. Secondly, the identity in [12, 7.421-4] states that

n

∞

αy2 4β(α − β) for any α,β ∈ C with Reβ > 0 and any ν > −1. Applying the above identity for α = 2π and β = π(a + 1) in conjunction with identity (3.4) we deduce that

α β

y2

2

yνe−

4β Ln(ν)

Ln(ν) αx2 Jν(xy)dx = (2β)−ν−1 1 −

xν+1e−βx

![image 58](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile58.png>)

![image 59](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile59.png>)

![image 60](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile60.png>)

- 0


Ln(ν)(2π x 2)e−π(a+1) x 2 (y) = (1 + a)−d/2

a − 1 a + 1

![image 61](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile61.png>)

n

Ln(ν)

2π y 2 1 − a2

![image 62](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile62.png>)

π y 2

e−

1+a , (3.5)

![image 63](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile63.png>)

where ν = d/2−1. Taking a = 0 in the above identity reads Ψn(y) = (−1)nΨn(y). Finally, since

2it y 2Ψn(y) = (−1)nLn(ν)(2π y 2)e−π(4πit+1) y

2

(ei∆tΨn)(y) = (−1)ne4π

, we can use identity (3.5) with a = 4πit to deduce (3.3).

Identity (3.2) in dimension d > 1 follows from its one-dimensional version since we have Φm(x) = Φm

(x1)...Φm

(xd) if m = (m1,...,md). We can now use identities [12, 7.388–2 and 7.388–4] to show that

1

d

√4πy √1 − a2

n

√

![image 64](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile64.png>)

![image 65](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile65.png>)

a − 1 a + 1

πy2

e−

4πx)e−π(a+1)x2 (y) = (1 + a)−d/2 −

![image 66](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile66.png>)

1+a, (3.6)

Hn

Hn(

![image 67](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile67.png>)

![image 68](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile68.png>)

![image 69](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile69.png>)

![image 70](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile70.png>)

for any a ∈ C with Re a > −1. Finally, identity (3.2) for d = 1 follows by an analogous way as in the Laguerre polynomial case, but now using identity (3.6) for

2it y 2Φn(y) (which can also be deduced from (3.6) by taking a = 0).

a = 4πit and the fact that (ei∆tΦn)(y) = (−i)ne−4π

Proof of Theorem 1. Step 1. Let f ∈ L2(Rd,dx) have the following expansion f(x) =

α(m)Φm(x)

m∈Zd+

α(m)Hm(x). By Lemma 11, we obtain that

and deﬁne g(x) = m∈Zd

+

|ei∆tf(x)| = |1 + 16π2t2|−d/4

α(m)

m∈Zd+

Recalling that Φm(x) = Hm(√4π x)e−π x

2

![image 71](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile71.png>)

![image 72](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile72.png>)

1 − 4πit 1 + 4πit

![image 73](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile73.png>)

|m|

Φm

x √1 + 16π2t2

![image 74](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile74.png>)

![image 75](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile75.png>)

![image 76](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile76.png>)

and λ = 2/p, we deduce that

.

q/p

|ei∆tf(x)|pdx

dt

R R

 

p

|m|

![image 77](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile77.png>)

1 − 4πit 1 + 4πit

x √1 + 16π2t2

Φm

α(m)

=

![image 78](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile78.png>)

![image 79](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile79.png>)

![image 80](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile80.png>)

Rd m

R

 

p

|m|

![image 81](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile81.png>)

1 − 4πit 1 + 4πit

= p−qd/2p

α(m)

dγd(y)

Hm(λy)

![image 82](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile82.png>)

Rd m

R

p

1/2

= (p−qd/2p/4)

α(m)eπi|m|sHm(λy)

dγd(y)

−1/2 Rd m

1/2

 Ht/2g qLp(dγ

= (p−qd/2p/4)

d)dt,

−1/2

 

q/p

dt (1 + 16π2t2)

dx

![image 83](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile83.png>)

qd 4

![image 84](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile84.png>)

 

q/p

dt 1 + 16π2t2

![image 85](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile85.png>)

q/p

ds

(3.7)

![image 86](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile86.png>)

where in the second identity above we did the change of variables y = 1+162πpπ2t2 x and used that qd4 − qd2p = 1, and in the third identity we did πs = arctan(−4πt). Similarly, we deduce that

![image 87](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile87.png>)

![image 88](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile88.png>)

![image 89](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile89.png>)

|f(x)|2dx = 2−d/2

Rd

|g(y)|2dγd(y). (3.8)

Rd

Step 2. We now need to deﬁne an auxiliary linear operator Tω : L2(Rd,dγd) → L2(Rd,dγd) for any ω ∈ C with |ω| ≤ 1 as follows

Tω(Hm)(x) = ω|m|Hm(x). (3.9) This deﬁnes a group with respect to complex multiplication: Tω

and Tω is an isometric transformation if |ω| = 1. Now, observe that by the deﬁnition of Ht in (2.2) we have Ht+s = HtTe2πis for all real s,t and, since Hn(−x) = (−1)nHn(x), we also have T−1g(x) = g(−x) for all g(x) and we conclude that HtT−1 = T−1Ht for all real t. All these considerations imply that Ht−1/4T−i = T−1Ht and Ht+1/4T−i =

Tω

1ω2 = Tω

2

1

Ht for all real t. For g(y) = m α(m)Hm(y) we obtain

1/2

 HtT−ig qLp(dγ

d)dt

−1/2

1/2

1/2

- 1

![image 90](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile90.png>)

- 2


- 1

![image 91](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile91.png>)

- 2


 Ht/2+1/4T−ig qLp(dγ

 Ht/2−1/4T−ig qLp(dγ

d)dt +

d)dt

=

−1/2

−1/2

1/2

1/2

- 1

![image 92](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile92.png>)

- 2


- 1

![image 93](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile93.png>)

- 2


 Ht/2g qLp(dγ

T−1Ht/2g qLp(dγ

=

d)dt +

d)dt

−1/2

−1/2

1/2

 Ht/2g qLp(dγ

=

d)dt.

−1/2

The Theorem 1 follows from (3.7), (3.8) and (3.10).

(3.10)

Before we prove Theorem 3 we need a basic lemma about self-adjoint linear transformations and their norms. The proof can be done using the Spectral Theorem and we leave the details to the interested reader.

- Lemma 12. Let O : B → B be a bounded self-adjoint linear transformation and B


be a separable Hilbert space over C with Hermitian inner product  ·,· B. Assume that there exists a real number θ > 0 such that

| Onu,v B| ≪ θn for all n ≥ 1 and all u,v ∈ B, where the implied constant depends only on u and v. Then

 Ou B

u B ≤ θ. Moreover, if in addition we have

 O B→B := sup u =0

![image 94](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile94.png>)

| Onu0,v0 B| ≫ θn for some vectors u0 and v0 and for all n ≥ 1 then

 O B→B = θ.

The linear operators Tω deﬁned in (3.9) for |w| ≤ 1 also play an important role in the proof of Theorem 3. These operators are given by the following Mehler Kernel (see [2, p. 163])

exp −ω2( x 2 + y 2) 2(1 − ω2)

1 (1 − ω2)d/2

Tω(x,y) =

+

![image 95](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile95.png>)

![image 96](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile96.png>)

Hm(x)Hm(y) m!

ω|m|

,

=

![image 97](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile97.png>)

m∈Zd+

ωx · y 1 − ω2

![image 98](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile98.png>)

(3.11)

where the convergence of the above series (for ﬁxed x and y) is absolute for |ω| < 1. In other words, for all g ∈ L2(Rd,dγd) we have

Tω(x,y)g(y)dγd(y). At this point we recommend the reader to recall the notation introduced in Section

Tωg(x) =

Rd

- 2.1.


Proof of Theorem 3. Step 1. The identities in (2.9) easily follow from the deﬁnitions of the space F and the operator P in conjunction with identities (2.4) and

- (2.5).


- Step 2. Let S ≥ 0. Our goal is to explicitly compute the n-fold composition Pn of the operator P for any n ≥ 0. In general, for any n ≥ 0, if ϕ ∈ F and M ∈ M with |M| = S we have


P(n)(M,N) M!

Pnϕ(M) =

,

ϕ(N)

![image 99](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile99.png>)

(3.12)

N∈M

|N|=S

for some coeﬃcients P(n)(M,N). The idea of the proof is the following: (a) Give a nice representation of these coeﬃcients P(n)(M,N) in terms of a certain multiplication operator; (b) Show that P(2)(M,N) = P(M,N) in the case (k −1)dℓ/2 = 1, hence P2 = P; (c) Use Lemma 12 to exactly compute the norm of P restricted to FS when µ = (k − 1)dℓ/2 = 1.

We start with n = 2. In this case, if ϕ ∈ F and M ∈ M with |M| = S we have P2ϕ(M) =

P(M,N) M!

P(N,L) N!

P(M,N) M!

=

ϕ(L)

Pϕ(N)

![image 100](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile100.png>)

![image 101](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile101.png>)

![image 102](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile102.png>)

L∈M

N∈M

N∈M

|L|=S

|N|=S

|N|=S

P(2)(M,L) M!

ϕ(L)

,

=

![image 103](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile103.png>)

L∈M

|L|=S

(3.13) where

P(M,N)P(N,L) N!

P(2)(M,L) =

.

![image 104](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile104.png>)

(3.14)

N∈M

|N|=S

To investigate the above coeﬃcients we need to deﬁne a new kernel involving Hermite polynomials. For any M = [mi,j] ∈ M and any collection of vectors {x1,...,xℓ} in Rd let

ℓ

k

Hmi,j(λxi)

HM(x1,...,xℓ) =

i=1

j=1

![image 105](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile105.png>)

![image 106](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile106.png>)

(recall that λ = 2/p = 1/k). For any S ≥ 0 deﬁne the following kernel

HM(x1,...,xℓ)HM(y1,...,yℓ) M!

KS(x1,...,xℓ;y1,...,yℓ) :=

.

![image 107](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile107.png>)

M=[ni,j]∈M

|M|=S

(3.15)

Also deﬁne the associated operator KS[g](x1,...,xℓ) =

KS(x1,...,xℓ;y1,...,yℓ)g(y1,...,yℓ)dγd(y1)...dγd(yℓ),

(Rd)ℓ

for any g ∈ L2((Rd)ℓ,dγd(y1)...dγd(yℓ)). Using (2.8), (3.13) and (3.14), we obtain that

P(2)(M,L) =

HM(x1,...,xℓ)KS[HL](x1,...,xℓ)dγd(x1)...dγd(xℓ)

(Rd)ℓ

for any M = [mi,j] and L = [li,j] in M. In an analogous way, if ϕ ∈ F and M ∈ M with |M| = S we have the following representation for the coeﬃcient in (3.12)

HM(x1,...,xℓ)KS(n−1)[HL](x1,...,xℓ)dγd(x1)...dγd(xℓ),

P(n)(M,L) =

(Rd)ℓ

(3.16) where KS(n−1) is the (n − 1)-fold composition of KS.

- Step 3. Let µ = (k−1)dℓ/2. We claim that the kernel KS in (3.15) has the following alternative form


KS(x1,...,xℓ;y1,...,yℓ)

⌊S/2⌋

(µ)s s!

=

![image 108](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile108.png>)

s=0

(x1)...Hm

(yℓ) m1!...mℓ!

(xℓ)Hm

(y1)...Hm

Hm

, (3.17)

1

ℓ

1

ℓ

![image 109](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile109.png>)

i |mi|=S−2s

mi∈Zd+

where (µ)s = Γ(Γ(µ+µ)s) is the Pochhammer symbol. In particular, for all n ≥ 1 we have that

![image 110](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile110.png>)

KS(n−1)[g](x1,...,xℓ)

⌊S/2⌋

n−1

(µ)s s!

(xℓ), (3.18)

(x1)...Hm

=

α(m1,...,mℓ)Hm

![image 111](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile111.png>)

1

ℓ

s=0

i |mi|=S−2s

mi∈Zd+

if g(x1,...,xℓ) is a polynomial of the following form

g(x1,...,xℓ) =

⌊S/2⌋

(x1)...Hm

(xℓ). (3.19)

α(m1,...,mℓ)Hm

1

ℓ

s=0 i |mi|=S−2s mi∈Zd+

![image 112](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile112.png>)

To prove the claim (3.17) we use the Mehler kernel (3.11). Recall that λ = 1/k. For any |ω| < 1 we obtain that

k j=1 Hmi,j(λxi)Hmi,j(λyi)

ℓ i=1

ω|M|

KS(x1,...,xℓ;y1,...,yℓ)ωS =

![image 113](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile113.png>)

M!

M∈M

S≥0

=

=

ℓ

ℓ

k

Tω(xi,yi)

Tω(λxi,λyi)

= (1 − ω2)−µ

i=1

i=1

(x1)Hm

(y1) m1!

Hm

(µ)a a!

ω2a

1

1

...

![image 114](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile114.png>)

![image 115](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile115.png>)

a≥0

b≥0 i |mi|=b mi∈Zd+

(xℓ)Hm

(yℓ) mℓ!

Hm

ℓ

ℓ

![image 116](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile116.png>)

ωb

=

S≥0

⌊S/2⌋

(µ)a a!

![image 117](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile117.png>)

a=0

(yℓ) m1!...mℓ!

(y1)...Hm

(x1)...Hm

(xℓ)Hm

Hm

1

1

ℓ

ℓ

![image 118](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile118.png>)

i |mi|=S−2a

mi∈Zd+

ωS.

The claim follows by from comparing the coeﬃcients of the power series of the ﬁrst and last expressions.

- Step 4. Let M ∈ M with |M| = S. It is easy to see that HM(x1,...,xℓ) has an expansion in terms of Hermite polynomials of the following form

HM(x1,...,xℓ) =

S

s=0 i |ni|=S−s ni∈Zd+

αM(n1,...,nℓ)Hn

1

(x1)...Hn

ℓ

(xℓ).

However, since HM(−x1,...,−xℓ) = (−1)SHM(x1,...,xℓ) (recall that Hn(−x) = (−1)nHn(x)), we deduce that αM(n1,...,nℓ) = 0 if s is not even, where S − s =

i |ni|. We conclude that HM(x1,...,xℓ) has the special form (3.19), which by (3.18) implies that KS[HM] = HM if µ = (k −1)dℓ/2 = 1. Using identity (3.16) we conclude that

P(2)(M,N) = P(M,N)

for all M,N ∈ M, if µ = 1. We deduce that the operator PS (the restriction of P to the subspace FS) is a projection for any S ≥ 0. Since the spaces FS are orthogonal and their span is dense in F, we deduce that P is well-deﬁned in the whole F and it is also a projection.

- Step 5. It remains to calculate the norm of PS on the space FS for µ = (k−1)dℓ/2 >

1. By the considerations of the previous step, the fact that the any function HL for L ∈ M has the special form (3.19) allow us to apply Ho¨lder’s inequality in (3.16) and obtain that

|P(n)(M,L)|2 ≪

(Rd)ℓ

|KS(n−1)[HL](x1,...,xℓ)|2dγd(x1)...dγd(xℓ)

=

⌊S/2⌋

s=0

(µ)s s!

![image 119](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile119.png>)

2n−2

i |ni|=S−2s

ni∈Zd+

|αL(n1,...,nℓ)|2 n1!...nℓ! ≪

![image 120](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile120.png>)

(µ)⌊S/2⌋ ⌊S/2⌋!

![image 121](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile121.png>)

2n−2

,

(3.20)

for any M,L ∈ M and all n ≥ 1, where the implied constants do not depend on n. Note that in (3.20) we used the fact that the map s  → (µ)

s

![image 122](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile122.png>)

s! is increasing for s > 0 if µ > 1. We can now apply Lemma 12 to deduce that

 PS FS→FS ≤

(µ)⌊S/2⌋ ⌊S/2⌋!

![image 123](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile123.png>)

.

- Step 6. Now we show the reverse estimate found in (3.20) for some matrix M = L = M0. It is simple to see that we can choose M0 ∈ M such that


(x1,...,xℓ) = HS(λx11),

HM

0

where xi = (xi1,...,xid) for i = 1,..,ℓ. It is known that Hn(λx) =

n

n a

λa(1 − λ2)(n−a)/2Hn−a(0)Ha(x),

a=0

- for all n ≥ 0 and that Hn(0) = 0 if and only if n is even. We deduce that


Hn(λx)dγ(x) = (1 − λ2)n/2Hn(0) = 0, if n is even and

R

Hn(λx)H1(x)dγ(x) = nλ(1 − λ2)(n−1)/2Hn−1(0) = 0 if n is odd (recall that λ = 1/k < 1 since k ≥ 2). We conclude that

R

![image 124](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile124.png>)

S

(x1)...Hn

(xℓ),

(x1,...,xℓ) =

(n1,...,nℓ)Hn

αM

HM

0

0

1

ℓ

s=0 i |ni|=S−2s ni∈Zd+

((1,0,...,0),0,...,0) = 0 if S is odd. We can now use (3.16) and (3.18) to deduce that

(0,...,0) = 0 if S is even and αM

where αM

0

0

- P(n)(M0,M0) =

⌊S/2⌋

s=0

(µ)s s!

![image 125](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile125.png>)

n−1

i |ni|=S−2s

ni∈Zd+

|αM

0

(n1,...,nℓ)|2 n1!...nℓ! ≫

![image 126](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile126.png>)

(µ)⌊S/2⌋ ⌊S/2⌋!

![image 127](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile127.png>)

n−1

.

We can now apply Lemma 12 again to ﬁnally conclude that

 PS FS→FS =

(µ)⌊S/2⌋ ⌊S/2⌋!

![image 128](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile128.png>)

. This ﬁnishes the proof.

Proof of Theorm 5. This proof is analogous to the proof of Theorem 1. The ﬁrst step is almost identical but now using the following change of variables: y =

![image 129](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile129.png>)

πp

![image 130](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile130.png>)

1+16π2t2 x and πs = arctan(−4πt). However, in this case we do not need to use an extra step to transform the multiplication factor eπims into e2πims, since it naturally emerges from the form of ei∆tΨm(x) proved in Lemma 11. The diﬀerent thing here is that the factor 11+4−4πitπit has no longer a square root on it.

![image 131](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile131.png>)

Proof of Theorem 6. Step 1. Identity (2.16) easily follows from identities (2.12) and (2.13).

- Step 2. We now show show the facts about matrix QS = [Q(a,S − a,c,S − c)]a,c=0,...,S in (2.15). The fact that Q(a,b,c,d) > 0 for all integers a,b,c,d ≥ 0 is shown in Theorem 14. Note that if a + b = c + d = S, the explicit formula for


- Q(a,b,c,d) in (4.2) can be written in the following form


Q(a,b,c,d) =

S

Fu(a,S − a)Fu(c,S − c)

u=0

where

u

2

a r

S − a u − r

(S − u)!u! a!(S − a)!2S

(−1)r

.

Fu(a,S − a) =

![image 132](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile132.png>)

r=0

Thus, if we deﬁne FS = [Fa(c,S − c)]a,c=0,...,S we obtain QS = FS∗FS. This implies that QS is positive semi-deﬁnite. Now we show that QS is doubly stochastic. For any ν > −1, the Laguerre polynomials satisfy the following summation formula

LN(aν+a−1)(x1 + ... + xa) =

(x1)...Ln(ν)

Ln(ν)

(xa). (3.21) We also have that

a

1

n1+...+na=N

Ln(ν+1)(x) − Ln(ν−+1)1 (x) = Ln(ν)(x), (3.22)

- for all n ≥ 1. Recalling that we denote L(0)n (x) = Ln(x) for simplicity, we can use (3.21) to obtain that


∞

La(x/2)Lb(x/2) Lc(x/2)Ld(x/2)e−xdx

Q(a,b,c,d) =

0 a+b=S

a+b=S

∞

L(1)S (x)Lc(x/2)Ld(x/2)e−xdx

=

0

∞

∞

L(1)S (x)e−xdx

L(1)S (x)[Lc(x/2)Ld(x/2) − 1]e−xdx +

=

0

0

∞

L(1)S (x)e−xdx. In the last identity we used that Ln(0) = 1 for all n ≥ 0 and that

=

0

∞

L(1)S (x)P(x)xe−xdx = 0,

0

for any polynomial P(x) of degree at most S − 1. Next, we can apply (3.22) to conclude by induction that

∞

∞

∞

L(1)S−1(x)e−xdx

{L(1)S−1(x) + LS(x)}e−xdx =

L(1)S (x)e−xdx =

0

0

0

∞

∞

L(1)S−2(x)e−xdx

{L(1)S−2(x) + LS−1(x)}e−xdx =

=

0

0

∞

∞

L(1)S−3(x)e−xdx = ... =

L(1)0 (x)e−xdx

=

0

0

∞

e−xdx = 1.

=

0

- Step 3. Clearly, since each QS is doubly stochastic, any function ϕ ∈ G with the property that ϕ(a,b) = ϕ(c,d) if a+b = c+d is a ﬁxed point of Q, that is, Qϕ = ϕ. Assume now that ϕ ∈ G is a non-zero function such that


ϕ,Qϕ G = ϕ 2G.

We conclude that  Qϕ 2G = ϕ 2G. Since the spaces GS are mutually orthogonal, Q(GS) ⊂ GS and their span is dense in G, we deduce that

 QS(ϕS) 2G =  Qϕ 2G = ϕ 2G =

ϕS 2G,

S≥0

S≥0

where ϕS ∈ GS is the projection of ϕ in GS (that is, ϕS(a,b) = ϕ(a,b) if a + b = S and ϕS(a,b) = 0 otherwise). This implies that  QS(ϕS) 2G = ϕS 2G for every S ≥ 0. Since the matrix (2.15) that represents QS is positive semi-deﬁnite and has strictly positive entries, the Ostrowski’s Theorem (see [12, 15.820]) guarantees that all the eigenvalues of QS other than 1 are non-negative and strictly less than 1, hence the vector (ϕ(0,S),ϕ(1,S − 1),...,ϕ(S,0)) must be a multiple of (1,1,...,1). This ﬁnishes the proof.

Proof of Corollary 7. The inequality (2.18) easily follows from Theorem 5 for

- d = 2 and p = q = 4 and Theorem 6 identities (2.16) and (2.17). Assume that


f(x) = n≥0 α(n)Ψn(x) is a non-zero radial function that maximizes (2.18). We can use Theorem 6 again to deduce that ϕ(a,b) = α(a)α(b) belongs to G, is not

identically zero and satisﬁes  Qϕ G = ϕ G. We conclude that ϕ(a,b) depends only on a + b. It is then a simple task to verify by induction on a + b that

ϕ(a,b) = α(0)2

α(1) α(0)

![image 133](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile133.png>)

a+b

for all a,b ≥ 0 and α(0) = 0. Moreover, since the norm of ϕ in G is ﬁnite, we must have αα(1)(0) < 1. This implies that α(n) = α(0) α α(0)(1)

n

for all n ≥ 0. We can now use the generating function for the Laguerre polynomials

![image 134](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile134.png>)

![image 135](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile135.png>)

e−xω/(1−ω) 1 − ω

Ln(x)ωn

=

![image 136](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile136.png>)

n≥0

2 |1−ω|2 > 0. This ﬁnishes the proof.

1+ω

1−ω x 2, where Re 11+−ωω = 1−|ω|

for ω = αα(1)(0) to deduce that f(x) = α(0)e−π

![image 137](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile137.png>)

![image 138](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile138.png>)

![image 139](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile139.png>)

![image 140](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile140.png>)

- 3.2. The Spherical Harmonics and Gegenbauer Polynomials Part.


Proof of Theorem 8. We make use of the Delta Calculus to reduce the problem to a bi-linear form on the sphere L2(Sd−1) (we refer to [7] for a short review of the basics aspects). Let f ∈ L2(Rd,dx) be a smooth function and deﬁne g(r,ξ) = f(rξ) for any r > 0 and ξ ∈ Sd−1. We obtain

dx x 2

|eit∆f(x)|2

dt

![image 141](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile141.png>)

R Rd

![image 142](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile142.png>)

2it( y 2− z 2)+2πix·(y−z)dydz

f(y) f(z)e−4π

=

R Rd (Rd)2

Γ(d/2 − 1) πd/2−2 (Rd)2

dydz y − z d−2

![image 143](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile143.png>)

f(y) f(z)δ 2π( y 2 − z 2)

=

![image 144](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile144.png>)

![image 145](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile145.png>)

dx x 2

dt

![image 146](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile146.png>)

dydz ( y + z ) y − z d−2

Γ(d/2 − 1) 2πd/2−1 (Rd)2

![image 147](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile147.png>)

f(y) f(z)δ y − z

=

![image 148](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile148.png>)

![image 149](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile149.png>)

∞

dζ ξ − ζ d−2

π (d − 2)|Sd−1|

dξrd−1dr,

![image 150](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile150.png>)

g(r,ξ)

g(r,ζ)

=

![image 151](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile151.png>)

![image 152](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile152.png>)

0 Sd−1

Sd−1

where in the second identity above we used that · −2  → Γ(πd/d/22−−21) · 2−d via the Fourier Transform (3.1).

![image 153](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile153.png>)

This proves identity (2.20). The above calculation begs us to study the boundedness of the operator R deﬁned in (2.19) which has the following alternative form

- 1

![image 154](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile154.png>)

- 2d/2−1 Sd−1


dζ (1 − ξ · ζ)d−2

.

R(g)(ξ) =

g(ζ)

![image 155](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile155.png>)

We now prove inequality (2.21). Any function g ∈ L2(Sd−1) can be decomposed in the following form

g(ξ) =

Yn(ξ),

n≥0

where Yn(ξ) is a spherical harmonic of degree n. We note that the set {Yn(ξ)}n≥0 is always orthogonal in L2(Sd−1) and that Y0(ξ) ≡ [the mean of g(ξ) over Sd−1]. In particular, this implies that

Dist(g,Const)2 =

n≥1

Yn 2L2(Sd−1). (3.23)

If g ≡ Yn, we can calculate R(g)(ξ) by using the Funk-Hecke formula (see [6, Theorem 1.2.9])

- 1

![image 156](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile156.png>)

- 2ν Sd−1


Yn(ζ)F(ξ · ζ)dζ

R(Yn)(ξ) =

(3.24)

1

= |Sd−2| 2νCnν(1)

Cnν(u)F(u)(1 − u2)ν−1/2 Yn(ξ),

![image 157](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile157.png>)

−1

where F(u) = (1 − u)−ν and {Cnν(u)}n≥0 are the Gegenbauer polynomials with parameter ν = d/2 − 1 (in fact, the Funk-Hecke calculation states that the above formula holds for any reasonable F(u)).

For any ν > −1/2, the Gegenbauer polynomials are deﬁned as the orthogonal polynomials with respect to the measure (1 − u2)ν−1/2du (u ∈ (−1,1)) and normalized by the condition

Γ(n + 2ν) Γ(2ν)n!

Cnν(1) =

. (3.25)

![image 158](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile158.png>)

We can use their relation with the Jacobi polynomials [12, 8.962-4] together with formula [12, 7.391-4] (for ρ = ν − 1/2 − a,α = β = ν − 1/2) to deduce that

1

1 Cnν(1)

Cnν(u)(1 − u)−a(1 − u2)ν−1/2du

![image 159](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile159.png>)

−1

(3.26)

Γ(ν + 1/2)Γ(ν + 1/2 − a)Γ(n + a) Γ(a)Γ(2ν + n + 1 − a)

= 22ν−a

![image 160](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile160.png>)

for any a < 1/2 + ν and any ν > −1/2. We can now use this formula at a = ν = d/2 − 1 in conjunction with (3.24) and (3.25) to deduce that

d − 2 2n + d − 2|Sd−1|Yn(ξ) for all n ≥ 0. We conclude that for g(ξ) = n≥0 Yn(ξ) we have

R(Yn)(ξ) =

![image 161](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile161.png>)

d − 2 2n + d − 2

Yn 2L2(Sd−1)

g(ξ)R(g)(ξ)dξ = |Sd−1|

![image 162](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile162.png>)

![image 163](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile163.png>)

Sd−1

n≥0

2n 2n + d − 2

= |Sd−1| g 2L2(Sd−1) −

Yn 2L2(Sd−1)

![image 164](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile164.png>)

n≥1

2 d n≥1

Yn 2L2(Sd−1)

≤ |Sd−1| g 2L2(Sd−1) −

![image 165](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile165.png>)

2 d

Dist(g,Const)2 . This concludes the theorem.

= |Sd−1| g 2L2(Sd−1) −

![image 166](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile166.png>)

Proof of Theorem (9). It is easy to see that Theorem 9 will follow from Theorem 8 once we prove the following lemma.

Lemma 13. Let f ∈ L2(Rd) and write g(r,ξ) = f(rξ) for any r > 0 and ξ ∈ Sd−1. Then we have

∞

Dist(f,Radial)2 =

Dist(g(r,·),Const)2rd−1dr.

0

Let f ∈ L2(Rd,dx). The functions g(r,ξ) = f(rξ) for ξ ∈ Sd−1 are measurable for almost every r > 0 and thus we can decompose them in spherical harmonics

g(r,ξ) =

Yn,r(ξ)

n≥0

for almost every r > 0. The projection Pf(r) of f(x) in the space of radial functions of L2(Rd,dx) is given by

1 |Sd−1| Sd−1

Pf(r) =

g(r,ξ)dξ = Y0,r. By (3.23) we obtain

![image 167](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile167.png>)

|g(r,ξ) − Pf(r)|2dξ = Dist(g(r,·),Const)2 for almost every r > 0 and we conclude that Dist(f,Radial)2 =

Sd−1

∞

|g(r,ξ) − Pf(r)|2dξrd−1dr

0 Sd−1

∞

Dist(g(r,·),Const)2dr. This ﬁnishes the lemma and the theorem.

=

0

4. Appendix

We now explain the unexpected combinatorial interpretation that we discovered for the coeﬃcients Q(a,b,c,d) in (2.14). Let a,b,c,d be non-negative integers and let N = a + b + c + d > 0. Consider the set W(a,b,c,d) = Span{1a2b3c4d} of all words formed with a 1’s, b 2’s, c 3’s and d 4’s. We can deﬁne a way of measuring how diﬀerent two given words w = ℓ1ℓ2...ℓN and w′ = ℓ′1ℓ′2...ℓ′N in W(a,b,c,d) are by considering the following distance function: D(w,w′) = #{i : ℓi = ℓ′i}. Now consider the elementary word

2...2

3...3

4...4

.

e = 1...1

![image 168](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile168.png>)

![image 169](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile169.png>)

![image 170](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile170.png>)

![image 171](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile171.png>)

![image 172](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile172.png>)

![image 173](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile173.png>)

![image 174](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile174.png>)

![image 175](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile175.png>)

a

c

b

d

We say that a word w ∈ W(a,b,c,d) is even if D(w,e) is even, if not we say that w is odd. If we consider the word w to be formed by permuting the letters of the word

- e, then D(w,e) measures how many letters were moved from its original block. For instance, if a = b = c = d = 1 then e = 1234 and w = 1243 is an even word


while w′ = 1342 is an odd word. Let Weven(a,b,c,d) and Wodd(a,b,c,d) denote the sets of even and odd words in W(a,b,c,d) respectively. In what follows we use

the convention m n = 0 if m < 0 or m > n. Theorem 14. For any a,b,c,d ≥ 0 with N = a + b + c + d > 0 we have

#Weven(a,b,c,d) − #Wodd(a,b,c,d) 2N

. (4.1) Moreover, we have the following formula

Q(a,b,c,d) =

![image 176](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile176.png>)

2NQ(a,b,c,d)

U

u

2

(a + b − u)!(c + d − u)!(u!)2 a!b!c!d!

a r

b u − r

c s

d u − s

(−1)r+s

=

, (4.2) where U = min{a + b,c + d}. In particular, Q(a,b,c,d) > 0.

![image 177](<2017-gonccalves-orthogonal-polynomials-sharp-estimates_images/imageFile177.png>)

u=0

r,s=0

Remark. The combinatorial connection (4.1) was ﬁrst proved by Askey, Ismail and Koorwinder in [1] using the Master MacMahon Theorem. They also showed that Q(a,b,c,d) > 0 using analytic tools from the theory of Laguerre polynomials. Formula (4.2) was ﬁrst found by Gillis and Kleeman in [9] using again analytic tools in conjunction with a combinatorial argument. Later, Gillis and Zeilberger in [11] found a pure (and quite clever) combinatorial argument for formula (4.2).

Acknowledgments

The author is grateful to Emanuel Carneiro, Diogo Oliveira e Silva and Neal Bez for the helpful comments. The author is also grateful for the math inspiration acquired during the time he spent at The University of Texas at Austin working under the guidance of William Beckner.

References

- [1] R. Askey, M. Ismail, and T. Koorwinder, Weighted permutation problems and Laguerre polynomials, Journal of Combinatorial Theory, Series A, 25(3)(1978), 277-287
- [2] W. Beckner, Inequalities in Fourier Analysis, Annals of Mathematics, 102 (1975), 159-182.
- [3] J. Bennett, N. Bez, A. Carbery and D. Hundertmark, Heat-Flow Monotonicity of Strichartz Norms, Analysis and Partial Diﬀerential Equations 2(2)(2008), 147-158.
- [4] N. Bez and M. Sugimoto, Optimal constants and extremizers for some smoothing estimates, (to appear in Journal d’Analyse Mathematique) arXiv:1206.5110.
- [5] E. Carneiro, A sharp inequality for the Strichartz norm, Int. Math. Res. Notices 2009 (2009), 3127-3145.
- [6] F. Dai and Y. Xu, Approximation Theory and Harmonic Analysis on Spheres and Balls, Springer Monographs in Mathematics, New York, NY, 2013.
- [7] D. Foschi and D. Oliveira e Silva, Some recent progress on sharp Fourier restriction theory, arXiv:1701.06895. New York, NY, 2013.
- [8] D. Foschi, Maximizers for the Strichartz inequality, J. Eur. Math. Soc. 9 (2007), 739-774.
- [9] J. Gillis and J. Kleeman, A combinatorial proof of a positivity result, Math. Proc. Camb. Phil. Soc. 86 (1979), 13-19.
- [10] F. Gon¸calves, A Central Limit Theorem for Operators, Journal of Functional Analysis, v. 271 (6), p. 1585-1603, (2016).
- [11] J. Gillis and D. Zeilberger, A Direct Combinatorial Proof of a Positivity Result, Europ. J. Combinatorics 4 (1983), 221-223.
- [12] I. S. Gradshteyn and I. M. Ryzhik, Table of integrals, series, and products. Translated from the Russian. Seventh edition. Elsevier/Academic Press, Amsterdam, (2007).
- [13] D. Hundertmark and V. Zharnitsky, On sharp Strichartz inequalities in low dimensions, Int. Math. Res. Not. (2006), 1-18.
- [14] B. Simon, Best constants in some operator smoothness estimates, J. Funct. Anal. 107 (1992), 66-71.
- [15] R. Strichartz, Restrictions of Fourier transforms to quadratic surfaces and decay of solutions of wave equations, Duke Math. J. 44 (1977), 705-714.
- [16] S. Shao, Maximizers for the Strichartz inequalities and the Sobolev-Strichartz inequalities for the Schro¨dinger equation, Electronic Journal of Diﬀerential Equations 2009 (2009), no. 03, 1-13.
- [17] E. M. Stein and G. Weiss, Interpolation of operators with change of measures, Trans. Amer. Math. Soc. 87 (1958), 159-172.
- [18] G. Szego¨, Orthogonal Polynomials, American Mathematical Society Colloquium Publications Volume XXIII, Fourth Edition, 1975.
- [19] T. Tao, Nonlinear dispersive equations: Local and global analysis, CBMS Regional Conference Series in Mathematics 106.
- [20] K. Watanabe, Smooth perturbations of the self-adjoint operator |∆|α/2, Tokyo J. Math. 14


(1991), 239-250.

University of Alberta, Mathematical and Statistical Sciences, CAB 632, Edmonton,

Alberta, Canada T6G 2G1 E-mail address: felipe.goncalves@ualberta.ca URL: sites.ualberta.ca/∼goncalve

