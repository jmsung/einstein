arXiv:1607.06010v2[math.AG]17Mar2017

A POSITIVSTELLENSATZ FOR SUMS OF NONNEGATIVE CIRCUIT POLYNOMIALS

MAREIKE DRESSLER, SADIK ILIMAN, AND TIMO DE WOLFF

Abstract. Recently, the second and the third author developed sums of nonnegative circuit polynomials (SONC) as a new certiﬁcate of nonnegativity for real polynomials, which is independent of sums of squares.

In this article we show that the SONC cone is full-dimensional in the cone of nonnegative polynomials. We establish a Positivstellensatz which guarantees that every polynomial which is positive on a given compact, semi-algebraic set can be represented by the constraints of the set and SONC polynomials. Based on this Positivstellensatz we provide a hierarchy of lower bounds converging against the minimum of a polynomial on a given compact set K. Moreover, we show that these new bounds can be computed eﬃciently via interior point methods using results about relative entropy functions.

1. Introduction

In this article we present a Positivstellensatz based on sums of nonnegative circuit polynomials providing an entirely new way to certify nonnegativity of polynomials on an arbitrary compact, semi-algebraic set. This Positivstellensatz yields a converging hierarchy of lower bounds for solving arbitrary constrained polynomial optimization problems on compact sets. We show that these bounds can be computed eﬃciently via relative entropy programming. Particularly, all results are independent of sums of squares and semideﬁnite programming.

Let f, g1, . . ., gs be elements of the polynomial ring R[x] = R[x1, . . ., xn] and let K = {x ∈ Rn : gi(x) ≥ 0, i = 1, . . ., s}

be a basic closed semi-algebraic set deﬁned by g1, . . ., gs. We consider the constrained polynomial optimization problem

fK∗ = inf

f(x). For K = Rn we write f∗ for fR∗n and talk about a global (polynomial) optimization problem.

x∈K

Constrained polynomial optimization problems are well-known to be NP-hard in general [DG14]. However, they have a wide range of applications like dynamical systems, robotics, control theory, computer vision, signal processing, and economics ; see, e.g., [BPT13, Las10].

![image 1](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile1.png>)

2010 Mathematics Subject Classiﬁcation. Primary: 14P10, 90C25; Secondary: 12D05, 52B20. Key words and phrases. Certiﬁcate, converging hierarchy, nonnegative polynomial, Positivstellensatz,

relative entropy programming, semideﬁnite programming, sum of nonnegative circuit polynomials, sum of squares.

1

The standard approach for the computation of fK∗ is Lasserre relaxation [Las01], which approximates nonnegative polynomials via sum of squares (SOS) polynomials and semideﬁnite programming (SDP); for further details see [BPT13, Lau09].

Recently, the second and the third author developed new nonnegativity certiﬁcates independent of SOS [IdW16], which are based on circuit polynomials, see Deﬁnition 2.2. For large classes of polynomials one can check membership in the convex cone of sums of nonnegative circuit polynomials via geometric programming (GP), a special type of convex optimization problems; see e.g. [BKVH07, BV04]. This is in direct analogy to the relation between SOS and SDP.

Using Lasserre relaxation, the corresponding semideﬁnite programs quickly get very large in size, which often is an issue for problems with high degrees or many variables. The SONC/GP based approach allows a signiﬁcantly faster computation of lower bounds than their counterparts in semideﬁnite programming for all classes of polynomials which have been investigated so far; see [DIdW16, Sections 4 and 5], [GM12, Tables 1-3, Page 470] and [IdW16, Section 4.1]. In several cases the new bounds are also better than the optimal bounds based on SOS and SDP; see [IdW16, Corollary 3.6]. However, the authors derive a lower bound for fK∗ by using only a single geometric optimization program. In this article, we extend this approach by developing a hierarchy of lower bounds, which converge to the optimal value of the polynomial optimization problem.

A necessary condition to establish SONC polynomials as a certiﬁcate, which is useful in practice, is to show that the convex cone of SONC polynomials is always full-dimensional in the convex cone of nonnegative polynomials. We show this in Theorem 4.3. Moreover, we present a new Positivstellensatz for sums of nonnegative circuit polynomials; see Theorem 4.8. The following statement is a rough version.

- Theorem 1.1 (Positivstellensatz for SONC polynomials; rough version). Let f ∈ R[x] be a real polynomial which is strictly positive on a given compact, basic closed semi-algebraic set K deﬁned by polynomials g1, . . ., gs ∈ R[x]. Then there exists an explicit representation of f as a sum of products of the gi’s and SONC polynomials.


The proof is based on methods from classical real algebraic geometry, which had been used very similarly by Chandrasekaran and Shah for sums of arithmetic geometric exponentials (SAGE); see [CS16]. We discuss the relation between the SAGE and the SONC cone in more detail in Section 3.

Our Positivstellensatz yields a hierarchy of lower bounds fsonc(d,q) for fK∗ based on the maximal allowed degree of the representing polynomials in the Positivstellensatz. We show in Theorem 5.2 that the bounds fsonc(d,q) converge against fK∗ for d, q → ∞.

Finally, we provide in (5.3) an optimization program for the computation of fsonc(d,q). We prove in Theorem 5.3 that our program (5.3) is a relative entropy program (REP), a convex optimization program, which is more general than a geometric program, but still eﬃciently solvable via interior point methods; see [CS15, NN94].

2. Preliminaries

In this section we recall key results about sums of nonnegative circuit polynomials (SONC), sums of arithmetic geometric exponentials (SAGE), geometric programming (GP), and relative entropy programing (REP), which are used in this article.

- 2.1. The Cone of Sums of Nonnegative Circuit Polynomials. We denote vectors in bold notation in general. Let R[x] = R[x1, . . ., xn] be the ring of real n-variate polynomials, R∗ = R\{0}, and N∗ = N\{0}. Let δij be the ij-Kronecker symbol, ei = (δi1, . . ., δin) be the i-th standard vector, and A ⊂ Nn be a ﬁnite set. We denote by conv(A) the convex hull of A, by V (conv(A)) its vertex set, and by V (A) the vertices of the convex hull of A. We consider polynomials f ∈ R[x] supported on A. Thus, f is of the form


f(x) = α∈A fαxα with fα ∈ R, xα = xα

1 · · ·xα

n . We call a lattice point even if it is in (2N)n. We deﬁne the Newton polytope of f as New(f) = conv{α ∈ Nn : fα = 0}. Furthermore, we denote by ∆n,2d the standard simplex in n variables of edge length 2d, i.e. the simplex satisfying V (∆n,2d) = {0, 2d·e1, . . ., 2d·en} and we deﬁne Ln,2d = ∆n,2d ∩Zn as the set of all integer points in ∆n,2d.

1

n

A polynomial is nonnegative on the entire Rn only if the following necessary conditions are satisﬁed; see e.g. [Rez78].

- Proposition 2.1. Let A ⊂ Nn be a ﬁnite set and f ∈ R[x] be supported on A such that New(f) = conv(A). Then f is nonnegative on Rn only if:


- (1) All elements of V (A) are even.
- (2) If α ∈ V (A), then the corresponding coeﬃcient fα is strictly positive.


In other words, if α ∈ V (A), then the term fαxα has to be a monomial square. We deﬁne the class of circuit polynomials as follows; see also [dW15, IdW16].

Deﬁnition 2.2. Let f ∈ R[x] be supported on A ⊂ Nn such that all elements of V (A) are even. Then f is called a circuit polynomial if it of the form

r

- (2.1) fα(j)xα(j) + fβxβ,


f(x) =

j=0

