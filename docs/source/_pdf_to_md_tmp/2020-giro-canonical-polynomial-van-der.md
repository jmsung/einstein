A CANONICAL POLYNOMIAL VAN DER WAERDEN’S THEOREM

ANTONIO´ GIRAO˜

arXiv:2004.07766v1[math.CO]16Apr2020

Abstract. We prove a canonical polynomial Van der Waerden’s Theorem. More precisely, we show the following. Let {p1(x), . . . , pk(x)} be a set of polynomials such that pi(x) ∈ Z[x] and pi(0) = 0, for every i ∈ {1, . . . , k}. Then, in any colouring of Z, there exist a, d ∈ Z such that {a + p1(d), . . . , a + pk(d)} forms either a monochromatic or a rainbow set.

1. Introduction

Arithmetic Ramsey theory is a branch of combinatorics where one is interested in studying the existence of monochromatic structures in any ﬁnite colouring of the integers. A well known theorem in the area due to Van der Waerden [8] and dating to 1927 states that in any ﬁnite colouring of the natural numbers there exist arbitrarily long monochromatic arithmetic progressions. This theorem has been considerably extended over the years and we emphasize some important extensions.

A classical result of Rado [7] characterizes all integer valued matrix M with the property that in any ﬁnite colouring of the naturals there exists a monochromatic solution to M ·  x = 0. Observe that a solution to the system of linear equations consisting of x1 − 2x2 + x3 = 0,

- x2 −2x3 +x4 = 0,... ,xk−2 −2xk−1 +xk = 0 forms a k-term arithmetic progression. Since such a system is easily seen to satisfy Rado’s characterization, Van der Waerden’s Theorem follows as a special case of Rado’s result. Another nice generalisation is the Gallai-Witt’s Theorem (see [4],[10]) which states that for any ﬁnite subset A ⊂ Zn, any ﬁnite colouring of Zn contains a monochromatic homothetic copy of A. This theorem can be viewed as a multidimensional generalisation of Van der Waerden’s Theorem.


Most ramsey-theoretical results (ﬁnite colourings) have a canonical version. In this setting, the palette of colours may be inﬁnite but one still would like to characterize all unavoidable sub-structures. For example, the canonical Van der Waerden’s Theorem, ﬁrst proved by Erd˝os and Graham [3], says the following.

- Theorem 1.1 (Canonical Van der Waerden). Whenever N is coloured, possibly with inﬁnitely many colours, there exist either arbitrarily long monochromatic arithmetic progressions or arbitrary long rainbow arithmetic progressions.


Note that both the Gallai-Witt and Rado’s classical theorems have canonical versions. Indeed, the canonical Gallai-Witt’s Theorem was originally proved by Deuber, Graham, Pr¨omel and Voigt [2] and it was later slightly simpliﬁed by Pr¨omel and Ro¨dl [6]. Rado’s canonical version was proved by Lefmann [5].

![image 1](<2020-giro-canonical-polynomial-van-der_images/imageFile1.png>)

School of Mathematics, University of Birmingham, Edgbaston, Birmingham, B15 2TT, United Kingdom. E-mail address: giraoa@bham.ac.uk. Date: 17th April 2020. The research leading to these results was partially supported by the EPSRC, grant no. EP/N019504/1.

1

A more recent and remarkable theorem in arithmetic Ramsey theory which once again extends Van der Waerden’s Theorem is the polynomial Van der Waerden’s Theorem, originally proved by Bergelson and Liebman [1]. Their proof uses heavy ergodic theory machinery, however, few years later, a beautiful and purely combinatorial proof was found by Walters [9].

- Theorem 1.2 (Polynomial Van der Waerden). Let p1,p2,... ,pk ∈ Z[x], where for every i ∈ [k],

- pi(0) = 0 and let n ∈ Z. Then, there exists N′ ∈ N such that for every colouring of {1,... ,N′} with n colours there exist a,d ∈ Z such that {a,a + p1(d),... ,a + pk(d)} ⊂ [N′] forms a monochromatic set.


The main purpose of this paper is to give a proof of the following canonical version of the polynomial Van der Waerden’s Theorem. We remark that our methods might be useful to show canonical versions of other theorems as well as giving new and shorter proofs of known canonical theorems.

- Theorem 1.3 (Canonical polynomial Van der Waerden). Let A = {p1,... ,pk}, where pi ∈ Z[x] and pi(0) = 0, for every i ∈ {1,... ,k}. Then, for any colouring of Z, there exist a,d ∈ Z such that {a,a+p1(d),... ,a+pk(d)} either forms a monochromatic set, or {a,a+p1(d),... ,a+pk(d)} forms a rainbow set.


We remark that our proof of Theorem 1.3 uses some nice ideas introduced by Walters in [9].

2. Preliminary definitions and notation

