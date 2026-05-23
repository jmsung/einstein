---
type: source
kind: paper
title: Cutting a Pancake with an Exotic Knife
authors: David O. H. Cutler, Jonas Karlsson, Neil J. A. Sloane
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2511.15864v3
source_local: ../raw/2025-cutler-cutting-pancake-exotic-knife.pdf
topic: general-knowledge
cites:
---

# arXiv:2511.15864v3[math.CO]19Apr2026

##### Cutting a Pancake with an Exotic Knife

David O. H. Cutler1 Mathematics Department Tufts University Medford, MA 02155 USA Email: david.cutler@tufts.edu

Jonas Karlsson Boden, 961 42 Sweden Website: jonka364.github.io Email: jonaskarls@gmail.com

Neil J. A. Sloane2 The OEIS Foundation Inc. Highland Park, NJ 08904 USA Visiting Scholar, Math. Dept. Rutgers University Piscataway, NJ 08854 Email: njasloane@gmail.com

Abstract

In the first chapter of their classic book Concrete Mathematics, Graham, Knuth, and Patashnik consider the maximum number of pieces that can be obtained from a pancake by making n cuts with a knife blade that is straight, or bent into a V, or bent twice into a Z. We extend their work by considering knives, or “cookie-cutters”, of even more exotic shapes, including a k-armed V, a chain of k connected line segments, long-legged versions of the letters A, E, H, L, M, T, W, or X, a convex polygon, a circle, a ϕ, a figure 8, a pentagram, a hexagram, or a lollipop (or qoppa). We also consider “constrained” versions of the long-legged letters A, H, L, T, and X. In most cases we are able to determine the maximum number of pieces, although for the constrained A and the lollipop we can only give bounds.

Like a long-legged fly upon the stream His mind moves upon silence.

W. B. Yeats, Long-Legged Fly [32]

### 1 Introduction

In this article we specify certain families of knives and then attempt to determine the maximum number of pieces that the plane can be divided into by making cuts from that family.

- 1Part of this work was carried out while D.O.H.C. was a participant in the 2025 DIMACS REU program at Rutgers University, NSF grant CCF-2447342.
- 2To whom correspondence should be addressed.


Examples of families are straight knives, V-shaped knifes, and circular knives (or cookie cutters). For example, the members of the family of V-shaped knives consist of two rays emanating from a point, with an arbitrary angle between the rays. The family of circular knives consists of all circles of nonzero radius and arbitrary center. For a given family S of knives, we wish to determine the maximum number of pieces into which the affine Euclidean plane can be decomposed by using n ≥ 0 cuts, where each cut is chosen independently from the family. We denote this number by aS(n).

The classic example of a family is the set of all infinite straight lines, which we denote by K (for ”knife”). This is the famous pancake-cutting problem3 [2], [5, pp. 72–73], [9, Ch. 20], [10, §1.2], [21, Ch. 1], [25, Ch. III], [28], [31, p. 13, Problem 44], for which the answer is that the maximum number of pieces of an infinite pancake that can be obtained with n straight cuts is

aK(n) = n(n + 1)/2 + 1 . (1)

We give a proof and an explicit construction in §5. Figure 1 shows solutions for 1 ≤ n ≤ 5 cuts.

Figure 1: The classical pancake-cutting problem: For the family K of infinite straight lines, the plane (an infinite pancake) can be cut with 1, 2, 3, 4, or 5 cuts into a maximum of 2, 4, 7, 11, or 16 pieces, respectively. Arrowheads indicate infinite lines.

For this family, the numbers (aK(n))n≥0 form entry A000124 in the On-Line Encyclopedia of Integer Sequences (or OEIS) [23]. Six-digit numbers prefixed by A will always refer to entries in the OEIS.

When we began this investigation, the OEIS already contained several other sequences of this type. The following list includes both pre-existing and new sequences. An asterisk ∗ indicates a sequence which was not hitherto associated with a dissection problem. We believe that our solutions (or, in two cases, partial solutions) to the problems indicated by the asterisks are new.

The sequences, associated families S, and section numbers if they are mentioned in this article, are as follows. The list is ordered by A-number, which is roughly the chronological order in which they were added to the OEIS (and not the order in which they were discovered, which would be difficult to determine).

A000124 (S is the family K of knife cuts, §§1, 5), A000125 (the family of planes in three dimensions), A046127 (spheres in three dimensions), A051890 (ellipses in the plane), A058331

3Also known as the pizza-cutting problem, although we prefer “pancake-cutting”, because pizzas often have a well-defined border and for our problems the natural setting is the infinite affine Euclidean plane, which seems more like a pancake than a pizza.

(hyperbolas in the plane), A069894 (squares or convex quadrilaterals, §12.1), A077588 (triangles, §1), A077591 (concave quadrilaterals), A080856∗ (4-chains, §8), A084849∗ (constrained X’s, §12.2), A117625 (constrained Z’s or zig-zags, §11), A125201∗ (constrained W’s or M’s, §11), A130883 (V’s, §7), A140063 (constrained H’s or ϕ’s, §12.3), A140064∗ (A’s, E’s, 3armed V’s, 3-chains, Wu’s (ᗐ), ( ), §§7, 9), A143689∗ (constrained L’s, §12.1), A330451∗ (constrained A’s, §13.2), A383464∗ (4-armed V’s, §7), A383465∗ (5-chains or H’s, §§8, 12.3), A383466∗ (pentagrams, §14.3), A386477∗ (hexagrams, §14.3), A386480 (circles (O), §15.1), A386485∗ (pentagons, §14.1), A386486∗ (8’s, §15.2), A389614∗ (constrained T’s, §13.1), A389624∗ (lollipops or qoppa ( ϙ ), §15.3), A393442 (unions of circles and lines, §12.4), and A393448∗ (wynns ( ᚹ ), §10).

In the two cases (A and lollipops) where we do not know the exact number of regions, the sequences mentioned are upper bounds. The second and third entries in the above list, A000125 and A046127, are the only three-dimensional families. From this point on, we will only consider two-dimensional families.

We will give references to the OEIS throughout this article, for several reasons. One is that much of the previous work on these problems first appeared in the OEIS rather than in a journal. We would appreciate hearing of any references we have overlooked, especially for the more exotic families. Another reason is that the OEIS entries include the initial terms of the sequence, additional formulas and illustrations, references, etc.

As we shall see, the OEIS also led us to make two unexpected discoveries. First, the sequences (aS(n))n≥0 where S is any one of three families, long-legged A’s, Wu’s, or 3-chains, are identical (§§7, 8, 9). Second, the sequences (aS(n))n≥0 where S is either the family of octagons or of concave quadrilaterals are identical (§14.2). For the first we give a geometric explanation, whereas the second may be simply a coincidence caused by the fact that the same formula arises in two different but closely related contexts.

### 2 Long-legged letters and other knives

Our interest in these exotic knives was kindled by two problems in the first chapter of Graham, Knuth, and Patashnik’s Concrete Mathematics [10], where, after discussing the classical pancake-cutting problem, they ask what would happen if the infinite knives were bent into the shape of a V with two very long limb:

or bent twice so as to make a “zig-zag”, with two long parallel limbs joined by a diagonal line segment:

In order to generalize these unusual knives, we observe that they may be regarded as “longlegged” versions of the upper-case letters V and Z, and of course an infinite straight knife can be regarded as a long-legged upper-case I. (The term was suggested by W. B. Yeats’s poem in praise of silence, Long-Legged Fly [32, pp. 327–328].)

This led us to consider families of long-legged versions of other letters. Informally, a long-legged version of a letter is obtained by replacing any protruding arms or legs by (semiinfinite) rays, indicated by arrow-heads in the figures, allowing arbitrary angles between these rays. For example, there is no restriction on the angle between the two arms of a long-legged V. We will, of course, be careful to give a precise definition for each family.

There are interesting long-legged versions of A,E,H,L,M,T,W, and X. Curved letters (B,C,D,G,P,Q,R,S, ...) do not seem appropriate for this treatment, since as we shall see, once curved knives are permitted (without any bound on their curvature), it is easy to create arbitrarily many regions with just one or two cuts. We do include four curved shapes, ϕ (§12.3), O (§15.1), 8 (§15.2), and the lollipop ϙ (§15.3), that are are based on just one or two circles.

A knife with the shape of a long-legged A initially looked challenging, although as we shall see in §9, it has a surprisingly simple solution. On the other hand, the constrained long-legged A (§13.2) appears to be genuinely hard, and it and the lollipop (or qoppa) family are the two families where we do not even have a conjectured solution (see Tables 6 and 8) .

Long-legged versions of some letters (A,H,L,T,X, among others) are potentially interesting, but because our rules allow arbitrary angles between the extended legs, they would be indistinguishable from other letters. An L would be the same as a V, for example. We therefore define families of “constrained” long-legged letters, indicated by a bar over the letter, which impose additional conditions. Examples (which include the zig-zag knife Z from [10]) will be found in Sections 12 and 13.

These constrained letters appear to be more difficult to analyze, and we will therefore separate the families we consider into two main genera, adopting a term from biology. We are working in the affine Euclidean plane, which is acted on by the full two-dimensional affine group Gaff, generated by linear transformations (which need not be isometries), followed by translations. If S is a family of knives, we define its symmetry group G(S) to be the largest subgroup of Gaff which preserves S, that is, has the property that, for any g ∈ G(S) and any s ∈ S, we have g(s) ∈ S.

The two genera are the affine genus, consisting of those families S for which G(S) = Gaff, and the similarity genus, consisting of those families for which G(S) = Gsim, the group of all similarity transformations, generated by translations, reflections, rotations, and dilations (or rescaling). We further split each of these genera into two subgenera, depending on whether or not the symmetry group G(S) acts transitively on S. Table 1 shows how our principal families fall into these four subgenera. (These families will be defined in the following sections.) We hope that this table, combined with the list given in §1, will bring order into what might

- seem like a bewildering array of shapes.


|genus|Gaff|Gsim<br><br>|
|---|---|---|
|transitive intransitive<br><br>|K(5), (6),A(9),ᚹ(10) kV (7),kC(8)<br><br>|L,X,H,ϕ(12),T(13),O,8,ϙ(15) Z,W (11),A(13)<br><br>|


Table 1: Principal families of knives classified into four subgenera, together with their section numbers.

Of course there are other important subgroups of Gaff that we could have focused on. If our knives were circles of a fixed radius, the appropriate subgroup would be the group Giso of isometries of the plane, which is strictly contained in the group of similarities: Giso ⊂ Gsim ⊂ Gaff. Or we might wish to study only orientation-preserving transformations. But neither of these groups will be considered here.

As their symbols suggest, the families O, 8, ϕ, and ϙ , are defined in terms of circles, which puts them in the similarity genus, since affine maps do not take circles to circles. Likewise, as their symbols suggest, the families L, X, and T involve perpendicular lines, and so are also not affine.

