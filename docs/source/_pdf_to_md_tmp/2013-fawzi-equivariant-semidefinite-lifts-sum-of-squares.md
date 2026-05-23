# arXiv:1312.6662v3[math.OC]15Apr2015

## Equivariant semideﬁnite lifts and sum-of-squares hierarchies

Hamza Fawzi James Saunderson Pablo A. Parrilo April 15, 2015

Abstract

A central question in optimization is to maximize (or minimize) a linear function over a given polytope P. To solve such a problem in practice one needs a concise description of the polytope P. In this paper we are interested in representations of P using the positive semideﬁnite cone: a positive semideﬁnite lift (psd lift) of a polytope P is a representation of P as the projection of an aﬃne slice of the positive semideﬁnite cone Sd+. Such a representation allows linear optimization problems over P to be written as semideﬁnite programs of size d. Such representations can be beneﬁcial in practice when d is much smaller than the number of facets of the polytope P. In this paper we are concerned with so-called equivariant psd lifts (also known as symmetric psd lifts) which respect the symmetries of the polytope P.

We present a representation-theoretic framework to study equivariant psd lifts of a certain class of symmetric polytopes known as orbitopes. Our main result is a structure theorem where we show that any equivariant psd lift of size d of an orbitope is of sum-of-squares type where the functions in the sum-of-squares decomposition come from an invariant subspace of dimension smaller than d3. We use this framework to study two well-known families of polytopes, namely the parity polytope and the cut polytope, and we prove exponential lower bounds for equivariant psd lifts of these polytopes.

### 1 Introduction

#### 1.1 Preliminaries and deﬁnitions

Linear programming is the problem of computing the maximum (or minimum) of a linear function over a polytope P. In order to solve such a problem in practice one needs to have an eﬃcient description of the polytope P. An important technique to obtain such eﬃcient formulations which has received renewed attention recently is that of extended formulations or lifts: the idea is to represent P as the projection of a higher-dimensional convex set Q which has a simpler description than P. For the purpose of optimizing a linear function, one can work over the higher-dimensional convex set Q instead of P: indeed if P = π(Q) where π is a linear projection map and is the linear objective function then we have:

( ◦ π)(y). (1)

max

(x) = max

x∈P

y∈Q

There are many examples where extended formulations allow us to reduce the size of optimization problems. Consider for example the 1 ball in Rn which requires 2n linear inequalities for its description: using a simple construction one can show that this polytope is the projection of a polytope in R2n which can be described using 2n linear inequalities only.

When lifting the polytope P to a higher-dimensional convex set Q, it is natural to consider convex sets Q of the form Q = K ∩ L where K is a proper cone (i.e., a convex, closed, full-dimensional and pointed cone) and L is an aﬃne subspace. Indeed in this case the optimization problem (1) over Q is a conic program [BTN01]. When the cone K is the nonnegative orthant K = Rm+ a K-lift is usually referred to as an LP lift since the resulting optimization problem is a linear program. Another important special case, which is the main focus of this paper, is when K is the cone of positive semideﬁnite matrices K = Sd+. In this case the lift is called a psd lift of size d and the resulting optimization problem (1) over Q is a semideﬁnite program.

The authors are with the Laboratory for Information and Decision Systems, Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology, Cambridge, MA 02139. Email: {hfawzi,jamess,parrilo}@mit.edu. This research was funded in part by AFOSR FA9550-11-1-0305 and AFOSR FA9550-12-1-0287.

- Deﬁnition 1. Let P ⊂ Rn be a polytope. We say that P has a psd lift of size d if there exist an aﬃne subspace L ⊂ Sd and a linear map π : Sd → Rn such that P = π(Sd+ ∩ L).

The polytope P ⊂ Rn of interest often has a lot of symmetries, i.e., it is invariant under a certain group of transformations of Rn. For example the square [−1,1]2 in the plane is invariant under permutation of coordinates; and the regular n-gon is invariant under the action of the dihedral group D2n consisting of n rotations and n reﬂections. For such symmetric polytopes one may be interested in lifts that “respect” this symmetry. In the context of linear programming, such lifts were ﬁrst studied by Yannakakis [Yan91] where he showed that any symmetric LP lift of the matching polytope must have exponential size. In the more recent works [KPT10, Goe14, Pas09, GPT13], it was shown that the symmetry requirement can have a signiﬁcant impact on the size of the smallest lifts, i.e., there are polytopes (like the permutahedron for example) where there is a large gap between the smallest LP lift and the smallest symmetric LP lift. The recent work of Chan el al. [CLRS13] establishes, among others, a strong connection between symmetric LP lifts and the Sherali-Adams hierarchy: it is shown that the approximation quality of any polynomial-size symmetric LP for the maximum cut problem can be achieved by a constant number of rounds of the Sherali-Adams hierarchy (in fact the paper [CLRS13] establishes a connection between general LP formulations, possibly nonsymmetric, and the Sherali-Adams hierarchy however the results are stronger in the case of symmetric LPs).

The works cited above studied the symmetry requirement in the context of LP lifts. In this paper we are interested in psd lifts that respect the symmetries of the polytope P. Intuitively a psd lift P = π(Q) where Q = Sd+ ∩ L respects the symmetry of P if any transformation g ∈ GL(Rn) which leaves P invariant can be lifted to a transformation Φ(g) ∈ GL(Sd) that preserves both Sd+ and L, and so that the following equivariance relation holds: for any y ∈ Q, π(Φ(g)y) = gπ(y). Such lifts are commonly called symmetric in the literature [KPT10, GPT13]. In this paper however we prefer to use instead the term equivariant which is more descriptive and mathematically standard. It is known that the transformations of Sd which leave the psd cone Sd+ invariant are precisely congruence transformations, see e.g. [Tun00, Theorem 9.6.1]. This motivates the following deﬁnition of equivariant psd lift which we adopt in this paper:

- Deﬁnition 2. Let P ⊂ Rn be a polytope invariant under the action of a group G ⊂ GL(Rn). Assume


P = π(Sd+ ∩ L) is a psd lift of P of size d. The lift is called G-equivariant if there is a group homomorphism ρ : G → GL(Rd) such that the following two conditions hold:

- (i) The subspace L is invariant under congruence by ρ(g), for all g ∈ G: ρ(g)Y ρ(g)T ∈ L ∀g ∈ G, ∀Y ∈ L. (2)
- (ii) The following equivariance relation holds:


π ρ(g)Y ρ(g)T = gπ(Y ) ∀g ∈ G, ∀Y ∈ Sd+ ∩ L. (3)

Observe that the notion of equivariant lift is deﬁned with respect to a group G which leaves P invariant. The group G does not have to be the full automorphism group Aut(P) in general. Indeed one may be interested in lifts that preserve only a certain subset of the symmetries of P, but not all of them. One example we discuss in detail later is the parity polytope which is invariant under permutation of coordinates as well as under certain sign switches. In Section 4 we mention two examples of well-known lifts of the parity polytope which are equivariant with respect to one set of transformations but not the other.

Examples To illustrate the deﬁnition of equivariant psd lift, we now give a simple example of an equivariant psd lift and another example of a psd lift that does not satisfy the deﬁnition of equivariance.

- Example 1. An equivariant psd lift of the square [−1,1]2 Consider the square [−1,1]2 in the plane. The following is a well-known positive semideﬁnite lift of [−1,1]2 of size 3:


 

 

 

  0

1 x1 x2 x1 1 u x2 u 1

[−1,1]2 =

(x1,x2) ∈ R2 : ∃u ∈ R

. (4)





We can write this lift in standard form as [−1,1]2 = π(S3+ ∩ L) where L and π are given by: L = {X ∈ S3 : X11 = X22 = X33 = 1} and π(X) = (X12,X13) ∈ R2. Note that the intersection S3+ ∩ L is known as the elliptope in S3 and is illustrated in Figure 1.

![image 1](<2013-fawzi-equivariant-semidefinite-lifts-sum-of-squares_images/imageFile1.png>)

Figure 1. A positive semideﬁnite lift of the square [−1, 1]2: the elliptope {X ∈ S3+ : diag(X) = 1} linearly projects onto the square [−1, 1]2.

The symmetry group of the square [−1,1]2 is the dihedral group of order 8, denoted D8. To show that the lift (4) is D8-equivariant, consider the group homomorphism ρ : D8 → GL(R3) deﬁned by:

1 0 0 g ∀g ∈ D8.

ρ(g) =

It is easy to see that the congruence operation by ρ(g) stabilizes the subspace L, and that the following equivariance relation holds:

π(ρ(g)Xρ(g)T) = gπ(X) ∀g ∈ D8,∀X ∈ S3+ ∩ L. Thus this shows that the psd lift (4) is D8-equivariant. ♦

We show later in the paper that any psd lift obtained from the Lasserre/theta-body hierarchy [Las09, GPT10] is in fact equivariant. For example, one concrete such psd lift is that of the stable set polytope for perfect graphs, which was originally introduced by Lov´sz [Lov79] and which can be understood as an instance of the Lasserre/theta-body lifts, see [GPT10, Section 3.1].

We now show an example of a non-equivariant psd lift.

- Example 2. A nonequivariant psd lift of the hyperboloid Let H be the hyperboloid in R3 deﬁned by:


H = {(x1,x2,x3) ∈ R3 : x1,x2,x3 ≥ 0 and x1x2x3 ≥ 1}. One can construct a psd lift of H of size 6 as follows (see e.g., [BPT13, page 261]): H = (x1,x2,x3) ∈ R3 : ∃y,z ≥ 0 x1x2 ≥ y2, x3 ≥ z2, yz ≥ 1

- x1 y
- y x2


x3 z z 1

y 1 1 z

= (x1,x2,x3) ∈ R3 : ∃y,z

0,

0,

0 .

(5)

The hyperboloid H is clearly invariant under permutation of coordinates, i.e., for any permutation σ ∈ S3 we have (x1,x2,x3) ∈ H ⇒ σ · (x1,x2,x3) ∈ H. However the lift we just constructed does not respect this symmetry: indeed to construct the lift we imposed a particular ordering of the variables where the last coordinate x3 does not play the same role as the ﬁrst two coordinates x1 and x2. It is not diﬃcult to formally show that the lift (5) does not satisfy Deﬁnition 2 of equivariance when G = S3. Note however that the lift is equivariant with respect to permuting the coordinates x1 and x2. ♦

Relation with symmetric LP lift It is not hard to see that symmetric LP lifts can be interpreted as equivariant psd lifts, where each ρ(g) consists of a permutation matrix. In fact, recall that an LP lift of a polytope P takes the form P = π(Rd+ ∩ L) where L is an aﬃne subspace of Rd and π : Rd → Rn is a linear map. An LP lift P = π(Rd+ ∩ L) is called G-symmetric (or G-equivariant) if there exists θ : G → Sd (where Sd is the group of permutations on d elements) such that for any y ∈ Rd+ ∩ L, π(θ(g) · y) = g · π(y). By working with diagonal matrices, any symmetric LP lift can be rewritten as an equivariant PSD lift: Indeed, if P = π(Rd+ ∩ L) is a symmetric LP lift of P, then P = π(Sd+ ∩ L) is an equivariant psd lift where L = {Y ∈ Sd,Y is diagonal and diag(Y ) ∈ L} and π = π ◦ diag where diag : Sd → Rd is the operator extracting the diagonal of a symmetric matrix. This psd lift clearly satisﬁes the deﬁnition of equivariance where ρ(g) is the permutation matrix associated to θ(g).

#### 1.2 Positive semideﬁnite lifts and sums-of-squares

Positive semideﬁnite lifts have a strong connection with sums-of-squares certiﬁcates for nonnegativity. A generic way to construct positive semideﬁnite lifts of a polytope P is to look for “small” sum-of-squares certiﬁcates for the facet-deﬁning inequalities of P. In order to make this statement precise, we ﬁrst introduce some notations and deﬁnitions that will be crucial for the rest of this paper. Given a ﬁnite set X ⊂ Rn, we let F(X,R) be the space of real-valued functions on X. Note that dimF(X,R) = |X|. Furthermore, we endow F(X,R) with pointwise multiplication operation:

(f1f2)(x) = f1(x)f2(x) ∀x ∈ X ∀f1,f2 ∈ F(X,R). We introduce the following important deﬁnition which will be used throughout the paper:

