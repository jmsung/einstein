---
type: source
kind: paper
title: Semidefinite programming bounds for distance distribution of spherical codes
authors: Oleg R. Musin
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2309.13854v2
source_local: ../raw/2023-musin-semidefinite-programming-bounds-distance.pdf
topic: general-knowledge
cites:
---

# Semidefinite programming bounds for distance distribution of spherical codes

##### Oleg R. Musin

## arXiv:2309.13854v2[math.OC]1Oct2023

###### Abstract

We present an extension of known semidefinite and linear programming upper bounds for spherical codes. We apply the main result for the distance distribution of a spherical code and show that this method can work effectively. In particular, we get a shorter solution to the kissing number problem in dimension 4.

Mathematics Subject Classification (2010) 90C22, 52C17

### 1 Introduction

Let G(kn)(t) (with G(kn)(1) = 1 and deg(G(kn)) = k ) be Gegenbauer polynomials that are orthogonal on the interval [−1,1] with respect to the weight function (1 − t2)(n−3)/2.

Let C be an N–element subset of the unit sphere Sn−1 ⊂ Rn. We define the k-th moment of C as

Gk(n)(c · c′) The positive semidefinite property of Gegenabauer polynomials yields that

Mk(C) :=

(c,c′)∈C2

Mk(C) ≥ 0 for all k = 1,2,... (1.1) Let f be a non-negative linear combination of Gegenabauer polynomials:

f(t) =

d

fkG(kn)(t), fk ≥ 0 for all k = 1,,..,d.

k=0

Then

d

f(c · c′) = f0N2 +

fkMk(C) ≥ f0N2. (1.2)

Sf(C) :=

(c,c′)∈C2

k=1

The distance distribution of C with respect to u ∈ C is the system of numbers {At(u) : −1 ≤ t ≤ 1}, where

At(u) := |{v ∈ C : v · u = t}|,

and the distance distribution of C is the system of numbers {At : −1 ≤ t ≤ 1}, where

1 N u∈C

At(C) = At :=

At(u).

Denote

Rf(C) :=

f(t)At(C).

t∈[−1,1)

Then

Sf(C) = NRf(C) + Nf(1) and (1.2) implies

Rf(C) ≥ f0N − f(1). (1.3) The semidefinite programming (SDP) method for spherical codes was proposed by Bachoc

and Vallentin [1] with further applications and extensions in [2, 3, 9, 10, 12, 15, 16, 18, 20]. The positive–semidefinite property of Gegenbauer polynomials yields the positive–

semidefinite property of matrices Skn. Now consider polynomials F that were defined by Bachoc and Vallentin. Let F(t,u,v) be a symmetric polynomial with expansion

F(t,u,v) =

d

⟨Hk,Skn(t,u,v)⟩

k=0

in terms of the matrices Skn.

Suppose that all matrices Hk with k > 0 are positive semidefinite and for a given F0 ∈ R, H0 − F0E0 is also positive semidefinite. (Here E0 denote a matrix whose only nonzero entry is the top left corner which contains 1). Then

F(x · y,x · z,y · z) ≥ F0N3. (1.4)

SF(C) :=

(x,y,z)∈C3

In [20] we consider an extension of known semidefinite and linear programming upper bounds for spherical codes and a version of this bound for distance graphs. This paper is a continuation and extension of [20]. We show how the bounds from [20] can be applied to the distance distribution of spherical codes.

In Section 2 for (N,n,T) spherical codes C we present a general 3-point bound, see Theorem 2.2. Actually, this theorem can be considered as a lower bound for Eg(C) (or equivalently for Rg(C), see Theorem 3.1), where g : T → R. We obtain functions g on T ⊂ [−1,1) that can play the same role as a nonnegative linear combination of Gegenbauer polynomials on [−1,1].

In Section 4 we show that this method can work effectively. For T = [−1,0.5] we consider two polynomials g1 and g2 that found using the SDP.

The expansion of the first polynomial in Gegenbauer polynomials has negative coefficients. However, the resulting boundary for it is almost exact and with its help we get a shorter solution to the kissing number problem in dimension 4.

The second polynomial has only positive coefficients, but the SDP bound for it is much stronger than (1.3).

