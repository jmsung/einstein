arXiv:1309.0563v3[cs.CC]8Feb2016

# Approximate constraint satisfaction requires large LP relaxations

Siu On Chan∗ James R. Lee† Prasad Raghavendra‡ David Steurer§

Abstract

We prove super-polynomial lower bounds on the size of linear programming relaxations for approximation versions of constraint satisfaction problems. We show that for these problems, polynomial-sized linear programs are no more powerful than programs arising from a constant number of rounds of the Sherali–Adams hierarchy.

In particular, any polynomial-sized linear program for Max Cut has an integrality gap of 21 and any such linear program for Max 3-Sat has an integrality gap of 78.

![image 1](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile1.png>)

![image 2](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile2.png>)

## 1 Introduction

Linear programming is one of the most powerful tools known for ﬁnding approximately optimal solutions to NP-hard problems. We refer to the books [Vaz01, WS11] which each contain a wealth of examples. If P NP, then for many such problems we do not expect polynomial-sized linear programs (LPs) to compute arbitrarily good approximations to the optimal solution. (More formally, if NP P/poly, then such LPs cannot exist [Yan91].)

Thus a line of research has sought to prove lower bounds on the eﬃcacy of small linear programs. The construction of integrality gaps for speciﬁc LPs has long been a topic of interest in approximation algorithms. Arora, Bollobás, and Lovász [ABL02] initiated a more systematic study; they explored the limitations of LPs arising from lift-and-project hierarchies like those of Lovász and Schrijver [LS91] and Sherali and Adams [SA90]. There has now been an extensive amount of progress made in this area; one can see a sampling in the section on previous work.

Arguably, the ultimate goal of this study is to prove unconditional lower bounds for every suﬃciently small LP. Since linear programming is P-complete

![image 3](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile3.png>)

∗Microsoft Research New England †University of Washington ‡U. C. Berkeley §Cornell University

under various notions of reduction, this would require proving that NP does not have polynomial-size circuits (see, e.g., the discussion in [Yan91]). But one could still hope to complete this program for LPs that use the natural encoding of the underlying combinatorial problem.

We make progress toward this goal for the class of constraint satisfaction problems (CSPs). For instance, we prove that every polynomial-sized LP for Max Cut has an integrality gap of 12, answering a question from [BFPS12]. As another example, every such LP for Max 3-Sat has an integrality gap of 87, and every such LP for Max 2-Sat has an integrality gap of 34. In fact, in both cases these integrality gaps hold for families of LPs of size up to no(

![image 4](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile4.png>)

![image 5](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile5.png>)

![image 6](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile6.png>)

log n

log logn). Corresponding upper bounds for all three problems can be achieved by

![image 7](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile7.png>)

simple polynomial-sized LPs. For Max 3-Sat, a 87-approximation is best-possible assuming P NP [Hås01]. For Max Cut, the seminal SDP-based algorithm of

![image 8](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile8.png>)

Goemans and Williamson [GW95] achieves a 0.878-approximation. In this case, our result yields a strict separation between the power of polynomial-sized LPs and SDPs for a natural optimization problem. Interestingly, even a simple spectral algorithm can do strictly better than 1/2 for Max Cut [Tre12].

To establish these lower bounds, we show that for approximating CSPs, polynomial-sized LPs are exactly as powerful as those programs arising from O(1) rounds of the Sherali–Adams hierarchy. We are then able to employ the powerful Sherali–Adams gaps that appear in prior work. This oﬀers a potential framework for understanding the power of linear programs for many problems by relating their expressive power to that of the very explicit Sherali–Adams hierarchy.

In Section 1.2, we discuss our approach for the speciﬁc example of Max Cut, including the class of LPs to which our results apply. Section 2 is devoted to a review of CSPs and their linear relaxations. There we explain our basic approach to proving lower bounds by exhibiting an appropriate separating hyperplane. We also review the Sherali–Adams hierarchy for CSPs. In Section 3, we present the technical components of our approach, as well as the proof of our main theorem.

Finally, Section 4 contains an illustrative discussion of how Sherali–Adams gap examples can be used to construct corresponding gaps for symmetric LPs. This connection is quantitatively stronger than our result for general LPs. We refer to Section 5 for a discussion of future directions.

Recent work. Since initial publication of this manuscript, there has been substantial followup work building on the ideas presented here. The papers [LRST14, FSP13] establish a connection between symmetric semideﬁnite programs and the Sum-of-Squares hierarchy by analogy with our work in Section 4. In [LRS15], a connection between general semideﬁnite extended formulations and the Sum-of-Squares hierarchy is established; in particular, the authors prove

exponential lower bounds on the semideﬁnite extension complexity of explicit polytopes (like the TSP polytopes). Finally, our models for approximation via linear programs are extended and reﬁned in the work [BPZ15]; the authors show that a suitable notion of reduction within the model allows one to derive lower bounds for additional problems (other than CSPs).

### 1.1 History and context

Extended formulations. In a seminal paper, Yannakakis [Yan91] proved that everysymmetricLP(i.e.,onewhoseformulationisinvariantunderpermutations of the variables) for TSP has exponential size. Only recently was a similar lower bound given for general LPs. More precisely, Fiorini, et al. [FMP+12] show that the extension complexity of the TSP polytope is at least 2Ω(

√n) for n-vertex graphs.

![image 9](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile9.png>)

Braun, et al. [BFPS12] expand the notion of extension complexity to include approximation problems and show that approximating Max Clique within O(n1/2−ε) requires LPs of size 2Ω(nε). Building on that work, Braverman and Moitra [BM13] show that approximating Max Clique within O(n1−ε) requires LPs of size 2Ω(nε). We remark that the encoding of Max Clique used in the later two works is somewhat lacking. Speciﬁcally, these lower bounds do not encompass, for instance, standard relaxations for Max Clique, including those given by the Sherali-Adams hierarchy.

These three latter papers all use Yannakakis’ connection between extension complexityandnon-negativerank(see[FMP+12]foradetaileddiscussion). They are based on increasingly more sophisticated analyses of a single family of slack matrices ﬁrst deﬁned in [FMP+12] (and extended to the approximation setting by [BFPS12]). Closely related slack matrices are employed in a recent paper of Rothvoss[Rot14] toshowexponentiallowerbounds ontheextensioncomplexity of the matching polytope. A signiﬁcant contribution of the present work is that the connection between general LPs and the Sherali–Adams hierarchy allows one to employ a much richer family of hard instances.

LP and SDP hierarchies. As mentioned previously, starting with the works [ABL02, ABLT06], the eﬃcacy of LP and SDP hierarchies for approximation problems has beenextensivelystudied. We refertothesurveyofLaurent[Lau03] for a discussion of the various hierarchies and their relationships.

We mention a few results that will be quite useful for us. Fernández de la Vega and Mathieu [FdlVKM07] showed that for any ﬁxed ε > 0 and k, Max Cut has an integrality gap of 12 +ε even after k rounds of the Sherali–Adams hierarchy. In a paper of Charikar, Makarychev, and Makarychev [CMM09], it is shown that Max Cut and Vertex Cover have integrality gaps of 21 +ε and 2−ε, respectively, for nΩ(ε) rounds of the Sherali–Adams hierarchy.

![image 10](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile10.png>)

![image 11](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile11.png>)

In work of Schoenebeck [Sch08], tight bounds are given on the number of rounds needed to approximate k-CSPs in the Lasserre hierarchy (which, in particular, is strongerthan theSherali–Adams hierarchy). Forinstance, he shows that for every ε > 0, Max 3-Sat has a 87 + ε integrality gap even after Ω(n) rounds. One should consult also the much earlier work of Grigoriev [Gri01] which achieves an equivalent family of lower bounds stated in the dual setting of Positivstellensatz proof systems. There are also Sherali–Adams integrality gaps for CSPs with a pairwise independent predicate, due to Benabbas et al. [BGMT12].

![image 12](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile12.png>)

Strong separation between nonnegative rank and smooth nonnegative rank. We remark that all previous lower bounds for nonnegative rank (at least in the context of extended formulations) are robust with respect to small multiplicative perturbations [Rot14, FMP+12, BFPS12, BM13]. Concretely, if we deﬁne the εsmooth nonnegative rank of a matrix A as

rank+,ε(A) := min rank+(A′) | (1 − ε)Aij A′ij (1 + ε)Aij ,

then all previous lower bounds for nonnegative rank also lower bound the εsmooth version for some absolute constant ε > 0. A related generalization of nonnegative rank is approximate nonnegative rank that allows additive instead of multiplicative error. 1 This version of nonnegative rank is equivalent to the smooth rectangle bound [KMSY14].

Incontrast,thematricesstudiedinthisworkturnouttohaveonlypolynomial approximate and smooth nonnegative rank. In this sense, our superpolynomial lower bounds on the nonnegative rank of these matrices give the ﬁrst separation between nonnegative rank and smooth nonnegative rank. See Section 3.4 for a discussion.

### 1.2 Outline: Max Cut

WenowpresentthebasicdetailsofourapproachappliedtotheMaxCutproblem. To this end, consider a graph G = (V,E) with |V| = n. For any S ⊆ V, we use

G(S) def= |E(S,S¯)| |E|

![image 13](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile13.png>)

