arXiv:1009.0125v3[math.OC]12May2011

A NEW LOOK AT NONNEGATIVITY ON CLOSED SETS AND POLYNOMIAL OPTIMIZATION

JEAN B. LASSERRE

Abstract. We ﬁrst show that a continuous function f is nonnegative on a closed set K ⊆ Rn if and only if (countably many) moment matrices of some signed measure dν = fdµ with supp µ = K, are all positive semideﬁnite (if K is compact µ is an arbitrary ﬁnite Borel measure with supp µ = K). In particular, we obtain a convergent explicit hierarchy of semideﬁnite (outer) approximations with no lifting, of the cone of nonnegative polynomials of degree at most d. Wen used in polynomial optimization on certain simple closed sets K (like e.g., the whole space Rn, the positive orthant, a box, a simplex, or the vertices of the hypercube), it provides a nonincreasing sequence of upper bounds which converges to the global minimum by solving a hierarchy of semideﬁnite programs with only one variable (in fact, a generalized eigenvalue problem). In the compact case, this convergent sequence of upper bounds complements the convergent sequence of lower bounds obtained by solving a hierarchy of semideﬁnite relaxations as in e.g. [12].

1. Introduction

This paper is concerned with a concrete characterization of continuous functions that are nonnegative on a closed set K ⊆ Rn and its application for optimization purposes. By concrete we mean a systematic procedure, e.g. a numerical test that can be implemented by an algorithm, at least in some interesting cases. For polynomials, Stengle’s Nichtnegativstellensatz [22] provides a certiﬁcate of nonnegativity (or absence of nonnegativity) on a semi-algebraic set. Moreover, in principle, this certiﬁcate can be obtained by solving a single semideﬁnite program (although the size of this semideﬁnite program is far beyond the capabilities of today’s computers). Similarly, for compact basic semi-algebraic sets, Schm¨udgen’s and Putinar’s Positivstellensa¨tze [20, 18] provide certiﬁcates of strict positivity that can be obtained by solving ﬁnitely many semideﬁnite programs (of increasing size). Extensions of those certiﬁcates to some algebras of non-polynomial functions have been recently proposed in Lasserre and Putinar [14] and in Marshall and Netzer [16]. However, and to the best of our knowledge, there is still no hierarchy of explicit (outer or inner) semideﬁnite approximations (with or without lifting) of the cone of polynomials nonnegative on a closed set K, except if K is compact and basic semi-algebraic (in which case outer approximations exist). Another exception is the convex cone of quadratic forms nonnegative on K = Rn+ for which inner and outer approximations are available; see e.g. Anstreicher and Burer [1], and D¨ur [7].

![image 1](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile1.png>)

1991 Mathematics Subject Classiﬁcation. 90C25 28C15. Key words and phrases. closed sets; nonnegative functions; nonnegative polynomials; semidef-

inite approximations; moments.

1

Contribution: In this paper, we present a diﬀerent approach based on a new (at least to the best of our knowledge) and simple characterization of continuous functions that are nonnegative on a closed set K ⊆ Rn. This characterization involves a single (but known) measure µ with suppµ = K, and sums of squares of polynomials. Namely, our contribution is twofold:

(a) We ﬁrst show that a continuous function f is nonnegative on a closed set K ⊆ Rn if and only if h2fdµ is nonnegative for all polynomials h ∈ R[x], where µ is a ﬁnite Borel measure1 with suppµ = K. The measure µ is arbitrary if K is compact. If K is not compact then one may choose for µ the ﬁnite Borel measure:

- - dµ = exp(− i |xi|)dϕ if f is a polynomial, and
- - dµ = (1 + f2)−1 exp(− i |xi|)dϕ, if f is not a polynomial,


where ϕ is any ﬁnite Borel measure with support exactly K. But many other choices are possible.

Equivalently, f is nonnegative on K if and only if every element of the countable family T of moment matrices associated with the signed Borel measure fdµ, is positive semideﬁnite. The absence of nonnegativity on K can be certiﬁed by exhibiting a polynomial h ∈ R[x] such that h2fdµ < 0, or equivalently, when some moment matrix in the family T is not positive semideﬁnite. And so, interestingly, as for nonnegativity or positivity, our certiﬁcate for absence of nonnegativity is also in terms of sums of squares. When f is a polynomial, these moment matrices are easily obtained from the moments of µ and this criterion for absence of nonnegativity complements Stengle’s Nichtnegativstellensatz [22] (which provides a certiﬁcate of nonnegativity on a semi-algebraic set K) or Schm¨udgen and Putinar’s Positivstellens¨atze [20, 18] (for certiﬁcates of strict positivity on compact basic semi-algebraic sets). At last but not least, we obtain a convergent explicit hierarchy of semideﬁnite (outer) approximations with no lifting, of the cone Cd of nonnegative polynomials of degree at most 2d. That is, we obtain a nested sequence Cd0 ⊃ ···Cdk ⊃ ··· ⊃ Cd such that each Cdk is a spectrahedron deﬁned solely in terms of the vector of coeﬃcients of the polynomial, with no additional variable (i.e., no projection is needed). Similar explicit hierarchies can be obtained for the cone of polynomials nonnegative on a closed set K (neither necessarily basic semi-algebraic nor compact), provided that all moments of an appropriate measure µ (with support exactly K) can be obtained. To the best of our knowledge, this is ﬁrst result of this kind.

(b) As a potential application, we consider the problem of computing the global minimum f∗ of a polynomial f on a closed set K, a notoriously diﬃcult problem. In nonlinear programming, a sequence of upper bounds on f∗ is usually obtained from a sequence of feasible points (xk) ⊂ K, e.g., via some (local) minimization algorithm. But it is important to emphasize that for non convex problems, providing a sequence of upper bounds (f(xk)), k ∈ N, that converges to f∗ is in general impossible, unless one computes points on a grid whose mesh size tends to zero.

We consider the case where K ⊆ Rn is a closed set for which one may compute all moments of a measure µ with suppµ = K. Typical examples of such sets are e.g. K = Rn or K = Rn+ in the non compact case and a box, a ball, an ellipsoid, a simplex, or the vertices of an hypercube (or hyper rectangle) in the compact case.

![image 2](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile2.png>)

1A ﬁnite Borel measure µ on Rn is a nonnegative set function deﬁned on the Borel σ-algebra of Rn (i.e., the σ-algebra generated by the open sets), such that µ(∅) = 0, µ(Rn) < ∞, and µ( ∞i=1 Ei) = ∞i=1 µ(Ei) for any collection of disjoint measurable sets Ei. Its support (denoted supp µ) is the smallest closed set K such that µ(Rn \ K) = 0; see e.g. Royden [19].

We then provide a hierarchy of semideﬁnite programs (with only one variable!) whose optimal values form a monotone nonincreasing sequence of upper bounds which converges to the global minimum f∗. In fact, each semideﬁnite program is a very speciﬁc one as it reduces to solving a generalized eigenvalue problem for a pair of real symmetric matrices.. (Therefore, for eﬃciency one may use specialized software packages instead of a SDP solver.) However, the convergence to f∗ is in general only asymptotic and not ﬁnite (except when K is a discrete set in which case ﬁnite convergence takes place). This is in contrast with the hierarchy of semideﬁnite relaxations deﬁned in Lasserre [12, 13] which provide a nondecreasing sequence of lower bounds that also converges to f∗, and very often in ﬁnitely many steps. Hence, for compact basic semi-algebraic sets these two convergent hierarchies of upper and lower bounds complement each other and permit to locate the global minimum f∗ in smaller and smaller intervals.

Notice that convergence of the hierarchy of convex relaxations in [12] is guaranteed only for compact basic semi-algebraic sets, whereas for the new hierarchy of upper bounds, the only requirement on K is to know all moments of a measure µ with suppµ = K. On the other hand, in general computing such moments is possible only for relatively simple (but not necessarily compact nor semi-algebraic) sets.