For a transitive family of knives, any single example will serve as a holotype, or typical member. We will call such a family holotypic, and it can be specified simply by giving its symmetry group and the holotype.

Since Gaff is 3-transitive, the family of non-degenerate triangular knives is a holotypic member of the transitive affine subgenus. In contrast, the family of right-angled triangular knives is an intransitive, or heterotypic, member of the similarity subgenus.

For the family of non-degenerate quadrilaterals (or those using any polygon with more than three vertices), the symmetry group is Gaff, which now acts intransitively, since there are not enough transformations in Gaff to take one quadrilateral to any other. Similarly, for k > 2, k-chains and k-armed V’s also have too many degrees of freedom to be holotypic. In a heterotypic family S, there would be a holotype for each orbit of the action of G(S).

Generally speaking, the bigger the group G(S), the easier it is to find aS(n), because there are more possibilities for the next knife. Intransitive families also give us more freedom.

### 3 Further remarks on the families

For a given family S of knives, our strategy for attempting to determine aS(n) is to select n members of S and analyze the planar graph ΓS(n) formed by their union. We describe this graph in §5, using the classical case when the knives are lines as an illustration.

Subsequent sections will then discuss other shapes, roughly in order of increasing complexity, beginning in §6 with the half-line or ray (§6). To emphasize the difference between a line and a ray, we refer to a ray as a hatpin, with symbol (see Fig. 6 below for some drawings of hatpins).

The next-simplest shape after the hatpin is the V, and in §7 we will analyze a long-legged k-armed V for k ≥ 2. The three-armed V, ᗐ, is particularly interesting. It is called a Wu, and is included in the Unified Canadian Aboriginal Syllabics section of Unicode, where it has the symbol U+15D0. The Wu has also been called a Boolean OR with a middle stem (U+2A5B). The numbers of regions obtained from a long-legged E or Shah ( ) turn out to be the same as for a Wu, so we simply define long-legged E’s and Shah’s to be long-legged Wu’s.

The sections following the multi-armed V are devoted to the multi-armed k-chain (§8), the long-legged A (§9), and the wynn, a Middle English rune (§10). These are followed by the constrained long-legged letters Z, W, and M (§11), and in §12 by L, X, H, and ϕ. Our solution to the H family given in (20) led us to D. Kinsella’s work on the ϕ family, where the

same formula as for H appears, although without proof. However, this formula, (20), had already been given 200 years earlier by J. Steiner [28], as we briefly discuss in §12.4. Two further (and more difficult) constrained letters, T and A, follow in (§13). We study several finite shapes in §14, namely a convex k-sided polygon (§14.1, §14.2), a

regular pentagram and hexagram (§14.3), and then three curved families the circle (§15.1), figure 8 (§15.2), and ending with the lollipop or qoppa ( ϙ ) (§15.3).

Our methods can be applied to many shapes besides these, and could be used to provide proofs for many formulas stated without proof in the OEIS entries mentioned in our initial list.

The final section lists some open problems. One in particular is worth emphasizing: is there any connection between the present work and the classical subject of “Geometrical Configurations” [14, 15, 18]? Many of our graphs are in fact geometrical configurations, so it is natural to wonder if any results from the classical literature can be applied to our problem.

![image 1](<2025-cutler-cutting-pancake-exotic-knife_images/imageFile1.png>)

Figure 2: A 6-set Venn diagram (with 64 regions) constructed from six copies of a sausage shape S, from Gru¨nbaum [13]. (A circle is a very simple sausage.) The construction easily generalizes to show that at least 2n regions can be achieved using n copies of a simple Jordan curve.

For most of the families that we consider (and also for most of those on the list at the start of this Introduction), aS(n) grows quadratically with n. For triangles (A077588), for example, aS(n) = 3n2 − 3n + 2 for n ≥ 1. It is possible, however, for aS(n) to grow much more rapidly than this. For example, Gr¨unbaum’s n-set Venn diagram construction [13, 27] (see Fig. 2 for n = 6), shows that if S is a simple Jordan curve, a snake or sausage shape, for example, we can achieve aJC(n) ≥ 2n. In fact, aJC(2) is already unbounded, since it can be made as large as we please by intertwining two snakes (as in drawings of a caduceus). Of course the very definition of a Jordan curve implies aJC(1) = 2. But even aS(1) itself can be arbitrarily large if S is a twisted sausage (Fig. 3). To avoid such complications, we will mostly only consider polygonal shapes.

Figure 3: A single twisted sausage shape can produce arbitrarily many regions.

### 4 Notation

Many of our knife families are named after letters of the alphabet, so in order to distinguish between the names of the families and the mathematical symbols used for their properties, we will use a sans serif font (A, L, V, etc.) for the families. Other family names are K for the infinite knife-cuts in the basic pancake-cutting problem, for the hatpin family, kV for the k-armed V’s, kC for the k-chains, kP for the k-sided polygons, O for circles (it should really be O, but we omit the bar for aesthetic reasons), and St (honoring Steiner) for knives formed from m circles and n lines. An overbar (L, X, etc.) indicates a constrained shape.

For a family S, s ∈ S is a knife in the family, ΓS(n) is any graph formed by drawing n knives s ∈ S, and aS(n) is the maximum number of regions in any ΓS(n). We will say that ΓS(n) is optimal if it has aS(n) regions. Red and black dots in ΓS(n) usually indicate base and crossing nodes, respectively (these terms will be defined in the next section).

The parameters of ΓS(n) will be denoted by VB, VC, V = VB +VC (numbers of base nodes, crossing nodes, total vertices), E∞, Ef, E = E∞ + Ef (infinite edges, finite edges, total edges), and R∞, Rf, R = R∞ + Rf (infinite regions, finite regions, total regions). Also α denotes the total number of arms in the graph, and cpa is the average number of crossing nodes per arm.

For individual knives, σ(S) is the maximum number of self-crossings in a single s ∈ S, κ(S) is the maximum number of intersections between s ̸= s′ ∈ S, and ξ(S) (which will not appear until §13.2) is a local intersection number.

The exotic symbols used in this article are: ᗐ (Unified Canadian Aboriginal symbol Wu, §3), (hatpin, §6), ᚹ (wynn, a Middle English rune, §10), and ϙ (lollipop or archaic Greek letter qoppa, §15.3).

### 5 The planar graph and the maximum number of regions

Given a family S, we start by thinking of the knives s ∈ S as planar graphs with certain vertices and edges. We call the vertices of s base nodes and its edges arms. A long-legged V, for example, has a single base node and two arms. A k-chain (§8) has k − 1 base nodes and k arms.

The planar graph ΓS(n) for a drawing formed from n knives s ∈ S is then the union of the graphs for the individual knives, together with a new vertex for any point where a pair of arms cross, and new edges that replace the portions of the arms between the new vertices. We will refer to these new vertices as crossing nodes. The arms of an s ∈ S may themselves cross, and these self-crossings are also considered to be crossing nodes. In some drawings the

base nodes are indicated by small red circles, and the crossing nodes by small black circles. (We have not done this in every drawing, to avoid clutter.)

We denote the set of base nodes for all n knives by B, and the degree of v ∈ B by dv, or by dB if the degree is the same for all v ∈ B.

Since our goal is always to maximize the number of regions, we will assume that no crossings ever involve more than two arms, and that no arm from one s intersects a base node from a different s (for otherwise a small perturbation would increase the number of regions). Since we are constructing these graphs ourselves, it is clear that these assumptions are justified. A similar perturbation argument is briefly mentioned in [20, p. 128].

Let VB denote the total number of base nodes over all n knives, VC the total number of crossing nodes, and V = VB + VC the total number of vertices of ΓS(n). Let E∞ and Ef respectively denote the number of infinite and finite edges, and E = E∞ + Ef the total number of edges, and similarly let R∞, Rf, and R = R∞+Rf denote the numbers of infinite, finite, and total regions.

If the knives s ∈ S are bounded and E∞ = 0, Euler’s formula [4, p. 22], [11, Ch. 8], [12, §2.2], [17] for ΓS(n) tells us that

R − E + V = 2 . (2) This version of Euler’s formula will be relevant in §14. But most of the knives we consider are infinite, with E∞ = R∞ > 0, in which case Euler’s formula for the Euclidean (or affine) plane tells us that ΓS(n) satisfies

R − E + V = 1 . (3)

We were surprised not to find (3) in Lakatos [17], a book devoted to proofs of different versions of Euler’s formula, nor in the standard books on finite graph theory. But (3) is simple to prove. Draw a rectangle around ΓS(n), large enough so that only the E∞ edges cross it. The rectangle itself (the frame) therefore has 4 +E∞ edges and 4 +E∞ vertices. Discard all portions of the E∞ edges that are outside the frame. The resulting finite graph has E+4+E∞ edges, V + 4 + E∞ vertices, and by (2) has (E + 4 + E∞) − (V + 4 + E∞) + 2 = E − V + 2 regions. But this includes the exterior of the rectangle, so inside the rectangle there are V − E + 1 regions, which establishes (3).

Let us assume then that the knives in S are connected graphs formed from straight line segments, some of which may be infinite. What greatly simplifies the analysis of ΓS(n) is that there is a second equation linking E and V , which we obtain by counting edge-vertex incidences in two ways. On the left side of this equation we sum the degrees dv of all the base nodes v ∈ B and add four times the number of crossing nodes. This will count each edge twice, except for the E∞ infinite edges, which will only be counted once, and so we add an extra term E∞ to the left side. On the right side we simply count each edge twice. The edge-vertex count then tells us that

that is,

dv + 4VC + E∞ = 2(E∞ + Ef) , (4)

v∈B

- 1

- 2 v∈B


Ef = 2VC +

dv −

- 1

- 2


E∞ . (5)

By combining this with Euler’s formula (3), we obtain our basic equation, which is

- 1

- 2


- 1

- 2 v∈B


dv − VB +

E∞ + 1 . (6)

R = VC +

On the right side, only VC depends on how the knives are placed in the plane, the other quantities being determined by S and n, and so we deduce that, for the families we are considering,

to maximize the number of regions, it is necessary and sufficient to maximize the number of crossings. (7)

Note that this conclusion holds both for finite and infinite knives: the constant term in the formula is different in the two cases, but its value is irrelevant.

We now illustrate this by studying the classic pancake-cutting problem mentioned in the Introduction, for which the knives s ∈ K are infinite straight lines, such as the line y = 0 (the “holotype”), or any of its images under the affine group Gaff. The knives s have one arm each and no base vertices. We form the pancake graph ΓK(n) by drawing n ≥ 2 such lines. We may assume that each line crosses at least one other line, so VB = 0 and E∞ = 2n. Equation (6) then says that

R = VC + n + 1 . (8)

We maximize VC by making every pair of lines intersect, giving VC = n2 , and so the maximum number of regions is R = aK(n) = n2 + n + 1, establishing (1).