to denote the fraction of edges of G crossing the cut (S,S¯). The maximum cut value of G is opt(G) = maxS⊆V G(S).

![image 14](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile14.png>)

1All previous lower bounds also hold for this generalization of nonnegative rank. However, some of the lower bound arguments do not apply to the additive-error setting. (For example, arguments that rely on the zero / non-zero pattern of the matrix.)

The standard LP. To construct an LP for computing (or approximating) opt(G), it is natural to introduce variables x = (x1,x2,...,xn) ∈ {−1,1}n corresponding to the vertices of G. One can then write, for instance,

1 − xixj 2

1 |E| {i,j}∈E

opt(G) = max

.

![image 15](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile15.png>)

![image 16](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile16.png>)

x∈{−1,1}n

To convert this computation into a linear program, we need to linearize the objective function.

The usual way is to introduce new LP variables y = (yi,j) ∈ R(n2) meant to represent the quantities (1 − xixj)/2. Now consider the vector vG ∈ {0,1}(n2) such that (vG){i,j} = 1 precisely when {i, j} ∈ E. Given that we have linearized both the graph G and the cut variable x, we can consider the LP relaxation

L(G) = max

y∈P

vG, y ,

where P is any polytopecontaining all the vectors y such that yi,j = (1−xixj/2) for some x ∈ {−1,1}n. The standard relaxation corresponds to a polytope P deﬁned

by the constraints {0 yi,j 1 : i, j ∈ V} and

yi,j yi,k + yk,j, yi,j + yi,k + yk,j 2 : i, j,k ∈ V . Clearly P is characterized by O(n3) inequalities.

Arbitrary linearizations. But it is important to point out that, for our purposes, any linearization of thenatural formulation of Max Cut suﬃces. We only require that there is a number D ∈ N such that:

- 1. For every graph G, we have a vector vG ∈ RD.
- 2. For every cut S ⊆ V, we have a vector yS ∈ RD.
- 3. For all graphs G and vectors yS, the condition G(S) = vG, yS holds.


Now any polytope P ⊆ RD, such that yS ∈ P for every S ⊆ V, yields a viable LP relaxation: L(G) = maxy∈P vG, y . The size of this relaxation is simply the number of facets of P, i.e. the number of linear inequalities needed to specify P.

- Remark 1.1. We stress that the polytope P depends only on the input size. This is akin to lower bounds in non-uniform models of computation like circuits wherein there is a single circuit for all inputs of a certain size. The input graph G is used only to deﬁne the objective function being maximized. In other words, the variables and constraints of the linear program are ﬁxed for each input size while the objective function is deﬁned by the input. To the best of our knowledge, all linear and semideﬁnite programs designed for approximating max-CSP problems are subsumed by relaxations of this nature.


In Section 3, we prove that every such relaxation of polynomial size has an integrality gap of 12 for Max Cut. We now give an informal outline of the proof. Provinga lower bound. In Theorem 2.3, we recall that if there is an LPrelaxation L of size R, then a simple application of Farkas’ Lemma shows that there are non-negative functions q1,...,qR : {−1,1}n → R 0 such that for every graph G, there are coeﬃcients λ0,λ1,...,λR 0 satisfying

![image 17](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile17.png>)

L(G) − G(x) = λ0 + λ1q1(x) + ··· + λRqR(x). (1.1)

for all x ∈ {−1,1}n. (Note that we have earlier viewed G as a function on cuts and we now view it as a function on {−1,1}n by associating these vectors with cuts.)

One should think of (1.1) as saying that L(G) − G ∈ cone(1,q1,q2,...,qR), where thelatter object is thecone generatedby {1,q1,q2,...,qR} inside theHilbert space L2({−1,1}n) of real-valued functions, and 1 denotes the function that is identically 1. These functions qi : {−1,1}n → R 0 encode the slack of each constraint of the LP. Thus if the ith LP constraint is of the form Ai,z bi, then qi(x) = bi − Ai, ySx where ySx is the cut vector corresponding to x ∈ {−1,1}n.

Consider some m ≪ n. The d-round Sherali–Adams relaxation for an mvertex graph G0 has value SAd(G0) c if and only if there exist a family of non-negative d-juntas {fi : {−1,1}m → R 0} such that

c − G0 =

i

λi fi , (1.2)

where λi 0 for each i. We recall thata d-junta is a function whosevalue depends on at most d of its inputs. See Section 2.1 for an explanation of (1.2).

In particular, if G0 is such that SAd(G0) > c, then no such representation (1.2) with d-juntas can exist. Our goal is to use (1.1) to ﬁnd a graph G on n vertices such that opt(G) = opt(G0), and such that G0 has a representationof theform (1.2) with c = L(G). This will showthatL(G) SAd(G0), completingour proof. (Recall that since we are dealing with maximization problems and opt(G) = opt(G0), this means that our LP is not doing better than Sherali–Adams.)

This proceeds in three steps: First, we argue that, by a truncation argument, it suﬃcestoconsiderfunctions{qi} thatare suﬃcientlysmooth. Thenin Section 3.1, we show that any suﬃciently smooth qi can be approximated (in a certain weak sense) by a K-junta q′i for K which may be quite large (e.g., K = n0.2).

In Section 3.2, we employ a random restriction argument: By planting the m-vertex instance G0 at random inside a larger graph G (on n vertices), we can ensure that for every q′i, the set of signiﬁcant coordinates when restricted to G0 is much smaller; in fact, we show that with high probability over the random planting, every such q′i has only d signiﬁcant coordinates in the support of G0. Here we use crucially the fact that we have only R functions {qi}, where R nαd for some small constant α > 0.

In particular, applying (1.1) to G and then restricting our attention to the vertices in V(G0), this yields a representation of the form

L(G) − G0 = λ0 +

R

λiqi|V(G0) , (1.3)

i=1

and, when restricted to G0, every qi is weakly approximated by a d-junta q′i. More speciﬁcally, all the low-degree Fourier coeﬃcients of qi −q′i are small. Now, the fact that (1.3) holds and each qi is approximately a d-junta will yield that L(G) SAd(G0), taking (1.2) into consideration. Here we remain vague, but the reader should notethat this implication would follow immediately if each qi|V(G0) were actually a d-junta.

This will hold true as long as the “approximation” does not hurt us too much. One might think that our approximation is too weak: We only know that q′i approximates qi on V(G0) in the low-degree part. Now we use the fact that the d-round Sherali–Adams relaxation is only capable of perceiving low-degree functions (more technically, the d-round Sherali–Adams functional introduced in Section 2.1 is a degree-d multilinear polynomial). In particular, it suﬃces that the low-degree parts of qi and q′i are close.

The ingredients are all put together in Section 3.3, where one can ﬁnd the proof of our main theorem for general CSPs.

## 2 Background

We now review the maximization versions of boolean CSPs, their linear programming relaxations, and related issues.

Throughout the paper, for a function f : {−1,1}n → R, we write E f =

2−n x∈{−1,1}n f(x). If : {−1,1}n → R, we denote the inner product f, = E[f ] on the Hilbert space L2({−1,1}n). Recall that any f : {−1,1}n → R can be written

uniquely in the Fourier basis as f = α⊆[n] fˆ(α)χα, where χα(x) = i∈α xi and fˆ(α) = f,χα . A function f is called a d-junta for d ∈ [n] if f depends only on a subset S ⊆ [n] of coordinates with |S| d. In other words, f can be written as f = α⊆S fˆ(α)χα.

We say that f is a density if it is non-negative and satisﬁes E f = 1. For such an f, we let µf denote the corresponding probability measure on {−1,1}n. Observe that for any : {−1,1}n → R, we have Ex∼µf [ (x)] = f, .

Constraint Satisfaction Problems. Constraint satisfaction problems form a broad class of discrete optimization problems that include, for example, Max Cut and Max 3-Sat. For simplicity of presentation, we will focus on constraint satisfaction problems with a boolean alphabet, though similar ideas extend to larger domains (of constant size). One can consult [LRS15, §7].

For a ﬁnite collection Π = {P} of k-ary predicates P: {−1,1}k → {0,1}, we let Max-Π denote the following optimization problem: An instance ℑ consists of boolean variables X1,...,Xn and a collection of Π-predicates P1(X),...,Pm(X) over these variables. A Π-predicate is a predicate P0: {−1,1}n → {0,1} such that P0(X) = P(Xi1,...,Xik) for some P ∈ Π and distinct indices i1,...,ik ∈ [n]. The objective is to ﬁnd an assignment x ∈ {−1,1}n that satisﬁes as many of the predicates as possible, that is, which maximizes

m

ℑ(x) def= m1

Pi(x).

![image 18](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile18.png>)

i=1

We denote the optimal value of an assignment for ℑ as opt(ℑ) = maxx∈{−1,1}n ℑ(x).

Examples: Max Cut corresponds to the case where Π consists of the binary inequality predicate. For Max 3-Sat, Π contains all eight 3-literal disjunctions, e.g., X1 ∨ X¯2 ∨ X¯3.

Linear Programming Relaxations for CSPs. In order to write an LP relaxation for such a problem, we need to linearize the objective function. For n ∈ N, let Max-Πn be the set of Max-Π instances on n variables. An LP-relaxation of size R for Max-Πn consists of the following.