For technical reasons, we will always be considering multi-sets but we will still call them sets. As usual, we denote by [N] := {1,... ,N}. We deﬁne an integral polynomial to be a polynomial with integer coeﬃcients taking the value zero at zero. Given a natural number m, we say ∆ : [N] → Nm is an m-type colouring of [N], i.e. a colouring of [N] where each colour c is an element of Nm. For an element a ∈ [N] and j ∈ [m], we deﬁne ∆j(a) to be the j-th coordinate of ∆(a).

Now, let n,m ∈ N. We say ∆ : [N] → Nm × {1,... ,n} is an (m,n)-type colouring of [N]. For every set of distinct integers {a1,a2,... ,ak} ⊆ [N], we say it forms a fully-rainbow set if the following holds.

- (R1) for every i,i′ ∈ {1,... ,k} and j,j′ ∈ {1,... ,m}, ∆j(ai) = ∆j′(ai′),
- (R2) there exists c ∈ {1,... ,n}, such that for every i ∈ {1,... ,k}, ∆m+1(ai) = c. We say {a1,... ,ak} (not necessarily distinct) forms a rainbow set if it satisﬁes (R1). Finally,


we say a set of integers {a′1,... ,a′k} (not necessarily distinct) forms a monochromatic set if the following holds.

(M1) there exists a coordinate j ∈ [m] such that ∆j(ai) = ∆j(ai′), for every i,i′ ∈ {1,2,... ,k}.

Let ∆ be an (m,n)-type colouring of Z, and B = {p′1,... ,p′k′} a set of polynomials. We say that a set of distinct integers A(d) := {a1,... ,ak′} ⊂ Z is B-focused at a ∈ Z if aj − a = p′j(d), for all j ∈ {1,... ,k′} and a ∈/ {a1,... ,ak}. Moreover, we say that the sets A1(d1),... ,Aq(dq) are fully-rainbow B-focused at a, if the following are satisﬁed.

- (FR1) for all i ∈ {1,... ,q}, Ai(di) is B-focused at a,
- (FR2) Ai(di) is fully-rainbow,
- (FR3) (∪qi=1Ai(di)) forms a rainbow set all of whose elements are distinct.


Finally, let F := {A1(d1),... ,Aq(dr)} be a collection of fully-rainbow sets B-focused at a. For each c ∈ {1,... ,n}, let wc(F) := |{i | ∆m+1(Ai(di)) = c}|. In other words, wc(F) (or wc whenever F is understood from the context) counts the number of fully-rainbow sets Ai(di) ∈ F for which ∆m+1(Ai(di)) = c. For technical reasons, we need to deﬁne g(F) := {c ∈ {1,... ,n} | wc(F) ≤ m + 1}. Now, we let  F  := c∈g(F) wc. This is basically an ℓ1-norm with a tweak.

Given N′ ∈ N, we may deﬁne the equivalence classes induced by ∆ on intervals of order N. Suppose we partition [N′] = I1 ∪ ... ∪ Iℓ into consecutive intervals of order N. Then, we say Ii ∼∆ Ij if the following hold. We may assume Ii = I1 = [N] and Ij = [tN], for some t ∈ N.

- (1) for all i ∈ {1,... N}, ∆m+1(i) = ∆m+1(tN + i),
- (2) for all i,j ∈ {1,... ,N} and k ∈ {1,... ,m}, ∆k(i) = ∆k(j) if and only if ∆k(tN + i) = ∆k(tN + j).


It is easy to see this is indeed an equivalence relation. We denote the set of equivalence classes by E∆,N

′

′

N . Crucially, note that for any m,n,N ∈ N, and any (m,n)-type colouring ∆, E∆,N

N

is a ﬁnite set and we denote by f(m,n,N), the total number of possible distinct equivalence classes. Also, for an interval I, we let E∆N(I) to be the equivalence class containing I. When N′ is clear from the context, we omit the superscript N′ in the above deﬁnitions.

Following [9], let A = {p1,... ,pk} be a set of integral polynomials. Let D be the maximum degree of these polynomials. For 1 ≤ i ≤ D, let Ni(A) be the number of distinct leading coeﬃcients of the polynomials in A of degree i. We deﬁne the weight vector ω(A) := (N1,... ,ND). For any two sets of integral polynomial A,A′ we say that ω(A) < ω(A′) if there exists r such that Nr(A) < Nr(A′) and Ni(A) = Ni(A′), for every i > r. This is easily seen to be a well ordering on the set consisting of all ﬁnite sets of integral polynomials. In our proof of Theorem 1.3, the ‘outer’ induction will be on the weight vector of B.

First, we shall sketch a short proof of the Canonical Van der Waerden’s Theorem which makes use of some deﬁnitions introduced before.

3. Proof of the canonical Van Der Waerden’s Theorem

In this section, we give a sketch of a short proof of the Canonical Van der Waerden’s Theorem. We hope this will help the reader getting used to some of the terminology and ideas when reading the proof of our main theorem. Our aim in this section is to prove the following result.

