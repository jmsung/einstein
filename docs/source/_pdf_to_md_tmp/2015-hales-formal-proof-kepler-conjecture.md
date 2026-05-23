arXiv:1501.02155v1[math.MG]9Jan2015

# A FORMAL PROOF OF THE KEPLER CONJECTURE

THOMAS HALES, MARK ADAMS, GERTRUD BAUER, DANG TAT DAT, JOHN HARRISON, HOANG LE TRUONG, CEZARY KALISZYK, VICTOR MAGRON, SEAN MCLAUGHLIN, NGUYEN TAT THANG, NGUYEN QUANG TRUONG, TOBIAS NIPKOW, STEVEN OBUA, JOSEPH PLESO, JASON RUTE, ALEXEY SOLOVYEV, TA THI HOAI AN, TRAN NAM TRUNG, TRIEU THI DIEP, JOSEF URBAN, VU KHAC KY, ROLAND ZUMKELLER,

Abstract. This article describes a formal proof of the Kepler conjecture on dense sphere packings in a combination of the HOL Light and Isabelle proof assistants. This paper constitutes the oﬃcial published account of the now completed Flyspeck project.

1. Introduction

The booklet Six-Cornered Snowﬂake, which was written by Kepler in 1611, contains the statement of what is now known as the Kepler conjecture: no packing of congruent balls in Euclidean three-space has density greater than that of the face-centered cubic packing [27]. This conjecture is the oldest problem in discrete geometry. The Kepler conjecture forms part of Hilbert’s 18th problem, which raises questions about space groups, anisohedral tilings, and packings in Euclidean space. Hilbert’s questions about space groups and anisohedral tiles were answered by Bieberbach in 1912 and Reinhardt in 1928. Starting in the 1950s, L. Fejes To´th gave a coherent proof strategy for the Kepler conjecture and eventually suggested that computers might be used to study the problem [6]. The truth of the Kepler conjecture was established by Ferguson and Hales in 1998, but their proof was not published in full until 2006 [18].

The delay in publicationwas caused by the diﬃculties that the referees had in verifying a complex computer proof. Lagarias has described the review process [30]. He writes, “The nature of this proof . . . makes it hard for humans to check every step reliably. . . . [D]etailed checkingof many speciﬁc assertions found them to be essentially correct in every case. The result of the reviewing process produced in these reviewers a strong degree of conviction of the essential correctness of this proof approach, and that the reduction method led to nonlinear programming problems of tractable size.” In the end, the proof was published without complete certiﬁcation from the referees.

At the Joint Math Meetings in Baltimore in January 2003, Hales announced a project to give a formal proof of the Kepler conjecture and later published a project description [17]. The project is called Flyspeck, an expansion of the acronym FPK, for the Formal Proof of the Kepler conjecture. The project has formalized both the traditional text parts of the proofand the parts of the proof that are implementedin computer code as calculations. This paper constitutes the oﬃcial published account of the now completed Flyspeck project.

The ﬁrst deﬁnite contribution to the project was the formal veriﬁcation by Bauer and Nipkowof a major piece of computer code that was used in the proof (see Section 7). Major work on the text formalization project started with NSF funding in 2008. An international conference on formal proofs and the Flyspeck project at the Institute of Math (VAST) in Hanoi in 2009 transformed the project into a large international collaboration. The PhD theses of Bauer [4], Obua [39], Zumkeller [48], Magron [32], and Solovyev [43] have been

1

Hales et al. A formal proof of the Kepler conjecture directly related to this project. The book “Dense Sphere Packings” gives the mathematical details of the proof that was formalized [14]. This article focuses on the components of the formalization project, rather than the mathematical details of the proof.

![image 25](<2015-hales-formal-proof-kepler-conjecture_images/imageFile25.png>)

The Flyspeck project has roughly similar size and complexity as other major formalization projects such as the Feit-Thompson odd order theorem [9], the CompCert project giving a veriﬁed C compiler [31], and the seL4 project that veriﬁed an operating system micro-kernel [28]. The Flyspeck project might actually set the current record in terms of lines of code in a veriﬁcation project.

The code and documentation for the Flyspeck project are available at a Google code repository devoted to the project [7]. The parts of the project that have been carried out in Isabelle are available from the Archive of Formal Proofs (afp.sf.net). Other required software tools are Subversion (for interactions with the code repository), Isabelle/HOL [37], HOL Light [21], OCaml (the implementation language of HOL Light), the CamlP5 preprocessor (for a syntax extension to OCaml for parsing of mathematical terms), and GLPK (for linear programming) [8].

The main statement in the Kepler conjecture can be formally veriﬁed in about ﬁve hours on a 2 GHz CPU directly from the proof scripts. As described in Section 4.5, the proof scripts of the main statement have been saved in a recorded proof format. In this format, the formal proof of the main statement executes in about forty minutes on a 2 GHz CPU. We encourage readers of this article to make an independentveriﬁcation of this main statement on their computers.

This main statement reduces the Kepler conjecture to three computationally intensive subclaims that are described in Section 3. Two of these subclaims can be checked in less than one day each. The third and most diﬃcult of these subclaims takes about 5000 CPU hours to verify.

2. The HOL Light proof assistant

The formal veriﬁcations have been carried out in the HOL Light and Isabelle proof assistants, with a second veriﬁcation of the main statement in HOL Zero.

HOL Light is one of a family of proof assistants that implement the HOL logic [11]. It is a classical logic based on Church’s typed lambda calculus and has a simple polymorphic type system. For an overview of the deductive system see [23]. There are ten primitive inference rules and three mathematicalaxioms: the axiom of inﬁnity (positing the existence of a function f : X → X that is one-to-onebut not onto), the axiom of extensionality (which states that two functions are equal if their outputs agree on every input), and the axiom of choice. HOL Light has a mechanism that permits the user to extend the system with new constants and new types.

HOL Light is implemented according to a robust software architecture known as the “LCF approach” [10], which uses the type system of its implementation language (OCaml in the case of HOL Light) to ensure that all deduction must ultimately be performed by the logic’s primitive deductive system implemented in a kernel. This design reduces the risk of logical unsoundness to the risk of an error in the kernel (assuming the correct implementation of the architecture).

The kernel of HOL Light is remarkably small, amounting to just a few hundred lines of code. Furthermore, the kernel has been subject to a high degree of scrutiny to guarantee that the underlying logic is consistent and that its implementation in code is free of bugs [29] [13]. This includes a formal veriﬁcation of its own correctness [20]. It is generally held by experts that it is extremely unlikely for the HOL Light proof assistant to create a “false”

2

Hales et al. A formal proof of the Kepler conjecture

![image 42](<2015-hales-formal-proof-kepler-conjecture_images/imageFile42.png>)

theorem, except in unusualcircumstancessuch as a user who intentionally hacksthe system with malicious intent. A formal proof in the HOL Light system is more reliable by orders of magnitude than proofs published through the traditional process of peer review.

One feature that makes HOL Light particularly suitable for the Flyspeck project is its large libraries of formal results for real and complex analysis. Libraries include multivariate (gauge) integration, diﬀerential calculus, transcendental functions, and point-set topology on Rn.

Proof scripts in the HOL Light are written directly as OCaml code and are executed in the OCaml read-eval-print loop. Mathematical terms are expressed in a special syntax, set apart from ordinary OCaml code by backquotes. For example, typed at the OCaml prompt, ‘1‘ equals the successor of zero in the set of natural numbers (deﬁned from the mathematical axiom of inﬁnity in HOL Light). It is not to be conﬂated with the informal 1 in OCaml, which is vulnerable to the usual properties of machine arithmetic.

This article displays various terms that are represented in HOL Light syntax. For the convenience of the reader, we note some of the syntactic conventions of HOL Light. The syntax is expressed entirely with ASCII characters. In particular, the universal quantiﬁer (∀) is written as (!), the existential quantiﬁer (∃) is written (?), the embedding of natural numbers into the real numbers is denoted (&), so that for instance &3 denotes the real number 3.0. The symbol |- (the keyboard approximation for ⊢) appears in front of a statement that is a theorem in the HOL Light system. Other logical symbols are given by keyboard approximations: ==> for =⇒, /\ for ∧, and so forth.

The logic of Isabelle/HOL is similar to that of HOL Light, but it also includes a number of features not available in HOL Light. The logic supports a module system and type classes. The package includes extensive front-end support for the user and an intuitive proof scripting language. Isabelle/HOL supports a form of computationalreﬂection (which is used in the Flyspeck project) that allows executable terms to be exported as ML and executed, with the results of the computation re-integrated in the proof assistant as theorems.

3. The statement

