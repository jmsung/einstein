arXiv:1905.02575v1[quant-ph]4May2019

The set of separable states has no ﬁnite semideﬁnite representation except in dimension 3 × 2

Hamza Fawzi∗ May 4, 2019

Abstract

Given integers n ≥ m, let Sep(n,m) be the set of separable states on the Hilbert space Cn ⊗ Cm. It is well-known that for (n,m) = (3,2) the set of separable states has a simple description using semideﬁnite programming: it is given by the set of states that have a positive partial transpose. In this paper we show that for larger values of n and m the set Sep(n,m) has no semideﬁnite programming description of ﬁnite size. As Sep(n,m) is a semialgebraic set this provides a new counterexample to the Helton-Nie conjecture, which was recently disproved by Scheiderer in a breakthrough result. Compared to Scheiderer’s approach, our proof is elementary and relies only on basic results about semialgebraic sets and functions.

# 1 Introduction

Entanglement is a fundamental aspect of quantum mechanics. The set of separable states (i.e., nonentangled states) on the Hilbert space Cn ⊗ Cm is deﬁned as:

Sep(n,m) = conv xx† ⊗ yy† : x ∈ Cn,|x| = 1,y ∈ Cm,|y| = 1 .

Here x† = x¯T indicates conjugate transpose, |x|2 = x†x = ni=1 |xi|2 and conv denotes the convex hull. The set Sep(n,m) lives in the space Hnm of Hermitian matrices of size nm × nm, and it is

full-dimensional in the subspace of matrices of trace equal to one.

A fundamental computational task in quantum information is to decide membership in the convex set Sep(n,m). One of the ﬁrst tests designed to check whether a state ρ ∈ Hnm is separable is the Peres-Horodecki criterion [Per96, HHH96] (also known as the Positive Partial Transpose (PPT) criterion). It is based on the observation that for any ρ ∈ Sep(n,m), (I ⊗ T)(ρ) is positive semideﬁnite where I is the identity map, and T the transpose map. Indeed one can easily verify that if ρ = xx† ⊗ yy† then (I ⊗ T)(ρ) = xx† ⊗ (yy†)T = xx† ⊗ y¯y¯† ≥ 0. In other words we have the inclusion Sep(n,m) ⊆ PPT(n,m) where

PPT(n,m) = ρ ∈ Hnm : ρ ≥ 0, (I ⊗ T)(ρ) ≥ 0, and Tr[ρ] = 1 . (1)

It is known, from earlier work of Woronowicz [Wor76], that we have equality Sep(n,m) = PPT(n,m) if, and only if n+m ≤ 5. Thus, the smallest cases where Sep(n,m) = PPT(n,m) are (n,m) = (4,2) and (n,m) = (3,3).

![image 1](<2019-fawzi-set-separable-states-has_images/imageFile1.png>)

∗Department of Applied Mathematics and Theoretical Physics, University of Cambridge. Email: h.fawzi@damtp.cam.ac.uk.

Semideﬁnite programming The description of the set PPT(n,m) in Equation (1) allows us to decide membership, and optimize linear functions on PPT(n,m), via semideﬁnite programming. Semideﬁnite programming is a fundamental tool in optimization that has played a crucial role in recent developments in quantum information theory. We say that a convex set C has a semideﬁnite representation (also called a semideﬁnite lift) of size r if it can be expressed as

C = π(S) (2)

where π : RD → Rd is a linear map and S ⊂ RD is a convex set deﬁned using a linear matrix inequality

S = {w ∈ RD : M0 + w1M1 + ··· + wDMD ≥ 0} (3)

where M0,... ,MD are Hermitian matrices of size r × r. A set S of the form (3) is known as a spectrahedron. In this paper we are most interested in when a semideﬁnite representation of ﬁnite size exists, and call this simply a semideﬁnite representation throughout. If a convex set C admits a semideﬁnite representation, then optimizing a linear function on C can be cast as a semideﬁnite program. Equation (1) gives a semideﬁnite representation of PPT(n,m).

Horodecki’s criterion The set of separable states has the following well-known description due to the Horodeckis [HHH96]:

Sep(n,m) = {ρ ∈ Hnm : Tr[ρ] = 1 and (I ⊗ Φ)(ρ) ≥ 0 ∀Φ : Mm → Mn positive}. (4)

Here Mk = Ck×k and a C-linear map Φ : Mm → Mn is positive if it is Hermitian preserving and if Φ(X) ≥ 0 for all X ≥ 0. When n = m, the relaxation PPT(n,m) corresponds to having only the identity and transpose maps in Equation (4), which are both positive. A recent result of Skowronek [Sko16] shows that when n = m = 3, there is no ﬁnite family of positive maps Φ1,... ,Φk : M3 → M3 such that Sep(3,3) = ρ ∈ H9 : (I ⊗ Φi)(ρ) ≥ 0 ∀i = 1,... ,k . Note that the right-hand side of the previous equation is a speciﬁc semideﬁnite representable set. Thus Skowronek’s result rules out certain speciﬁc semideﬁnite representations for Sep(3,3).1

DPS hierarchy In [DPS04], Doherty, Parrilo and Spedalieri proposed a complete hierarchy of approximations to the set of separable states based on semideﬁnite programming. The ﬁrst level of the hierarchy coincides with the PPT test, and subsequent levels form tighter and tighter convex relaxations of the set of separable states. If we denote the convex relaxation at level k by DPSk(n,m) we have (dropping the (n,m)):

Sep ⊆ ··· ⊆ DPSk ⊆ DPSk−1 ⊆ ··· ⊆ DPS1 = PPT.

The key property of the DPS hierarchy is that each set DPSk has a semideﬁnite representation of size min(n,m)O(k). The hierarchy is known to be complete, meaning that if ρ ∈/ Sep, then there

exists a ﬁnite k such that ρ ∈/ DPSk. The integer k however depends on the state ρ and it is known that, unless n + m ≤ 5, there is no ﬁnite k such that DPSk(n,m) = Sep(n,m) [DPS04, Section VIII.B].

![image 2](<2019-fawzi-set-separable-states-has_images/imageFile2.png>)

1The result of Skrownek is in fact more general than this, and rules any formulation of the form ρ : (I ⊗ Φi)((I ⊗ B)ρ(I ⊗ B†)) ≥ 0 ∀i = 1, . . . , k, ∀B ∈ M3 where Φ1, . . . , Φk is a ﬁnite set of positive maps.

Contributions The main result of this paper is

- Theorem 1. If Sep(n,m) = PPT(n,m) then Sep(n,m) has no (ﬁnite) semideﬁnite representation. In other words, Sep(n,m) has no semideﬁnite representation when n + m > 5.


- Remark 1. Some remarks concerning Theorem 1:


- • Note that Theorem 1 contains as a special case the fact that whenever Sep(n,m) = PPT(n,m), then there is no representation of Sep(n,m) as {ρ ∈ Hnm : Tr[ρ] = 1 and (I⊗Φi)(ρ) ≥ 0, ∀i = 1,... ,k} where Φ1,... ,Φk : Mm → Mn is a ﬁnite family of positive maps. This is because the latter set is semideﬁnite representable (in fact it is a spectrahedron). Let us mention that if one is only interested in approximating the set Sep(n,m), Aubrun and Szarek [AS17b] gave a lower bound on the number k of positive maps needed.
- • Our result also includes as a special case the fact that there is no ﬁnite k such that DPSk(n,m) = Sep(n,m), when n + m > 5. We note that our result is a strict generalization of this fact. Indeed, the failure of the DPS hierarchy to converge in a ﬁnite number of levels does not preclude by itself the existence of another semideﬁnite program that represents Sep(n,m) exactly. There are well-known examples of convex sets where the sum-of-squares hierarchy (of which DPS can be seen as a particular instance) is never exact and yet a ﬁnite semideﬁnite representation does exist, see e.g., [NPS10, Example 3.7].
- • Observe that if Sep(n,m) has no semideﬁnite representation, then the same is true for Sep(N,m) for N ≥ n. This is because Sep(n,m) can be realized as a linear section of Sep(N,m) as follows:


Sep(n,m) ≃ {ρ ∈ Sep(N,m) : (Tr2 ρ)ii = 0 ∀i = n + 1,... ,N}

where Tr2 ρ is the result of tracing out the second subsystem from ρ. Indeed, setting (Tr2 ρ)ii = 0 implies that in any representation of ρ as ρ = k pkxkx†k ⊗ykyk†, the vectors xk must satisfy (xk)i = 0 for all i = n + 1,... ,N, i.e., that xk ∈ Cn × {0}N−n ≃ Cn. To prove our theorem it thus suﬃces to prove that Sep(3,3) and Sep(4,2) have no semideﬁnite representations.

Helton-Nie conjecture The question of ﬁnding semideﬁnite representations for convex sets has attracted a lot of attention in the optimization community [Nem06, GPT13]. Helton and Nie [HN09] gave suﬃcient conditions for a set to have a semideﬁnite representation, and conjectured that any convex semialgebraic set has a semideﬁnite representation. (A set is semialgebraic set if it can be described using a ﬁnite boolean combinations of polynomial equations and inequalities. One can verify that Sep(n,m) is a semialgebraic set, see Section 2.3.) In his breakthrough paper, Scheiderer [Sch18] disproved this conjecture and exhibited convex semialgebraic sets that have no semideﬁnite representations.

Our proof of Theorem 1 is inspired from the arguments of Scheiderer. Compared to the paper of Scheiderer the present paper has two main contributions. First, the proof we give simpliﬁes the arguments of Scheiderer and does not rely on any specialized results from algebraic geometry. We only use basic results from analysis (Taylor expansions), and some standard facts about semialgebraic sets and functions which are elementary to state. The proof should thus be accessible to readers in quantum information and optimization. The second contribution is the application of the method of proof for Sep(n,m) which is deﬁned in terms of complex numbers. This turns out to cause certain diﬃculties as certain standard facts about real polynomials are not true about Hermitian polynomials, particularly on the relation between homogeneous polynomials and their dehomogenizations (see Section 5 and Appendix A for more details).

Main technical result Our main technical result, Theorem 2 below and of which Theorem

- 1 is a corollary, gives a general way to construct a convex set with no semideﬁnite representation from a nonnegative Hermitian polynomial that is not a sum of squares. We recall that a Hermitian polynomial p(z) is a polynomial with complex coeﬃcients in the indeterminates


(z,z¯) = (z1,... ,zn,z¯1,... ,z¯n) such that p(z) ∈ R for all z ∈ Cn. A Hermitian polynomial is a sum of squares if it can be written as a sum of squares of Hermitian polynomials. (More details about Hermitian polynomials are given in Section 2.) For the statement of the theorem, we use the monomial notation zu = ni=1 ziui for u ∈ Nn.

- Theorem 2 (General theorem). Let p(z) = (u,v)∈A puvzuz¯v be a Hermitian polynomial supported on A ⊂ Nn × Nn, and assume that p is nonnegative on Cn but not a sum of squares. Assume furthermore that A is downward closed, i.e., if (u,v) ∈ A then all (u′,v′) ∈ Nn×Nn with 0 ≤ u′ ≤ u


and 0 ≤ v′ ≤ v are in A. Deﬁne the monomial map mA : Cn → C|A|, z  → [zuz¯v](u,v)∈A for z ∈ Cn. Then the convex set

CA = cl conv {mA(z) : z ∈ Cn} (5) is not semideﬁnite representable, where cl denotes topological closure.

The set of separable states is of the form (5) for well-chosen set A. Indeed, dropping the normalization condition and letting SEP(n,m) be the convex cone of separable states, we have:

: (x,y) ∈ Cn × Cm

SEP(n,m) = conv [xix¯jyky¯l]1≤i,j≤n 1≤k,l≤m

= conv xαx¯βyγy¯δ

: (x,y) ∈ Cn × Cm

|α|=|β|=|γ|=|δ|=1

where for ζ ∈ Nk we let |ζ| = ki=1 ζi. This shows that SEP(n,m) = CA where A = {(α,β,γ,δ) ∈ (Nn × Nn) × (Nm × Nm) : |α| = |β| = |γ| = |δ| = 1} . (6)

The attentive reader will notice that this set A is not downward closed, and so does not satisfy the condition of Theorem 2. As a matter of fact, to prove Theorem 1 we apply Theorem 2 with a dehomogenization of A which satisﬁes the downward closed condition, and then homogenize back to get the desired convex cone. The details are explained in Section 5.

Overview of proof We brieﬂy sketch the main ideas for the proof of Theorem 2.

- • We ﬁrst show that if the set CA has a semideﬁnite representation, then there exists a ﬁnite number of functions f1,... ,fr : R2n ≃ Cn → R such that any nonnegative Hermitian polyno-

mial supported on A∪{(0,0)} can be written as a sum of squares from spanR(f1,... ,fr). This characterization of semideﬁnite representations via sums of squares is not new: it follows from the factorization theorem of Gouveia, Parrilo and Thomas [GPT13] and its sum-of-squares interpretation see e.g., [Faw16]. We note that a similar characterization is also used in Scheiderer’s paper, see [Sch18, Theorem 3.4].

- • One of the main observations needed to prove Theorem 2 is to note that the functions


f1,... ,fr can be chosen to be semialgebraic. (We recall the precise deﬁnition of semialgebraic functions in Section 2.) One key property of such functions that turns out to be particularly important is that they are smooth almost everywhere. Combining this property with a simple observation regarding smooth sum of squares decompositions of homogeneous

polynomials allows us to prove Theorem 2 already in the special case where p is a homogeneous polynomial. This allows us to prove that Sep(n,m) is not semideﬁnite representable when (n,m) = (5,3) or (4,4). The complete proof of Theorem 2 which allows us to cover the cases (n,m) = (4,2) and (3,3) for separable states, requires an additional technical argument using Puiseux expansions for univariate continuous semialgebraic functions.