- Theorem 3.1. Let k,t,m ∈ N. Then, there exists N0 := N(k,t,m) ∈ N such that for every m-type colouring ∆ : [N(k,t,m)] → Nm one of the two must hold.


- • There exists a monochromatic arithmetic progression A ⊆ [N0] of length k or
- • there exists a rainbow arithmetic progression B ⊆ [N0] of length t.


Note that trivially this implies the canonical Van der Waerden’s Theorem taking m = 1 and k arbitrarily large. Proof. The proof goes by induction on t. Clearly, N(k,1,m) exists for every k,m ∈ N.

Suppose we want prove the the existence of N(k,t+1,m). We shall assume by the induction

step that N(k,t,m′) exists for every k,m′ ∈ N. Let N ∈ N be a suﬃciently large positive integer and let ∆ be a m-type colouring of [2N]. First, we partition [N] into consecutive intervals I1,I2,... ,IN′′ each of length N′, for some N′′ := N/N′ ∈ N. The colouring ∆ induces a (mN′)-type colouring ∆′ of [N′′], where the colour of an interval Ij is the vector formed by the concatenation of the colours of the elements of Ij

in increasing order. Formally, for every j ∈ {1,... ,N′′}, ∆′(Ij) = (∆((j − 1)N′ + 1),∆((j − 1)N′ + 2),... ,∆(jN′)).

We may assume N′′ ≥ N(k,t,mN′). By induction, suppose there exist a coordinate i ∈

{1,... ,mN′} and an arithmetic progression A = {a1,a2,... ,ak} of length k such that ∆′i(aj) = c, for every j ∈ {1,... ,k}. Let i = mi′ + f, for some i′ ∈ {0,... ,N′ − 1} and f ∈ {1,... ,m}.

Then, it follows by construction of ∆′, that A′ = {a1N′+mi′,a2N′+mi′,... ,akN′+mi′} ⊆ [N] is an arithmetic progression and ∆f(x) = c, for every x ∈ A′. Hence, A′ forms a monochromatic progression, as we wanted to show. We may then assume [N′′] contains a rainbow arithmetic progression of length t. Let A∗ = {a′1,a′2,... ,a′t} ⊆ [N′′] be such a rainbow arithmetic progression and let d > 0 be the progression diﬀerence.

Now, let at+1 := at + d ∈ [2N′′] and Iat+1 the corresponding interval. Also, let x ∈ [2N] be the largest element of Iat+1 and ∆(x) = (c1,... ,cm). Observe that for any q ∈ {0,... ,N′ − 1}, the sets Tq := {x,x − (dN′ + q),x − 2(dN′ + q),... ,x − t(dN′ + q)} ⊆ [2N] form an arithmetic progression of length t+1. Moreover, since x−j(dN′ +q) ∈ Iat+1−j and A∗ is rainbow, we have that every Tq \ {x} forms a rainbow set.

Let us look at Iat. We will construct now a ﬁnite colouring st : Iat → {0} ∪ [m] × [m].

For ℓ ∈ Iat, st(ℓ) := (i,j) ∈ [m] × [m], if there exists i,j ∈ {1,... ,m} such that ∆i(ℓ) = cj (if there are many such pairs, choose one arbitrarily). If no such i,j exist, then we set set s(ℓ) = 0. This is a ﬁnite colouring so by Van der Waerden’s Theorem either there exists a k-term arithmetic progression At ⊂ Iat of colour (i,cj) ∈ [m] × [m], in which case we are done, because A′′ forms a monochromatic arithmetic progression(see (M1)) or there exists a suﬃciently large arithmetic progression Pt ⊂ Iat of colour 0. Observe that by construction {y,x} forms a rainbow set (see (R1)), for every y ∈ Pt. Let Pt := {x − at,x − at − dt),... ,x − at − ptdt)}, for some at,dt ∈ [N′] and a suﬃciently large pt ∈ N. Let It−1 := {x − 2(dN′ + at),x − 2(dN′ + at + dt),... ,x − 2(dN′ + a + dtpt)} be arithmetic progression of length pt inside Iat−1. We will apply the same reasoning to It−1 as we did with It. We deﬁne a ﬁnite colouring st−2st : It−1 → {0} ∪ [m] × [m], as before. By Van der Waerden’s Theorem, either there exists a k-term arithmetic progression At−1 ⊂ It−1 of colour (i,cj) ∈ [m] × [m], in which case we are done, or there exists a suﬃciently large arithmetic progression Pt−1 ⊂ It−1 of colour 0. Let Pt−1 := {x − at−1,x − at−1 − dt−1,... ,x − at−1 − pt−1dt−1}, for some at,−1,dt−1 ∈ [N′] and suﬃciently large pt−1 ∈ N. We may continue in the same fashion for t all the way down to 1. Indeed, suppose we have constructed Pt ⊆ Iat,Pt−1 ⊂ It−1 ⊂ Iat−1 ... ,Pt−i ⊂ It−i ⊆ Iat−i and we wish to construct Pt−i−1 ⊆ It−i−i ⊆ Iat−i−1. Suppose Pt−i := {x−at−i,... ,x−at−i−dt−ipt−i}, for some at−i,dt−i ∈ [N′] and suﬃciently large pt−i ∈ N. Then, let It−i−1 := {x−2at−i−dN′,x− 2(at−i +dt−i)−dN′,... ,x−2(at−i +dt−ipt−i)−dN′} ⊆ Iat−i−1. As before, we construct a ﬁnite colouring st−i−1 : It−i−1 → {0} ∪ [m] × [m]. Then, we can either ﬁnd a k-term arithmetic progression At−i−1 ⊂ It−i−1 of colour (i,cj) ∈ [m] × [m], in which case we are done, or we can ﬁnd a suﬃciently large arithmetic progression Pt−i−1 ⊂ It−i−1 of colour 0. Note now, that as long as P1 = ∅ (which is guaranteed by starting with a suﬃciently large pt) we may ﬁnd a t-term rainbow arithmetic progression. Indeed, let x − a1 ∈ P1 be the largest element in P1. Note that by construction x − a1/2i−1 + (i − 1)dN′ ∈ Ii, for every i ∈ {1,... ,t}. Therefore, the set {x} ∪ {x − a1/2i−1 + (i − 1)dN′ | i ∈ {1,... ,t}} forms a rainbow arithmetic progression of length t + 1, as we wanted to show.