As mentioned in the introduction, the Kepler conjecture asserts that no packing of congruent balls in Euclidean three-space can have density exceeding that of the face-centered cubic packing. That density is π/ √18, or approximately 0.74. The hexagonal-close packing and various packings combining layers from the hexagonal-close packing and the facecentered cubic packing also achieve this bound. The theorem that has been formalized does not make any uniqueness claims.

![image 43](<2015-hales-formal-proof-kepler-conjecture_images/imageFile43.png>)

The density of a packing is deﬁned as a limit of the density obtained within ﬁnite containers, as the size of the container tends to inﬁnity. To make the statement in the formal proof as simple as possible, we formalize a statement about the density of a packing inside a ﬁnite spherical container. This statement contains an error term. The ratio of the error term to the volume of the container tends to zero as the volume of the container tends to inﬁnity. Thus in the limit, we obtain the Kepler conjecture in its traditional form.

As a ratio of volumes, the density of a packing is scale invariant. There is no loss of generality in assuming that the balls in the packing are normalized to have unit length. We identify a packing of balls in R3 with the set V of centers of the balls, so that the distance between distinct elements of V is at least 2, the diameter of a ball. More formally, we have the following theorem that characterizes a packing.

|- packing V <=>

3

Hales et al. A formal proof of the Kepler conjecture

![image 60](<2015-hales-formal-proof-kepler-conjecture_images/imageFile60.png>)

(!u v. u IN V /\ v IN V /\ dist(u,v) < &2 ==> u = v)

This states that V ⊂ R3 is a packing if and only if for every u, v ∈ V, if the distance from u to v is less than 2, then u = v. To ﬁx the meaning of what is to be formalized, we deﬁne the constant the kepler conjecture as follows:

![image 61](<2015-hales-formal-proof-kepler-conjecture_images/imageFile61.png>)

![image 62](<2015-hales-formal-proof-kepler-conjecture_images/imageFile62.png>)

|- the_kepler_conjecture <=> (!V. packing V

==> (?c. !r. &1 <= r

==> &(CARD(V INTER ball(vec 0,r))) <= pi * r pow 3 / sqrt(&18) + c * r pow 2))

In words, we deﬁne the Kepler conjecture to be the following claim: for every packing V, there exists a real number c such that for every real number r ≥ 1, the number of elements of V contained in an open spherical container of radius r centered at the origin is at most

π r3 √18

+ c r2.

![image 63](<2015-hales-formal-proof-kepler-conjecture_images/imageFile63.png>)

![image 64](<2015-hales-formal-proof-kepler-conjecture_images/imageFile64.png>)

An analysis of the proof shows that there exists a small computable constant c that works uniformly for all packings V, but we only formalize the weaker statement that allows c to depend on V. The restriction r ≥ 1, which bounds r away from 0, is needed because there can be arbitrarily small containers whose intersection with V is nonempty.

The proof of the Kepler conjecture relies on a combination of traditional mathematical argument and three separate bodies of computer calculations. The results of the computer calculations have been expressed in precise mathematical terms and speciﬁed formally in HOL Light. The computer calculations are as follows.

- (1) The proof of the Kepler conjecture relies on nearly a thousand nonlinear inequalities. The term the_nonlinear_inequalities in HOL Light is the conjunction of these nonlinear inequalities. See Section 5.
- (2) The combinatorial structure of each possible counterexample to the Kepler conjecture is encoded as a plane graph satisfying a number of restrictive conditions. Any graph satisfying these conditions is said to be tame. A list of all tame plane graphs up to isomorphism has been generated by an exhaustive computer search. The formal statement that every tame plane graph is isomorphic to one of these cases can be expressed in HOL Light as import_tame_classification. See Section 7.
- (3) The ﬁnal body of computer code is a large collection of linear programs. The results have been formally speciﬁed as linear_programming_results in HOL Light. See Section 9.


It is then natural to break the formal proof of the Kepler conjecture into four parts: the formalization of the text part (that is, the traditional non-computer portions of the proof), and the three separate bodies of computer calculations. Because of the size of the formal proof, the full proof of the Kepler conjecture has not been obtained in a single session of HOL Light. What we formalize in a single session is a theorem

|- the_nonlinear_inequalities /\ import_tame_classification

==> the_kepler_conjecture

4

Hales et al. A formal proof of the Kepler conjecture

![image 81](<2015-hales-formal-proof-kepler-conjecture_images/imageFile81.png>)

This theorem represents the formalization of two of the four parts of the proof: the text part of the proof and the linear programming. It leaves the other two parts (nonlinear inequalities and tame classiﬁcation) as assumptions. The formal proof of the assumption the_nonlinear_inequalities is described in Section 5. The formal proof of import_tame_classification in Isabelle is described in Section 7. Thus, combining all these results from various sessions of HOL Light and Isabelle, we have obtained a formalization of every part of the proof of the Kepler conjecture.

4. Text formalization

The next sections of this article turn to each of the four parts of the proof of the Kepler conjecture, starting with the text part of the formalization in this section. In the remainder of this article, we will call the proof of the Kepler conjecture as it appears in [18] the original proof. The proof that appears in [14] will be called the blueprint proof. The formalization closely follows the blueprint proof. In fact, the blueprint and the formalization were developed together, with numerous revisions of the text in response to issues that arose in the formalization.

Since the blueprint and formal proof were developed at the same time, the numbering of lemmas and theorems continued to change as project took shape. The blueprint and formal proof are cross-linked by a system of identiﬁers that persist through project revisions, as described in [47, §5].

- 4.1. standard libraries. The Flyspeck proof rests on a signiﬁcant body of mathematical prerequisites, including basics of measure, geometric notions, and properties of polyhedra and other aﬃne and convex sets in R3. HOL Light’s standard library, largely under the inﬂuence of Flyspeck, has grown to include a fairly extensive theory of topology, geometry, convexity, measure and integration in Rn. Among the pre-proved theorems, for example, are the Brouwer ﬁxed-pointtheorem, the Krein-Milman theorem and the Stone-Weierstrass theorem, as well as a panoply of more forgettable but practically indispensable lemmas.

Besides the pre-proved theorems, the library includes a number of automated procedures that can make formal proofs much less painful. In particular, one tool supports the common style of picking convenient coordinate axes ‘without loss of generality’ by exploiting translation, scaling and orthogonal transformation. It works by automatically using a database of theorems asserting invariance of various properties under such transformations [22]. This is invaluable for more intricate results in geometry, where a convenient choice of frame can make the eventual algebraic form of a geometrical problem dramatically easier.

The text formalization also includes more specialized results such as measures of various shapes that are particularly signiﬁcant in the partitioning of space in the Flyspeck proof. Among these, for example, is the usual ‘angle sum’ formula for the area of a spherical triangle, or more precisely, the volume of the intersection of its conic hull and a ball. Flyspeck also uses results about special combinatorial and geometrical objects such as hypermaps and fans, and a substantial number of non-trivial results are proved about these, including in eﬀect the Euler characteristic formula for planar graphs.

- 4.2. blueprint proof outline. It is not our purpose to go into the details of the proof of the Kepler conjecture, for which we refer the reader to [14]. We simply recall enough of the high level strategy to permit an understanding of the structure of the formalization. The proof considers an arbitrary packing of congruent balls of radius 1 in Euclidean space and


5

Hales et al. A formal proof of the Kepler conjecture

![image 98](<2015-hales-formal-proof-kepler-conjecture_images/imageFile98.png>)

the properties that it must have to be a counterexample to the Kepler conjecture. Recall that we identify a packing of congruent balls with the discrete set V of centers of the balls.

The ﬁrst step of the proof reduces the problem from a packing V involving a countably inﬁnite number of congruent balls to a packing involving at most ﬁnitely many balls in close proximity to one further ﬁxed central ball. This reduction is obtained by making a geometric partition of Euclidean space that is adapted to the given packing. The pieces of this partition are called Marchal cells (replacing the decomposition stars in the original proof)[33]. A key inequality (the Cell Cluster Inequality,which is discussed in Section 4.4) providesthe link between the Kepler conjecture and a local optimization problem (the local annulus inequality) involving at most ﬁnitely many balls. This reduction appears as the following formal result:

|- the_nonlinear_inequalities /\ (!V. cell_cluster_inequality V) /\ (!V. packing V /\ V SUBSET ball_annulus

==> local_annulus_inequality V)

==> the_kepler_conjecture

All three assumptions can be viewed as explicit optimization problems of continuous functions on compact spaces. The constant ball annulus is deﬁned as the set A = {x ∈ R3 : 2 ≤ ||x|| ≤ 2.52}. As this set is compact and any packing V is discrete, the intersection of a packing with this set is necessarily ﬁnite. The local annulus inequality for a ﬁnite packing V ⊂ A can be stated in the following form:

f(||v||) ≤ 12,