At last but not least, the nonincreasing sequence of upper bounds converges to f∗ even if f∗ is not attained, which when K = Rn, could provide an alternative and/or a complement to the hierarchy of convex relaxations provided in Schweighofer [21] (based on gradient tentacles) and in Ha` and Pham [8] (based on the truncated tangency variety), which both provide again a monotone sequence of lower bounds.

Finally, we also give a very simple interpretation of the hierarchy of dual semideﬁnite programs, which provides some information on the location of global minimizers.

2. Notation, definitions and preliminary results

A Borel measure on Rn is understood as a positive Borel measure, i.e., a nonnegative set function µ on the Borel σ-algebra B (i.e., the σ-algebra generated by the open sets of Rn) such that µ(∅) = 0, and with the countably additive property

∞

∞

µ(Ei),

Ei =

µ

i=1

i=1

for any collection of disjoint measurable sets (Ei) ⊂ B; see e.g. Royden [19, pp. 253–254].

Let R[x] be the ring of polynomials in the variables x = (x1,...,xn), and Σ[x] ⊂ R[x] its subset of polynomials that are sums of squares (s.o.s.). Denote by R[x]d ⊂ R[x] the vector space of polynomials of degree at most d, which forms a vector space

of dimension s(d) = n+dd , with e.g., the usual canonical basis (xα) of monomials. Also, denote by Σ[x]d ⊂ Σ[x] the convex cone of s.o.s. polynomials of degree at

most 2d. If f ∈ R[x]d, write f(x) = α∈Nn fαxα in the canonical basis and denote by f = (fα) ∈ Rs(d) its vector of coeﬃcients. Let Sn denotes the vector space of p × p real symmetric matrices. For a matrix A ∈ Sp the notation A 0 (resp.

- A ≻ 0) stands for A is positive semideﬁnite (resp. deﬁnite).


Moment matrix. With y = (yα) being a sequence indexed in the canonical basis (xα) of R[x], let Ly : R[x] → R be the linear functional

fα xα)  → Ly(f) =

f (=

fα yα,

α

α

and let Md(y) be the symmetric matrix with rows and columns indexed in the canonical basis (xα), and deﬁned by:

- (2.1) Md(y)(α,β) := Ly(xα+β) = yα+β, α,β ∈ Nnd

with Nnd := {α ∈ Nn : |α| (= i αi) ≤ d}.

If y has a representing measure µ, i.e., if yα = xαdµ for every α ∈ Nn, then f,Md(y)f = f(x)2 dµ(x) ≥ 0, ∀f ∈ R[x]d,

and so Md(y) 0. A measure µ is said to be moment determinate if there is no other measure with same moments. In particular, and as an easy consequence of the Stone-Weierstrass theorem, every measure with compact support is determinate2.

Not every sequence y satisfying Md(y) 0, d ∈ N, has a representing measure. However: Proposition 2.1 (Berg [3]). Let y = (yα) be such that Md(y) 0, for every d ∈ N. Then:

- (a) The sequence y has a representing measure whose support is contained in the

ball [−a,a]n if there exists a,c > 0 such that |yα| ≤ c a|α| for every α ∈ Nn.

- (b) The sequence y has a representing measure µ on Rn if


- (2.2)

∞

t=1

Ly(x2it)−1/2t = +∞, ∀i = 1,...,n. In addition, in both cases (a) and (b) the measure µ is moment determinate.

Condition (b) is an extension to the multivariate case of Carleman’s condition in the univariate case and is due to Nussbaum [17]. For more details see e.g. Berg [3] and/or Maserick and Berg [11].

Localizing matrix. Similarly, with y = (yα) and f ∈ R[x] written x  → f(x) =

γ∈Nn

fγ xγ,

let Md(f y) be the symmetric matrix with rows and columns indexed in the canonical basis (xα), and deﬁned by:

- (2.3) Md(f y)(α,β) := Ly f(x)xα+β = γ

fγ yα+β+γ, ∀α,β ∈ Nnd.

If y has a representing measure µ, then g,Md(f y)g = g2fdµ, and so if µ is supported on the set {x : f(x) ≥ 0}, then Md(f y) 0 for all d = 0,1,... because

- (2.4) g,Md(f y)g = g(x)2f(x)dµ(x) ≥ 0, ∀g ∈ R[x]d.


![image 3](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile3.png>)

2To see this note that (a) two measures µ1, µ2 on a compact set K ⊂ Rn are identical if and

only if K fdµ1 = K fdµ2 for all continuous functions f on K, and (b) by Stone-Weierstrass, the polynomials are dense in the space of continuous functions for the sup-norm.

3. Nonnegativity on closed sets

Recall that if X is a separable metric space with Borel σ-ﬁeld B, the support suppµ of a Borel measure µ on X is the (unique) smallest closed set B ∈ B such that µ(X \ B) = 0. Given a Borel measure µ on Rn and a measurable function

- f : Rn → R, the mapping B  → ν(B) := B fdµ, B ∈ B, deﬁnes a set function on B. If f is nonnegative then ν is a Borel measure (which is ﬁnite if f is µ-integrable); see e.g. Royden [19, p. 276 and p. 408]. If f is not nonnegative then setting


- B1 := {x : f(x) ≥ 0} and B2 := {x : f(x) < 0}, the set function ν can be written as the diﬀerence


- (3.1) ν(B) = ν1(B) − ν2(B), B ∈ B, of the two positive Borel measures ν1,ν2 deﬁned by
- (3.2) ν1(B) = B1∩B

fdµ, ν2(B) = −

B2∩B

fdµ, ∀B ∈ B.

Then ν is a signed Borel measure provided that either ν1(B1) or ν2(B2) is ﬁnite; see e.g. Royden [19, p. 271]. We ﬁrst provide the following auxiliary result which is also of self-interest.

Lemma 3.1. Let X be a separable metric space, K ⊆ X a closed set, and µ a Borel measure on X with suppµ = K. A continuous function f : X → R is nonnegative

on K if and only if the set function B  → ν(B) = K∩B fdµ, B ∈ B, is a positive measure.

Proof. The only if part is straightforward. For the if part, if ν is a positive measure then f(x) ≥ 0 for µ-almost all x ∈ K. That is, there is a Borel set G ⊂ K such that µ(G) = 0 and f(x) ≥ 0 on K \ G. Indeed, otherwise suppose that there exists a Borel set B0 with µ(B0) > 0 and f < 0 on B0; then one would get the contradiction that ν is not positive because ν(B0) = B

0

fdµ < 0. In fact, f is called the Radon-Nikodym derivative of ν with respect to µ; see Royden [19, Theorem 23, p. 276].

Next, observe that K \ G ⊂ K and µ(K \ G) = µ(K). Therefore K \ G = K because suppµ(= K) is the unique smallest closed set such that µ(X \ K) = 0. Hence, let x ∈ K be ﬁxed, arbitrary. As K = K \ G, there is a sequence (xk) ⊂ K \ G, k ∈ N, with xk → x as k → ∞. But since f is continuous and f(xk) ≥ 0 for every k ∈ N, we obtain the desired result f(x) ≥ 0.

![image 4](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile4.png>)

![image 5](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile5.png>)

![image 6](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile6.png>)

![image 7](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile7.png>)

Lemma 3.1 itself (of which we have not been able to ﬁnd a trace in the literature) is a characterization of nonnegativity on K for a continuous function f on X. However, one goal of this paper is to provide a more concrete characterization. To do so we ﬁrst consider the case of a compact set K ⊂ Rn.

- 3.1. The compact case. Let K be a compact subset of Rn. For simplicity, and with no loss of generality, we may and will assume that K ⊆ [−1,1]n.


Theorem 3.2. Let K ⊆ [−1,1]n be compact and let µ be an arbitrary, ﬁxed, ﬁnite Borel measure on K with suppµ = K, and with vector of moment y = (yα), α ∈ Nn. Let f be a continuous function on Rn. Then:

- (a) f is nonnegative on K if and only if


- (3.3) K


g2 f dµ ≥ 0, ∀g ∈ R[x],

or, equivalently, if and only if

- (3.4) Md(z) 0, d = 0,1,...

where z = (zα), α ∈ Nn, with zα = xαf(x)dµ(x), and with Md(z) as in (2.1).

If in addition f ∈ R[x] then (3.4) reads Md(f y) 0, d = 0,1,..., where Md(f y) is the localizing matrix deﬁned in (2.3).

(b) If in addition to be continuous, f is also concave on K, then f is nonnegative on the convex hull co (K) of K if and only if (3.3) holds.

Proof. The only if part is straightforward. Indeed, if f ≥ 0 on K then K ⊆ {x : f(x) ≥ 0} and so for any ﬁnite Borel measure µ on K, K g2fdµ ≥ 0 for every g ∈ R[x]. Next, if f is concave and f ≥ 0 on co (K) then f ≥ 0 on K and so the “only if” part of (b) also follows.

If part. The set function ν(B) = B fdµ, B ∈ B, can be written as the diﬀerence ν = ν2 − ν2 of the two positive ﬁnite Borel measures ν1,ν2 described in (3.1)-(3.2), where B1 := {x ∈ K : f(x) ≥ 0} and B2 := {x ∈ K : f(x) < 0}. As K is compact and f is continuous, both ν1,ν2 are ﬁnite, and so ν is a ﬁnite signed Borel measure; see Royden [19, p. 271]. In view of Lemma 3.1 it suﬃces to prove that in fact ν is a ﬁnite and positive Borel measure. So let z = (zα), α ∈ Nn, be the sequence deﬁned by:

- (3.5) zα = K

xαdν(x) :=

K

xαf(x)dµ(x), ∀α ∈ Nn.

Every zα, α ∈ Nn, is ﬁnite because K is compact and f is continuous. So the condition

K

g(x)2f(x)dµ(x) ≥ 0, ∀f ∈ R[x]d,

reads g,Md(z)g ≥ 0 for all g ∈ Rs(d), that is, Md(z) 0, where Md(z) is the moment matrix deﬁned in (2.1). And so (3.3) implies Md(z) 0 for every d ∈ N. Moreover, as K ⊆ [−1,1]n,

|zα| ≤ c :=

K

|f|dµ, ∀α ∈ Nn.

Hence, by Proposition 2.1, z is the moment sequence of a ﬁnite (positive) Borel measure ψ on [−1,1]n, that is, as suppν ⊆ K ⊆ [−1,1]n,

- (3.6) [−1,1]n


xα dψ(x), ∀α ∈ Nn. But then using (3.1) and (3.6) yields

xα dν(x) =

[−1,1]n

xα dν1(x) =

[−1,1]n

xα d(ν2 + ψ)(x), ∀α ∈ Nn,

[−1,1]n

which in turn implies ν1 = ν2 + ψ because measures on a compact set are determinate. Next, this implies ψ = ν1 − ν2 (= ν) and so ν is a positive Borel measure on K. Hence by Lemma 3.1, f(x) ≥ 0 on K.

If in addition f ∈ R[x], the sequence z = (zα) is obtained as a linear combination of (yα). Indeed if f(x) = β fβ xβ then

fβ yα+β, ∀α ∈ Nn,

zα =

β∈Nn

and so in (3.4), Md(z) is nothing less than the localizing matrix Md(f y) associated with y = (yα) and f ∈ R[x], deﬁned in (2.3), and (3.4) reads Md(f y) 0 for all d = 0,1,...

Finally, if f is concave then f ≥ 0 on K implies f ≥ 0 on co(K), and so the only if part of (b) also follows.

Therefore, to check whether a polynomial f ∈ R[x] is nonnegative on K, it suﬃces to check if every element of the countable family of real symmetric matrices (Md(f y)), d ∈ N, is positive semideﬁnite.

Remark 3.3. An informal alternative proof of Theorem 3.2 which does not use Lemma 3.1 is as follows. If f is not nonnegative on K there exists a ∈ K such that f(a) < 0, and so as K is compact, there is a continuous function, e.g, x  → h(x) := exp(−c x − a 2) close to 1 in some open neighborhood B(a,δ) of a, and very small in the rest of K. By the Stone-Weierstrass’s theorem, one may choose

- h to be a polynomial. Next, the complement B(a,δ)c (= Rn \ B(a,δ)) of B(a,δ) is closed, and so K ∩ B(a,δ)c is a closed set contained in K (hence smaller than K). Therefore µ(B(a,δ)) > 0 because otherwise µ(K ∩ B(a,δ)c) = µ(K) which would imply that K ∩ B(a,δ)c is a support of µ smaller than K, in contradiction with suppµ = K. Hence, we would get the contradiction


h2 f dµ ≈ h(a)2f(a)µ(B(a,δ)) < 0.

However, in the non compact case described in the next section, this argument is not valid.

- 3.2. The non-compact case. We now consider the more delicate case where K is a closed set of Rn, not necessarily compact. To handle arbitrary non compact sets K and arbitrary continuous functions f, we need a reference measure µ with suppµ = K and with nice properties so that integrals such as g2fdµ, g ∈ R[x], are well-behaved.


So, let ϕ be an arbitrary ﬁnite Borel measure on Rn whose support is exactly K, and let µ be the ﬁnite Borel measure deﬁned by:

- (3.7) µ(B) := B

exp −

n

i=1

|xi| dϕ(x), ∀B ∈ B(Rn).

Observe that suppµ = K and µ satisﬁes Carleman’s condition (2.2). Indeed, let z = (zα), α ∈ Nn, be the sequence of moments of µ. Then for every i = 1,...,n, and every k = 0,1,..., using x2ik ≤ (2k)!exp|xi|,

- (3.8) Lz(x2ik) = K


x2ik dµ(x) ≤ (2k)!

e|x

i| dµ(x) ≤ (2k)!ϕ(K) =: (2k)!M.

K

Therefore for every i = 1,...,n, using (2k)! < (2k)2k for every k, yields

∞

Lz(x2ik)−1/2k ≥

k=1

∞

M−1/2k ((2k)!)−1/2k ≥

k=1

∞

M−1/2k 2k

![image 8](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile8.png>)

k=1

= +∞,

i.e., (2.2) holds. Notice also that all the moments of µ (deﬁned in (3.7)) are ﬁnite, and so every polynomial is µ-integrable.

- Theorem 3.4. Let K ⊆ Rn be closed and let ϕ be an arbitrary ﬁnite Borel measure whose support is exactly K. Let f be a continuous function on Rn. If f ∈ R[x] (i.e., f is a polynomial) let µ be as in (3.7) whereas if f is not a polynomial let µ be deﬁned by


- (3.9) µ(B) := B

exp(− ni=1 |xi|) 1 + f(x)2

![image 9](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile9.png>)

dϕ(x), ∀B ∈ B(Rn).

Then (a) and (b) of Theorem 3.2 hold.

For a detailed proof see §6. It is important to emphasize that in Theorem 3.2 and 3.4, the set K is an arbitrary closed set of Rn, and to the best of our knowledge, the characterization of nonnegativity of f in terms of positive deﬁniteness of the moment matrices Md(z) is new. But of course, this characterization becomes even more interesting when one knows how the compute the moment sequence z = (zα), α ∈ Nn, which is possible in a few special cases only.

Important particular cases of nice such sets K include boxes, hyper rectangles, ellipsoids, and simplices in the compact case, and the positive orthant, or the whole space Rn in the non compact case. For instance, for the whole space K = Rn one may choose for µ in (3.7) the multivariate Gaussian (or normal) probability measure

µ(B) := (2π)−n/2

B

exp(−

- 1

![image 10](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile10.png>)

- 2


x 2)dx, B ∈ B(Rn),

which the n-times product of the one-dimensional normal distribution

µi(B) :=

1 √2π B

![image 11](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile11.png>)

![image 12](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile12.png>)

exp(−x2i /2)dxi, B ∈ B(R),

whose moments are all easily available in closed form. In Theorem 3.4 this corresponds to the choice

- (3.10) ϕ(B) = (2π)−n/2 B

exp(− x 2/2) exp(− ni=1 |xi|)

![image 13](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile13.png>)

dx, B ∈ B(Rn).

When K is the positive orthant Rn+ one may choose for µ the exponential probability measure

- (3.11) µ(B) := B


exp(−

n

xi)dx, B ∈ B(Rn+),

i=1

which the n-times product of the one-dimensional exponential distribution

µi(B) :=

exp(−xi)dxi, B ∈ B(R+),

B

whose moments are also easily available in closed form. In Theorem 3.4 this corresponds to the choice

ϕ(B) = 2n

n

exp(−

B

i=1

xi)dx, B ∈ B(Rn+).

- 3.3. The cone of nonnegative polynomials. The convex cone Cd ⊂ R[x]2d of nonnegative polynomials of degree at most 2d (a nonnegative polynomial has nec-


essarily even degree) is much harder to characterize than its subcone Σ[x]d of sums of squares. Indeed, while the latter has a simple semideﬁnite representation with lifting (i.e. Σ[x]d is the projection in Rs(2d) of a spectrahedron3 in a higher dimensional space), so far there is no such simple representation for the former. In addition, when d is ﬁxed, Blekherman [4] has shown that after proper normalization, the “gap” between Cd and Σ[x]d increases unboundedly with the number of variables.

We next provide a convergent hierarchy of (outer) semideﬁnite approximations (Cdk), k ∈ N, of Cd where each Cdk has a semideﬁnite representation with no lifting (i.e., no projection is needed and Cdk is a spectrahedron). To the best of our knowledge, this is the ﬁrst result of this kind.

Recall that with every f ∈ R[x]d is associated its vector of coeﬃcients f = (fα), α ∈ Nnd, in the canonical basis of monomials, and conversely, with every f ∈ Rs(d) is associated a polynomial f ∈ R[x]d with vector of coeﬃcients f = (fα) in the canonical basis. Recall that for every k = 1,...,

∞

0 if p = 2k + 1,

1 √2π

2/2 dx =

xp e−x

γp :=

k j=1(2j − 1) if p = 2k,

![image 14](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile14.png>)

![image 15](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile15.png>)

−∞

- as γ2k = (2k − 1)γ2(k−1) for every k ≥ 1.


- Corollary 3.5. Let µ be the probability measure on Rn which is the n-times product of the normal distribution on R, and so with moments y = (yα), α ∈ Nn,


n

∞

1 √2π

2/2dx , ∀α ∈ Rn.

e−x

xα

xα dµ =

- (3.12) yα = Rn


i

![image 16](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile16.png>)

![image 17](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile17.png>)

−∞

i=1

For every k ∈ N, let Cdk := {f ∈ Rs(2d) : Mk(f y) 0}, where Mk(f y) is the localizing matrix in (2.3) associated with y and f ∈ R[x]2d. Each Cdk is a closed convex cone and a spectrahedron.

Then Cd0 ⊃ Cd1 ··· ⊃ Cdk ··· ⊃ Cd and f ∈ Cd if and only if its vector of coeﬃcients f ∈ Rs(2d) satisﬁes f ∈ Cdk, for every k = 0,1,....

Proof. Following its deﬁnition (2.3), all entries of the localizing matrix Mk(f y) are linear in f ∈ Rs(2d), and so Mk(f y) 0 is an LMI. Therefore Cdk is a spectrahedron and a closed convex cone. Next, let K := Rn and let µ be as in Corollary 3.5 and so of the form (3.7) with ϕ as in (3.10). Then µ satisﬁes Carleman’s condition (2.2). Hence, by Theorem 3.4 with K = Rn, f is nonnegative on K if and only if (3.4) holds, which is equivalent to stating that Mk(f y) 0, k = 0,1,..., which in turn is equivalent to stating that f ∈ Cdk, k = 0,1,...

So the nested sequence of convex cones Cd0 ⊃ Cdk ··· ⊃ Cd deﬁnes arbitrary close outer approximations of Cd. In fact ∩∞k=0Cdk is closed and Cd = ∩∞k=0Cdk. It is worth emphasizing that each Cdk is a spectrahedron with no lifting, that is, Cdk is deﬁned solely in terms of the vector of coeﬃcients f with no additional variable (i.e., no projection is needed).

![image 18](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile18.png>)

3A spectrahedron is the intersection of the cone of positive semideﬁnite matrices with an aﬃne-linear space. Its algebraic representation is called a Linear Matrix Inequality (LMI).

For instance, the ﬁrst approximation Cd0 is just the set {f ∈ Rs(2d) : fdµ ≥ 0}, which is a half-space of Rs(2d). And with n = 2,

 

 





fdµ x1fdµ x2fdµ x1fdµ x21fdµ x1x2fdµ x2fdµ x1x2fdµ x22fdµ

f ∈ Rs(d) :

Cd1 =

,

0

 

 





or, equivalently, Cd1 is the convex basic semi-algebraic set: f ∈ Rs(2d) : fdµ ≥ 0

2

x2ifdµ fdµ ≥ xifdµ

, i = 1,2

2

x21fdµ x22fdµ ≥ x1x2fdµ

fdµ x21fdµ x22fdµ − x1x2fdµ

2

−

x1fdµ

2

x22fdµ − x2fdµ

2

x21fdµ +

2 x1fdµ x2fdµ x1x2fdµ ≥ 0 , where we have just expressed the nonnegativity of all principal minors of M1(f y).

A very similar result holds for the convex cone Cd(K) of polynomials of degree

- at most d, nonnegative on a closed set K ⊂ Rn.


- Corollary 3.6. Let K ⊂ Rn be a closed set and let µ be deﬁned in (3.7) where ϕ is a an arbitrary ﬁnite Borel measure whose support is exactly K.


For every k ∈ N, let Cdk(K) := {f ∈ Rs(d) : Mk(f y) 0}, where Mk(f y) is the

localizing matrix in (2.3) associated with y and f ∈ R[x]d. Each Cdk(K) is a closed convex cone and a spectrahedron.

Then Cd0(K) ⊃ Cd1(K)··· ⊃ Cdk(K)··· ⊃ Cd(K) and f ∈ Cd(K) if and only if its vector of coeﬃcients f ∈ Rs(d) satisﬁes f ∈ Cdk(K), for every k = 0,1,....

The proof which mimicks that of Corollary 3.5 is omitted. Of course, for practical computation, one is restricted to sets K where one may compute eﬀectively the moments of the measure µ. An example of such a set K is the positive orthant, in which case one may choose the measure µ in (3.11) for which all moments are explicitly available. For compact sets K let us mention balls, boxes, ellipsoids, and simplices. But again, any compact set where one knows how to compute all moments of some measure with support exactly K, is ﬁne.

To the best of our knowledge this is the ﬁrst characterization of an outer approximation of the cone Cd(K) in a relatively general context. Indeed, for the basic semi-algebraic set

- (3.13) K = {x ∈ Rn : gj(x) ≥ 0, j = 1,...,m },


Stengle’s Nichtnegativstellensatz [22] states that f ∈ R[x] is nonnegative on K if and only if

- (3.14) p f = f2s + q,


for some integer s and polynomials p,q ∈ P(g), where P(g) is the preordering4 associated with the gj’s. In addition, there exist bounds on the integer s and the degree of the s.o.s. weights in the deﬁnition of p,q ∈ P(g), so that in principle, when f is known, checking whether f ≥ 0 on K reduces to solving a single SDP to compute h,p in the nonnegativity certiﬁcate (3.14). However, the size of this SDP is potentially huge and makes it unpractical. Moreover, the representation of Cd(K) in (3.14) is not convex in the vector of coeﬃcients of f because it involves f2s as well as the product pf.

Remark 3.7. If in Corollary 3.6 one replaces the ﬁnite-dimensional convex cone Cd(K) ⊂ R[x]d with the inﬁnite-dimensional convex cone C(K) ⊂ R[x] of all polynomials nonnegative on K, and Cdk(K) ⊂ R[x]d with Ck(K) = {f ∈ Rs(2k) : Mk(f y) 0}, then the nested sequence of (increasing but ﬁnite-dimensional) convex cones Ck(K), k ∈ N, provides ﬁnite-dimensional approximations of C(K).

4. Application to polynomial optimization Consider the polynomial optimization problem

- (4.1) P : f∗ = inf x

{ f(x) : x ∈ K }, where K ⊆ Rn is closed and f ∈ R[x].

If K is compact let µ be a ﬁnite Borel measure with suppµ = K and if K is not compact, let ϕ be an arbitrary ﬁnite Borel measure with suppϕ = K and let µ be as in (3.7). In both cases, the sequence of moments y = (yα), α ∈ Nn, is well-deﬁned, and we assume that yα is available or can be computed, for every α ∈ Nn.

Consider the sequence of semideﬁnite programs:

- (4.2) λd = sup λ∈R


{λ : Md(fλ y) 0 }

where fλ ∈ R[x] is the polynomial x  → f(x) − λ. Notice that (4.2) has only one variable!

- Theorem 4.1. Consider the hierarchy of semideﬁnite programs (4.2) indexed by d ∈ N. Then:


- (i) (4.2) has an optimal solution λd ≥ f∗ for every d ∈ Nn.
- (ii) The sequence (λd), d ∈ N, is monotone nonincreasing and λd ↓ f∗ as d → ∞.


Proof. (i) Since f − f∗ ≥ 0 on K, by Theorem 3.2, λ := f∗ is a feasible solution of

- (4.2) for every d. Hence λd ≥ f∗ for every d ∈ N. Next, let d ∈ N be ﬁxed, and let λ be an arbitrary feasible solution of (4.2). From the condition Md(fλ y) 0, the


diagonal entry Md(fλ y)(1,1) must be nonnegative, i.e., λy0 ≤ α fα yα, and so, as we maximize and y0 > 0, (4.2) must have an optimal solution λd.

(ii) Obviously λd ≤ λm whenever d ≥ m, because Md(fλ y) 0 implies Mm(fλ y) 0. Therefore, the sequence (λd), d ∈ N, is monotone nonincreasing and being bounded below by f∗, converges to λ∗ ≥ f∗. Next, suppose that

![image 19](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile19.png>)

4The preordering P(g) associated with the gj’s is the set of polynomials of the form α∈{0,1}m σα g1α1 · · · gmαm where σα ∈ Σ[x] for each α.

λ∗ > f∗; ﬁx k ∈ N, arbitrary. The convergence λd ↓ λ∗ implies Mk(fλ∗ y) 0. As k was arbitrary, we obtain that Md(fλ∗ y) 0 for every d ∈ N. But then by

- Theorem 3.2 or Theorem 3.4, f − λ∗ ≥ 0 on K, and so λ∗ ≤ f∗, in contradiction with λ∗ > f∗. Therefore λ∗ = f∗.

For each d ∈ N, the semideﬁnite program (4.2) provides an upper bound on the optimal value f∗ only. We next show that the dual contains some information on global minimizers, at least when d is suﬃciently large.

4.1. Duality. Let Sd be the space of real symmetric s(d) × s(d) matrices. One may write the semideﬁnite program (4.2) as

(4.3) λd = sup

λ

{λ : λMd(y) Md(f y)},

which in fact is a generalized eigenvalue problem for the pair of matrices Md(y) and Md(f y). Its dual is the semideﬁnite program

inf

X∈Sd

{ X,Md(f y) : X,Md(y) = 1; X 0 }, or, equivalently,

(4.4) λ∗d = inf

σ K

f σ dµ :

K

σ dµ = 1; σ ∈ Σ[x]d .

So the dual problem (4.4) is to ﬁnd a sum of squares polynomial σ of degree at most 2d (normalized to satisfy σdµ = 1) that minimizes the integral fσdµ, and a simple interpretation of (4.4) is as follows:

With M(K) being the space of Borel probability measures on K, we know that f∗ = inf

ϕ∈M(K) K

fdϕ. Next, let Md(µ) ⊂ M(K) be the space of probability measures on K which have a density σ ∈ Σ[x]d with respect to µ. Then (4.4) reads

inf

ϕ∈Md(µ) K

fdϕ, which clearly shows why one obtains an upper bound on f∗. In-

deed, instead of searching in M(K) one searches in its subset Md(µ). What is not obvious at all is whether the obtained upper bound obtained in (4.4) converges to f∗ when the degree of σ ∈ Σ[x]d is allowed to increase!

- Theorem 4.2. Suppose that f∗ > −∞ and K has nonempty interior. Then :


- (a) There is no duality gap between (4.2) and (4.4) and (4.4) has an optimal

solution σ∗ ∈ Σ[x]d which satisﬁes

K

(f(x) − λd)σ∗(x)dµ(x) = 0.

- (b) If K is convex and f is convex, let x∗d := xσ∗(x)dµ(x). Then x∗d ∈ K


and f∗ ≤ f(x∗d) ≤ λd, so that f(x∗d) → f∗ as d → ∞. Moreover, if the set {x ∈ K : f(x) ≤ f0} is compact for some f0 > f∗, then any accumulation point x∗ ∈ K of the sequence (x∗d), d ∈ N, is a minimizer of problem (4.1), that is, f(x∗) = f∗.

Proof. (a) Any scalar λ < f∗ is a feasible solution of (4.2) and in addition, Md((f − λ)y) ≻ 0 because since K has nonempty interior and f − λ > 0 on K,

g,Md((f − λ)y)g =

(f(x) − λ)g(x)2µ(dx) > 0, ∀g ∈ R[x]d.

K

But this means that Slater’s condition5 holds for (4.2) which in turn implies that there is no duality gap and (4.4) has an optimal solution σ∗ ∈ Σ[x]d; see e.g. [23]. And so,

(f(x) − λd)σ∗(x)dµ(x) =

f σ∗ dµ − λd = 0.

K

K

- (b) Let ν be the Borel probability measure on K deﬁned by ν(B) = B σ∗dµ, B ∈ B. As f is convex, by Jensen’s inequality (see e.g. McShane [15]),


fσ∗dµ =

xdν = f(x∗d).

fdν ≥ f

K

K

K

In addition, if K is convex then x∗d ∈ K and so, λd ≥ f(x∗d) ≥ f∗. Finally if for some f0 > f∗, the set H := {x ∈ K : f(x) ≤ f0} is compact, and since λd → f∗, then f(x∗d) ≤ f0 for d suﬃciently large, i.e., x∗d ∈ H for suﬃciently large d. By compactness there is a subsequence (dℓ), ℓ ∈ N, and a point x∗ ∈ K such that x∗d

→ x∗ as ℓ → ∞. Continuity of f combined with the convergence f(x∗d) → f∗ yields f(x∗d

ℓ

) → f(x∗) = f∗ as ℓ → ∞. As the convergent subsequence (x∗d

) was arbitrary, the proof is complete.

ℓ

ℓ

So in case where f is a convex polynomial and K is a convex set, Theorem 4.2 provides a means of approximating not only the optimal value f∗, but also a global minimizer x∗ ∈ K.

In the more subtle nonconvex case, one still can obtain some information on global minimizers from an optimal solution σ∗ ∈ Σ[x]d of (4.4). Let ǫ > 0 be ﬁxed, and suppose that d is large enough so that f∗ ≤ λd ≤ f∗ + ǫ. Then, by Theorem 4.4(a),

(f(x) − f∗)σ∗(x)dµ(x) = λd − f∗ < ǫ.

K

As f − f∗ ≥ 0 on K, necessarily the measure dν = σ∗dµ gives very small weight to regions of K where f(x) is signiﬁcantly larger than f∗. For instance, if ǫ = 10−2 and ∆ := {x ∈ K : f(x) ≥ f∗ +1}, then ν(∆) ≤ 10−2, i.e., the set ∆ contributes to less than 1% of the total mass of ν. So if µ is uniformly distributed on K (which is a reasonable choice if one has to compute all moments of µ) then a simple inspection of the values of σ∗(x) provides some rough indication on where (in K) f(x) is close to f∗.

The interpretation (4.4) of the dual shows that in general the monotone convergence is only asymptotic and cannot be ﬁnite. Indeed if K has a nonempty interior then the probability measure dν = σdµ cannot be a Dirac measure at any global minimizer x∗ ∈ K. An exception is the discrete case, i.e., when K is a ﬁnite number of points, like in e.g. 0/1 programs. Indeed we get:

Corollary 4.3. Let K ⊂ Rn be a discrete set (x(k)) ⊂ Rn, k ∈ J, and let µ be the probability measure uniformly distributed in K, i.e.,

s

1 s

µ =

δx(k),

![image 20](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile20.png>)

k=1

where s = |J| and δx denote the Dirac measure at the point x. Then the optimal value λd of (4.2) satisﬁes λd = f∗ for some integer d.

![image 21](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile21.png>)

5For an optimization problem infx{f0(x) : fj(x) ≥ 0, j = 1, . . . , m}, Slater’s condition states that there exists x0 such that fj(x0) > 0 for every j = 1, . . . , m.

Proof. Let x∗ = x(j∗) (for some j∗ ∈ J) be the global minimizer of min{f(x) :

- x ∈ K}. For each k = 1,...,s there exists a polynomial qk ∈ R[x] such that qk(x(j)) = δk=j for every j = 1,...,s (where δk=j denotes the Kronecker symbol).


The polynomials (qk) are called interpolation polynomials. So let σ∗ := sqj2∗ ∈ Σ[x], so that

σ∗dµ = 1.

f(x)σ∗(x)dµ(x) = f(x(j∗)) = f∗ and

K

K

Hence as soon as d ≥ deg qj∗, σ∗ ∈ Σ[x]d is a feasible solution of (4.4), and so from f∗ = fσ∗dµ ≥ λ∗d ≥ λd ≥ f∗ we deduce that λ∗d = λd = f∗, the desired result.

There are several interesting cases where the above described methodology can apply, i.e., cases where y can be obtained either explicitly in closed form or numerically. In particular, when K is either:

- • A box B := ni=1[ai,bi] ⊂ Rn, with µ being the normalized Lebesgue measure on B. The sequence y = (yα) is trivial to obtain in closed form.
- • The discrete set {−1,1}n with µ being uniformly distributed and normal-

ized. Again the sequence y = (yα) is trivial to obtain in closed form. Notice that in this case we obtain a new hierarchy of semideﬁnite relaxations (with only one variable) for the celebrated MAXCUT problem (and any nonlinear 0/1 program).

- • The unit Euclidean ball B := {x : x 2 ≤ 1} with µ uniformly distributed, and similarly the unit sphere S := {x : x 2 = 1}, with µ being the rotation invariant probability measure on S. In both cases the moments y = (yα) are obtained easily.
- • A simplex ∆ ⊂ Rn, in which case if one takes µ as the Lebesgue measure then all moments of µ can be computed numerically. In particular, with d ﬁxed, this computation can be done in time polynomial time. See e.g. the recent work of [2].
- • The whole space Rn in which case µ may be chosen to be the product

measure ⊗ni=1νi with each νi being the normal distribution. Observe that one then obtains a new hierarchy of semideﬁnite approximations (upper bounds) for unconstrained global optimization. The corresponding monotone sequence of upper bounds converges to f∗ no matter if the problem has a global minimizer or not. This may be an alternative and/or a complement to the recent convex relaxations provided in Schweighofer [21] and Ha` and Vui [8] which also work when f∗ is not attained, and provide a convergent sequence of lower bounds.