Linearization: Let D be a natural number. For every ℑ ∈ Max-Πn, we associate a vector ℑ˜ ∈ RD and for every assignment x ∈ {−1,1}n, we associate a point x˜ ∈ RD, such that ℑ(x) = ℑ ˜ ,x˜ for all ℑ ∈ Max-Πn and all x ∈ {−1,1}n.

Feasible region: A closed, convex (possibly unbounded) polyhedron P ⊆ RD described by R linear inequalities, such that x˜ ∈ P for all assignments x ∈ {−1,1}n. Note that the polytope P is independent of the instance ℑ of Max-Πn.

Given an instance ℑ ∈ Max-Πn, the LP relaxation L has value L(ℑ) def= max

ℑ ˜ , y .

y∈P

Since x˜ ∈ P for all assignments x ∈ {−1,1}n and ℑ ˜ ,x˜ = ℑ(x), we have L(ℑ) opt(ℑ) for all instances ℑ ∈ Max-Πn.

- Remark 2.1. For concreteness, there is a “universal linearization” for CSPs that one can always use (this is sometimes referred to as the “vertex extended formulation”). One views x  → ℑ(x) as a multilinear polynomial over {−1,1}n. In the


Fourier basis {χα : α ⊆ [n]}, one would have ℑ˜ = α ℑˆ (α)χα and x˜ = α χα(x)χα. Note that if the Πn contains k-ary predicates, then ℑ˜ and x˜ are multilinear polynomials of degree at most k.

Remark 2.2. Of course, in the preceding linearization, the number of variables is now 2n. But if the number of deﬁning inequalities small, one can reduce the number of variables via an appropriate linear transformation; see [FMP+12].

SymmetricLinearPrograms. AsymmetricLPisoneforwhichthelinearization is symmetric under any permutation of the input variables. More precisely, let us suppose L is a linear program for Max-Πn that associates to each instance ℑ, a linearization ℑ˜ ∈ RD and to every assignment x ∈ {−1,1}n a point x˜ ∈ RD.

LetSym(n) denotethe symmetric group on {1,2,...,n}. Notethat Sym(n) acts naturally on elements x ∈ Rn by permutation of the coordinates. Speciﬁcally, for a permutation σ ∈ Sym(n) and x ∈ {−1,1}n, let σx = xσ(1),xσ(2),...,xσ(n) . This action extends to an action of Sym(n) on functions f : {−1,1}n → R by deﬁning σf(x) = f(σx) for σ ∈ Sym(n).

We say thatthelinearprogramLissymmetricifthefollowingholds: Forevery permutation σ ∈ Sym(n), there exists a corresponding permutation σ˜ ∈ Sym(D) such that for every assignment x ∈ {−1,1}n,

σx = σ˜x˜ ,

and the feasible region P ⊂ RD remains invariant under the permutation σ˜ of coordinates, i.e.,

σ˜P = P.

To the best of our knowledge, all linear and semideﬁnite programming relaxations designed for approximating max-CSP problems have been symmetric relaxations. In general, assymetric relaxatiosn could be much more powerful as demonstrated by Kaibel et al. [KPT10] who show that asymmetric LPs can be superpolynomially smaller than symmetric LPs for optimizing over logn-sized partial matchings.

(c,s)-approximation. For c > s 0, we say that a linear programming relaxation L for Max-Πn is a (c,s)-approximation if L(ℑ) c for all instances ℑ ∈ Max-Πn with opt(ℑ) s. We also say that L achieves an α-factor approximation if L(ℑ)

αopt(ℑ) for all ℑ ∈ Max-Πn.

The following theorem is inspired by Yannakakis’s characterization of exact linear programming relaxations. It appears in similar form in previous works [Pas12] and [BFPS12, Thm. 1]. For simplicity, we specialize it here for constraint satisfaction problems.

- Theorem 2.3. For every c,s ∈ [0,1], there exists an LP relaxation of size at most R that achieves a (c,s)-approximation for Max-Πn if and only if there exist non-negative functions q1,...,qR: {−1,1}n → R 0 such that for every instance ℑ ∈ Max-Πn with opt(ℑ) s, the function c − ℑ is a nonnegative combination of the functions q1,...,qR and 1, i.e.


R

c − ℑ ∈ λ0 +

λiqi λ0,λ1,...,λR 0 . (2.1)

i=1

Moreover, if the LP relaxation is symmetric then there exist nonnegative functions q1,...,qR : {−1,1}n → R 0 witnessing (2.1) and such that q1,...,qR is closed under the action of Sym(n).

Proof. First, we prove that the existence of an LP relaxation of size R yields a representation of the form (2.1). Consider a natural number D and linearizations ℑ˜ ,x˜ ∈ RD for every ℑ ∈ Max-Πn and x ∈ {−1,1}n. Let P ⊆ RD be speciﬁed by R linear inequalities Ai, y bi, and such that x˜ ∈ P for every x ∈ {−1,1}n. We deﬁne the function qi : {−1,1}n → R+ by qi(x) = bi − Ai,x˜ .

Consider now any instance ℑ with opt(ℑ) s. By assumption, we have L(ℑ) c, meaningthat c y,ℑ ˜ holds for all y ∈ P. NowFarkas’ Lemma[Sch03, Corollary 5.3c] tells us that every valid linear inequality over P can be written as a non-negative combination of the inequalities {bi − Ai, y 0 : i = 1,2,...,R}, and the inequality 1 0. This yields the existence of non-negative numbers {λi} such that c − y,ℑ ˜ = λ0 + Ri=1 λi(bi − Ai, y ) holds for all y ∈ P.

In particular, this holds for every x˜, where x ∈ {−1,1}n. Now, a deﬁning property of the linearization is that x ˜,ℑ ˜ = ℑ(x) for every x ∈ {−1,1}n. Thus we have arrived at a representation of the form (2.1).

We now show the reverse implication. Considerfunctions {qi} satisfying (2.1). We will let D = 2n and the D-dimensional Hilbert space for our linearization will be L2({−1,1}n), which we identify with the linear span of the Fourier characters {χα : α ⊆ [n]}. We use the linearization appearing in Remark 2.1. We may think of each qi as lying in L2({−1,1}n). Deﬁne a polyhedron P ⊆ L2({−1,1}n) by P = {y ∈ L2({−1,1}n) : y,qi 0,i = 1,...,R}. This yields an LP of size at most R since x ˜,qi = qi(x) 0 for every i and x ∈ {−1,1}n. Now (2.1) tells us that whenever opt(ℑ) s, the inequality y,ℑ ˜ c is valid over P, implying that L(ℑ) c. Thus our LP is a (c,s)-approximation.

Finally, suppose the LP relaxation is symmetric. By deﬁnition, for every σ ∈ Sym(n), there exists a σ˜ ∈ Sym(D) such that σx = σ˜x˜ for all x ∈ {−1,1}n and the polytope P is invariant under the action of σ˜. We may assume that P is full-dimensional, and moreover that the facet-deﬁning inequalities Ai, y bi are normalized so that Ai 2 = 1.

Consider an inequality of Ai, y bi of the polyhedron P and the corresponding function qi : {−1,1}n → R deﬁned by qi(x) = bi − Ai,x˜ . Since P is invariant under the action of σ˜, the faces of P are mapped to each other by the permutation σ˜. Now by our choice of normalization Ai 2 = 1 for i = 1,2,...,R, the facet-deﬁning inequality Ai,σ˜y bi is the same as Aj, y bj for some j ∈ {1,2,... ,R}. Henceforall x ∈ {−1,1}n, qi(σx) = bi− Ai,σ˜x˜ = bj− Aj,x˜ = qj(x). This implies that one can choose the family Q = {q1,...,qR} of functions to be invariant under the action of Sym(n).

A communication model. The characterization in Theorem 2.3 has an illustrative interpretation as a two-party, one-way communication complexity problem: Alice’s input is a Max-Π instance ℑ with opt(ℑ) s. Bob’sinput is an assignment x ∈ {−1,1}n. Their goal is to compute the value ℑ(x) in expectation. To this end, Alice sends Bob a randomized message containing at most L bits. Given the

message Bob outputs deterministically a number v such that v c. The protocol is correct if for every input pair (ℑ,x), the expected output satisﬁes Ev = ℑ(x) (the expectation is over Alice’s randomness).

An L-bit protocol for this communication problem yields an LP relaxation of size 2L: If Bob outputs a value v(x,i) based on message i from Alice, then deﬁne qi(x) = c − v(x,i). This yields 2L non-negative functions satisfying the conditions of Theorem 2.3.

On the other hand, if there exist R = 2L functions {q1,q2,...,qR} as in

- Theorem 2.3, then by adding the constant function q0 and an appropriate λ0 0,


we may assume that Ri=0 λi = 1, i.e. that we have a convex combination instead of a non-negative combination. This yields a strategy for Alice and Bob: Alice sends an index i ∈ {0,1,...,R}, drawn from a distribution depending on ℑ (speciﬁed by the coeﬃcients {λi}), and then Bob outputs c − qi(x) c.