Real version of Theorem 2 We note that one can state an analogue of Theorem 2 dealing with real polynomials instead of Hermitian polynomials. The proof is similar, and we state it below just for convenience and for future reference.

- Theorem 3 (Main theorem for real polynomials). Let p(x) = u puxu ∈ R[x] where A ⊂ Nn ﬁnite, be a real polynomial that is nonnegative on Rn but not a sum of squares. Assume furthermore that A is downward closed, i.e., if u ∈ A then all u′ ∈ Nn with 0 ≤ u′ ≤ u are in A. Deﬁne the monomial map mA(x) = [xu]u∈A for x ∈ Rn. Then the convex set


cl conv {mA(x) : x ∈ Rn} is not semideﬁnite representable.

The theorem above can be used to recover the result of Scheiderer [Sch18, Corollary 4.25], that the cone Pn,2d of nonnegative (real) forms in n variables of degree 2d is not semideﬁnite representable when it is distinct from Σn,2d, the cone of sums of squares. Indeed, it suﬃces to take p in Theorem 3 to be a dehomogenization of a nonnegative form that is not a sum of squares, and to use the well-known fact that a convex set has a semideﬁnite representation if and only if its dual has one.

Organization The paper is organized as follows. In Section 2 we set some of the notations and present some background material on Hermitian polynomials, sums of squares, and semialgebraic sets and functions that are useful for the proof of the main theorem. In Section 3 we review the connection between the existence of semideﬁnite programming representations, and sums of squares. The proof of Theorem 2 is in Section 4 and the proof of Theorem 1 in Section 5.

# 2 Preliminaries

We recall in this section some results on Hermitian polynomials, the duality Sep/nonnegative polynomials and PPT/sums of squares and semialgebraic sets and functions.

## 2.1 Hermitian polynomials

For z ∈ Cn, we denote the elementwise complex conjugate of z by z¯ = (¯z1,... ,z¯n). If u ∈ Nn we deﬁne the monomial zu = z1u1 ... znun. A Hermitian polynomial p(z) is a polynomial in z and z¯ of the form

puvzuz¯v (A ⊂ Nn × Nn) (7)

p(z) =

(u,v)∈A

such that p(z) ∈ R for all z ∈ Cn. This is equivalent to saying that puv = pvu for all u,v. The support of p is supp(p) = {(u,v) : puv = 0} ⊂ Nn ×Nn. The Hermitian polynomial p is nonnegative if p(z) ≥ 0 for all z ∈ Cn. Further, we say that p is a sum of squares if we can write

![image 3](<2019-fawzi-set-separable-states-has_images/imageFile3.png>)

p =

k

qk2 (8)

for Hermitian polynomials qk. If p(z) is a Hermitian polynomial we will often consider the real polynomial P(a,b) = p(a+ib) in R[a1,... ,an,b1,... ,bn]. One can check that p is a sum-of-squares if and only if P is a sum-of-squares of real polynomials.

- Remark 2 (Sums of squares for Hermitian polynomials). Another common deﬁnition of a Hermitian


polynomial p(z) being a sum-of-squares is that p can be written as p(z) = k |gk(z)|2 where gk are (holomorphic) polynomials in z only (and not in z¯). Clearly if p has such a representation then it

is a sum-of-squares in the sense (8) since then p = k Re[gk]2 + Im[gk]2 and Re[gk] and Im[gk] are both Hermitian polynomials. The converse however is not true. It is possible that a polynomial

p has a representation (8) and cannot be written as a sum of modulus squares of holomorphic polynomial mappings. See e.g., [DP09] for more on this distinction. In this paper we only work with the deﬁnition (8) of sums of squares.

## 2.2 Sep, PPT, nonnegative polynomials, and sums of squares

For convenience, we will work in this paper with the cone of separable states, where we drop the normalization condition:

SEP(n,m) = conv xx† ⊗ yy† : x ∈ Cn,y ∈ Cm .

One can verify that Sep(n,m) is the compact slice Sep(n,m) = SEP(n,m) ∩ {ρ : Trρ = 1}.2 Let also PPT be the cone of states that have positive partial transpose, i.e.,

PPT (n,m) = {ρ ∈ Hnm : ρ ≥ 0 and (I ⊗ T)(ρ) ≥ 0} so that PPT(n,m) = PPT (n,m) ∩ {ρ : Trρ = 1}.

Dual of Sep For any integer k, let Mk = Ck×k. A C-linear map Φ : Mn → Mm that is Hermitian preserving is positive if Φ(ρ) ≥ 0 whenever ρ ≥ 0. Equivalently, Φ is positive if the degree-four Hermitian polynomial p(x,y) = y†Φ xx† y is nonnegative on Cn+m ≃ Cn × Cm. It is well-known that the dual of SEP(n,m) can be identiﬁed, via the Choi isomorphism, with the cone of positive maps Mn → Mm (see e.g., [AS17a, Table 2.2]). Equivalently, the dual of SEP(n,m) can be identiﬁed with nonnegative degree-four Hermitian polynomials of the form

p(x,y) =

pijklxix¯jyky¯l (x ∈ Cn,y ∈ Cm) (9)

1≤i,j≤n 1≤k,l≤m

where pijkl = Φ(Eij)lk. Polynomials of the form (9) have a biquadratic structure: they are quadratic independently in each block of variables x and y. The duality between SEP and nonnegative polynomials of the form (9) is in fact immediate from the deﬁnition of SEP.

Dual of PPT Using the identiﬁcation above, it turns out that the dual of PPT (n,m) corresponds to polynomials p(x,y) that are sums of squares. Indeed, it is well-known (see again [AS17a, Table 2.2]) that the dual cone of PPT (n,m) can be identiﬁed, via the Choi isomorphism, with the cone of maps Φ : Mn → Mm that are decomposable, i.e., that can be written Φ = S1 + S2 ◦ T where S1 and S2 are two completely positive maps, and T is the transpose map. Recall that a map S : Mn → Mm

![image 4](<2019-fawzi-set-separable-states-has_images/imageFile4.png>)

2Indeed if ρ = i pkxkx†k ⊗ ykyk† with Trρ = 1 and pk ≥ 0, then by redeﬁning pk ← pk|xk|2|yk|2 we can assume without loss of generality that |xk| = |yk| = 1. Taking the trace on both sides of ρ = i pkxkx†k ⊗ ykyk† tells us that 1 = k pk since Tr ρ = 1, i.e., ρ ∈ Sep(n, m).

is completely positive if there exist matrices Vt such that S(X) = t Vt∗XVt. One can verify that a map Φ is decomposable if and only if, the associated Hermitian polynomial (9) is a sum of squares.

We did not ﬁnd any reference for this equivalence, so we include a proof here. (The proofs we found in the literature are only for the direction ⇒ in Proposition 1. The proof of Proposition 1 is a special case of a more general result in [FF19], joint with Kun Fang, where it is shown that the dual of DPSk can be identiﬁed with a sum-of-squares condition of degree k.)