- • The positive orthant Rn+, in which case µ may be chosen to be the product measure ⊗ni=1νi with each νi being the exponential distribution νi(B) =


R+∩B e−xdx, B ∈ B. In particular if x  → f(x) := xTAx where A ∈ Sn, then one obtains a hierarchy of numerical tests to check whether A is a copositive matrix. Indeed, if λd is an optimal solution of (4.3) then A is copositive if and only if λd ≥ 0 for all d ∈ N. Notice that we also obtain a hierarchy of outer approximations (COPd) ⊂ Sn of the cone COP of n × n copositive matrices. Indeed, for every A ∈ Sn, let fA be the quadratic form x  → fA(x) := xTAx. Then, for every d, the set

COPd := {A ∈ Sn : Md(fA y) 0 }

is a convex cone deﬁned only in terms of the coeﬃcients of the matrix A. It is even a spectrahedron since Md(fA y) is a linear matrix inequality in the coeﬃcients of A. And in view of Theorem 3.2(a), COP = d∈N COPd.

- 4.2. Examples. In this section we provide three simple examples to illustrate the above methodology.


- Example 1. Consider the global minimization on K = R2+ of the Motzkin-like polynomial x  → f(x) = x21x22 (x21 +x22 −1) whose global minimum is f∗ = −1/27 ≈ −0.037, attained at (x∗1,x∗2) = (± 1/3,± 1/3). Choose for µ the probability