- (1) v∈V


where f(t) = (2.52−t)/(2.52−2) is the linear function that decays from 1 to 0 on the given annulus. An argument which we do not repeat here shows that it is enough to consider V with at most 15 elements [14, Lemma 6.110]. We discuss the nonlinear inequalities and the cell cluster inequality elsewhere in this paper. The local annulus inequality has been used to solve other open problems in discrete geometry: Bezdek’s strong dodecahedral conjecture and Fejes-To´th’s contact conjecture [16].

The rest of the proof consists in proving the local annulus inequality. To carry this out, we assume that we have a counterexample V. The compactness of the ball annulus allows us to assume that the counterexample has a special form that we call contravening. We make a detailed study of the properties of a contravening V. The most important of these properties is expressed by what is called the main estimate (see Section 4.4). These properties imply that V gives rise to a combinatorial structure called a tame planar hypermap. (In this brief summary, we consider tame planar hypermaps to be essentially the same as plane graphs with certain restrictive properties. The nodes of the graph are in bijection with V.) A computer is used to enumerate all of the ﬁnitely many tame plane graphs up to isomorphism. This reduces the possible counterexamples V to an explicit ﬁnite family of cases.

For each explicitly given tame planar hypermap H, we may consider all contravening packings V associated with H. By deﬁnition, these are counterexamples to Equation (1). We express the conditions on V as a system of nonlinear inequalities. We relax the nonlinear system to a linear system and use linear programming techniques to show that the linear programs are infeasible and hence that the nonlinear system is inconsistent, so that the potential counterexample V cannot exist. Eliminating all possible counterexamples in this way, we conclude that the Kepler conjecture must hold.

6

Hales et al. A formal proof of the Kepler conjecture

![image 115](<2015-hales-formal-proof-kepler-conjecture_images/imageFile115.png>)

- 4.3. diﬀerences between the original proof and the blueprint proof. The blueprint proof follows the same general outline as the original proof. However, many changes have been made to make it more suitable for formalization. We list some of the primary diﬀerences between the two proofs

- (1) In the blueprint proof, topological results concerning plane graphs are replaced with purely combinatorial results about hypermaps.
- (2) The blueprint proof is based on a diﬀerent geometric partition of space than that originally used. Marchal introduced this partition and ﬁrst observed its relevance to the Kepler conjecture [33]. Marchal’s partition is described by rules that are better adapted to formalization than the original.
- (3) In a formal proof, every new concept comes at a cost: libraries of lemmas must be developed to support each concept. We have organized the blueprint proof around a small number of major concepts such as spherical trigonometry, volume, hypermap, fan, polyhedra, Voronoi partitions, linear programming, and nonlinear inequalities of trigonometric functions.
- (4) The statements of the blueprint proof are more precise and make all hypotheses explicit.
- (5) To permit a large collaboration, the chapters of the blueprint have been made as independent from one another as possible, and long proofs have been broken up into series of shorter lemmas.
- (6) In the original, computer calculations were a last resort after as much was done by hand as feasible. In the blueprint, the use of computer has been fully embraced. As a result, many laborious lemmas of the original proof can be automated or eliminated altogether.


Because the original proof was not used for the formalization, we cannot assert that the original proof has been formally veriﬁed to be error free. Similarly, we cannot assert that the computer code for the original proof is free of bugs. The detection and correction of small errors is a routine part of any formalization project. Overall, hundreds of small errors in the proof of the Kepler conjecture were corrected during formalization.

- 4.4. appendix to the blueprint. As part of the Flyspeck project, the blueprint proof has been supplemented with an 84 page unpublished appendix ﬁlled with additional details about the proof. We brieﬂy describe the appendix.


The ﬁrst part of the appendix gives details about how to formalize the main estimate [14, Sec 7.4]. The main estimate is the most technically challenging part of the original text, and its formalization was the most technically challenging part of the blueprint text. In fact, the original proof of the main estimate contained an error that is described and corrected in [19]. This is the most signiﬁcant error that was found.

A second major part of the appendix is devoted to the proof of the Cell Cluster Inequality [14, Thm 6.93]. In the blueprint text, the proof is skipped, with the following comment: “The proof of this cell cluster inequality is a computer calculation, which is the most delicate computer estimate in the book. It reduces the cell cluster inequality to hundreds of nonlinear inequalities in at most six variables.” The appendix gives full details.

A ﬁnal part of the appendix deals with the ﬁnal integration of the various libraries in the project. As a large collaborative eﬀort that used two diﬀerent proof assistants, there were many small diﬀerences between libraries that had to be reconciled to obtain a clean ﬁnal theorem. The most signiﬁcant diﬀerence to reconcile was the notion of planarity as used in classiﬁcation of tame plane graphs and the notion of planarity that appears in the

7

Hales et al. A formal proof of the Kepler conjecture

![image 132](<2015-hales-formal-proof-kepler-conjecture_images/imageFile132.png>)

hypermap library. Until now, in our discussion, we have treated tame plane graphs and tame planar hypermaps as if there were essentially the same. However, in fact, they are based on two very diﬀerent notions of planarity. The recursive procedure deﬁning tame graph planarity is discussed in Section 7.1. By contrast, in the hypermap library, the Euler characteristic formula is used as the basis of the deﬁnition of hypermap planarity. The appendix describes how to relate the two notions. This part of the appendix can be viewed as an expanded version of Section 4.7.4 of [14].

- 4.5. recording and replaying the proof. We also have an alternative weaker form of the main statement of the Kepler conjecture (from Section 3) that makes explicit all three computational portions of the proof. This form of the theorem leaves the list of graphs in the archive as an unspeciﬁed bound variable a. This weaker form has the advantage that it can be veriﬁed relatively quickly. |- !a. tame_classification a /\


good_linear_programming_results a /\ the_nonlinear_inequalities

==> the_kepler_conjecture

We have employed an adapted version of HOL Light to record and export the formal proof steps generated by the proof scripts of the main statement in this form (www.prooftechnologies.com/flyspeck/). The exported proof objects have been imported and executed in a separate HOL Light session involving just the HOL Light core system and a simple proof importing mechanism. They have also been imported and replayed in HOL Zero, another member of the HOL family [1].

This exercise has various beneﬁts. First, it is generally much faster to import and replay a recorded formal proof than to execute the corresponding high-level proof script, whose execution typically involves a substantial amount of proof search beyond the actual formal proof steps. Second, it gives a further check of the formal proof. The successful import into HOL Zero, a system that pays particular attention to trustworthiness, eﬀectively eliminates any risk of error in the proof. Finally, the exported proof objects are available to be imported and replayed in other HOL systems, opening the Flyspeck libraries of theorems to the users of other proof assistants.

5. Nonlinear inequalities

All but a few nonlinear inequalities in the Flyspeck project have the following general form

- (2) ∀x, x ∈ D =⇒ f1(x) < 0 ∨ . . . ∨ fk(x) < 0.


where D = [a1, b1] × . . . × [an, bn] is a rectangular domain inside Rn and x = (x1, . . ., xn). In the remaining few inequalities, the form is similar, except that k = 1 and the inequality is not strict. In every case, the number of variables n is at most six. The following functions and operations appear in inequalities: basic arithmetic operations, square root, sine, cosine, arctangent, arcsine, arccosine, and the analytic continuation of arctan( √x)/ √x to the region x > −1. For every point x ∈ D, at least one of the functions fi is analytic in a neighborhood of x (and takes a negative value), but situations arise in which not every function is analytic or even deﬁned at every point in the domain.

![image 133](<2015-hales-formal-proof-kepler-conjecture_images/imageFile133.png>)

![image 134](<2015-hales-formal-proof-kepler-conjecture_images/imageFile134.png>)

The formal veriﬁcation of inequalities is based on interval arithmetic [35]. For example, [3.14, 3.15] is an interval approximation of π since 3.14 ≤ π ≤ 3.15. In order to work with interval approximations, arithmetic operations are deﬁned over intervals. Denote the set

8

Hales et al. A formal proof of the Kepler conjecture

![image 151](<2015-hales-formal-proof-kepler-conjecture_images/imageFile151.png>)

of all intervals over R as IR. A function (operation) F : IR → IR is called an interval extension of f : R → R if the following condition holds

∀I ∈ IR, {f(x) : x ∈ I} ⊂ F(I).

This deﬁnition can be easily extended to functions on Rk. It is easy to construct interval extensions of basic arithmetic operations and elementary functions. For instance,

[a1, b1] ⊕ [a2, b2] = [a, b] for some a ≤ a1 + a2 and b ≥ b1 + b2.