The underlying reason that (7) holds is that, because our shapes are built out of straight lines, locally the graphs have a tendency to look like a square mesh, with E ≈ 2V (cf. (5), (13)). This also explains why the associated sequences (aS(n)) have only quadratic growth.

- 0 1 2 3 4 5 6 7 8 9

−3

−2

−1

- 1

- 2

- 3

- 4

- 5


Figure 4: An optimal pancake graph GK(7) defined by (9) with n = 6 and θ = 15◦. The t = 0 line is the x-axis, and the t = 6 line is x = 6.

Since the optimal pancake graph ΓK(n) is the basis for other constructions, we summarize its properties: V = VC = n2 , E∞ = R∞ = 2n, Ef = n(n − 2),E = n2, Rf = n−21 , and

R = aK(n) = (n2 + n + 2)/2 (A000124). Our very first figure, Figure 1 above, shows some ad hoc drawings of these graphs. The following is an explicit construction of an optimal pancake graph with N + 1 ≥ 2 lines. Let θ = π/(2N), and take the lines to have equations

(x − t)sintθ = y costθ for t = 0,1,...N . (9) Figure 4 illustrates the construction of a ΓK(7), taking N = 6 .

For use in §14 and §15 we give the analog of our basic equation (6) that applies if the knives s ∈ S are finite graphs. Since E∞ = 0, the equation is now

- 1

- 2 v∈B


dv − VB + 2 . (10)

R = VC +

We end this section by defining three parameters associated with a family S that are helpful when searching for optimal graphs. First, if the definition of S permits, it may be possible to move the arms of S so as to increase the number of self-crossings (this applies to the k-chain, for example). We let σ(S) denote the maximum number of self-crossings in a single s ∈ S.

Second, κ(S) will denote the maximum number of intersections between two knives s ̸= s′ ∈ S. With n copies of S, an upper bound on the total number of crossings is therefore

n 2

VC ≤ nσ(S) +

κ(S) . (11)

If equality holds in (11), the graph is optimal.

In many of the examples studied in this article, we are able to achieve equality in (11). The chief difficulty, once we have determined κ(S), lies in placing the n knives so that every pair intersect in κ(S) points. We run into difficulties if, once one s has been positioned, there is only a small range of possibilities for the second (and therefore all) subsequent copies. This is the case for the constrained letters T (§13.1) and A (§13.2), the figure 8 (§15.2), and the lollipop (§15.3).

Third, by assumption, each crossing node is at the intersection of exactly two arms, and so the average number of crossings per arm (abbreviated cpa) is

nσ(S) + n2 κ(S) α(n)

2VC α(n) ≤

cpa =

, (12)

where α(n) is the total number of arms. The cpa is not always an integer, even for optimal graphs (the k-chains for k ≥ 3, for example). But if the right side of (12) is an integer, the cpa can be useful when searching for optimal graphs. If in the graph we are currently trying to optimize there is an arm with fewer than cpa crossings, then either that arm needs to be changed, or it is a signal that the bound in (12) cannot be achieved.

### 6 The hatpin

We define a hatpin to be a planar graph consisting of a distinguished point, its head, with a ray emanating from it. The family of all hatpins will be denoted by ( ). Its group is Gaff, which acts transitively, and for holotype we may take the ray {x = 0, y ≤ 0} with head (0,0). A graph Γ (n) formed by drawing n hatpins has VB = n base nodes, dB = 1, and E∞ = n, so (6) gives R = VC + 1, which we maximize by making all the hatpins cross each other, giving a (n) = n2 + 1. The left-hand figure in Figure 6 below shows a Γ (4). In some drawings we have indicated the heads of the hatpins by small red circles.

Since the optimal hatpin graph Γ (n) is also used in other constructions, we note that it

has parameters VB = n,dB = 1,VC = n2 ,V = n+12 , E∞ = R∞ = n, Ef = n(n−1),E = n2, Rf = n−21 , and R = aK(n − 1) = (n2 − n + 2)/2.

Figure 5: A graph G3V(2) with 14 regions, formed from two 3-armed V’s (or Wu’s).

|k\n|0 1 2 3 4 5 6 7 8 ...<br><br>|
|---|---|
|0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>|1 1 1 1 1 1 1 1 1 ...<br><br>1 1 2 4 7 11 16 22 29 ...<br><br><br>1 2 7 16 29 46 67 92 121 ...<br><br>1 3 14 34 63 101 148 204 269 ...<br><br>1 4 23 58 109 176 259 358 473 ...<br><br>1 5 34 88 167 271 400 554 733 ...<br><br>1 6 47 124 237 386 571 792 1049 ...<br><br>1 7 62 166 319 521 772 1072 1421 ...<br>|


Table 2: Table of akV(n), the maximum number of regions formed in the plane by drawing n long-legged k-armed V’s. The entries are given by (14). Rows 1-4 are A000124, A130883, A140064, A383464, column 2 is A008865, the main diagonal is A393441, and the OEIS entry for the array itself is A386481.

### 7 The k-armed V

Our next shape is a long-legged k-armed V, which we define to consist of a distinguished point, its tip, with dB = k ≥ 1 rays, or arms, emanating from it, with arbitrary angles between the arms. We denote the family of all such knifes by kV. Its group is Gaff, but if k > 2 it does not act transitively: this is a heterotypic family. A graph ΓkV(n) formed by drawing n ≥ 0 k-armed V’s has VB = n base nodes and nk arms, with E∞ = R∞ = nk. For maximizing the number of regions, it turns out to be best to take the arms to be distinct, and forming a fan with a small angular spread, as in Figs. 5 and 6.

From Equations (5) and (6) we obtain Ef = 2VC, R = VC + n(k − 1) + 1 . (13)

The crossing number κ(kV) is clearly k2. We maximize VC by making every pair of kV’s cross each other in k2 points, for a total value of VC = n2 k2, leading to the maximum of

R = akV(n) =

n 2

k2 + n(k − 1) + 1 (k ≥ 1,n ≥ 0) (14)

regions.4 This is easily achieved by taking a Γ (n) hatpin graph and replacing the hatpins by long narrow k-armed V’s. (see Fig. 6, which illustrates the construction for four 3-armed V’s). We note that for k = 2 our counts match those of [10], as they should. Those authors give a different explicit construction. They also note (as their Exercise 19) that imposing a minimal angle between the arms of the V makes this maximal count unattainable; whichever construction we use, the V’s must necessarily get thinner and thinner. Table 2 shows the values of akV(n) for 0 ≤ k ≤ 7 and 0 ≤ n ≤ 8.

|k\n|0 1 2 3 4 5 6 7 8 ...<br><br>|
|---|---|
|0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>|1 1 1 1 1 1 1 1 1 ...<br><br>1 2 4 7 11 16 22 29 37 ...<br><br><br>1 2 7 16 29 46 67 92 121 ...<br><br>1 3 14 34 63 101 148 204 269 ...<br><br><br>1 5 25 61 113 181 265 365 481 ... 1 8 40 97 179 286 418 575 757 ... 1 12 59 142 261 416 607 834 1097 ... 1 17 82 196 359 571 832 1142 1501 ...<br><br>|


Table 3: Table of akC(n), the maximum number of regions formed in the plane by drawing n k-chains. The entries are given by (16). Rows 1-5 are A000124, A130883, A140064, A080856, A383465, columns 1 and 2 are A152948 and A386479, the main diagonal is A387525, and the array itself is A386478.

.

4The k = 3 case of (14), (9n2 − 5n + 2)/2 (A140064), was first discovered by Edward Xiong, Jonathan Pei, and David O. H. Cutler on June 24 2025 (see Acknowledgments).

- I
- II
- III
- IV


V

Figure 6: Transforming a hatpin graph GH(4) to an optimal G3V(4) graph with a3V(4) = 63 regions, by replacing hatpins with long narrow 3-armed V’s (or Wu’s). The new graph has VC = 54 crossings and α(3V) = 12 arms, and a cpa of 9, in agreement with (12). (Some of the arrowheads on the right have been omitted for clarity.)

We may verify (14) directly by considering what happens to the different parts of the hatpin graph when the hatpins are replaced by kVs. There are five parts in the hatpin graph, which we denote by I (base nodes), II (finite edges), III (crossing nodes), IV (cells), and V (infinite edges), as shown in Fig. 6. Each crossing node, for example, becomes a k × k grid with κ(kV) = k2 vertices, 2k(k − 1) edges, and (k − 1)2 regions, and there are n2 such crossing points, as we know from the last paragraph of §6. By combining these counts for the five parts we can verify (14).

### 8 The k-chain

We define a k-chain for k ≥ 1 to be any continuous plane curve made up of k piecewise linear segments. A line is a 1-chain, and a V is a 2-chain. Since it can only help in increasing the number of regions, we will assume that the outer line segments (the first and the kth) are infinite. The other segments are required to be finite. We make no restriction on the lengths of the finite segments, nor on the angles between them, and we allow self-intersections. Thus a k-chain for k ≥ 2 is essentially an ordered set of k − 1 points in the plane, with successive points joined by line segments and with semi-infinite rays attached to the first and last point. We denote the family of all such knifes by kC. Its group is Gaff, but (as in the previous section) if k > 2 it does not act transitively: this is also a heterotypic family. (The reason is that a k-chain has 2k degrees of freedom: 2(k − 1) to choose the base nodes in the plane and another 2 to describe the infinite rays.)

A single k-chain may intersect itself if k ≥ 3, producing a maximum of k−21 internal regions and σ(kC) = k−21 self-intersections.

A graph ΓkC(n) formed by drawing n k-chains has VB = n(k − 1) base nodes and nk

- Figure 7: Long narrow drawings of a 3-chain, a 4-chain, and a 5-chain, used in the proof of (16). The first two are essentially unique, but there are two ways to draw the 5-chain–see Fig. 10.

- Figure 8: Transforming a pancake graph GK(3) to an optimal G3C(3) graph with a3C(3) = 34 regions, by replacing the knife cuts by long narrow 3-chains.


arms, with dB = 2, and E∞ = 2n. The basic equation (6) then gives R = VC + n + 1 , (15)

just as for the pancake graph (see (8)). So again we must maximize VC, which we can do by first maximizing the self-intersections in each k-chain, giving n k−21 intersections, and then using a construction similar to that of the previous section. That is, we draw the individual k-chains as long narrow graphs (as in Fig. 7), and then substitute them into a pancake graph if k is odd (and the k-chain has infinite edges pointing in opposite directions), or into a hatpin graph if k is even (and both infinite edges of the k-chain point in the same direction). See Fig. 8, which illustrates the construction for three 3-chains. As a result we obtain VC = n k−21 + n2 k2, and a maximum of

k2n2 2 −

3kn 2

R = akC(n) =

+ 2n + 1 , (16)

regions. The cpa for an optimal graph is 2VC/nk, which is an integer if and only if k ≤ 2. Table 3 shows the values of akC(n) for 0 ≤ k ≤ 7 and 0 ≤ n ≤ 8.