![image 22](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile22.png>)

![image 23](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile23.png>)

measure µ(B) := B e−x

1−x2dx, B ∈ B(R2+), for which the sequence of moments y = (yij), i,j ∈ N, is easy to obtain. Namely yij = i!j! for every i,j ∈ N. Then the semideﬁnite relaxations (4.2) yield λ0 = 92, λ1 = 1.5097, and λ14 = −0.0113, showing a signiﬁcant and rapid decrease in ﬁrst iterations with a long tail close to f∗, illustrated in Figure 1. Then after d = 14, one encounters some numerical problems and we cannot trust the results anymore.

If we now minimize the same polynomial f on the box [0,1]2, one choose for µ the probability uniformly distributed on [0,1]2, whose moments y = (yij), i,j ∈ N, are also easily obtained by yij = (i + 1)−1(j + 1)−1. Then one obtains λ0 = 0.222, λ1 = −0.055, and λ10 = −0.0311, showing again a rapid decrease in ﬁrst iterations with a long tail close to f∗, illustrated in Figure 2.

0 2 4 6 8 10 12 14

−0.2

0

0.2

0.4

0.6

- 0.8

- 1


1.2

1.4

1.6

Figure 1. Minimizing the Motzkin-like polynomial in R2+

- Example 2. Still on K = R2+, consider the global minimization of the polynomial x  → x21 + (1 − x1x2)2 whose global minimum f∗ = 0 is not attained. Again,