Example: Suppose the optimization problem is Max Cut. In this case, Alice receives a graph G = (V,E) and Bob a cut S ⊆ V. If Alice sends Bob a uniformly random edge {u,v} ∈ E and Bob outputs the value |1S(u) − 1S(v)|, the result is a communication (in expectation) protocol using at most log2 n2 bits of communication. In this communication protocol, the value output by Bob is always at most 1. Therefore, this corresponds to a trivial (1,s)-approximation for Max Cut for every s < 1. In any protocol achieving a less trivial approximation, Bob would have to always output numbers strictly less than 1.

A similar communication in expectation model is considered in [FFGT11], where they show that the communication complexity is equal to the logarithm of the non-negative rank (up to an additive constant) of the associated slack matrix. There is an importantdistinction, however; theirmodelinvolves communicating a slack matrix in expectation (the value c − ℑ(x)), while the model here deals directly with the underlying combinatorial problem (the value ℑ(x)).

### 2.1 Sherali–Adams LP relaxations for CSPs

A primary component of our approach involves leveraging known integrality gaps for the Sherali–Adams (SA) hierarchy. To that end, we now give a brief overview of Sherali–Adams LP relaxations. For a more detailed account, we refer the reader to [Lau03].

A d-round Sherali–Adams LP relaxation for a Max-Πn instance will consist of variables {XS : S ⊆ [n],|S| d} for all products of up to degree-d on the n variables. These variables {XS : |S| d} are to be thought of as the moments up to degree-d of the variables, under a purported distribution.

An important property of an SA solution {XS : |S| d} is that these moments agree with a set of local marginal distributions. In particular, for everyset S ⊆ [n] with |S| d there exists a distribution µS over {−1,1}S such that,

χA(x) = XA ∀A ⊆ S.

E

x∼µS

In an alternate but equivalent terminology, a d-round SA instance can be thought of as d-local expectation functional (d-ℓ.e.f.). Fix n 1. We deﬁne a d-local expectation functional to be a linear functional E˜ on degree-d n-variate multilinear polynomials such that E˜ 1 = 1 and E˜ P 0 for every degree-d multilinear polynomial P that is nonnegative over {−1,1}n and depends only on d variables. In terms of the local marginal distributions, E˜ : {−1,1}n → R is the unique linear functional satisfying

E˜ χS = E

x∼µS

χS(x) ∀|S| d,S ⊆ [n], (2.2)

and E˜ χS = 0 for |S| > d,S ⊆ [n]. The d-round Sherali–Adams value of a Max-Πn instance ℑ is deﬁned as

SAd(ℑ) def= max

E˜ ℑ. (2.3)

d-ℓ.e.f. E˜

This optimization problem can be implemented by an nO(d)-sized linear programming relaxation for Max-Πn. (Notice that E˜ is a di=0 ni -dimensional object.) In particular, if d-rounds of Sherali–Adams achieve a (c,s)-approximation for Max-Πn, then so do general nO(d)-sized LP relaxations.

We remark that a d-ℓ.e.f. E˜ is a linear functional, but using self-duality of L2({−1,1}n), we may also think of E˜ ∈ L2({−1,1}n). It has the Fourier representation

E˜ (χα)χα .

E˜ =

|α| d

We will use this representation freely.

- Lemma 2.4. If E˜ is a d-ℓ.e.f. on L2({−1,1}n), then the following properties hold:


- i For any non-negative d-junta f : {−1,1}n → R+, we have E˜ f 0.
- ii For any α ⊆ [n], we have |E˜ χα| 1.
- iii E ˜ ∞ di=0 ni .


Proof. Property (i) follows directly from the deﬁnition of a d-ℓ.e.f.. Property (ii) follows from (2.2). Property (iii) follows from (ii) using the fact that E˜ has at most di=0 ni non-zero Fourier coeﬃcients.

It might help the reader, at this point to recall Theorem 2.3 and the representation (2.1). Suppose that we had such a representation where the family of functions {qi} were all d-juntas. Fix an instance ℑ and let E˜ denote an optimal solution to (2.3). Applying E˜ to the right-hand side of (2.1) yields

E˜ λ0 + λ1q1 + ··· + λRqR = λ0 +

R

λi E˜ qi 0,

i=1

using Lemma 2.4(i). On the other hand, applying it to the left-hand-side yields E˜ (c−ℑ) = c−SAd(ℑ). Altogether, we conclude that SAd(ℑ) c. In particular, this holds for any c L(ℑ), hence SAd(ℑ) L(ℑ), implying that in this special case (when all the qi functions are d-juntas), the Sherali–Adams relaxation is at least

- as good as the given LP. In general, our approach will be to approximate the {qi} functions by juntas, and then apply a variant of this reasoning.


- Remark 2.5. Some work on Sherali–Adams relaxations for Max Cut focus on edge variables instead of vertex variables. This includes [FdlVKM07, CMM09]. In those papers, the d-round Sherali–Adams relaxation consists of variables {XS : S ⊆ [n2] ,|S| d} for every subset of d edges in the complete graph. Since


their base polytope also includes triangle inequalities, any d2 -round Sherali– Adams solution with edge variables can be converted to a d-round solution for

vertex variables. One should observe that the d-round vertex relaxation is at least as strong as the d-round edge relaxation.

Moreover, both papers [FdlVKM07, CMM09] actually prove a lower bound against the d-round vertex version and then argue that this yields a lower bound for the weaker edge relaxation. For general max-CSPs, the vertex version is arguably the canonical relaxation, and it is perhaps misguided to consider the edge version even for Max Cut. In [Sch08] (which studies general CSPs), the more natural vertex version is considered.

A major beneﬁt of the “extended formulation” model to which our results apply is that the edge/vertex relaxation distinctions are not relevant; in fact no speciﬁc meaning is ascribed to the variables of the LP. All that matters is the number of deﬁning inequalities.

## 3 Sherali–Adams and general LPs

Our main theorem is that general LP relaxations are no more powerful than Sherali–Adams relaxations (in the polynomial-size regime).

- Theorem 3.1 (Main). Fix a positive number d ∈ N, and a sequence of k-ary CSPs {Max-Πn}, with k d. Suppose that the d-round Sherali–Adams relaxation cannot achieve a (c,s)-approximation for Max-Πn for every n. Then no sequence of LP relaxations of size at most nd/2 can achieve a (c,s)-approximation for Max-Πn for every n.


We prove the following result for super-polynomial sized linear programs in Section 3.3.

- Theorem 3.2. Consider a function f : N → N. Suppose that the f(n)-round Sherali–


Adams relaxation cannot achieve a (c,s)-approximation for Max-Πn. Then for all suﬃciently large n, no LP relaxation of size at most nf(n)2 can achieve a (c,s)-approximation for Max-ΠN, where N n10f(n).

In particular, by choosing f(n) ≍ nε for ε > 0, and n ≍ (logN)/(log logN) 1/ε, known Sherali–Adams gaps for Max Cut [CMM09] and Max 2-Sat, Max 3-Sat [Sch08] imply the same integrality gaps for LPs of size no(

log n

loglogn).

![image 19](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile19.png>)

### 3.1 High-entropy distributions vs. juntas

Ourﬁrstgoalistoobserve thefollowing consequence ofChang’sLemma[Cha02] (and, speciﬁcally, the proof in [IMR14]).

- Lemma 3.3. Let q: {−1,1}n → R 0 be a density and let µq denote the corresponding measure on {−1,1}n. If µq has entropy at least n − t for some t n, then for every 1 d n and γ > 0, there exists a set J ⊆ [n] with


2td γ2

|J|

(3.1)

![image 20](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile20.png>)

such that for all subsets α J with |α| d, we have |qˆ(α)| γ. Proof. Consider some γ > 0 and let S = {|α| d : |qˆ(α)| > γ}. Let S′ ⊆ S denote a maximal set of linearly independent elements over Fn2. In [IMR14], it is proved that |S′| 2γ−2t. Let J = α∈S′ α so that |J| 2dγ−2t.

- Remark 3.4. The claim in [IMR14] (namely Lemma 2 in [IMR14]) is only stated for


a q = (2n/|A|)1A that is the (scaled) characteristic function of a subset A ⊆ {−1,1}n, but the proof only uses the entropy of q. A formal statement with a somewhat diﬀerent proof can be found in [LRS15, §7].

Discussion of Lemma 3.3. It is interesting to note examples for which

- Lemma 3.3 cannot be improved much. First, suppose that n is odd, and consider the density coming from majority on n bits:


q(x) = 2 · 1{x1+···+xn>0} . (3.2)

The corresponding measure µq has entropy n − 1. In this case, we have |qˆ(α)| ≈ n−d/2 for |α| = d, d odd, and d ≪

√n. Thus (3.1) is essentially tight for t = d = 1.

![image 21](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile21.png>)

Considerthe taskof obtaining |J| = n1−δ and γ = n−ω(1), for some δ > 0. This is the interesting range of parameters in the next section. For the majority density (3.2), this is clearly impossible in light of our discussion. On the other hand, if one could obtain a rate of decay of the form n−c(d), with c(d) → ∞ as d → ∞ on the non-junta low-degree Fourier coeﬃcients, then one could improve our main theorem (see (3.7)).

Unfortunately, the next example shows that this is impossible. Let k,n ∈ N

be such that k divides n, and partition {1,2,...,n} = B1 ∪ B2 ∪ ··· ∪ Bn/k into n/k disjoint blocks, each of size k. Consider the density

k2k n

q(x) =

![image 22](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile22.png>)

n/k