Here, ⊕ denotes an interval extension of +. We do not deﬁne the result of ⊕ as [a1+a2, b1+ b2] since we may want to represent all intervals with limited precision numbers (for example, decimal numbers with at most 3 signiﬁcant ﬁgures). With basic interval operations, it is possible to construct an interval extension of an arbitrary arithmetic expression by replacing all elementary operations with corresponding interval extensions. Such an interval extension is called the natural interval extension. Natural interval extensions can be imprecise, and there are several ways to improve them.

One simple way to improve upon the natural interval extension of a function is to subdivide the original interval into subintervals and evaluate an interval extension of the function on all subintervals. Using basic interval arithmetic and subdivisions, it would theoretically be possible to prove all nonlinear inequalities that arise in the project. This method does not work well in practice because the number of subdivisions required to establish some inequalities would be enormous, especially for multivariate inequalities.

Both the C++ informal veriﬁcation code (from the original proof of the Kepler conjecture) and our formal veriﬁcation procedure implemented in OCaml and HOL Light use improved interval extensions based on Taylor approximations.

Suppose that a function g : R → R is twice diﬀerentiable. Fix y ∈ [a, b]. Then we have the following formula for all x ∈ [a, b]:

- 1

![image 152](<2015-hales-formal-proof-kepler-conjecture_images/imageFile152.png>)

- 2


g′′(ξ)(x − y)2 for some value ξ = ξ(x) ∈ [a, b]. Choose w such that w ≥ max{y − a, b − y} and deﬁne r(x) = |g′(y)|w + 12|g′′(ξ(x))|w2. We get the following inequalities

g(x) = g(y) + g′(y)(x − y) +

![image 153](<2015-hales-formal-proof-kepler-conjecture_images/imageFile153.png>)

∀x ∈ [a, b]. g(y) − r(x) ≤ g(x) ≤ g(y) + r(x). Let G, G1, and G2 be any interval extensions of g, g′, and g′′. Choose e such that

2

- e ≥ iabs G1([y, y]) w + w


2 iabs G2([a, b]) , where iabs [c, d] = max{|c|, |d|}. Assume that G([y, y]) = [gl, gu]. Then the following function deﬁnes a (second order) Taylor interval approximation of g(x):

![image 154](<2015-hales-formal-proof-kepler-conjecture_images/imageFile154.png>)

GTaylor([a, b]) = [l, u] where l ≤ gl − e and u ≥ gu + e. That is,

∀x ∈ [a, b]. g(x) ∈ GTaylor([a, b]). In our veriﬁcation procedure, we always take y close to the midpoint (a + b)/2 of the interval in order to minimize the value of w. There is an analogous Taylor approximation for multivariate functions based on the multivariate Taylor theorem.

As a small example, we compute a Taylor interval approximation of g(x) = x−arctan(x) on [1, 2]. We have g′(x) = 1 − 1/(1 + x2) and g′′(x) = −2x/(1 + x2)2. Take y = 1.5 and natural interval extensions G1 and G2 of g′(x) and g′′(x). Then w = 0.5, G([1.5, 1.5]) = [0.517, 0.518], G1([1.5, 1.5]) = [0.692, 0.693], and G2([1, 2]) = [−0.5, −0.16]. We get

- e = 0.409 and hence GTaylor([1, 2]) = [0.108, 0.927]. This result is much better than the result obtained with the natural extension G([1, 2]) = [−0.11, 1.22]. We note that in the


9

Hales et al. A formal proof of the Kepler conjecture

![image 171](<2015-hales-formal-proof-kepler-conjecture_images/imageFile171.png>)

calculation of GTaylor([1, 2]), we evaluate the expensive interval extension of arctan only once. To obtain similar accuracy with subdivision, more than one evaluation of arctan is needed. In general, it is necessary to subdivide the original interval into subintervals even when Taylor interval approximations are used. But in most cases, Taylor interval approximations lead to fewer subdivisions than natural interval extensions.

Taylor interval approximationsmay also be used to prove the monotonicityof functions. By expanding g′(x) in a Taylor series, we obtain a Taylor interval approximation in a similar way:

∀x ∈ [a, b]. g′(x) ∈ G′

Taylor([a, b])

for some interval G′Taylor([a, b]). If 0 is not in this interval, then the derivative has ﬁxed sign, and the function g is monotonic, so that the maximum value of g occurs at the appropriate endpoint. More generally, in multivariate inequalities, a partial derivative of ﬁxed sign may be used to reduce the veriﬁcation on a rectangle of dimension k to an abutting rectangle of dimension k − 1.

A few of the inequalities are sharp. That is, the inequalities to be proved have the form

- f ≤ 0, where f(x0) = 0 at some point x0 in the domain D of the inequality. In each case that arises, x0 lies at a corner of the rectangular domain. We are able to prove these inequalities by showing that (1) f(x0) = 0 by making a direct computation using exact arithmetic; (2)


- f < 0 on the complement of some small neighborhood U of x0 in the domain; and (3) every partial derivative of f on U has the appropriate sign to make the maximum of f on


U to occur at x0. The ﬁnal two steps are carried out using our standard tools of Taylor intervals.

All the ideas presented in the discussion above have been formalized in HOL Light and a special automatic veriﬁcation procedure has been written in the combination of OCaml and HOL Light for veriﬁcation of general multivariate nonlinear inequalities. This procedure consists of two parts. The ﬁrst part is an informal search procedure which ﬁnds an appropriate subdivision of the original inequality domain and other information which can help in the formal veriﬁcation step (such as whether or not to apply the monotonicity argument, which function from a disjunction should be veriﬁed, etc.). The second part is a formal veriﬁcation procedure which takes the result of the informal search procedure as input and produces a ﬁnal HOL Light theorem. A detailed description of the search and veriﬁcation procedures can be found in [43, 45].

All formal numerical computations are done with special ﬁnite precision ﬂoating-point numbers formalized in HOL Light. It is possible to change the precision of all computations dynamically, and the informal search procedure tries to ﬁnd minimal precision necessary for the formal veriﬁcation. At the lowest level, all computations are done with natural numbers in HOL Light. We improved basic HOL Light procedures for natural numbers by representing natural numerals over an arbitrary base (the base 2 is the standard base for HOL Light natural numerals) and by providing arithmetic procedures for computing with such numerals. Note that all computations required in the nonlinear inequality veriﬁcation procedure are done entirely inside HOL Light, and the results of all arithmetic operations are HOL Light theorems. The native ﬂoating point operations of the computer are not used in any formal proof. As a consequence, the formal veriﬁcation of nonlinear inequalities in HOL Light is much slower than the original informal C++ code.

The term the_nonlinear_inequalities is deﬁned as a conjunction of several hundred nonlinear inequalities. The domains of these inequalities have been partitioned to create more than 23,000 inequalities. The veriﬁcation of all nonlinear inequalities in HOL Light on the Microsoft Azure cloud took approximately 5000 processor-hours. Almost

10

Hales et al. A formal proof of the Kepler conjecture

![image 188](<2015-hales-formal-proof-kepler-conjecture_images/imageFile188.png>)

all veriﬁcations were made in parallel with 32 cores using GNU parallel [46]. Hence the real time was less than a week (5000 < 32 × 168 hours per week). These veriﬁcations were made in July and August, 2014. Nonlinear inequalities were veriﬁed with compiled versions of HOL Light and the veriﬁcation tool developed in Solovyev’s 2012 thesis.

The veriﬁcations were rechecked at Radboud University on 60 hyperthreading Xeon 2.3GHz CPUs, in October 2014. This second veriﬁcation required about 9370 processorhours over a period of six days. Identical results were obtained in these repeated calculations.

6. Combining HOL Light sessions

The nonlinear inequalities were obtained in a number of separate sessions of HOL Light that were run in parallel. By the design of HOL Light, it is not possible to pass a theorem from one session to another without fully reconstructing the proof in each session. To combine the results into a single session of HOL Light, we used a specially modiﬁed version of HOL Light that accepts a theorem from another session without proof. We brieﬂy describe this modiﬁed version of HOL Light.

Each theorem is expressed by means of a collection of constants, and those constants are deﬁned by other constants, recursively extending back to the primitive constants in the HOL Light kernel. Similarly, the theorem and constants have types, and those types also extend recursively back through other constants and types to the primitive types and constants of the kernel. A theorem relies on a list of axioms, which also have histories of constants and types. The semantics of a theorem is determined by this entire history of constants, types, and axioms, reaching back to the kernel.

The modiﬁed version of HOL Light is designed in such a way that a theorem can be imported from another session, provided the theorem is proved in another session, and the entire histories of constants, types, and axioms for that theorem are exactly the same in the two sessions. To implement this in code, each theorem is transformed into canonical form. To export a theorem, the canonical form of the theorem and its entire history are converted faithfully to a large string, and the MD5 hash of the string is saved to disk. The modiﬁed version of HOL Light then allows the import of a theorem if the appropriate MD5 is found. The import mechanism is prevented from being used in ways other than the intended use, through the scoping rules of the OCaml language.