with r ≤ n, exponents α(j), β ∈ A, and coeﬃcients fα(j) ∈ R>0, fβ ∈ R, such that the following conditions hold:

(C1): The points α(0), α(1), . . ., α(r) are aﬃnely independent and equal V (A). (C2): The exponent β can be written uniquely as

β =

r

λjα(j) with λj > 0 and

j=0

r

λj = 1

j=0

in barycentric coordinates λj relative to the vertices α(j) with j = 0, . . ., r.

We call the terms fα(0)xα(0), . . ., fα(r)xα(r) the outer terms and fβxβ the inner term of f. We denote the set of all circuit polynomials with support A by CircA.

For every circuit polynomial we deﬁne the corresponding circuit number as

r

λj

fα(j) λj

- (2.2) .


Θf =

![image 2](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile2.png>)

j=0

Condition (C1) implies that V (A) = {α(0), . . ., α(r)} is the vertex set of an r-dimensional simplex, which coincides with New(f) = conv(A). In this case we say that New(f) is a simplex Newton polytope. Note that, by [IdW16, Lemma 3.7], we assume w.l.o.g. that β ∈ int(New(f)).

The terms “circuit polynomial” and “circuit number” are chosen since β and the α(j) form a circuit; this is a minimally aﬃne dependent set; see e.g. [GKZ94].

A fundamental fact is that nonnegativity of a circuit polynomial f can be decided easily via its circuit number Θf alone.

- Theorem 2.3 ([IdW16], Theorem 3.8). Let f be a circuit polynomial with inner term fβxβ and let Θf be the corresponding circuit number, as deﬁned in (2.2). Then the following are equivalent:


- (1) f is nonnegative.
- (2) |fβ| ≤ Θf and β  ∈ (2N)n or fβ ≥ −Θf and β ∈ (2N)n.


Note that (2) can be stated equivalently as: |fβ| ≤ Θf or f is a sum of monomial squares. Writing a polynomial as a sum of nonnegative circuit polynomials is a certiﬁcate of nonnegativity. We denote by SONC both the class of polynomials that are sums of nonnegative circuit polynomials and the property of a polynomial to be in this class. In what follows let Pn,2d be the cone of nonnegative polynomials of degree 2d and let Σn,2d denote the cone of n-variate sums of squares of degree 2d.

Deﬁnition 2.4. We deﬁne for every n, d ∈ N∗ the set of sums of nonnegative circuit polynomials (SONC) in n variables of degree 2d as

Cn,2d = f ∈ R[x] : f =

k

µipi, µi ≥ 0, pi ∈ CircA ∩Pn,2d, A ⊆ Ln,2d, k ∈ N∗ .

i=1

Indeed, SONC polynomials form a convex cone independent of the SOS cone. Theorem 2.5 ([IdW16], Proposition 7.2). Cn,2d is a convex cone satisfying:

- (1) Cn,2d ⊆ Pn,2d for all n, d ∈ N∗,
- (2) Cn,2d ⊆ Σn,2d if and only if (n, 2d) ∈ {(1, 2d), (n, 2), (2, 4)},
- (3) Σn,2d  ⊆ Cn,2d for all (n, 2d) with 2d ≥ 6.


For further details about the SONC cone see [dW15, IdW16].

- 2.2. Relative Entropy and the SAGE Cone. There exists an important concept related to the SONC cone, which was introduced by Chandrasekaran and Shah in [CS16], namely the cone of sums of arithmetic geometric exponentials (SAGE). In what follows, we introduce relative entropy programs and the SAGE cone. Later, in Section 3, we discuss its relationship to SONC polynomials and how we can use relative entropy programming for our results.


We denote by  ·, ·  the standard inner product. Following [CS16], a signomial is a sum of exponentials

f(x) =

l

fα(j)e α(j),x

j=0

with fα(j) ∈ R, x ∈ Rn and real vectors α(0), . . ., α(l) ∈ Rn. A signomial with at most one negative coeﬃcient is called an AM/GM-exponential. Thus, an AM/GM-exponential has the following form

f(x) =

l

fα(j)e α(j),x + fβ · e β,x ,

j=0

where fβ ∈ R, fα(j) ∈ R>0 and β, α(j) ∈ Rn for j = 0, . . ., l. Note that l > n is possible.

As shown in [CS16], testing whether an AM/GM-exponential is nonnegative is possible via the relative entropy function. This function is deﬁned as follows for ν = (ν0, . . ., νl) and ζ = (ζ0, . . ., ζl) in the nonnegative orthant Rl≥+10 :

D(ν, ζ) =

l

νj log

j=0

νj ζj

![image 3](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile3.png>)

.

= 0 for any ζj ∈ R≥0 and νj log ν0j = 0 if νj = 0 and

By convention, we deﬁne 0 log ζ0

![image 4](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile4.png>)

![image 5](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile5.png>)

j

νj log ν0j = ∞ if νj > 0. Let furthermore fα = (fα(0), . . ., fα(l)) ∈ Rl>+10 . Then the following lemma holds.

![image 6](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile6.png>)

Lemma 2.6 ([CS16], Lemma 2.2). Let f(x) be an AM/GM-exponential. Then f(x) is nonnegative for all x ∈ Rn if and only if there exists a ν ∈ Rl≥+10 satisfying the conditions

- (2.3) D(ν, efα) − fβ ≤ 0 , Qν = 1, ν β with Q = (α(0) · · ·α(l)) ∈ Rn×(l+1).


Checking whether such a ν ∈ Rl≥+10 exists is a convex optimization problem by means of the joint convexity of the relative entropy function D(ν, ζ). More speciﬁcally, the corresponding problem is a relative entropy program; see [CS15].

Deﬁnition 2.7. Let ν, ζ ∈ Rl≥+10 and δ ∈ Rl+1. A relative entropy program (REP) is of the form:

 

minimize p0(ν, ζ, δ), subject to:

- (1) pi(ν, ζ, δ) ≤ 1 for all i = 1, . . ., m,
- (2) νj log νζj


- (2.4)




≤ δj for all j = 0, . . ., l,

![image 7](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile7.png>)

j

where p0, . . ., pm are linear functionals and the constraints (2) are jointly convex functions in ν, ζ, and δ deﬁning the relative entropy cone.

Relative entropy programs are convex and can be solved eﬃciently via interior-point methods [NN94]. Geometric programs, a prominent class of convex optimization programs [BKVH07, BV04, DPZ67], comprise a subclass of relative entropy programs; see [CS15] for further information.

If a signomial consists of more than one negative term, then a natural and suﬃcient condition for certifying nonnegativity is to express the signomial as a sum of nonnegative AM/GM-exponentials. For a ﬁnite set of exponents M ⊂ Rn, one denotes by

SAGE(M) = f =

m

fi :

i=1

every fi is a nonnegative AM/GM-exponential with exponents in M

the set of sums of nonnegative AM/GM-exponentials (SAGE) with respect to M; see [CS16].

- 2.3. Signomials and Polynomials. The connection between signomials and polynomials is given by the bijective componentwise exponential function


exp : Rn → Rn>0, (x1, . . ., xn)  → (ex

, . . ., ex

). Via this mapping a signomial

1

n

f(x) =

l

fα(j)e α(j),x

j=0

is transformed into

f(x) =

l

fα(j)xα(j),

j=0

which is a polynomial if α(0), . . ., α(l) ∈ Nn. Hence, checking nonnegativity of such signomials corresponds to checking nonnegativity of a polynomial on the positive orthant. Note that is suﬃcient to consider the positive orthant to certify nonnegativity, since the positive orthant is dense in the nonnegative orthant. We call such a polynomial f(x) = lj=0 fα(j)xα(j) a SAGE polynomial, and we call it an AM/GM-polynomial if it has at most one negative coeﬃcient.