Section 5 contains several possible applications of Theorems 2.2 and 3.1 and their generalizations.

### 2 General bounds for spherical codes

Let C be an N–element subset of the unit sphere Sn−1 ⊂ Rn. Denote I(C) := {t = x · y |x,y ∈ C &x ̸= y}. Let T ⊂ [−1,1). We say that C is an (N,n,T) spherical code if I(C) ⊂ T. Let g be a real function on I(C). Define Eg(C) :=

g(x · y)

(x,y)∈C2,x̸=y

#### 2.1 General 2-point bound

Theorem 2.1. Let C be an (N,n,T) spherical code. Suppose g : T → R, f : [−1,1] → R and f0 ∈ R are such that

- 1. f(t) ≤ g(t) for all t ∈ T.
- 2. Sf(C) ≥ f0N2.


Then

Nf(1) + Eg(C) ≥ f0N2. Proof. Note that for all x ∈ C ⊂ Sn−1 we have x2 = x · x = 1. Then f0N2 ≤ Sf(C) = Nf(1) + Ef(C) ≤ Nf(1) + Eg(C).

| |
|---|


Note that if f is a non-negative linear combination of the Gegenbauer polynomials then (1.2) implies that f satisfies assumption 2 in Theorem 2.1.

Suppose f0 > 0 and g(t) = 0 for all t ∈ T. Since Eg(C) = 0, the theorem yields that

f(1) f0

N ≤

.

This bound is called the linear programming (LP) or Delsarte’s bound for spherical codes. Let q : (0,4] → R be any function. Then for positive semidefinite f and g(t) = q(2 − 2t)

- Theorem 2.1 implies that Every set of N points on Sn−1 has potential energy Eq(C) := Eg(C) at least

f0N2 − Nf(1). This fact first proved by Yudin [24] and has a lot of applications.

2.2 General 3-point bound

The Gram matrix of a set of vectors v1,...,vn in Rd is the matrix of inner products, whose entries are given by the inner product Gij = vi · vj. The Gram matrix is symmetric and positive semidefinite. Moreover, a symmetric matrix M is positive semidefinite if and only if it is the Gram matrix of some vectors v1,...,vn.

Let

M3 =

 

1 u v

- u 1 t
- v t 1


 .

If this matrix is positive semidefinite (M3 ⪰ 0), then there are three distinct points x,y,z in S2 such that t = x · y,u = x · z, and v = y · z. It is easy to see that M3 ⪰ 0 if and only if t,u,v ∈ [−1,1] and det(M3) = 1 + 2tuv − t2 − u2 − v2 ≥ 0.

This fact explains the following definition. D3(T) := (t,u,v) : t,u,v ∈ T &1 + 2tuv − t2 − u2 − v2 ≥ 0 , T ⊂ [−1,1).

- Theorem 2.2. Let C be an (N,n,T) spherical code and F : [−1,1]3 → R be a symmetric function. Suppose f : T → R and g : T → R, are such that


- 1. F(1,t,t) ≤ f(t) for all t ∈ T,
- 2. F(t,u,v) ≤ g(t) + g(u) + g(v) for all (t,u,v) ∈ D3(T).


If SF(C) ≥ F0N3, where F0 ∈ R, then

NF(1,1,1) + 3Ef(C) + (3N − 6)Eg(C) ≥ F0N3. Proof. We have SF(C) = S1 + S2 + S3, where

F(x · y,x · z,y · z),

S1 =

x=y=z

F(x · y,x · z,y · z), H = {(x,y,z) ∈ C3 |x = y ̸= z or x = z ̸= y or x ̸= y = z},

S2 =

(x,y,z)∈H

F(x · y,x · z,y · z).

###### S3 =

x̸=y̸=z̸=x

Since x2 = 1 for all x ∈ C, we have

S1 =

F(x2,x2,x2) = NF(1,1,1),

x∈C

F(1,x · y,x · y) ≤ 3

S2 = 3

x̸=y

(x,y)∈C2,x̸=y

By assumption 2

f(x · y) = 3Ef(C)).

Thus

S3 ≤

(g(x · y) + g(x · z) + g(y · z)) = 3(N − 2)Eg(C).

x̸=y̸=z̸=x