- Deﬁnition 3. Let X ⊂ Rn be a ﬁnite set. Let f ∈ F(X,R) and let V be a subspace of F(X,R). We say that f is V -sos on X if there exist functions f1,...,fJ ∈ V such that f = f12 + ··· + fJ2.


Given a ﬁnite set X ⊂ Rn and a linear form on Rn, deﬁne max := maxx∈X (x). Observe that max −

takes only nonnegative values on X, i.e., max− (x) ≥ 0 for all x ∈ X. In other words max− |X ∈ F(X,R) is a nonnegative function on X. The following theorem establishes a relation between sum-of-squares certiﬁcates of max − on X and psd lifts of conv(X). The theorem is essentially due to Lasserre [Las09] and Gouveia et al. [GPT10].

- Theorem A. Let X ⊂ Rn be a ﬁnite set and assume that X spans Rn. Assume there is a subspace V of


F(X,R) such that for any linear form on Rn, max − is V -sos on X, where max := maxx∈X (x). Then conv(X) has an (explicit) psd lift of size dimV .

- Remark 1. Lasserre [Las09] and Gouveia et al. [GPT10] considered the special case where V is the space of polynomials of degree at most k on X. However the same arguments in [Las09] and [GPT10] actually apply more generally to any subspace V of functions in F(X,R).


Theorem A can actually be (almost) turned into an exact characterization of psd lifts of conv(X). Indeed one can show that if conv(X) has a psd lift of size d, then there exists a subspace V of F(X,R) with dimV ≤ d2 such that for any linear form on Rn, max − is V -sos on X. This partial converse to Theorem

- A can be proven using the factorization theorem [GPT13, Theorem 1] (see also Theorem 11 in Appendix B). Assume now that X is invariant under the action of a group G and that we are looking for a G-equivariant


psd lift. In this case it is not hard to formulate a version of Theorem A where the psd lift produced is guaranteed to be equivariant. To make this precise, we need the following deﬁnition: Observe that the action of G on X induces an action on F(X,R) deﬁned by:

(g · f)(x) = f(g−1 · x)

for any g ∈ G,f ∈ F(X,R),x ∈ X (this action is known as the left regular representation of G). A subspace V of F(X,R) is called G-invariant if g · f ∈ V for any f ∈ V and g ∈ G. Then one can show that if the subspace V in Theorem A is G-invariant, then the resulting psd lift of conv(X) is G-equivariant:

- Theorem B. Let X ⊂ Rn be a ﬁnite set that spans Rn and assume that X is invariant under the action of a group G. Assume furthermore that there is a G-invariant subspace V of F(X,R) such that for any


linear form on Rn, max − is V -sos on X, where max := maxx∈X (x). Then conv(X) has an (explicit) G-equivariant psd lift of size dimV .

Proof. We provide the proof in Appendix A.

| |
|---|


We saw earlier that Theorem A for general psd lifts is actually almost tight, since it admits a partial converse. One of the main contributions of this paper is to show that a similar partial converse to Theorem

- B also holds (cf. Theorem 1 to follow). As mentioned earlier, the well-known Lasserre/theta-body lift of conv(X) can be understood in the


context above by taking V to be the space of polynomials of degree at most k on X. We say that a function

- f ∈ F(X,R) is a polynomial of degree at most k on X if there exists a polynomial p ∈ R[x1,...,xn] with deg p ≤ k such that f(x) = p(x) for all x ∈ X. We denote by Pol≤k(X) the subspace of F(X,R) consisting of polynomials of degree at most k on X. The following deﬁnition of theta-rank from [GPT10] will be useful later in the paper:


- Deﬁnition 4 (Theta-rank [GPT10]). Let X be a ﬁnite subset of Rn. The theta-rank of X is the smallest integer k such that the following holds: for any linear form on Rn, max − is Pol≤k(X)-sos on X where


max := maxx∈X (x).

Note that if X has theta-rank k then by Theorem B, conv(X) has an equivariant psd lift of size dimPol≤k(X), since Pol≤k(X) is a G-invariant subspace of F(X,R).

The explicit lifts In this paragraph we describe the explicit psd lift that one obtains from Theorems A and B. The details of this construction are not, strictly speaking, needed for the rest of this paper. However we believe that the description given here is beneﬁcial for some of the discussions in Sections 4 and 5 on the parity polytope and the cut polytope. The construction we describe here is essentially due to [Las09, GPT10]. Let ei ∈ F(X,R), for i = 1,...,n be deﬁned by ei(x) = xi and let F(X,R)∗ be the space of linear forms on F(X,R). If V is a subspace of F(X,R) that satisﬁes the assumption of Theorem A, then one can show that we have the following explicit psd lift of conv(X) (Theorem A):

conv(X) = THV (X) (6) where

THV (X) := (E(e1),...,E(en)) : E ∈ F(X,R)∗ where

(7)

E(1) = 1, E(f2) ≥ 0 ∀f ∈ V .

Note that by picking a basis for V , the constraint E(f2) ≥ 0 ∀f ∈ V in (7) can be written as a psd constraint of size d (we refer to Appendix A for more details on how to write (7) in the form conv(X) = π(Sd+ ∩L)). In the deﬁnition of THV (X), one can think of E ∈ F(X,R)∗ as playing the role of an expectation operator for a certain measure supported on X (E is sometimes called a pseudo-expectation, see e.g., [LRS14]). In fact one can compare (7) to the following trivial representation of conv(X):

conv(X) = (E(e1),...,E(en)) : E ∈ F(X,R)∗ where E(f) =

f(x)dµ(x)

X

for some prob. measure µ on X .

(8)

By comparing Equations (7) and (8), one can easily see that conv(X) ⊆ THV (X) for any subspace V of F(X,R).

Theorem B asserts that if V is a G-invariant subspace, then the psd lift (6)-(7) is G-equivariant. The Lasserre/theta-body hierarchy of conv(X) can now be deﬁned as follows:

- Deﬁnition 5 (Lasserre/theta-body hierarchy). Let X be a ﬁnite subset of Rn and let F(X,R) be the space of functions on X. The k’th level of the Lasserre/theta-body hierarchy of X is the set THV (X) where V = Pol≤k(X) is the space of polynomials of degree at most k on X. This set will be denoted THk(X) for simplicity.


In light of this deﬁnition note that the theta-rank of X is the smallest k such that the equality conv(X) = THk(X) holds.

- Remark 2. In [GPT10], the theta-body hierarchy and the theta-rank are deﬁned for an ideal I of R[x]. Our deﬁnition for the theta-rank of X ⊂ Rn corresponds to the theta-rank of the vanishing ideal of X.


#### 1.3 Contributions

##### 1.3.1 Summary

In this paper we present a representation-theoretic framework to study equivariant psd lifts of a general class of symmetric polytopes known as orbitopes [SSS11].

- • Our ﬁrst contribution is a structure theorem which can be regarded as a converse to Theorem B: namely we show that any equivariant psd lift of size d of an orbitope must have the form given in Theorem B where the dimension of V is bounded by d3. Furthermore, the bound d3 can be improved when the symmetry group has some speciﬁc structure. One consequence of the structure theorem is that in order to study equivariant psd lifts, one has to understand the structure of low-dimensional invariant subspaces in F(X,R). In particular if one can show that low-dimensional invariant subspaces are composed only of low-degree polynomials, then any lower bound on the Lasserre/theta-body hierarchy would automatically translate to a lower bound on equivariant psd lifts.
- • We apply the theorem to two well-known examples where such a phenomenon occurs, namely the parity polytope and the cut polytope. In both cases we show that low-dimensional invariant subspaces of F(X,R) correspond (essentially) to low-degree polynomials. Thus using the structure theorem, this shows that if we have a small equivariant psd lift, then the sum-of-squares hierarchy is exact after a small number of steps. For the parity polytope we prove a lower bound of n/4 on the sum-of-squares hierarchy which implies an exponential lower bound on the size of any equivariant psd lift of the parity polytope. Similarly for the cut polytope using the well-known lower bound of Laurent of n/2 [Lau03] our results yield an exponential lower bound on the size of any equivariant psd lift of the cut polytope.


##### 1.3.2 Statement of results

In this brief section we give a more precise statement of our results. The family of polytopes that we focus on in this paper are known as orbitopes [BV88, BB05, SSS11]: Let G be a ﬁnite subgroup of GL(Rn), the group of n × n real invertible matrices. Given x0 ∈ Rn, let X = G · x0 := {g · x0 : g ∈ G} be the orbit of x0 under G, and consider the polytope P deﬁned as the convex hull of X:

P = conv(X) = conv(G · x0). (9) Such a polytope is called an orbitope [SSS11].

Orbitopes are symmetric by construction; for example they are clearly invariant under the action of G. In this paper we are interested in psd lifts of orbitopes that respect their symmetry. We prove that any equivariant psd lift of size d of an orbitope P is essentially a sum-of-squares lift where the functions in the sum-of-squares decomposition come from a certain G-invariant subspace of dimension at most d3. More precisely we prove the following theorem:

Theorem 1. Let P be a G-orbitope as in (9). Assume P has a G-equivariant psd lift of size d. Then there exists a G-invariant subspace V of F(X,R) such that:

- (i) For any linear form on Rn, max − is V -sos on X, where max := max x∈X

(x).

- (ii) dimV ≤ d3.


The theorem above establishes a connection between small G-equivariant psd lifts and low-dimensional G-invariant subspaces of F(X,R). Thus to obtain lower bounds on the sizes of equivariant psd lifts one has to study the structure of such subspaces of F(X,R). In particular, if one can show that such subspaces correspond to low-degree polynomials, then any lower bound on the sum-of-squares hierarchy will yield a lower bound on G-equivariant psd lifts.

In the case where the group G has a certain product structure, one can strengthen the conclusion of

- Theorem 1 with a better bound on the dimension of V (we refer the reader to Section 3.3 for the precise statement). Using these structure theorems we study certain well-known orbitopes and we prove lowerbounds on the size of equivariant psd lifts.

Parity polytope The ﬁrst example we study is the so-called parity polytope, denoted PARn, and which is deﬁned as the convex hull of all points x ∈ {−1,1}n that have an even number of −1’s:

PARn = conv x ∈ {−1,1}n :

n

i=1

xi = 1 .

It is easy to see that PARn is an orbitope. The symmetry group of PARn consists of coordinate permutations

- as well as transformations that switch the sign of an even number of coordinates. Let Gparity be the subgroup of GL(Rn) generated by these transformations. We show that low-dimensional Gparity-invariant subspaces of F(X,R) consist of low-degree polynomials (where X denotes the vertices of the parity polytope). We also


show that the sum-of-squares hierarchy for PARn requires at least n/4 levels to be exact. Thus, using the structure theorem, this allows us to obtain the following exponential lower bound on the size of any Gparity-equivariant psd lift of the parity polytope:

- Theorem 2. Any Gparity-equivariant psd lift of PARn for n ≥ 8 must have size ≥ n/ n4 .

Note that in the theorem above, equivariance is with respect to the full symmetry group Gparity consisting of coordinate permutations and even sign switches. As we see in Section 4 there are well-known polynomial-

size LP lifts of PARn, however they are not equivariant with respect to the full symmetry group. Cut polytope Using the framework described above we also study the cut polytope deﬁned as:

CUTn = conv xxT : x ∈ {−1,1}n ⊂ Sn.

Let Gcube ⊂ GL(Rn) be the symmetry group of the hypercube [−1,1]n which consists of signed permutation matrices, i.e., permutation matrices where nonzero entries are either +1 or −1 (the group Gcube is also known as the hyperoctahedral group). The cut polytope is invariant under the action of Gcube which acts on the space of n × n symmetric matrices by congruence transformations. By studying low-dimensional invariant subspaces of functions on the vertices of the hypercube {−1,1}n and using the lower bound of Laurent [Lau03] on the sum-of-squares hierarchy for the cut polytope, we prove the following exponential lower bound on the size of any equivariant psd lift of CUTn:

- Theorem 3. Any Gcube-equivariant psd lift of CUTn must have size ≥ n/ n4 .


Note that Theorems 2 and 3 above are stated in terms of exact psd lifts of the parity polytope and cut polytope. Our framework also allows us to consider approximate lifts. For example, for the parity polytope and the cut polytope, we show that the approximation quality of any approximate equivariant psd lift of small size can be achieved with a small number of rounds of the sum-of-squares hierarchy. We refer to Sections 4 and 5 for the precise statements of these results.