1{xj=1∀j∈Bi} .

i=1

This function has a transitive symmetry, and thus for k = o(n), does not admit an interesting junta set of size o(n). On the other hand for any α ⊆ Bi, we have

k n

2k−|α| .

|qˆ(α)| = | q,χα | =

![image 23](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile23.png>)

If we put k = √n, then we do not have an appreciable decay of the form n−c(d) with c(d) → ∞ as d → ∞.

![image 24](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile24.png>)

But not all hope is lost: It is plainly clear that q can be approximated by a nonnegative combination of non-negative k-juntas. Furthermore, an approximation of this form would be just as goodfor us in the arguments that follow. Thus another possible direction for improving our lower bounds signiﬁcantly would be to prove a variant of Lemma 3.3 using an approximation by convex combinations of non-negative juntas, such that one achieves a strong form of decay on the Fourier coeﬃcients.

Some improvement is possible in this case: In the setting of Lemma 3.3, one can achieve a non-negativecombination of k-juntas with k = O(td/γ) (as opposed to γ2); see [LRS15, §7]. But this approach too reaches a bottleneck: Suppose that m divides n and partition [n] = S1 ∪ S2 ∪ ··· ∪ Sn/m where |Si| = m. Consider functions of the form q(x) = f χS1(x),χS2(x),... ,χSn/m(x) where χS(x) = i∈S xi is the corresponding Fourier character and f : {−1,1}n/m → R 0 is a function. The eﬀect of this operation is to lift the low-degree Fourier coeﬃcients of f to higher-degree coeﬃcients of q, cutting oﬀ the hope for a strong form of decay. For instance, if m = √n and f is the majority density on n/m = √n bits (as in (3.2)).

![image 25](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile25.png>)

![image 26](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile26.png>)

### 3.2 Random restrictions

We ﬁrst recall the following standard estimates (see, e.g., [McD98]). Suppose X1,...,Xn are i.i.d {0,1} random variables with E[Xi] = p. Then,

 

  1 − e−pn/8 . (3.3)

n

pn 2

Xi

P

![image 27](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile27.png>)

i=1

Furthermore,

 

 

 



n

n t · pt (pn)t (3.4)

Xi = t

Xi t

P

P

 S∈(nt)

i∈S

i=1

- Lemma 3.5. For any d ∈ N, the following holds. Let Q be a collection of densities


q: {−1,1}n → R 0 such that the corresponding measures µq have entropy at least n − t. If |Q| nd/2, then for all integers m with 3 m n/4, there exists a set S ⊆ [n] such that

- – |S| = m


- – For each q ∈ Q, there exists a set of at most d coordinates J(q) ⊆ S such that under


the distribution µq, all d-wise correlations in S − J(q) are small. Quantitatively, we have

1/2

16mtd √n

∀α ⊆ S,α J(q),|α| d

|qˆ(α)|

![image 28](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile28.png>)

![image 29](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile29.png>)

Proof. We will sample the set S ⊆ [n] by including each element independently with probability 2m/n, then argue that with non-zero probability, both the conditions on S hold.

First, by (3.3), we have |S| m with probability at least 1 − e−m/4 > 1/2. Fix γ = 16√mtdn

1/2

. By Lemma 3.3, for each q ∈ Q there exists a set J′(q) of at most 2γtd2

![image 30](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile30.png>)

![image 31](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile31.png>)

√n 8m coordinates such that for all subsets α J′(q) with |α| d, we have

![image 32](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile32.png>)

![image 33](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile33.png>)

![image 34](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile34.png>)

|qˆ(α)| γ.

The set J(q) for a distribution q is given by J(q) = J′(q) ∩ S. By (3.4), we can write

√n 8m

d 1 4dnd/2

d 2m n ·

![image 35](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile35.png>)

2m n · |J′(q)|

P |J′(q) ∩ S| d

.

![image 36](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile36.png>)

![image 37](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile37.png>)

![image 38](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile38.png>)

![image 39](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile39.png>)

The existence of the set S follows by taking a union bound over all the |Q| nd/2 densities in the family Q. Note that we have concluded with |S| m, but we can remove some elements from S to achieve |S| = m.

### 3.3 Proof of Main Theorem

In this subsection, we will prove Theorem 3.1 and Theorem 3.2. Let m n be parameters m,n ∈ N to be chosen later. Consider an instance ℑ0 of Max-Πm. Recalling (2.3), let E˜ be a corresponding optimal d-ℓ.e.f., i.e. such that E˜ [ℑ0] = SAd(ℑ0).

Suppose that L is an LP relaxation of size at most R nd/2 for Max-Πn. Our goal is to show that there exists an instance ℑ that is a “shift” of ℑ0, and a value εn > 0 such that L(ℑ) SAd(ℑ0) − εn, with εn → 0 as n → ∞. By “shift,” we mean a planting of the instance ℑ0 on some subset of the variables {1,2,...,n}. Since opt(ℑ) = opt(ℑ0), we will conclude our proof by taking εn → 0.

By Theorem 2.3, there are densities q1,q2,...,qR : {−1,1}n → R 0 such that for every Max-Πn instance ℑ, we have

R

L(ℑ) − ℑ = λ0(ℑ) +

λi(ℑ)qi , (3.5)

i=1

for some non-negative numbers λi(ℑ) depending on ℑ. For some t 0 to be chosen later, let

Qt = {1 i R : qi ∞ 2t}.

Observing that the left-hand side of (3.5) is pointwise at most 1, for any i Qt, we must have λi(ℑ) 2−t for every instance ℑ. At this point, one should also observe that Ri=0 λi(ℑ) 1 by taking expectations over both sides of (3.5).

If i ∈ Qt, then since qi ∞ 2t, we can lower bound the entropy of µqi as follows,





2n qi ∞

2n qi(x)

2n qi ∞

qi(x) 2n

qi(x) 2n

n − t.

· log

H(µqi) =

= log

log





![image 40](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile40.png>)

![image 41](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile41.png>)

![image 42](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile42.png>)

![image 43](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile43.png>)

![image 44](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile44.png>)

x∈{−1,1}n

x∈{−1,1}n

Apply Lemma 3.5 to the set of densities with index in Qt, and let S ⊆ [n] with |S| = m be the subset whose existence is guaranteed. Let ℑS denote the instance ℑ0 planted on the subset S, and similarly let E˜ S be the Sherali–Adams functional E˜ planted on S. Equation (3.5) gives us a representation of the form

L(ℑS) − ℑS = λ0(ℑS) +

R

λi(ℑS)qi , (3.6)

i=1

For each i ∈ Qt, let qSi = α⊆S qˆi(α)χα. Observe that qSi is the conditional density on the variables in S (equivalently, we obtain qSi by averaging over all variables outside S). By our application of Lemma 3.5, we can write qSi = q˜Si + ei

1/2

where q˜Si = α⊆J(qi)∩S qˆi(α)χα is a non-negative d-junta and |eˆi(α)| 16√mtdn

for all |α| d.

![image 45](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile45.png>)

![image 46](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile46.png>)

Using the fact that E˜ S only dependson variables in S, we have E˜ S(qi) = E˜ S(qSi ) for all i ∈ Qt. Also observe that for i Qt, we have |E˜ S(qi)| E ˜ S ∞ md , ﬁrst using Eqi = 1 and then using property (iii) of Lemma 2.4. Now we apply E˜ S to both sides of (3.6) to obtain

λi(ℑS)E˜ S(qSi ) +

λi(ℑS)E˜ S(qi)

L(ℑS) − SAd(ℑ0) = λ0(ℑS) +

i∈Qt

i Qt

λi(ℑS) E ˜ S(q˜Si ) + E˜ S(ei) − E ˜ S ∞

λi(ℑS)

i∈Qt

i Qt

m d

nd/22−t ,

λi(ℑS)E˜ S(ei) −

i∈Qt

where in the ﬁnal line we have used the fact that q˜Si is a non-negative d-junta (along with property (i) of Lemma 2.4), the fact that λi(ℑS) 2−t for i Qt, and our assumption that the total number of indices i ∈ {1,2,... ,R} is at most nd/2.

Finally, it remains to observe that

|E˜ S(ei)|

|E˜ S[χα]| · |eˆi(α)|

α⊆S

m d

16mtd √n

![image 47](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile47.png>)

![image 48](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile48.png>)

1/2

, (3.7)

where we have employed property (ii) of Lemma 2.4. Plugging this estimate into the preceding inequality yields

m d

L(ℑS) − SAd(ℑ0) −

16mtd √n

![image 49](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile49.png>)

![image 50](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile50.png>)

1/2

−

m d

nd/22−t .

If we set t = dlog2 n, then L(ℑS) SAd(ℑ0) − εn, where

 

  . (3.8)

![image 51](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile51.png>)

md mdlogn n1/4

εn = O

![image 52](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile52.png>)

Clearly for m,d ﬁxed, we have εn → 0 as n → ∞, completing the proof of

- Theorem 3.1.


- Proof of Theorem 3.2. Fix an instance size m and put d = f(m). In the preceding


argument, require that n grows like m10d = m10f(m) so that εn = o(1) (see (3.8)). The lower bound achieved is nd/2 m5f(m)2.

### 3.4 Nonnegative rank