SF(C) ≤ NF(1,1,1) + 3Ef(C) + 3(N − 2)Eg(C).

| |
|---|


- Corollary 2.1. Under the assumptions of Theorem 2.2 let f(t) = p(t)−q(t) with p : T → R and q : [−1,1] → R. If Sq(C) ≥ 0, then

NF(1,1,1) + 3Nq(1) + 3Ep(C) + (3N − 6)Eg(C) ≥ F0N3. Proof.

S2 ≤ 3Ef(C) = 3Ep(C) − 3Eq(C)). Since q(C) = Nq(1) + Eq(C) ≥ 0, we have

S2 ≤ 3Nq(1) + 3Ep(C). Thus

SF(C) ≤ NF(1,1,1) + 3Nq(1) + 3Ep(C) + 3(N − 2)Eg(C).

| |
|---|


- Corollary 2.2. Under the assumptions of Theorem 2.2 let f(t) = B + 2g(t) − q(t) with q : [−1,1] → R. If Sq(C) ≥ 0, then


F(1,1,1) + 3q(1) + 3(N − 1)B + 3Eg(C) ≥ F0N2. Proof.

- S2 ≤ 3Nq(1)+3Ep(C) = 3Nq(1)+3


x̸=y

(B + 2g(x · y)) = 3Nq(1)+3N(N −1)B +6Eg(C).

Then F0N3 ≤ SF(C) ≤ NF(1,1,1) + 3Nq(1) + 3N(N − 1)B + 6Eg(C) + 3(N − 2)Eg(C)

= NF(1,1,1) + 3Nq(1) + 3N(N − 1)B + 3NEg(C). Thus

F(1,1,1) + 3q(1) + 3(N − 1)B + 3Eg(C) ≥ F0N2.

| |
|---|


Note that if (F − F0) and q are positive semidefinite then SF(C) ≥ F0N3 and q(C) ≥ 0. This makes it possible to find new bounds for N and Eg(C) using the SDP. We will look at these methods in more detail in later sections.

Suppose g(t) ≡ 0 and F0 > 0. Then Corollary 2.2 yields

F(1,1,1) + 3q(1) + 3(N − 1)B F0

N2 ≤

.

This inequality as well as Corollary 2.1 with g = 0 first were proposed by Bachoc and Vallentin [1, 2] with further applications and extensions in [3, 10, 15, 16, 18]. In particular, Cohn and Woo [10] got three-point bounds for potential energy minimization.

#### 2.3 General k-point bound

Theorems 2.1 and 2.2 can be extensed for all k: 2 ≤ k ≤ n − 2. Theorem 5.4 from our paper [18] is a particular case of this general theorem.

It is clear how to derive a generalization of Theorem 2.2, see some details in Section 5 [18] and [12]. However, the resulting formulas for k > 3 are quite cumbersome. We decided not to present the general theorem here even for the case k = 4.

### 3 SDP bounds for the distance distribution

Let C be an (N,n,T) spherical code. In the Introduction we defined At(C) and Rf(C). It is clear that A1 = 1, At = 0 for all t ̸= 1 and t ∈/ T,

At = N − 1 and Ef(C) = NRf(C).

t∈T

The following theorem is a restatement of Theorem 2.2 for the distance distribution of spherical codes.

- Theorem 3.1. Let C be an (N,n,T) spherical code and F : [−1,1]3 → R be a symmetric function. Suppose h : T → R and g : T → R, are such that


- 1. h(t) + h0 + F(1,t,t) ≤ 2g(t) for all t ∈ T,
- 2. F(t,u,v) ≤ g(t) + g(u) + g(v) for all (t,u,v) ∈ D3(T).


If SF(C) ≥ F0N3, then

1 3

1 3N

1 N2

1 3

h0 −

At g(t) ≥

F0N +

F(1,1,1) +

Rg(C) =

Eh

t∈T

Corollary 3.1. Under the assumptions of Theorem 3.1 let F0 = 0 and h0 = 1. If Sh(C) ≥ 0 then

N − M 3N

At g(t) ≥ B(N) :=

, M = F(1,1,1) + 3h(1)

Rg(C) =

t∈T

Proof. Since Sh(C) = Nh(1) + Eh(C) ≥ 0, we have Eh(C) ≥ −Nh(1). Thus, Theorem 3.1 yields the inequality.

