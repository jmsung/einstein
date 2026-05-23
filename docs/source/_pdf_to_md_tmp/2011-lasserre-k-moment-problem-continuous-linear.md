arXiv:1102.5763v2[math.AG]5Sep2011

THE K-MOMENT PROBLEM FOR CONTINUOUS LINEAR FUNCTIONALS

JEAN B. LASSERRE

Abstract. Given a closed (and non necessarily compact) basic semialgebraic set K ⊆ Rn, we solve the K-moment problem for continuous linear functionals. Namely, we introduce a weighted ℓ1-norm ℓw on R[x], and show that the ℓw-closures of the preordering P and quadratic module Q (associated with the generators of K) is the cone Psd(K) of polynomials nonnegative on K. We also prove that P and Q solve the K-moment problem for ℓw-continuous linear functionals and completely characterize those ℓw-continuous linear functionals nonnegative on P and Q (hence on Psd(K)). When K has a nonempty interior we also provide in explicit form a canonical ℓw-projection gfw for any polynomial f, on the (degree-truncated) preordering or quadratic module. Remarkably, the support of gfw is very sparse and does not depend on K! This enables us to provide an explicit Positivstellensatz on K. At last but not least, we provide a simple characterization of polynomials nonnegative on K, which is crucial in proving the above results.

1. Introduction

This paper is concerned with basic closed semi-algebraic sets K ⊆ Rn and the preordering P(g) and quadratic module Q(g) associated with the ﬁnite family of polynomials (gj), j ∈ J, that generate K. In particular, when K = Rn then the latter two convex cones coincide with the cone Σ[x] of sums of squares (s.o.s.) of polynomials. The convex cones P(g) and Q(g) (which are subcones of the convex cone Psd(K) of polynomials nonnegative on K) are of practical importance because on the one hand nonnegative polynomials are ubiquitous but on the other hand, polynomials in P(g) or Q(g) are much easier to handle. For instance, and in contrast with nonnegative polynomials, checking whether a given polynomial is in Pd(g)(⊂ P(g)) or Qd(g)(⊂ Q(g)) (i.e., with an a priori degree bound d on its representation) can be done eﬃciently by solving a semideﬁnite program, a powerful technique of convex optimization.

The celebrated K-moment problem is concerned with characterizing all

real sequences y = (yα), α ∈ Nn, which can be realized as the moment sequence of some ﬁnite Borel measure on K. For such sequences y, the

![image 1](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile1.png>)

1991 Mathematics Subject Classiﬁcation. 44A60 13B25 14P10 30C10. Key words and phrases. Moment problems; real algebraic geometry; positive polyno-

mials; semi-algebraic sets.

1

linear form Ly associated with y is called a K-moment functional and Haviland’s theorem states that Ly is a K-moment functional if and only if Ly(f) ≥ 0 for all f ∈ Psd(K). And so one says that P(g) (resp. Q(g)) solves the K-moment problem if the K-moment functionals are those which satisfy Ly(f) ≥ 0 on P(g) (resp. Q(g)). However, this is true if and only if P(g) (resp. Q(g)) is dense in Psd(K) for the ﬁnest locally convex topology on R[x]. When K is compact, the K-moment problem was completely solved (with P(g) = Psd(K)) in Schmu¨dgen [15] and soon reﬁned to Q(g) = Psd(K) in Putinar [13] for Archimedean quadratic modules Q(g).

![image 2](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile2.png>)

![image 3](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile3.png>)

Since then, recent contributions have tried to better understand (in even a more general framework) the links between Psd(K) and closures (and sequential closures) of preorderings and quadratic modules, one important goal being to extend (or provide analogues of) Schmu¨dgen and Putinar’s Positivstellensatze¨ [15, 13] to cases where K is not compact. In particular, Scheiderer [14] has shown rather negative results in this direction. For more details on those recent results, the interested is referred to e.g. Powers and Scheiderer [12], Kuhlmann and Marshall [8], Kuhlmann et al. [9], and Cimpric et al. [5].

On the one hand, all linear functionals are continuous in the ﬁnest locally convex topology, on the other hand, the negative results of Scheiderer [14] suggest that solving the K-moment problem via preorderings or quadratic modules is possible only in speciﬁc cases, and so this topology is not the most appropriate in general. So why not rather consider other topologies on R[x] and the K-moment problem for linear functionals Ly that are continuous for these topologies? This is the point of view taken in Ghasemi et al. [6] where the authors consider certain (weighted) norm-topologies and show that the closure of the cone of sums of squares is Psd([−1,1]n) as did Berg [3] for the ℓ1-norm. Notice that this was also the point of view taken in Schmu¨dgen [16] for a class of non commutative (enveloping) ∗-algebra; in the latter context [16], the author proves that the cone of strongly positive elements is the closure of the (smallest) cone of sums of squares in certain topologies.

Contribution. In view of the negative results in Scheiderer [14], we also consider the above mentioned viewpoint and look at the K-moment problem by using a particular weighted ℓ1-norm on R[x] (denoted ℓw for a certain sequence w : Nn → R>0) rather than the usual ﬁnest locally convex topology. In this framework we solve the K-moment problem for basic closed semi-algebraic sets K ⊆ Rn in the following sense. We prove that (a) the ℓw-closure of P(g) and Q(g) is exactly Psd(K), and (b) P(g) and Q(g) solve the moment problem, i.e., the K-moment (ℓw-continuous) functionals are those Ly that are ℓw-continuous and nonnegative on Q(g) (or P(g)). In fact, such linear functionals Ly are characterized by:

- - Ly(h2gj) ≥ 0 for all h ∈ R[x], and every generator gj of K.


- - ∃M > 0 such that |yα| ≤ M wα for all α ∈ Nn.


• Next, when K has a nonempty interior, there exist ℓw-projections of a polynomial onto Pd(g) and Qd(g), where Pd(g) (resp. Qd(g)) denotes the subcone of elements of P(g) (resp. of Q(g)) which have a degree bound d in their representation. In general these projections are not unique but we provide a canonical ℓw-projection gf for any polynomial f, which takes a remarkably simple and “sparse” form, and particularly when ℓw is the usual ℓ1-norm, in which case

n

λi x2id,

- (1.1) gf = f + λ0 +


i=1