The lowerbounds of Theorem 3.1 can be stated equivalently in terms of nonnegative rank. We recall that the nonnegative rank of a nonnegative matrix A ∈ Rm×n

+

is deﬁned by rank+(A) = min r : Aij = ui,vj for some {ui,vj} ⊆ Rr+ .

Fix n 1. Let M = (MG,x) be the matrix indexed by n-vertex Max Cut instances with Max Cut value at most s (e.g., s = 1/2 + γ) and bipartitions x ∈ {±1}n such that

MG,x = c − G(x), where G(x) denotes the fraction of edges crossing the bipartition corresponding to x. A corollary of Theorem 3.1 is that rank+(M) nΩ

logn

![image 53](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile53.png>)

log logn . Deﬁne for ε > 0, the ε-smooth nonnegative rank of a matrix A as

rank+,ε(A) := min rank+(A′) | (1 − ε)Aij A′ij (1 + ε)Aij ∀i, j ,

Our main result shows that M has superpolynomial nonnegative rank. We claim that M has only polynomial nonnegative approximate rank for every ﬁxed ε > 0. (Since the entries of M are bounded from above and bounded away from

- 0, the notions of approximate and smooth nonnegative rank coincide.) In order to demonstrate that M has small approximate nonnegative rank, for each t ∈ N,


we will exhibit a matrix M′ that approximates M well, M′G,x − MG,x 2−Ω(t) for all G and x, but has a small nonnegative rank, i.e., rank+(M′) nO(t). To this end, we will use the reformulation of nonnegative rank as a communication model discussed in Section 2. Consider the following communication protocol between Alice and Bob:

- – Alice receives as input an n-vertex graph G with Max Cut value at most s.
- – Bob receives as input a bipartition x ∈ {±1}n.
- – Alice chooses t edges e1,...,et of G independently at random and sends the endpoints of the sampled edges to Bob.
- – Bob computes what fraction θ of the edges e1,...,et cross the bipartition x. If θ > c, then Bob outputs 0 else Bob outputs c − θ.


LetM′ bethematrixcomputedbytheaboveprotocol,i.e.,M′G,x istheexpected value of Bob’s output when Alice receives the graph G and Bob receives x as input. This protocol yields a rank-2t·2 logn nonnegative factorization of the matrix M′, as follows.

Let θG,x be the random variable given by Bob’s output when the inputs for Alice and Bob are G and x, respectively. Then, M′G,x = c − EθG,x for all G and x.

At the same time, we have

MG,x = c − E θG,x − δG,x , where

δG,x 2P[θG,x > c]. In words, the discrepancy between the computed matrix M′ and the target

matrix M is accounted for by the probability of the events {θG,x > c}. However, since G(x) s < c is bounded away from c by some constant, a standard Chernoﬀ bound yields

P[θG,x > c] 2−Ω(t) , for all G and x. It follows that the matrix M′ satisﬁes rank+(M′) nO(t) and maxG,x|M′G,x − MG,x| 2−Ω(t).

## 4 Symmetric linear programs

We will now prove the following theorem relating Sherali–Adams gaps to those for symmetric LPs for Max Cut. While this connection holds more generally for max-CSP problems, we will focus on Max Cut for clarity. Recent work has extended these ideas to problems like TSP [LRST14], and also to a connection between symmetric SDPs and the Sum-of-Squares hierarchy [LRST14, FSP13].

- Theorem 4.1. Fix a k-ary CSP Max-Π over the boolean domain. Suppose that, for some numbers m,d > 0, the d-round Sherali–Adams relaxation for Max-Πm cannot


achieve a (c,s)-approximation. Then no symmetric LP of size nd can achieve a (c,s)-approximation on Max-Πn where n = 2m.

We note here that the Sherali-Adams hierarchy produces symmetric linear programs. Hence,theaboveresultcanbeviewedasassertingthatSherali-Adams hierarchy is complete for the class of symmetric linear programs.

By appealing to the known Sherali–Adams gaps for Max Cut [CMM09] and Max 2-Sat, Max 3-Sat [Sch08], we get the same integrality gaps for arbitrary symmetric LPs. For example, in the case of Max Cut, we obtain the following lower bound.

Corollary 4.2. For every ε > 0, there exists δ > 0 such that no symmetric linear program of size 2nδ yields a (1 − ε, 21 + ε)-approximation for Max Cut.

![image 54](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile54.png>)

In order to prove Theorem 4.1, we will need the following characterization of symmetric function families.

- Lemma 4.3. Suppose a family of functions Q = {qi : {−1,1}n → R : i = 1,2,...,R} is


closed under the action of Sym(n). If R < nd for d < n/4, then each function qi depends only on a subset Ji ⊆ [n] of at most d coordinates and possibly the value of the sum

n j=1 xj.

Proof. Here we will need a few basic notions about group actions. A group G acts on a universe X, if each element ∈ G permutes the elements of the universe X, and this action commutes with the group operation. Formally, a group action is deﬁned by a map ι : G × X → X such that ι( ,ι(h,x)) = ι( h,x) for all ,h ∈ G and x ∈ X. For convenience, we will denote · x def= ι( ,x).

For an element x ∈ X, its orbit Orb(x) is given by Orb(x) = { · x | ∈ G} and its stabilizer is given by Stab(x) = { ∈ G | · x = x}. A basic fact from group theory is that for every action of a ﬁnite group G and every x ∈ X, it holds that |Stab(x)| · |Orb(x)| = |G|.

The group Sym(n) of all permutations on n elements acts on the space of functions over {−1,1}n by permutation of the coordinates. Let Orb(f) denote the orbit of a function f under the action of Sym(n), and let Stab(f) denote the stabilizer of f. Since Q is closed under this action, it contains the orbits of each of the functions q1,...,qR.

This implies that for each i ∈ [R], we have |Orb(qi)| < nd . Since |Orb(qi)| · |Stab(qi)| = |Sym(n)| = n!, we conclude that for each i ∈ [R], |Stab(qi)| d!(n−d)!. At this point, we appeal to the following group theoretic fact that we borrow from the work of Yannakakis [Yan91].

- Lemma 4.4 ([Yan91, Claim 2]). Let H be a group of permutations whose index in


Sym(n) is at most nd for some d < n/4. Then there exists a set J ⊆ {1,2,... ,n} of size

- at most d such that H contains all even permutations that ﬁx the elements of J.


By Lemma 4.4, the stabilizer subgroup Stab(qi) contains all even permutations that ﬁx a subset of coordinates Ji with |Ji| d. We claim that Stab(qi) contains all permutations that ﬁx the coordinates in Ji. We know that for every x ∈ {−1,1}n, and every even permutation σ ∈ Sym(J¯i) we have, qi(x) = qi(σx). Here, we use Sym(J¯i) to denote the subgroup of Sym(n) ﬁxing elements in Ji.

For every x ∈ {−1,1}n, there will be two coordinates a,b ∈ J¯i such that xa = xb. Let πab denote the transposition that swaps a and b. Since πab(x) = x, we have qi(πab(x)) = qi(x). So for even permutations σ ∈ Sym(J¯i),

qi(σπabx) = qi(πabx) = qi(x).

As σ varies over all even permutations in Sym(J¯i), σπab varies over all odd permutations in Sym(J¯i), leading to the conclusion that Sym(J¯i) ⊆ Stab(qi).

This symmetry of the function qi(x) implies that it depends only on the assignment to coordinates in Ji and the hamming weight of the assignment to coordinates in J¯i, i.e. the value nj=1 xj − j∈Ji xj. This shows that qi is a function depending only on the coordinates in Ji and the value i∈[n] xi.

We are now in position to prove the main theorem of this section.

- Proof of Theorem 4.1. Let L be a symmetric LP relaxation for Max-Πn of size


R nd . Supposing that this relaxation achieves a (c,s)-approximation, we will derive a contradiction.

By applying Theorem 2.3, there exists a family of functions Q = {q1,...,qR: {−1,1}n → R 0} such that for every instance ℑ of Max-Πn with opt(ℑ) s, we have

R

c − ℑ = λ0 +

λiqi .

i=1

for some non-negative weights {λi}Ri=0. Moreover, the family of functions Q is invariant under the action of Sym(n). Therefore, by Lemma 4.3, each of the

functions qi ∈ Q depends on a set Ji of at most d coordinates and possibly the value ni=1 xi.

Fix an instance ℑ of Max-Πm on which thed-round Sherali–Adams relaxation fails to achieve a (c,s)-approximation, i.e.,

opt(ℑ) s and SAd(ℑ) > c.

For n = 2m, construct an instance ℑ′ of Max-Πn by including m additional dummy variables in ℑ with no constraints among them. Concretely, if X1,...,Xn are variables in ℑ′, then restricted to the variables X1,...,Xm, the constraints are identical to ℑ while there are no constraints among Xm+1,...,Xn.

For an assignment x ∈ {−1,1}n, we will denote xA = (x1,...,xm) and xB = (xm+1,...,xn). In this notation, it is easy to see that for every assignment x,

ℑ′(x) = ℑ(xA). By construction, we have opt(ℑ′) = opt(ℑ) s. Since the symmetric LP

relaxation L yields a (c,s)-approximation to Max-Πn, there exist {λi 0}Ri=0 such that

R

c − ℑ′ = λ0 +