To check that no pieces were overlooked in the distribution of inequalities to various cores, the pieces have been reassembled in the specially modiﬁed version of HOL Light. In that version, we obtain a formal proof of the theorem |- the_nonlinear_inequalities

This theorem is exactly the assumption made in the formal proof of the Kepler conjecture, as stated in Section 3. We remark that the modiﬁed version of HOL Light is not used during the proof of any other result of the Kepler conjecture. It is only used to assemble the small theorems from parallel sessions to produce this one master theorem.

7. Tame Classification

The ﬁrst major success of the Flyspeck projectwas the formalization of the classiﬁcation of tame plane graphs. In the original proof of the Kepler conjecture, this classiﬁcation was done by computer, using custom software to generate plane graphs satisfying given properties. This formalization project thus involved the veriﬁcation of computer code. The formal veriﬁcation of the code became the subject of Gertrud Bauer’s PhD thesis under the direction of Nipkow. The work was completed by Nipkow [38].

11

Hales et al. A formal proof of the Kepler conjecture

![image 205](<2015-hales-formal-proof-kepler-conjecture_images/imageFile205.png>)

As explained in Section 4, the tame plane graphs encode the possible counterexamples to the Kepler conjecture as plane graphs. The archive is a computer-generated list of all tame graphs. It is a text ﬁle that can be imported by the diﬀerent parts of the proof. In this section we explain how the followingcompleteness theorem is formalized in Isabelle/HOL:

|− ”g ∈ PlaneGraphs” and ”tame g” shows ”fgraph g ∈≃ Archive”

The meaning of the terms PlaneGraphs, tame, fgraph, and Archive is explaned in the following paragraphs. In informal terms, the completeness theorem asserts that every tame plane graph is isomorphic to a graph appearing in the archive.

Plane graphs are represented as an n-tuple of data including a list of faces. Faces are represented as lists of vertices, and each vertex is represented by an integer index. A function fgraph strips the n-tuple down to the list of faces.

To prove the completeness of the archive, we need to enumerate all tame plane graphs. For this purpose we rely on the fact that HOL contains a functional programming language. In essence, programs in HOL are simply sets of recursion equations, i.e., pure logic. The original proof classiﬁes tame plane graphs by a computer program written in Java. Therefore, as a ﬁrst step in the formalization, we recast the original Java program for the enumeration of tame plane graphs in Isabelle/HOL. The result is a set of graphs called TameEnum. In principle we could generate TameEnum by formal proof but this would be extremely time and space consuming because of the huge number of graphs involved (see below). Therefore we rely on the ability of Isabelle/HOL to execute closed HOL formulas by translating them automatically into a functional programming language (in this case ML), running the program, and accepting the original formula as a theorem if the execution succeeds [12]. The programming language is merely used as a fast term rewriting engine.

We prove the completeness of the archive in two steps. First we prove that every tame plane graph is in TameEnum. This is a long interactive proof in Isabelle/HOL. Then we prove that every graph in TameEnum is isomorphic to some graph in the archive. Formally this can be expressed as follows:

|− fgraph ‘ TameEnum ⊆≃ Archive

This is a closed formula that Isabelle proves automatically by evaluating it (in ML) because all functions involved are executable.

In the following two subsections we give a high-level overview of the formalization and proof. For more details see [38, 36]. The complete machine-checked proof, including the archive is available online in the Archive of Formal Proofs afp.sf.net [5]. Section 7.3 discusses the size of the archive and some performance issues.

- 7.1. plane graphs and their enumeration. Plane graphs are not deﬁned by the conventional mathematical deﬁnition. They are deﬁned by an algorithm that starts with a polygon and inductively adds loops to it in a way that intuitively preserves planarity. (The algorithm is an implementation in code of a process of drawing a sequence of loops on a sheet of paper, each connected to the previous without crossings.)


Expressed as a computer algorithm, the enumeration of plane graphs proceeds inductively. It starts with a seed graph (the initial polygon) with two faces (intuitively corresponding to the two components in the plane of the complement of a Jordan curve), a ﬁnal outer one and a non-ﬁnal inner one, where a ﬁnal face means that the algorithm is not permitted to make further modiﬁcations of the face. If a graph contains a non-ﬁnal face, it can be subdivided into a ﬁnal face and any number of non-ﬁnal ones. Because a face can be subdivided in many ways, this process deﬁnes a forest of graphs. The leaves are ﬁnal graphs. The formalization deﬁnes an executable function next_plane that maps a 12

Hales et al. A formal proof of the Kepler conjecture

![image 222](<2015-hales-formal-proof-kepler-conjecture_images/imageFile222.png>)

graph to the list of successor graphs reachable by subdividing one non-ﬁnal face. The set of plane graphs, denoted PlaneGraphs in Isabelle/HOL, is deﬁned to be the set of ﬁnal graphs reachable from some seed graph in ﬁnitely many steps.

- 7.2. tame graphs and their enumeration. The deﬁnition of tameness is already relatively close to an executable formulation. The two crucial constraints are that the faces of a tame graph may only be triangles up to hexagons, and that the “admissible weight” of a tame graph is bounded from above. The tameness constraints imply that there are only ﬁnitely many tame plane graphs up to isomorphism (although we never need to prove this directly). The Isabelle/HOL predicate is called tame.

The enumeration of tame plane graphs is a modiﬁed enumeration of plane graphs where we remove ﬁnal graphs that are deﬁnitely not tame, and prune non-ﬁnal graphs that cannot lead to any tame graphs. The description in [15] is deliberately sketchy, but the Java programs provide precise pruning criteria. In the formalization we need to balance eﬀectiveness of pruning with simplicity of the completeness proof: weak pruning criteria are easy to justify but lead to unacceptable run times of the enumeration, sophisticated pruning criteria are diﬃcult to justify formally. In the end, for the formalization, we simpliﬁed the pruning criteria found in the Java code.

The formalization deﬁnes a function next_tame from a graph to a list of graphs. It is a restricted version of next_plane where certain kinds of graphs are removed and pruned, as described above. For computationalreasons, the tameness check here is approximate: no tame graphs are removed, but non-tame graphs may be produced. This is unproblematic: in the worst case a fake counterexample to the Kepler conjecture is produced, which is eliminated at a later stage of the proof, but we do not miss any real ones.

Each step next_tame is executable. The exhaustive enumeration of all ﬁnal graphs reachable from any seed graph via next_tame yields a set, denoted TameEnum.

- 7.3. the archive. The archive that came with the original proof contained (for historical reasons) over 5000 graphs. The ﬁrst formalization [38] resulted in a reduced archive of 2771 graphs. During the completeness proof, the veriﬁed enumeration of tame graphs has to go through 2 × 107 intermediate and ﬁnal graphs, which takes a few hours. With the advent of the blueprint proof, the deﬁnition of tameness changed. This change lead to 2 × 109 intermediate and ﬁnal graphs and an archive with 18762 graphs. The enumeration process had to be optimized to prevent it running out space and time [36]. In the end, the enumeration again runs in a few hours. The formalization uncovered and ﬁxed a bug in the original Java program, related to symmetry optimizations. Fortunately, this bug was not executed in the original proof, so that the output was correct. However, the bug caused two graphs to be missed in an early draft of the blueprint proof.


8. Importing results from Isabelle

The tame graph classiﬁcation was done in the Isabelle/HOL proof assistant, while all the rest of the project has been carried out in HOL Light. It seems that it would be feasible to translate the Isabelle code to HOL Light to have the entire project under the same roof, but this lies beyond the scope of the Flyspeck project.

Current tools do not readily allow the automatic import of this result from Isabelle to HOL Light. A tool that automates the import from Isabelle to HOL Light was written by McLaughlin with precisely this application in mind [34], but this tool has not been maintained. A more serious issue is that the proof in Isabelle uses computational reﬂection as described at the end of Section 2, but the HOL Light kernel does not permit reﬂection.

13

Hales et al. A formal proof of the Kepler conjecture

![image 239](<2015-hales-formal-proof-kepler-conjecture_images/imageFile239.png>)

Thus, the reﬂected portions of the formal proof would have to be modiﬁed as part of the import.

Instead, we leave the formalization of the Kepler conjecture distributed between two diﬀerent proof assistants. In HOL Light, the Isabelle work appears as an assumption, expressed through the following deﬁnition. |- import_tame_classification <=>

(!g. g IN PlaneGraphs /\ tame g ==> fgraph g IN_simeq archive)

The left-hand side is exactly the assumption made in the formal proof of the Kepler conjecture, as stated in Section 3. The right-hand side is the verbatim translation into HOL Light of the following completeness theorem in Isabelle (repeated from above):