1−x2dx, B ∈ B(R2+). Then the semideﬁnite relaxations (4.2) yield λ0 = 5, λ1 = 1.9187 and λ15 = 0.4795, showing again a signiﬁcant and rapid decrease in ﬁrst iterations with a long tail close to f∗,

choose for µ the probability measure µ(B) := B e−x

0.03

0.02

0.01

0

−0.01

−0.02

−0.03

−0.04

1 2 3 4 5 6 7 8 9 10 11

Figure 2. Minimizing the Motzkin-like polynomial in [0,1]2

illustrated in Figure 3; numerical problems occur after d = 15. However, this kind of problems where the global minimum f∗ is not attained, is notoriously diﬃcult. Even the semideﬁnite relaxations deﬁned in [8] (which provide lower bounds on f∗) and especially devised for such problems, encounter numerical diﬃculties; see [8, Example 4.8].

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5

- 5




0 2 4 6 8 10 12 14 16

Figure 3. Minimizing x21 + (1 − x1x2)2 on R2+

- Example 3. The following example illustrates the duality results of Section §4.1. The univariate polynomial x  → f(x) := 0.375−5x+21x2−32x3+16x4 displayed in Fig 4 has two global minima at x∗1 = 0.1939 and x∗2 = 0.8062, with f∗ = −0.0156. In Fig 5 is plotted the sequence of upper bounds λd → f∗ as dˆ → ∞, with again a rapid decrease in ﬁrst iterations. One has plotted in Fig 6 the s.o.s. polynomial x  → σ(x), optimal solution of (4.4) with d = 10, associated with the probability density σ(x)dx as explained in §4.1. As expected, two peaks appear at the points x˜i ≈ x∗i , i = 1,2.

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