4. Proof of Theorem 1.3 First, we need to show a simple lemma concerning integer valued polynomials.

Lemma 4.1. Let A = {p1,... ,pk} be a collection of distinct integral polynomials. Then, there exists h ∈ N such that for every i,j ∈ {1,... ,k} (possibly i = j), and for every h′ > h,

- pj(x) = pi(h′ + x) − pi(h′) as elements of Z[x]. Proof. If not, there exist i,j ∈ {1,... ,k}, and h1 ∈ N such that pi(x) = pj(h1 +x)−pi(h1). Let


- pi(x) = anxn + ... + a1x and pj(x) = bn′xn′ + ... + b1x. By substituting, pi(x) = pj(h1 + x) −
- pj(h1) = bn′(h1 + x)n′ + bn′−1(x + h1)n′−1 + ... + b1(x + h1) − pj(h1), hence n = n′, an = bn and n · h1 + bn−1 = an−1. Therefore, h1 = (an−1 − bn−1)/n, which contradicts the fact h1 could have been chosen suﬃciently large.


Given a collection A = {p1,... ,pk} of distinct integral polynomials, we deﬁne h(A) to be the smallest positive integer for which pi(x) = pj(x + h′) − pj(h′), for every h′ > h(A) and every

- i = j ∈ {1,... ,q}. This is well deﬁned by Lemma 4.1. In order to prove Theorem 1.3, it will be useful to prove the following slightly stronger


statement, from which Theorem 1.3 can be easily deduced.

- Theorem 4.2. Let h,k,k′,m,n ∈ N, A = {p1,... ,pk},B = {p′1,... ,p′k′} be two sets of integral


polynomials. Moreover, suppose that for every i,j ∈ {1,... ,k′}, p′i = p′j. Then, there exists N ∈ N such that for every (m,n)-type colouring of [N], one of the following holds.

- • there exist a,d ∈ Z such that {a,a+p1(d),... ,a+pk(d)} ⊆ [N] forms a monochromatic set,
- • there exist a′,d′ ∈ Z such that d′ > h and {a′,a′ + p′1(d′),... ,a′ + p′k(d′)} ⊆ [N] forms a fully-rainbow set.


Proof of Theorem 1.3. The induction will be on the weight of B. We may and will assume

- h > h(B).


Outer induction hypothesis. For every h,m,n,k,k′ ∈ N, any two sets of integral poly-

nomials A = {p1,... ,pk} and B = {p′1,... ,p′k′} where p′i = p′j (for all i,j ∈ {1,... ,k′}), there exists [N], such that for any (m,n)-type colouring of [N], there exist a,d ∈ Z such that

{a,a + p1(d),... ,a + pk(d)} ⊆ [N] forms a monochromatic set, or there exists a,d′ > h such that {a,a + p′1(d),... ,a + p′k(d)} ⊆ [N] forms a fully-rainbow set.

Suppose that the outer induction hypothesis is true for all h,m,n,k ∈ N, for every set of integral polynomials A of order k and for every set B′ of distinct integral polynomials satisfying ω(B′) < ω(B).

To check the base case, let h,m,n ∈ N and B′ = {a1x}, for some a1 ∈ Z \ {0}. Let N′ ∈ N be given by Theorem 1.2 when applied to the collection of integral polynomials p∗1 := p1(a1hx)/(a1h),... ,p∗k(x) := pk(a1hx)/(a1h) and n′ := ((m + 1)2 · n)n playing the role of n.