- Proposition 1. A map Φ : Mn → Mm is decomposable if, and only if, the Hermitian polynomial p(x,y) = y†Φ xx† y is a sum of squares.


Proof. If S(ρ) = t VtρVt† is a completely positive map then y†S(xx†)y = t y†Vtxx†Vt†y = t |y¯TVtx|2 is a sum-of-squares. Also for the transpose map T, we have y†(S ◦ T)(xx†)y =

y†S(¯xx¯†)y = t |yTV¯tx|2 is also a sum-of-squares. It follows that if Φ is decomposable then p(x,y) = y†Φ xx† y is a sum-of-squares.

We now prove the converse. Assume p(x,y) = y†Φ(xx†)y is a sum-of-squares, i.e., p(x,y) =

t qt(x,y)2 for some Hermitian polynomials qt. We need to show that Φ is decomposable. Since the coeﬃcient of the monomial x2ix¯i2 in p is 0, we see that qt cannot have monomials x2i,x¯i2 or xix¯i. To be sure, let αt,α¯t,βt be the coeﬃcients in qt of these monomials (note that βt ∈ R since xix¯i is real). The coeﬃcient of x2ix¯i2 in t qt2 is t 2|αt|2 + βt2 = 0 which implies that αt = βt = 0 for all t. Similarly, by looking at the coeﬃcient of xix¯ixjx¯j in p, we see that the qt cannot have monomials of the form xixj,x¯ix¯j,xix¯j or x¯ixj. The same of course is true for the y’s. Thus this means that qt must have the form

+x¯TM¯ty¯

+x¯TNty

+xTNty¯

qt(x,y) = xTMty

![image 5](<2019-fawzi-set-separable-states-has_images/imageFile5.png>)

![image 6](<2019-fawzi-set-separable-states-has_images/imageFile6.png>)

![image 7](<2019-fawzi-set-separable-states-has_images/imageFile7.png>)

![image 8](<2019-fawzi-set-separable-states-has_images/imageFile8.png>)

![image 9](<2019-fawzi-set-separable-states-has_images/imageFile9.png>)

![image 10](<2019-fawzi-set-separable-states-has_images/imageFile10.png>)

![image 11](<2019-fawzi-set-separable-states-has_images/imageFile11.png>)

![image 12](<2019-fawzi-set-separable-states-has_images/imageFile12.png>)

h ¯t where M ∈ Cn×n and N ∈ Cm×m. Squaring qt we get

g ¯t

gt

ht

qt2 = gt2 + 2|gt|2 + 2gtht + 2gth¯t + g¯t2 + 2¯gtht + 2¯gth¯t + h2t + 2|ht|2 + h¯t2.

When summing k qt2 we see that the only terms that can produce monomials of the form xix¯jyky¯l (the monomials that appear in p) are the terms 2|gt|2 and 2|ht|2. The sum of all the other terms must thus be equal to 0. At the end we get (including the constant 2 in Mt and Nt):

p =

k

|xTMty|2 + |xTNty¯|2.

From here it easily follows that Φ = S1 +S2 ◦T where S1(ρ) = t NtρNt† and S2(ρ) = t M¯tρM¯t†.

![image 13](<2019-fawzi-set-separable-states-has_images/imageFile13.png>)

![image 14](<2019-fawzi-set-separable-states-has_images/imageFile14.png>)

![image 15](<2019-fawzi-set-separable-states-has_images/imageFile15.png>)

![image 16](<2019-fawzi-set-separable-states-has_images/imageFile16.png>)

The following diagram summarizes the discussion above.

SEP ⊂ PPT (duality)   (duality)

Nonnegative Hermitian polynomials (9)

Sum-of-squares Hermitian polynomials (9)

⊃

## 2.3 Semialgebraic sets and functions

Semialgebraic sets A semialgebraic subset of Rn is a subset that can be deﬁned by a ﬁnite boolean combination of polynomial equations (P = 0) and inequalities (P > 0) where P ∈ R[x1,... ,xn]. For example a set of the form {w ∈ RD : M0 + w1M1 + ··· + wDMD ≥ 0} is semialgebraic since the condition that a matrix is positive semideﬁnite can be expressed by a ﬁnite number of polynomial inequalities. The set of separable states can be shown to be semialgebraic. One can prove this using the celebrated and powerful result of Tarski stating that the projection of a semialgebraic set is semialgebraic. A consequence of Tarski’s theorem is that the convex hull of a semialgebraic set S ⊂ Rn is semialgebraic. Indeed this is because we can write conv(S) as the projection on the x component of the following semialgebraic set

(x,λ,s1,... ,sn+1) ∈ Rn × Rn+1 × (Rn)n+1 :

λ1,... ,λn+1 ≥ 0,s1,... ,sn+1 ∈ S, x =

n+1

λisi and

i=1

n+1

λi = 1 .

i=1

(Note that, by Carathe´odory theorem any element in conv(S) is a convex combination of at most n + 1 points in S.) To see why the set Sep(n,m) is a semialgebraic subset of Hnm ≃ R2(nm)2 ﬁrst note that the following set

(ρ,x,y) ∈ Hnm × Cn × Cm s.t. ρ = xx† ⊗ yy† and |x|2 = |y|2 = 1 (10)

is a semalgebraic subset of Hnm × Cn × Cm ≃ R2(nm)2 × R2n × R2m since the equations can all be written as real polynomial equations in the real and imaginary components. By Tarski’s theorem it follows that the projection of (10) on the Hnm component, which is precisely the set of pure product states, is semialgebraic. Thus Sep is semialgebraic as the convex hull of a semialgebraic set.

Semialgebraic functions A function f : Rn → Rm is called semialgebraic if its graph {(x,f(x)) : x ∈ Rn} ⊆ Rn ×Rm is a semialgebraic set. Even though semialgebraic functions form a very broad class of functions, they are tame and possess nice regularity properties. Examples of semialgebraic functions are polynomials, rational functions, or power functions (with rational exponent). Functions that are not semialgebraic are e.g., exp(x), or the indicator function of the rationals in R. We state two basic results about semialgebraic functions that will be crucial for us.

- Theorem 4 (Almost everywhere smoothness of semialgebraic functions). Let f : Rn → R be a semialgebraic function. Then f is smooth (C∞) everywhere except possibly on the zero set of a polynomial P ∈ R[x1,... ,xn] \ {0}. Proof. See e.g., [HP16, Theorem 1.7].

![image 17](<2019-fawzi-set-separable-states-has_images/imageFile17.png>)

![image 18](<2019-fawzi-set-separable-states-has_images/imageFile18.png>)

![image 19](<2019-fawzi-set-separable-states-has_images/imageFile19.png>)

![image 20](<2019-fawzi-set-separable-states-has_images/imageFile20.png>)

Clearly Theorem 4 is not true for general functions, cf. the indicator function of the rationals in R. The second result that we will need concerns semialgebraic functions in one variable.