| |
|---|


### 4 Some applications. A shorter proof of the kissing number problem in four dimensions.

In this section we show that the method discussed in Sections 2 and 3 works effectively. We consider polynomials g1 and g2 found using SDP for the corresponding inequalities on the distribution of distances of spherical codes cannot be found using LP bounds. These polynomial satisfy assumptions of Corollary 3.1 with n = 4 and T = [−1,0.5]. Using g1 and the same method from our paper [17], discarding the most difficult case of five points we get a shorter proof that the kissing number in four dimensions k(4) = 24.

Remark. I would like to note that these polynomials were found by Maria Dostert during our work on the uniqueness problem of the maximum kissing arrangement in dimension 4 [13]. Maria also found several tight polynomials for other intervals. To do this, she had to overcome a large number of technical obstacles and, along the way, develop and improve an algorithm for finding SDP bounds for the distance distribution.

#### 4.1 Two examples.

Let T = [−1,0.5]. In this case we denote a spherical code (N,n,T) by (N,n,π/3). Here we consider the bound given by Corollary 3.1 for (N,4,π/3) spherical codes.

- 1. Let the expansion of g1 in Gegenbauer polynomials G(4)k have the following coefficients: [c0,...,c22]= [-0.5438, -2.0024, -3.8887, -5.6414, -6.7025, -6.8508, -6.0698, -4.6566, -3.0047,


-1.4686, -0.3226, 0.3704, 0.6521, 0.6486, 0.5104, 0.3361, 0.1911, 0.0963, 0.0411, 0.0157, 0.0056, 0.001, 0.0004].

√2/2,1/2]. Fig. 1 shows the graph of g1 with normalization g˜1(−1) = 100. Since there are negative coefficients ck, we

We observe that g1(−1) = 0.02 and g1(t) ≤ 0 for all t ∈ [−

![image 1](<2023-musin-semidefinite-programming-bounds-distance_images/imageFile1.png>)

Figure 1: Graphs of g˜1, g˜2 and p˜4

cannot use the LP (Delsarte) bound. The SDP bound in Corollary 3.1 gives M = M1 := 22.5689.

Let B1(N) := (N − M1)/N. Then B1(25) = 0.0324 and B1(24) = 0.0199.

- 2. The coefficients [c0,...,c22] in the expansion of g2 in G(4)k


= [0.222, 0.8648, 1.8875, 3.1425, 4.5059, 5.7052, 6.5739, 6.9286, 6.7119, 6.0157, 4.9575, 3.7767, 2.6446, 1.6914, 0.9947, 0.5249, 0.2524, 0.1097, 0.0409, 0.0153, 0.0042, 0.001, 0.0002].

We have g2(−1) = 0.02 and g2(t) ≤ 0 for all t ∈ [−0.73,0.5]. Fig. 1 shows the graph of g2 with normalization g˜2(−1) = 100.

This case is very interesting. Note that all coefficients of g2 are positive and therefore we can apply bound (1.3):

(C) ≥ LP(N) := c0N − g2(1) = 0.222N − 57.5714. On the other side the SDP bound in Corollary 3.1 gives

Rg

2

N − M 3N

(C) ≥ B2(N) =

Rg

2

N − 22.6452 3N

=

Then for the most interesting cases N = 24 and N = 25 we have B2(24) = 0.0188 > −52.2431 = LP(24), B2(25) = 0.0314 > −52.0211 = LP(25).

#### 4.2 A shorter proof of the kissing number problem in four dimensions.

- In [17] we proved that k(4) = 24. Let t0 ∈ (−1,−0.5) and f(t) be is a nonnegative combina-


tion of G(4)k with coefficients ck ≥ 0 such that f(t) ≤ 0 for all t ∈ [t0,0.5). From [17, Theorem 1] follows that

1 c0

max{h0,h1,...,hµ,}

k(4) ≤

where µ = A(4,π/3,ψ0), ψ0 = arccos|t0|, and hm is the maximum of Hf(Y ) = f(1) + f(e1,y1) + ... + f(e1,ym) over all configurations of m unit vectors yj in the spherical cap in S3 given by e1 · yj ≤ t0 whose pairwise scalar products are at most 21.

We considered a polynomial p4 (see Fig. 1) with t0 = −0.6058. In this case µ = 6. Technically, the most difficult case turned out to be m=5. This case takes up a significant

part of the proof. We tried to exclude this case and reduce t0. However, numerous experiments with an extended LP bound did not lead to success.

- Theorem 4.1. k(4) = 24


Proof. The 24–cell is an example of a kissing arrangement. Then k(4) ≥ 24. It remains to prove k(4) < 25. Assume the converse: N ≥ 25.

√2/2,1/2], we have t0 = −