Let ∆ be an (m,n)-type colouring of [a1hnN′], our aim is to prove we can ﬁnd either a rainbow set {a,a + a1(hd)} ⊂ [a1hnN′] or a monochromatic set {a,a + p1(d),... ,a + pk(d)} ⊂ [a1hnN′], for some d ∈ N. First, let {a1hx1,... ,a1hxt} ⊆ [a1hnN′] be a largest set such that ∆m+1(a1hxi) = ∆m+1(a1hxi′), for every i,i′ ∈ {1,... ,t}. Note that t ≤ n and therefore there must exist an interval I ⊆ [a1hnN′], where |I| ≥ a1hN′ and xi ∈/ I, for every i ∈ {1,... ,t}.

Clearly, we may assume I = [a1hN′] since intervals are translation invariant with respect to satisfying our main theorem.

Now, consider the following n′-colouring of [N′], ∆∗ : [N′] → {1,... ,n′}, where ∆∗(x) = c, for some c ∈ {(i,j,b) | i,j ∈ {1,... ,m},b ∈ {1,... ,n}}t. For g ∈ {1,... ,t}, ∆∗g(x) = (i1,j2,b3), where i1,j2 ∈ {1,... ,m} are any two indices for which ∆i1(a1hx) = ∆j2(a1hxg), if no such two indices indices exist then i1 = j2 = m + 1. Finally, we let b3 = ∆m+1(a1hxg), i.e. the third coordinate of ∆∗g(x) equals the last coordinate of ∆(a1hxg). Clearly, ∆∗ is an n′-colouring of [N′] and hence by construction there exists a monochromatic set {a,a +

p∗1(d),... ,a + p∗k(d))} ⊆ [N′] of colour c = tr=1(ir,jr,br), where ir,jr ∈ {1,... ,m + 1} and br ∈ {1,... ,n}. Suppose there exists r ∈ {1,... ,t} for which ir,jr ∈ {1,... ,m}, then M := {a1ha,a1ha + p1(a1hd),... ,a1ha + pk(a1hd)} ⊂ [a1hN′] forms a monochromatic set with respect to ∆. Indeed, observe that ∆ir(y) = ∆jr(a1hxr), for all y ∈ M. Suppose, on the other hand, ir = jr = m + 1, for all r ∈ {1,... ,t}, and ∆m+1(a1ha) = ∆m+1(a1hxq), for some q ∈ {1,... t}. Hence, {a1ha,a1ha + a1(h(xq − a)) = a1hxq} ⊆ [a1hnN′] forms a rainbow set, as we wanted to show.

Inner induction hypothesis. For all r ≤ (m + 1)n there exist N ∈ N such that if ∆ is an (m,n)-type colouring of [N], then at least one of the following holds.

- (i) there exist a collection F = {A1(d1),... ,Aq(dq) ⊆ [N]} of fully-rainbow sets B-focused at a, for some a ∈ Z, such that di > h, for all i ∈ {1,... ,q}. Furthermore,  F  = r.
- (ii) there exists a′,d′ ∈ Z such that d > h and the set {a′,a′+p′1(d′),a+p′2(d′),... ,a+p′k′(d′)} is fully-rainbow,
- (iii) there exist a,d ∈ Z such that the set {a,a+p1(d),a+p2(d),... ,a+pk(d)} is monochromatic.