- Theorem 5 (Puiseux expansion for one-dimensional semialgebraic functions). Assume f : (0,η) → R where η > 0, is a semialgebraic continuous function that is bounded. Then f can be extended by continuity to the interval [0,η). Additionally, there exists an integer m such that the map t  → f(tm) is C∞ on [0,ǫ) for some 0 < ǫ < η.


Proof. For the ﬁrst part, see [BPR06, Proposition 3.18]. For the second part, see [Cos05, page 10].

![image 21](<2019-fawzi-set-separable-states-has_images/imageFile21.png>)

![image 22](<2019-fawzi-set-separable-states-has_images/imageFile22.png>)

![image 23](<2019-fawzi-set-separable-states-has_images/imageFile23.png>)

![image 24](<2019-fawzi-set-separable-states-has_images/imageFile24.png>)

We note that the theorem above is not true for arbitrary functions. For example the function x  → sin(1/x) is bounded and continuous on any interval (0,η) but cannot be extended by continuity at 0. We ﬁnally record the following result which will also be needed for our proof. It simply says that any linear map, restricted to a semialgebraic set always admits a semialgebraic inverse.

- Theorem 6. Let S ⊂ RN be a semialgebraic set and let π : RN → Rn be a linear map. Then there exists a semialgebraic function F : π(S) → S that satisﬁes π(F(x)) = x for all x ∈ π(S). Proof. See [HP16, Lemma 1.5].

![image 25](<2019-fawzi-set-separable-states-has_images/imageFile25.png>)

![image 26](<2019-fawzi-set-separable-states-has_images/imageFile26.png>)

![image 27](<2019-fawzi-set-separable-states-has_images/imageFile27.png>)

![image 28](<2019-fawzi-set-separable-states-has_images/imageFile28.png>)

- 3 Semideﬁnite programming lifts


We are now ready to start the proof of Theorem 2 (and thus of Theorem 1 too). The ﬁrst thing we need is a necessary condition for the existence of a semideﬁnite representation for a given convex set C. The condition we state in Theorem 7 below is very similar to [GPT13, Theorem 1]3. Recall that, for A ⊂ Nn × Nn we denote by mA(z) the monomial map:

mA(z) = [zuz¯v](u,v)∈A . We also denote by cl S the (topological) closure of a set S.

- Theorem 7. Let A ⊂ Nn × Nn. Assume that CA = cl conv {mA(z) : z ∈ Cn}


has a semideﬁnite representation of size k. Then there exists 2k2 + 1 semialgebraic functions fj : Cn → R (j = 1,... ,2k2 + 1) such that any nonnegative Hermitian polynomial p supported on A ∪ {(0,0)} is a sum-of-squares from V = spanR(f1,... ,f2k2+1), i.e., p = j h2j for some hj ∈ V . Furthermore, the magnitude of the coeﬃcients expressing the hj in terms of the basis (f1,... ,f2k2+1) are all bounded by φ( p ) where p is the largest magnitude of the coeﬃcients of p, and φ is some polynomial that only depends on the semideﬁnite representation of CA.

The main diﬀerence between the statement above and the one in [GPT13] (see also [Faw16, Theorem 5, Chapter 2]) is that here the functions f1,... ,f2k2+1 are semialgebraic. (We say that a function f : Cn → R is semialgebraic if the function F : Rn×Rn → R deﬁned by F(a,b) = f(a+ib) is semialgebraic.) This observation will be crucial to us. We note that a statement similar to the theorem above appears as Theorem 3.4 in [Sch18]. Instead of working with semialgebraic functions, Scheiderer works with polynomial functions on an algebraic variety X.

Proof. Assume that CA = π(S) where S is a spectrahedron deﬁned using a linear matrix inequality of size k × k:

S = w ∈ RN : M(w) := M0 + M1w1 + ··· + MNwN ≥ 0 .

We can assume without loss generality that S has nonempty interior in RN. This in turn implies, using standard results about spectrahedra, that there exists w ∈ S such that M( w) is positive deﬁnite (possibly after changing M), see e.g., [RG95, Section 2.4].

![image 29](<2019-fawzi-set-separable-states-has_images/imageFile29.png>)

3The given condition is also suﬃcient, but we will only need necessity here

For any z ∈ Cn there exists w(z) ∈ S such that π(w(z)) = mA(z). Since M(w(z)) ≥ 0 we can ﬁnd F(z) ∈ Ck×k such that M(w(z)) = F(z)F(z)†. Furthermore, by Theorem 6, the function z ∈ Cn  → F(z) ∈ Ck×k can be taken to be semialgebraic.

Let p(z) be a Hermitian polynomial supported on A ∪ {(0,0)}, i.e., p(z) = p,mA(z) + c for some c ∈ R, where p denotes the coeﬃcients of the polynomial p(z) in the monomial basis. Since p ≥ 0 we get p,mA(z) + c ≥ 0 for all z ∈ Cn. This implies that p,σ + c ≥ 0 for all σ ∈ CA. We can lift this linear inequality to an inequality on the spectrahedron S, i.e., we have p,π(w) +c ≥ 0 for all w ∈ S, in other words

π∗( p),w + c ≥ 0 ∀w ∈ RN s.t. M(w) ≥ 0. By Farkas’ lemma/duality for SDPs, this means that there exists B ≥ 0 and b ≥ 0 such that

π∗( p),w + c = B,M(w) + b ∀w ∈ RN. (11) Plugging w = w(z) we get

p,π(w(z)) + c = B,M(w(z)) + b = B,F(z)F(z)† + b.

Since π(w(z)) = mA(z) and p,mA(z) = p(z) we get ﬁnally that p(z)+c = B,F(z)F(z)† +b for all z ∈ Cn. Factorizing B = DD† we get

p(z)+c = Tr DD†F(z)F(z)† +b =

k

|D†F(z)|2ij+b =

ij=1

k

Re[(D†F(z))ij]2+Im[(D†F(z))ij]2+b.

ij=1

If we deﬁne the 2k2 +1 semialgebraic functions to be the constant function and the z  → Re[Fij(z)] and z  → Im[Fij(z)], we get the desired claim.

For the last statement of the theorem, we show that the coeﬃcients of B (and thus of D) are bounded by a polynomial in the coeﬃcients of p. To get this, we can simply plug the value w = w that makes M(w) positive deﬁnite in (11). If we denote by λ > 0 the smallest eigenvalue of M( w) we get π∗( p), w + c = B,M( w) + b ≥ λTr[B] + b ≥ λ B + b, thus max( B ,b) ≤ ( π∗( p), w + c)/min(λ,1) ≤ O(max{ p ,|c|}).

![image 30](<2019-fawzi-set-separable-states-has_images/imageFile30.png>)

![image 31](<2019-fawzi-set-separable-states-has_images/imageFile31.png>)

![image 32](<2019-fawzi-set-separable-states-has_images/imageFile32.png>)

![image 33](<2019-fawzi-set-separable-states-has_images/imageFile33.png>)

# 4 Proof of Theorem 2