The k = 2 rows of Tables 2 and 3 are of course identical, since a 2-chain is the same as a 2-armed V. The k = 1 rows agree except that they are offset from each other by one position. The reason for this is that a 1-chain is a line, whereas a 1-armed V is a hatpin (V’s have a distinguished point, lines do not.) But the real surprise is that the k = 3 rows of the two tables agree. This will be explained in the next section.

![image 2](<2025-cutler-cutting-pancake-exotic-knife_images/imageFile2.png>)

Figure 9: The six ways to draw five lines in general position in the plane [Jonathan Wild and Lawrence Reeves, from A090338]. (The arrowheads are not shown.) Only the first two correspond to 5-chains (see Fig. 10).

Before leaving this section we mention another, somewhat surprising, property of Table 3: it is very nearly symmetrical. For example, a4C(3) = 61, while a3C(4) = 63. This is easily explained by the formula: from (16), |akC(n) − anC(k)| = 2|k − n|, which is exactly the difference between the numbers of infinite regions in the two optimal graphs. Indeed, if we define bkC(n) to be the maximum number of bounded regions in any arrangement of n k-chains, (16) implies that

3 2

- 1

- 2


(kn)2 −

kn + 1,

bkC(n) =

since the 2n edges extending to infinity create 2n unbounded regions. This expression is manifestly symmetric in k and n. So we understand the near-symmetry algebraically.

We can also give a geometric explanation. One possible explanation might have been that there is a 1-to-1-correspondence between optimal ΓkC(n) graphs and optimal ΓnC(k) graphs. But this is false even in the simplest case. An optimal Γ1C(n) graph consists of n lines in general position in the plane, and the number of such graphs is known for 0 ≤ n ≤ 9 (A090338):

1,1,1,1,1,6,43,922,38609,3111341,... Figure 9 shows the six ways to draw five lines in general position. On the other hand, ΓkC(1) is a single optimal k-chain (meaning it has σ(n) = n−21 self-intersections) and the number

Figure 10: The two optimal 5-chains.

of such graphs for 0 ≤ k ≤ 5 is 1,1,1,1,1,2,..., the two optimal five-chains being shown in Fig. 10.

Figure 11: A pentagon and its stellation. The edges of the pentagon are replaced by lines, creating five new bounded regions and ten infinite regions.

However, the symmetry can be explained by invoking the classical process of stellation ([6], [7, pp. 168–173], [29, Part II]). For polyhedra, stellation refers to extending the faces to create new regions, and can be carried out in stages, so that a polyhedron can have multiple stellations. We do not need this level of detail, so for our planar figures, we interpret stellation to mean that all rays and line segments are extended to infinite lines in a single step. The terminology is illustrated in Figure 11.

Figure 12: When an optimal chain is stellated (here, a 5-chain), only unbounded regions are added.

So let us take an optimal configuration of n k-chains, and stellate it. No new bounded regions can be created. This is because in such a configuration, any two rays or segments must already intersect: either they are consecutive elements of the same chain, in which case they share an endpoint, or else they intersect as a consequence of optimality (recall that we have already established that such configurations are possible). In either case, the stellation creates no new intersections, but only adds rays going off to infinity. This is readily

- seen to be the case in the optimal configurations already depicted. For example, stellating the lowermost chain in Figure 7 produces Figure 12, in which only unbounded regions are created. Figure 13, on the other hand, shows a non-optimal situation.


Figure 13: If the stellation of a chain produces new bounded regions, the chain was not optimal to start with.

Thus, stellating an optimal configuration of n k-chains produces a configuration of kn lines, all of which intersect pairwise; and the number of bounded regions in the resulting configuration is the same as the number of bounded regions in the original chain configuration. This explains the observed symmetry.

It would be interesting (see §16) to know further terms in the enumeration of optimal k-chains, and, more generally, the numbers of graphs that achieve any of the values shown in Tables 2 and 3.

Figure 14: 14 regions can be obtained with two long-legged A’s. The crossbars are shown in red.

### 9 The long-legged A

Our next knife is a long-legged A, which is a long-legged 2-armed V (§7) with a crossbar joining the two arms::

The crossbar need not meet the arms at the same distance from the tip, and the angle between the arms of the V is arbitrary. Equivalently, a long-legged A is a triangle where the two sides incident with a vertex have been extended to rays pointing away from that vertex. The family A of all such knives has symmetry group Gaff, which acts transitively.

Our drawings suggested that the initial values of aA(n), the maximum numbers of regions achievable with n A’s, for n = 1,2, and 3, were 3, 14 (Fig. 14), and 34, matching the counts for both 3-armed Vs and 3-chains. This was not a coincidence!

Theorem 1. The maximum number of regions that can be formed in the plane by drawing n long-legged 3-armed V’s, or n 3-chains, or n long-legged A’s, is (9n2 −5n+ 2)/2 (A140064).

The theorem also applies to long-legged versions of the letters E, ᗐ, and .

Figure 15: Converting an optimal graph with n long-legged A’s (left) into a graph with n 3-armed V ’s (right). The steps do not decrease the number of regions. Reversing the last step (going from right to center) performs the inverse operation.

Sketch of proof. We have already established the theorem for 3-armed V’s (in §7) and 3-chains (in §8). It remains to consider long-legged A’s.

Let G be an optimal arrangement of n long-legged A’s. Take the crossbar of any A, and suppose the left end of the crossbar is closer to its tip, and the right end is further from its tip. Slide the left end of this crossbar so it is closer to the tip than any crossing node on that arm, and slide the right end of the crossbar so that it is further from the tip than any other crossing node on that arm. This is illustrated in Figure 15. We claim that after this operation has been performed on all A’s, the resulting configuration is still optimal. Indeed, the legs have not been moved at all, hence all their intersections are intact. The crossbar of any A must now intersect all legs of all the other A’s in the configuration, and all pairs of crossbars must intersect, as illustrated in Figure 16.

Figure 16: After sliding, the crossbars join alternate sides of the quadrilateral formed by the legs of the As and so must intersect.

Finally, we can move the left end of the crossbar so it actually coincides with the tip and the right end so it is cut free from its arm. This A has now become a 3-armed V, and since G was optimal, the number of regions has remained unchanged throughout the process. By repeating this operation for all the A’s in G we turn the A graph into a 3-armed V graph. The converse operation is equally simple.

Figure 17: Converting a long-legged A (left) into a 3-chain (right),

On the other hand, to convert the long-legged A graph G into an arrangement of 3-chains, we simply apply the transformation shown in Fig. 17 to each A. This preserves the number of regions (we invite the reader to apply it to Fig. 14 and check that the result still has 14 regions).

### 10 The wynn

In this section we consider the Runic (and Middle English) letter wynn ( ᚹ ). One reason this family of knives is interesting is that it provides a counterexample to a conjecture we once made, that for any family in the affine genus it would be possible to achieve equality in Equation (11). This would have been a powerful result, for it would have meant that the maximal number of crossings between any number of copies of an affine shape was limited solely by the number of self-crossings and the number of crossings between two copies, with

no additional restrictions required for three or more copies. The wynn family will show that our belief was too optimistic.

Figure 18: A wynn.

We define a wynn to be a (non-degenerate) triangle, one of whose sides has been extended to an infinite ray (Fig. 18). One instinctively draws an isosceles triangle, but the triangle may be equilateral, isosceles, or scalene. Any two such figures are equivalent under the affine group Gaff, since as already mentioned in §2, this group is 3-transitive. Two wynns can

Figure 19: Two wynns can intersect in 7 points and divide the plane into 10 regions.

intersect in at most seven points, and this can only happen if they are related by an improper affine map, that is, one that reverses orientations (Fig. 19). This immediately implies that three copies of the wynn cannot be placed so that each pair has seven intersections: there are only two orientations! The best we can do, given n wynns, is to split them as evenly as possible into two groups, and arrange them so that two wynns in different groups intersect in seven points, while two wynns in the same group intersect in six points. This is possible, because the six intersections between two wynns with the same orientation can be achieved by a small rotation of the triangle, as in Figure 20.

The resulting configuration is optimal, since we have the largest number of pairs with seven intersection points, and all remaining pair have six intersection points. Thus, with

- m = ⌊n/2⌋ and m′ = n − m, we have


m′ 2

m 2

VC = 7mm′ + 6

+

. The number of regions is then given by R = VC + n + 1, and so

n2 4

aᚹ(n) = 3n2 − 2n + 1 +

(A393448) . (17)

This argument—finding optimal configurations for a small number of shapes and then doubling up the shapes—will be used again for the constrained long-legged T.

Figure 20: Wynns with the same orientation can intersect in six points.

### 11 The constrained long-legged Z, W and M

Starting in this section we consider several families of constrained long-legged knives for which the symmetry group is the smaller group Gsim of similarities of the plane: rigid motions and scalings. Now the notions of angle and parallelism become meaningful. If we were still working with the affine group, the shapes we are about to consider would simply be special cases of chains. The formula (6) for the number of regions is still valid, as it depends only on the graph formed by the figures. The role of the group is just to help in defining the class of figures to be considered.

For the long-legged Z knife mentioned in the Introduction (the zig-zag curve of [10]), the basic equation (6) gives (8) again. To maximize VC we substitute n long narrow copies of Z into the pancake graph, which results in a maximum of R = aZ(n) = (9n2 − 7n + 2)/2 regions (see A117625). This is exactly the construction used in [10] (although they do not use our counting argument to prove it is optimal).

A natural sequel is worth mentioning. After drawing the first three arms of the Z, we may truncate the third arm and add a fourth (infinite) arm that is parallel to the second arm, obtaining this long-legged W (or M) knife:

Our standard analysis (this time substituting into a hatpin graph) shows that the maximum number of regions is aW(n) = 8n2 −7n+1 (A125201). Figure 21 illustrates aW(2) = 19. The parallelism constraints still allow us to make this letter arbitrarily long and thin, so that the maximum in indeed achievable.

Figure 21: Two long-legged W’s divide the plane into 19 regions.

### 12 The constrained long-legged L, X, H, and ϕ

In this section we discuss another four shapes from the similarity genus, L, X, H, and ϕ, all of which we are able to solve.

##### 12.1 The constrained long-legged L

With no restriction on the angle, a long-legged L would be indistinguishable from a longlegged V. We define a constrained long-legged L to consist of a distinguished point, its center, from which two perpendicular rays emanate. We denote the family of all such knifes by L. The group Gsim acts transively and as holotype we may take the center (0,0) and the rays {y = 0,x ≥ 0} and {x = 0,y ≥ 0}. Two L’s can intersect in at most κ(L) = 3 points, so VC ≤ 3 n2 and then (6) gives

R ≤ 3

n 2

+ n + 1 = (3n2 − n + 2)/2 (A143689) . (18)

Figure 22: The construction of n constrained long-legged L’s, showing the case n = 5. There are 36 regions.