3. A Comparison of SAGE and SONC The concept of SAGE polynomials explicitly addresses the question of nonnegativity

of polynomials on Rn>0. However, the second and third author showed already before the development of the SAGE class that for circuit polynomials global nonnegativity coin-

cides with nonnegativity on Rn>0 assuming that its inner term is negative; see [IdW16, particularly Section 3.1]. This fact was, next to the circuit number, the key motivation to consider the class of circuit polynomials. Hence, in what follows we can use results from the analysis of the SAGE cone applied to circuit polynomials as a certiﬁcate for global nonnegativity rather than just nonnegativity on Rn>0.

- Let f(x) = rj=0 fα(j)xα(j) + fβxβ be a circuit polynomial which is not a sum of


monomial squares. We can assume without loss of generality that fβ < 0 after a possible transformation of variables xj  → −xj. In this case, we have

- (3.1) f(x) ≥ 0 for all x ∈ Rn ⇐⇒ f(x) ≥ 0 for all x ∈ Rn>0;

see [IdW16, Section 3.1]. Using this fact, we can explicitly characterize the corresponding AM/GM-exponential coming from a circuit polynomial under the exp-map. We call this a simplicial AM/GM-exponential.

Proposition 3.1. Let f be a nonnegative simplicial AM/GM-exponential with interior point β. Then (2.3) is always satisﬁed for the probability measure νj = λj for j = 0, . . ., r where λj is the j-th coeﬃcient in the convex combination of the interior point β ∈ Nn with respect to the vertices α(0), . . ., α(r) ∈ (2N)n.

Proof. By (3.1) it is suﬃcient to investigate circuit polynomials. The proof follows from

- Theorem 2.3 where nonnegativity of circuit polynomials is explicitly characterized via the circuit number and hence by the convex combination of the interior point β in terms of


the vertices α(0), . . ., α(r). The coeﬃcients λ0, . . ., λr in the convex combination form a probability measure by deﬁnition.

The circuit number is deﬁned via barycentric coordinates; see Section 2.1. This parametrization for nonnegativity corresponds to the geometric programming literature; see [CS16, (2.2), Page 1151] and also [DPZ67]:

- (3.2) D(ν, fα) + log(−fβ) ≤ 0, ν ∈ Rl≥+10 , Qν = β, 1, ν = 1.


Note that we assume fβ < 0 here. Chandrasekaran and Shah showed that the conditions (2.3) and (3.2) are equivalent (this is non-obvious); see [CS16]. However, they also point out in [CS16] that restricting ν to a probability measure as in (3.2) comes with the drawback that the parametrization in (3.2) is not jointly convex in ν, fα, and fβ. This is in sharp contrast to the parametrization (2.3), which is jointly convex in ν, fα, and fβ and yields a convex relative entropy program, which can be solved eﬃciently. Thus, the chosen parametrization has a signiﬁcant impact from the perspective of optimization.

However, while this fact is a serious problem for arbitrary AM/GM-exponentials, it turns out that this problem is much simpler for circuit polynomials and the corresponding simplicial AM/GM-exponentials as we show in what follows.

For a simplicial AM/GM-exponential we have that l = r in (2.3). Moreover, since the support is a circuit, Q is a full-rank matrix. Thus, ν is unique up to a scalar multiple. By the deﬁnition of circuit polynomials, Deﬁnition 2.2, we know that the barycentric coordinates (λ0, . . ., λr) of β with respect to the vertices α(0), . . ., α(r) of New(f) are the unique solution of (3.2). It follows that the barycentric coordinates (λ0, . . ., λr) are also a solution of (2.3). Hence, we obtain for every solution ν that ν = d·(λ0, . . ., λr) for some d ∈ R∗. We can now conclude the following theorem.

- Theorem 3.2. Let f(x) = rj=0 fα(j)xα(j) + fβxβ be a circuit polynomial, which is not a sum of monomial squares. Then f(x) is nonnegative on Rn if and only if a particular


relative entropy program is feasible, which is jointly convex in ν, the fα(j), |fβ|, and an additional vector δ ∈ Rr+1.

Note that the question whether a given f(x) is a sum of monomial squares is computationally trivial such that these circuit polynomials can safely be excluded. Proof. By Theorem 2.3 we know that the circuit polynomial f(x) is nonnegative if and only if |fβ| ≤ Θf.

r

λj fα(j)

|fβ| ≤ Θf ⇔ |fβ| ·

![image 8](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile8.png>)

j=0

r

|fβ| · λj fα(j)

⇔

![image 9](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile9.png>)

j=0

λj

≤ 1 ⇔

r

j=0

|fβ| · λj fα(j)

![image 10](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile10.png>)

|fβ|·λj

≤ 1|f

β| = 1

λj

≤ 1

r

|fβ| · λj fα(j)

⇔

|fβ| · λj · log

≤ 0

![image 11](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile11.png>)

j=0

 

minimize 1

- (1) νj = |fβ| · λj for all j = 0, . . ., r,
- (2) νj · log f νj

![image 12](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile12.png>)

α(j)

≤ δj for all j = 0, . . ., r,

- (3) rj=0 δj ≤ 0.


⇔

subject to:



Note that |fβ| is redundant in the REP given in the proof of Theorem 3.2 since one can leave out the constraint (1) e.g. for j = 0 and replace |fβ| by ν0/λ0.

There exists another important diﬀerence between SAGE and SONC next to the char-

acterization of nonnegativity on Rn>0 (SAGE) and nonnegativity on Rn (SONC). In the SONC cone we decompose a polynomial f in a sum of nonnegative circuit polynomials

- fi with simplex Newton polytopes. However, in SAGE we decompose a polynomial f in a sum of nonnegative AM/GM-polynomials fi such that the Newton polytopes of the fi are not simplices in general and the supports of the fi have several points in the interior of New(fi) in general. If a polynomial f can be decomposed in SAGE, then this certiﬁes


Figure 1. The set S4 is shown in the green area.

nonnegativity of f on Rn>0, but not globally on Rn. Stated in other words, the SAGE cone approximates the nonnegativity cone from the outside, while the SONC cone approximates the nonnegativity cone from the inside. However, as we showed, circuit polynomials are special since they are nonnegative on Rn if and only if they are nonnegative on Rn>0.

In the following example, which was discussed by Chandrasekaran and Shah, we demonstrate how our explicit characterization of circuit polynomials yields an explicit convex, semi-algebraic description for special nonnegativity sets compared to SDP methods.

Example 3.3 ([CS16], page 1167). Let Sd = {(a, b) ∈ R2 : x2d + ax2 + b ≥ 0}.

The set Sd is a convex, semi-algebraic set for each d ∈ N∗. Since a univariate polynomial is nonnegative if and only if it is a sum of squares, Sd is also SDP representable, i.e., a projection of a slice of the cone of quadratic, positive semideﬁnite matrices of some size

- wd ∈ N∗. As noted in [CS16], the algebraic degree of the boundary of Sd grows with d and hence the size wd of the smallest SDP description of Sd must also grow with d. In [CS16], the authors use the corresponding relative entropy description (2.3) of Sd (note that here nonnegativity on R is the same as nonnegativity on R>0):


Sd = {(a, b) ∈ R × R≥0 : ∃ν ∈ R2≥0 such that D(ν, e · (1, b)T) ≤ a, (d − 1)ν1 = ν2}.

A major advantage of this description over the SDP method is that the size of Sd does not grow with d. However, we can do even better and use circuit polynomials and our