λiqi .

i=1

Using ℑ(x) = ℑ(xA), we can rewrite the above identity as,

R

c − ℑ(xA) = λ0 +

λiqi(xA,xB).

i=1

Deﬁne hi : {−1,1}m → R 0 as hi(x) = qi(x,−x). Setting xB = −xA in the above identity, we arrive at

c − ℑ(xA) = λ0 +

λihi(xA). (4.1)

i

Recall that each of the functions qi dependson a subset Ji of at most d coordinates and possibly the value of ni=1 xi. This implies that hi(x) = qi(x,−x) is a d-junta, since the sum of all the coordinates of (x,−x) is always equal to 0. In particular, the identity in (4.1) expresses the function c − ℑ as a non-negative combination of d-juntas.

LetE˜ denotethed-round Sherali–Adams functional fortheinstanceℑ. Apply the E˜ functional to both sides of (4.1) to obtain a contradiction. By Lemma 2.4 and the fact that each hi is a non-negative d-junta, we have E˜ [hi] 0. On the other hand, the left hand side E˜ (c − ℑ) = c − SAd(ℑ) < 0.

## 5 Conclusion

We have shown that for constraint satisfaction problems, there is an intimate relationship between general polynomial-sized linear programs and those arising from O(1) rounds of the Sherali–Adams hierarchy. There are a few natural questions that readily suggest themselves.

Firstly, our quantitative bounds are far from optimal. For instance, it is known that the integrality gap of 1/2 + ε for Max Cut persists for ncε rounds of Sherali-Adams hierarchy, where cε is some constant depending on ε [CMM09], while we are only able to prove an integrality gap for LPs of size no(

logn

log logn). This is due to the factor of md appearing in our Fourier estimate (3.7).

![image 55](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile55.png>)

- Question 5.1. Is it the case that for approximating (boolean) max-CSP problems on n variables, linear programs of size R(n) are only as powerful as those arising from poly(loglogR(nn)) rounds of the Sherali–Adams hierarchy?

![image 56](<2013-chan-approximate-constraint-satisfaction-requires_images/imageFile56.png>)

Secondly, given the connection for linear programs, it is natural to suspect that a similar phenomenon holds for SDPs.

- Question 5.2. For max-CSP problems, is there a connection between the efﬁcacy of general SDPs and those from the Sum-of-Squares SDP hierarchy [Las01, Par00]?


As mentioned in the introduction, recent work [LRS15] yields a positive solution to this question, although the approach has similar limitations to those highlighted in Question 5.1.

Finally, our techniques have made very strong use of the product structure on the space of feasible assignments for CSPs. One might hope to extend these connections to other types of problems like TSP and ﬁnding maximum-weight perfect matchings in general graphs [Rot14, Yan91] or approximations for vertex cover. See [BPZ15] for progress on the latter problem.

### Acknowledgements

We thank the anonymous referees for many useful suggestionsand observations.

S. O. Chan was supported by NSF grants CCF-1118083 and CCF-1017403. P. Raghavendra was supported by NSF Career Award CCF-1343104 and an Alfred P. Sloan Fellowship. J. R. Lee was supported by NSF grants CCF-1217256 and CCF-0905626. D. Steurer was supported by NSF grants, an Alfred P. Sloan Fellowship, and a Microsoft Research Faculty Fellowship.

## References

[ABL02] SanjeevArora, BélaBollobás, and LászlóLovász, Provingintegrality gaps without knowing the linear program, FOCS, 2002, pp. 313–322. 1, 3

[ABLT06] Sanjeev Arora, Béla Bollobás, László Lovász, and Iannis Tourlakis, Proving integrality gaps without knowing the linear program, Theory of Computing 2 (2006), 19–51. 3

[BFPS12] Gábor Braun, Samuel Fiorini, Sebastian Pokutta, and David Steurer, Approximation limits of linear programs (beyond hierarchies), FOCS, 2012, pp. 480–489. 2, 3, 4, 9

[BGMT12] Siavosh Benabbas, Konstantinos Georgiou, Avner Magen, and Madhur Tulsiani, SDP gaps from pairwise independence, Theory of Computing 8 (2012), no. 12, 269–289. 4

[BM13] Mark Braverman and Ankur Moitra, An information complexity approach to extended formulations, STOC, ACM, 2013, pp. 161–170. 3, 4

[BPZ15] GáborBraun, SebastianPokutta,andDanielZink, Inapproximability of combinatorial problems via small LPs and SDPs, STOC (New York, NY, USA), ACM, 2015, pp. 107–116. 3, 23

[Cha02] Mei-Chu Chang, A polynomial bound in Freiman’s theorem, Duke Math. J. 113 (2002), no. 3, 399–419. MR 1909605 (2003d:11151) 14

[CMM09] Moses Charikar, Konstantin Makarychev, and Yury Makarychev, Integrality gaps for Sherali-Adams relaxations, STOC, ACM, 2009, pp. 283–292. 3, 13, 14, 20, 22, 27, 28

[FdlVKM07] Wenceslas Fernández de la Vega and Claire Kenyon-Mathieu, Linear programming relaxations of Maxcut, SODA, 2007, pp. 53–61. 3, 13, 27, 28

[FFGT11] Yuri Faenza, Samuel Fiorini, Roland Grappe, and Hans Raj Tiwary, Extended formulations, non-negative factorizations and randomized communication protocols, arXiv:1105.4127, 2011. 11

[FMP+12] Samuel Fiorini, Serge Massar, Sebastian Pokutta, Hans Raj Tiwary, and Ronald de Wolf, Linear vs. semideﬁnite extended formulations: exponential separation and strong lower bounds, STOC, 2012, pp. 95– 106. 3, 4, 8

[FSP13] HamzaFawzi, James Saunderson,and PabloA.Parrilo, Equivariant semideﬁnite lifts and sum-of-squares hierarchies, arXiv:1312.6662, 2013. 2, 19

[Gri01] Dima Grigoriev, Linear lower bound on degrees of Positivstellensatz calculus proofs for the parity, Theoret. Comput. Sci. 259 (2001), no. 12, 613–622. MR 1832812 (2002e:03093) 4

[GW95] Michel X. Goemans and David P. Williamson, Improved approximation algorithms for maximum cut and satisﬁability problems using semideﬁnite programming, Journal of the ACM 42 (1995), 1115–1145. 2

[Hås01] Johan Håstad, Some optimal inapproximability results, Journal of the ACM 48 (2001), no. 4, 798–859. MR 2144931 (2006c:68066) 2

[IMR14] Russell Impagliazzo, Cristopher Moore, and Alexander Russell, An entropic proof of Chang’s inequality, SIAM J. Discrete Math. 28

(2014), no. 1, 173–176. MR 3162401 14

[KMSY14] Gillat Kol, Shay Moran, Amir Shpilka, and Amir Yehudayoﬀ, Approximate nonnegative rank is equivalent to the smooth rectangle bound., Electronic Colloquium on Computational Complexity (ECCC), vol. 21, 2014, p. 46. 4

[KPT10] Volker Kaibel, Kanstantsin Pashkovich, and Dirk Oliver Theis, Symmetry matters for the sizes of extended formulations, IPCO, 2010, pp. 135–148. 9

[Las01] Jean B. Lasserre, Global optimization with polynomials and the problem ofmoments, SIAMJ.Optim.11(2000/01), no.3,796–817.MR1814045 (2002b:90054) 22

[Lau03] Monique Laurent, A comparison of the Sherali-Adams, LovászSchrijver, and Lasserre relaxations for 0-1 programming, Math. Oper. Res. (2003), 470–496. 3, 11

[LRS15] James R. Lee, Prasad Raghavendra, and David Steurer, Lower bounds onthe size of semideﬁnite programming relaxations, STOC (New York, NY, USA), ACM, 2015, pp. 567–576. 2, 7, 14, 15, 23

[LRST14] James R. Lee, Prasad Raghavendra, David Steurer, and Ning Tan, On the power of symmetric LP and SDP relaxations, CCC, IEEE, 2014. 2, 19

[LS91] László Lovász and Alexander Schrijver, Cones of matrices and setfunctions and 0-1 optimization, SIAM J. Optim. 1 (1991), 166–190. 1

[McD98] Colin McDiarmid, Concentration, Probabilistic methods for algorithmic discrete mathematics, Algorithms Combin., vol. 16, Springer, Berlin, 1998, pp. 195–248. MR 1678578 (2000d:60032) 15

[Par00] Pablo Parrilo, Structured semideﬁnite programs and semialgebraic geometry methods in robustness and optimization, Ph.D. thesis, California Institute of Technology, 2000. 22

[Pas12] Kanstantsin Pashkovich, Extended formulations for combinatorial polytopes, Ph.D. thesis, Magdeburg Universität, 2012. 9

[Rot14] Thomas Rothvoß, The matching polytope has exponential extension complexity, STOC (New York, NY, USA), ACM, 2014, pp. 263–272. 3, 4, 23

[SA90] Hanif D. Sherali and Warren P. Adams, A hierarchy of relaxations between the continuous and convex hull representations for zero-one programming problems, SIAM J. Discrete Math. 3 (1990), 411–430. 1, 27, 28