for some nonnegative vector λ ∈ Rn+1. In other words, the support gf 0 of gf does not depend on K and does not depend on d either! The dependence of gf on the gj’s that deﬁne K is only through the coeﬃcients (λ∗j). In addition, the support is very sparse since gf 0 ≤ f 0+n+1. This conﬁrms the property of the ℓ1-norm with respect to sparsity, already observed in other contexts. Minimizing the ℓ1-norm aims at ﬁnding a solution with small support (where x 0 = #{i : xi = 0}). Finally, the vector λ in (1.1) is an optimal solution of an explicit semideﬁnite program, and so can be computed eﬃciently.

![image 4](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile4.png>)

• We also provide a canonical ℓ1-projection of f onto P(g) ∩ R[x]2d which is again of the form (1.1), and use this result to characterize the sequential closure P(g)‡ of P(g) for the ﬁnest locally convex topology. Namely,

P(g)‡ = f ∈ R[x] : ∃ d s.t. ∀ǫ > 0, f + ǫ 1 +

n

x2id ∈ P(g) ,

i=1

and the same statement is true for the quadratic module Q(g). This latter result exhibits the particularly simple form q := (1 + ni=1 x2id) for the possible polynomials q in the characterization of P(g)‡ (and Q(g)‡) provided in e.g. [5, 9]; e.g., in [9] it is stated that one may take the polynomial (1 + x 2)s for some s.

• Thanks to the characterization of canonical ℓw-projections, we ﬁnally obtain a Positivstellensatz on K of the following form: f ∈ Psd(K) if and only if for every ǫ > 0, there is some d ∈ N such that the polynomial

f + ǫ(1 + ni=1 dk=1 x2ik/(2k)!) is in P(g) (or Q(g)).

• At last but not least, and crucial for the above results, we prove a result of independent interest, concerned with sequences y = (yα), α ∈ Nn, that have a ﬁnite representing Borel measure µ. Namely, we prove that a polynomial f is nonnegative on the support of µ if and only if h2fdµ ≥ 0

- for all h ∈ R[x]. The paper is organized as follows. In Section 2, and after introducing


the notation and deﬁnitions, we present the intermediate result mentioned above. In Section 3 we show that P(g) and Q(g) solve the K-moment problem for ℓw-continuous linear functionals. In section 4, we provide explicit

expressions for the canonical ℓw-projections onto P(g), Q(g) and their truncated versions. Moreover, we characterize the sequential closures Q(g)‡ and

- P(g)‡ and we end up with a Positivstellensatz for K.


2. Notation, definitions and preliminaries

- 2.1. Notation and deﬁnitions. The notation B stands for the Borel σﬁeld of Rn. Let R[x] (resp. R[x]d) denote the ring of real polynomials in the variables x = (x1,... ,xn) (resp. polynomials of degree at most d), whereas Σ[x] (resp. Σ[x]d) denotes its subset of sums of squares (s.o.s.) polynomials (resp. of s.o.s. of degree at most 2d). For every α ∈ Nn the


notation xα stands for the monomial xα11 ··· xαnn, |α| stands for the integer a := α1 + ··· + αn, and α! stands for the integer a! For an arbitrary set S ⊆ Rn, let Psd(S) denote the convex cone of polynomials that are nonnegative on S.

For every i ∈ N, let Nnd := {β ∈ Nn : j βj ≤ d} whose cardinal is s(d) = n+nd . A polynomial f ∈ R[x] is written

fα xα,

x  → f(x) =

α∈Nn

and f can be identiﬁed with its vector of coeﬃcients f = (fα) in the canonical basis (xα), α ∈ Nn. The support of f ∈ R[x] is the set {α ∈ Nn : fα = 0} and let f 0 := card {α : fα = 0}. Denote by f 1 the ℓ1-norm α |fα| of the coeﬃcient vector f.

Crucial in the sequel is the use of the following ℓw-norm which is a weighted ℓ1-norm deﬁned from the sequence w = (wα), α ∈ Nn, where

- wα := (2⌈|α|/2⌉)!. Namely, denote by f w the ℓw-norm α wα|fα| of the coeﬃcient vector f; hence the ℓ1-norm corresponds to the case where wα = 1 for all α ∈ Nn. Both ℓ1 and ℓw also deﬁne a norm on R[x]d.


Let Sp ⊂ Rp×p denote the space of real p × p symmetric matrices. For any two matrices A,B ∈ Sp, the notation A 0 (resp. ≻ 0) stands for A is positive semideﬁnite (resp. positive deﬁnite), and the notation A,B stands for trace AB.

Let vd(x) = (xα), α ∈ Nnd, and let B0α ∈ Rs(d)×s(d) be real symmetric matrices such that

- (2.1) vd(x)vd(x)T = α∈Nn2d


xα B0α.

Recall that a polynomial g ∈ R[x]2d is a s.o.s. if and only if there exists a real positive semideﬁnite matrix X ∈ Rs(d)×s(d) such that

gα = X,B0α , ∀α ∈ Nn2d.

Let gj ∈ R[x], j = 0,1,... ,m, with g0 being the constant polynomial g0(x) = 1 for all x, and let K ⊆ Rn be the basic closed semi algebraic set:

- (2.2) K := {x ∈ Rn : gj(x) ≥ 0, j = 1,... ,m},


For every J ⊆ {1,... ,m} let gJ := k∈J gk, with the convention g∅ := 1, and let vJ := ⌈(deg gJ)/2⌉ (with vj := v{j}).

Deﬁnition 2.1. With K as in (2.2), let P(g),Q(g) ⊂ R[x] and Pk(g),Qk(g) ⊂ R[x]2k be the convex cones:

P(g) :=   

σJ gJ : σJ ∈ Σ[x], J ⊆ {1,... ,m}  

,

J⊆{1,...,m}

Pk(g) :=   

σJ gJ : σJ ∈ Σ[x]k−vJ, J ⊆ {1,... ,m}  

,

J⊆{1,...,m}

σj gj : σj ∈ Σ[x], j = 1,... ,m  

Q(g) :=   

m

,

j=0

Qk(g) :=   

σj gj : σj ∈ Σ[x]k−vj, j = 1,... ,m  

m

.

j=0

The set P(g) (resp. Q(g)) is a convex cone called the preordering (resp. the quadratic module) associated with the gj’s. Obviously, if h ∈ P(g) (resp. h ∈ Q(g)), the associated s.o.s. weights σJ’s (resp. σj’s) of its representation provide a certiﬁcate of nonnegativity of h on K. The convex cone Pk(g) (resp. Qk(g)) is the subset of elements h ∈ P(g) (resp. h ∈ Q(g)) with a degree bound 2k certiﬁcate. Observe that Pk(g) ⊂ P(g) ∩ R[x]2k and Qk(g) ⊂ Q(g) ∩ R[x]2k.

Moment matrix. With a sequence y = (yα), α ∈ Nn, let Ly : R[x] → R be the linear functional

f (=

α

fα xα)  → Ly(f) =

α

fα yα, f ∈ R[x].

With d ∈ N, the d-moment matrix associated with y is the real symmetric matrix Md(y) with rows and columns indexed in Nnd, and deﬁned by:

- (2.3) Md(y)(α,β) := Ly(xα+β) = yα+β, ∀α,β ∈ Nnd.


yαB0α. It is straightforward to check that Ly(g2) ≥ 0 ∀g ∈ R[x]d ⇔ Md(y) 0, d = 0,1,... .

Alternatively, Md(y) = α∈Nn

2d

A sequence y = (yα) has a representing measure if there exists a ﬁnite Borel measure µ on Rn, such that yα = xαdµ for every α ∈ Nn. Moreover, the measure µ is said to be determinate if it is the unique such measure. Notice that with the ℓw-norm on R[x] is associated a dual norm · ∗w on the dual space R[x]∗ of ℓw-continuous linear functionals on R[x], by

Ly ∗w = sup{|yα|/wα : α ∈ Nn}.

Localizing matrix. With y as above, J ⊆ {1,... ,m}, and gJ ∈ R[x] (with gJ(x) = γ gJγ xγ), the localizing matrix of order d associated with y and gJ is the real symmetric matrix Md(gJ y) with rows and columns indexed by Nnd, and whose entry (α,β) is just

- (2.4)

Md(y)(gJ y)(α,β) := Ly(gJ(x)xα+β) =

γ

gJγ yα+β+γ, ∀α,β ∈ Nnd.

If BJα ∈ Ss(d) is deﬁned by:

- (2.5) gJ(x)vd(x)vd(x)T =

α∈Nn2d+deg g

J

BJα xα, ∀x ∈ Rn,

then Md(gJ y) = α∈Nn

2d+deggJ

yα BJα. Alternatively, Md(gJ y) = Md(z) where z = (zα), α ∈ Nn, with zα = Ly(gJ xα). Multivariate Carleman’s condition. Let y = (yα), α ∈ Nn, be such that Md(y) 0 for all d ∈ N. If for every i = 1,... ,n,

- (2.6)


∞

Ly(x2ik)−1/2k = ∞,

k=1

then y has a ﬁnite representing Borel measure µ on Rn, which in addition, is determinate; see e.g. Berg [3].

![image 5](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile5.png>)

Closures. For a set A ⊂ R[x] we denote by A the closure of A for the ﬁnest locally convex topology on R[x] (treated as a real vector space). With this topology, every ﬁnite-dimensional subspace of R[x] inherits the euclidean topology, so that A also denotes the usual euclidean closure of a subset A ⊂ R[x]d. Following Cimpric et al. [5] and Kuhlmann et al. [9], we also denote by A‡ the set of all elements of R[x] which are expressible as the limit of some sequence of elements of A, and so A‡ is called the sequential closure of A, and clearly A ⊆ A‡ ⊆ A. If A ⊂ R[x] is a convex cone

![image 6](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile6.png>)

![image 7](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile7.png>)

A‡ = {f ∈ R[x] : ∃ q ∈ R[x] s.t. f + ǫq ∈ A, ∀ǫ > 0 },

and in fact, q can be chosen to be in A. Moreover, if A has nonempty interior (equivalently, has an algebraic interior) then A‡ = A.

![image 8](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile8.png>)

Semideﬁnite programming. A semideﬁnite program is a convex (more precisely convex conic) optimization problem of the form

{ C,X : A X = b; X 0 },

inf

X

for some real symmetric matrices C,X ∈ Sp, vector b ∈ Rm, and some linear mapping A : Sp → Rm. Semideﬁnite programming is a powerful technique of convex optimization, ubiquitous in many areas. A semideﬁnite program can be solved eﬃciently and even in time polynomial in the input size of the problem, for ﬁxed arbitrary precision. For more details the interested reader is referred to e.g. [17].

- 2.2. A preliminary result of independent interest. Recall that in a complete separable metric space X, the support of a ﬁnite Borel measure µ (denoted suppµ) is the unique smallest closed set K ⊆ X such that µ(X \ K) = 0.


- Theorem 2.2. Let f ∈ R[x] and µ be a ﬁnite Borel measure with all moments y = (yα), α ∈ Nn, ﬁnite and such that for some M > 0 and all k ∈ N and all i = 1,... ,n, Ly(x2ik) ≤ (2k)! M. Then:


- (2.7) f ≥ 0 on suppµ ⇐⇒ h2 f dµ ≥ 0 ∀h ∈ R[x]

⇐⇒ Md(f y) 0, ∀d = 0,1,...

Proof. The implication ⇒ is clear. For the reverse implication, consider the signed Borel measure ν(B) := B fdµ, for all Borel sets B ∈ B, and let z = (zα), α ∈ Nn, be its sequence of moments. By Lemma 5.1, the sequence z satisﬁes Carleman’s condition (2.6). Next, recalling that Mk(f y) = Mk(z) for every k ∈ N,

h2f dµ ≥ 0 ∀h ∈ R[x] ⇐⇒ Mk(z) 0,∀ k ∈ N.

This combined with the fact that z satisﬁes Carleman’s condition yields that z is the moment sequence of a ﬁnite Borel measure ψ on Rn, which in addition, is determinate. Therefore,

- (2.8) zα = xα f(x)dµ(x) dν(x)


= xα dψ(x), ∀α ∈ Nn.

![image 9](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile9.png>)

![image 10](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile10.png>)

Let Γ+ := {x : f(x) ≥ 0}, Γ− := {x : f(x) < 0} and let µ = µ+ + µ− with µ+(B) = µ(B ∩ Γ+), µ−(B) = µ(B ∩ Γ−), for all B ∈ B. Similarly, let ν = ν+ − ν− with ν+ and ν− being the positive measures deﬁned by ν+(B) = B fdµ+ and ν−(B) = − B fdµ−, for all B ∈ B. Since µ+,µ− ≤ µ, one has

x2ikdµ+(x) ≤ x2ikdµ(x) and x2ikdµ−(x) ≤ x2ikdµ(x),

- for all i = 1,... ,n and all k ∈ N. Therefore, again by Lemma 5.1, both ν+ and ν− satisfy Carleman’s condition (2.6) so that both are determinate. On the other hand, (2.8) can be rewritten,


xα dν+(x) = xα dν−(x) + xα dψ(x), ∀α ∈ Nn,

and so ν+ = ν− + ψ because ν+ and ν− + ψ are determinate. But then 0 = ν+(Γ−) ≥ ν−(Γ−) implies that ν− = 0, i.e., ν = ν+ = ψ, and so the signed Borel measure ν is in fact a positive measure. This in turn implies that f ≥ 0 for all x ∈ suppµ \ G, where G ⊂ suppµ and µ(G) = 0. Notice that by minimality of the support , suppµ \ G = suppµ. Hence let

![image 11](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile11.png>)

![image 12](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile12.png>)

- x ∈ suppµ be ﬁxed, arbitrary. As suppµ \ G = suppµ, there is sequence


(xℓ) ⊂ suppµ \ G such that xℓ → x as ℓ → ∞, and f(xℓ) ≥ 0 for all ℓ. But then continuity of f yields that f(x) ≥ 0.

Interestingly, as we next see, Theorem 2.2 yields alternative characterizations of the cone Psd(S) for an arbitrary closed set S ⊂ Rn.

For a ﬁnite Borel measure µ (with all moments ﬁnite) and a polynomial f ∈ R[x], let µf be the ﬁnite signed Borel measure deﬁned by µf(B) :=

B fdµ for all B ∈ B. Let Θµ := {µσ : σ ∈ Σ[x]}, i.e., Θµ is the set of ﬁnite Borel measures absolutely continuous with respect to µ, and whose density (or Radon Nikodym derivative) is a sum of squares of polynomials.

Let Σ[x]∗ ⊂ R[x]∗ be the dual cone of the cone of Σ[x], i.e., the set of linear forms Ly on R[x] such that Ly(h2) ≥ 0 for all h ∈ R[x], and similarly, let Θ∗µ ⊂ R[x] be the dual cone of Θµ, i.e., Θ∗µ := {h ∈ R[x] : hdν ≥ 0, ∀ν ∈ Θµ}.

Corollary 2.3. Let S ⊆ Rn be an arbitrary closed set and let µ be any ﬁnite Borel measure such that suppµ = S and x  → exp(|xi|) is µ-integrable for all i = 1,... ,n. Then with f ∈ R[x],

- (2.9) f ∈ Psd(S) ⇐⇒ µf ∈ Σ[x]∗
- (2.10) Psd(S) = Θ∗µ.


Proof. Let y = (yα), α ∈ Nn, be the moment sequence of µ. Observe that for every i = 1,... ,n, and all k ∈ N,

x2ik (2k)!

exp (|xi|)dµ(x) ≤ M,

≤

Ly

![image 13](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile13.png>)

S

for some M > 0. Moreover, suppµ = S and so by Theorem 2.2, f ≥ 0 on S if and only if S h2fdµ ≥ 0 for all h ∈ R[x]. Equivalently, if and only if S σdµf ≥ 0 for all σ ∈ Σ[x] (which yields (2.9)), or if and only if

S fdµσ ≥ 0 for all σ ∈ Σ[x], which yields (2.10).

- 3. The K-moment problem for ℓw-continuous linear functionals


We ﬁrst show that Q(g) (and P(g)) solve the K-moment problem for ℓw-continuous linear functionals.

When equipped with the ℓw-norm, we may and will identify R[x] as the subspace of sequences with ﬁnite support, in the Banach space of real inﬁnite sequences f = (fα), α ∈ Nn, that are w-summable, i.e., such that

α wα|fα| < +∞.

Proposition 3.1. The dual of (R[x], · w) is the space (R[x]∗, · ∗w) of linear functionals Ly associated with the sequence y = (yα), α ∈ Nn, which satisfy Ly ∗w < ∞, where Ly ∗w := sup{|yα|/wα : α ∈ Nn}.

Proof. If Ly ∈ R[x]∗ satisﬁes Ly ∗w < ∞, then |Ly(f)| ≤

yα wα

≤ f w Ly ∗w,

|fα|wα

![image 14](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile14.png>)

α

and so Ly is bounded, hence ℓw-continuous. Conversely, if Ly is ℓw-continuous, then consider the sequence of polynomials (fα) ⊂ R[x] with x  → fα(x) :=

- xα/wα for every α ∈ Nn. Then fα w = 1 for every α ∈ Nn, and Ly(fα) =
- yα/wα for all α ∈ Nn. And so, if Ly is ℓw-continuous then sup{|yα|/wα : α ∈ Nn} < +∞.


- Theorem 3.2. Let K ⊆ Rn be as in (2.2) and let y = (yα), α ∈ N, be a given real sequence such that Ly is ℓw-continuous. Then y has a ﬁnite representing Borel measure µ on K if and only if Ly is nonnegative on Q(g). Equivalently if and only if:


- (3.1)


|yα| wα

Ly(h2gj) ≥ 0 ∀ h ∈ R[x], j = 0,... ,m; sup α∈Nn

≤ M for some M.

![image 15](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile15.png>)

Proof. The necessity is clear. Indeed, if y has a representing measure µ on K then Ly(h2gj) = K h2gjdµ ≥ 0 for all h ∈ R[x] and all j = 0,1,... ,m; and so Ly(f) ≥ 0 for all f ∈ Q(g). Moreover, Ly ∗w < ∞ because Ly is ℓw-continuous; hence (3.1) holds.

Suﬃciency. Suppose that Ly is a non trivial ℓw-continuous linear functional, nonnegative on Q(g), i.e., suppose that (3.1) holds. In particular, Ly(x2ik) ≤ M(2k)! for every k ∈ N and every i = 1,... ,n. Therefore, y satisﬁes Carleman’s condition (2.6) and since Mk(y) 0 for all k ∈ N, y has a representing ﬁnite Borel measure µ on Rn, which in addition, is determinate. Next, using Ly(h2gj) ≥ 0 for all h ∈ R[x], and invoking Theorem 2.2, one may conclude that gj ≥ 0 on suppµ, for every j = 1,... ,m. Hence suppµ ⊆ K.

- Theorem 3.2 states that Q(g) solves the K-moment problem for ℓw-

continuous functionals. Of course, Theorem 3.2 is also true if one replaces the quadratic module Q(g) with the preordering P(g).

The ℓw-closure of Q(g) and P(g). Observe that Psd(K) is ℓw-closed. To see this, notice that with every every x ∈ K is associated the Dirac measure δx, whose associated sequence y = (xα), α ∈ Nn, is such that Ly is ℓw-continuous. Indeed, let a := maxi |xi| so that |xα| ≤ a|α|, and let M := exp(a).

M−1 |yα| = exp(a)−1|xα| ≤ exp(a)−1 a|α| < α! ≤ (2⌈|α|/2⌉)! = wα,

and so Ly ∗w < M, i..e., Ly is ℓw-continuous. Therefore, let (fn) ⊂ Psd(K) be such that fn−f w → 0 as n → ∞. As Ly is ℓw-continuous one must have 0 ≤ limn→∞ Ly(fn) = Ly(f) = f(x). As x ∈ K was arbitrary, f ∈ Psd(K).

- Theorem 3.3. Let K ⊆ Rn be as in (2.2) and recall that Psd(K) := {f ∈ R[x] : f ≥ 0 on K}. Then clw(P(g)) = clw(Q(g)) = Psd(K).


Proof. As Psd(K) is ℓw-closed and Q(g) ⊂ Psd(K), clw(Q(g)) ⊆ Psd(K), and so we only have to prove the reverse inclusion. Let f  ∈ clw(Q(g)). Since Q(g) is a convex cone, by the Hahn-Banach separation theorem there

exists an ℓw-continuous linear functional Ly that strictly separates f from clw(Q(g)). That is, there exists y ∈ Nn such that Ly is ℓw-continuous, Ly(f) < 0 and Ly(h) ≥ 0 for all h ∈ clw(Q(g)). By Theorem 3.2, such a y has a representing ﬁnite Borel measure µ on K, and so Ly(f) = K fdµ <

- 0 yields that necessarily f(x0) < 0 for some x0 ∈ K. Hence Psd(K) ⊆ clw(Q(g)), which in turn yields the desired result.


For instance, from Berg [3], the ℓ1-closure of Σ[x] is Psd([−1,1]n). On the other hand, its ℓw-closure is now Psd(Rn), which is what we really want.

It is worth mentioning that Theorem 3.2 and 3.3 can be extended to any preordering or quadratic module (ﬁnitely generated or not). The proof is the same. Any closed set K ⊂ Rn may be represented as the non-negativity set of such a quadratic module (taking generators of the form x  → g(x) :=

n i=1(xi − ai) − r2, for suitable a ∈ Rn and r > 0). However, for reasons

that become obvious in the next section, the focus of the present paper is on the ﬁnitely generated case.

4. Canonical ℓw-projections onto Pd(g) and Qd(g)

As we next see, the ℓw- and ℓ1-norm have the nice feature that one may ﬁnd particular (canonical) projections onto various truncations of P(g) and

- Q(g) with a particularly simple expression. For ℓw- and ℓ1- projections to be well-deﬁned we assume that K has a nonempty interior.


We ﬁrst provide an explicit form of canonical ℓ1- and ℓw-projection of any given polynomial f onto Pd(g) and Qd(g) respectively, and analyze their limit as d → ∞. Then we will consider the projections onto Pd(g)∩R[x]s for ﬁxed s,d ∈ N, which, letting s → ∞, will permit to obtain the projection of f onto P(g) ∩ R[x]d, and so to also characterize the sequential closure P(g)‡.

![image 16](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile16.png>)

As in the previous section, for a polynomial in R[x]t we use indiﬀerently the notation h for both the polynomial and its vector of coeﬃcients h ∈ Rs(t). The context will make clear which one of the two is concerned.

Let K ⊆ Rn be as in (2.2) and consider the following optimization problem:

{ f − h w : h ∈ Pd(g) }.

- (4.1) pdw := inf h


That is, one searches for the best ℓw-approximation of f by an element h∗ of Pd(g), or equivalently, an ℓw-projection of f onto Pd(g). In general, such

- a best approximation h∗ ∈ Pd(g) is not unique1 but we provide a canonical solution with a very simple expression. Of course, and even though (4.1) is well deﬁned for an arbitrary f ∈ R[x], such a problem is of particular interest when f is nonnegative on K but not necessarily an element of P(g).


![image 17](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile17.png>)

1The following example was kindly provided by an anonymous referee: Let n = 2, d = 1, x  → f(x) := −2x1x2, and let C ⊂ R[x]2d be the cone of sums of squares of linear polynomials. Then any polynomial x  → pλ(x) := λ(x1 − x2)2 with λ ∈ [0, 1], is an ℓw-projection (and an ℓ1-projection) of f onto C and f − pλ w = 2.

- Theorem 4.1. Let K ⊆ Rn in (2.2) be with nonempty interior. Let f ∈ R[x] and let 2d ≥ deg f. There is an ℓw-projection of f onto Pd(g) which is a polynomial gfPw ∈ R[x]2d of the form:


- (4.2) x  → gfPw(x) := f(x) + λP0 w +

n

i=1

d

k=1

λPikw

x2ik (2k)!

![image 18](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile18.png>)

,

where the nonnegative vector λPw ∈ Rnd+1 is an optimal solution of the semideﬁnite program:

- (4.3) inf

λ≥0

λ0 +

n

i=1

d

k=1

λik : f + λ0 +

n

i=1

d

k=1

λi

x2ikk (2k)!

![image 19](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile19.png>)

∈ Pd(g) ,

and pdw = f − gfPw w = λP0 w +

n

i=1

d

k=1

λPikw.

Proof. Consider f as an element of R[x]2d by setting fα = 0 whenever |α| > deg f (where |α| = αi), and rewrite (4.1) as the semideﬁnite program:

- (4.4)

pdw := inf

λ,XJ,h

α∈Nn2d

wα λα

s.t. λα + hα ≥ fα, ∀α ∈ Nn2d λα − hα ≥ −fα, ∀α ∈ Nn2d hα −

m

J⊆{1,...,m}

XJ,BJα = 0, ∀α ∈ Nn2d

λ ≥ 0; h ∈ R[x]2d; XJ 0, ∀J ⊆ {1,... ,m}. The dual semideﬁnite program of (4.4) reads:

- (4.5)

 



sup

u,v≥0,y

α∈Nnd

fα(uα − vα)

s.t. uα + vα ≤ wα ∀α ∈ Nn2d uα − vα + yα = 0 ∀α ∈ Nn2d,

Md(gJ y) 0, ∀J ⊆ {1,... ,m}, or, equivalently,

- (4.6)


 

−Ly(f) s.t. Md(gJ y) 0, ∀J ⊆ {1,... ,m} |yα| ≤ wα, ∀α ∈ Nn2d.

sup

y



The semideﬁnite program (4.6) has an optimal solution y∗ because the feasible set is nonempty and compact. In addition, let y = (yα) be the moment sequence of the ﬁnite Borel measure µ(B) = K∩B e− x 2dx, for all B ∈ B, scaled so that |yα| < wα for all α ∈ Nn2d. Then (y,u,v) with u = −min[y,0]

and v = max[y,0], is strictly feasible in (4.5). Indeed, as K has nonempty interior, then necessarily Md(gJ y) ≻ 0 for all J ⊆ {1,... ,m}, and so Slater’s condition2 holds for (4.5). Therefore, by a standard duality result in convex optimization, there is no duality gap between (4.4) and (4.5) (or (4.6)), and (4.4) has an optimal solution (λ∗,(X∗j),gfP). Hence pdw = −Ly∗(f) for any optimal solution y∗ of (4.6).

Next, recall that with J := ∅, Md(g∅ y) = Md(y). Moreover, Md(y) 0 implies Mk(y) 0 for all k ≤ d. By [11, Lemma 1], Mk(y) 0 implies that |yα| ≤ max[Ly(1),maxi Ly(x2ik)], for every α ∈ Nn2k, and all k ≤ d. Therefore, (4.6) has the equivalent formulation

 

pd = −inf

Ly(f)) s.t. Md(gJ y) 0, ∀J ⊆ {1,... ,m} Ly(1) ≤ 1