Theorem 2.3 to describe the convex, semi-algebraic set Sd directly:

1

Sd = (a, b) ∈ R × R≥0 : a + (d)

d ·

![image 13](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile13.png>)

d · b d − 1

![image 14](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile14.png>)

d−1 d

![image 15](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile15.png>)

≥ 0 .

For d = 4 the set S4 is given as the green area in Figure 1.

4. The Positivstellensatz using SONC

In this section we analyze the SONC cone Cn,2d and prove that Cn,2d is full-dimensional in the nonnegativity cone Pn,2d for every n and d; see Theorem 4.3. In the second part of this section we formulate and prove our Positivstellensatz for sums of nonnegative circuit polynomials; see Theorem 4.8.

- 4.1. Analyzing the SONC Cone. The following property of SONC polynomials stands in strong contrast to SOS polynomials. Lemma 4.1. For every n, d ∈ N∗ there exists f, g ∈ Cn,2d such that f · g ∈/ Cn,4d.


Proof. A circuit polynomial in Cn,2d has at most 2n aﬃne real zeros in (R∗)n, which is a sharp bound for every d ∈ N∗; see [IdW16, Corollary 3.9]. Thus, the same holds for a SONC polynomial since it is a sum of nonnegative circuit polynomials. More precisely, if we choose a circuit polynomial f(x) = λ0 + nj=1 fjx2jd + fβxβ ∈ ∂ Cn,2d such that New(f) = ∆n,2d, then every entry vj of every zero v ∈ Rn of f satisﬁes |vj| = (λj/fj)1/(2d). Then f(x) is nonnegative and has exactly 2n aﬃne zeros in (R∗)n if fβ = −Θf and β ∈ (2N)n. Therefore, for such a given f(x) we can construct a new nonnegative circuit polynomial g(x) with 2n diﬀerent aﬃne zeros in (R∗)n by changing every fj by a small εj ∈ R and adjusting fβ to the new circuit number −Θg; see (2.2). The product f(x)·g(x), a product of two SONC polynomials, is a polynomial with 2n+2n = 2n+1 aﬃne real zeros in (R∗)n and of degree at most 4d. Consequently, this product cannot be a SONC polynomial in Cn,4d.

An immediate consequence of this lemma is the following statement: Corollary 4.2. Not every square of a polynomial is a SONC polynomial.

These observations imply that SONC polynomials neither form a preordering nor a quadratic module; see [Mar08] for the formal deﬁnitions. Hence, we cannot expect to exploit several of the classical techniques from real algebraic geometry in order to derive a Putinar like Positivstellensatz, since these techniques rely heavily on the fact that sums of squares form both a preordering and a quadratic module. However, this does not contradict the possibility to derive a similar result or even the exact equivalent of Putinar’s Positivstellensatz for SONC polynomials. We address this topic again in the resume in Section 6.

- Theorem 4.3. Let n, d ∈ N∗. Then the SONC cone Cn,2d is full-dimensional in the cone of nonnegative polynomials Pn,2d.


Proof. To prove the theorem it is suﬃcient to provide a single polynomial f ∈ Cn,2d such that for every g ∈ Pn,2d there exists a suﬃciently small ε > 0 such that we have f + εg ∈ Cn,2d. We choose f as follows: Let New(f) = ∆n,2d be the standard simplex with edge length 2d, i.e. V (New(f)) = {0, 2d · e1, . . ., 2d · en}. Moreover, assume that f has full support, i.e. supp(f) = Ln,2d. Since f is a SONC polynomial, we can write f as a

sum of nonnegative circuit polynomials f1, . . ., fs such that for every j = 1, . . ., s it holds that

rj

fj,ix2id − fβ(j)xβ(j),

fj(x) = fj,0 +

i=1

rj ≤ n. Furthermore, we assume that every fj is in the interior of Cn,2d, i.e. |fβ(j)| < Θ(fj). Thus, f is in the interior of Cn,2d, too. Let

δ = min

- (4.1) Θ(fj) − |fβ(j)| > 0.

Let g(x) = α∈L

n,2d

gαxα ∈ Pn,2d be arbitrary. By Proposition 2.1 we have g0 ≥ 0 and g2d·e

i

≥ 0 for i = 1, . . ., n. For a given δ we choose ε = min

α∈Ln,2d\V (New(f)), gα =0

δ 2 · |gα|

![image 16](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile16.png>)

- (4.2) > 0.

Since f has full support and every fj has exactly one inner term and satisﬁes V (New(fj)) ⊆ V (New(f)) = V (∆n,2d), the exponent α ∈ Ln,2d \ {0, 2d · e1, . . ., 2d · en} of a term in g equals the exponent β(j) of an inner term of exactly one nonnegative circuit polynomial fj. Thus, it holds that

f(x) + ε · g(x) =

s

j=1

fj(x) + ε · gβ(j)xβ(j) + ε · g0 +

n

i=1

g2d·e

i

- (4.3) · x2id


1≤j≤s

for a suitable matching of the gα’s of g(x) and the gβ(j)’s. For every j = 1, . . ., s we have

n

ε s

· x2id

fj(x) + ε · gβ(j)xβ(j) +

· g0 +

g2d·e

![image 17](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile17.png>)

i

i=1

n

ε s

ε s

x2id − (fβ(j) − ε · gβ(j))xβ(j)

= fj,0 +

· g0 +

fj,i +

· g2d·e

![image 18](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile18.png>)

![image 19](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile19.png>)

i

i=1

n

fj,ix2id − (fβ(j) − ε · gβ(j))xβ(j).

≥ fj,0 +

i=1

Every polynomial fj,0 + ni=1 fj,ix2id − (fβ(j) − ε · gβ(j))xβ(j) is a circuit polynomial. Hence, we can conclude that it is nonnegative if we show that the norm of the coeﬃcient of its inner term is bounded by the corresponding circuit number. This is the case since

|fβ(j) − ε · gβ(j)|

(4.2)

≤ fβ(j) + min

α∈Ln,2d\V (New(f)), gα =0

δ 2

≤ fβ(j) +

![image 20](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile20.png>)

(4.1)

< Θ(fj).

δ 2 · |gα|

![image 21](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile21.png>)

· |gβ(j)|

Thus, for every j = 1, . . ., s we conclude that fj(x)+εgβ(j)xβ(j)+εs· g0 + ni=1 g2d·e

x2id is a nonnegative circuit polynomial. Hence, by (4.3), it follows that f + ε · g ∈ Cn,2d.

![image 22](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile22.png>)

i

- 4.2. Formulation and Proof of the Positivstellensatz. In this section we formulate and prove our Positivstellensatz for sums of nonnegative circuit polynomials.


First, we give some basic deﬁnitions and recall a representation theorem from real algebraic geometry, which we need to prove our Positivstellensatz. We use Marshall’s book [Mar08] as a general source making some very minor adjustments.

Deﬁnition 4.4. A preprime P is a subset of R[x] that contains R≥0, and that is closed under addition and multiplication. A preprime P is called Archimedean if for every f ∈ R[x] there exists an integer N ≥ 1 such that N − f ∈ P.

Let P be a preprime. We deﬁne the corresponding ring of P-bounded elements of R[x] as follows:

HP = {f ∈ R[x] : there exists an integer N ≥ 1 such that N ± f ∈ P}.

The set HP is an indicator how close a given preprime P is to being Archimedean. In particular, a preprime P is Archimedean if and only if HP = R[x].

Note that HP is actually a ring [Mar08, Proposition 5.1.3, (1)], which immediately implies the following lemma; see e.g. [Sch09].

- Lemma 4.5. Let P ⊆ R[x] be a preprime. Then the following are equivalent:


- (1) P is Archimedean.
- (2) There exists an integer N ≥ 1 such that N ± xi ∈ P for all i = 1, . . ., n.


For convenience of the reader, we give a proof here. Proof. Implication (1) ⇒ (2) is clear. Let f, g ∈ R[x] with N ± f ∈ P and M ± g ∈ P

for some N, M ∈ N∗, so f and g are P-bounded elements. Since P is closed under addition and multiplication we have

(N ± f) + (M ± g) = (N + M) ± (f + g) ∈ P , and

- 1

![image 23](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile23.png>)

- 2


((N ± f) · (M − g) + (N ± f) · (M + g)) = N · M ± f · g ∈ P .

This means, products and sums of P-bounded elements are P-bounded; in fact HP is a subring of R[x]. By assumption (2) the variables xi are P-bounded elements and therefore every polynomial expression in the variables xi is also P-bounded. Thus, P is Archimedean.

Given f1, . . ., fs ∈ R[x] we denote by Prep(f1, . . ., fs) the preprime generated by the

- f1, . . ., fs, i.e., the set of ﬁnite sums of elements in R[x] of the form aifi


1 · · ·fi

s , where i = (i1, . . ., is) ∈ Ns and ai ∈ R≥0:

1

s

aifi

1 · · ·fi

s : i ∈ Ns, ai ∈ R≥0 .

Prep(f1, . . ., fs) =

1

s

ﬁnite

The ﬁnal algebraic structure, which we need to formulate the statements in this section, is a module over a preprime:

Deﬁnition 4.6. Let P ⊆ R[x] be a preprime. Then M ⊆ R[x] is a P-module if it is closed under addition, closed under multiplication by an element of P, and if it contains 1. Analogous to preprimes, a P-module M is Archimedean if for each f ∈ R[x] there exists an integer N ≥ 1 such that N − f ∈ M.

Note that 1 ∈ M for a P-module M implies that P ⊆ M. Obviously, P itself is a P-module.

Now, we state the theorem, which provides the foundation for the proof of our Positivstellensatz. There exist various diﬀerent variations of this statement. E.g., one prominent version is by Krivine [Kri64a, Kri64b]. We follow Marshall’s book where the reader can ﬁnd an overview about the diﬀerent versions; see [Mar08, page 79].

- Theorem 4.7 ([Mar08], Theorem 5.4.4). Let P ⊆ R[x] be an Archimedean preprime and


let M be an Archimedean P-module. Let KM denote the semi-algebraic set of points in Rn on which every element of M is nonnegative:

KM = {x ∈ Rn : g(x) ≥ 0 for all g ∈ M}. Let f ∈ R[x]. If f(x) > 0 for all x ∈ KM, then f ∈ M.

Note that if a preprime P is Archimedean, then every P-module M is also Archimedean since P ⊆ M.

Let f, g1, . . ., gs be elements of the polynomial ring R[x] and let K = {x ∈ Rn : gi(x) ≥ 0, i = 1, . . ., s}

be the basic closed semi-algebraic set given by the gi’s. We consider the constrained polynomial optimization problem

fK∗ = inf

f(x). In what follows we have to assume that K is compact. Namely, in order to use Theorem

x∈K

- 4.7, we need the involved preprime to be Archimedean. We ensure this by enlarging the deﬁnition of K by the 2n many redundant constraints N ±xi ≥ 0 with N ∈ N suﬃciently large. We denote these constraints by lj(x) for j = 1, . . ., 2n. Geometrically spoken, we know that if K is a compact set, then it is contained in some cube [−N, N]n. Hence, if we know the edge length N of such a cube, then we can add the redundant cube constraints lj to the description of K. We obtain:


- (4.4) K = {x ∈ Rn : gi(x) ≥ 0 for i = 1, . . ., s and lj(x) ≥ 0 for j = 1, . . ., 2n}.


Furthermore, we consider for the given compact K the set of polynomials deﬁned as products of the enlarged set of constraints

q

- (4.5) hk : hk ∈ {1, g1, . . ., gs, l1, . . ., l2n} .

Moreover, we deﬁne ρq = |Rq(K)| and τq = max

i=1,...,s

{deg(gi), 1} · q. Now we state the Positivstellensatz for sums of nonnegative circuit polynomials.

- Theorem 4.8 (Positivstellensatz for SONC). Let f, g1, . . ., gs ∈ R[x], K be a compact, basic closed semi-algebraic set as in (4.4), and Rq(K) be deﬁned as in (4.5). If f(x) is strictly positive for all x ∈ K, then there exist d, q ∈ N∗, SONC polynomials sj(x) ∈ Cn,2d, and polynomials Hj(x) ∈ Rq(K) indexed by j = 1, . . ., ρq such that


f(x) =

ρq

j=1

sj(x)Hj(x).

Note that the sum ρj=1q sj(x)Hj(x) is of degree at most 2d + τq and it contains a summand s0 · 1 ∈ Cn,2d, which is in analogy to the structure of various SOS based Positivstellens¨atze.

Proof. Let f, g1, . . ., gs ∈ R[x] and P ⊆ R[x] be the preprime generated by all polynomials

- g1, . . ., gs and the redundant linear constraints l1, . . ., l2n, which we were allowed to add since K is compact, i.e.


P = Prep(g1, . . ., gs, l1, . . ., l2n). P is Archimedean since it contains the cube inequalities; see Lemma 4.5. In what follows we consider the set

- (4.6) M =


Rq(K) =

k=1

s(x)H(x) : ∃d, q ∈ N∗ such that s(x) ∈ Cn,2d, H(x) ∈ Rq(K) .

ﬁnite

- Claim 1: M is an Archimedean P-module. By deﬁnition, M is closed under addition. 1 ∈ M, because 1 ∈ Rq(K) and 1 ∈ Cn,2d.

M is closed under multiplication by an element of P, because P is generated by the gi and lj, which both are elements of Rq(K), so multiplication of m ∈ M with an element p ∈ P lies in M. Thus, M is a P-module. Furthermore, M is Archimedean, since P is Archimedean.

- Claim 2: The nonnegativity set KM = {x ∈ Rn : g(x) ≥ 0 for all g ∈ M} equals K. On the one hand, we have that KM ⊆ K since M is a P-module. Thus, the polynomials


deﬁning K are contained in M. On the other hand, a polynomial in M has the form

ﬁnite s(x)H(x), such that every s(x) ∈ Cn,2d. So, every s(x) is nonnegative on Rn. Thereby, the nonnegativity of polynomials in M only depends on the polynomials H(x) ∈ Rq(K). But these polynomials are exactly products of the constraint polynomials in K. Thus, we can conclude K ⊆ KM and hence K = KM .

With Claim 1 and Claim 2 satisﬁed we can apply Theorem 4.7 to conclude that f ∈ M. By (4.6) the expression of the Positivstellensatz is of the desired form.

For a ﬁxed q, the number of elements in the set Rq(K) is at most s+2qn+q ; thus, its cardinality is exponential in q. One may ask whether it is possible to formulate a Positivstellensatz involving only a linear number of terms, like Putinar’s Positivstellensatz based on sum of squares decomposition for polynomial optimization problems. It would be desirable to deﬁne an object like a quadratic module of the constraint polynomials. The main diﬃculty in carrying out such a construction is that the product of two SONC polynomials is not a SONC polynomial in general in contrast to the product of two SOS, which are an SOS; see Lemma 4.1, and also the resume, Section 6.

5. Application of the SONC Positivstellensatz in Constrained

Polynomial Optimization Problems In this section we establish a hierarchy of lower bounds fsonc(d,q) given by the SONC Posi-