We are now ready to prove our main theorem, Theorem 2. We ﬁrst recall a piece of notation that we will use throughout the proof: for any function f : Cn → R we associate the function of real variables F : Rn × Rn → R, denoted by a capital letter, deﬁned by F(a,b) = f(a + ib). We will also sometimes think of a vector z ∈ Cn as z ∈ R2n and write for instance F(z).

Assume that CA has an SDP representation. Then, from Theorem 7 there exist semialgebraic functions f1,... ,fr : Cn → R such that the following is true:

Any nonnegative Hermitian polynomial supported on A ∪ {(0,0)} is a sum-of-squares of functions from spanR(f1,... ,fr).

(∗)

We will now prove that the functions fi can be taken to be smooth at the origin. (By this we mean that the associated functions Fi : Rn × Rn → R are smooth at (0,0).) This will follow from our assumption that A is downward closed. Since the Fi are semialgebraic we know from Theorem 4 that each Fi is smooth almost everywhere. Thus we can ﬁnd a common point z0 = (a0,b0) ∈ Rn×Rn

such that all functions Fi are smooth at z0. Now let fi(z) = fi(z − z0) for all i ∈ {1,... ,r}. We claim that these semialgebraic functions still satisfy the property (∗). Indeed if q is a nonnegative Hermitian polynomial supported on A∪{(0,0)} then q(z+z0) is nonnegative and is also supported on A, since A is downward closed. It follows that q(z+z0) is a sum-of-squares from spanR(f1,... ,fr). But this implies that q(z) is a sum-of-squares from spanR( f1,... , fr).

In the rest of the proof we will thus assume that the F1,... ,Fr are smooth at the origin. If p is homogeneous we are almost done by the following simple observation: if P is a real homogeneous polynomial and P = j Hj2 for some functions Hj : Rm → R that are smooth at the origin, then P is a sum-of-squares of polynomials. This can be proved by a simple Taylor expansion; for example by applying the following proposition to the identity t2kP(z) = P(tz) = j Hj(tz)2 and observing that dtdkk Hj(tz)

is a degree k polynomial in z ∈ R2n (it is the k’th term in the Taylor expansion of Hj at z).

![image 34](<2019-fawzi-set-separable-states-has_images/imageFile34.png>)

t=0

- Proposition 2. Assume that gj : [0,η) → R are smooth functions4 and that there exists a ∈ R


2

(k) j (0)

such that at2k = j gj(t)2 for all t ∈ [0,η). Then a = j g

.

![image 35](<2019-fawzi-set-separable-states-has_images/imageFile35.png>)

k!

Proof. If we Taylor expand the gj at 0 we get at2k = j(gj(0)+tgj′ (0)+···+tkgj(k)(0)/k!+o(tk))2. By equating powers of t we get that gj(0) = ··· = gj(k−1)(0) = 0 and that a = j(gj(k)(0)/k!)2 as desired.

![image 36](<2019-fawzi-set-separable-states-has_images/imageFile36.png>)

![image 37](<2019-fawzi-set-separable-states-has_images/imageFile37.png>)

![image 38](<2019-fawzi-set-separable-states-has_images/imageFile38.png>)

![image 39](<2019-fawzi-set-separable-states-has_images/imageFile39.png>)

The case where p is not necessarily homogeneous requires an additional argument. The following argument is inspired from [Sch18, Proposition 4.18]. Let 2d = deg p, and for any t ∈ R consider the Hermitian polynomial pt(z) = t2dp(z/t). This Hermitian polynomial is nonnegative and is also supported on A. Thus we know from property (∗) that there exist real coeﬃcients aj(t) ∈ Rr s.t.

Pt(z) =

j

aj(t)TF(z)

2

∀z ∈ R2n (12)

where we let F(z) = (F1(z),... ,Fr(z)). The functions aj(t) are deﬁned by a semialgebraic relation and so can be taken to be semialgebraic. As such the aj must be continuous on some (0,η) for η > 0. From the last part of the statement of Theorem 7 we also know that the aj must be bounded on (0,η). Thus, by Theorem 5 we know that the aj can be extended by continuity to [0,η) and that for large enough m, aj(tm) is smooth on [0,η′) for some 0 < η′ < η. From (12) we get:

Ptm(tmz) =

j

(aj(tm)TF(tmz))2.

But note that Ptm(tmz) = t2dmP(z). Thus t2dmP(z) =

j

(aj(tm)TF(tmz))2.

If we let gj(t) = aj(tm)TF(tmz) we know that the gj are smooth on [0,η′), since the F are smooth at the origin. We can apply the observation of Proposition 2 to get that

P(z) =

![image 40](<2019-fawzi-set-separable-states-has_images/imageFile40.png>)

4Smoothness at 0 is smoothness on the right

j

gj(dm)(0) (dm)!

![image 41](<2019-fawzi-set-separable-states-has_images/imageFile41.png>)

2

.

But, from the deﬁnition of gj, gj(dm)(0) is a polynomial (of degree d) in z. This contradicts the assumption that p(z) is not a sum of squares of polynomials.

# 5 Proof of Theorem 1

The case Sep(3,3): We prove that SEP(3,3) has no semideﬁnite representation. Deﬁne the Choi polynomial [Cho75] by

p(x,y) = |x1|2|y1|2 + |x2|2|y2|2 + |x3|2|y3|2 − 2(Re[x1x¯2y1y¯2] + Re[x2x¯3y2y¯3] + Re[x1x¯3y1y¯3])

+ 2(|x1|2|y2|2 + |x2|2|y3|2 + |x3|2|y1|2).

It was shown in [Cho75] (see also [Cho80, Appendix B]) that p(x,y) ≥ 0 for all (x,y) ∈ C3×C3, and yet p(x,y) is not a sum of squares. In fact the real polynomial p(x,y) when (x,y) ∈ R3 × R3 is not a sum of squares. It follows, by a simple homogenization argument, that the Hermitian polynomial pˆ(x1,x2,y1,y2) = p(x1,x2,1,y1,y2,1) is not a sum of squares. Note that the support of pˆ satisﬁes

supppˆ ⊂ Aˆ = (α,β,γ,δ) ∈ (N2 × N2) × (N2 × N2) : |α| ≤ 1,|β| ≤ 1,|γ| ≤ 1,|δ| ≤ 1 . Since Aˆ is downward closed it follows from Theorem 2 that

CAˆ = cl conv mAˆ(x,y) : (x,y) ∈ C2 × C2

= cl conv xαyβx¯γy¯δ

: (x,y) ∈ C2 × C2

|α|≤1,|β|≤1,|γ|≤1,|δ|≤1

(13)

does not have a semideﬁnite representation. To conclude that SEP(3,3) has no semideﬁnite representation, it remains to note that CAˆ is a hyperplane section of SEP(3,3). Indeed, ﬁrst recall that SEP(3,3) can be written as

SEP(3,3) = clconv mA(x,y) : (x,y) ∈ C3 × C3 where