|− ”g ∈ PlaneGraphs” and ”tame g” shows ”fgraph g ∈≃ Archive”

All of the HOL Light terms PlaneGraphs, tame, archive, IN_simeq, fgraph are verbatim translations of the corresponding deﬁnitions in Isabelle (extended recursively to the constants appearing in the deﬁnitions). The types are similarly translated between proof assistants (lists to lists, natural numbers to natural numbers, and so forth). These deﬁnitions and types were translated by hand. The archive of graphs is generated from the same ML ﬁle for both the HOL Light and the Isabelle statements.

Since the formal proof is distributed between two diﬀerent systems with two diﬀerent logics, we brieﬂy indicate why this theorem in Isabelle must also be a theorem in HOL Light. Brieﬂy, this particular statement could be expressed as a SAT problem in ﬁrst-order propositional logic. SAT problems pass directly between systems and are satisﬁable in one system if and only if they are satisﬁable in the other (assuming the consistency of both systems). In expressing the classiﬁcation theorem as a SAT problem, the point is that all quantiﬁers in the theorem run over bounded discrete sets, allowing them to be be expanded as ﬁnitely many cases in propositional logic. We also note that the logics of Isabelle/HOL and HOL Light are very closely related to each another.

9. Linear programs

We return to the sketch of the proof from Section 4 and add some details about the role of linear programming. The blueprint proof reduces inﬁnite packings that are potential counterexamples to the Kepler conjecture to ﬁnite packings V, called contravening packings. The combinatorial structure of a contravening packing can be encoded as a tame planar hypermap. The tame graph classiﬁcation theorem implies that there are ﬁnitely many tame planar hypermaps up to isomorphism. For each such hypermap it is possible to generate a list of inequalities which must be satisﬁed by a potential counterexample associated with the given tame planar hypermap. Most of these inequalities are nonlinear.

To rule out a potential counterexample, it is enough to show that the system of nonlinear inequalities has no solution. A linear relaxation of these inequalities is obtained by replacing nonlinear quantities with new variables. For instance, the dihedral angles of a simplex are nonlinear functions of the edge lengths of the simplex; new variables are introduced for each dihedral angle to linearize any expression that is linear in the angles. The next step is to show that the linear program is not feasible. Infeasibility implies that the original system of nonlinear inequalities is inconsistent, and hence there is no contravening packing associated with the given tame planar hypermap. The process of construction and solution of linear programs is repeated for all tame planar hypermaps and it is shown that no contravening packings (and hence no counterexamples to the Kepler conjecture) exist.

14

Hales et al. A formal proof of the Kepler conjecture

![image 256](<2015-hales-formal-proof-kepler-conjecture_images/imageFile256.png>)

There are two parts in the formal veriﬁcation of linear programs. First, linear programs are generated from formal theorems, nonlinear inequalities, and tame planar hypermaps. Second, a general linear program veriﬁcation procedure veriﬁes all generated linear programs.

The formal generation of linear programs follows the procedure outlined above. The ﬁrst step is generation of linear inequalities from properties of contravening packings. Many such properties directly follow from nonlinear inequalities. As described above, nonlinear inequalities are transformed into linear inequalities by introducing new variables for nonlinear expressions. In fact, we do not change the original nonlinear inequalities but simply introduce new HOL Light constants for nonlinear functions and reformulate nonlinear inequalities in a linear form.

For example, suppose we have the following inequalities: x + x2 ≤ 3 and x ≥ 2. Deﬁne y = x2 to obtain the following linear system of inequalities: x + y ≤ 3, x ≥ 2, and y ≥ 4. (The last inequality follows from x ≥ 2.) We ignore the nonlinear dependency of y on x, and obtain a system of linear inequalities which can be easily shown to be inconsistent.

The generation of linear inequalities from properties of contravening packings is a semiautomatic procedure: many such inequalities are derived with a special automatic procedure but some of them need manual formal proofs.

The next step is the relaxation of linear inequalities with irrational coeﬃcients. We

do√2ynot≤ πsolve, x +lineary ≤ programs with irrational numbers directly. Consider the example, x −

√35, x ≥ 5, y ≥ 0. These inequalities imply x ≥ 5, y ≥ 0, x − 1.42y ≤ 3.15, x + y ≤ 6.

![image 257](<2015-hales-formal-proof-kepler-conjecture_images/imageFile257.png>)

![image 258](<2015-hales-formal-proof-kepler-conjecture_images/imageFile258.png>)

This system with rational coeﬃcients is inconsistent and thus the original system is inconsistent.

The relaxation of irrational coeﬃcients is done completely automatically. In fact, inequalities with integer coeﬃcients are produced by multiplying each inequality by a suﬃciently large power of 10 (decimal numerals are used in the veriﬁcation of linear programs).

The last step of the formal generation of linear programs is the instantiation of free variables of linear inequalities with special values computed from an associated tame planar hypermap. In this way, each tame planar hypermap produces a linear program which is formally checked for feasibility. Not all linear programs obtained in this way are infeasible. For about half of the tame planar hypermaps, linear relaxations are insuﬃciently precise and do not yield infeasible linear programs. In that situation, a feasible linear program is split into several cases where new linear inequalities are introduced. New cases are produced by considering alternatives of the form x ≤ a ∨ a ≤ x where x is some variable and a is a constant. Case splitting leads to more precise linear relaxations.

Case splitting for veriﬁcation of linear programs in the project is automatic. In fact, a special informal procedure generates all required cases ﬁrst, and the formal veriﬁcation procedure for linear programs is applied to each case.

Formal veriﬁcation of general linear programs is relatively easy. We demonstrate our veriﬁcation procedure with an example. A detailed description of this procedure can be found in [44]. All variables in each veriﬁed linear program must be nonnegative and bounded. In the following example, our goal is to verify that the following system is infeasible:

x − 1.42y ≤ 3.15, x + y ≤ 6, 5 ≤ x ≤ 10, 0 ≤ y ≤ 10.

15

Hales et al. A formal proof of the Kepler conjecture

![image 275](<2015-hales-formal-proof-kepler-conjecture_images/imageFile275.png>)

Introduce slack variables s1, s2 for inequalities which do not deﬁne bounds of variables, and construct the following linear program:

minimize s1 + s2 subject to x − 1.42y ≤ 3.15 + s1, x + y ≤ 6 + s2, 5 ≤ x ≤ 10, 0 ≤ y ≤ 10, 0 ≤ s1, 0 ≤ s2.

- (3)


If the objective value of this linear program is positive then the original system is infeasible. We are interested in a dual solution of this linear program. Dual variables correspond to the constraints of the primal linear program. We use an external linear programming tool for ﬁnding dual solutions, which may be imprecise. A procedure, which is described in [44], starts with an initial imprecise dual solution and modiﬁes it to obtain a carefully constructed dual solution that has suﬃcient numerical precision to prove the infeasibility of the original (primal) system. In the example at hand, we get the following modiﬁed dual solution:

(0.704, 1, −1.705, 0.001, −0.00032,0,0.296, 0), whose entries correspond with the ordered list of eight inequalities in the system (3). With this modiﬁed dual solution, the sum of the constraints of the system (3) with the slack variables set to zero, weighted by the coeﬃcients of the dual vector, yields 0x + 0y ≤ −0.2974. This contradiction shows that our original system of inequalities is infeasible. We stress that the coeﬃcients of x and y in this sum are precisely zero, and this is a key feature of the modiﬁed dual solutions.

If we know a modiﬁed dual solution, then the formal veriﬁcation reduces to the summation of inequalities with coeﬃcients from the modiﬁed dual solution and checking that the ﬁnal result is inconsistent. A modiﬁed dual solution can be found with informal methods. We use GLPK for solving linear programs [8] and a special C# program for ﬁnding the required modiﬁed dual solutions for linear programs. All dual solutions are also converted to integer solutions by multiplying all coeﬃcients by a suﬃciently large power of 10. The formal veriﬁcation procedure uses formal integer arithmetic. There are 43,078 linear programs (after considering all possible cases). All these linear programs can be veriﬁed in about 15 hours on a 2.4GHz computer. The veriﬁcation time does not include time for generating modiﬁed dual solutions. These dual solutions need only be computed once and saved to ﬁles that are later loaded by the formal veriﬁcation procedure.

10. Auditing a distributed formal proof

A proof assistant largely cuts the mathematical referees out of the veriﬁcation process. This is not to say that human oversight is no longer needed. Rather, the nature of the oversight is such that specialized mathematical expertise is only needed for a small part of the process. The rest of the audit of a formal proof can be performed by any trained user of the HOL Light and Isabelle proof assistants.