y

- (4.7)




Ly(x2ik) ≤ (2k)!, k = 1,... ,d; i = 1,... ,n. Indeed, any feasible solution of (4.7) satisﬁes

Ly(x2ik)] ≤ (2k)! = wα,

|yα| ≤ max[Ly(1),max

i

for every α with |α| = 2k and 2k − 1, k = 1,... ,d. The dual of (4.7) is exactly the semideﬁnite program (4.3). Again Slater’s condition holds for

- (4.7) and it has an optimal solution y∗. Therefore (4.3) also has an optimal

solution λPw ∈ Rnd+ +1 with pdw = λPw0 + ni=1 dk=1 λPikw, which is the desired result.

The polynomial gfPw ∈ Pd(g) in (4.2) is what we call the canonical ℓwprojection of f onto Pd(g).

Of course, all statements in Theorem 4.1 remain true if one replaces Pd(g) with Qd(g). Moreover, if wα = 1 for all α (and so ℓw is now the usual ℓ1norm) the polynomial gfPw in (4.2) simpliﬁes and is of the form:

- (4.8) x  → gfP(x) := f(x) + (λP0 +


n

λPi x2id),

i=1

for some nonnegative vector λP ∈ Rn+1. If K = Rn then gfP is the canonical ℓ1-projection of f onto the cone of s.o.s. polynomials., as illustrated in the following example.

Example 1. Let n = 2 and K = R2, in which case Pd(g) = Qd(g) = Σ[x]d for all d ∈ N. Consider the Motzkin-like polynomial3 x  → f(x) =

![image 20](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile20.png>)

2Slater’s condition holds for the conic optimization problem P : infx{c′x : Ax =

- b; x ∈ K}, where K ⊂ Rn is a convex cone and A ∈ Rp×n, if there exists a feasible solution x0 ∈ intK. In this case, there is no duality gap between P and its dual P∗ :


supz{b′z : c − A′z ∈ K∗}. In addition, if the optimal value is bounded then P∗ has an optimal solution.

3Computation was made by running the GloptiPoly software [7] dedicated to solving the generalized problem of moments.

x21x22(x21 + x22 − 1) + 1/27 of degree 6, which is nonnegative but not a s.o.s., and with a global minimum f∗ = 0 attained at 4 global minimizers x∗ = (±(1/3)1/2,±(1/3)1/2). The results are displayed in Table 1 for d = 3,4,5.

d λ∗ pd

![image 21](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile21.png>)

![image 22](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile22.png>)

![image 23](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile23.png>)

![image 24](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile24.png>)

![image 25](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile25.png>)

![image 26](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile26.png>)

![image 27](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile27.png>)

![image 28](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile28.png>)

- 3 ≈ 10−3 (5.445,5.367,5.367) ≈ 1.610−2

![image 29](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile29.png>)

![image 30](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile30.png>)

![image 31](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile31.png>)

![image 32](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile32.png>)

![image 33](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile33.png>)

![image 34](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile34.png>)

- 4 ≈ 10−4 (2.4,9.36,9.36) ≈ 2.10−3

![image 35](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile35.png>)

![image 36](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile36.png>)

![image 37](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile37.png>)

![image 38](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile38.png>)

![image 39](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile39.png>)

![image 40](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile40.png>)

- 5 ≈ 10−5 (0.04,4.34,4.34) ≈ 8.10−5


![image 41](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile41.png>)

![image 42](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile42.png>)

![image 43](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile43.png>)

![image 44](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile44.png>)

![image 45](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile45.png>)

![image 46](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile46.png>)

![image 47](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile47.png>)

![image 48](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile48.png>)

Table 1. Best ℓ1-approximation for the Motzkin polynomial.

- 4.1. Canonical ℓw-projection onto P(g)t ∩ R[x]2d and Q(g)t ∩ R[x]2d. We now consider ℓw-projection of f onto Pt(g) ∩ R[x]2d for given integers d,t ∈ N, i.e.,


- (4.9) pdtw := inf g

{ f − g w : g ∈ Pt(g) ∩ R[x]2d }.

In other words, we are interested in searching for a polynomial of degree 2d in Pt(g) which is the closest to f for the ℓw-norm. For instance, if 2d = deg f, one wishes to ﬁnd an ℓw-projection onto Pt(g) of same degree as f. One may also consider the analogue problem with the quadratic module, i.e., an ℓw-projection onto Qt(g) ∩ R[x]2d. We also analyze the limit as t → ∞.

Theorem 4.2. Let K ⊆ Rn in (2.2) be with nonempty interior and let d ∈ N. Let f ∈ R[x] and let 2t ≥ max[2d,deg f]. There is an ℓw-projection of f onto Pt(g) ∩ R[x]2d which is a polynomial gfPw ∈ R[x]2d of the form:

- (4.10) x  → gfPw(x) = f(x) + λP0 w +

n

i=1

d

k=1

λPikw

x2id (2k)!

![image 49](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile49.png>)

,

where the nonnegative vector λPw ∈ Rnd+1 is an optimal solution of the semideﬁnite program:

- (4.11)


n

d

n

d

pdtw = inf λ≥0

λ0 +

λik : f + λ0 +

λik

i=1

i=1

k=1

k=1

x2id (2k)!

∈ Pt(g) ,

![image 50](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile50.png>)

n

and pdtw = f − gPPwf w = λP0 w +

i=1

d

λPikw.

k=1

Proof. The proof is almost a verbatim copy of that of Theorem 4.1 with a slight diﬀerence. For instance, (4.4) is now replaced with

- (4.12)

pdtw := inf

λ,XJ,h

α∈Nn2d

wα λα

s.t. λα + hα ≥ fα, ∀α ∈ Nn2d λα − hα ≥ −fα, ∀α ∈ Nn2d hα −

m

J⊆{1,...,m}

XJ,BJα = 0, ∀α ∈ Nn2t

λ ≥ 0; h ∈ R[x]2d; XJ 0, ∀J ⊆ {1,... ,m}. (where hα = 0 whenever |α| > 2d) and the dual (4.6) now reads

- (4.13)


 

−Ly(f) s.t. Mt(gJ y) 0, ∀J ⊆ {1,... ,m} |yα| ≤ wα, ∀α ∈ Nn2d.

sup

y



Again with exactly the same arguments, (4.12) has a feasible solution and (4.13) has a strictly feasible solution y, and so Slater’s condition holds for

- (4.13), which in turn implies that there is no duality gap between (4.12) and


- (4.13), and (4.12) has an optimal solution (λ,(XJ),gfPw). However (and this is the only diﬀerence with the proof of Theorem 4.1) now one cannot guarantee any more that (4.13) has an optimal solution because |yα| ≤ wα only for α ∈ Nn2d and not for all α ∈ Nn2t.

As before, we call gfPw in (4.10) the canonical ℓw-projection of f onto Pt(g) ∩ R[x]2d. Of course, an analogue of Theorem 4.2 (with obvious ad hoc adjustments) holds for the canonical ℓw-projection gfQw onto Qt(g)∩R[x]2d. Also and again, if wα = 1 for all α ∈ Nn2d, then the polynomial gfPw in (4.10) simpliﬁes to the form in (4.8).

We next analyze the behavior of gfPw as t → ∞ to obtain the canonical ℓw-projection of f onto P(g) ∩ R[x]2d. Recall that

![image 51](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile51.png>)

![image 52](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile52.png>)

P(g) ∩ R[x]2d =   t≥0

![image 53](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile53.png>)

Pt(g)

 ∩ R[x]2d =

![image 54](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile54.png>)

t≥0

Ptd(g).

Corollary 4.3. Let K ⊆ Rn be as in (2.2) and with nonempty interior, f ∈ R[x]2d, and let gfPw(t) ∈ Pt(g) ∩ R[x]2d be an optimal solution of (4.9). Then there is an ℓw-projection of f onto P(g) ∩ R[x]2d which is a polynomial gfw ∈ R[x]2d of the form

![image 55](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile55.png>)

- (4.14) x  → gfw(x) = f(x) + λ∗0 +


d

n

λ∗ik x2id ,

i=1

k=1

for some nonnegative vector λ∗ ∈ Rdn+1. In particular, if K is compact and f ≥ 0 on K then λ∗ = 0 and gfw = f.

Proof. Let (pdtw), t ∈ N, be the sequence of optimal values of (4.9), which is nonnegative and monotone non increasing. Therefore it converges to some nonnegative value pdw ≥ 0. For every t ∈ N, (4.9) has an optimal solution gfPw(t) of the form

- (4.15) x  → gfPw(t)(x) = f(x)+λP0 w(t)+

n

i=1

d

k=1

λPikw(t)

x2ik 2k!

![image 56](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile56.png>)

, ∀x ∈ Rn,

with λPw(t) ≥ 0 and i,k λPikw(t) = pdtw ≤ pdt0w. Hence there is a subsequence (tj), j ∈ N, and some nonnegative vector λ∗ ∈ Rnd+ +1 such that λPw(tj) → λ∗ as j → ∞. In addition,

pdw = lim

j→∞

pdtjw = lim

j→∞

λP0 w(tj) +

n

i=1

d

k=1

λPikw(tj) = λ∗0 +

n

i=1

d

k=1

λ∗ik.

Hence gfPw(tj) → gfw ∈ R[x]2d as j → ∞ where gfw is as in (4.14). And of course, as gfPw(t) − gfw w → 0, gfw is in the closure P(g) ∩ R[x]2d of P(g) ∩ R[x]2d.

![image 57](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile57.png>)

Next, suppose that there exists h ∈ P(g) ∩ R[x]2d with f − h w < f − gfw w. Then there exists a sequence (ht) ⊂ R[x]2d, t ∈ N, with ht ∈ Ptd(g) such that ht − h w → 0 as t → ∞. But then

![image 58](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile58.png>)

f − h w = f − ht + ht − h w ≥ f − ht w

![image 59](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile59.png>)

![image 60](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile60.png>)

≥ f−gfPw(t) w

− ht − h w →0 as t→∞

![image 61](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile61.png>)

![image 62](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile62.png>)

, ∀ t,

and so taking limit as t → ∞ yields the contradiction f − gfw w > f − h w ≥ lim

t→∞

f − gfPw(t) w = f − gfw w.

Therefore f − gfw w = minh { f − h w : h ∈ P(g) ∩ R[x]2d}.

![image 63](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile63.png>)

The last statement (when K is compact) follows from Schmu¨dgen’s Positivstellensatz [15] which implies that if f is nonnegative on K then f + ǫ ∈

- P(g) for every ǫ > 0.

Of course there is an analogue of Corollary 4.3 with Q(g) in lieu of P(g). The only change is concerned with the last statement where one needs that

- Q(g) is Archimedean. And also, if wα = 1 for every α ∈ Nn, then gfw in


(4.14) simpliﬁes to the form (4.8). 4.2. The sequential closures of P(g) and Q(g). Recall that for any convex cone A ⊂ R[x]

- (4.16) A‡ = {f ∈ R[x] : ∃ q ∈ R[x] s.t. f + ǫq ∈ A, ∀ǫ > 0 }.


We have seen that P(g) ⊂ P(g)‡ ⊆ P(g), where A denotes the closure of A for the ﬁnest locally convex topology. Therefore, it is of particular interest

![image 64](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile64.png>)

![image 65](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile65.png>)

to describe P(g)‡, which the goal of this section. We know that

- (4.17) P(g)‡ = d∈N

![image 66](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile66.png>)

P(g) ∩ R[x]d,

and if for instance P(g) has an algebraic interior then P(g) = P(g)‡. (See e.g. Kuhlmann and Marshall [9, Prop. 1.4] and Cimpric et al. [5, Prop. 1.3].)

![image 67](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile67.png>)

Notice that Q(g)‡ = d∈N Q(g) ∩ R[x]d ([9]) and by [5, Prop. 1.3], we also have Q(g) = Q(g)‡ if Q(g) is archimedean. Theorem 4.4. Assume that K ⊆ Rn in (2.2) has a nonempty interior and let f ∈ R[x]. Then:

![image 68](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile68.png>)

![image 69](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile69.png>)

- (a) f ∈ P(g)‡ if and only if there is some d ∈ N such that for every ǫ > 0,

the polynomial

(4.18) x  → f(x) + ǫ 1 +

n

i=1

x2id is in P(g).

- (b) The same statement as (a) also holds with Q(g) instead of P(g). In other words, q ∈ R[x] in (4.16) for A = P(g) can be taken as x  →




(1+ ni=1 x2id) independently of K. The dependence of q on f is through the power d only.

Proof. (a) From (4.17) f ∈ P(g)‡ if and only if f ∈ P(g) ∩ R[x]2d for some d ∈ N. Next, by Corollary 4.3, f ∈ P(g) ∩ R[x]2d if and only if the polynomial gfw ∈ R[x]2d deﬁned in (4.14) (and which simpliﬁes to (4.8) when wα = 1 for all α ∈ Nn) is identical to f. But then this implies that the polynomial gfPw(t) ∈ Pt(g) ∩ R[x]2d in (4.15) is such that ni=0 λPi w(t) → 0 as t → ∞ (recall that wα = 1 for all α ∈ Nn). Let λ(t) := maxi[λPi w(t)] so that λ(t) → 0 as t → ∞, and the polynomial

![image 70](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile70.png>)

![image 71](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile71.png>)

x  → f(x) + λ(t) 1 +

n

x2id

i=1

belongs to Pt(g) ∩ R[x]2d because

f + λ(t) 1 +

n

x2id = gfPw(t) + λ(t) − λP0 (t)

+

![image 72](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile72.png>)

![image 73](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile73.png>)

i=1

≥0

n

(λ(t) − λPf (t)) ≥0

x2id.

i=1

![image 74](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile74.png>)

![image 75](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile75.png>)

Therefore, for every ǫ > 0, choosing tǫ such that λ(tǫ) ≤ ǫ ensures that the polynomial f +ǫ(1+ ni=1 x2id) is in Ptǫ(g)∩R[x]2d, which implies the desired result in (a).

The proof of (b) is omitted as it follows similar arguments. Indeed, it was already mentioned that Theorem 4.2 and Corollary 4.3 have obvious analogues for the quadratic module Q(g).

2k i

Of course in (4.18) one may replace 1+ ni=1 x2id with 1+ ni=1 dk=1 x

(2k)!. In fact, and as pointed out by an anonymous referee, in (a) one may also replace 1 + ni=1 x2id with any point in the interior of Pd(g) in R[x]2d and in (b) with any point in the interior of Qd(g) in R[x]2d. The fact that

![image 76](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile76.png>)

- 1 + ni=1 x2id is an interior point of Σ[x]d in R[x]2d (and hence also an interior point of Pd(g) and Qd(g) in R[x]2d) seems to be well-known. For instance, it can be deduced from [11, Theorem 3].


4.3. A Positivstellensatz for non compact K. As we know how to project with the ℓw-norm, we are now able to obtain the following Positivstellensatz on K.

Corollary 4.5. Let K ⊆ Rn in (2.2) be nonempty interior. Then f ≥ 0 on K if and only if for every ǫ > 0 there exists d ∈ N such that

n

- (4.19) x  → f(x) + ǫ 1 +


i=1

d

x2ik (2k)!

![image 77](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile77.png>)

k=1

∈ P(g).

Proof. The only if part: Recall that P(g) = d≥0 Pd(g), and from Theorem 3.3, Psd(K) = clw(P(g)). Let gfPw(d) ∈ R[x]2d be the canonical ℓwprojection of f onto Pd(g) given in (4.2), where pdw = λP0 w+ ni=1 dk=1 λPikw. As f ∈ clw(P(g)), we necessarily have limd→∞ pdw = 0, because f − gfPw(d) w → 0. Hence given ǫ > 0, let d be such that maxi,k λPikw ≤ ǫ. Then

d

n

x2ik (2k)!

f + ǫ 1 +

![image 78](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile78.png>)

i=1

k=1

n

= gfPw(d) + (ǫ − λP0 w) +

i=1

![image 79](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile79.png>)

∈Σ[x]

d

x2ik (2k)!

(ǫ − λPikw)

,

![image 80](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile80.png>)

k=1

![image 81](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile81.png>)

2k i

and so f + ǫ(1 + ni=1 dk=1 x

(2k)!) ∈ P(g). The if part. Let qd ∈ R[x] be the polynomial in (4.19), and let x ∈ K be

![image 82](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile82.png>)

ﬁxed, arbitrary. Then 0 ≤ qd(x) ≤ f(x)+ǫ ni=1 exp |xi|. Therefore, letting ǫ → 0 yields f(x) ≥ 0.

5. Appendix Lemma 5.1. Let µ a ﬁnite Borel measure whose sequence of moments y = (yα), α ∈ Nn, is such that for all i = 1,... ,n, and all k ∈ N, Ly(x2ik) ≤ (2k!)M for some M. Let f ∈ R[x] be such that Ly(x2itf) ≥ 0 for all i = 1,... ,n, and all t ∈ N. Then the sequence zf = (zαf), α ∈ Nn, where

- zαf = Lzf(xα) := Ly(xαf) for all α ∈ Nn, satisﬁes Carleman’s condition (2.6).


Proof. Let 1 ≤ i ≤ n be ﬁxed arbitrary, and let 2s ≥ degf. Observe that whenever |α| ≤ k, |x|α ≤ |xj|k on the subset Wj := {x ∈ Rn \ [−1,1]n :

|xj| = maxi |xi|}. And so, |f(x)| ≤ f 1 |xj|2s for all x ∈ Wj. Hence, Lzf(x2ik) = f(x)x2ikdµ(x) ≤

n

xj2(k+s)dµ(x)

|f(x)|x2ikdµ(x) + f 1

[−1,1]n

j=1 Wj

≤ M f 1 + Mn f 1 (2(k + s))! ≤ 2Mn f 1 (2(k + s))!, and so we have

(k+s)/k

Lzf(x2ik)−1/2k ≥ (2Mn f 1)−1/2k ((2(k + s))!)−1/2(k+s)

≥

≥

- 1

![image 83](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile83.png>)

- 2


- 1

![image 84](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile84.png>)

- 2


((2(k + s))!)−1/2(k+s)

(k+s)/k

1 2(k + s)

![image 85](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile85.png>)

(k+s)/k

,

where k ≥ k0 is suﬃciently large so that (2Mn f 1)−1/2k ≥ 1/2. Therefore,

∞

∞

(k+s)/k

- 1

![image 86](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile86.png>)

- 2


1 2(k + s)

Lzf(x2ik)−1/2k ≥

= +∞.

![image 87](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile87.png>)

k=1

k=k0

where the last equality follows from (2(k1+s))(k+s)/k = (2(k1+s))(2(k1+s))s/k and (2(k1+s))s/k ≥ 1/2 whenever k is suﬃciently large, say k ≥ k1. Hence the sequence zf satisﬁes Carleman’s condition (2.6).

![image 88](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile88.png>)

![image 89](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile89.png>)

![image 90](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile90.png>)

![image 91](<2011-lasserre-k-moment-problem-continuous-linear_images/imageFile91.png>)

Acknowledgement. The author wishes to thank an anonymous referee for several comments and suggestions that helped writing the ﬁnal version.

References

- [1] R. Ash. Real Analysis and Probability, Academic Press, Inc., Boston (1972).
- [2] C. Berg, J.P.R. Christensen and P. Ressel, Positive deﬁnite functions on Abelian semigroups. Math. Ann. 223, 253–274 (1976)
- [3] C. Berg, The multidimensional moment problem and semigroups. Proc. Symp. Appl. Math. 37, 110–124 (1987).
- [4] G. Blekherman, There are signiﬁcantly more nonnegative polynomials than sums of squares, Isr. J. Math. 153, 355-380 (2006)
- [5] J. Cimpric, M. Marshall, T. Netzer, Closures of quadratic modules, Israel J. Math., to appear.
- [6] M. Ghasemi, S. Kuhlmann, E. Samei, The moment problem for continuous positive semideﬁnite linear functionals, arXiv:1010.279v3, November 2010.
- [7] D. Henrion, J.B. Lasserre and J. Lofberg, Gloptipoly 3: moments, optimization and semideﬁnite programming, Optim. Methods and Software 24, 761–779 (2009)
- [8] S. Kuhlmann, M. Marshall, Positivity sums of squares and the multidimensional moment problem, Trans. Amer. Math. Soc. 354, 4285–4301 (2002)
- [9] S. Kuhlmann, M. Marshall, N. Schwartz, Positivity sums of squares and the multidimensional moment problem II, Adv. Geom. 5, 583–606 (2005)
- [10] J.B. Lasserre and T. Netzer, SOS approximations of nonnegative polynomials via simple high degree perturbations, Math. Z. 256, 99–112 (2006)


- [11] J.B. Lasserre, Suﬃcient conditions for a real polynomial to be a sum of squares, Arch. Math. 89, 390–398 (2007)
- [12] V. powers, C. Scheiderer, The moment problem for non-compact semialgebraic sets, Adv. Geom. 1, 71–88 (2001)
- [13] M. Putinar, Positive polynomials on compact sets, Ind. Univ. Math. J. 42, 969–984

(1993).

- [14] C. Scheiderer, Positivity and sums of squares: A guide to recent results. In: Emerging Applications of Algebraic Geometry (M. Putinar, S. Sullivant, eds.), IMA Volumes Math. Appl. 149, Springer, 2009, pp. 271-324.
- [15] K. Schmudgen¨ , The K-moment problem for compact semi-algebraic sets, Math. Ann. 289, 203–206 (1991).
- [16] K. Schmudgen¨ , Positive cones in enveloping algebras, Rep. Math. Physics 14, 385– 404 (1978).
- [17] L. Vandenberghe and S. Boyd, Semideﬁnite programming, SIAM Rev. 38, 49–95


(1996)

LAAS-CNRS and Institute of Mathematics, University of Toulouse, LAAS, 7 avenue du Colonel Roche, 31077 Toulouse C´edex 4,France

E-mail address: lasserre@laas.fr