tivstellensatz, Theorem 4.8, for the solution fK∗ of a constrained polynomial optimization problem on a compact, semi-algebraic set, and we formulate an optimization problem to

compute these bounds. As main results we show ﬁrst that the bounds fsonc(d,q) converge against fK∗ for d, q → ∞, Theorem 5.2, and second we show that the corresponding optimization problem is a relative entropy program and hence eﬃciently solvable with interior point methods, Theorem 5.3. We also discuss an example in Section 5.3.

- 5.1. A Converging Hierarchy for Constrained Polynomial Optimization. Minimizing a polynomial f(x) ∈ R[x] on a semi-algebraic set K ⊆ Rn is equivalent to maximizing a lower bound of this polynomial. Thus, we have:


fK∗ = inf

f(x) = sup{γ ∈ R : f(x) − γ ≥ 0 for all x ∈ K}.

x∈K

To obtain a general lower bound for fK∗ , which is eﬃciently computable, we relax the nonnegativity condition to ﬁnding the real number:

ρq

fsonc(d,q) = sup γ ∈ R : f(x) − γ =

sj(x)Hj(x) ,

j=1

where sj(x) ∈ Cn,2d are SONC polynomials and Hj(x) ∈ Rq(K) with Rq(K) being deﬁned as in (4.5). Indeed, the number fsonc(d,q) is a lower bound for fK∗ and grows monotonically in d and q as the following lemma shows.

- Lemma 5.1. Let f, g1, . . ., gs ∈ R[x], and let K be a semi-algebraic set. Then we have


- (i) fsonc(d,q) ≤ fK∗ for all d, q ∈ N∗.
- (ii) fsonc(d,q) ≤ fsonc(d,˜q˜) for all d ≤ d, q˜ ≤ q˜ with d, d, q,˜ q˜ ∈ N∗.


Lemma 5.1 yields a sequence fsonc(d,q)

both in d and q. Proof.

d,q∈N∗

of lower bounds of fK∗ which is increasing

- (i) For every sj(x) ∈ Cn,2d and every Hj(x) ∈ Rq(K) the polynomial sj(x)Hj(x) is nonnegative on K. Thus, we have for every γ ∈ R and every x ∈ K that

f(x) − γ =

ρq

j=1

sj(x)Hj(x) ⇒ f(x) − γ ≥ 0.

Hence, we have fsonc(d,q) ≤ fK∗ for every d, q ∈ N∗.

- (ii) We have Cn,2d ⊆ Cn,2d˜, and Rq(K) ⊆ Rq˜(K) for all d ≤ d, q˜ ≤ q˜with d, d, q,˜ q˜ ∈ N∗. Thus, the hierarchy of the bounds follows.


Note that Lemma 5.1 does not require K to be compact. An analogous statement and proof can be given literally without involving the redundant cube constraints l1, . . ., l2n in the deﬁnition of Rq(K).

For a compact constraint set K, however, we have an asymptotic convergence to the optimum fK∗ of the sequence fsonc(d,q)

. Thus, for compact K the provided hierarchy is complete.

d,q∈N∗

- Theorem 5.2. Let everything be deﬁned as in Lemma 5.1. In addition, let K be compact. Then


fsonc(d,q) ↑ fK∗ , for d, q → ∞.

Note that q is bounded from above by the chosen d. Therefore, it is suﬃcient to investigate d → ∞ and choose for every d the corresponding maximal q.

Proof. Let ε > 0 be arbitrary. Then f(x) − (fK∗ − ε) is strictly positive on K for all x ∈ Rn. According to Theorem 4.8, there exist suﬃciently large d, q ∈ N∗ such that

f(x) − fK∗ + ε = ρj=1q sj(x)Hj(x). Thus,

- (5.1) fK∗ − ε ≤ fsonc(d,q),

by deﬁnition of fsonc(d,q). Since d, q → ∞, (5.1) holds for all ε ↓ 0 for suﬃciently large d, q. By Lemma 5.1 (ii) the values fsonc(d,q) are monotonically increasing in d, q and the result follows.

5.2. Computation of the new Hierarchy via Relative Entropy Programming. Let n, 2d, q be ﬁxed. We intend to compute fsonc(d,q) via a suitable optimization program. This means for f ∈ R[x] and a compact set K we are looking for the maximal γ ∈ R such that

f(x) − γ =

ﬁnite

- (5.2) Hℓ(x)sℓ(x),


where Hℓ(x) ∈ Rq(K) and sℓ(x) ∈ Cn,2d. We formulate such a program in (5.3) and show in Theorem 5.3 that this program is a relative entropy program and hence eﬃciently solvable.

In what follows it is suﬃcient to consider nonnegative circuit polynomials instead of general SONC polynomials. Namely, since every sℓ(x) ∈ Cn,2d in (5.2) is of the form

ﬁnite pi,ℓ(x) where every pi,ℓ(x) is a nonnegative circuit polynomial, we can split up every term Hℓ(x)sℓ(x) into ﬁnite Hℓ(x)pi,ℓ(x) by distribution law.

Recall that CircA denotes the set of all circuit polynomials with support A ⊂ Zn, that ∆n,2d denotes the standard simplex in n variables of edge length 2d, and that we deﬁned Ln,2d = ∆n,2d ∩ Zn. The support of every circuit polynomial is contained in a suﬃciently large scaled standard simplex ∆n,2d. We deﬁne

Circn,2d = {p ∈ CircA : A ⊆ Ln,2d}, that is the set of all circuit polynomials with a support A which is contained in ∆n,2d. Let f(x) = f0 + η∈L

n,2d+τq\{0} fηxη ∈ R[x]. Note that we allow fη = 0. Furthermore, let K be a compact, semi-algebraic set given by a list of constraints g1, . . ., gs. Here, we simplify the notation by assuming that the gi already contain the linear constraints l1, . . ., l2n, which we added in Section 4. Let

Circn,2d = CircA(1) ⊔· · · ⊔ CircA(t),

where A(1), . . ., A(t) ⊆ Ln,2d is the ﬁnite list of possible support sets of circuit polynomials in ∆n,2d. We use the notation

CircA(i) =

ri

cα(j,i)xα(j,i) + ε · cβ(i)xβ(i) :

j=0

cα(j,i), cβ(i) ∈ R≥0, and ε ∈ {1, −1}

.

i,i the barycentric coordinates satisfying r Let Rq(K) = {H1, . . ., Hρ

- i
- j=0 λj,iα(j, i) = β(i).


We denote by λ0,i, . . ., λr

} such that Hℓ(x) = k

=1 Hγ(,ℓ)xγ(,ℓ) with Hγ(,ℓ) ∈ R. Moreover, we deﬁne the following support vectors

ℓ

q

supp(Circn,2d) = [α(j, i), β(i) : i = 1, . . ., t, j = 0, . . ., ri], supp(Rq(K)) = [γ(, ℓ) : ℓ = 1, . . ., ρq,  = 0, . . ., kℓ].

That means, supp(Circn,2d) is the vector which contains all exponents contained in A(1), . . ., A(t) with repetition. Similarly, supp(Rq(K)) is the vector which contains all exponents contained in the supports of H1, . . ., Hρ

with repetition. By construction, we have that supp(Circn,2d) is contained in Ln,2d, and every entry of supp(Rq(K)) is contained in Ln,τ

q

. By (5.2) we have to construct an optimization program which guarantees that for every

q

we have that the term fηxη of the given polynomial f, which has to be minimized, equals the sums of a term with exponent η in ﬁnite Hℓsℓ with Hℓ ∈ Rq(K) and sℓ ∈ Cn,2d. Thus, we have to (1) guarantee that the involved functions are indeed sums of nonnegative circuit polynomials and (2) we have to add a linear constraint for every η ∈ Ln,2d+τ