Equality in (18) can be achieved by modifying the standard construction for drawing

- n squares with the maximum number of regions (see A069894). This construction starts


by marking 4n equally-spaced points P0,...,P4n−1 around the full circumference of a circle. To get an optimal arrangement of n squares, we would take the squares with vertices {Pi,Pi+n,Pi+2n,Pi+3n} for i = 0,1,...,n − 1. To get an optimal arrangement of n L’s, we take the L’s formed by the top left corners of these squares. That is, we draw an L centered at Pi with arms Pi−Pi+n and Pi−Pi+3n, for i = 0,...,n−1 . Figure 22 shows the construction when n = 5. In general the graph contains 2n infinite regions, there are n rows of n−1 cells each, and a further triangle of (n−1)(n−2)/2 cells, for a total of R = aL(n) = (3n2−n+2)/2

regions. For n ≥ 0 the values are 1,2,6,13,36,52,71,... (A143689). The OEIS entry makes

- no mention of this geometric application, so this result may be new.


There are V = n + 3 n2 = n(3n − 1)/2 = R − 1 vertices, which is a pentagonal number (A000326—). The presence of pentagonal numbers can be explained as follows. The familiar picture of the pentagonal numbers ([10, p. 380], for example) shows a pentagonal array of dots divided into successive shells of 1,4,7,10,13,... dots. Careful examination of the grid of points formed by the above construction (as in Fig. 22) reveals exactly the same shells of points.

- 0 1 2 3 4 5 6 7 8 9

−3

−2

−1

- 1

- 2

- 3

- 4

- 5


Figure 23: Dividing the plane into the maximum number of pieces using n X’s (or coordinate frames). For n = 3, draw a grid of lines λt defined by (9) with θ = π/(4n) = π/12 and t = 0,...,3n − 1 = 8. The three X’s (centered at the red dots, and with blue axes) are λ0 ∪λ6, λ1 ∪λ7, and λ2 ∪λ8. An enlargement of the figure will show that, although it is not clear from this illustration, there is no point where any three of the lines intersect.

##### 12.2 The constrained long-legged X

A constrained long-legged X consists of a distinguished point, its center, from which two perpendicular lines (its arms, or axes) emanate. The group Gsim acts transitively on this family, and as holotype we may take the center (0,0) and the lines x = 0 and y = 0.

A graph ΓX(n) with n X’s is also a pancake graph ΓK(2n) with 2n lines, so (1) gives aX(n) ≤ aK(2n) = 2n2 + n + 1 (A084849) . (19)

Two X’s can intersect in at most κ(X) = 4 points, so VC ≤ 4 n2 , and then (6) also gives R ≤ 2n2 + n + 1.

We can indeed achieve equality in (19) by modifying the construction of pancake graphs given in §5. To construct a ΓX(n) containing n copies of X, set θ = π/(4n), and let λt denote the line (9). Draw the lines λt for t = 0,1,...,3n − 1 (now we need more of these lines than when we constructed the pancake graph). The t-th copy of X is formed from the lines λt

and λt+2n for t = 0,...,n − 1. Figure 23 illustrates the construction for n = 3. Of all our constructions, this one seems to be the most likely to have applications, since the X suggests the cross-hairs of an optical instrument.

Figure 24: An unconstrained long-legged H is the same as two V’s joined by a line segment, which can be rearranged to have four self-crossings, and then (invertibly) transformed into a 5-chain by “raising the bar” (the heavy line).

##### 12.3 The constrained long-legged H and ϕ

Our rules for long-legged letters tell us that an (unconstrained) long-legged H is the same as two long legged V’s with their tips joined by a line segment (see Fig. 24). Then σ(H) = 4, κ(H) = 25, and with n H’s, (5) tells us that aH(n) ≤ (25n2 − 11n + 2)/2. This upper bound matches the counts for a 5-chain, (16) (A383465), and equality is easily achieved since the invertible transformation shown in Fig. 24 maps an optimal graph with n H’s into one with n 5-chains.

- Figure 25: One of the three inequivalent ways in which two constrained H’s can interesct in seven points.


- Figure 26: Construction of n H’s with each pair intersecting in 7 points (here n = 3).


We define a constrained long-legged H to consist of a pair of parallel lines joined by a perpendicular line segment (the crossbar). The group Gsim acts transitively on the family of all such knives. Two H’s can meet in a maximum of κ(H) = 7 points. This can be done in three inequivalent ways, but we will only make use of one of them, the arrangement shown in Fig. 25.

It is straightforward to arrange n H’s so that each pair intersect in seven points in this way, by first drawing the n crossbars so that each one crosses the others at a small angle, similar to the arrangement of lines in Fig. 4. By making these crossbars have slowly increasing and incommensurable lengths, we ensure that when we add the parallel lines to the crossbars, there are no triple intersections in the resulting graph. Figure 26 illustrates the construction when n = 3.

From (5), the maximum number of regions with n H’s is then

7n2 − n + 2 2

aH(n) =

(A140063) . (20)

with initial values 1,4,14,31,55,.... We were surprised to find that this sequence was already in the OEIS, in a 2008 entry. This entry formerly contained a link to a webpage [16] of David Kinsella, where it was stated that this sequence gives the maximum number of regions that the plane can be divided into by drawing n circles and n lines. This webpage now seems to be lost, but the Internet Archive’s Wayback Machine has preserved enough of this document (see [16]: the figures are missing) to make it clear that this was an empirical observation based on examination of the constructions for n ≤ 4 pairs of circles and lines.

A stronger version of this claim can be obtained from our analysis of the H shape. Define a constrained ϕ to consist of a circle with a line through its center. Two such ϕ’s can intersect

| | | |
|---|---|---|
| | | |


Figure 27: An invertible map from H’s to ϕ’s.

in a maximum of seven points. An optimal graph containing n ϕ’s, each intersecting all of the others in seven points, can be obtained from an optimal graph with n H’s by applying the invertible transformation shown in Fig. 27. This map does not preserve the number of intersections between the figures in general, but an elementary check shows that it does map two shapes with seven intersections to two shapes with seven intersections. It follows that (20) applies also to ϕ’s. Thus, not only is Kinsella’s claim true, but it is possible to achieve the maximum number of regions under the additional constraint that each line must pass through the center of a circle.

##### 12.4 Steiner’s theorem: m circles and n lines

Unsurprisingly, the combination of n circles and n lines had already been discussed in the literature. In fact, Steiner [28] had already shown that the maximum number of regions that the plane can be divided into by making m independent cuts with circular knives from the family O and at the same time making n independent cuts with straight knives from K is given by

aSt(m,n) =

m2 − m + 2mn + (n2 + n + 2)/2, if n > 0 or m = n = 0; m2 + m + 2, if n = 0 and m > 0 .

The diagonal terms aSt(n,n) agree with (20). The OEIS entry A393442 contains the array aSt(m,n) itself (analogous to Tables 2 and 3), the first three columns of which are essentially A014206, and the first two rows are A000124 and A034856.

We remark that this family of knives does not fit into our usual classification into genera, since now we are choosing a single knife from the very large family St(m,n) rather then making n independent choices from a smaller family.

It is worth remarking that Steiner’s article [28] appeared exactly 200 years ago in the first volume of what became one of the most famous of all mathematical journals, the Journal fu¨r die reine und angewandte Mathematik, often simply called Crelle’s Journal. Steiner’s proof of his formula essentially uses a case-by-case analysis, considering all possible ways in which m circles can be divided into families of parallel circles and all possible ways in which n lines can be divided into families of parallel lines. The article occupies 15 pages of Crelle’s Journal, and we will not present the proof here. Steiner’s proof is also discussed by Wetzel [30].

The many citations of Steiner’s paper in the literature contain a great deal of information about dissections by lines and circles and refinements (going beyond simply maximizing the number of pieces, for example), generalizations (e.g., to higher dimensions), and applications. At present, Google Scholar lists over 130 citations. See for example [1], [2], [8], [22], [24], [26], [30].

### 13 The constrained long-legged T and A

Up to this point in our investigations we were able to analyze the shapes by hand, using pencil and paper and traditional drawing instruments. But the next two families in the similarity genus, T and A, appear to be more difficult and we invoked the aid of the computer. In the case of T, we find an exact formula, which, however, is no longer a polynomial in n but a quasipolynomial. The case of A is harder and here we are only able to determine the numbers up to n = 3. Beyond that point, we only have lower and upper bounds.

Figure 28: Three constrained long-legged T’s can divide the plane into 19 regions. It is impossible to add a fourth T that meets each of the first three in 4 points.

##### 13.1 The constrained long-legged T

A constrained long-legged T consists of a distinguished point, its center, which is at the intersection of a line—sometimes referred to as the crossbar—and a perpendicular ray, the stem.. The group Gsim acts transitively on this family, and as holotype we may take the center (0,0) and the lines y = 0 and {x = 0,y ≤ 0}.

Two such T’s can intersect in at most four points, our standard analysis gives R ≤ VC + 2n + 1 ≤ 4 n2 + 2n + 1, and so

aT(n) ≤ 2n2 + 1 . (21)

Figure 28 illustrates aT(3) = 19. However, the configuration of three T’s shown in that figure is essentially unique, and one can check (by hand, or by using Lemma 1 below) that there is no way to add a fourth T that meets each of the first three in four points. So equality does not hold in (21) for n ≥ 4. For n = 4 the best we can achieve is 32 regions (Fig. 29).

Figure 29: Four constrained long-legged T’s can divide the plane into 32 regions. The first three are the same as in Fig. 28, and the fourth (which meets one of the first three in only three points, not four) is drawn in red.

To treat the general case, we need to consider the directions of the stems. For two T’s to intersect in four points, their stems must not be too close to parallel. To see this, suppose the first T is placed in some standard position—we take it to be y = 0 and {x = 0,y ≤ 0}

- so that the stem is the negative y-axis. We claim that if another T achieves the maximum number of intersections with this reference T, then its center node must lie in the lower half-plane {y < 0}. Indeed, if the center node of the second T is (x,y) with y > 0 and if the direction of its stem is (cosθ,sinθ), then we must have sinθ < 0, or else the stem could not enter the lower half-plane.


#### (x,y) θ

Figure 30: Parameters for a constrained long-legged T: coordinates (x,y) of the center, and the angle θ between the stem and the x-axis.

More precisely, if the center node lies in the first quadrant, both cosθ and sinθ must be negative. Assuming this and computing the point of intersection between the crossbar of the second T and the y-axis, we find that this intersection point has y > 0, so that the crossbar does not intersect the stem of the reference T. Similarly, assuming the second center node

to lie in the second quadrant again forces the second crossbar to miss the first stem (if the center node lies on the positive y-axis and the stems intersect we would have a degenerate configuration, which we rule out). It follows that the second center node must lie in the lower half-plane, and then for the second stem to intersect the first crossbar (which is the x-axis) its direction (cosθ,sinθ) must satisfy sinθ > 0. Remembering that our reference T has θ = −π/2, we have shown:

- Lemma 1. If two T’s intersect in four points, and if their stems have the directions (cosθ1,sinθ1) and (cosθ2,sinθ2) respectively, then cos(θ1−θ2) < 0. In other words, the angle between their bearings must be strictly greater than π/2.


Figure 31: A good pair: two T’s that intersect in four points. The angle between the stems must be strictly greater that π/2.

This fact will determine how many pairs of T’s can achieve four intersections. Let us say that two T’s form a good pair if they intersect in four points (Fig. 31). We will denote the maximum number of good pairs among n T’s by gp(n). We already know that with n = 3 we can have three good pairs, but that with n = 4, only five out of the six pairs can be good. Thus gp(3) = 3 and gp(4) = 5.

To find a formula for gp(n), let us imagine that we choose n points on the unit circle and form the graph Ω whose vertices are those points and whose edges are the good pairs (points strictly more than π/2 apart). Then gp(4) = 5 implies that Ω contains no K4, that is, it contains no complete subgraph on four vertices.

A classic theorem of Tur´an [4, p. 108] then implies that Ω can have no more edges than the Tura´n graph T(3,n), the graph formed by letting the n vertices be the set of integers {0,1...n − 1} and joining two vertices by an edge if and only if they are not congruent modulo 3. We can in fact achieve this bound simply by taking the kth angle θk to be 2πk/3. Thus gp(n) equals the number of edges in the Tura´n graph, that is

gp(3m) = 3m2,

- gp(3m + 1) = 3m2 + 2m,
- gp(3m + 2) = 3m2 + 4m + 1.


It remains to check that we can turn this into a non-degenerate configuration, but this is easy: place the kth T with its center vertex at (cos2πk/3,sin2πk/3) and with its stem through the origin. Displace each group of T’s slightly so as to break up the triple intersection at the origin. Then spread the centers in each group so that each pair has one stem-crossbar intersection, as indicated in Figure 32. Finally, rotate the T’s by small generic angles to create the missing stem-stem and crossbar-crossbar intersections.

Figure 32: A step in breaking up the groups of overlaid T’s.

In the resulting configuration, two T’s in different groups have 4 intersection points, while two T’s in the same group have 3 intersection points, for a total of

VC = 4gp(n) + 3

n 2 − gp(n)

intersections. Optimality is clear, since we have the maximum number of good pairs (contributing 4 each), and all remaining pairs contribute as much as they can, namely 3. Reexpressing the function gp using the floor function and simplifying the formula, we have shown that

aT(n) =

n2 3

3 2

n2 +

+

- 1

- 2


n + 1 =

11n2 + 3n + 6 6

(A389614) . (22)

##### 13.2 The constrained long-legged A

The unconstrained long-legged A was discussed in §9, where we showed that it is equivalent to a three-armed V. A constrained long-legged A is defined to be a long-legged A in which the ends of the crossbar are equidistant from the tip. As in the previous section, the group Gsim acts transitively on this family.

For both the unconstrained A and the constrained A, the degrees of the base nodes are not all equal. For both shapes, there are three base nodes: the tip, which has degree 2, and the two crossbar nodes, which have degree 3.

![image 3](<2025-cutler-cutting-pancake-exotic-knife_images/imageFile3.png>)

Figure 33: Two constrained A’s can intersect in 8 points, and divide the plane into aA(2) = 13 regions. (In this picture one A has a purple tip, the other a brown tip. One of the intersection points is not shown: it occurs a long way below the bottom of the picture. The arrowheads are also not shown.)

Figure 34: Three constrained A’s can divide the plane into 30 regions.

Two constrained A’s can intersect in a maximum of κ(A) = 8 points, and divide the plane

into aA(2) = 13 regions. To see this, observe that a line can cut an A in at most three points, so κ(A) ≤ 9. But if the two legs of a second A cut the first A in three points, it is impossible for the crossbar of the second A to cut the first A in three points.

Even the construction that achieves κ(A) = 8 was not easy to find (it was discovered by

Figure 35: Enlargement of the portion of Fig. 34 where the three crossbars come together.

our program), so we provide a colored illustration in Fig. 33. This family A was by far the most difficult that we studied.

From (6) we obtain

aA(n) ≤ 4n2 − 2n + 1 (A054554) . (23) However, it appears that equality does not hold in (23) for n > 2. We modified the program used in the previous section to apply to this problem. For 0 ≤ n ≤ 5 the maximum number of regions we found were

1,3,13,30,53,83 . (24)

In particular, for three A’s, only 23 crossings are possible, not 24, giving 30 regions rather than 31. We do not give full details of the proof of this claim, as they are elementary and not very enlightening, but in outline the argument goes as follows: suppose two A’s intersect in eight points. By enumerating all possible geometries of such a configuration, we can reduce them to two essentially different arrangements. An analysis of the geometry of these two cases gives bounds on the tip angles of the A’s, and also on the angle between their symmetry axes. One then checks that these constraints are incompatible if we seek a configuration of three A’s every pair of which intersect in eight points. Thus 24 intersection points are impossible, and from examples we know that 23 are possible.

At this point, we introduce two general methods, one for obtaining lower bounds, the other for obtaining upper bounds.

The lower bounds are obtained as follows. Suppose we have a configuration of n copies of a shape S, labeled 1 through n, and that we assign integer multiplicities m1,...mn to those figures. We think of such a figure-with-multiplicity as a cluster of mi superimposed copies of figure number i, and the whole collection of clusters as a configuration of N = m1 + ...mn figures. This is not yet a valid configuration, because of the superpositions, but then we perturb the members of each cluster so as to remove the superpositions.

In all the cases we are interested in, it is possible to spread the figures in each cluster so that each pair has ξ(S) intersection points, where ξ(S) is a local intersection number defined as follows. Recall that in §5 we defined the intersection number κ(S) to be the maximum

number of intersections between two copies of a figure S. In those cases where the set of figures is generated from a holotype by the action of a group, κ(S) is the maximum number of intersections between S and g(S) as g ranges over the whole group; and we now define ξ(S) to be the corresponding maximum intersection number when g is restricted to an arbitrarily small neighborhood of the identity element.

Clearly ξ(S) ≤ κ(S), and in general the inequality is strict. For example, the operation illustrated in Figure 32 shows that while κ(T) = 4, we have ξ(T) = 3. Similarly κ(A) = 8 but ξ(A) = 6.

To compute the total number of intersection points thus achieved, we first write down a table of the actual intersection counts between the figures S1,...Sn, before we assign any multiplicities. So as not to double-count, we only consider pairs (Si,Sj) with i < j. For example, the configuration with three A’s in Figure 34 produces Table 4. Assigning the

| |1 2 3<br><br>|
|---|---|
|1<br>2<br>3<br>|∗ 8 7 ∗ 8 ∗<br><br>|


Table 4: Intersections counts between the 3 A’s in Figure 34

figures the multiplicities (m1,m2,m3) and perturbing as described above, the total number of intersection points becomes

I(m1,m2,m3) = 8m1m2 + 8m2m3 + 7m1m3 + 6

m1 2

+

m2 2

+

m3 2

.

By fixing N = m1 + m2 + m3 and maximizing the quantity I(m1,m2,m3), we obtain lower bounds on the optimal intersection numbers, as follows:

- I(1,2,1) = 45, so aA(4) ≥ 54,

and

- I(1,2,2) = 74, so aA(5) ≥ 85,


and so on.

In general, then, we start with a graph formed from the intersection of S1,...Sn, having multiplicities mi, whose pairwise intersection counts are the coefficients of the terms mimj, and the quantity ξ determines how many additional intersections we get from each cluster. By fixing N = m1+m2+···+mn and maximizing the corresponding quantity I(m1,m2,...,mn), we obtain lower bounds on the optimal intersection numbers.

Turning now to upper bounds, we make the following (trivial) observation: if we have a configuration and form its intersection table; and if we then choose a subset of the indices and delete the corresponding rows and columns, what remains is a possible intersection table. In other words, a principal submatrix of a possible intersection table is again a possible intersection table. This is obvious since the operation of dropping rows and corresponding columns is just the operation of omitting some of the figures in a configuration.

As soon as we have an upper bound on the number of intersections for some n, this can be leveraged to obtain bounds for all larger values of n. We illustrate this idea by an example. Suppose we find a configuration of four A’s and write down its intersection table, as in Table 5. Then, because dropping the first row and column gives a valid intersection

| |1 2 3 4<br><br>|
|---|---|
|1<br><br>2<br><br>3<br><br>4<br><br><br>|∗ a1,2 a1,3 a1,4 ∗ a2,3 a2,4 ∗ a3,4<br><br>∗|


Table 5: Hypothetical intersection table for four A’s.

table for three A’s, we have

a2,3 + a2,4 + a3,4 ≤ 23, and for the same reason we have

a1,3 + a1,4 + a3,4 ≤ 23, a1,2 + a1,4 + a2,4 ≤ 23, a1,2 + a1,3 + a2,3 ≤ 23.

Adding up these inequalities, we have

ai,j ≤ 4 · 23. (25)

2

i<j

To formalize this, fix a shape S, and let M(n) denote the largest possible number of intersection points between n copies of S, that is, the largest possible sum of all entries in all possible intersection tables of size n (we may assume that the below-diagonal elements are zero). Thus, since Table 4 is optimal, we have M(3) = 23 for the figure A, and our argument shows that this implies M(4) ≤ 46.

In general, we can imagine starting with a table of size n and deleting one row and column pair in all possible ways, obtaining n possible tables of size n − 1. Next, we add the entries in each table, and add up all these sums. The result will be a multiple of the sum of the original table of size n, specifically n − 2. This is so because any entry in the table, say (1,2), will be present precisely in those tables where the (n − 1)-subset of remaining indices contains 1 and 2 (the diagonal elements are zero so the indices may be assumed to be distinct). On the other hand, each of the n tables of size n−1 sums to at most M(n−1). Since the original table was arbitrary (apart from being possible), we have

(n − 2)M(n) ≤ nM(n − 1) as in (25), and we conclude that

M(n) ≤

n n − 2

M(n − 1) . (26)

(It would be possible to delete any number of columns, but deleting a single column seems to give the best bound.)

For example, knowing that M(3) = 23 for A, we get M(4) ≤ 46, whence M(5) ≤ 76 after taking the integer part, and so on. The upper and lower bounds are summarized in Table 6.

|n<br><br>|lower upper|
|---|---|
|1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6<br><br>7<br><br><br>|3 3 13 13 30 30 54 55 85 87<br><br>123 127 169 174|


Table 6: Bounds on aA(n).

It is also easy to extract bounds on the leading term of M(n) as a function of n. For a lower bound, we maximize the function I(m1,m2,m3) over the real numbers, getting a leading term of 25n2/7. Rounding to an integer only incurs a linear correction. For an upper bound, we may simply leave out the floor function from some point on — k, say. Then the bound on M(n) is