From this hypothesis, we prove our result by setting r = q(m + 1). To see this, note that if either (ii), or (iii) hold, we are done. On the other hand, suppose (i) holds and let F be such a collection with  F  = (m + 1)n. Let ∆m+1(a) = c, for some c ∈ {1,... ,n}. Observe that by assumption on the norm of F, there are m+ 1 sets Ai1(di1),... ,Aim+1(dm+1) ∈ F such that ∆m+1(Aij(dij) = c, for all j ∈ {1,... ,m}. Now, we show at least one of the Aij(dij)’s has the property that Aij(dij) ∪ {a} forms a rainbow set and hence a fully-rainbow set, as required. Suppose not, then for all w ∈ {1,... ,m + 1}, there are i(w),i′(w) ∈ {1,... ,m} and x(w) ∈ Aiw(diw) such that ∆i(w)(a) = ∆i′(w)(x(w)), hence there must exist w,w′ ∈ {1,... ,m+1} where i(w) = i(w′), which contradicts the fact Aiw(diw) ∪ Aiw′(diw′) forms a rainbow set. Therefore, if (i) holds for r = n(m + 1), then there exist a,d ∈ Z, where d > h such that the set {a,a + p′1(d),a + p′2(d),... ,a + p′k(d)} ⊆ [N] is fully-rainbow, as we wanted to show.

Now, we turn to the proof the inner induction hypothesis. The induction will be on r. Suppose the ﬁrst inner induction hypothesis is true for r − 1 taking N ∈ N. We will show that there is N′ ∈ N satisfying the hypothesis for r (an upper bound for N′ could be computed but for simplicity of the argument we will avoid doing this). Throughout the proof, we will assume that neither (ii) or (iii) hold. As in [9], let dmax be the largest d > h for which there exist a,a1,... ,ak ⊂ [N] satisfying ai − a = p′i(d), for all i ∈ {1,... ,k′}. Note dmax exists since all polynomials in B tend to inﬁnity. We may assume that p′1 has minimal degree amongst the

polynomials in B. We now deﬁne the set B∗ consisting of the following polynomials

p′di,j(x) := p′j(x + di) − p′1(x) − p′j(di) h < di ≤ dmax, 1 ≤ i ≤ k′, and p′0,j(x) := p′j(x) − p′1(x) 1 ≤ j ≤ k′.

By taking a subset B∗, we may assume all polynomials are distinct. Clearly, these polynomials are integral. More importantly, ω(B∗) < ω(B). To see this, suppose that p′j has larger degree than p′1. Then, all polynomials p′d

i,j, for h < di ≤ dmax or di = 0 have the same leading coeﬃcient and the same degree as p′j. If p′j has the same degree but a diﬀerent leading coeﬃcient from that of p′1, then all polynomials p′d

i,j, for h < di ≤ dmax or di = 0 have the same leading coeﬃcient equal to the leading coeﬃcient of p′j−p′1. Finally, if p′j has the same degree and leading coeﬃcient as p′1, then all the polynomials p′d

i,j, for h < di ≤ dmax or di = 0, have smaller degree than p′1. This implies that ωr(B∗) = ωr(B), for all r > deg(p′1) and ωr(B∗) = ωr(B) − 1, for r = deg(p′1). (The coordinates of ω(B∗) may increase for r < deg(p′1)). Thus, ω(B∗) < ω(B), as we wanted to show. By assumption on h, p′0,j(x) = p′d

i,j′(x) for every h < di ≤ d and every j,j′ ∈ {1,... ,k′}.

We will have to modify the polynomials in A and B∗ slightly. We need to do this since later in the proof we are going to divide [N′] into blocks of length N and we need to take this into account.

i,j ∈ B∗. Let A′ and B′ be the set consisting of the polynomials qj and qd′

Let qj(x) := pj(Nx)/N and qd′

i,j(x) := p′d

i,j(Nx)/N, for every pj ∈ A and p′d

i,j, respectively. It is easy to see that all polynomials in A′,B′ are integral polynomials and B′ still forms a collection of distinct integral polynomials. Also, observe that ω(B′) = ω(B∗) since, although the leading coeﬃcients may change, the number of distinct leading coeﬃcients of polynomials of a given degree does not. Thus the outer induction hypothesis applies to A′, B′.

(P1) By deﬁnition of h(B), and the fact h > h(B) we have the following. For every h < di ≤ dmax and every j,j′ ∈ {1,... ,k′}, q0′,j(x) = qd′

i,j′(x) (as elements of Z[x]).

Now, we divide [N′] into intervals of size N and we let Cs := {N(s − 1) + 1,... ,Ns}, for every s ∈ {1,... ,N′′ := N′/N}. As seen in Section 2, ∆ induces an equivalence relation ∼∆ on {C1,... ,CN′′}. Since there are at most f(N,n,m) distinct equivalence relations, we may apply the outer induction hypothesis to the sets A′, B′, h, N · m, and f(N,n,m) playing the roles of A, B, h, m, and n. For every s ∈ [N′′], let ∆′(s) = (∆1(N(s − 1) + 1),... ,∆m(N(s − 1) + 1),... ,∆1(Ns),... ,∆m(Ns),E∆(Cs)). By deﬁnition, ∆′ is an (N · m,f(N,n,m))-type colouring of [N′′]. Therefore, provided N′′ is suﬃciently large, one of the following holds.

- Case 1. There is s′,d′ ∈ Z and a collection of intervals C′ := {Cs′′,Cs′′


| 1 ≤ j ≤ k}, where

j

s′j − s′ = qj(d′) and B := {s′,s′j | 1 ≤ j ≤ k} ⊆ [N′′] forms a monochromatic set with respect to ∆′.

Case 2. There exist s,d ∈ Z, d > h and a collection of intervals C := {Cs,Csd

i,j | h < di ≤ dmax, or di = 0, and 1 ≤ j ≤ k′}, where sdi,j − s = qd′

i,j(d) and A := {s,sdi,j | h ≤ di ≤ dmax, or di = 0 and 1 ≤ j ≤ k′} ⊆ [N′′] is fully-rainbow with respect to ∆′.

First, let us suppose Case 1. holds. From the deﬁnition of a monochromatic set, we know

there exists an index i(B) ∈ {1,... ,N·m}, such that ∆′i(B)(s′j) = ∆′i(B)(s′), for all j ∈ {1,... ,k}. Let i(B) = (i′(B) − 1) · m + ℓ, for some 1 ≤ i′(B) ≤ N and 1 ≤ ℓ ≤ m.

- Claim 1. The set A′ := {(s′ −1)·N +i′(B),(s′1 −1)·N +i′(B),... ,(s′k −1)·N +i′(B)} ⊆ [N′] forms a monochromatic set with respect to ∆.

Proof. Observe that for every j ∈ {1,... ,k}, ((s′j−1)N+i′(B))−((s′−1)N+i′(B)) = N·qj(d′) = pj(Nd′), as required. Moreover, we have (s′j − 1)N + i′(B) ∈ Cs′

j

, for every j ∈ {1,... ,k}. By

construction of ∆′, we have that ∆ℓ((s′ − 1)N + i′(B)) = ∆ℓ((s′j − 1)N + i′(B)), for every j ∈ {1,... ,k} and therefore A′ forms a monochromatic set. ◭

This is a contradiction, as we assumed no such monochromatic set exists in [N′]. Hence, Case 2. must hold. Now, observe that by the choice of N and the assumption that there do not exist a,d ∈ Z with {a,a+p1(d),... ,a+pk(d)} forming a monochromatic set or a′ and d′′ > h with {a′,a′ + p′1(d′′),... ,a′ + p′k′(d′′)} forming a fully-rainbow set, it follows that Cs contains a collection F = {A′1(d1),... ,A′q′−1(dq′−1) ⊆ Cs} of fully-rainbow B-focused sets at a ∈ Cs such that h < d1,... ,dq′−1 ≤ dmax, where  F  = r − 1. Suppose that for every i ∈ {1,... ,q′}, A′i(di) = {ai,j | 1 ≤ j ≤ k′} and ai,j − a = p′j(di). We prove now the following claim.

- Claim 2. Let d0 := 0, A0(0) := {a} and a0,j := a, for all j ∈ {1,... ,k′}. Then, for every


i,j(d) | 1 ≤ j ≤ k′} ⊂ [N′] form a collection F′ of fully-rainbow sets, B-focused at a − p1(Nd) and  F′ = r.