Adams [2] describes the steps involved in the auditing of this formal proof. The proofs scripts must be executed to see that they produce the claimed theorem as output. The deﬁnitions must be examined to see that the meaning of the ﬁnal theorem (the Kepler conjecture) agrees with the common understanding of the theorem. In other words, did the right theorem get formalized? Were any unapproved axioms added to the system? The formal proof system itself should be audited to make sure there is no foul play in the syntax, visual display, and underlying internals. A fradulent user of a proof assistant might “exploit a ﬂaw to get the project completed on time or on budget. In their review, the auditor must assume malicious intent, rather than use arguments about the improbability of innocent error” [2].

16

Hales et al. A formal proof of the Kepler conjecture

![image 292](<2015-hales-formal-proof-kepler-conjecture_images/imageFile292.png>)

This particular formal proof has several special features that call for careful auditing. The most serious issue is that the full formal proof was not obtained in a single session of HOL Light. An audit should check that the statement of the tame classiﬁcation theorem in Isabelle has been faithfully translated into HOL Light. (It seems to us that our single greatest vulnerability to error lies in the hand translation of this one statement from Isabelle to HOL Light, but even here there is no mathematical reasoning involved beyond a rote translation.) In particular, an audit should check that the long list of tame graphs that is used in Isabelle is identical to the list that is used in HOL Light. (As mentioned above, both systems generated their list from the same master ﬁle.)

The auditor should also check the design of the special modiﬁcation of HOL Light that was used to combine nonlinear inequalities into a single session.

11. Related work and acknowledgements

Numerous other research projects in formal proofs have made use of the Flyspeck project in some way or have been inspired by the needs of Flyspeck. These projects include the work cited above on linear programming and formal proofs of nonlinear inequalities, automated translation of proofs between formal proof systems [42], [24], [34], the refactoring of formal proofs [3], machine learning applied to proofs and proof automation [25] [26], an SSReﬂect mode for HOL Light [43], and a mechanism to execute trustworthy external arithmetic from Isabelle/HOL [40], [41].

The roles of the various members of the Flyspeck project have been spelled out in the email announcement of the project completion, posted at [7].

We wish to acknowledge the help, support, inﬂuence, and various contributions of the following individuals: Nguyen Duc Thinh, Nguyen Duc Tam, Vu Quang Thanh, Vuong Anh Quyen, Catalin Anghel, Jeremy Avigad, Henk Barendregt, Herman Geuvers, Georges Gonthier, Daron Green, Mary Johnston, Christian Marchal, Laurel Martin, Robert Solovay, Erin Susick, Dan Synek, Nicholas Volker, Matthew Wampler-Doty, Benjamin Werner, Freek Wiedijk, Carl Witty, and Wenming Ye.

We wish to thank the following sources of institutional support: NSF grant 0503447 on the “Formal Foundations of Discrete Geometry” and NSF grant 0804189 on the “Formal Proof of the Kepler Conjecture,” Microsoft Azure Research, William Benter Foundation, University of Pittsburgh, Radboud Research Facilities, Institute of Math (VAST), and VIASM.

12. Appendix on definitions

The following theorem provides evidence that key deﬁnitions in the statement of the Kepler conjecture are the expected ones. |// real absolute value:

(&0 <= x ==> abs x = x) /\ (x < &0 ==> abs x = -- x) /\ // powers:

x pow 0 = &1 /\ x pow SUC n = x * x pow n /\ // square root:

(&0 <= x ==> &0 <= sqrt x /\ sqrt x pow 2 = x) /\ // finite sums:

17

Hales et al. A formal proof of the Kepler conjecture

![image 309](<2015-hales-formal-proof-kepler-conjecture_images/imageFile309.png>)

sum (0..0) f = f 0 /\ sum (0..SUC n) f =

sum (0..n) f + f (SUC n) /\ // pi:

abs (pi / &4 - sum (0..n) (\i. (-- &1) pow i / &(2 * i + 1))) <= &1 / &(2 * n + 3) /\

// finite sets and their cardinalities: (A HAS_SIZE n <=> FINITE A /\ CARD A = n) /\ {} HAS_SIZE 0 /\ {a} HAS_SIZE 1 /\ (A HAS_SIZE m /\ B HAS_SIZE n /\ (A INTER B) HAS_SIZE p

==> (A UNION B) HAS_SIZE (m+n - p)) /\

// bijection between Rˆ3 and ordered triples of reals: triple_of_real3 o r3 = (\w:real#real#real. w) /\ r3 o triple_of_real3 = (\v:realˆ3. v) /\

// the origin:

vec 0 = r3(&0,&0,&0) /\ // the metric on Rˆ3:

dist(r3(x,y,z),r3(x’,y’,z’)) =

sqrt((x - x’) pow 2 + (y - y’) pow 2 + (z - z’) pow 2) /\ // a packing:

(packing V <=> (!u v. u IN V /\ v IN V /\ dist(u,v) < &2 ==> u = v))

References

- [1] Mark Adams. Introducing HOL Zero. In Mathematical Software–ICMS 2010, pages 142–143. Springer, 2010.
- [2] Mark Adams. Flyspecking Flyspeck. In Mathematical Software–ICMS 2014, pages 16–20. Springer, 2014.
- [3] Mark Adams and David Aspinall. Recordingand refactoringHOL Light tactic proofs. In Proceedings of the IJCAR workshop on Automated Theory Exploration, 2012.
- [4] Gertrud Bauer. Formalizing Plane Graph Theory – Towards a Formalized Proof of the Kepler Conjecture. PhD thesis, Technische Universita¨t Mu¨nchen, 2006. http: //mediatum.ub.tum.de/doc/601794/document.pdf.
- [5] Gertrud Bauer and Tobias Nipkow. Flyspeck I: Tame graphs. In G. Klein, T. Nipkow, and L. Paulson, editors, The Archive of Formal Proofs. http://afp.sf.net/ entries/Flyspeck-Tame.shtml, May 2006. Formal proof development.
- [6] L. Fejes To´th. Lagerungen in der Ebene auf der Kugel und im Raum. Springer-Verlag, Berlin-New York, ﬁrst edition, 1953.
- [7] Flyspeck. The Flyspeck Project, 2014. http://code.google.com/p/flyspeck.
- [8] GLPK. GLPK (GNU Linear Programming Kit). http://www.gnu.org/ software/glpk/.
- [9] Georges Gonthier, Andrea Asperti, Jeremy Avigad, Yves Bertot, Cyril Cohen, Franc¸ois Garillot, Ste´phane Le Roux, Assia Mahboubi, Russell O’Connor, Sidi Ould


18

Hales et al. A formal proof of the Kepler conjecture

![image 326](<2015-hales-formal-proof-kepler-conjecture_images/imageFile326.png>)

Biha, et al. A machine-checked proof of the odd order theorem. In Interactive Theorem Proving, pages 163–179. Springer, 2013.

- [10] Michael Gordon, Robin Milner, and Christopher Wadsworth. Edinburgh LCF: a mechanized logic of computation, volume 78 of lecture notes in computer science, 1979.
- [11] Michael JC Gordon and Tom F Melham. Introduction to HOL: a theorem proving environment for higher order logic. Cambridge University Press, 1993.
- [12] Florian Haftmann and Tobias Nipkow. Code generation via higher-order rewrite systems. In Functional and Logic Programming, 10th International Symposium, FLOPS 2010, Sendai, Japan, April 19-21, 2010. Proceedings, pages 103–117, 2010. doi: 10.1007/978-3-642-12251-4 9. URL http://dx.doi.org/10.1007/9783-642-12251-4_9.

![image 327](<2015-hales-formal-proof-kepler-conjecture_images/imageFile327.png>)

- [13] Thomas Hales. Developments in formal proofs. Bourbaki Seminar, (1086), 2014.
- [14] Thomas C. Hales. Dense Sphere Packings: a blueprint for formal proofs, volume 400 of London Math Soc. Lecture Note Series. Cambridge University Press, 2012.
- [15] Thomas C. Hales. A proof of the Kepler conjecture. Annals of Mathematics, 162: 1063–1183, 2005.
- [16] Thomas C Hales. The strong dodecahedral conjecture and Fejes To´th’s contact conjecture. Technical report, 2011.
- [17] Thomas C. Hales. Introduction to the Flyspeck project. In Thierry Coquand, Henri Lombardi, and Marie-Franc¸oise Roy, editors, Mathematics, Algorithms, Proofs, number 05021 in Dagstuhl Seminar Proceedings, Dagstuhl, Germany, 2006. Internationales Begegnungs- und Forschungszentrum fu¨r Informatik (IBFI), Schloss Dagstuhl, Germany. http://drops.dagstuhl.de/opus/volltexte/2006/432.
- [18] Thomas C. Hales and Samuel P. Ferguson. The Kepler conjecture. Discrete and Computational Geometry, 36(1):1–269, 2006.
- [19] Thomas C. Hales, John Harrison, Sean McLaughlin, Tobias Nipkow, Steven Obua, and Roland Zumkeller. A revision of the proof of the Kepler Conjecture. Discrete & Computational Geometry, 44(1):1–34, 2010.
- [20] John Harrison. Towards self-veriﬁcation of HOL Light. In Ulrich Furbach and Natarajan Shankar, editors, Automated Reasoning, Third International Joint Conference, IJCAR 2006, Seattle, WA, USA, August 17-20, 2006, Proceedings, volume 4130 of Lecture Notes in Computer Science, pages 177–191. Springer, 2006. ISBN 3-540-37187-7. doi: 10.1007/11814771 17. URL http://dx.doi.org/10.1007/ 11814771_17.