n(n − 1) k(k − 1)

M(n) ≤

M(k)

for any fixed k. For example, using M(7) ≤ 159 shows that the coefficient of the leading term is at most 53/14 = 3.785.... It is easy to improve this slightly by going past points where the floor would have made a difference. Moreover, the difference between the number of crossings and the number of regions is linear in n. Altogether, then, we find that aA(n) asymptotically satisfies

25 7

53 14

n2 ≤ aA(n) <

n2.

It is conceivable that the lower bound is tight but to prove this seems to require a closer analysis of the possible intersection tables.

### 14 Finite shapes 1: Polygons

##### 14.1 Convex polygons

The family of k-sided convex polygonal knives, for k ≥ 3, abbreviated kP, is the last of our families in the affine genus. Since VB = k and vB = 2, (10) tells us that R = VC + 2. Observe that any line segment can intersect a convex polygon in at most two points. In particular, each side in one of the polygons can intersect at most two sides of the other polygon. Therefore, two such polygons can intersect in at most 2k points, so VC ≤ 2k n2 . This is easily achieved, so

akP(n) = kn2 − kn + 2 (n ≥ 1), with akP(0) = 1 . (27)

The solutions for k = 3, 4, and 5 (for the triangle, square or convex quadrilateral, and pentagon) are given in sequences A077588, A069894, and A386485. It was a slight surprise to discover that taking k = 1 and k = 2 in (27) matched A386480 and A051890, which are the numbers of regions attainable with n circles (see §15.1) and n ellipses, respectively. More surprising, however, was the case k = 8, which we discuss in the next subsection.

Figure 36: Two regular octagons divide the plane into 18 regions.

##### 14.2 The octagon and concave quadrilateral

For a convex octagon, the values of a8P(n) are 1, 2, 18, 50, 98, 162, 242,.... that is, 2(2n − 1)2 for n > 0. Figure 36 illustrates a8P(2) = 18. Remarkably, this sequence also matches A077591, whose definition is the maximum number of regions obtainable in the plane by drawing n concave quadrilaterals. The latter is illustrated in Figure 37 for n = 2 (and which also has 18 regions). Since there is no obvious connection between the two dissections, the result may be just a coincidence.

Figure 37: Two concave quadrilaterals also divide the plane into 18 regions. Is it just a concidence tht the maximum number of pieces that can be obtained with n (convex) octagonal cuts is the same as what can be obtained with n concave quadrilateral cuts? We do not know!

##### 14.3 The pentagram and hexagram

A regular pentagram or hexagram is based on 5 or 6 equally spaced points around a circle. To attain the maximum number of regions we will use regular figures, but our analysis

- Figure 38: No line can intersect a pentagram in more than four points.

- Figure 39: Three pentagrams can divide the plane into 77 regions.


applies equally to non-regular figures. A single pentagram (regular or non-regular) has 5 base nodes, the exterior vertices, with degree dB = 2, and 5 self-intersections, in the interior. To compute κ for the pentagram, we can reason as follows: suppose we place a pentagram in the plane, and draw any line not incident with any of its vertices, as illustrated in Figure 38. It is clear that the line will intersect a side of the pentagram if and only if the vertices joined by that side lie on opposite sides of the line. It follows from this that no line can intersect the pentagram in more than four points, and a fortiori that no line segment can intersect it in more than four points. Thus the five sides of one pentagram can intersect another pentagram in no more than 20 points, so κ ≤ 20. But this is also achievable by taking two pentagrams with their vertices on the same circle and placed so that their vertices interlace as we go around the circle.

Since κ = 20, with n pentagrams we have VC ≤ 5n + 20 n2 , and our basic equation (10)

then gives R ≤ VC + 2 ≤ 5n + 20 n2 + 2 = 10n2 − 5n + 2 (A383466), a bound which is easily achieved using regular pentagons based on 5n equally spaced points around a circle. The

construction is illustrated for n = 3 in Fig. 39. To verify the number of regions, note that each of the base nodes is a vertex of a triangular region (indicated by the three blue dots in Fig. 39), containing 2n − 1 cells. We were led to investigate pentagrams because an optimal 5-chain (§8) necessarily contains a pentagram (see Figs. 7 and 10).

A hexagram initially contains two disjoint triangles and is not a connected graph, which would violate the assumption that our shapes are connected, but it is connected if we take the self-intersections into account. The analysis is similar to that of the pentagram, so we just state the result: the maximum number of regions that can be attained in the plane by drawing n hexagrams is 2(6n2 − 3n + 1) (A386477).

### 15 Finite shapes 2: Three curved shapes

Although our basic equation (10) would not apply to curved shapes with arbitrarily many twists, it does apply to the three shapes considered in this section. These families all belong to the transitive similarity subgenus.

0

C1 P

## Q C2

Figure 40: Four circles can divide the plane into 14 regions. There are four base nodes (red) and twelve crossing nodes (black). The two outer circles have centers C1 = (−1,0) and C2 = (1,0), and the two inner circles have centers P = (−1/3,0) and Q = (1/3,0). All the circles have radius 3/2. The x-axis is for reference only, it is not part of the graph.

##### 15.1 The circle

It is a classical result that the maximum number of regions that can be obtained with n circular cuts is

aO(n) = n2 − n + 2. (28)

This is already mentioned in Steiner’s 1826 paper [28], and other references can be found in A014206. We discuss the circle here because it is an interesting application of our method, and also because a similar argument will be used in the next section.

In order to apply our method, we formally define the circle shape to consist of a distinguished point, the base, and a circle of arbitrary positive radius through that point. Note that without the base point, Euler’s formula itself (3) fails for a single circle, since there is a single edge, no vertices, and two regions, and E − V + 2 = 3, not 2. But, after adding a base node, we have E − V + 2 = 1 − 1 + 2 = 2, as it should be.

It is clear that two circles can intersect in at most two points, so with n circles, maintaining our standard convention that no other circle can pass through a base node, we have VB = n, VC ≤ 2 n2 , and (10) implies that R ≤ 2 n2 + 2.

If we can guarantee that every pair of circles meet in two points, then equality holds in the latter expression, and establishes (28). This is easily accomplished. For n ≥ 2 we draw two circles of radius 3/2 centered respectively at C1 = (−1,0) and C2 = (1,0), and then draw n−2 further circles of the same radius centered at points equally spaced along the line C1 − C2. Figure 40 illustrates the construction for n = 4. The base nodes (shown in red), whose only function is to ensure that each circle contains at least one vertex, can be placed anywhere on the circles, except at the intersection points. In Fig. 40 we have lined them up in a row.

Figure 41: Two figure 8’s can divide the plane into 12 regions

##### 15.2 The figure 8

A figure 8 shape consists of two tangential circles of equal but arbitrary radius. A graph with n 8’s contains 2n circles, and so aO(2n) from the previous section is an upper bound on a8(n). However, we cannot achieve all the intersections needed to achieve that bound, since the two constituent circles of each 8 cannot properly intersect. The effect of this constraint is simply to reduce the number of crossings by 2 for each figure 8, and so the solution for the 8 satisfies a8(n) ≤ 4n2 − 3n + 2.

We can achieve equality in that expression using figure 8’s of equal size, by a construction similar to that of the previous section. We start from a figure 8 in a standard position, say the two circles (x ± 1)2 + y2 = 1, with centers C1 = (−1,0), C2 = (1,0). Imagine adding another copy of this figure, slightly displaced. Then, for the right circle to intersect the original left circle in two points, its center must have x < 1, and be situated to the left of C2. By symmetry, the new left circle must have its center to the right of C1. At the same time, the distance between the centers must be constant. This suggests rotating the whole figure about a point on the line C1 − C2. We cannot use the origin as the center of rotation, for then the point of tangency between the circles would become a multiple point. On the other hand, any other interior point on C1 − C2 will do, and any small rotation about that point will create eight intersection points. By placing n − 1 equally-spaced figure 8’s along C1 − C2, we obtain a total of n figure 8’s, each pair of which intersect in eight points. We

Figure 42: Eight intersections between two figure 8’s can be achieved by an arbitrarily small rotation.

conclude that5

a8(n) = 4n2 − 3n + 2 (A386486) . (29)

Figure 43: Two lollipops can intersect in at most 7 points and can divide the plane into 10 regions. The stems of the lollipops are colored red.

##### 15.3 The lollipop or qoppa

Although it does not quite meet our conditions, since it is both curved and infinite, we cannot resist ending with the lollipop shape ( ϙ ). This is essentially the same as the archaic Greek letter qoppa (Unicode symbols U+03D8, U+03D9). Formally, a lollipop or qoppa is

5This result was independently discovered by the referee of the first version of this article.

Figure 44: With each pair intersecting in 7 points, three lollipops can divide the plane into 25 regions.

a circle together with a ray (the stem) emanating from its center but with the portion of the ray inside the circle omitted. Again Gsim acts transitively on this family. Besides its intrinsic appeal, the lollipop is also a possible candidate for a long-legged version of both the letters P and Q. (The Latin letter Q is in fact a descendant of the qoppa.)

Two lollipops can meet in a maximum of κ = 7 points (Fig. 43). Equation (6) applies to this shape, and implies that the maximum number of regions possible with n lollipops is

7n2 − 5n + 2 2

R ≤

(A389608) . (30)

This can be achieved for n ≤ 3 (Fig. 44). For n = 4, however, we will show that the maximum number of intersection points is 40, and the maximum number of regions is 45. This can be achieved by taking an optimal configuration of three very large lollipops and inserting a fourth in the small central cavity. Figure 45 shows an enlargement of the central portion of the configuration. In this close-up, the three original lollipops appear as T shapes.

It turns out that the same kind of analysis that we applied to the T applies here, although we are not able to solve it completely. Recall that we define a good pair to be a pair of T’s in which the stem of each intersects the other in two points, and that this restricts the relative position of the two figures. For lollipops, we say that two of them form a good pair if they achieve three or four stem-circle intersections, as in Figure 46.

As in § 13.1, by choosing coordinates for one of the lollipops and writing down equations for the stem of the other, we can establish an analog of Lemma 1:

- Figure 45: Enlargement of the central portion of a configuration of four lollipops with 40 intersections. Three of the lollipops are so large they appear as T shapes.

- Figure 46: Good pairs of lollipops, with three or four stem-circle intersections. As in Fig. 31, the angle between the stems must be strictly greater that π/2.


- Lemma 2. If two lollipops form a good pair, that is, if together they have three or four stem-circle intersections, then the angle between the directions of their stems must be strictly greater than π/2.


Moreover, one can show that in the case of three stem-circle intersections, it is not possible for the two stems to intersect, while four stem-circle intersections are compatible with both one stem-stem and two circle-circle intersections. We have not included this fact as part of the lemma as it will not be used below, but it could be relevant for future investigations.