−0.05

0

0.05

0.1

0.15

0.2

0.25

0.3

0.35

0.4

Figure 4. f(x) = 0.375 − 5x + 21x2 − 32x3 + 16x4 on [0,1]

- Example 4. We ﬁnally consider a discrete optimization problem, namely the celebrated MAXCUT problem


f∗ = min

{xTQx : x ∈ {−1,1}n},

x

where Q = (Qij) ∈ Rn×n is a real symmetric matrix whose all diagonal elements vanish. The measure µ is uniformly distributed on {−1,1}n so that its moments are readily available. We ﬁrst consider the equal weights case, i.e., Qij = 1/2 for all (i,j) with i = j in which case f∗ = −⌊n/2⌋. With n = 11 the successive values for λd, d ≤ 4, are displayed in Table 1 and λ4 is relatively close to f∗. Next we have generated ﬁve random instances of MAXCUT with n = 11 but Qij = 0 with probability 1/2, and if Qij = 0 it is randomly generated using the Matlab “rand” function. The successive values of λd, d ≤ 4, are displayed in Table 2, and again, λ4 is quite close to f∗6.

The above examples seem to indicate that even though one chooses a measure µ uniformly distributed on K, one obtains a rapid decrease in the ﬁrst iterations and

![image 24](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile24.png>)

6The optimal value f∗ has been computed using the GloptiPoly software [10] dedicated to solving the Generalized Problem of Moments

0.08

0.07

0.06

0.05

0.04

0.03

0.02

0.01

0

−0.01

1 2 3 4 5 6 7 8 9 10

Figure 5. Minimizing 0.375 − 5x + 21x2 − 32x3 + 16x4 on [0,1]

5

4.5

4

3.5

3

2.5

2

1.5

1

0.5

0

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

Figure 6. The probability density σ(x)dx on [0,1]