![image 328](<2015-hales-formal-proof-kepler-conjecture_images/imageFile328.png>)

- [21] John Harrison. The HOL Light theorem prover, 2014. http://www.cl.cam.ac. uk/˜jrh13/hol-light/index.html.
- [22] John Harrison. Without loss of generality. In Stefan Berghofer, Tobias Nipkow, Christian Urban, and Makarius Wenzel, editors, Proceedings of the 22nd International Conference on Theorem Proving in Higher Order Logics, TPHOLs 2009, volume 5674 of Lecture Notes in Computer Science, pages 43–59, Munich, Germany,

2009. Springer-Verlag.

- [23] John Harrison. HOL Light: An overview. In Theorem Proving in Higher Order Logics, pages 60–66. Springer, 2009.
- [24] Cezary Kaliszyk and Alexander Krauss. Scalable LCF-style proof translation. In Sandrine Blazy, Christine Paulin-Mohring, and David Pichardie, editors, Proc. of the 4th International Conference on Interactive Theorem Proving (ITP’13), volume 7998 of LNCS, pages 51–66. Springer, 2013.


19

Hales et al. A formal proof of the Kepler conjecture

![image 345](<2015-hales-formal-proof-kepler-conjecture_images/imageFile345.png>)

- [25] Cezary Kaliszyk and Josef Urban. Learning-assisted automated reasoning with Flyspeck. J. Autom. Reasoning, 53(2):173–213, 2014. doi: 10.1007/s10817-014-9303-

3. URL http://dx.doi.org/10.1007/s10817-014-9303-3.

- [26] Cezary Kaliszyk and Josef Urban. Learning-assisted theorem proving with millions of lemmas. Journal of Symbolic Computation, (0):–, 2014. ISSN 0747-7171. doi: http://dx.doi.org/10.1016/j.jsc.2014.09.032. URL http://www.sciencedirect. com/science/article/pii/S074771711400100X.
- [27] Johannes Kepler. Strena seu de nive sexangula. Frankfurt: Gottfried. Tampach, 1611.
- [28] Gerwin Klein, Kevin Elphinstone, Gernot Heiser, June Andronick, David Cock, Philip Derrin, Dhammika Elkaduwe, Kai Engelhardt, Rafal Kolanski, Michael Norrish, Thomas Sewell, Harvey Tuch, and Simon Winwood. seL4: formal veriﬁcation of an OS kernel. In Jeanna Neefe Matthews and Thomas E. Anderson, editors, Proc. 22nd ACM Symposium on Operating Systems Principles 2009, pages 207–220. ACM, 2009.
- [29] Ramana Kumar, Rob Arthan, Magnus O. Myreen, and Scott Owens. HOL with definitions: Semantics, soundness, and a veriﬁed implementation. In Gerwin Klein and Ruben Gamboa, editors, Interactive Theorem Proving - 5th International Conference, ITP 2014, Held as Part of the Vienna Summer of Logic, VSL 2014, Vienna, Austria, July 14-17, 2014. Proceedings, volume 8558 of Lecture Notes in Computer Science, pages 308–324. Springer, 2014. ISBN 978-3-319-08969-0. doi: 10.1007/978-3-31908970-6 20. URL http://dx.doi.org/10.1007/978-3-319-08970-6_20.

![image 346](<2015-hales-formal-proof-kepler-conjecture_images/imageFile346.png>)

- [30] J. Lagarias. The Kepler Conjecture and its proof, pages 3–26. Springer, 2009.
- [31] Xavier Leroy. Formal certiﬁcation of a compiler back-end, or: programming a compiler with a proof assistant. 33rd ACM symposium on Principles of Programming Languages, pages 42–54, 2006. http://compcert.inria.fr/.
- [32] Victor Magron. Formal Proofs for Global Optimization – Templates and Sums of Squares. PhD thesis, Ecole´ Polytechnique, 2013.
- [33] Christian Marchal. Study of the Keplers conjecture: the problem of the closest packing. Mathematische Zeitschrift, 267(3-4):737–765, 2011. ISSN 0025-5874. doi: 10.1007/s00209-009-0644-2. URL http://dx.doi.org/10.1007/s00209-0090644-2.
- [34] Sean McLaughlin. An interpretation of Isabelle/HOL in HOL Light. In Ulrich Furbach and Natarajan Shankar, editors, IJCAR, volume 4130 of Lecture Notes in Computer Science, pages 192–204. Springer, 2006.
- [35] Ramon E Moore, R Baker Kearfott, and Michael J Cloud. Introduction to interval analysis. Siam, 2009.
- [36] Tobias Nipkow. Veriﬁed eﬃcient enumeration of plane graphs modulo isomorphism. In Van Eekelen, Geuvers, Schmaltz, and Wiedijk, editors, Interactive Theorem Proving (ITP 2011), volume 6898 of Lect. Notes in Comp. Sci., pages 281–296. SpringerVerlag, 2011.
- [37] Tobias Nipkow, Lawrence Paulson, and Markus Wenzel. Isabelle/HOL — A Proof Assistant for Higher-Order Logic, volume 2283 of Lect. Notes in Comp. Sci. SpringerVerlag, 2002. http://www.in.tum.de/˜nipkow/LNCS2283/.
- [38] Tobias Nipkow, Gertrud Bauer, and Paula Schultz. Flyspeck I: Tame graphs. In U. Furbach and N. Shankar, editors, Automated Reasoning (IJCAR 2006), volume 4130 of Lect. Notes in Comp. Sci., pages 21–35. Springer-Verlag, 2006.
- [39] Steven Obua. Proving bounds for real linear programs in Isabelle/HOL. In J. Hurd and T. F. Melham, editors, Theorem Proving in Higher Order Logics, volume 3603


20

Hales et al. A formal proof of the Kepler conjecture

![image 363](<2015-hales-formal-proof-kepler-conjecture_images/imageFile363.png>)

of Lect. Notes in Comp. Sci., pages 227–244. Springer-Verlag, 2005.

- [40] Steven Obua. Flyspeck II: The Basic Linear Programs. PhD thesis, Technische Universita¨t Mu¨nchen, 2008.
- [41] Steven Obua and Tobias Nipkow. Flyspeck II: the basic linear programs. Annals of Mathematics and Artiﬁcial Intelligence, 56(3–4), 2009.
- [42] Steven Obua and Sebastian Skalberg. Importing HOL into Isabelle/HOL. In Automated Reasoning, volume 4130 of Lecture Notes in Computer Science, pages 298–

302. Springer, 2006.

- [43] Alexey Solovyev. Formal Methods and Computations. PhD thesis, University of Pittsburgh, 2012. http://d-scholarship.pitt.edu/16721/.
- [44] Alexey Solovyev and Thomas C. Hales. Eﬃcient formal veriﬁcation of bounds of linear programs, volume 6824 of LNCS, pages 123–132. Springer-Verlag, 2011.
- [45] Alexey Solovyev and Thomas C. Hales. Formal Veriﬁcation of Nonlinear Inequalities with Taylor Interval Approximations. In NFM, volume 7871 of LNCS, pages 383–

397. 2013.

- [46] O. Tange. GNU parallel - the command-line power tool. ;login: The USENIX Magazine, 36(1):42–47, Feb 2011. URL http://www.gnu.org/s/parallel.
- [47] Carst Tankink, Cezary Kaliszyk, Josef Urban, and Herman Geuvers. Formal mathematics on display: A wiki for Flyspeck. In Jacques Carette, David Aspinall, Christoph Lange, Petr Sojka, and Wolfgang Windsteiger, editors, MKM/Calculemus/DML, volume 7961 of LNCS, pages 152–167. Springer, 2013. ISBN 978-3-642-39319-8.
- [48] Roland Zumkeller. Global Optimization in Type Theory. PhD thesis, Ecole´ Polytechnique Paris, 2008.


21