exponent η ∈ Ln,2d+τ

q

to match the coeﬃcients of the terms with exponent η in f with the coeﬃcients of the terms with exponent η in ﬁnite Hℓsℓ; see (5.2).

q

Let R be the subset of a real space given by

R = cα(ℓ,ε(j,i) ), cβ(ℓ,ε(i)), νj,i(ℓ,ε) ∈ R≥0, δj,i(ℓ,ε) ∈ R :

for every ℓ = 1, . . ., ρq, ε ∈ {1, −1}, and α(j, i), β(i) ∈ supp(Circn,2d)

.

Note that we are constructing a relative entropy program. The νj,i(ℓ,ε) ∈ R≥0, and

δj,i(ℓ,ε) ∈ R in R form the vectors ν and δ of variables in the general form of a relative entropy program as deﬁned in Deﬁnition 2.7.

In order to match the coeﬃcients of f with a representing polynomial coming from our Positivstellensatz, we deﬁne for every η ∈ Ln,2d+τ

\ {0} the following linear functions from R to R:

q

Γ1(η) =

ε · cβ(ℓ,ε(i)) · Hγ(,ℓ), Γ2(η) =

β(i)+γ(,ℓ)=η β(i)∈supp(Circn,2d) γ(,ℓ)∈supp(Rq(K)) ε∈{1,−1}

cα(ℓ,ε(j,i) ) · Hγ(,ℓ)

α(j,i)+γ(,ℓ)=η α(j,i)∈supp(Circn,2d) γ(,ℓ)∈supp(Rq(K)) ε∈{1,−1}

. We deﬁne an optimization program to compute fsonc(d,q). In what follows, the variables

where the Hγ(,ℓ) are constants given by the coeﬃcients of the functions H1, . . ., Hρ

q

νj,i(ℓ,ε) and δj,i(ℓ,ε) are completely redundant for the actual optimization process; see (1a), (1b), and (1c). We only have to introduce them to guarantee that the program (5.3) has the form of a relative entropy program.



minimize

cα(ℓ,ε(j,i) ) · Hγ(,ℓ)

α(j,i)+γ(,ℓ)=0 α(j,i)∈supp(Circn,2d) γ(,ℓ)∈supp(Rq(K)) ε∈{1,−1}

over the subset R′ of R deﬁned by:



- (5.3)


- (1a) νj,i(ℓ,ε) = cβ(ℓ,ε(i)) · λj,i

for all ℓ = 1, . . ., ρq; ε ∈ {1, −1}; j = 0, . . ., ri; i = 1, . . ., t,

- (1b) νj,i(ℓ,ε) · log ν

(ℓ,ε) j,i

![image 24](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile24.png>)

cα(j,i) ≤ δj,i(ℓ,ε)

for all ℓ = 1, . . ., ρq; ε ∈ {1, −1}; j = 0, . . ., ri; i = 1, . . ., t,

- (1c) r


- i
- j=0 δj,i(ℓ,ε) ≤ 0 for all ℓ = 1, . . ., ρq; ε ∈ {1, −1}; i = 1, . . ., t,




\ {0} . Theorem 5.3. The program (5.3) is a relative entropy program and hence eﬃciently solvable, and its output coincides with f0 − fsonc(d,q).

(2) Γ1(η) + Γ2(η) = fη for every η ∈ Ln,2d+τ

q

Proof. First, we show that (5.3) is indeed a relative entropy program, i.e. we need to show that it is of the form (2.4) in Deﬁnition 2.7. Constraint (1b) in (5.3) is a constraint

of the form (2) in (2.4) satisfying νj,i(ℓ,ε), cα(ℓ,ε(j,i) ) ≥ 0 and δj,i(ℓ,ε) ∈ R as required. The constraints (1a),(1c), and (2) in (5.3) are linear constraints since all λj,i, Hγ(,ℓ), and ε are

![image 25](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile25.png>)

Figure 2. ∆2,4 with the lattice points L2,4. The even points are the green ones.

constants; note that linear equalities can be represented by two linear inequalities. Thus, these constraints are of the form (1) in (2.4). Finally, the objective function is also linear as required by (2.4). Hence, (5.3) is a relative entropy program by Deﬁnition 2.7.

Second, we need to show that the program provides the correct output. Note that the

program is infeasible if there exist i, j, ℓ such that cα(ℓ,ε(j,i) ) = 0 and cβ(ℓ,ε(i)) · λj,i > 0. Hence, we can omit this case. By Theorem 3.2 the union of the constraints (1a),(1b), and (1c) are equivalent to a constraint

ri

(3) cβ(ℓ,ε(i))

j=0

λj,i cα(ℓ,ε(j,i) )

![image 26](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile26.png>)

λj,i

≤ 1 for every i = 1, . . ., t, ε ∈ {1, −1}.

The variables cα(ℓ,ε(j,i) ) and cβ(ℓ,ε(i)) in the program (5.3) are by construction the coeﬃcients of circuit polynomials. For the purpose of the program, these circuit polynomials need to be nonnegative; see (5.2). This is guaranteed by constraint (3).

\ {0} constraint (2) guarantees that every coeﬃcient fη equals Γ1(η) + Γ2(η), which are exactly all polynomials of the form ﬁnite Hℓsℓ, where Hℓ ∈ Rq(K) and sℓ ∈ Cn,2d. Particularly, it is suﬃcient to consider (nonnegative) circuit polynomials in Γ1(η) and Γ2(η) instead of SONC polynomials. Namely, for every term Hℓsℓ with sℓ ∈ Cn,2d we can write sℓ = ﬁnite pi,ℓ, where pi,ℓ are nonnegative circuit polynomials. Thus, on the one hand, we obtain an expression Hℓsℓ = ﬁnite Hℓpi,ℓ which only depends on circuit polynomials. On the other hand, we can guarantee that (5.2) is satisﬁed, which we need to show. Finally, the program minimizes the constant term of the function ﬁnite Hℓsℓ, where Hℓ ∈ Rq(K), which is equivalent to maximizing γ.

For every η ∈ Ln,2d+τ

q

- 5.3. An Example. We consider the polynomial f = x31+x32−x1x2+4 and a semialgebraic set K given by constraints g1 = −x1 + 1, g2 = x1 + 1, g3 = −x2 + 1, g4 = x2 + 1. It is easy to see that f is positive on K. We want to represent f with our Positivstellensatz 4.8. We consider C2,4.


Circ2,4 is a union of 28 diﬀerent support sets. There exist:

- • six even lattice points in L2,4 and thus 6 zero dimensional circuit polynomials,
- • 62 = 15 circuit polynomials with one dimensional Newton polytope, and
- • 63 even 2-simplices, which are contained in ∆2,4. One simplex contains three lattice points in the interior, four contain one lattice point in the interior, and the remaining ones contain no lattice point in the interior. Thus, we only need to consider seven circuit polynomials with 2-dimensional Newton polytope.


The number of elements in Rq(K) is ρq = 4+qq ; see Section 4.2. I.e., we have in this example ρ1 = 5, ρ2 = 15, ρ3 = 35.

Let us assume that we want to compute fsonc(2,1). We are looking for the maximal γ such that f −γ can be represented as a sum sj(x)Hj(x) with sj(x) ∈ C2,4 and Hj(x) ∈ R1(K). We would, however, not consider all these polynomials in practice. First, the circuit polynomials with 1-dimensional Newton polytope are suﬃcient, to construct every lattice point in L2,4 and thus it makes sense to disregard all 2-simplices. Second, f does not contain every lattice point in L2,4 as an exponent and hence it is not surprising that several further circuit polynomials can be omitted. Indeed, we ﬁnd a decomposition according to the Positivstellensatz 4.8 of the form