A = (α,β,γ,δ) ∈ (N3 × N3) × (N3 × N3) : |α| = 1,|β| = 1,|γ| = 1,|δ| = 1 . It is easy to see that there is a one-to-one correspondence between Aˆ and A. In terms of the monomial map m this simply means that mA is the homogenization of mAˆ. For example under an appropriate ordering of the monomials we have mA(x1,x2,x3,y1,y2,y3) = |x3|2|y3|2mAˆ x x

, yy

![image 42](<2019-fawzi-set-separable-states-has_images/imageFile42.png>)

![image 43](<2019-fawzi-set-separable-states-has_images/imageFile43.png>)

3

3

where we let x = (x1,x2) and y = (y1,y2). It thus follows that SEP(3,3) can be written as

SEP(3,3) = clconv |x3|2|y3|2mAˆ

x x3

y y3

,

![image 44](<2019-fawzi-set-separable-states-has_images/imageFile44.png>)

![image 45](<2019-fawzi-set-separable-states-has_images/imageFile45.png>)

: (x,y) ∈ C3 × C3 .

It can then be readily veriﬁed that CAˆ is a hyperplane section of SEP(3,3) where the appropriate coordinate (corresponding to the monomial |x3|2|y3|2) is set to 1.

The case Sep(4,2): Following the same approach as above, we need to exhibit a Hermitian polynomial pˆ(x1,x2,x3,y) supported on

Aˆ = (α,β,γ,δ) ∈ (N3 × N) × (N3 × N) : |α| ≤ 1,|β| ≤ 1,|γ| ≤ 1,|δ| ≤ 1 (14)

that is nonnegative but not a sum-of-squares. Since Sep(4,2) = PPT(4,2) we know that there exists a Hermitian homogeneous polynomial p(x,y) on (x,y) ∈ C4 × C2 of the form

p(x,y) =

pijklxix¯jyky¯l (x ∈ C4,y ∈ C2)

ijkl

that is nonnegative but not a sum of squares. Note that such a p satisﬁes p(λx,µy) = |λ|2|µ|2p(x,y) for any (λ,µ) ∈ C2. To get the desired polynomial pˆit would suﬃce to dehomogenize the polynomial p by setting one of the x variables to 1, and one of the y variables to 1. It turns out, however, that one cannot guarantee in general that this dehomogenized polynomial is not a sum of squares. (We give an explicit example in Appendix A.) The reason we could dehomogenize the Choi polynomial in the (3,3) case was that the Choi polynomial is not a sum of squares when the variables are real. One cannot expect this to be true for our polynomial in (4,2) variables as it is known that any biquadratic real polynomial in (n,2) variables is a sum of squares [Cal73]. Nevertheless we show in Appendix A that by choosing an appropriate polynomial p, and an appropriate dehomogenization we can get a polynomial pˆ(x,y) supported on Aˆ of Equation (14) that is not a sum-of-squares. This implies that CAˆ is not semideﬁnite representable. Using a similar argument as for the (3,3) case we get that SEP(4,2) is not semideﬁnite representable.

# A The case Sep(4, 2)

In this section we exhibit a nonnegative Hermitian polynomial pˆ(x1,x2,x3,y) supported on Aˆ, deﬁned in Equation (14), that is not a sum of squares.

Consider the following map Φ : M2 → M4 studied in [HK16]:

  

  .

3w + 4x − 2y − 2z 2z − 2x 0 0 2y − 2x 2x z 0

x y z w

Φ

=

0 y 2w −w − 2z 0 0 −w − 2y 2w + 4x

It is shown in [HK16] that the map Φ is positive but not decomposable. We associate to Φ the Hermitian polynomial

W(x,y) = x†Φ(yy†)x x ∈ C4,y ∈ C2.

Then we know from Proposition 1 that W is positive but not a sum of squares. The purpose of this section is to prove the following:

- Proposition 3. The (nonhomogeneous) Hermitian polynomial W(1,x2,x3,x4,1,y2) is not a sum of squares.


The proof of this proposition involves some computations, and we use the speciﬁc properties of W (its zeros) which have been studied in [HK16]. We note that there are other dehomogenizations of W that are sums of squares. For example, we show later that W(x1,x2,−6,x4,1,y2) is a sum of squares.

Proof of Proposition 3. To lighten the notation we let y2 = α. In [HK16], the zeros of the polynomial W were identiﬁed. Namely it was shown that

W(x1(α),x2(α),x3(α),x4(α),1,α) = 0 ∀α ∈ C (15)

where

x(α) := 2α(1 − α), α 4 − 2(α + α¯) + 3|α|2 , −4 − 2|α|2, −α¯(2 + α) ∈ C4.

Let p(x2,x3,x4,α) = W(1,x2,x3,x4,1,α). The explicit formula of p is p(x2,x3,x4,α) = 2|α|2|x3|2 + 2|α|2|x4|2 − x3x¯4|α|2 − x¯3x4|α|2

+ x¯2x3α + x2x¯3α¯ − 2x¯3x4α − 2x3x¯4α¯

+ 3|α|2 + 2|x2|2 + 4|x4|2 + 2x2α + 2x¯2α¯ − 2x2 − 2x¯2 − 2α − 2¯α + 4.

Assume that p = i gi2 where gi are Hermitian polynomials in x2,x3,x4,α. Since p has no terms |x3|2 we see that the gi cannot contain monomials x3 or x¯3. Similarly p does not have a term |α|2|x2|2 and so p cannot contain monomials αx2, αx¯ 2, αx¯2 or α¯x¯2. It follows that each gi must be a linear combination of the monomials

1, α, x2, x4, αx3, αx4, αx¯ 3, αx¯ 4 and their conjugates. In other words, each gi is of the form:

gi(x2,x3,x4,α) = ai + biα + cix2 + dix4 + eiαx3 + fiαx4 + giαx¯ 3 + hiαx¯ 4

+ b¯iα¯ + c¯ix¯2 + d¯ix¯4 + e¯iα¯x¯3 + f¯iα¯x¯4 + g¯iαx¯3 + h¯iαx¯4

(16)

where ai,bi,... ,hi ∈ C. We will now use the information about the zeros of W (and thus of p) to deduce relations about these coeﬃcients and reach a contradiction.

Since W is bihomogeneous in the ﬁrst set of variables, we have (dividing by |x1(α)|2) from (15) that

x2(α) x1(α)

x3(α) x1(α)

x4(α) x1(α)

p

,

,

, α = 0, ∀α ∈ C \ {0,1}.

![image 46](<2019-fawzi-set-separable-states-has_images/imageFile46.png>)

![image 47](<2019-fawzi-set-separable-states-has_images/imageFile47.png>)

![image 48](<2019-fawzi-set-separable-states-has_images/imageFile48.png>)

Since p = i gi2 we get that for all i,

gi

x2(α) x1(α)

,

![image 49](<2019-fawzi-set-separable-states-has_images/imageFile49.png>)

x3(α) x1(α)

,

![image 50](<2019-fawzi-set-separable-states-has_images/imageFile50.png>)

x4(α) x1(α)