Let C be an (25,4,π/3) spherical code. Since g1(t) ≤ 0 for all t ∈ [−

√2/2 and µ = 4. Using the same method as in [17] we consider the cases µ = 0,1,2,3,4 to find the maximum of Rg

(C) = t Atg1(t). This maximum is achieved at µ = 2 and is 0.0266, i.e. Rg

1

(C) < 0.0266. On the other side we have Rg

(C) > B(25) = 0.0324, a contradiction.

1

1

| |
|---|


#### 4.3 New bounds for the distance distribution on a (24,4,π/3) spherical code

Now we consider a maximal kissing arrangement in dimension 4 that is a (24,4,π/3) spherical code. The long-standing open uniqueness conjecture on this code states that this arrangement is isometric to the 24–cell. In fact, the uniqueness conjecture is equivalent to the following

Conjecture. Let C be a (24,4,π/3) spherical code. Then

A−1 = 1, A−1/2 = 8, A0 = 6, A1/2 = 8, At = 0, t ̸= ±1,±1/2,0. (3.1) Note that in this dimension the equality A−1 = 1 yields (3.1), see [7]. Moreover, in [13]

we show that every equality in (3.1) implies all other equalities.

Recently, using Corollaries 1 and 2 from [20] we found several bounds on the distance distribution of a kissing arrangements in four dimensions [13]. For several intervals these bounds are sharp.

Let S ⊂ [−1,0.5]. Denote

A(S) :=

At.

t∈S:At>0

- Theorem 4.2. Let C be a (24,4,π/3) – spherical code. Then A([−1,−0.45]) ≤ 9; A([−1,0.05]) ≤ 15, A([−0.55,0.05]) ≤ 14, A([−0.05,0.5] ≤ 14,


A([−1,−0.73]) ≥ 1, A([0.35,0.5]) ≥ 8

### 5 Concluding Remarks

In conclusion, we outline some applications of Theorems 2.2 and 3.1 and their generalizations.

#### 5.1 Towards a proof of the uniqueness conjecture

We know that k(4) = 24 [17]. However, in dimension 4 the uniqueness of the maximal kissing arrangement is conjectured to be the 24–cell but not yet proven. Equivalently, the uniqueness conjecture is the following:

Denote by sd(n) the optimal SDP bound on k(n) given by (3) with deg(F) = d (see [16]). In the following table it is shown that this minimization problem is a semidefinite program and that every upper bound on sd(4) provides an upper bound for the kissing number in dimension 4.

- • s7(4) < 24.5797 – Bachoc & Vallentin [1];
- • s11(4) < 24.10550859 – Mittelmann & Vallentin [16];
- • s12(4) < 24.09098111 [16];
- • s13(4) < 24.07519774 [16];
- • s14(4) < 24.06628391 [16];
- • s15(4) < 24.062758 – Machado & de Oliveira Filho [15];
- • s16(4) < 24.056903 [15].


This table shows that sd with d > 12 is relatively close to 24, sd − 24 < 2/N = 1/12. We think that our approach which is based on Theorems 2.2 and 3.1 can help to prove the uniqueness conjecture.

#### 5.2 Towards a proof of the 24-cell conjecture

The sphere packing problem asks for the densest packing of Rn with unit balls. In four dimensions, the old conjecture states that a sphere packing is densest when spheres are centered at the points of lattice D4, i.e. the highest density ∆4 is π2/16, or equivalently the highest center density is δ4 = ∆4/B4 = 1/8. For lattice packings, this conjecture was proved by Korkin and Zolatarev in 1872. Currently, for general sphere packings the best known upper bound for δ4 is 0.130587, a slight improvement on the Cohn–Elkies bound of δ4 < 0.13126, but still nowhere near sharp.

In [19] we considered the following conjecture:

The 24–cell conjecture. Consider the Voronoi decomposition of any given packing P of unit spheres in R4. The minimal volume of any cell in the resulting Voronoi decomposition of P is at least as large as the volume of a regular 24–cell circumscribed to a unit sphere.

Note that a proof of the 24-cell conjecture also proves that D4 is the densest sphere packing in 4 dimensions.

In [18, Sect. 4] and [19, 3.3] we considered polynomials Hk that are positive–definite in Rn. Actually, Hk are polynomials that extend the Bachoc–Vallentin polynomials Sk. It is an interesting problem to find generalizations of Theorems 2.2 and 3.1 for sphere packings in Rn. Perhaps, these bounds for n = 4 can help to prove the 24–cell conjecture.

#### 5.3 SDP bounds for Thomson’s and related problems

The objective of the Thomson problem is to determine the minimum electrostatic potential energy configuration of N electrons constrained to the surface of a unit sphere. More generally, a configuration is called h-optimal for a potential interaction h : [−1,1] → R, if it minimizes the h-energy.

The logarithmic potential, Thomson, Newton potential, and more generally the Riesz potential as well as as well as the Gaussian potential have been well studied in the literature [6]. All of these potentials are absolutely monotone potentials. Cohn and Kumar invented universally optimal configurations, namely they minimize the energy for all absolutely monotone potentials h [8].

The regular simplex, the cross polytope and the so-called isotropic spaces are the only known classes of are universally optimal configurations, (see [8, Table 1]). All other known optimal configurations in the literature, even when the interacting potential h is fixed, have particular values of the dimension d and the cardinality N, see the fundamental monograph on this topic [6]. For instance, the Thomson problem is solved only for N ≤ 6 and N = 12.

Note that one of the most powerful tool for lower bounding h-energy is the Delsarte–Yudin linear programming method. This method was applied to most of the configurations in [8, Table 1] to prove that they are universally optimal.

Let a potential h is given. Let g(t) ≤ h(t) on some interval T. Then Theorem 2.2 can be considered as a Yudin type bound the minimum energy. It is a very interesting task to

consider various cases of optimal configurations for known potentials and see what kind of bounds can be obtained using this method.

#### 5.4 SDP bound for contact graphs and the Tammes problem

The following problem was first asked by the Dutch botanist Tammes in 1930: Find the largest angular separation θ of a spherical code C in S2 of cardinality N. In other words, How are N congruent, non-overlapping circles distributed on the sphere when the common radius of the circles is as large as possible?

The Tammes problem is presently solved for only a few values of N: for N = 3,4,6,12 by L. Fejes To´th; for N = 5,7,8,9 by Sch¨utte and van der Waerden; for N = 10,11 by Danzer; for N = 24 by Robinson.; and for N = 13,14 by Musin & Tarasov [21, 22].

The computer-assisted solution of Tammes’ problem for N = 13 and N = 14 consists of three parts: (i) creating the list LN of all planar graphs with N vertices that satisfy the conditions of [22, Proposition 3.1]; (ii) using linear approximations and linear programming to remove from the list LN all graphs that do not satisfy the known geometric properties of the maximal contact graphs [22, Proposition 3.2]; (iii) proving that among the remaining graphs in LN only one is maximal.

In fact, the list LN consists of a huge number of graphs. (For N = 13 it is about 108 graphs.) We think that this paper can help to reduce the number of graphs in LN.

#### 5.5 Generalization of the k–point SDP bound for spherical codes

- In [18] we invented the k–point SDP bound for spherical codes. Note that for k = 2 that is the classical Delsarte bound. The 3–point SDP bound was first considered by Bachoc and Vallentin [1]. Recently, this method with k = 4,5,6 was apply for upper bounds of the maximum number of equiangular lines in n dimensions [12]. It is an interesting problem to find generalizations of results in this paper using the k–point SDP bounds and apply these bounds for s–distance sets and equiangular lines.


Acknowledgments. I am very grateful to Maria Dostert, Alexander Kolpakov and Philippe Moustrou for helpful discussions and useful comments. We spent a lot of time together discussing ideas, algorithms and current results on the uniqueness problem of kissing arrangements. We have encouraging results and I hope that we can complete our paper [13].

### References

- [1] C. Bachoc and F. Vallentin. New upper bounds for kissing numbers from semidefinite programming. J. Amer. Math. Soc., 21(3): 909–924, 2008.


- [2] C. Bachoc and F. Vallentin. Optimality and uniqueness of the (4,10,1/6) spherical code. J. Comb. Theory, Ser. A, 116(1): 195–204, 2009.
- [3] C. Bachoc and F. Vallentin. Semidefinite programming, multivariate orthogonal polynomials, and codes in spherical caps. European J. Combin., 30(3): 625–637, 2009.
- [4] E. Bannai and N. J. A. Sloane. Uniqueness of certain spherical codes, Canadian J. Math., 33: 437–449, 1981.
- [5] A. Barg and O. R. Musin. Codes in spherical caps. Adv. Math. Comm., 1(1): 131–149, 2007.
- [6] S.Borodachov, D.Hardin, E.Saff, Discrete Energy on Rectifiable Sets, Springer Monographs in Mathematics, Springer, 2019.
- [7] P.G. Boyvalenkov. Nonexistence of certain symmetric spherical codes, Designs, Codes and Cryptography, 3, 69–74, 1993.
- [8] H.Cohn and A.Kumar, Universally optimal distribution of points on spheres, J. of AMS, 20 (2007), 99–148.
- [9] H.Cohn, D. de Laat, A. Salmon, Three–point bounds for sphere packing, preprint, arXiv:2206.15373
- [10] H. Cohn and J. Woo. Three–point bounds for energy minimization. J. Amer. Math. Soc., 25: 929–958, 2012.
- [11] J.H. Conway and N.J.A. Sloane, Sphere Packings, Lattices, and Groups, New York, Springer-Verlag, 1999 (Third Edition).
- [12] D. de Laat, F.C. Machado, F. M. de Oliveira Filho and F. Vallentin. k–point semidefinite programming bound for equiangular lines, Math. Program. 194, 533–567, 2022.
- [13] M. Dostert, A. Kolpakov, P. Moustrou, and O. R. Musin. Uniqueness of spherical codes via SDP, in preparation.
- [14] V.I. Levenshtein, On bounds for packing in n-dimensional Euclidean space, Sov. Math. Dokl. 20 (2): 417–421, 1979.
- [15] F. C. Machado and F. M. de Oliveira Filho. Improving the semidefinite programming bound for the kissing number by exploiting polynomial symmetry, Experimental Math., 27: 362–369, 2018.
- [16] H. D. Mittelmann and F. Vallentin, High-accuracy semidefinite programming bounds for kissing numbers, Experimental Math., 9: 175–179, 2010.
- [17] O. R. Musin. The kissing number in four dimensions. Ann. of Math., 168: 1–32, 2008.


- [18] O. R. Musin, Multivariate positive definite functions on spheres, in: Discrete Geometry and Algebraic Combinatorics, AMS Series: Contemporary Mathematics, 625: 177–190, 2014.
- [19] O. R. Musin. Towards a proof of the 24-cell conjecture, Acta Math. Hungar., 155(1): 184–199, 2018.
- [20] O. R. Musin. An extension the semidefinite programming bound for spherical codes. preprint, arXiv:1903.05767
- [21] O. R. Musin and A. S. Tarasov. The strong thirteen spheres problem. Discrete Comput. Geom., 48(1): 128–141, 2012.
- [22] O. R. Musin and A. S. Tarasov, The Tammes problem for N=14. Experimental Math., 24: 460–468, 2015.
- [23] A.M. Odlyzko and N.J.A. Sloane, New bounds on the number of unit spheres that can touch a unit sphere in n dimensions, J. of Combinatorial Theory A 26: 210–214, 1979.
- [24] V.A. Yudin, Minimal potential energy of a point system of charges. Discret. Mat. 4, 115–121 (1992) (in Russian). English translation: Discr. Math. Appl., 3, 75–81 (1993)


O. R. Musin, School of Mathematical and Statistical Sciences, University of Texas Rio Grande Valley, One West University Boulevard, Brownsville, TX, 78520.

E-mail address: oleg.musin@utrgv.edu