then a slow convergence close to f∗. If on the one hand the convergence to f∗ is likely to be slow, on the other hand, one has to solve semideﬁnite programs (4.2) with only one variable! In fact solving the semideﬁnite program (4.3) is computing the smallest generalized eigenvalue associated with the pair of real symmetric matrices (Md(f y),Md(y)), for which specialized codes are available (instead of using

d d = 0 d = 1 d = 2 d = 3 d = 4 f∗ λd 0 -1 -2.662 -3.22 -4 -5 Table 1. MAXCUT: n = 11; Q(i,j) = 1 for all i = j.

![image 25](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile25.png>)

![image 26](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile26.png>)

![image 27](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile27.png>)

![image 28](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile28.png>)

![image 29](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile29.png>)

![image 30](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile30.png>)

![image 31](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile31.png>)

![image 32](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile32.png>)

![image 33](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile33.png>)

![image 34](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile34.png>)

![image 35](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile35.png>)

![image 36](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile36.png>)

![image 37](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile37.png>)

![image 38](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile38.png>)

![image 39](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile39.png>)

![image 40](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile40.png>)

![image 41](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile41.png>)

![image 42](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile42.png>)

![image 43](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile43.png>)

![image 44](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile44.png>)

![image 45](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile45.png>)

![image 46](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile46.png>)

d λ0 λ1 λ2 λ3 λ4 f∗

![image 47](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile47.png>)

![image 48](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile48.png>)

![image 49](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile49.png>)

![image 50](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile50.png>)

![image 51](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile51.png>)

![image 52](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile52.png>)

![image 53](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile53.png>)

![image 54](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile54.png>)

![image 55](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile55.png>)

![image 56](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile56.png>)

![image 57](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile57.png>)

![image 58](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile58.png>)

![image 59](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile59.png>)

![image 60](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile60.png>)

![image 61](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile61.png>)

![image 62](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile62.png>)

![image 63](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile63.png>)

![image 64](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile64.png>)

![image 65](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile65.png>)

![image 66](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile66.png>)

![image 67](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile67.png>)

Ex1 0 -1.928 -3.748 -5.22 -6.37 -7.946 Ex2 0 -1.56 -3.103 -4.314 -5.282 -6.863 Ex3 0 -1.910 -3.694 -5.078 -6.161 -8.032 Ex4 0 -2.164 -4.1664 -5.7971 -7.06 -9.198 Ex5 0 -1.825 -3.560 -4.945 -5.924 -7.467 Table 2. MAXCUT: n = 11; Q random.

![image 68](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile68.png>)

![image 69](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile69.png>)

![image 70](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile70.png>)

![image 71](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile71.png>)

![image 72](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile72.png>)

![image 73](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile73.png>)

![image 74](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile74.png>)

![image 75](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile75.png>)

![image 76](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile76.png>)

![image 77](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile77.png>)

![image 78](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile78.png>)

![image 79](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile79.png>)

![image 80](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile80.png>)

![image 81](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile81.png>)

![image 82](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile82.png>)

![image 83](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile83.png>)

![image 84](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile84.png>)

![image 85](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile85.png>)

![image 86](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile86.png>)

![image 87](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile87.png>)

![image 88](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile88.png>)

![image 89](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile89.png>)

![image 90](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile90.png>)

![image 91](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile91.png>)

![image 92](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile92.png>)

![image 93](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile93.png>)

![image 94](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile94.png>)

![image 95](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile95.png>)

![image 96](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile96.png>)

![image 97](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile97.png>)

![image 98](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile98.png>)

![image 99](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile99.png>)

![image 100](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile100.png>)

![image 101](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile101.png>)

![image 102](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile102.png>)

![image 103](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile103.png>)

![image 104](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile104.png>)

![image 105](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile105.png>)

![image 106](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile106.png>)

![image 107](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile107.png>)

![image 108](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile108.png>)

a solver for semideﬁnite programs). However, one has to remember that the choice is limited to measures µ with suppµ = K and whose moments are available or easy to compute. Hence, the present methodology is so far limited to simple sets K as described before. Finally, analyzing how the convergence to f∗ depends on µ is beyond the scope of the present paper and is a topic of further research.

- 4.3. Discusssion. In nonlinear programming, sequences of upper bounds on the global minimum f∗ are usually obtained from feasible points x ∈ K, e.g., via some (local) minimization algorithm. But for non convex problems, providing a sequence of upper bounds that converges to the global minimum f∗ is in general impossible unless one computes points on a grid whose mesh size tends to zero. In the above methodology one provides a monotone nonincreasing sequence of upper bounds converging to f∗ for polynomial optimization problems on sets K, non necessarily compact but such that one may compute all moments of some ﬁnite Borel measure µ with suppµ = K. In fact, if there are only ﬁnitely many (say up to order 2d) moments available then one obtains a ﬁnite sequence of upper bounds.


In contrast to the hierarchy of semideﬁnite relaxations in e.g. [12, 13] which provide lower bounds converging to f∗ when K is a compact basic semi-algebraic set, the convergence of the upper bounds to f∗ is only asymptotic and never ﬁnite, except when K is a discrete set. However, and even if we expect the convergence to be rather slow when close to f∗, to our knowledge it is the ﬁrst approach of this kind, and in a few iterations one may obtain upper bounds which (even if crude) complements the lower bounds obtained in [12] (in the compact case).

Also note that to solve (4.3) several improvements are possible. For instance, we have already mentioned that it could be solved via specialized packages for generalized eigenvalue problems. Next, if instead of using the canonical basis of monomial (xα), one now expresses the moment matrix Md(y) with rows and columns indexed in the basis of polynomials (pα) ⊂ R[x] (up to degree d) orthogonal7 with respect to µ, then Md(y) becomes the identity matrix. And so problem (4.3) reduces to a standard eigenvalue problem, namely that of computing the smallest eigenvalue of the (real and symmetric) localizing matrix Md(f y) (expressed in the basis of

![image 109](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile109.png>)

7A family of univariate polynomials (pk) ⊂ R[x] is orthogonal with respect to a ﬁnite measure µ on R if pipkdµ = δi=k. For extensions to the multivariate case see e.g. [6, 9].

orthogonal polynomials)! And it turns out that computing the orthogonal polynomials is easy once the moment matrix Md(y) is available, since they can be obtained via computing certain determinants, as explained in e.g. [6, 9].

Inverse problem from moments. Finally, observe that the above methodology perfectly ﬁts inverse problems from moments, where precisely some Borel measure µ is known only from its moments (via some measurement device), and one wishes to recover (or approximately recover) its support K from the known moments; see e.g. the work of Cuyt et al. [5] and the many references therein. Hence if f ∈ R[x] is ﬁxed then by deﬁnition f − f∗ ≥ 0 (on K) provides a strong valid (polynomial) inequality for the unknown set K. So computing an optimal solution λd of (4.2) for d suﬃciently large, will provide an almost-valid polynomial inequality f − λd ≥ 0 for K. One may even let f ∈ R[x]d be unknown and search for the “best” valid inequality f(x) − f∗ ≥ 0 where f varies in some family (e.g. linear or quadratic polynomials) and minimizes ome appropriate (linear or convex) objective function of its vector of coeﬃcents f.

5. Conclusion

In this paper we have presented a new characterization of nonnegativity on a closed set K which is based on the knowledge of a single ﬁnite Borel measure µ with suppµ = K. It permits to obtain a hierarchy of spectrahedra which provides a nested sequence of outer approximations of the convex cone of polynomials of degree at most d, nonnegative on K. When used in polynomial optimization for certain “simple sets” K, one obtains a hierarchy of semideﬁnite approximations (with only one variable) which provides a nonincreasing sequence of upper bounds converging to the global optimum, hence a complement to the sequence of upper bounds provided by the hierarchy of semideﬁnite relaxations deﬁned in e.g. [12, 13] when K is compact and basic semi-algebraic. A topic of further investigation is to analyze the eﬃciency of such an approach on a sample of optimization problems on simple closed sets like the whole space Rn, the positive orthant Rn+, a box, a simplex, or an ellipsoid, as well as for some inverse problems from moments.

6. appendix Proof of Theorem 3.4.

Proof. The only if part is exactly the same as in the proof of Theorem 3.2. For the if part, let z = (zα) be the sequence deﬁned in (3.5). The sequence z is well deﬁned because x  → xαf(x) is µ-integrable for all α ∈ Nn. Indeed, if f is a polynomial (so that µ is deﬁned in (3.7)) we have seen that all moments of µ are ﬁnite and since xαf(x) is a polynomial the result follows. If f is not a polynomial (so that µ is deﬁned in (3.9)) then

n

|xi|)dϕ(x) ≤ ϕ(Rn)