f(x) = (x1 + 1) · (x21 − 2x1 + 1) + (x2 + 1) · (x22 − 2x2 + 1) + 1 ·

+1 ·

- 1

![image 27](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile27.png>)

- 2


1 2

x21 + x1 +

![image 28](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile28.png>)

+ 1 ·

- 1

![image 29](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile29.png>)

- 2


- 1

![image 30](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile30.png>)

- 2


x22 + x2 +

+ 1,

- 1

![image 31](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile31.png>)

- 2


x21 − x1x2 +

- 1

![image 32](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile32.png>)

- 2


x22

which only involves 3 of the 15 1-dimensional circuit polynomials, one 0-dimensional circuit polynomial, and no 2-dimensional one.

6. Resume and Open Problems

In this article we have established a Positivstellensatz for SONC polynomials. This Positivstellensatz provides a new way to attack constrained polynomial optimization problems independent of SOS and SDP. Namely, it provides a converging hierarchy of lower bounds, which can be computed eﬃciently via relative entropy programming.

The ﬁrst future task is to implement the program (5.3), to test it for various instances of constrained polynomial optimization problems, and to compare the runtime and optimal values with the counterparts from SDP results using Lasserre relaxation. Given the runtime comparison of the SONC and the SOS approach in previous works [DIdW16, GM12, IdW16] using geometric programming, there is reasonable hope that our relative entropy programs are faster than semideﬁnite programming in several cases.

Second, an important problem is to establish statements which guarantee convergence of

the bounds fsonc(d,q) after ﬁnitely many steps. Unfortunately, there is no obvious way to attack this problem, since similar statements for Lasserre relaxation (see e.g. [Las10, Lau09]) cannot be proven with analogous methods for our Positivstellensatz straightforwardly.

Third, we have seen in Section 5.3 that it can (and likely will often) happen that many of the circuit polynomials in supp(Circn,2d) are redundant for ﬁnding a representation of

a given polynomial with respect to our Positivstellensatz 4.8. Hence, the corresponding optimization problem (5.3) can be reduced in these cases. For practical applications, we have to develop strategies to restrict ourselves to useful subsets of circuit polynomials to reduce the runtime of our programs via reducing the number of variables.

Fourth, in our Positivstellensatz, Theorem 4.8, it is a delicate open problem to analyze whether there always exists a decomposition with q = 1, which corresponds to a Putinar equivalent Positivstellensatz for SONC polynomials. If such a representation does not exist in general, then it would also be interesting to search for certain instances of polynomials for which there exists such a minimal representation.

Fifth, both the SONC cone itself and the connection between the SONC and the SAGE cone need to be analyzed more carefully. Important problems concern e.g. the boundary and the extreme rays of the SONC cone, and the question whether there is a primal/dual-relation between the SAGE and the SONC cone. These questions will be discussed in a follow-up paper.

Sixth, we hope to ﬁnd a way to combine SOS and SONC certiﬁcates in theory and practice.

Acknowledgements We thank the anonymous referees for their helpful comments. References

[BKVH07] S. Boyd, S.J. Kim, L. Vandenberghe, and A. Hassibi, A tutorial on geometric programming, Optim. Eng. 8 (2007), no. 1, 67–127.

[BPT13] G. Blekherman, P.A. Parrilo, and R.R. Thomas, Semideﬁnite optimization and convex algebraic geometry, MOS-SIAM Series on Optimization, vol. 13, SIAM and the Mathematical Optimization Society, Philadelphia, 2013.

[BV04] S. Boyd and L. Vandenberghe, Convex optimization, Cambridge University Press, Cambridge, 2004. [CS15] V. Chandrasekaran and P. Shah, Relative entropy optimization and its applications, 2015, To appear in Mathematical Programming. [CS16] , Relative Entropy Relaxations for Signomial Optimization, SIAM J. Optim. 26 (2016), no. 2, 1147–1173. [DG14] P.J.C. Dickinson and L. Gijben, On the computational complexity of membership problems for the completely positive cone and its dual, Comput. Optim. Appl. 57 (2014), no. 2, 403–415.

![image 33](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile33.png>)

[DIdW16] M. Dressler, S. Iliman, and T. de Wolﬀ, An approach to constrained polynomial optimization via nonnegative circuit polynomials and geometric programming, 2016, Preprint, arXiv:1602.06180.

[DPZ67] R.J. Duﬃn, E.L. Peterson, and C. Zener, Geometric programming: Theory and application, John Wiley & Sons, Inc., New York-London-Sydney, 1967. [dW15] T. de Wolﬀ, Amoebas, nonnegative polynomials and sums of squares supported on circuits, Oberwolfach Rep. (2015), no. 23, 1308–1311. [GKZ94] I.M. Gelfand, M.M. Kapranov, and A.V. Zelevinsky, Discriminants, Resultants and Multidimensional Determinants, Birkh¨user, Boston, 1994. [GM12] M. Ghasemi and M. Marshall, Lower bounds for polynomials using geometric programming, SIAM J. Optim. 22 (2012), no. 2, 460–473. [IdW16] S. Iliman and T. de Wolﬀ, Amoebas, nonnegative polynomials and sums of squares supported on circuits, Res. Math. Sci. 3 (2016), 3:9.

- [Kri64a] J.-L. Krivine, Anneaux pre´ordonne´s, J. Analyse Math. 12 (1964), 307–326.
- [Kri64b] , Quelques proprie´te´s des pre´ordres dans les anneaux commutatifs unitaires, C. R. Acad. Sci. Paris 258 (1964), 3417–3418.


![image 34](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile34.png>)

[Las01] J.B. Lasserre, Global optimization with polynomials and the problem of moments, SIAM J. Optim. 11 (2000/01), no. 3, 796–817. [Las10] , Moments, positive polynomials and their applications, Imperial College Press Optimization Series, vol. 1, Imperial College Press, London, 2010.

![image 35](<2016-dressler-positivstellensatz-sums-nonnegative-circuit_images/imageFile35.png>)

[Lau09] M. Laurent, Sums of squares, moment matrices and optimization over polynomials, Emerging applications of algebraic geometry, IMA Vol. Math. Appl., vol. 149, Springer, New York, 2009, pp. 157–270.

[Mar08] M. Marshall, Positive polynomials and sums of squares, Mathematical Surveys and Monographs, vol. 146, American Mathematical Society, Providence, RI, 2008. [NN94] Y. Nesterov and A. Nemirovskii, Interior point polynomial algorithms in convex programming,

Studies in Applied Mathematics, Society for Industrial and Applied Mathematics, 1994. [Rez78] B. Reznick, Extremal PSD forms with few terms, Duke Math. J. 45 (1978), no. 2, 363–374. [Sch09] C. Scheiderer, Positivity and sums of squares: a guide to recent results, Emerging applications

of algebraic geometry, IMA Vol. Math. Appl., vol. 149, Springer, New York, 2009, pp. 271–324.

Mareike Dressler, Goethe-Universitat,¨ FB 12 – Institut fur¨ Mathematik, Postfach 11

19 32, 60054 Frankfurt am Main, Germany E-mail address: dressler@math.uni-frankfurt.de Sadik Iliman, Frankfurt am Main, Germany E-mail address: iliman@gmx.de Timo de Wolff, Texas A&M University, Department of Mathematics, College Station,

TX 77843-3368, USA E-mail address: dewolff@math.tamu.edu