- i ∈ {0,1,... ,q − 1}, the sets A′i(N(d + di)) := {ai,j + N · qd′


Proof. First, we need to show that for every i ∈ {0,1,... ,q − 1}, A′i(N(d + di)) is B-focused at a − p1(N · d′). To see this observe that for every j ∈ {1,... ,k′},

ai,j + N · qd′i,j(d) − (a − p′1(Nd)) = (ai,j − a) + N · qd′i,j(d) + p′1(Nd)

= p′j(di) + (p′j(N(di + d)) − pj(di) − p′1(Nd)) + p′1(Nd)

= p′j(N(di + d)),

and (FR1) is satisﬁed. We also need to show that every A′i(N(d + di)) forms a fully-rainbow set. Note that ai,j + N · qd′

i,j and i′,j′, {x,y} is rainbow with respect to ∆.

i′,j′, then for any x ∈ Csd

i,j(d) ∈ Csd

i,j and if Csd

i,j = Csd

- y ∈ Csd


i,j′(x) if j = j′, hence by the deﬁnition of A′, we must have that Csd

Now, it is easy to see that for every i ∈ {0,... ,q}, qd′

i,j(x) = qd′

i,j′. Therefore, by the construction of ∆′, for every i ∈ {0,... ,q −1}, A′i(N(d+di)) forms a rainbow set. Finally, since E∆(Cs) = E∆(Csd

i,j = Csd

i,j), for all j ∈ {1,... ,k′}, it implies in particular, that ∆m+1(ai,j) = ∆m+1(ai,j+N ·qd′

i,j(d)). Hence, for every i ∈ {0,... ,q−1}, A′i(N(d+di)) forms a fully-rainbow set and (FR2) holds. It remains to show (FR3). Clearly, A′i(N(d + di)) ∩ A′i′(N(d + di′)) = ∅, for every i,i′ ∈ {0,... ,q − 1}. Indeed, this holds because every element of A′i(N(d + di)) is a translation of an element of A′i(di) by a multiple of N, since by assumption, A′i(di) ∩ A′i′(di′) = ∅ and A′i(di) ⊂ Cs, for all i = i′ ∈ {1,... ,q − 1}, all elements in ∪iq=0−1A′i(N(d + di)) are distinct. To conclude the proof of (FR3), we just need to show that ∪iq=0−1A′i(N(d + di)) forms a rainbow set. Recall that by (P1), q0′,j(x) = qd′

i,j′ which implies that Cs0,j = Cdi,j′, for all h < di ≤ dmax and j′,j ∈ {1,... ,k′}. Hence, by the above, A′0(0)∪A′i(di) forms a rainbow set for all i ∈ {1,... ,k′}. Finally, note that since A′ is fully-rainbow with respect to ∆′, we have that E∆(Cs) = E∆(Csd

i,j), for every h < di ≤ dmax and j ∈ {1,... k′}. Suppose for contradiction that {ai,j +Nqd′′

i,j(d),ai′,j′+Nqd′

i′,j′(d)} is not rainbow with respect to ∆. Then, i = i′ (since we already have proved A′i(N(d + di)) is rainbow), also i = 0 and i′ = 0 (since we have proved A′0(0) ∪ A′i(di) is rainbow). First, if

Csd

i,j = Csd

i′,j, we are done by the above observation. So we must have that Csd

i,j = Csd

i′,j or equivalently qd′′

i,j(d) = qd′

i′,j′(d). In this case, we use the fact that E∆(Cs) = E∆(Csd

i,j) = E∆(Csd

i′,j′), which implies that {ai,j,ai′,j′} is rainbow if and only if {ai,j + Nqd′′

i,j(d),ai′,j′ + Nqd′′

i′,j′(d)} is rainbow. Since the former is rainbow with respect to ∆, we obtain the desired contradiction. Let us show now that  F′ = r. First, we may assume that wi(F) = m+1, for all i ∈ {1,... ,n1} and wi(F) < m+1, for n1 < i ≤ n. From the deﬁnition of  F , we have that nj=n

wj(F) = r−1. Let ∆m+1(a) = c and suppose that c ∈ {1,... ,n1}. Let

1

Fc := {A′ℓ1(dℓ1),... ,A′ℓm+1(dℓm+1) | A′ℓi(dℓi) ∈ F and ∆m+1(A′ℓi(dℓi)) = c}. Then, there must j ∈ {1,... ,m+1} such that A′ℓ

(dℓj)∪{a} forms a rainbow set and hence a fullyrainbow set, contradicting the fact (ii) does not hold. Indeed, if for all j ∈ {1,... ,m+1}, there are i(j),i′(j) ∈ {1,... ,m} and x ∈ A′ℓ

j

(dℓj) such that ∆i(j)(a) = ∆i′(j)(x), there must exist, by pigeon-hole principle, j = f ∈ {1,... ,m + 1} for which A′ℓ

j

(dℓj) ∪ A′ℓ

(dℓf) is not rainbow, contradicting (FR3). Therefore, c ∈/ {1,... ,n1}. By the above, ∆m+1(a) = ∆m+1(A′0(0)) = c. Moreover, it is easy to see that wj(F′) = wj(F), for all j ∈ {1,... ,n} \ {c} as ∆m+1(A′i(N(d + di))) = ∆m+1(A′i(di)), for all i ∈ {1,... ,q′ − 1}. Hence,  F′ =  F  + 1 = r. ◭

j

f

With this claim, we have shown F′ = {A0(0),A′1(N(d+d1)),... ,A′q′−1(N(d+dq′−1)) ⊆ [N′]} contains q′ fully-rainbow sets B-focused at a−p1(Nd), where Nd,N(d+d1),... ,N(d+dq−1) > h, and  F′ = r, as required for the inductive step.

This proves the inner induction hypothesis and concludes the proof of Theorem 1.3.

References

- [1] V. Bergelson and A. Liebman. Polyonimal extensions of van der Waerden and Szemere´di theorems’. J. Amer. Math. Soc., 9:725–753, 1996.
- [2] W. Deuber, R. L. Graham, H. J. Pro¨mel, and B. Voigt. A canonical partition theorem for equivalence relations on Zt. J. Combin. Theory, Ser. A, 34:331–339, 1983.
- [3] P. Erd˝s and R. L. Graham. Old and new problems and results in combinatorial number theory, volume 28. L’Enseignement Math, Monographie, Geneva, 1980.
- [4] R. L. Graham, B. L. Rothschild, and J. H. Spencer. Ramsey Theory. Wiley, New-York, 1980.
- [5] H. Lefmann. A canonical version for partition regular systems of linear equations. J. Combin. Theory, Ser. A, 41:95–104, 1986.
- [6] H. J. Pro¨mel and V. Ro¨dl. An elementary proof of the canonizing version of Gallai-Witt’s theorem. J. Combin. Theory, Ser. A, 42:144–149, 1986.
- [7] R. Rado. Studien zur kombinatorik. Math. Z., 36:424–470, 1933.
- [8] B. L. van der Waerden. Beweis einer baudetschen vermutung. Nieuw Arch. Wisk., 15:212–216, 1927.
- [9] M. Walters. Combinatorial Proofs of the Polynomial van der Waerden Theorem and the Polynomial HalesJewett Theorem. J. London Math. Soc., 61:1–12, 2000.
- [10] E. Witt. Ein kombinatorischer Satz der Elementargeometrie. Math. Nach., 6:261–262, 1952.