Related work In independent work, Lee et al. [LRST14] have also considered symmetric psd lifts for the maximum cut problem (and more generally constraint satisfaction problems) and proved that such lifts cannot be much stronger than the sum-of-squares hierarchy. In their work however they adopted a deﬁnition of symmetric psd lift that is diﬀerent from the one we consider here: in [LRST14], a psd lift of the cut polytope CUTn = π(Sd+ ∩ L) is called symmetric if for any permutation σ of {1,...,n} there exists a d × d permutation matrix ρ(σ) such that π(ρ(σ)Y ρ(σ)T) = σ · π(Y ) for all Y ∈ Sd+ ∩ L (where σ · π(Y ) denotes the natural action of Sn on Sn which permutes rows/columns). Note that this deﬁnition is more restrictive than ours since it requires ρ(σ) to be a permutation matrix whereas in our Deﬁnition 2, we allow ρ(σ) to be any invertible matrix in GL(Rd). In this regard our framework is more general and applies to a wider class of psd lifts.

Our framework also allows us to study equivariant lifts with respect to arbitrary groups and not only permutation symmetry. Note for example that in Theorem 3 we consider lifts of the cut polytope that are equivariant with respect to Gcube which is larger than Sn. For this reason the lower bound as stated in

- Theorem 3 cannot be directly compared with the lower bound in [LRST14]. By modifying Lemma 3 however


one could actually prove a result similar to Theorem 3 where the group Gcube is replaced with Sn: the lower bound we get is slightly worse but is still exponential in n.

Finally, note that in a very recent breakthrough paper [LRS14] it was shown that any psd lift of the cut polytope must have exponential size (with no equivariance assumption). In fact the authors of [LRS14] propose a new technique to obtain lower bounds on the psd rank [FGP+14] which they apply to get exponential lower bounds for the cut polytope, the traveling salesman polytope, as well as the stable set polytope.

Organization of the paper The paper is organized as follows. In Section 2 we review some background material in representation theory which are used later in the paper. In Section 3 we describe the general setting of the paper and we prove the structure theorem (Theorem 1) and we also consider the special case of symmetry groups with a product structure. In Section 4 we study the parity polytope. We ﬁrst prove a lower bound of n/4 on the sum-of-squares hierarchy of the parity polytope. We then prove a key lemma showing that in F(X,R) (where X is the set of vertices of the parity polytope), any low-dimensional invariant subspace can be realized by low-degree polynomials. This allows us to obtain an exponential lower bound on the size of any equivariant psd lift of the parity polytope. Finally in Section 5 we consider the cut polytope. Just as for the parity polytope we study low-dimensional invariant subspaces of F({−1,1}n,R) and we show that they (essentially) consist of low-degree polynomials. This lemma combined with the structure theorem and the lower bound of Laurent [Lau03] yields an exponential lower bound on the size of any equivariant psd lift of the cut polytope.

Notations We collect here some of the notations that are used throughout the paper. We denote by Sn the space of n × n real symmetric matrices and by Sn+ the cone of positive semideﬁnite matrices. The group of n × n real invertible matrices is denoted by GL(Rn). The group of n × n orthogonal matrices is denoted O(Rn). Also if V is a vector space we let V ∗ be the dual space of V which consists of linear forms on V . For a set X we let F(X,R) be the space of real-valued functions on X. The symmetric group on n elements is denoted by Sn. For a matrix A with real entries we denote by A F the Frobenius norm of A deﬁned by

A F = trace(ATA) = ( i,j A2ij)1/2.

### 2 Background in representation theory

In this section we recall some basic facts concerning representation theory of ﬁnite groups which will be used later in the paper. We refer to [Ser77] for a reference. Given a ﬁnite group G, a real ﬁnite-dimensional representation of G is a pair (V,ρ) where V is a real ﬁnite-dimensional vector space and ρ : G → GL(V ) is a group homomorphism. Two representations (V1,ρ1) and (V2,ρ2) are called G-isomorphic if there is an isomorphism f : V1 → V2 such that f(ρ1(g)x) = ρ2(g)f(x) for all x ∈ V1 and g ∈ G. A subspace W of V is an invariant subspace for the representation ρ if for any x ∈ W and g ∈ G we have ρ(g)x ∈ W. The representation (V,ρ) of G is called irreducible if it does not contain any invariant subspace except {0} and

- V itself. Irreducible representations of a group G are the building blocks of any representation of G. The following result is a standard fact in representation theory: any ﬁnite-dimensional real representation (V,ρ)


of G can be decomposed as

V = V1 ⊕ ··· ⊕ Vk (10) where each Vi is isomorphic to a direct sum of mi copies of an irreducible representation Wi of G. This decomposition (10) is a canonical decomposition and is called the isotypic decomposition of V . It satisﬁes the following important property: if W is an irreducible subspace of V that is G-isomorphic to Wi then W is contained in Vi. The subspace Vi is called the isotypic component of the irreducible representation Wi in

- V . This decomposition result can be used to prove the following proposition which will be needed later:

- Proposition 1. Let (V,ρ) be a real ﬁnite-dimensional representation of a ﬁnite group G and assume V = W1 ⊕ ··· ⊕ Wh

is a decomposition of V into irreducibles, i.e., each Wi is an irreducible subspace of V . Assume furthermore that the Wi are sorted in nondecreasing order of dimension, i.e., dimW1 ≤ dimW2 ≤ ··· ≤ dimWh. Assume W is an invariant subspace of V with dimW < dimWi

0

for some i0 ∈ {1,...,h}. Then necessarily W is contained in the direct sum W1 ⊕ ··· ⊕ Wi

0−1.

Proof. Any irreducible subrepresentation of W is isomorphic to one of the Wi for some i < i0. Thus W is contained in the direct sum of isotypic components of the Wi’s for i < i0, thus W is contained in

i0−1 i=1 Wi.

| |
|---|


The following well-known proposition will be also be useful later.

- Proposition 2. Let ρ : G → GL(Rn) be a real ﬁnite-dimensional representation of a ﬁnite group G. Then there exists an invertible matrix Q such that Qρ(g)Q−1 is orthogonal for all g ∈ G.

Proof. With the choice Q = ( g∈G ρ(g)ρ(g)T)−1/2, one can easily verify that Qρ(g)Q−1 is orthogonal for all g ∈ G.

| |
|---|


- 3 The structure theorem




In this section we state and prove our main structure theorems. We ﬁrst recall an important result from [GPT13] which charaterizes positive semideﬁnite lifts in terms of certiﬁcates of nonnegativity for linear inequalities. Using this characterization, we prove our general structure theorem, Theorem 1. Then we look

- at an important special case where the symmetry group has a certain product structure and where the result can be strengthened. This special case will be useful in subsequent sections when we look at the parity polytope and the cut polytope. We conclude the section with an illustration of the structure theorem on the polytope P = [−1,1]2.


#### 3.1 The factorization theorem

An important tool that allows us to study equivariant psd lifts is a certain factorization theorem. In [Yan91], Yannakakis showed that LP lifts of a polytope P can be characterized by nonnegative factorizations of the so-called slack matrix of P. For symmetric lifts over general cones, a similar factorization theorem exists and was proved by Gouveia et al. in [GPT13]. The following result, which we will use later in the proof of our main theorem, can be proved using arguments identical to the proof of Theorem 2 in [GPT13]. We include a proof in Appendix B for completeness.

- Theorem 4. Let G be a ﬁnite group acting on Rn and let X = G · x0 where x0 ∈ Rn. Assume conv(X) = π(Sd+ ∩ L) is a G-equivariant psd lift of conv(X) of size d, i.e., there is a homomorphism ρ : G → GL(Rd)


such that conditions (i) and (ii) of Deﬁnition 2 hold. Then there exists a map A : X → Sd+ with the following properties:

- (i) For any linear form on Rn there exists B( ) ∈ Sd+ such that if we let max := maxx∈X (x) we have: max − (x) = A(x),B( ) ∀x ∈ X.


- (ii) The map A satisﬁes the following equivariance relation: A(g · x) = ρ(g)A(x)ρ(g)T ∀x ∈ X, ∀g ∈ G.


In particular if H denotes the stabilizer of x0, then we have: A(x0) = ρ(h)A(x0)ρ(h)T ∀h ∈ H. (11) Furthermore, the representation ρ : G → GL(Rd) can be taken to be orthogonal, i.e., ρ(g) ∈ O(Rd) for all

- g ∈ G. Proof. See Appendix B for a proof.


| |
|---|


#### 3.2 Structure theorem for general orbitopes

We are now ready to state and prove our main structure theorem for orbitopes (Theorem 1) which we restate here for convenience.

Theorem 1. Let G be a ﬁnite group acting on Rn and let X = G · x0 where x0 ∈ Rn. Assume conv(X) has a G-equivariant psd lift of size d. Then there exists a G-invariant subspace V of F(X,R) such that:

- (i) For any linear form on Rn, max − is V -sos on X, where max := max x∈X

(x).

- (ii) dimV ≤ d3.


Proof. Assume we have a G-equivariant psd lift of size d of conv(X). By the factorization theorem (Theorem 4), we know that there exist maps A : X → Sd+ and B : (Rn)∗ → Sd+ such that for any linear form ∈ (Rn)∗ we have:

max − (x) = A(x),B( ) ∀x ∈ X (12)

where max := maxx∈X (x). Furthermore, since the lift is G-equivariant, the map A satisﬁes the equivariance relation

A(g · x) = ρ(g)A(x)ρ(g)T ∀x ∈ X ∀g ∈ G (13) where ρ : G → O(Rd) is a group homomorphism.

Let H be the stabilizer of x0, i.e., H = {g ∈ G : g · x0 = x0}. Note that the set X can be identiﬁed with G/H, the set of left cosets of H. Furthermore the left action of G on X is isomorphic to the left action of G on G/H. For simplicity of notation, we will thus think of functions on X as functions on G/H, or equivalently, as functions on G that are constant on the left cosets of H. For example since the point x0 is identiﬁed with the left coset 1GH of H, we will write A(1G) instead of A(x0).

We ﬁrst show how to construct the subspace V of F(X,R) ∼= F(G/H,R) and then we prove that it satisﬁes the properties of the statement.

• Deﬁnition of V : Let

r

A(1G) =

λiPW

i

i=1

is an orthogonal projection on the eigenspace Wi. Observe that from Equation (11) we have A(1G) = ρ(h)A(1G)ρ(h)T for all h ∈ H. Since ρ(h) is orthogonal, this means that A(1G) commutes with ρ(h), and so ρ(h)Wi = Wi for each eigenspace Wi of A(1G), which also implies that ρ(h)PW

be an eigendecomposition of A(1G), where each PW

i

ρ(g)T are constant on the left cosets of H, thus we can think of them as functions on G/H. Let V be the subspace of F(G/H,R) spanned by the matrix entries of x ∈ G/H  → ρ(x)PW

ρ(h)T = PW

. An important consequence of this is that the functions g  → ρ(g)PW

i

i

i

ρ(x)T, namely

i

ρ(x)T)k,l, i = 1,...,r and k,l = 1,...,d . (14)

V = span x ∈ G/H  → (ρ(x)PW

i

• It is clear that V is G-invariant (since ρ is a homomorphism) and that dimV ≤ d3. It thus remains to

show that max − is V -sos for any ∈ (Rn)∗. We know from (12) that there exists B = B( ) ∈ Sd+ such that max − (x) = A(x),B for any x ∈ X. Now for any x ∈ G/H we have:

r

A(x),B = ρ(x)A(1G)ρ(x)T,B =

ρ(x)T,B . (15)

λi ρ(x)PW

i

i=1

Note that even though ρ(x) is not well-deﬁned when x ∈ G/H, the quantities ρ(x)A(1G)ρ(x)T and ρ(x)PW

ρ(x)T are well-deﬁned and do not depend on the representative of the coset x ∈ G/H (cf. previous remarks). Observe that since PW

i

ρ(x)T)2 = ρ(x)PW

is an orthogonal projection and ρ(x) is orthogonal, we have (ρ(x)PW

i

i

ρ(x)T. Thus continuing from Equation (15) we can write:

i

A(x),B =

r

ρ(x)T)2,B =