Using this lemma, we can show that our configuration of four lollipops with 40 intersection points is optimal. Indeed, all pairs of circles contribute two intersections, and all pairs of stems contribute one intersection. The stem-circle intersections are given in Table 7.

The only number in the table that could be improved is the zero, which indicates that circle 1 and stem 2 do not intersect. But if that entry were equal to 1 or 2, we would have

| |S1 S2 S3 S4<br><br>|
|---|---|
|C1 C2 C3 C4|∗ 0 2 2 2 ∗ 2 2 2 2 ∗ 2 2 2 2 ∗<br><br>|


Table 7: Intersections between circles and stems in our 40-intersection configuration of four lollipops.

six good pairs, and we know that five is optimal for four directions. Thus this configuration is optimal, as claimed.

Just as with the letter T, we can leverage this result to obtain both lower and upper bounds for general n. For the lower bound, we assign multiplicities to the four lollipops in our best configuration and calculate the number of intersection points after the configuration has been made generic by a small perturbation. This is where the lollipop proves more difficult than the T: while the maximum number of intersections between two lollipops is κ = 7, the local maximum (achievable by arbitrarily small motions) is only ξ = 4. Because of this large decrease, we are unable to show that the resulting configurations are optimal. At present they certainly are the best that we know—see Table 8.

|n|lower upper<br><br>|
|---|---|
|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>|2 2 10 10 25 25 45 45 71 72<br><br>104 106 142 146 186 193<br><br>|


Table 8: Bounds on aϙ(n).

A389624 gives further details about our construction, including a drawing of and coordinates for a 40-crossing, 45-region optimal arrangement of four lollipops.

### 16 Open problems

- 1. Find optimal graphs for the two shapes that we left unfinished: the constrained longlegged letter A (§13.2), and the lollipop (§15.3).

- 2. Enumerative Geometry. We have already mentioned (in §8) the sequence A090338, which gives the number of ways to draw n lines in general position in the Euclidean plane, and which is also the number of ways to cut the plane into the maximum number


- of pieces with n straight cuts. The values are known for n ≤ 9. If we omit “in general position”, and just ask for the number of ways to draw n lines in the plane, there are more possibilities, and the values (A241600) are known only for n ≤ 7. For n = 3, for example, there are four possibilities: three parallel lines, two parallel lines and a line cutting both, three lines through a point, and three lines in general position. There are still more ways if we restrict the question to a disk (a pizza, say). For 0 ≤ n ≤ 6 it appears that the values are 1,1,2,5,19,130,1814 (A272906), although the last term is unconfirmed. There has been no progress on either of the last two questions for ten years.
- 3. More generally, for any shape S for which we have determined the maximum number

of regions aS(n) (which includes all the entries in Tables 2 and 3), we may ask for the number of distinct graphs having that many regions. The case when S is a circle has been studied by J. Wild in A250001 and A288554. Wild shows that the numbers of distinct planar graphs composed of n overlapping circles that divide the plane into n2−n+2 regions are respectively 1,1,4,45,5102 for n = 1,...,5. The four possibilities for n = 3 are shown in Fig. 47. One of the 45 is shown in Fig. 40. Arrangements of circles in the plane are classified from a different point of view in Mathar [19].

Figure 47: Three circles can divide the plane into a maximum of 8 regions, and this can be done in 4 ways. (Only the first is a Venn diagram.)

- 4. Is there a geometric explanation for the apparent coincidence mentioned in §14.2?
- 5. Geometrical Configurations. In the classical theory of Geometrical Configurations [14],


[15, Chap. III, Projective Configurations], [18], a configuration with symbol (pλ,ℓπ) is an arrangement of p points and ℓ lines in the plane such that each point is incident with λ lines, and each line is incident with π points.

Our graphs ΓS(n) satisfy this condition provided the number of crossings per arm (cpa) is constant, as it is in most cases considered here, and if so then ΓS(n) is a geometrical configuration with p = VC, λ = 2, ℓ = number of arms α(S), and π = cpa.

For example, the optimal constrained long-legged T graphs discussed in §13.1, which we showed do not exist for n > 3, would have formed configurations with p = 4 n2 , λ = 2, ℓ = 2n, and π = 2(n − 1) for integers n ≥ 1. Could the classical theory have resolved that question? Does the theory have any other application to our problems? Gru¨nbaum’s book [14], although it is mostly concerned with configurations of type (pλ,pλ), contains a large number of striking illustrations similar to those in the present article.

- 6. The Inverse Problem. Can one characterize the integer sequences that arise as {aS(n) : n ≥ 0} for some shape S? They are obviously monotonically increasing, and (11) gives a bound on the growth rate.
- 7. Computational Complexity. All our shapes have been semi-algebraic curves. This means that for any shape S and for any integers n and k, the statement “it is possible to place n copies of shape S so as to create k intersections” is decidable [3]. Of course, general-purpose algorithms for quantifier elimination have doubly exponential complexity, so a frontal attack is futile. However, it is conceivable that certain classes of shapes lead to more tractable problems. After all, the shapes we are interested in lead to polynomial growth in n, while more general classes can give rise to exponentially many regions.


### 17 Acknowledgments

N.J.A.S. mentioned the subject of this article in a Research Experience for Undergraduates seminar at Rutgers University on June 24 2025. Following the talk, three participants in the seminar, Edward Xiong, Jonathan Pei, and David O. H. Cutler, solved the 3-armed V problem (see §7). Their solution led us to the edge-vertex formula of (5), which underlies all our calculations. We thank Susanna S. Cuyler, Sean A. Irvine, Gareth McCaughan, Hilarie Orman & Rich Schroeppel, Scott R. Shannon, and Jonathan Wild for comments on the manuscript. We also thank Scott R. Shannon for his dramatic illustrations of the pentagram and hexagram graphs (see A383466 and A386477).

We are very grateful to the referee of the first version of this paper for many helpful comments and suggestions.

### References

- [1] G. L. Alexanderson and J. E. Wetzel, Arrangements of planes in space, Discrete Math. 34:3 (1981), 219–240.
- [2] J.-L. Baril and C. Moreira Dos Santos, The pizza-cutter’s problem and hamiltonian paths, Math. Mag., 92:5 (2019), 359–367.
- [3] S. Basu and B. Mishra, Computational and quantitative real algebraic geometry, in Handbook of Discrete and Computational Geometry, eds. J. E. Goodman, J. O’Rourke and C. D. To´th, Chapman and Hall/CRC Press, pp. 969–1002, 2018.
- [4] B. Bolloba´s, Modern Graph Theory, Springer, 1998.
- [5] L. Comtet, Advanced Combinatorics, Reidel, 1974.
- [6] H. S. M. Coxeter, P. du Val, H. T. Flather, and J. F. Petrie, The Fifty-Nine Icosahedra, University of Toronto Studies (Math. Series, No. 6), Toronto, 1938. Reprinted, Springer, 1982.


- [7] P. R. Cromwell, Polyhedra, Cambridge, 1997.
- [8] H. Edelsbrunner, J. O’Rourke, and R. Seidel Constructing arrangements of lines and hyperplanes with applications, SIAM J. Computing, 15:2 (1986), 341–363.
- [9] M. Gardner, New Mathematical Diversions from Scientific American, Simon and Schuster, 1966.
- [10] R. L. Graham, D. E. Knuth, and O. Patashnik, Concrete Mathematics, Addison-Wesley, 2nd ed., 1994.
- [11] B. Gru¨nbaum, Convex Polytopes, John Wiley & Sons, 1967.
- [12] B. Gru¨nbaum, Arrangements and Spreads, CBMS Regional Conference Series in Mathematics, No. 10, Amer. Math. Soc., 1972.
- [13] B. Gru¨nbaum, Venn diagrams and independent families of sets, Math. Mag., 48 (1975), 12–23.
- [14] B. Gru¨nbaum, Configurations of Points and Lines, Graduate Studies in Math. 103, Amer. Math. Soc., 2009.
- [15] D. Hilbert and S. Cohn-Vossen, Geometry and the Imagination, Chelsea, NY, 1952; 2nd ed., Springer, 1996.
- [16] D. Kinsella, Plane division by Lines AND Circles (Problem, Analysis and Solution), A Maths Puzzle Page, no date, but modified in 2009. This document is now apparently lost, although an incomplete copy was preserved by the Internet Archive’s Wayback Machine and can be seen here: https://web.archive.org/web/20210414225350 /http://www.90thkilmacudscouts.com/maths/circles lines soln.html.

- [17] I. Lakatos, Proofs and Refutations: The Logic of Mathematical Discovery, Cambridge, 1976.
- [18] F. Levi, Geometrische Konfigurationen, Hirzel, 1929.
- [19] R. J. Mathar, Topologically distinct sets of non-intersecting circles in the plane, arXiv:1603.00077 [math.CO], 2016 (https://arxiv.org/abs/1603.00077).
- [20] J. Matousˇek, Lectures on Discrete Geometry, Springer, 2002.
- [21] T. S. Michael, How to Guard an Art Gallery and Other Discrete Mathematical Adventures, Johns Hopkins University Press, 2009.
- [22] R. E. Miles, A generalization of a formula of Steiner, Zeit. f¨ur Wahrscheinlichkeitstheorie und Verwandte Gebiete 61:3 (1982), 375–378.
- [23] OEIS Foundation Inc. (2025), The On-Line Encyclopedia of Integer Sequences, https://oeis.org.


- [24] J. Pach and P. K. Agarwal, Combinatorial Geometry, John Wiley & Sons, 1995.
- [25] G. Po´lya, Induction and Analogy in Mathematics, Princeton University Press, 1954.
- [26] G. Ringel, Teilungen der Ebene durch Geraden oder topologische Geraden, em Math. Zeit., 64:1 (1956). 79–102.
- [27] F. Ruskey and M. Weston, A survey of Venn diagrams, Electronic J. Combin., Dynamic Surveys 5, 2005.
- [28] J. Steiner, Einige Gesetze u¨ber die Theilung der Ebene und des Raumes, J. Reine Angew. Math., 1 (1826), 349–364; Gesammelte Werke, ed. K. Weierstrass, Vol. 1, pp. 80–100, AMS Chelsea Publishing, 1997.
- [29] M. J. Wenninger, Polyhedron Models, Cambridge, 1971.
- [30] J. E. Wetzel, On the division of the plane by lines, Amer. Math. Monthly, 85:8 (1978), 647–656.
- [31] A. M. Yaglom and I. M. Yaglom, Challenging Mathematical Problems with Elementary Solutions. Vol. I. Combinatorial Analysis and Probability Theory, Dover Publications, 1987.
- [32] W. B. Yeats, The Collected Poems of W. B. Yeats, Macmillan, 1956.


Keywords: pancake cutting, plane dissection, bent line, zig-zag, configuration, cookie cutter 2010 Mathematics Subject Classification: Primary 05C10, Secondary 05C63, 52C30