|xα|exp(−

|xα f(x)|dµ(x) ≤

αi!,

K

K

i=1

i

where we have used that |xα

i | ≤ αi!exp|xi|, and |f|/(1 + f2) ≤ 1 for all x. As in the proof of Theorem 3.2, the set function B  → ν(B) := B fdµ, B ∈ B, is a signed Borel measure because again ν can be written as the diﬀerence ν1 − ν2 of the two positive Borel measures ν1,ν2 in (3.1)-(3.2). With same majorizations as above, both ν1 and ν2 are ﬁnite Borel measures and so ν is a ﬁnite signed Borel measure.

i

The same arguments as in the proof of Theorem 3.2 show that Md(z) 0 for every d ∈ N. Next, the sequence z satisﬁes the generalized Carleman’s condition (2.2).

Indeed, ﬁrst consider the case where f is a polynomial (and so µ is as in (3.7)). Let 1 ≤ i ≤ n be ﬁxed arbitrary, and let 2s ≥ degf. Observe that whenever |α| ≤ k, |x|α ≤ |xj|k on the subset Wj := {x ∈ Rn \ [−1,1]n : |xj| = maxi |xi|}. And so, |f(x)| ≤ f 1 |xj|2s for all x ∈ Wj (and where f 1 := α |fα|). Hence,

f(x)x2ikdµ(x)

Lz(x2ik) =

K

n

x2(j k+s)dµ(x)

|f(x)|x2ikdµ(x) + f 1

≤

K∩[−1,1]n

j=1 K∩WJ

- (6.1) ≤ f 1µ(K) + Mn f 1 (2(k + s))! ≤ 2Mn f 1 (2(k + s))!,

where M is as in (3.8) and assuming with no loss of generality that µ(K) ≤ Mn(2(k + s))! (otherwise rescale ϕ). And so we have

Lz(x2ik)−1/2k ≥ (2Mn f 1)−1/2k (2(k + s))!)−1/2(k+s)

(k+s)/k

≥

- 1

![image 110](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile110.png>)

- 2


(2(k + s))!)−1/2(k+s)

(k+s)/k

≥

- 1

![image 111](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile111.png>)

- 2


1 2(k + s)

![image 112](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile112.png>)

(k+s)/k

,

where k ≥ k0 is suﬃciently large so that (2Mn f 1)−1/2k ≥ 1/2. Therefore,

∞

k=1

Lz(x2ik)−1/2k ≥

- 1

![image 113](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile113.png>)

- 2


∞

k=k0

1 2(k + s)

![image 114](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile114.png>)

(k+s)/k

= +∞,

where the last equality follows from ∞k=1(2k)−1 = +∞. Indeed, (2(k1+s))(k+s)/k = (2(k1+s))(2(k1+s))s/k and (2(k1+s))s/k ≥ 1/2 whenever k is suﬃciently large, say k ≥ k1. Hence the sequence z satisﬁes Carleman’s condition (2.2).

![image 115](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile115.png>)

![image 116](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile116.png>)

![image 117](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile117.png>)

![image 118](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile118.png>)

If f is not a polynomial then µ is as in (3.9) and so

Lz(x2ik) = x2ik

exp(− ni=1 |xi|) 1 + f2

![image 119](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile119.png>)

f(x)dϕ(x)

≤ x2ik

exp(− ni=1 |xi|) 1 + f2 |f(x)|dϕ(x)

![image 120](<2010-lasserre-new-look-nonnegativity-closed_images/imageFile120.png>)

≤ x2ik exp −

n

i=1

- (6.2) |xi| dϕ(x) ≤ (2k)!M,

where we have used that |f|/(1 + f2) ≤ 1 for all x, and x2ik ≤ (2k)!exp|xi|. And so again, the sequence z satisﬁes Carleman’s condition (2.2).

Next, as Md(z) 0 for every d ∈ N, by Proposition 2.1, z is the moment sequence of a measure ψ on Rn and ψ is determinate. In addition, from the deﬁnition (3.5) of ν and z, we have

- (6.3) Rn


xαdν(x), ∀α ∈ Nn.

xα dψ(x) = zα =

K

But then using ν = ν1 − ν2 in (3.1)-(3.2), (6.3) reads xα d(ψ + ν2)(x) =

xαdν1(x), ∀α ∈ Nn.

- (6.4) Rn


K

Let v = (vα), α ∈ Nn, be the sequence of moments associated with ν1. Of course, Md(v) 0 for all d ∈ N. Next,

x2ik |f(x)|dµ(x),

x2ik f(x)dµ(x) ≤

Lv(x2ik) =

B1

K

and so, depending on whether f is a polynomial or not, we obtain Lv(x2ik) ≤ 2Mn f 1 (2(k + s))! as in (6.1) or Lv(x2ik) ≤ (2k)!M as in (6.2). In both cases the sequence v satisﬁes Carleman’s condition (2.2) and since Md(v) 0 for all d ∈ N, by Proposition 2.1, ν1 is moment determinate. But then (6.4) yields ν1 = ψ + ν2, or equivalently, ψ = ν1 − ν2 (= ν), that is, ν is a positive measure. The rest of the proof is exactly the same as for proof of Theorem 3.2.

References

- [1] K.M. Anstreicher, S. Burer. Computable representations for convex hulls of low-dimensional quadratic forms, Math. Program. Ser. B 124 (2010), pp. 33?43.
- [2] V. Baldoni, N. Berline, J. De Loera, M. K¨ppe, and M. Vergne. How to integrate a polynomial on a simplex, Math. Comp. 80 (2011), pp. 297–325.
- [3] C. Berg. The multidimensional moment problem and semi-groups, Proc. Symp. Appl. Math. 37 (1980), pp. 110–124.
- [4] G. Blekherman. There are signiﬁcantly more nonnegative polynomials than sums of squares, Israel J. Math. 153 (2006), pp. 355–380.
- [5] A. Cuyt, G. Golub, P. Milanfar and B. Verdonk. Mutlidimensional integral inversion with application in shape reconstruction, SIAM J. Sci. Comput. 27 (2005), pp. 1058–1070.
- [6] C.F. Dunkl and Y. Xu. Orthogonal Polynomials of Several Variables, Cambridge Univ. Press., Cambridge, 2001.
- [7] M. Du¨r. Copositive Programming: A survey, Optimization-online, 2009.
- [8] H`a Huy Vui and T. S. Pham. Global optimization of polynomials using the truncated tangency variety and sums of squares, SIAM J. Optim. 19 (2008), pp. 941–951.
- [9] J.W. Helton, J.B. Lasserre, and M. Putinar. Measures with zeros in the inverse of their moment matrix, Ann. Probab. 36 (2008), pp. 1453–1471.
- [10] D. Henrion, J.B. Lasserre, Y. L¨ofberg. Gloptipoly 3: moments, optimization and semideﬁnite programming, Optim. Methods and Softwares 24 (2009), pp. 761–779.
- [11] P.H. Maserick and C. Berg. Exponentially bounded positive deﬁnite functions. Ill, J. Math. 28 (1984), pp. 162– 179.
- [12] J.B. Lasserre. Global optimization with polynomials and the problem of moments, SIAM J. Optim. 11 (2001), pp. 796–817.
- [13] J.B. Lasserre. Moments, Positive Polynomials and Their Applications, Imperial College Press, London, 2009.
- [14] J.B. Lasserre and M. Putinar. Positivity and optimization for semi-algebraic functions, SIAM J. Optim. 20 (2010), pp. 3364–3383.
- [15] E.J. McShane. Jensen’s inequality, Bull. Amer. Math. Soc. 43 (1937), pp. 521–527.
- [16] M. Marshall and T. Netzer. Positivstellensa¨tze for real function algebras (2010). arXiv:1004.4521v1.
- [17] A.E. Nussbaum. Quasi-analytic vectors. Ark. Mat. 6 (1966), pp. 179–191.
- [18] M. Putinar. Positive polynomials on compact semi-algebraic sets, Indiana Univ. Math. J. 42

(1993), 969–984.

- [19] H.L. Royden. Real Analysis, 3rd. ed., Macmillan Publishing Company, New York, 1988.
- [20] K. Schmu¨dgen. The K-moment problem for compact semi-algebraic sets, Math. Ann. 289

(1991), 203–206.

- [21] M. Schweighofer. Global optimization of polynomials using gradient tentacles and sums of squares, SIAM J. Optim. 17 (2006), pp. 920–942.


- [22] G. Stengel. A Nullstellensatz and a Positivstellensatz in semialgebraic geometry, Math. Ann. 207, pp. 87–97.
- [23] L. Vandenberghe and S. Boyd. Semideﬁnite programming, SIAM Rev. 38 (1996), pp. 49–95.


LAAS-CNRS and Institute of Mathematics, University of Toulouse, LAAS, 7 avenue du Colonel Roche, 31077 Toulouse C´edex 4,France

E-mail address: lasserre@laas.fr