, α = 0, ∀α ∈ C \ {0,1}. (17)

![image 51](<2019-fawzi-set-separable-states-has_images/imageFile51.png>)

We can clear denominators in (17) by multiplying the expression by |x1(α)|2. As a result we get that

x3(α) x1(α)

x4(α) x1(α)

x2(α) x1(α)

|x1(α)|2gi

,

,

, α = 0, ∀α ∈ C. (18)

![image 52](<2019-fawzi-set-separable-states-has_images/imageFile52.png>)

![image 53](<2019-fawzi-set-separable-states-has_images/imageFile53.png>)

![image 54](<2019-fawzi-set-separable-states-has_images/imageFile54.png>)

The left-hand side of (18) is a Hermitian polynomial in α that is identically zero. Hence all its coeﬃcients must be equal to 0. This allows us to derive conditions on the coeﬃcients of gi in (16). More precisely:

- • The coeﬃcient of α4 is 4h¯i. Setting 4h¯i to zero yields hi = 0.
- • The coeﬃcient of α4α¯ is 4¯gi + 2h¯i. Setting to zero we get gi = 0.
- • The coeﬃcient of α2 is −4d¯i − 8¯gi. Setting to zero we get di = 0.


This gives a contradiction: indeed the coeﬃcient of |x4|2 in p is 4 > 0 and yet i |di|2 = 0.

![image 55](<2019-fawzi-set-separable-states-has_images/imageFile55.png>)

![image 56](<2019-fawzi-set-separable-states-has_images/imageFile56.png>)

![image 57](<2019-fawzi-set-separable-states-has_images/imageFile57.png>)

![image 58](<2019-fawzi-set-separable-states-has_images/imageFile58.png>)

We conclude this appendix by proving, as promised, that there is another dehomogenization of W that is a sum of squares. Let:

q(x1,x2,x4,α) = W(x1,x2,−6,x4,1,α). Let









0 0 0 6 0 3 0 0 0 0 0 −1

36 0 −3 0 0 0 0 2 −1 0 −1 0

- 0 0 0 0 0 0 6 0 0 0 1 0
- 0 0 0 1 0 0 3 −1 0 0 0 0


−3 −1 1 0 1 0 0 0 0 2 0 0 0 −1 1 0 23 0 0 0 0 0 0 1

, B =

A =

.

 

 

 

 

![image 59](<2019-fawzi-set-separable-states-has_images/imageFile59.png>)

One can verify that A − B ≥ 0 and A + B ≥ 0, i.e., that B A BA ≥ 0. Let m(x1,x2,x4,α) = (α,x1,x2,x4,αx¯ 1,αx¯ 4). Then one can check that we have the following sum of squares decomposition of q:

† A B B A

m(x,α) m¯ (x,α)

m(x,α) m¯ (x,α)

q(x1,x2,x4,α) =

.

Acknowledgements I would like to thank Omar Fawzi for his encouragements and for helpful comments on the paper. I would also like to thank Claus Scheiderer for useful discussions and exchanges related to the material of this paper, and James Saunderson for comments that helped improved the exposition.

# References

- [AS17a] Guillaume Aubrun and Stanis aw Szarek. Alice and Bob Meet Banach: The Interface of Asymptotic Geometric Analysis and Quantum Information Theory, volume 223. American Mathematical Soc., 2017.
- [AS17b] Guillaume Aubrun and Stanis aw Szarek. Dvoretzky’s theorem and the complexity of entanglement detection. Discrete Analysis, 2017.


[BPR06] Saugata Basu, Richard Pollack, and Marie-Franc¸oise Roy. Algorithms in real algebraic geometry. Springer-Verlag, 2006.

[Cal73] AP Calder´on. A note on biquadratic forms. Linear Algebra and its Applications, 7(2):175– 177, 1973.

[Cho75] Man-Duen Choi. Positive semideﬁnite biquadratic forms. Linear Algebra and its Applications, 12(2):95–100, 1975.

[Cho80] Man-Duen Choi. Some assorted inequalities for positive linear maps on c*-algebras. Journal of Operator Theory, pages 271–285, 1980.

[Cos05] Michel Coste. Real algebraic sets, 2005. Lecture notes available at https://perso.univ-rennes1.fr/michel.coste/polyens/RASroot.pdf.

[DP09] John P. D’Angelo and Mihai Putinar. Polynomial optimization on odd-dimensional spheres. In Emerging applications of algebraic geometry, pages 1–15. Springer, 2009.

[DPS04] Andrew C. Doherty, Pablo A. Parrilo, and Federico M. Spedalieri. Complete family of separability criteria. Physical Review A, 69(2):022308, 2004.

[Faw16] Hamza Fawzi. Power and limitations of convex formulations via linear and semideﬁnite programming lifts. PhD thesis, Massachusetts Institute of Technology, 2016.

[FF19] Kun Fang and Hamza Fawzi. Sums of squares on the sphere and quantum separability. In preparation, 2019.

[GPT13] Joa˜o Gouveia, Pablo A. Parrilo, and Rekha R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of Operations Research, 38(2):248–264, 2013.

[HHH96] Micha  Horodecki, Pawe  Horodecki, and Ryszard Horodecki. Separability of mixed states: necessary and suﬃcient conditions. Physics Letters A, 223(1):1 – 8, 1996.

[HK16] Kil-Chan Ha and Seung-Hyeok Kye. Construction of exposed indecomposable positive linear maps between matrix algebras. Linear and Multilinear Algebra, 64(11):2188–2198, 2016.

[HN09] J. William Helton and Jiawang Nie. Suﬃcient and necessary conditions for semideﬁnite representability of convex hulls and sets. SIAM Journal on Optimization, 20(2):759–791, 2009.

[HP16] Huy-Vui H`a and Tieˆn-Son Pham. Genericity in Polynomial Optimization, volume 3. World Scientiﬁc, 2016.

[Nem06] Arkadi Nemirovski. Advances in convex optimization: conic programming. In Proceedings of the International Congress of Mathematicians (ICM 2006), 2006.

[NPS10] Tim Netzer, Daniel Plaumann, and Markus Schweighofer. Exposed faces of semideﬁnitely representable sets. SIAM Journal on Optimization, 20(4):1944–1955, 2010.

[Per96] Asher Peres. Separability criterion for density matrices. Physical Review Letters, 77(8):1413, 1996.

[RG95] Motakuri Ramana and AJ Goldman. Some geometric results in semideﬁnite programming. Journal of Global Optimization, 7(1):33–50, 1995.

[Sch18] Claus Scheiderer. Spectrahedral shadows. SIAM Journal on Applied Algebra and Geometry, 2(1):26–44, 2018.

[Sko16]  Lukasz Skowronek. There is no direct generalization of positive partial transpose criterion to the three-by-three case. Journal of Mathematical Physics, 57(11):112201, 2016.

[Wor76] Stanis aw Lech Woronowicz. Positive maps of low dimensional matrix algebras. Reports on Mathematical Physics, 10(2):165–183, 1976.