λi (ρ(x)PW

i

i=1

r

λi LTρ(x)PW

ρ(x)T 2F

i

i=1

where L is such that B = LTL. Since each entry function of x ∈ G/H  → LTρ(x)PW

ρ(x)T lives in V , this shows that A(x),B is a sum-of-squares of functions in V , which is what we wanted.

i

| |
|---|


#### 3.3 Special case: regular orbitopes

In this section we look at a special case where the symmetry group G has a certain product structure. In this case we show that one can improve Theorem 1 and obtain a better bound on the dimension of the subspace V .

We saw in the proof of Theorem 1 that the stabilizer H of x0 plays an important role. In this section we consider the situation where the group G has a semidirect product structure

G = N H (16)

where N is a normal subgroup of G and H is the stabilizer of x0. Concretely, (16) simply means that any element g ∈ G can be written in a unique way as g = nh where n ∈ N and h ∈ H. The following example illustrates this situation.

Example 3 (The hypercube). Let G ⊂ GL(Rn) be the group of signed permutations, i.e., the group of permutation matrices where nonzero entries are either +1 or −1. Let x0 = (1,...,1), and note that G · x0 = {−1,1}n. The stabilizer of x0 is Sn, the group of permutation matrices (with positive signs everywhere). Observe that G has the following semidirect product structure: G = N Sn where N is the subgroup of diagonal matrices with +1 or −1 on the diagonal. ♦

Let X = G·x0. If (16) holds and H is the stabilizer of x0, then it is easy to see that we have G·x0 = N·x0, i.e., X is an N-orbitope: indeed if x = g · x0 for some g ∈ G, then since we can write g = nh where n ∈ N and h ∈ H we have g · x0 = nh · x0 = n · x0 since h · x0 = x0. Furthermore, one can show that for any x ∈ N · x0, there is a unique n ∈ N such that n · x0 = x (indeed, if n,n ∈ N are such that n · x0 = n · x0, then n −1n stabilizes x0 and so by the semidirect product property we must have n −1n = 1G). In this case we say that X is an N-regular orbitope, since the action of N on X is regular.

We now state and prove our structure theorem in this particular case.

- Theorem 5. Let G be a ﬁnite group acting on Rn and let X = G·x0 where x0 ∈ Rn. Let H be the stabilizer of x0 and assume that G has the form G = N H where N is a normal subgroup of G. Assume P has a G-equivariant psd lift of size d. Then there exists a G-invariant subspace V of F(X,R) with the following properties:


- (i) For any linear form on Rn, max − is V -sos on X, where max := max x∈X


(x).

- (ii) dimV ≤ αN(d) · d where αN(d) is the largest dimension of any real irreducible representation of N of dimension ≤ d (in particular dimV ≤ d2).


Proof. Assume we have a G-equivariant psd lift of size d of conv(X). By the factorization theorem (Theorem 4), we know that there exist maps A : X → Sd+ and B : (Rn)∗ → Sd+ such that for any linear form ∈ (Rn)∗ we have:

max − (x) = A(x),B( ) ∀x ∈ X (17)

where max := maxx∈X (x). Furthermore, since the lift is G-equivariant, the map A satisﬁes the equivariance relation

A(g · x) = ρ(g)A(x)ρ(g)T ∀x ∈ X ∀g ∈ G (18)

where ρ : G → GL(Rd) is a group homomorphism (in fact we can choose ρ to take values in O(Rd) however we will not need this in this proof).

Note that since G has the product structure G = N H we can identify X with N, and the left action of G on X is isomorphic to the left action of G on N deﬁned by g · x = nhxh−1 ∈ N, where g = nh ∈ G and x ∈ N. Thus in the rest of the proof we will think of functions on X as functions on N. For example since the point x0 is identiﬁed with 1N, we will write A(1N) instead of A(x0).

We now deﬁne the subspace V of F(X,R) ∼= F(N,R) and then we show it has the required properties.

- • Deﬁnition of V : Let V be the subspace of F(N,R) spanned by the matrix entry functions of ρ|N, i.e.,

V = span x ∈ N  → ρ(x)ij,i,j = 1,...,d .

- • We need to show that V is a G-invariant subspace and that Properties (i) and (ii) in the statement of


the theorem are satisﬁed.

∗ To see why V is G-invariant, note that for any x ∈ N and g = nh ∈ G we have ρ(g ·x) = ρ(nhxh−1) = ρ(nh)ρ(x)ρ(h−1) thus for any i,j the function x  → ρ(g · x)ij is a linear combination of the functions x  → ρ(x)k,l. This shows that V is G-invariant.

∗ To prove that dimV ≤ αN(d) · d, observe that if n1,...,nk are the dimensions of the irreducible components of the representation ρ|N : N → GL(Rd) of N, then the matrices ρ(x) (x ∈ N) are all, up to a global change of basis, block-diagonal with blocks of size n1,...,nk. Thus we have dimV ≤

i n2i ≤ i niαN(d) = αN(d) · d since each ni ≤ αN(d) and i ni = d. ∗ Finally, it remains to prove Property (i). Let ∈ (Rn)∗ and let B = B( ) ∈ Sd+ such that (17) is true. Note that for any x ∈ N we have: A(x),B = ρ(x)A(1N)ρ(x)T,B = trace(ρ(x)A(1N)ρ(x)TB). (19)

Since A(1N) and B are positive semideﬁnite matrices, we can write A(1N) = LALTA and B = LBLTB for some matrices LA and LB. Then we have:

A(x),B = trace(ρ(x)LALTAρ(x)TLBLTB) = LTBρ(x)LA 2F.

Since each entry function of x  → LTBρ(x)LA lives in V , it follows that x  → A(x),B has a sum-ofsquares representation with functions from V . This completes the proof.

| |
|---|


- Remark 3. Observe that the theorem above could be stated more generally without using the language of lifts. Assume p(x) is a function that is nonnegative on X and has an equivariant certiﬁcate of nonnegativity of the form


p(x) = A(x),B ∀x ∈ X where B ∈ Sd+ and A : X → Sd+ satisﬁes the equivariance relation:

A(g · x) = ρ(g)A(x)ρ(g)T ∀x ∈ X, ∀g ∈ G.

Then the arguments in the proofs above show that p(x) must be a sum of squares of functions from a Ginvariant subspace V of F(X,R) whose dimension is bounded by a certain function of d (d3 in the setting of

- Theorem 1 and αN(d)d in the setting of Theorem 5). In the theorems above, the function p(x) corresponds to the facet-deﬁning linear function p(x) = max − (x) but the proofs did not use this speciﬁc form of the function p(x). ♦


#### 3.4 Example: the square [−1,1]2

Before concluding this section we illustrate Theorem 1 by considering the example of the square P = [−1,1]2. As we saw in Example 3 the square [−1,1]2 is a N-regular orbitope where the group N is the group of 2 × 2 diagonal matrices with +1 or −1 on the diagonal and where x0 = (1,1) ∈ R2. The full symmetry group of the square [−1,1]2 is the dihedral group of order 8, which we will denote by G here. Note that G has a semidirect product structure G = N S2 where S2 is the group of 2 × 2 permutation matrices and corresponds to the stabilizer of x0.

In Example 1 in the introduction we gave a construction of a G-equivariant psd lift of P of size 3. We can apply Theorem 5 to this lift: Theorem 5 says that there must exist a G-invariant subspace V of F({−1,1}2,R) with the following properties:

- (i) Any facet inequality (x) ≤ max of P has a sum-of-squares certiﬁcate with functions from V :

max − (x) =

j

fj(x)2 ∀x ∈ {−1,1}2

where fj ∈ V .

- (ii) dimV ≤ 1 · 3 = 3 (indeed αN(3) = 1 since N is isomorphic to Z22 for which all the real irreducible representations have dimension one).


It is actually not diﬃcult to construct this subspace V explicitly. Indeed, let V be the subspace spanned by the following three functions:

(x1,x2) ∈ {−1,1}2  → 1, (x1,x2) ∈ {−1,1}2  → x1, (x1,x2) ∈ {−1,1}2  → x2.

Clearly dimV ≤ 3, and it is easy to see that this subspace is G-invariant. To check that point (i) above is true consider for example the facet inequality 1−x1 ≥ 0 of P. Then we can verify that for any x ∈ {−1,1}2 we have:

1 − x1 = f(x)2

with f(x) = (1 − x1)/√2 (note that f ∈ V ). The same is also true for the other facet inequalities. Thus the subspace V we just constructed satisﬁes points (i) and (ii).

Now one may wonder if there exists an equivariant psd lift of the square P = [−1,1]2 of size 2. Using

- Theorem 5 this would mean that there exists a G-invariant subspace V of F({−1,1}2) of dimension ≤ 2 which allows us to certify the four facet inequalities of P using sum-of-squares. Later in the paper we will study in more detail the space of functions on the hypercube {−1,1}n and their invariant subspaces, cf. Lemma 3. Using this lemma one can actually show that such a subspace V of dimension ≤ 2 cannot exist, ruling out the existence of G-equivariant psd lifts of size 2 of the square [−1,1]2.


- Remark 4. Actually it is known that there does not exist any psd lift (even a nonequivariant one) of the square [−1,1]2 of size 2. Indeed it was shown in [GRT13] that any psd lift of a full-dimensional polytope P in Rn must have size at least n + 1. ♦


### 4 The parity polytope

In this section we consider the case of the parity polytope and we prove exponential lower bounds on equivariant psd lifts using the results from the previous section.

- 4.1 Deﬁnitions Deﬁne EVENn to be the set of points x ∈ {−1,1}n that have an even number of −1’s, i.e.:


n

EVENn = x ∈ {−1,1}n :

xi = 1 . (20)

i=1

The convex hull of EVENn is called the parity polytope and is denoted PARn: PARn = conv(EVENn).

Symmetry group Note that the parity polytope is the orbitope conv(Nparity · x0) where x0 = 1 ∈ Rn is the vector of all-ones and Nparity ⊂ GL(Rn) is the subgroup of GL(Rn) consisting of diagonal matrices with +1 or −1 on the diagonal and with an even number of −1’s, i.e.:

Nparity = {diag(x) : x ∈ EVENn}.

The parity polytope is invariant under the action of Nparity, i.e., it is invariant under switching an even number of signs. In addition to Nparity-invariance, the parity polytope is also invariant under permutation of coordinates. Let Gparity be the group that consists of evenly-signed permutation matrices, i.e., signed permutation matrices with an even number of −1’s; then one can check that PARn is invariant under the action of Gparity. Note that the group Gparity consists of all possible products of the form  h where ∈ Nparity and h ∈ Sn:

Gparity := { h : ∈ Nparity,h ∈ Sn} = Nparity Sn.

The group Gparity has the product structure described in Section 3.3. In fact we have Gparity = Nparity Sn and Sn corresponds to the stabilizer of x0 = 1 ∈ Rn.

Facet description of the parity polytope When n > 2, the parity polytope is a full-dimensional polytope in Rn. It has the following description using linear inequalities:

PARn = x ∈ Rn : −1 ≤ x ≤ 1,

xi −

xi ≤ n − 2 ∀A ⊆ [n],|A| odd . (21)

i∈Ac

i∈A

If n ≥ 4 each of the 2n + 2n−1 inequalities are facet-deﬁning. If n = 3 the inequalities −1 ≤ x ≤ 1 are redundant giving the simpler description with 4 facets

PAR3 = {x ∈ Rn : x1 + x2 − x3 ≤ 1

x1 − x2 + x3 ≤ 1 −x1 + x2 + x3 ≤ 1 −x1 − x2 − x3 ≤ 1}.

(22)

Nonequivariant polynomial-size lifts of the parity polytope Polynomial-size lifts of the parity polytope have been known since the original paper of Yannakakis [Yan91]. In fact there are two known LP lifts of the parity polytope of size respectively O(n2) and O(n). The two lifts respect some of the symmetry of the parity polytope however none of them is equivariant with respect to the full symmetry group Gparity = Nparity Sn.

- • The lift of size O(n2) given by Yannakakis [Yan91] relies on the observation that


PARn = conv

Sk

k even

where Sk are the “slices” of the hypercube deﬁned by the equation 1T x = n − 2k: Sk = conv{x ∈ {−1,1}n : x has exactly k components equal to −1}

= {x ∈ [−1,1]n : 1T x = n − 2k}.

Since each Sk has a simple description using only O(n) linear inequalities, this can be used to construct a lift of PARn of size O(n2). One can easily verify that this lift is equivariant with respect to permutation of the coordinates. One can show however that this lift is not equivariant with respect to switching an even number of signs. Intuitively, the reason behind this is that the operation of switching signs does not preserve the slices Sk.

- • There is a smaller yet less well known LP lift of the parity polytope due to [CK04, Section 2.6.3] (see also [KP11]) which has size O(n). This lift is equivariant with respect to switching an even number of signs, however it is not equivariant with respect to the permutation action. The key observation behind this LP lift is that (x1,x2,...,xn) ∈ EVENn if and only if there exists z ∈ {−1,1} such that (x1,x2,z) ∈ EVEN3 and (z,x3,...,xn) ∈ EVENn−1 (simply take z = x1x2). In fact one can establish an analog of this statement for the parity polytope:


PARn = {x ∈ Rn : ∃z s.t. (x1,x2,z) ∈ PAR3 and (z,x3,...,xn) ∈ PARn−1}.

Repeatedly applying (23) shows that

(23)

PARn = x ∈ Rn : ∃z2,z3,...,zn−2 s.t. (x1,x2,z2) ∈ PAR3, (zn−2,xn−1,xn) ∈ PAR3, and (zi,xi+1,zi+1) ∈ PAR3 for i ∈ {2,3,...,n − 3} .

This description shows that PARn is the projection of a polytope with 4(n − 2) facets. It is not too hard to show that this lift is actually equivariant with respect to switching an even number of signs. However one can see that this lift is not equivariant with respect to permutations since we have broken permutation symmetry by imposing a particular ordering on the variables.

#### 4.2 Functions on EVENn

Let n ≥ 1. If I ⊆ [n] deﬁne the monomial map Rn x  → xI := i∈I xi. We can regard these as functions on EVENn by simply restricting their domain. When we do so, we write them as eI : EVENn → R deﬁned by eI(x) = xI. We now describe a basis for F(EVENn,R) in terms of these functions.

##### Proposition 3. Let n ≥ 1.

- • If n is odd, then the functions eI for |I| < n/2 form a basis of F(EVENn,R).
- • If n is even, then the functions eI with |I| < n/2 together with the functions (eI + eIc)/2 for |I| = n/2 constitute a basis of F(EVENn,R).


Proof. Given a ∈ EVENn, let 1a ∈ F(EVENn,R) be the indicator function for a, i.e., 1a(x) = 1 if x = a and 1a(x) = 0 otherwise. Clearly the family of functions {1a}a∈EVENn

forms a basis of F(EVENn,R). Observe that 1a can be written as the following polynomial:

1a(x) =

- 1

- 2n


(1 + a1x1)...(1 + anxn) ∀x ∈ EVENn.

c

Furthermore, the following identities are true on EVENn: x2i = 1 and xI = xI

for any x ∈ EVENn. If we expand the polynomial expression for 1a above using the previous identities we see that, when n is odd, 1a is a linear combination of the square-free monomials xI for |I| < n/2. When n is even any monomial of the form xI where |I| = n/2 can be rewritten as (xI + xI

c

)/2. Thus this shows that the functions given in the statement of the proposition form a generating set for F(EVENn,R). Since the number of such functions is 2n−1 = dimF(EVENn,R), they form a basis of F(EVENn,R).

| |
|---|


Given 0 ≤ k < n/2, denote by Polk(EVENn) the subspace of F(EVENn,R) spanned by the eI with |I| = k. If k = n/2 let Polk(EVENn) be the subspace of F(EVENn,R) spanned by the (eI + eIc)/2 with |I| = n/2. So we have:

n k if k < n/2

dimPolk(EVENn) =

n

- 1

- 2


n/2 if k = n/2. The proposition above shows that the space F(EVENn,R) decomposes as:

F(EVENn,R) = Pol0(EVENn) ⊕ ··· ⊕ Pol n/2 (EVENn).

The next lemma expresses the pointwise product of the functions eI and eJ in terms of our basis for F(EVENn,R). (Here, and subsequently, if I,J ⊆ [n] then I J is the symmetric diﬀerence of I and J.)

- Lemma 1. If I,J ⊆ [n] then


 

eI J if |I J| < n/2 e(I J)c if |I J| > n/2 (eI J + e(I J)c)/2 if |I J| = n/2.

eIeJ =



Proof. For any x ∈ EVENn we have that x2i = 1 for all i ∈ [n] and i∈[n] xi = 1. Hence for any I,J ⊆ [n], xIxJ = xI J = x(I J)

c

c

= (xI J + x(I J)

)/2. The result then follows by recognizing that at least one of these can be written in terms of the given basis from Proposition 3.

| |
|---|


- 4.3 A lower bound on the theta-rank of the parity polytope For any 1 ≤ k ≤ n/2 denote by Pol≤k(EVENn) the subspace of F(EVENn,R) deﬁned by


Pol≤k(EVENn) = Pol0(EVENn) ⊕ ··· ⊕ Polk(EVENn).

Observe that the theta-rank (cf. Deﬁnition 4) of the parity polytope is the smallest k such that the following holds:

∀ ∈ (Rn)∗, max − is Pol≤k(EVENn)-sos on EVENn, where for a linear form ∈ (Rn)∗, we call max := maxx∈EVEN

(x).

n

Note that if |I|,|J| < n/4 then the product of eI(x) = xI and eJ(x) = xJ when thought of as functions on EVENn is the same as their product when thought of as functions on {−1,1}n. This is the basic reason why the following lower bound on the theta-rank of the parity polytope holds.

- Proposition 4. The theta-rank of the parity polytope PARn is at least n/4 .


Proof. We ﬁrst sketch the outline of the proof before ﬁlling in the details. We choose a function max − ∈ Pol≤1(EVENn) that is nonnegative on EVENn but when viewed as a polynomial on Rn takes a negative value on some point p ∈ {−1,1}n \ EVENn. (One can think of this as a facet inequality for PARn that is not valid for the hypercube.) We use this point p to construct a linear functional Lp ∈ F(EVENn,R)∗ (deﬁned to mimic evaulation of the function at p) such that Lp( max − ) < 0 and yet whenever k < n/4 and f ∈ Pol≤k(EVENn) we have that Lp(f2) ≥ 0. This would imply that if k < n/4 then Lp separates the linear function max − (that is nonnegative on EVENn) from the cone of functions that are Pol≤k(EVENn)-sos on EVENn, which would complete the proof.

We now ﬁll in the details. Let max − (x) = (n − 2)e∅(x) + e{n}(x) − i n=1−1 e{i}(x) and observe that this is a nonnegative function on EVENn (since it deﬁnes a facet of PARn). Let p = (1,1,...,1,−1) ∈ Rn, and note that p has an odd number of −1s. Deﬁne a linear functional Lp ∈ F(EVENn,R)∗ by deﬁning it on our basis for F(EVENn,R) by

Lp(eI) =

pi if |I| < n/2 and

i∈I

Lp((eI + eIc)/2) =

pi +

i∈I

pi /2 = 0 if |I| = n/2.

i∈Ic

Observe that Lp( max − ) = (n − 2) + Lp(e{n}) − ni=1−1 Lp(e{i}) = (n − 2) − 1 − (n − 1) = −2.

We now show that if k < n/4 and f ∈ Pol≤k(EVENn) then Lp(f2) ≥ 0. Observe that if |I J| < n/2 and |I|,|J| < n/2 then

Lp(eIeJ) = Lp(eI J) =

pi = i∈I pi j∈J pj = Lp(eI)Lp(eJ). (24)

i∈I J

If f ∈ Pol≤k(EVENn) where k < n/4 then there are constants cI ∈ R such that f = km=0 |I|=k cIeI. Hence by (24), and the observation that if |I|,|J| < n/4 then |I J| < n/2, we can see that any f ∈

Pol≤k(EVENn) satisﬁes

k

Lp(f2) =

cIcJLp(eIeJ)

m,m =0 |I|=m |J|=m

k

cIcJLp(eI) p(eJ) = Lp(f)2 ≥ 0.

=

m,m =0 |I|=m |J|=m

(25)

This completes the proof.

| |
|---|


- Remark 5. One can show that the lower bound of n/4 on the theta-rank of the parity polytope PARn is in fact tight, cf. Proposition 5 in [FSP14].


#### 4.4 Equivariant psd lifts of the parity polytope

In this section we study psd lifts of the parity polytope that are equivariant under the full symmetry group Gparity of evenly signed permutations. Given two integers n and k ≤ n/2 we deﬁne:

n k if n is odd

Dn,k :=

(26)

min nk , 21 n/ n2 if n is even.

We prove the following theorem:

- Theorem 6. Assume PARn has a Sd+-lift that is Gparity-equivariant of size d < Dn,k where k ≤ n/2. Then the (k − 1)’st theta-body relaxation is exact, i.e., THk−1(EVENn) = PARn.

Proof. Assume we have a Gparity-equivariant psd lift of PARn of size d. We can apply Theorem 5 with P = PARn and G = Gparity = Nparity Sn. Since Nparity ∼= Zn2−1, all the real irreducible representations of Nparity are one-dimensional. Thus Theorem 5 says that there exists a Gparity-invariant subspace V of F(EVENn,R) with dimV ≤ d such that for any linear form ∈ (Rn)∗ we have that

max − is V -sos on EVENn. (27)

In Lemma 2 (cf. below) we show that such an invariant subspace, when d < Dn,k, is composed entirely of polynomials of degree at most k − 1, i.e. V is a subspace of Pol≤k−1(EVENn). Thus this shows that THk−1(EVENn) = PARn.

| |
|---|


Note that, using Remark 3 from the previous section, one can actually state a more general theorem relating approximate equivariant psd lifts and the sum-of-squares hierarchy. Indeed one can prove the following:

- Theorem 7. Assume P ⊆ Rn is an outer-approximation of PARn (i.e., PARn ⊆ P) and assume P has a Gparity-equivariant psd lift of size d. If d < Dn,k for some k ≤ n/2 then necessarily


PARn ⊆ THk−1(EVENn) ⊆ P where THk−1(EVENn) is the (k − 1)’st Lasserre/theta-body relaxation for the parity polytope.

Proof. The proof is very similar to the proof of Theorem 6 above. Given a linear form ∈ (Rn)∗ let max and max be respectively the maximum of on PARn and P. Note that max ≤ max since PARn ⊆ P, and hence the linear function max − (x) is nonnegative on EVENn. Since P has a Gparity-equivariant psd lift of size d, and since EVENn ⊆ P one can show (using a simple generalization of Theorem 4) that we have an equivariant certiﬁcate of nonnegativity of max − on EVENn of the form:

max − (x) = A(x),B ∀x ∈ EVENn

where A satisﬁes the equivariance relation A(g · x) = ρ(g)A(x)ρ(g)T for all x ∈ EVENn, g ∈ Gparity. Thus by Remark 3, we know that max − (x) is a sum-of-squares of functions in a Gparity-invariant subspace V of dimension ≤ d. Thus using Lemma 2 below it holds that max − (x) is a sum-of-squares of functions of degree ≤ k − 1 on EVENn.

This is true for any facet-deﬁning linear form of P thus, by the deﬁnition of the theta-body relaxation (cf. Equation (7) with V = Pol≤k−1(EVENn)) we have THk−1(EVENn) ⊆ P.

| |
|---|


Exponential lower bounds Before stating Lemma 2 on invariant subspaces of F(EVENn,R) which is crucial for the proofs of the two theorems above, we show how by combining Theorem 6 and Proposition 4 we get an exponential lower bound for equivariant psd lifts of the parity polytope. This is Theorem 2 from the introduction which we restate for convenience.

- Theorem 2. Any Gparity-equivariant psd lift of PARn for n ≥ 8 must have size ≥ n/ n4 .


Proof. We apply Theorem 6 above with k = n/4 . By Proposition 4, we know that the theta body relaxation of order n/4 − 1 is not exact. Thus this means that any Gparity-equivariant psd lift of PARn must have size d ≥ Dn, n/4 . One can then easily check from the deﬁnition of Dn,k that when n ≥ 8 we have Dn, n/4 ≥ n/ n4 .

| |
|---|


Invariant subspaces of functions on EVENn To complete the proof of Theorems 6 and 7, it remains to show that low-dimensional invariant subspaces of F(EVENn,R) are necessarily composed of low-degree polynomials.

We are interested in subspaces of F(EVENn,R) that are Gparity-invariant. Recall that Gparity is the group of evenly signed permutations. Thus a subspace V of F(EVENn,R) is Gparity-invariant if for any f ∈ V , and any ∈ {−1,+1}n such that ni=1 i = 1, and any σ ∈ Sn the function:

x  → f( 1xσ(1),..., nxσ(n))

is also in V . Recall that an invariant subspace V is called irreducible if it does not contain any nontrivial invariant subspace, i.e., if W is an invariant subspace of V , then W = {0} or W = V .

It is clear that the subspaces Polk(EVENn) are Gparity-invariant. The next result shows that these subspaces are actually irreducible. Recall, for the statement to follow, that that the notation Dn,k is deﬁned in (26).

- Lemma 2. Under the action of Gparity, F(EVENn,R) decomposes into irreducible invariant subspaces as F(EVENn,R) = Pol0(EVENn) ⊕ ··· ⊕ Pol n/2 (EVENn).


Hence if V is a Gparity-invariant subspace of F(EVENn,R) with dim(V ) < Dn,k then V ⊆ Pol≤k−1(EVENn). Proof. It is easy to see that Polk(EVENn) is invariant for each k = 0,1,..., n/2 . It remains to show that each of these is irreducible. For any k = ∈ [n], let k,  ∈ Gparity be deﬁned by k,  = diag(1,...,−1,...,−1,...,1) where all the entries are equal to 1 except the entries in position k and which are equal to −1. Given an element p ∈ F(EVENn,R) we denote by (id+ k ) · p the polynomial p + k  · p. Observe that whenever I ⊂ [n], then

2xI if (k ∈ I and ∈ I) or (k ∈/ I and ∈ / I) 0 if either exactly one of k ∈ I and ∈ I occur.

(id+ k ) · xI = xI + k  · xI =

Now ﬁx some arbitrary k < n/2 (we deal with the case n = 2k separately) and let V be a (non-zero) invariant subspace of Polk(EVENn). Let p be a non-zero element of V . By the invariance of V under the permutation action, we can assume that the coeﬃcient of the monomial x1x2 ···xk in p is non-zero, and so p is of the form: p(x) = cx1 ···xk + |I|=k,I ={1,2,...,k} cIxI where c = 0. We will show that necessarily V = Polk(EVENn). We ﬁrst show that

n

(id+ k+1,i) · p(x) = 2n−k−1x1x2 ···xk. (28)

i=k+2

Once this is established we will know, by the Sn-invariance of V , that V is equal to Polk(EVENn). To establish (28), ﬁrst note that if i ∈ {k + 2,k + 3,...,n} then

(id+ k+1,i)(x1x2 ···xk) = 2x1x2 ···xk

because neither of xi and xk+1 appear in x1x2 ···xk. It remains to check that every other monomial of degree k is in the kernel of ni=k+2(id+ k+1,i) . Consider any other monomial xI, i.e. I ⊂ {1,2,...,n} with |I| = k and for which there is some ∈ I with ≥ k + 1. Consider two cases, ﬁrst the case where k + 1 ∈/ I. Then there is some ≥ k + 2 such that ∈ I. But then (id+ k+1, ) · xI = 0 and so since the i,j commute, ni=k+2(id+ k+1,i) · xI = 0. Now suppose k + 1 ∈ I. Then there is some ≥ k + 2 such that ∈ / I. This is because if there were no such then we must have I ⊇ {k + 1,k + 2,...,n} which cannot have cardinality k since we assumed k < n/2. It then follows that (id+ k+1, ) · xI = 0 and so that

n i=k+2(id+ k+1,i) · xI = 0. Finally consider the case when n = 2k. In this situation since V is invariant under the permutation

action we can assume p(x) = c(x1 ···xn/2 + xn/2+1 ···xn) +

c

cI(xI + xI

).

|I|=n/2,I ={1,2,...,n/2} I ={n/2,n/2+1,...,n}

Applying the same argument as above, we see that

n

(id+ k+1,i) · p(x) = 2n−n/2−1 x1x2 ···xn/2 + xn/2+1xn/2+2 ···xn .

i=k+2

Since the action of Sn on

x1x2 ···xn/2 + xn/2+1xn/2+2 ···xn generates a basis for Poln/2(EVENn) we can conclude that V = Poln/2(EVENn).

The second part of the theorem is a direct consequence of Proposition 1 on low-dimensional invariant subspaces. When n is odd note that dimPol0(EVENn) < dimPol1(EVENn) < ··· < dimPol n/2 (EVENn) with dimPolk(EVENn) = nk . Thus any invariant subspace V of F(EVENn,R) with dimV < dimPolk(EVENn) =

n k = Dn,k must be contained in Vk−1 = Pol0(EVENn) ⊕ ··· ⊕ Polk−1(EVENn) and thus consists of polynomials of degree at most k − 1. In the case where n is even we have dimPoln/2(EVENn) = 21 n/ n2 . Thus any invariant subspace V with dimV < min nk , 12 n/ n2 = Dn,k must be contained in Pol≤k−1(EVENn) = Pol0(EVENn) ⊕ ··· ⊕ Polk−1(EVENn).

| |
|---|


### 5 The cut polytope

#### 5.1 Deﬁnitions

The maximum cut problem on a graph G = (V,E) with V = {1,...,n} and weights wij for ij ∈ E is the problem of labeling each vertex i ∈ V with a label xi = +1 or xi = −1 in such a way that the total weight of edges connecting two vertices with a diﬀerent label is maximized. This problem can be written as follows:

maximize ij∈E wij(1 − xixj)/2 subject to x ∈ {−1,1}n.

(29)

Note that for a given labeling xi = ±1 of vertices, the quantity (1 − xixj)/2 is equal to 1 if i and j have diﬀerent labels, and 0 otherwise. The formulation (29) shows that the maximum cut problem is the problem of maximizing a quadratic form on the hypercube {−1,1}n. Using standard techniques, one can convert this problem into a linear program, by working in a lifted space. Indeed it is not hard to see that the problem (29) is equivalent to the problem below:

maximize ij∈E wij(1 − Xij)/2 subject to X = xxT for some x ∈ {−1,1}n.

(30)

Note that the objective is now linear in the variable X. Deﬁne the cut polytope CUTn as the convex hull of all outer products xxT for x ∈ {−1,1}n:

CUTn = conv xxT : x ∈ {−1,1}n . (31)

The formulation (30) shows that the maximum cut problem is a linear program over the cut polytope CUTn. Note that the cut polytope is a n(n−1)/2-dimensional polytope in the space Sn of n×n symmetric matrices.

#### 5.2 Sum-of-squares relaxations

In this section we review the sum-of-squares relaxations of the cut polytope as described for example in [Lau03]. The construction we describe here actually applies to general polytopes P of the form:

P = conv xxT : x ∈ X ⊂ Sn (32)

where X is a ﬁnite set in Rn. The construction of the relaxation is very similar to the one described in the introduction, Section 1.2, except that we work with quadratic forms instead of linear forms. Note that a polytope P of the form (32) can be seen as the set of second-order moments of probability distributions on X:

P = (E(eij))ij : E ∈ F(X,R)∗ where

(33)

E(f) =

f(x)dµ(x) for some prob. measure µ on X

X

where eij is the element of F(X,R) deﬁned by eij(x) = xixj. Given a subspace V of F(X,R) we can thus deﬁne the following relaxation of P in the same way we did in Section 1.2:

TH(2)V (X) := (E(eij))ij : E ∈ F(X,R)∗ where E(1) = 1, E(f2) ≥ 0 ∀f ∈ V . (34)

By comparing (33) and (34) it is clear that P ⊆ TH(2)V (X). One can show, like in Theorem A that the relaxation is tight TH(2)V (X) = P if for any quadratic form q on Rn, qmax − q is V -sos, where qmax = maxx∈X q(x).

When X = {−1,1}n, the convex body TH(2)V ({−1,1}n) is a relaxation of the cut polytope. When V = Pol≤k({−1,1}n) is the space of polynomials of degree at most k, we will denote the relaxation by Qk(CUTn):

Qk(CUTn) = TH(2)V ({−1,1}n) where V = Pol≤k({−1,1}n). (35)

The relaxation Qk(CUTn) is known as the “node-based” relaxation and is usually described in the literature in terms of explicit moment matrices, see e.g., [Lau04]. In fact if we use the basis of Pol≤k({−1,1}n) formed by square-free monomials of degree up to k, we get that Qk(CUTn) can be written as:

 

 

y∅ = 1 yij = zij, ∀i < j Mk(y) 0

z ∈ R(n

) : ∃(yI)|I|≤2k such that

Qk(CUTn) =

(36)

2





where (yI)|I|≤2k is a vector indexed by subsets I ⊆ [n] of cardinality ≤ 2k and where Mk(y) is the moment matrix associated to y deﬁned by:

Mk(y)I,J = yI J ∀I,J ⊆ [n], |I|,|J| ≤ k

where I J denotes symmetric diﬀerence. Laurent showed in [Lau03] that when k ≤ n/2 we have Qk(CUTn) = CUTn.

- Theorem 8 (Laurent, [Lau03]). For k ≤ n/2 , the inclusion CUTn ⊂ Qk(CUTn) is strict.

Laurent conjectured in [Lau03] that the relaxation is actually tight for k = n/2 . This conjecture was proved recently in [FSP15].

5.3 Equivariant psd lifts of the cut polytope

Symmetries of the hypercube and the cut polytope Let

Cn = {−1,1}n

be the vertices of the hypercube in Rn. In Example 3 we saw that conv(Cn) is the orbitope conv(Ncube · x0) where x0 = 1 ∈ Rn and Ncube := {diag( ) : ∈ {−1,+1}n}. The full symmetry group of the hypercube is:

Gcube = { h : ∈ Ncube,h ∈ Sn} = Ncube Sn

where Sn is the group of n×n permutation matrices. The group Gcube is known as the hyperoctahedral group and consists of signed permutation matrices, i.e., permutation matrices where each nonzero entry is either +1 or −1. Note that Gcube has the product structure described in Section 3.3, since Gcube = Ncube Sn and Sn is the stabilizer of x0 = 1 ∈ Rn.

The group Gcube acts on the space of n×n symmetric matrices by congruence transformations as follows: g · X := gXgT ∀g ∈ Gcube, ∀X ∈ Sn. (37)

It is easy to verify that CUTn is invariant under this action of Gcube. Furthermore the sum-of-squares relaxations Qk(CUTn) are also Gcube-invariant and using the same ideas as in Appendix A, one can show that the psd lifts (35)-(34) of Qk(CUTn) are Gcube-equivariant.

Equivariant psd lifts of CUTn In this section we are interested in psd lifts of CUTn that are Gcubeequivariant. Our main result is to show that any such equivariant lift must have exponential size. To do so we ﬁrst prove that any Gcube-equivariant lift of CUTn must essentially be a low-degree sum-of-squares lift like Qk(CUTn). Then using the lower bound of Laurent [Lau03], this implies an exponential lower bound on any Gcube-equivariant psd lift of CUTn.

- Theorem 9. Assume CUTn has a Gcube-equivariant Sd+-lift where d < nk for some k ≤ n/2. Then the (k − 1)’st sum-of-squares relaxation of CUT n/2 is exact, i.e., Qk−1(CUT n/2 ) = CUT n/2 .


Proof. Assume we have a Gcube-equivariant psd lift of CUTn of size d. Using arguments very similar to Theorem 5 (where linear forms are replaced by quadratic forms) we can show that there exists a Gcubeinvariant subspace V of F(Cn,R) with dimV ≤ d such that for any quadratic form q on n variables with qmax := maxx∈C

q(x) we have:

n

qmax − q(x) =

i

fi(x)2 ∀x ∈ Cn (38)

where each fi ∈ V . In Lemma 3 (cf. below) we show that such an invariant subspace of dimension d < nk , is composed entirely of polynomials of the form g(x) + en(x)h(x) where g and h are polynomials of degree at most k − 1 and en(x) = x1 ···xn is the n’th elementary symmetric polynomial.

We can use this to show that the (k − 1)’st sos relaxation of CUT n/2 is exact. Assume for simplicity that n is even, n = 2m (the argument for n odd is very similar). Let q be an arbitrary quadratic form on m

variables. We will show that qmax − q(x) is a sum-of-squares of polynomials of degree at most k on Cm (i.e., it is Pol≤k(Cm)-sos). Deﬁne qˆ a quadratic form in n = 2m variables by:

qˆ(x1,...,xn) = q(x1,...,xm). Note that the polynomial qˆdoes not depend on xm+1,...,xn and note also that maxx∈C

q(x), i.e., qˆmax = qmax. From Equation (38) we know that qˆmax − qˆ(x) admits a sum-of-squares decomposition where each sos term lives in the subspace V , i.e., we have:

###### qˆ(x) = maxx∈C

n

m

qˆmax − qˆ(x) =

j

(ˆgj(x) + en(x)hˆj(x))2 ∀x ∈ Cn (39)

where gˆj ∈ Pol≤k−1(Cn) and hˆj ∈ Pol≤k−1(Cn) and en(x) is the n’th elementary symmetric polynomial en(x) = x1 ···xn. If we plug xm+1 = x1,xm+2 = x2,...,x2m = xm in Equation (39) we get:

qmax − q(x) =

j

(gj(x) + hj(x))2 ∀x ∈ Cm (40)

where we used the fact that en(x1,...,xm,x1,...,xm) = 1 for all x ∈ Cm and where we let

gj(x1,...,xm) = gˆj(x1,...,xm,x1,...,xm) hj(x1,...,xm) = hˆj(x1,...,xm,x1,...,xm)

∀(x1,...,xm) ∈ Cm.

Since gj,hj ∈ Pol≤k−1(Cn) it is easy to see that gˆj,hˆj ∈ Pol≤k−1(Cm). Equation (40) thus shows that qmax − q is Pol≤k−1(Cm)-sos on Cm. Since q was an arbitrary quadratic form on m = n/2 variables, this shows that the (k − 1)’st level of the SOS hierarchy of CUTn/2 is exact.

| |
|---|


Like for the parity polytope one can also state a result relating approximate equivariant lifts of the cut polytope and the sum-of-squares hierarchy. To state the result it is convenient to introduce the notion of a (c,s)-approximation from the paper [CLRS13]. Given two real numbers c ≤ s we say that an outerapproximation P of CUTn achieves a (c,s)-approximation of CUTn if for any linear form L on Sn such that Lmax ≤ c it holds that Lmax ≤ s, where Lmax and Lmax are respectively the maximum of L on CUTn and P. We can now state the following theorem (we omit the proof since it is very similar to the arguments from the previous proofs):

- Theorem 10. Assume P is an outer-approximation of CUTn which achieves a (c,s)-approximation and


which admits a Gcube-equivariant psd lift of size d. If d < nk for some k ≤ n/2 then the (k − 1)’st sum-of-squares relaxation of CUT n/2 is a valid (c,s)-approximation of CUT n/2 .

Exponential lower bound If we combine Theorem 9 with Laurent’s n/2 lower bound on the sum-ofsquares hierarchy for the cut polytope we obtain the following exponential lower bound for Gcube-equivariant psd lifts of CUTn. This is Theorem 3 from the introduction which we restate here for convenience.

- Theorem 3. Any Gcube-equivariant psd lift of CUTn must have size ≥ n/ n4 .


Proof. Let m = n/2 . We apply Theorem 9 with k = m/2 +1. Laurent [Lau03] proved that Qk−1(CUTm) = CUTm and thus this means that any Gcube-equivariant psd of lift of CUTn must have size greater than or equal nk ≥ n/ n4 .

| |
|---|


A lemma on invariant subspaces of functions on the hypercube To complete the proof of Theorem 9, it remains to study low-dimensional invariant subspaces of F(Cn,R). It is known that any function f ∈ F(Cn,R) can be seen as a square-free polynomial of degree at most n. Let Polk(Cn) be the space of homogeneous square-free polynomials of degree k. Note that dimPolk(Cn) = nk and that:

F(Cn,R) = Pol0(Cn) ⊕ ··· ⊕ Poln(Cn).

We are interested in subspaces of F(Cn,R) that are Gcube-invariant. Recall that Gcube is the group of signed permutation matrices. Thus a subspace V of F(Cn,R) is Gcube-invariant if for any f ∈ V,  ∈ {−1,+1}n,σ ∈ Sn the function:

x  → f( 1xσ(1),..., nxσ(n)) is also in V .

It is clear that the subspaces Polk(Cn) are Gcube-invariant. The next result shows that these subspaces are actually irreducible under the action of Gcube.

- Lemma 3. Under the action of Gcube, F(Cn,R) decomposes into irreducible invariant subspaces as F(Cn,R) = Pol0(Cn) ⊕ ··· ⊕ Poln(Cn).


Furthermore, suppose k < n/2. Then Poln−k(Cn) ∼= en(x)Polk(Cn) where en(x) = x1 ···xn is the n’th elementary symmetric polynomial. Hence if V is a Gcube-invariant subspace with dim(V ) < nk then every

- f ∈ V has the form f(x) = g(x) + en(x)h(x)


where g(x) and h(x) have degree ≤ k − 1.

Proof. It is easy to see that Polk(Cn) is Gcube-invariant for each k. It remains to show that each of these is irreducible. For any k ∈ [n], let k ∈ Gcube be deﬁned by k = diag(1,...,−1,...,1) where the −1 is in the k’th position. If I ⊆ [n] we denote by xI the monomial i∈I xi. Observe that for a given k ∈ [n] and I ⊆ [n] we have:

2xI if k ∈/ I 0 otherwise.

(id+ k) · xI =

In other words the action of (id+ k) on F(Cn,R) annihilates all monomials involving xk. Similarly the action of k∈K(id+ k) on F(Cn,R) annihilates all monomials involving any xk, k ∈ K since the (id+ k) commute. Now ﬁx some arbitrary k and let V be a (non-zero) invariant subspace of Polk(Cn). We will show that necessarily V = Polk(Cn). Since V = {0}, V contains a nonzero square-free polynomial p(x). By the invariance of V under the permutation action, we can assume that the coeﬃcient of the monomial x1x2 ···xk in p is non-zero, and so p is of the form: p(x) = cx1 ···xk + |I|=k,I ={1,2,...,k} cIxI with c = 0. Now note that by the previous observation we have:

n

(id+ i) · p(x) = 2n−kx1x2 ···xk.

i=k+1

Hence V is a subspace containing x1x2 ···xk and hence, since V is invariant under the permutation action, it contains every square-free monomial of degree k. It follows that V = Polk(Cn) and so Polk(Cn) is irreducible.

To show the second part of the theorem, we use Proposition 1 from the introduction. Indeed note that

dimPolk(Cn) = nk . Thus Proposition 1 says that if V is an invariant subspace and dimV < nk with k ≤ n/2 then necessarily V is contained in the direct sum

k−1

(Poli(Cn) ⊕ Poln−i(Cn)).

i=0

Thus this means that any f ∈ V can be decomposed as:

k−1

f =

gi + gn−i

i=0

where gi ∈ Poli(Cn) and gn−i ∈ Poln−i(Cn). Now note that for i < n/2, Poln−i(Cn) ∼= en(x)Poli(Cn) because multiplication by en(x) is an involution of F(Cn,R) that sends square-free polynomials of degree i to square-free polynomials of degree n − i. Thus we can write gn−i(x) = en(x)hi(x) for some hi ∈ Poli(Cn). Thus we get that

k−1

f(x) =

gi(x) + en(x)hi(x) = g(x) + en(x)h(x) where deg g ≤ k − 1 and deg h ≤ k − 1.

i=0

| |
|---|


### 6 Conclusion

In this paper we presented a general framework to study equivariant psd lifts of orbitopes using tools from representation theory. We studied two particular examples in detail, namely the parity polytope and the cut polytope and we derived strong lower bounds for sizes of equivariant psd lifts.

Other examples of orbitopes There are clearly other examples of orbitopes that one could study using the framework developed in this paper. In a follow-up paper [FSP14] (see also [FSP15]) we looked at the case of regular polygons in the plane. We showed that regular N-gons in the plane admit equivariant psd lifts of size O(log N) and we established a matching lower bound. Our construction of the equivariant psd lift relies on ﬁnding a sparse sum-of-squares certiﬁcate for the facet inequalities of the regular N-gon. In the more recent paper [FSP15] we also give eﬃcient equivariant psd lifts of certain trigonometric cyclic polytopes. Other examples of orbitopes that are interesting to study are for example the permutahedron and the perfect matching polytope.

Non-polyhedral orbitopes Also, even though our paper was mainly concerned with orbitopes constructed from ﬁnite groups G, the structure theorems of Section 3 also apply when G is a compact subgroup of GL(Rn) and P is not necessarily polyhedral. For example, an interesting orbitope initially studied in [SSS11] is the convex hull of SO(n), where SO(n) is the set of n×n special orthogonal matrices. In [SPW14] it is shown that this convex body is a spectrahedron and an explicit semideﬁnite description is given. The structure theorem of this paper can also be applied to this example and shows that one can study equivariant psd lifts of conv(SO(n)) by studying invariant subspaces of F(SO(n),R) (the space of real-valued functions on SO(n)).

It is interesting that, for the purpose of obtaining lower bounds, our study of the parity polytope already implies an exponential lower bound on the size of equivariant lifts of conv(SO(n)): indeed it is known, by a celebrated result of Horn [Hor54] that SO(n) projects onto PARn via the diagonal map, i.e., diag(SO(n)) = PARn. This can be used to show that any psd lift of conv(SO(n)) equivariant with respect to an appropriate symmetry group can be turned into a Gparity-equivariant psd lift of PARn of the same size. Hence our exponential lower bound on the size of Gparity-equivariant psd lifts of PARn automatically gives an exponential lower bound on the size of certain equivariant psd lifts of conv(SO(n)). The details of this argument are given in [SPW14].

### A Proof of Theorem B: equivariance of sum-of-squares lifts when V is G-invariant.

Let X be a ﬁnite set in Rn and assume X is invariant under the action of a group G ⊆ GL(Rn). We also assume that conv(X) is full-dimensional. In this appendix, we show that the psd lift (6)-(7) is G-equivariant when the subspace V is chosen to be G-invariant.

Assume V is a subspace of F(X,R) such that any valid linear inequality on conv(X) has a sum-of-squares certiﬁcate from V . Then we saw in Section 1.2 that we have the following description of conv(X):

conv(X) = (E(e1),...,E(en)) : E ∈ F(X,R)∗ where

E(1) = 1, E(f2) ≥ 0 ∀f ∈ V .

(41)

where for each i, ei ∈ F(X,R) is the function deﬁned by ei(x) = xi. Equation (41) expresses conv(X) as a psd lift of size d = dimV . Indeed the last constraint on E in (41) is equivalent to saying that the bilinear form HE on V deﬁned by

HE : V × V → R, HE(f1,f2) = E(f1f2) is positive semideﬁnite. Thus if we identify Sd with bilinear forms on V (by ﬁxing a basis) then Equation

(41) can be rewritten as:

conv(X) = π(Sd+ ∩ L) (42) where

- • L ⊂ Sd is the aﬃne subspace L := {HE : E ∈ F(X,R)∗,E(1) = 1},

i.e., L the image of the aﬃne space {E ∈ F(X,R)∗,E(1) = 1} under the linear map E  → HE;

- • and π is the linear map, which given a bilinear form of the form HE for some E ∈ F(X,R)∗, returns the n-tuple (E(e1),...,E(en)) ∈ Rn (this linear map π is well-deﬁned when P is full-dimensional, since one can show in this case that the functions ei are all in span{f2 : f ∈ V }).


We now proceed to show that the psd lift (42) satisﬁes the deﬁnition of G-equivariance, where G is the automorphism group of X.

Since G acts on F(X,R), it also acts on the dual space F(X,R)∗ as follows: If E ∈ F(X,R)∗ then we let

(g · E)(f) := E(g−1 · f) ∀f ∈ F(X,R). Equivariance of the lift (42) now follows from the following main lemma:

- Lemma 4. Given E ∈ F(X,R)∗ we have for any g ∈ G and any f,h ∈ V : Hg·E(f1,f2) = HE(g−1 · f1,g−1 · f2). (43)


- Remark 6. One can interpret the identity (43) in matrix terms as follows: Given g ∈ G, let θ(g) be the d × d matrix which corresponds to the linear map f ∈ V  → g · f. Deﬁne ρ(g) = θ(g−1)T. Then identity (43) is the same as:


Hg·E = ρ(g)HEρ(g)T (44) where Hg·E and HE are interpreted as symmetric matrices of size d. ♦ Proof. The following sequence of equalities proves the claim:

Hg·E(f1,f2) = (g · E)(f1f2) = E(g−1 · (f1f2)) (=∗) E((g−1 · f1)(g−1 · f2)) = HE(g−1 · f1,g−1 · f2).

In Equality (*) we used the fact that the action of G on F(X,R) satisﬁes:

g · (f1f2) = (g · f1)(g · f2) which can be easily seen since for any x ∈ X we have:

g · (f1f2)(x) = (f1f2)(g−1 · x) = f1(g−1 · x)f2(g−1 · x) = (g · f1)(x)(g · f2)(x).

Using this lemma it is easy to check that the lift (42) satisﬁes the deﬁnition of G-equivariance.

| |
|---|


### B Proof of Theorem 4: factorization theorem for equivariant psd lifts

In this appendix we give the proof of the factorization theorem for equivariant psd lifts, Theorem 4. Before doing so, we ﬁrst prove the following factorization theorem for general positive semideﬁnite lifts from [GPT13]:

- Theorem 11. Let P be a polytope in Rn and let X be any subset of P. Assume P has a psd lift of size


d, i.e., P = π(Sd+ ∩ L) where L is an aﬃne subspace of Sd. Let A : X → Sd+ ∩ L be any map such that π(A(x)) = x for all x ∈ X. Then for any linear function ∈ (Rn)∗, there exists B( ) ∈ Sd+ such that:

max − (x) = A(x),B( ) ∀x ∈ X

where max := maxx∈P (x). Proof. The proof is mainly an application of SDP duality. Let ∈ (Rn)∗. Let Y0 ∈ L and let L0 = L − Y0 be the linear subspace parallel to L. The following two SDPs are dual to each other:

max ( ◦ π)(Y ) s.t. Y ∈ Sd+

min − H,Y0 s.t. − ◦ π = B + H

(45)

B ∈ Sd+, H ∈ L⊥0

Y − Y0 ∈ L0

We assume for simplicity that the intersection of L with the interior of Sd+ is nonempty, so that strong duality holds (the general case can also be handled). In this the case the value of the two SDPs above is equal to

max. Let B,H be the optimal points of the dual (minimization) problem in (45). From dual feasibility we have − ◦ π = B + H and so since max = − H,Y0 we get that:

max − ◦ π = B + H − H,Y0 . Evaluating this equality at A(x), for any x ∈ X we get:

max −  ,x = B,A(x) where we used the fact that ◦ π,A(x) =  ,x (since π(A(x)) = x) and H,A(x) − H,Y0 = 0.

| |
|---|


We now prove the factorization theorem for equivariant psd lifts, Theorem 4 from Section 3 which we restate below for convenience (the proof belows looks at the case where X consists of a single orbit of G, i.e., X = G · x0 which are the main focus of this paper – the proof however can be easily extended to the case where X consists of more than a single orbit, see e.g., [GPT13, Theorem 2]).

- Theorem 4. Let G be a ﬁnite group acting on Rn and let X = G · x0 where x0 ∈ Rn. Assume conv(X) = π(Sd+ ∩ L) is a G-equivariant psd lift of conv(X) of size d, i.e., there is a homomorphism ρ : G → GL(Rd)


such that conditions (i) and (ii) of Deﬁnition 2 hold. Then there exists a map A : X → Sd+ with the following properties:

- (i) For any linear form on Rn there exists B( ) ∈ Sd+ such that if we let max := maxx∈X (x) we have: max − (x) = A(x),B( ) ∀x ∈ X.
- (ii) The map A satisﬁes the following equivariance relation: A(g · x) = ρ(g)A(x)ρ(g)T ∀x ∈ X, ∀g ∈ G.


In particular if H denotes the stabilizer of x0, then we have: A(x0) = ρ(h)A(x0)ρ(h)T ∀h ∈ H. (46) Furthermore, the representation ρ : G → GL(Rd) can be taken to be orthogonal, i.e., ρ(g) ∈ O(Rd) for all

- g ∈ G.


Proof. We ﬁrst treat the case where the stabilizer of x0 is {1G}. In this case the proof is almost trivial: Let A(x0) be any point in Sd+ ∩ L such that π(A(x0)) = x0. Deﬁne, for any g ∈ G, A(g · x0) := ρ(g)A(x0)ρ(g)T. Note that A(g · x0) ∈ Sd+ ∩ L by the deﬁnition of an equivariant psd lift (Deﬁnition 2). Also note that

π(A(g · x0)) = π(ρ(g)A(x0)ρ(g)T) (=a) g · π(A(x0)) (=b) g · x0 (47)

where in (a) we used the deﬁnition of equivariant psd lift, and in (b) we used the fact that π(A(x0)) = x0. Since X = G · x0, Equation (47) shows that π(A(x)) = x for all x ∈ X. Thus we can use Theorem 11 with our choice of map A to show that Property (i) of the statement holds. Note that Property (ii) holds by construction of the map A.

We now treat the general case. Let H be the stabilizer of x0. Let A0 be any point in Sd+ ∩ L such that π(A0) = x0 and deﬁne:

1 |H| h∈H

ρ(h)A0ρ(h)T.

A(x0) =

Now we extend the map A to the whole X by letting A(x) = ρ(g)A(x0)ρ(g)T where g is any element of G such that g · x0. Note that this is well-deﬁned since if g · x0 = g · x0, we have, with h = g−1g ∈ H:

ρ(g )A(x0)ρ(g )T = ρ(gh)A(x0)ρ(gh)T

= ρ(g)ρ(h)A(x0)ρ(h)Tρ(g)T = ρ(g)A(x0)ρ(g)T.

It is easy to verify, like in the previous case, that the map we just deﬁned satisﬁes π(A(x)) = x for all x ∈ X. Thus by applying Theorem 11 with our choice of map A we get that Property (i) of the statement holds. Also Property (ii) holds by construction of the map A.

Note that we can assume ρ(g) to be orthogonal for any g ∈ G, by a simple change of basis: By Proposition 2 let Q be an invertible matrix such that Qρ(g)Q−1 is orthogonal. By letting ρˆ(g) = Qρ(g)Q−1, Aˆ(x) = QA(x)QT, Bˆ = Q−TBQ−1 we have A ˆ(x),Bˆ = A(x),B , Aˆ(g · x) = ρˆ(g)Aˆ(x)ˆρ(g)T and ρˆ(g)ˆρ(g)T = Id which is what we need.

| |
|---|


### References

[BB05] Alexander Barvinok and Grigoriy Blekherman. Convex geometry of orbits. Combinatorial and Computational Geometry. MSRI Publications, 52:51–77, 2005. 6

[BPT13] Grigoriy Blekherman, Pablo A. Parrilo, and Rekha R. Thomas. Semideﬁnite optimization and convex algebraic geometry. SIAM, 2013. 3

[BTN01] Aharon Ben-Tal and Arkadi Nemirovski. Lectures on modern convex optimization: analysis, algorithms, and engineering applications. SIAM, 2001. 1

[BV88] Alexander Barvinok and Anatolii Moiseevich Vershik. Convex hulls of orbits of representations of ﬁnite groups and combinatorial optimization. Functional Analysis and Its Applications, 22(3):224– 225, 1988. 6

[CK04] Robert D. Carr and Goran Konjevod. Polyhedral combinatorics. In Tutorials on emerging methodologies and applications in Operations Research, chapter 2, edited by Harvey Greenberg. Springer,

2004. 15

[CLRS13] Siu On Chan, James R. Lee, Prasad Raghavendra, and David Steurer. Approximate constraint satisfaction requires large LP relaxations. In IEEE 54th Annual Symposium on Foundations of Computer Science (FOCS), pages 350–359, 2013. 2, 22

[FGP+14] Hamza Fawzi, Jo˜o Gouveia, Pablo A. Parrilo, Richard Z. Robinson, and Rekha R. Thomas. Positive semideﬁnite rank. arXiv preprint arXiv:1407.4095, 2014. 8

- [FSP14] Hamza Fawzi, James Saunderson, and Pablo A. Parrilo. Equivariant semideﬁnite lifts of regular polygons. arXiv preprint arXiv:1409.4379, 2014. 17, 24
- [FSP15] Hamza Fawzi, James Saunderson, and Pablo A. Parrilo. Sparse sum-of-squares certiﬁcates on ﬁnite abelian groups. arXiv preprint arXiv:1503.01207, 2015. 21, 24


[Goe14] Michel Goemans. Smallest compact formulation for the permutahedron. Mathematical Programming, 2014. 2

[GPT10] Jo˜o Gouveia, Pablo A. Parrilo, and Rekha R. Thomas. Theta bodies for polynomial ideals. SIAM Journal on Optimization, 20(4):2097–2118, 2010. 3, 4, 5, 6

[GPT13] Jo˜o Gouveia, Pablo A. Parrilo, and Rekha R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of Operations Research, 38(2):248–264, 2013. 2, 4, 9, 26

[GRT13] Jo˜o Gouveia, Richard Z. Robinson, and Rekha R. Thomas. Polytopes of minimum positive semideﬁnite rank. Discrete & Computational Geometry, 50(3):679–699, 2013. 13

[Hor54] Alfred Horn. Doubly stochastic matrices and the diagonal of a rotation matrix. American Journal of Mathematics, 76(3):620–630, 1954. 24

[KP11] Volker Kaibel and Kanstantsin Pashkovich. Constructing extended formulations from reﬂection relations. In Integer Programming and Combinatorial Optimization, pages 287–300. Springer,

2011. 15

[KPT10] Volker Kaibel, Kanstantsin Pashkovich, and Dirk Theis. Symmetry matters for the sizes of extended formulations. Integer programming and combinatorial optimization, pages 135–148,

2010. 2 [Las09] Jean-Bernard Lasserre. Convex sets with semideﬁnite representation. Mathematical programming, 120(2):457–477, 2009. 3, 4, 5

- [Lau03] Monique Laurent. Lower bound for the number of iterations in semideﬁnite hierarchies for the cut polytope. Mathematics of Operations Research, 28(4):871–883, 2003. 6, 7, 8, 20, 21, 22
- [Lau04] Monique Laurent. Semideﬁnite relaxations for max-cut. The Sharpest Cut: The Impact of Manfred Padberg and His Work, (4):257, 2004. 20


[Lov79] L´szl´ Lov´sz. On the shannon capacity of a graph. IEEE Transactions on Information Theory, 25(1):1–7, 1979. 3

[LRS14] James R. Lee, Prasad Raghavendra, and David Steurer. Lower bounds on the size of semideﬁnite programming relaxations. arXiv preprint arXiv:1411.6317, 2014. 5, 8

[LRST14] James R. Lee, Prasad Raghavendra, David Steurer, and Ning Tan. On the power of symmetric LP and SDP relaxations. In Proceedings of the 29th IEEE Conference on Computational Complexity, pages 13–21. IEEE Computer Society, 2014. 8

[Pas09] Kanstantsin Pashkovich. Tight lower bounds on the sizes of symmetric extensions of permutahedra

and similar results. arXiv preprint arXiv:0912.3446, 2009. 2 [Ser77] Jean-Pierre Serre. Linear representations of ﬁnite groups. Springer New York, 1977. 8 [SPW14] James Saunderson, Pablo A. Parrilo, and Alan S. Willsky. Semideﬁnite descriptions of the convex

hull of rotation matrices. arXiv preprint arXiv:1403.4914, 2014. 24 [SSS11] Raman Sanyal, Frank Sottile, and Bernd Sturmfels. Orbitopes. Mathematika, 57(02):275–314,

2011. 6, 24 [Tun00] Levent Tunc¸el. Potential reduction and primal-dual methods. In Handbook of semideﬁnite programming, pages 235–265. Springer, 2000. 2 [Yan91] Mihalis Yannakakis. Expressing combinatorial optimization problems by linear programs. Journal of Computer and System Sciences, 43(3):441–466, 1991. 2, 9, 14