[Sch03] Alexander Schrijver, Combinatorial optimization. Polyhedra and eﬃciency. Vol. A, Algorithms and Combinatorics, vol. 24, SpringerVerlag, Berlin, 2003, Paths, ﬂows, matchings, Chapters 1–38. MR 1956924 (2004b:90004a) 10

[Sch08] Grant Schoenebeck, Linear level Lasserre lower bounds for certain kCSPs, FOCS, IEEE, 2008, pp. 593–602. 4, 13, 14, 20

[Tre12] Luca Trevisan, Max cut and the smallest eigenvalue, SIAM J. Comput.

41 (2012), no. 6, 1769–1786. MR 3029271 2

[Vaz01] Vijay V. Vazirani, Approximation algorithms, Springer-Verlag, Berlin,

2001. MR 1851303 (2002h:68001) 1

[WS11] David P. Williamson and David B. Shmoys, The design of approximation algorithms, Cambridge University Press, Cambridge, 2011. 1

[Yan91] Mihalis Yannakakis, Expressing combinatorial optimization problems by linear programs, J. Comput. System Sci. 43 (1991), no. 3, 441–466. 1, 2, 3, 20, 23

## A What is Sherali–Adams?

Our deﬁnition of Sherali–Adams relaxation diﬀers from the deﬁnition in prior works (in particular, the works that proved lower bounds on the size of SheraliAdams relaxations for approximating CSPs) [SA90, FdlVKM07, CMM09]. This discrepancy stems from the fact that traditionally LP hierarchies like Sherali– Adams are applied to integer linear programming formulations of a problem, whereas our relaxations can be viewed as applying the analogous reasoning to a more direct formulation of the problem. It turns out that the latter approach typically leads to relaxations that are easier to describe and a-priori more powerful.

We will argue that the two versions of Sherali–Adams are equivalent for the problems we consider, in the sense that each relaxation in one hierarchy is captured by a relaxation in the other hierarchy of comparable size (at most a polynomial factor more constraints).

We remark that our relaxations are equivalent to the viewpoint of Sherali– Adams as a collection of mutually-consistent “local distributions over assignments.” This viewpoint was used in previous works for proving lower bounds. These previous works show that this viewpoint captures the power of Sherali– Adams. We will argue that this viewpoint is indeed equivalent to the Sherali– Adams hierarchy.

### A.1 Edge-based Sherali–Adams relaxations for Max Cut

The cut polytope CUTn is the convex hull of all vectors y ∈ {0,1}(n2) such that there exists a bipartition x ∈ {±1}n with yi,j = 1{xi xj} for all i j ∈ [n]. We can formulate Max Cut as the problem of optimizing a linear function of the form

ij∈E(G) yi,j over CUTn for a graph G. The standard LP relaxation of CUTn is the metric polytope METRICn, which consists of all vectors y ∈ [0,1](n2) that satisfy the inequalities yi,j yi,k + yk,j and yi,j + yi,k + yk,j 2 for all i, j,k ∈ [n]. This O(n3)size LP relaxation corresponds to an exact integer linear programming (ILP) formulation in the sense that the convex hull of the integer vectors METRICn ∩ {0,1}(n2) is precisely the cut polytope CUTn. In our notation, the level-r Sherali– Adams relaxation of this ILP formulation consists of all linear functionals E˜ on L2({0,1}(n2)) such that E˜ 1 = 1 and E˜ f · ℓ 0 for every non-negative r-junta f on {0,1}(n2) and every linear function ℓ on {0,1}(n2) corresponding to one of the deﬁning linear inequalities of METRICn, i.e., ℓ is of the form yi,j, 1 − yi,j, yi,k + yk,j − yi,j, or 2 − yi,j − yi,k − yk,j for some i, j,k ∈ [n]. The value of the level-r Sherali–Adams relaxation for a Max Cut instance G is the maximum value of E˜ ij∈E(G) yi,j over all linear functionals E˜ that satisfy the previous conditions. (From our description it is not immediately clear that this optimization problem has a small linear programming formulation. However note that nO(r) linear

inequalities are enough to deﬁne the set of all admissible linear functionals E˜ . Hence, we can reduce this problem to a linear program of size nO(r). It’s also possible, but somewhat cumbersome, to describe this small linear program explicitly [SA90, FdlVKM07, CMM09].)

A.1.1 Why is this hierarchy of relaxations equivalent to the previously described hierarchy?

Let G be any graph. First, consider any k-local pseudo-expectation E˜ x as deﬁned before. We will construct an equivalent linear functional E˜ y for the level-r Sherali–Adams relaxation with r = k/2 − 3. Recall that E˜ x is a linear functional on L2({±1}n) such that E˜ x 1 = 1 and E˜ x f 0 for every nonnegative k-junta f. We deﬁne a linear functional E˜ y on L2({0,1}(n2)) as follows,

E˜ y f = E˜ x(f ◦ ϕ), where ϕ is the function that maps any bipartition x ∈ {±1}n to the corresponding vector {0,1}(n2), i.e., ϕ(x)i,j = 1{xi xj}. (Note that algebraically ϕ(x)i,j = (1 − xixj)/2.) This linear functional satisﬁes E˜ y 1 = E˜ x 1 = 1 and E˜ y i,j∈E(G) yi,j = E˜ x ij∈E(G)(1 − xixj)/2. Consider any nonnegative r-junta f over {0,1}(n2) and any facet deﬁning linear inequality {ℓ 0} for METRICn. We are to show E˜ y f · ℓ = E˜ x(f ◦ ϕ) · (ℓ ◦ ϕ) 0. Since {ℓ 0} is a valid inequality for the vertices of CUTn, we have ℓ◦ϕ 0 over {±1}n. Therefore, (f ◦ϕ)·(ℓ◦ϕ) is nonnegative over {±1}n. Notice that each facet deﬁning linear inequality {ℓ 0} for METRICn depends only on three yij variables, and therefore ℓ ◦ φ depends on at most 6 of the variables {x1,...,xn}. Therefore, the function (f ◦φ)·(ℓ◦φ) depends onat most2r+6 k of thevariables {x1,...,xn}. Itfollowsthat E˜ x(f ◦ϕ)·(ℓ◦ϕ) 0 as required.

Next, consider any linear functional E˜ y for the level-r Sherali–Adams relaxation. We will construct an equivalent k-local pseudo-expectation E˜ x for k = r. We deﬁne E˜ x as follows,

E˜ x f = E˜ y(f ◦ ψ), where ψ(y)i = 1 if yi,1 = 0 and ψ(y)i = −1 if yi,1 = 1. In words, we assign

- 1 to all vertices i on the same side of the bipartition as vertex 1 and −1 to all vertices on the other side. (Algebraically, ψ is deﬁned by ψ(y)i = 1 − 2yi,1.) This linear functional satisﬁes E˜ x 1 = E˜ y 1 = 1 and E˜ x f 0 for every nonnegative k-junta f (because f ◦ ψ is also a nonnegative k-junta). It remains to show that


E˜ x ij∈E(G)(1 − xixj)/2 = E˜ y ij∈E(G) yi,j. By our construction of the functional E˜ x, we have E˜ x(1 − xixj)/2 = E˜ y(yi,1 − yj,1)2 and thus it’s enough to establish E˜ y(yi,1 − yj,1)2 − yi,j = 0. To simplify notation let us assume i = 2 and j = 3. Let 1000,...,1111 be theindicators fortheeightpossible assignments for thevariables y1,2, y1,3, y2,3. Since 1 = 1000 + ··· + 1111 as functions over {0,1}(n2), it is enough

to verify that E˜ y 1abc · (y1,2 − y1,3)2 − y1,2 = 0 for all a,b,c ∈ {0,1}. Note that the identity (y1,2 − y1,3)2 = y2,3 holds if y is one of the vertices of CUTn. (In words, vertices 2 and 3 are on diﬀerent sides of the bipartition if and only if exactly one of them is on the same side as vertex 1.) We claim that either E˜ y 1abc = 0 or (a,b,c) ∈ CUT3 ∩ {0,1}3. This claim implies the desired identity,

1abc · (y1,2 − y1,3)2 − y2,3

(y1,2 − y1,3)2 − y2,3 =

E˜

E˜

y

y

a,b,c∈{0,1}

E˜

1abc · (a − b)2 − c

=

y

a,b,c∈{0,1}

E˜

1abc · (a − b)2 − c (by claim)

=

y

(a,b,c)∈CUT3∩{0,1}3

= 0

(The second step uses that 1abc · (y1,2 − y1,3)2 − y2,3 = 1abc · (a − b)2 − c for all y.) It remains to prove the claim. Since CUTn ∩ {0,1}n = METRICn ∩ {0,1}n, it is enough to show that for every a,b,c ∈ {0,1} and every valid linear inequality {ℓ 0} for METRIC3 either E˜ y 1abc = 0 or ℓ(a,b,c) 0. Indeed, since 1abc is a nonnegative 3-junta and {ℓ(y1,2, y1,3, y2,3)} is a valid linear inequality for METRICn,

0 E ˜

1abc · ℓ(y1,2, y1,3, y2,3) = E˜ y

1abc · ℓ(a,b,c),

y

which means that either E˜ y 1abc = 0 or ℓ(a,b,c) 0. (The second step uses that 1abc · ℓ(y1,2, y1,3, y2,3) = 1abc · ℓ(a,b,c) for all y.)

