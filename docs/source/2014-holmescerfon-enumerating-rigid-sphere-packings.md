---
type: source
kind: paper
title: Enumerating rigid sphere packings
authors: Miranda C. Holmes-Cerfon
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1407.3285v2
source_local: ../raw/2014-holmescerfon-enumerating-rigid-sphere-packings.pdf
ingested_for_concept: basin-rigidity.md
cites:
  - ../wiki/concepts/basin-rigidity.md
  - ../wiki/problems/5-*.md
  - ../wiki/problems/6-*.md
  - ../wiki/problems/10-*.md
  - ../wiki/problems/11-*.md
  - ../wiki/problems/12-*.md
  - ../wiki/problems/13-*.md
  - ../wiki/problems/14-*.md
  - ../wiki/problems/15-*.md
  - ../wiki/problems/16-*.md
  - ../wiki/problems/19-*.md
  - ../wiki/problems/22-*.md
---

# arXiv:1407.3285v2[cond-mat.soft]8May2015

## Enumerating rigid sphere packings

Miranda C. Holmes-Cerfon

Courant Institute of Mathematical Sciences, New York University.

Packing problems, which ask how to arrange a collection of objects in space to meet certain criteria, are important in a great many physical and biological systems, where geometrical arrangements at small scales control behaviour at larger ones. In many systems there is no single, optimal packing that dominates, but rather one must understand the entire set of possible packings. As a step in this direction we enumerate rigid clusters of identical hard spheres for n ≤ 14, and clusters with the maximum number of contacts for n ≤ 19. A rigid cluster is one that cannot be continuously deformed while maintaining all contacts. This is a nonlinear notion that arises naturally because such clusters are the metastable states when the spheres interact with a short-range potential, as is the case in many nano- or micro-scale systems. We expect these lists are nearly complete, except for a small number of highly singular clusters (linearly ﬂoppy but nonlinearly rigid.) The data contains some major geometrical surprises, such as the prevalence of hypostatic clusters: those with less than the 3n − 6 contacts generically necessary for rigidity. We discuss these and several other unusual clusters, whose geometries may shed insight into physical mechanisms, pose mathematical and computational problems, or bring inspiration for designing new materials.

#### INTRODUCTION

The study of sphere packings has a long and rich history in mathematics [1, 2]. A large body of work has searched for optimal packings – for example, those that maximize the density of an inﬁnite collection of spheres in diﬀerent dimensions [3, 4], or those that minimize an energy or volume functional [5–8], such as the Thomson problem which considers electrons on a unit sphere [9]. However, many applications call for knowing the total set of packings – all the possible ways to arrange a given, ﬁnite number of spheres to satisfy certain conditions. For example, in condensed-matter physics, spheres are used to model atoms, molecules, colloids, or other units of matter, and one asks how large numbers of units behave collectively. A rich set of phases can emerge, such as crystals, gels, and glasses, and the dynamics of forming these or changing between them are often controlled by the geometrical ways to arrange small groups of spheres without overlap [10–14]. Granular materials, such as sand, are also modelled as packings of spheres or other shapes. The total number of mechanically stable packings is argued to give rise to an extensive entropy [15, 16], so once this is known then statistical mechanical ideas may be applied to a system that has so far deﬁed this approach. In chemistry, the set of clusters of hard spheres is conjectured to have the most “rugged” energy landscape, so it may be possible to derive the landscape of molecules with smoother interactions from these [17, 18]. Engineers and materials scientists have proposed to use clusters of nanoparticles as the basis for new materials, but must know the possibilities and how to build them with high yield [19–21].

Here we ask: what are all the ways to arrange n spheres so they form a rigid cluster? A rigid cluster is one that cannot be deformed continuously by any ﬁnite amount and still maintain all contacts. We argue this is the most

natural set of clusters to consider: ﬁrst, because rigid clusters are topologically equivalent – they are all isolated solutions to the system of equations (see (1)) – and second, because when the spheres interact with a shortrange potential, as is the case for many nano- or microscale particles, then these conformations are the local minima on the energy landscape, hence the metastable states where the system spends most of its time [22].

The number of clusters is expected to increase very rapidly so we cannot hope to solve this for arbitrary n [10, 16, 23], yet the solution even for small cluster size would provide valuable insight into the problems above. In physics, a bar is set at n = 13. This is the smallest number where one sphere becomes caged: completely surrounded by neighbouring spheres, so there is expected to be a richer variety of geometrical structures and physical implications [17]. Previous work has listed clusters of n ≤ 11 spheres [24, 25] but these approaches are not easy to extend to higher n, and they use a notion of “rigid” which is not the most physically natural.

We attack this question computationally, using a bottom-up, dynamical algorithm to list rigid clusters of n ≤ 14 spheres, and a subset for n ≤ 19 that contains the ground states (clusters with the maximum number of contacts.) While we have no proof these sets are complete, there is good empirical evidence to suggest they are missing only a very small number of clusters that are too singular (see below) for the algorithm to handle. Thus, for the ﬁrst time, we produce a nearly complete dataset in a physically relevant size regime.

The data contains several surprises – clusters that run counter to certain basic physical intuitions or assumptions – and the main aim of the paper is to highlight these. The biggest surprise is the prevalence of (i) Clusters with fewer than 3n − 6 contacts. This runs counter to the commonly-cited Maxwell’s criterion, which states that a rigid cluster should have at least 3n − 6 contacts

[26–29]. Other surprises include: (ii) Geometrically distinct clusters with the same adjacency matrices – i.e. clusters with the same set of contacts but which are not related by rotations, reﬂections, or permutations; (iii) Ground state clusters that are almost all close-packing fragments (stackings of hexagonal plane fragments) beyond n 15. This occurs at much lower n than for a longer-range potential such as Lennard-Jones; (iv) A sharply decreasing overall proportion of clusters that are close packing fragments; (v) A roughly constant proportion of “singular” clusters (≈ 2.5%) – those that are linearly ﬂoppy but nonlinearly rigid; (vi) Clusters with “circular” modes of deformation: when a single contact is broken, the cluster continuously deforms until it reforms exactly the same contact in exactly the same conﬁguration; (vii) A rigid cluster that has no one-dimensional paths to it: if any contact is broken, it acquires at least two modes of deformation.

These clusters are intended to stimulate the imagination, but they are more than simply geometrical curiosities. Many of them, such as the singular and hypostatic ones, represent states of matter whose behaviour in a thermodynamic system are not yet understood. They bring data to materials science — the bulk behaviour of a material arises in part from geometrical arrangements of its most basic components, for which the set of clusters forms a catalogue of all possible motifs. Inventing new materials may be possible by changing the arrangements of a few localized components [30], and this catalogue can bring inspiration for unusual geometries that are hard to construct explicitly. Additionally, it has been remarked to the author that these clusters have educational value because they are physical representations of unusual solutions to algebraic equations — “a nilpotent group you can hold in your hand” [31]. While the surprises are not surprising from a mathematical perspective – indeed, they are solutions to a system of nonlinear equations, so in principle any type of pathology could occur [32] it is valuable for all of the above reasons to have concrete examples where they occur in a physically relevant system.

A second aim of the paper is to point to problems that could beneﬁt from an applied mathematics perspective. This type of packing problem occurs widely, so having a more rigorous understanding of the problem, its physical implications, and the methods used to solve it would be valuable.

Here is an outline of the paper. In section 2 we precisely deﬁne the problem, brieﬂy describe how we test for rigidity, and outline the enumeration algorithm. In section 3 we show results from the algorithm. Section 4 discusses selected aspects of the methods and results. Section 5 is a brief conclusion.

#### PROBLEM AND METHODS

Here is the problem we wish to solve: given n spheres in three dimensional-space with unit diameters, what are all the possible ways to arrange them without overlap so they form a rigid cluster?

Mathematically, let a cluster be represented as a vector x = (x1,x2,...,xn) ∈ R3n where xi = (x3i−2,x3i−1,x3i) is the center of the ith sphere, combined with a set of algebraic equations of the form

|xi − xj|2 − 1 = 0 (1)

for each pair of spheres (i,j) that are in contact. Additionally, we add six equations to remove the translational and rotational degrees of freedom, for example by ﬁxing one sphere at the origin, another on the x-axis, and a third on the xy-plane, as

xs = 0, s ∈ {1,2,3,5,6,9}. (2)

The system (1) is often represented by an adjacency matrix A by setting Aij = 1 if spheres i,j are in contact, and Aij = 0 otherwise. We consider only clusters where the spheres do not overlap, so require |xi − xj| ≥ 1 for all i = j.

Deﬁning and testing rigidity

A cluster x with adjacency matrix A is rigid if x is an isolated solution to (1),(2), i.e. the solution is a zerodimensional point [33–35]. A cluster x is ﬂoppy if it lies on a positive-dimensional solution set.

Generically, we expect a rigid cluster to have 3n − 6 contacts. This comes from equating the number of variables (3n) to the number of equations, and is the origin of “Maxwell’s criterion” in the physics literature [26]. However, this condition is neither necessary nor suﬃcient for rigidity.

This notion of rigidity is a nonlinear one (to distinguish it from others, we will sometimes say “nonlinearly rigid”), and there is a good physical reason to consider it. Suppose the spheres interact with a very short-range potential, as is often the case for mesoscale particles such as colloids [14, 22, 36, 37]. Then, the energy of a cluster is basically proportional to the number of contacts, so a ﬂoppy cluster can lower its energy by moving along its degrees of freedom until it forms another contact. Once it reaches a rigid cluster it cannot rearrange without breaking a contact to overcome an energy barrier, so these clusters are metastable states where the system spends most of its time in equilibrium.

Testing for rigidity is a hard problem and there is no known algorithm to do it eﬃciently. Indeed, determining whether a given conﬁguration of a linkage is rigid is thought to be coNP-hard [38, 39]. Instead, we test for a

stronger condition: that of pre-stress stability. This is a concept that comes from structural engineering, and asks that a cluster x be the minimum of certain energy function, whose Hessian at the minimum is positive deﬁnite [34, 40].

Here is how we test this. Suppose there is a deformation p(t) depending analytically on parameter t, with p(0) = x. Taking one derivative of the system (1),(2) gives

R(x)p |t=0 = 0, (3)

where R(x) is the Jacobian of (1),(2), called the rigidity matrix. If the right null space of R(x) is empty, we cannot solve for p (0) so the cluster is inﬁnitestimally rigid, or ﬁrst-order rigid. This is suﬃcient for rigidity [34].

This is a linear criterion, so we will sometimes say “linearly rigid” or “linearly ﬂoppy.” A cluster that is linearly ﬂoppy may or may not be rigid. The right null space of the rigidity matrix gives the linear deformations of the cluster, and to check whether these are extendable to ﬁnite deformations we must continue the expansion to higher order.

Taking two derivatives of (1),(2) gives R(x)p |t=0 = −R(p )p |t=0. (4)

By the Fredholm alternative, we can solve for p (0) if and only if there exists v ∈ V such that wTR(v)v = 0 for all w ∈ W, where V,W are the right and left null spaces of R(x). When this condition does not hold, the cluster is second-order rigid and this is also suﬃcient for rigidity [34]. Finding a w for each v to make the inner product non-zero is a challenge, but sometimes it is possible to ﬁnd a single w that works for all v. This happens when wTR(v)v is sign-deﬁnite for v ∈ V, and then the cluster is pre-stress stable. It is possible to ﬁnd such a w by semi-deﬁnite programming methods, for example. See Supplementary Information for details about how this is implemented.

To compute the number of internal degrees of freedom of a cluster when it is not pre-stress stable, we use a numerical method that estimates the dimension of the solution set by taking small steps in each of the candidate tangent directions [41].

Enumeration algorithm

We search for rigid clusters by following all the onedimensional transition paths between clusters. We begin with a single rigid cluster of n spheres. This is easy to obtain, for example by gluing a sphere with three contacts to a cluster of n−1 spheres. Next we break a contact on this cluster, by deleting a single equation in (1). Typically, this makes a cluster with a single internal degree of freedom, i.e. the set of solutions to the reduced system

of equations forms a one-dimensional manifold. When this is the case we follow this one-dimensional path numerically until a new contact is formed [41]. The new contact adds an equation to the system, so the resulting cluster is typically rigid. This cluster could be merely a permutation of the cluster we originally started with, but it could also be an entirely distinct cluster. In the latter case, we add it to our list of rigid clusters.

For each cluster in our list, we break all subsets of contacts that lead to a one-dimensional transition path, follow each path, and keep track of the clusters at the other end. When we reach the end of the list, we stop: we have the entire set of pre-stress stable clusters that are connected to the starting cluster by the one-dimensional paths that are computed.

#### RESULTS

This algorithm was run to enumerate rigid clusters of size n ≤ 14. Table I shows the total number of rigid clusters found for each n; the coordinates are available in the Supplementary Materials or on the website [42]. The total number N(n) increases very quickly: a good ﬁt is N(n) ≈ 2.5(n − 5)!. This is faster than the exponential increase of clusters with smooth potentials [10, 23]. The discrepancy may be because the minimum gap between non-contacting spheres in a packing appears to become arbitrarily close to 1 — for n = 14 it is 1.3×10−5 [41] but for a smooth potential it is typically bounded away from the potential’s minimum because of the huge strain that would otherwise be imposed.

To ﬁnd clusters[43] with the maximum possible number of contacts M(n) for n = 15–19 we make the following approximations. First, we restrict computations to the set of clusters with at least m contacts; call this set Sm. Second, we break no more than 3 contacts simultaneously to ﬁnd each transition path. These truncations are reasonable because we checked that for n ≤ 13, Sm is connected provided m > M(n), where M(n) is the maximum possible number of contacts, and this continues to hold even when breaking no more than 3 contacts.

Table I organizes the data according to the number of contacts in each cluster. A generic rigid cluster must have 3n − 6 contacts, and indeed most clusters do: 97% for n = 11 − 14. However, our system is not generic because the spheres all have the same diameters, so there are many solutions that are special in some way. We now highlight these and other interesting features of the dataset.

Hypostatic clusters The biggest surprise is the existence of clusters with fewer than 3n − 6 contacts: hypostatic clusters. The smallest has n = 10 spheres and is “missing” one contact; it is shown in Figure 1 (left). To our knowledge this is the ﬁrst discovery of a hypostatic packing of spheres. (Hypostatic packings of ellipsoids

|n<br><br>|number of contacts 3n − 9 3n − 8 3n − 7 3n − 6 3n − 5 3n − 4 3n − 3 3n − 2<br><br>|Total|
|---|---|---|
|5<br><br>6<br><br>7<br><br>8<br><br>9<br><br>10<br><br>11<br><br>12<br><br>13<br><br>14<br><br><br>|1<br>2 5<br><br><br>13 52 1 259 3 2 18 1618 20 1<br><br>11 148 11,638 174 8 1 87 1221 95,810 1307 96 8 1 707 10,537 872,992 10,280 878 79 4|1<br><br>2<br><br><br>5 13 52 263 1659 11,980 98,529 895,478<br><br>|
| |3n − 4 3n − 3 3n − 2 3n − 1 3n 3n + 1 3n + 2| |
|15<br>16<br>17<br>18<br>19<br>|7675 782 55 6<br><br>7895 664 62 8<br><br>7796 789 85 6<br><br>9629 1085 91 5<br><br>13,472 1458 95 7|(9 × 106 est.) (1 × 108 est.) (1.2 × 109 est.)<br><br>(1.6 × 1010 est.)<br><br>(2.2 × 1011 est.)<br>|


TABLE I. Number of clusters found for each n, organized by number of contacts in each cluster. For n ≥ 15 only clusters with a given minimum number of contacts were enumerated.

![image 1](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile1.png>)

- FIG. 1. Selected hypostatic clusters. From left to right: n = 10 (smallest hypostatic cluster, missing 1 contact), n = 11 (missing 2 contacts), n = 11 (missing 2 contacts), n = 14 (missing 3 contacts; light blue spheres are n = 10 hypostatic cluster), n = 19 (missing 6 contacts; dark blue spheres are n = 11 hypostatic cluster).


have been observed [44], but these arise because of the extra rotational degrees of freedom when the aspect ratio of the sphere is perturbed [45].) For n = 11 there are 2 clusters missing two contacts, also shown in Figure 1, and 18 clusters missing one contact. Most clusters missing one contact are obtained from the n = 10 hypostatic cluster by gluing a sphere, but the clusters missing two contacts cannot be formed this way. The smallest cluster missing 3 contacts occurs for n = 14, see Figure 1.

All of these are rigid, despite having several linear degrees of freedom. It is helpful to build these using a magnetic ball-and-stick set,[46] because the rigidity is a highly cooperative property that is hard to convey in two dimensions. A common feature is that several spheres lie in a plane stabilized at its boundary. Spheres in the plane can move perpendicular to it inﬁnitesimally, but cannot move any ﬁnite amount without breaking a contact somewhere else. For example, the n = 10 cluster is made of a rigid 6-cluster (dark+light blue) and a tetrahe-

dron (green+light blue) that share a sphere (light blue) and two contacts to make a square face. Without the red sphere, these can twist along a single degree of freedom. When the red sphere is added exactly in the plane of the spheres it contacts, this stabilizes the twist and rigidiﬁes the cluster.

Not all hypostatic clusters are built on planar arrangements though; see the cluster in Figure 6 which will be discussed later.

One might wonder: is it possible to build a rigid cluster missing arbitrarily many contacts? The answer is yes, and can be done using the left-most n = 11 cluster as a scaﬀold. This cluster is formed from a rigid cluster of 7 spheres (dark blue) combined with a group of 4 (light blue) arranged in three planes that intersect in a line. One can continually add groups of 4 on top of this to extend the planes; each group of 4 increases the number of contacts missing by 2, so that asymptotically the number of contacts is ∼ 2n as n → ∞. Figure 1 shows a cluster

of n = 19 that is missing 6 contacts.

In fact, Robert Kusner [47] pointed out a family of rigid n-clusters where the number of contacts grows asymptotically as ∼ n: Construct a rigid n-cluster from a large, ball-like region of the face-centered cubic (fcc) sphere packing, carving out the inside in such a way that the remaining spheres form a rigid shell surrounding a large cavern crossed by many parallel columns of spheres from the fcc packing. Since the number of spheres in this cluster is dominated by the number of spheres in the columns, which scales like the volume of the cavern, while the remaining number of spheres scales like the area of the shell, the number of contacts is asymptotically that for the columns, namely, 1 per sphere. This is the smallest possible asymptotic growth rate for the number of contacts, since otherwise the cluster loses connectivity.

Clusters with the same adjacency matrices Another big surprise is that sometimes (1),(2) has more than one physically realizable solution. In this case a single adjacency matrix corresponds to two or more distinct clusters. The smallest cluster for which this occurs is n = 11 and the pair of solutions is shown in Figure 2. They diﬀer by the location of a single sphere (red), which forms contacts with three spheres (light blue) either above or below the plane of the these spheres.

For n = 12 and 13 we ﬁnd 23 and 474 pairs with the same adjacency matrix respectively. For n = 14 there are 666,3,3 adjacency matrices with 2,3,4 solutions respectively. These multiple solutions do not all diﬀer by a single sphere but can vary in more complicated ways. For example, Figure 2 shows a pair of solutions for which all spheres have at least four contacts. This solution is made of two rigid clusters of 6 (light blue / red) and 7 (green/red) spheres, glued together so they share a sphere (red) and form 3 other contacts. One can check this gluing condition implies the resulting cluster has 3n−6 contacts if the two sub-clusters do. The ﬁgure also shows a quadruple of solutions for n = 14, which is hard to decompose into rigid body sub-components.

Note that generically, for an inﬁnitesimally rigid cluster with no inequality constraints and random edge lengths, one actually expects to have a very large number of diﬀerent embeddings – the best-known upper bound on the number of embeddings grows exponentially with n, and one can construct classes of two-dimensional graphs where the lower bound does also [48]. Therefore, the surprise could equally be construed as there being so few cases where (1),(2) have multiple solutions. This points to the importance of non-overlap constraints, and the related phenomenon of geometrical frustration, in physical systems.

Hyperstatic clusters / Ground states At n = 10 we begin to ﬁnd clusters with greater than 3n − 6 contacts: hyperstatic clusters. This is expected, since the densest known sphere packing of R3 has spheres with 6 contacts each, arranged in a close-packing by stacking

planes of a hexagonal lattice [4].

The ground-state clusters, those with the maximum possible number M(n) of contacts, are shown for selected n in Figure 3. Dark blue spheres form fragments of a close-packing, and other colours represent defects. The ground states appear to converge rapidly to closepackings: for n = 15,16,19 there is one ground state with a defect, and for n = 17,18, there are none. This is in marked contrast to clusters with a smoother potential such as Lennard-Jones clusters, where non-close-packed arrangements are common in low-energy clusters for n up to at least 100 [23].

A famous mathematical problem is the “kissing problem,” which asks how many spheres can touch a single sphere without overlap. The answer is 12 [1], and the two clusters that achieve this, one a piece of a hexagonal close-packed (hcp) lattice, the other of a face-centered cubic (fcc) lattice, are the left-most ground states for n = 13. What is not commonly known is there are six other clusters with the same number of contacts, three of which have defects. As n increases, ground states more frequently contain caged spheres: 2/4, 5/6, 6/8, 6/6, 5/5, 6/7 for n =14–19 respectively.

Close-packing fragments Overall, the percentage of clusters which are fragments of a close-packing decreases with n, as 17%,7.2%,3.6%,1.6%,0.63% for n =10-14 respectively. A greater proportion of hyperstatic clusters are close-packing fragments [41]. Some of these are fragments of an hcp or fcc lattice; the ground states have slightly more hcp than fcc fragments, though we expect random stackings (neither hcp nor fcc) to dominate as n increases as the stacking pattern should be combinatorially favoured. It is interesting that spheres in condensed-matter systems frequently crystallize to form a close-packed lattice, despite an apparently increasingly large entropy favouring other states, particularly nonground-states. This dataset and the associated rearrangement and growth pathways could be used to understand such nucleation phenomena.

Singular clusters The dataset contains a great many singular clusters: those which are linearly ﬂoppy, but nonlinearly rigid[49]. All hypostatic clusters are singular, but many others are as well including those with ≥ 3n − 6 contacts. The smallest occurs at n = 9 and is shown in Figure 4 (left); this is a fragment of an fcc lattice. As n increases the fraction of singular clusters is nearly constant: 3%,2.9%,2.7%,2.5% for n = 11,12,13,14 [41]. Hyperstatic clusters can also be singular, as are two of the ground states for n = 13.

The n = 9 singular cluster was observed to occur experimentally with surprisingly high probability. These experiments considered isolated systems of N = 9 (or smaller) micron-scale hard spheres in a ﬂuid, interacting with a short-range potential induced by depletion forces. They measured the equilibrium probabilities of all 52 clusters [14], and found the singular one with frequency

![image 2](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile2.png>)

- FIG. 2. (a) Smallest clusters with the same adjacency matrix (n = 11) . The dark(light) blue spheres have identical coordinates on each, while the red sphere forms three contacts with the light blue spheres in two diﬀerent ways. (b) Another pair with the same adjacency matrix (n = 12). The green+red spheres form a rigid cluster and have identical locations in each cluster, while the blue+red forms another rigid cluster. It shares three contacts and the red sphere with the green+red cluster, and there are two diﬀerent ways to perform this gluing. (c) Four clusters with the same adjacency matrix (n = 14) . The ﬁve dark blue spheres form a rigid cluster, while other spheres are colored to aid visualization.


11%. This is much higher than if all clusters occurred with equal probability, and is not explained by considering particle permutations, or rotational or translational entropies. What is a likely candidate is the vibrational entropy — the volume of conﬁguration space explored by fast particle vibrations induced by the short-range potential. For a regular cluster, one can approximate this entropy by supposing the spheres in contact are attached by harmonic springs, so the energy near the cluster is quadratic. For a singular cluster, this approach fails, because one of the directions of the quadratic function becomes perfectly ﬂat so the entropy associated with this direction diverges.

Therefore, singular clusters may be an important part of the free-energy landscape when the spheres are thermal. Since they appear to be robust (at least for small n), it is important to learn how to evaluate the entropies of these clusters correctly. Ideally one would like the result to be independent of the choice of interaction potential, for example as in [22]. While it is not yet known how to do this beyond the harmonic approximation, it is possible that ideas from algebraic geometry involving asymptotic volumes of intersecting manifolds may be helpful [50], provided they can also be turned into a computational algorithm that can be applied to systems with many variables.

Circular transition paths The paths used to ﬁnd rigid clusters are also relevant pieces of a cluster’s conﬁguration space. For example, they are the minimumenergy paths between rigid clusters when the spheres interact with a short-range potential, so can be used to evaluate the leading-order transition rates [22]. What are the topologies of the paths? Most are intervals connecting distinct clusters, as expected (Figure 5 (left).) Interestingly, we also ﬁnd paths which are circles: we break a contact, move along the one-dimensional path, and re-form exactly the same contact in exactly the same conﬁguration. This ﬁrst happens for n = 11 as shown in Figure 5 (right). For n = 13 there are roughly 18,300 circular paths, and they occur for all types of clusters and paths (regular/singular/hyperstatic/hypostatic.)

This suggests there could be circular paths that do not eventually form another contact: the cluster may internally deform indeﬁnitely without ever becoming rigid. Such a cluster would be metastable since it could not reach a lower-energy state without ﬁrst breaking a contact, so for certain applications one should treat them on par with rigid clusters. How to ﬁnd such circular metastable states is an open question.

We note in passing that these paths may be analogous to the “localized” soft modes recently discovered in gels and networks [30, 51], where an inﬁnite collection of points with distance constraints contains an ap-

![image 3](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile3.png>)

- FIG. 3. Clusters with the maximum number of contacts, for 13 ≤ n ≤ 19. Dark blue spheres all form a close-packing, while coloured spheres form defects. In some cases there is more than one natural way to group the spheres so the defects are given diﬀerent colours, i.e. the close-packing is either (dark blue + light blue), or (dark blue + green).


parently circular deformation mode with nearly localized point displacements.

A cluster with no one-dimensional deformation paths We found a cluster at n = 11 that cannot be accessed from any other by one-dimensional paths, shown in Figure 6. We checked that breaking any single contact

except two (in red) forms a regular cluster with two degrees of freedom. When either or both of the red contacts is broken, the cluster is still rigid. Therefore there does not exist a subset of contacts that, when broken, forms a cluster with one degree of freedom.

We found this cluster by accident, by deleting a sphere

![image 4](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile4.png>)

- FIG. 4. Selected singular clusters, for n = 9, 10, 11 (left to right). Each has a linear degree of freedom, but is nonlinearly rigid. These are new seeds: they cannot be formed by gluing spheres to a smaller cluster. They all have 3n − 6 contacts.

![image 5](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile5.png>)

- FIG. 5. Left: a typical transition path, with the topology of


- a line segment. A contact is broken, and the cluster deforms into a geometrically distinct cluster. Right: a circular transition path (n = 11.) When the red contact breaks (top left), the light blue spheres twist to the right (top right), creating space for the red sphere to move down past the plane of the dark blue spheres, which are ﬁxed in place. When the light blue spheres twist back to center all spheres return to their original positions except the red one (bottom right). The light blue spheres twist left (bottom left), allowing the red sphere to move back up through the plane and return to its original position.


(red) from an n = 12 cluster. This leads to an intriguing idea — perhaps other such highly singular clusters could be discovered through this method of “catalysis” by extra particles?

DISCUSSION

How to understand hypostaticity?

How is it possible for a cluster to have fewer than 3n − 6 contacts? To answer, it is helpful to have a lowdimensional analogy of system (1). Suppose the space of “clusters” is three-dimensional. Then each single contact equation in (1) is solved by points on a two-dimensional manifold: a surface. Two contacts make two surfaces that generically intersect in a one-dimensional manifold, or a curve, and three contacts make three surfaces that generically intersect at a point, as shown in Figure 7 (left).

Following this analogy, having extra contacts means

![image 6](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile6.png>)

- FIG. 6. A cluster the algorithm cannot ﬁnd (left) (n=11). This is a fragment of an hcp lattice that is missing 1 contact. Breaking either or both of the red contacts gives a nonlinearly rigid cluster. Breaking any other contact gives a cluster with two degrees of freedom. Therefore there are no onedimensional transition paths leading to this cluster. Right: the cluster it came from (n=12), by deleting the red sphere.

![image 7](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile7.png>)

- FIG. 7. A low-dimensional analogy to understand nonlinear rigidity. Each contact is represented by a surface, and a nonlinearly rigid cluster is an isolated intersection point (in red). Left: generically, three surfaces are required in R3 for an isolated intersection point; this is an analogy for a regular cluster. Middle: four surfaces intersecting at a single point,


- as for a hyperstatic cluster. Right: two surfaces that intersect
- at a single point, as for a hypostatic cluster.


there is one (or more) additional equation in (1) for which x is already a solution. Figure 7 (middle) shows an example where four surfaces intersect at a point instead of three. Deleting one of the surfaces still leads to an isolated intersection point.

Having fewer contacts is also possible, as shown in Figure 7 (right). Here two surfaces intersect at a single point where they are exactly tangent. Linear analysis would predict a two-dimensional solution set, however we cannot move any small but ﬁnite distance away and remain on both surfaces, so this point is a rigid solution. Perturbing the surfaces slightly, for example by shifting one up or down, will either destroy the intersection point or turn it into a one-dimensional curve, so a hypostatic cluster (and any singular cluster) is a special case that is extremely sensitive to the choice of parameters.

Comparison with previous results

Two previous studies sought to enumerate clusters with 3n − 6 contacts, by listing all non-isomorphic adjacency matrices and trying to solve (1) for each. Arkus et al. [24] solved for the positions of the sphere centers analytically, or proved there is no solution, so this is guaranteed to be the complete set of clusters up to n = 10 with at least 3n−6 contacts, although these were not tested for rigidity. Hoy et. al. [25] used Newton’s method with random initial conditions to solve for the positions of the sphere centers. Their method is not provably complete, partly because Newton’s method is not guaranteed to ﬁnd a solution even if it exists, and partly because they incorrectly assumed a rigid cluster always contains a Hamiltonian path [52]. Nevertheless they produced a large dataset for n ≤ 11 that can be used to test other methods.[53] Our set of clusters is nearly identical to theirs, but with the following discrepancies for n = 11: (i) They list two clusters as rigid that our method identiﬁes as ﬂoppy. (ii) They do not ﬁnd the second solution for the adjacency matrix with two solutions. (iii) They do not ﬁnd hypostatic clusters, because they do not look for these.

Completeness of the data

The discovery of a cluster that has no one-dimensional deformation paths implies the algorithm cannot ﬁnd all rigid clusters — there may be other single clusters or collections of clusters that are not accessible from the starting set by such paths. Additionally, we test only for pre-stress stability, and do not consider clusters that are rigid under weaker conditions. Nevertheless, the agreement with previous studies for smaller n makes it reasonable to expect it ﬁnds the vast majority of rigid sphere packings; we suspect the missing clusters or collections are rare. Perhaps it enumerates a complete subset of packings: for example, the set of non-singular clusters may be connected by one-dimensional transition paths. Proving such a statement or a variant (such as for nonidentical spheres, or overlapping spheres), would be valuable because the algorithm is fast, so it could be applied to less-studied systems such as spheres of diﬀerent sizes, or objects of diﬀerent shapes.

Bottleneck

The computational bottleneck is not only the factorial growth in the number of clusters, but also the growth in the number of subsets of contacts that must be broken to ﬁnd transition paths leading out of hyperstatic clusters. For example, for a cluster of n = 13 with 3 extra contacts, we have to break 4 contacts generically to ﬁnd a

transition path, so we have to check roughly 3n4−3 sets. This is the equivalent of ≈ 2,000 regular clusters, or 1/50

of the total number. This worsens at the number of extra bonds grows: for n = 19, a ground state with 9 extra contacts is the equivalent of roughly 3n9+3 /(3n − 6) ≈ 109 regular clusters. Higher n may be feasible by developing new methods to avoid checking all possible subsets, e.g. by predicting in advance which subsets are likely to lead to valid transition paths. Ideas from physics may be useful, for example those which study the “soft” modes of interacting particle systems and show these give rise to catastrophic deformations [54, 55].

Weaker rigidity tests

It would be fascinating to ﬁnd clusters that are rigid under a weaker condition than pre-stress stability, but there is no known eﬃcient method to test this. Indeed, even the notion of higher-order rigidity is diﬃcult to deﬁne [56, 57]. Yet, to compute clusters for physical applications, it is not always necessary to prove rigidity, numerically or otherwise. Sometimes, knowing that a cluster is rigid or ﬂoppy “to a certain order” is useful information, because it may be that higher-order physics controls the ﬂexibility properties beyond this. It would be interesting to extend rigidity tests to include physically relevant higher-order information, despite what these do or do not imply for actual rigidity.

A related problem is to consider tests for ﬂoppy clusters. Is there an equivalent notion of pre-stress stability for a cluster with one or more internal degrees of freedom – i.e. is there a test that guarantees the cluster lives on a manifold of a particular dimension? Answering this would not only make the algorithm above more rigorous, but would also aid in computing more general conﬁguration spaces, which can include ﬂoppy components [58].

Questions such as these arise in more general systems than clusters. For example, [30] has found a network of linkages (points connected by distance constraints), with a mode of deformation that appears only in the limit as the system size approaches inﬁnity. The mode is localized, with displacements decreasing exponentially away from a hot spot, yet these very small displacements are enough to cause the system to be technically rigid for any ﬁnite system size. Whether the mode is a ﬁnite or an inﬁnitesimal motion determines how the network behaves as a material, but it is not yet understood how to determine this within the current rigidity framework.

It is worth noting that (1),(2) is a system of algebraic equations, so in principle we can extract any information about the solution, such as whether it is an isolated root, a multiple root, or a positive-dimensional solution, by knowing its full algebraic properties. We have tried implementing known algorithms — such as computing the Gr¨bner basis [59], Hilbert function [60–62], or solving

directly using the numerical algebraic geometry package Bertini [63], but the system was too large for all of these. For certain clusters these worked when we could reduce the system size, for example by decomposing the cluster into rigid sub-clusters that are already known, but we have not yet found a way to make this work for the full generality of clusters encountered.

#### CONCLUSION

We computed a set of rigid clusters of n ≤ 14 hard spheres, using a dynamical algorithm that follows all possible transition paths between clusters. There is empirical evidence to believe this is the entire set of such clusters, minus a few rare clusters that are either too singular or cannot be reached by one-dimensional transition paths. This dataset is much larger and more complete than those produced before, so we expect it to be useful in addressing questions in physics, chemistry, and materials science, for example. Along the way we raised several issues that could usefully be addressed from a mathematical, geometrical, or computational perspective. The data contains several surprises, perhaps the biggest of which is clusters that are hypostatic. The thermodynamic and material importance of these is currently unknown. We discussed these and other clusters, which are hoped will stimulate the mathematical and material imaginations.

Thanks to Michael Brenner, Steven Gortler, and Vinothan Manoharan for many helpful discussions, and to Robert Hoy for sharing his data. This material is based upon work supported by the U.S. Department of Energy, Oﬃce of Science, Oﬃce of Advanced Scientiﬁc Computing Research under award DE-SC0012296.

- [1] J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices, and Groups (Springer, New York, 1999).
- [2] E. B. Saﬀ and A. B. J. Kuijlaars, The Mathematical Intelligencer 19, 5 (1997).
- [3] H. Cohn and N. Elkies, Annals of Math. 157, 689 (2003).
- [4] T. C. Hales, Ann. Math. 162, 1065 (2005).
- [5] P. W. Fowler and T. Tarnai, Proc. R. Soc. Lond. A 452, 2043 (1996).
- [6] H. Cohn and A. Kumar, J. Am. Math. Soc. 20, 99 (2007).
- [7] P. K. Newton and T. Sakajo, Proc. Ro. Soc. A 467

(2011).

- [8] C. Uhler and S. J. Wright, SIAM Review 55, 671 (2013).
- [9] M. Bowick, http://thomson.phy.syr.edu/.
- [10] F. Stillinger and T. Weber, Science 225 (1984).
- [11] D. R. Nelson and F. Spaepen, Solid State Physics 42, 1

(1989).

- [12] S. Auer and D. Frenkel, Nature 409, 1020 (2001).
- [13] C. P. Royall, S. R. Williams, T. Ohtsuka, and H. Tanaka, Nat. Mater. 7, 556 (2008).


- [14] G. Meng, N. Arkus, M. Brenner, and V. Manoharan, Science 327, 560 (2010).
- [15] S. Edwards and R. Oakeshott, Physica A 157, 1080

(1989).

- [16] D. Asenjo, F. Paillusson, and D. Frenkel, Phys. Rev. Lett. 112, 098002 (2014).
- [17] M. R. Hoare and J. A. McInnes, Advances in Physics 32, 791 (1983).
- [18] D. J. Wales, Science 293, 2067 (2001).
- [19] V. N. Manoharan and D. J. Pine, Mater. Res. Soc. Bull. 29, 91 (2004).
- [20] J. A. Fan, C. Wu, K. Bao, J. Bao, R. Bardhan, N. J. Halas, V. N. Manoharan, P. Nordlander, G. Shvets, and F. Capasso, Science 328, 1135 (2010).
- [21] N. B. Schade, M. Holmes-Cerfon, E. R. Chen, D. Aronzon, J. W. Collins, J. A. Fan, F. Capasso, and V. N. Manoharan, Phys. Rev. Lett. 110, 148303 (2013).
- [22] M. C. Holmes-Cerfon, S. J. Gortler, and M. P. Brenner, Proc. Natl. Acad. Sci. 110 (2013).
- [23] D. J. Wales and J. P. K. Doye, J. Phys. Chem. A 101, 5111 (1997).
- [24] N. Arkus, V. Manoharan, and M. Brenner, SIAM J. Disc. Math. 25, 1860 (2011).
- [25] R. Hoy, J. Harwayne-Gidansky, and C. O’Hern, Phys. Rev. E 85 (2012).
- [26] J. C. Maxwell, Philos. Mag. 27, 294 (1864).
- [27] J.-N. Roux, Phys. Rev. E 61, 6802 (2000).
- [28] M. V. Hecke, J. Phys.: Condens. Matter 22, 033101

(2010).

- [29] K. Sun, A. Souslov, X. Mao, and T. C. Lubensky, Proc. Natl. Acad. Sci. 109, 12369 (2012).
- [30] J. Paulose, B. G. ge Chen, and V. Vitelli, arXiv:1406.3323 (2014).
- [31] R. Vakil, Personal communication.
- [32] R. Vakil, Invent. math. 164, 569 (2006).
- [33] L. Asimow and B. Roth, Trans. Amer. Math. Soc. 245, 279 (1978).
- [34] R. Connelly and W. Whiteley, SIAM J. Disc. Math. 9, 453 (1996).
- [35] S. J. Gortler, A. D. Healy, and D. P. Thurston, Am. J. of Math. 132, 897 (2010).
- [36] J. P. K. Doye and D. J. Wales, Chem. Phys. Lett. 262, 167 (1996).
- [37] W. B. Rogers and J. C. Crocker, PNAS 108 (2011).
- [38] E. D. Demaine and J. O’Rourke, Geomtric folding algorithms: Linkages, Origami, Polyhedra (Cambridge University Press, 2007).
- [39] T. G. Abbott, Generalizations of Kempe’s universality theorem, Master’s thesis, Massachusetts Institute of Technology (2008).
- [40] R. Connelly and S. Gortler, arxiv:1401.7029 (2014).
- [41] “See supplementary information for more details.”.
- [42] M. Holmes-Cerfon, “http://cims.nyu.edu/∼holmes/packings.html,”.
- [43] Hereafter we say “cluster” to mean “rigid cluster” unless context makes it clear otherwise.
- [44] A. Donev, I. Cisse, D. Sachs, E. A. Variano, F. H. Stillinger, R. Connellly, S. Torquato, and P. M. Chaikin, Science 303, 990 (2004).
- [45] A. Donev, R. Connelly, R. H. Stillinger, and S. Torquato, Phys. Rev. E 75, 051304 (2007).
- [46] For example as manufactured by Geomags or CMS Magnetics.
- [47] R. Kusner, Personal communication at PCMI, June 2014, and subsequent written correspondence.


- [48] C. Borcea and I. Streinu, Discrete Comput. Geom. 31, 287 (2004).
- [49] Usually “singular” also includes all clusters with extra contacts, but here we use the word to mean a more restrictive set.
- [50] A. Chamber-Loir and Y. Tschinkel, Conﬂuentes Mathematici 2, 351 (2010).
- [51] C. L. Kane and T. C. Lubensky, Nature Phys. 10 (2014).
- [52] B. Hayes, “Sphere packings and Hamiltonian paths,” http://bit-player.org/2013/sphere-packings-andhamiltonian-paths (2013).
- [53] Since this paper was submitted, one more enumeration study has been published [64]. This uses the same method as [25] without the Hamiltonian path assumption, to list clusters of n ≤ 13.
- [54] M. Wyart, L. E. Silbert, S. Nagel, and T. A. Witten, Phys. Rev. E 72, 051306 (2005).
- [55] M. Wyart, Phys. Rev. Lett. 109, 125502 (2012).
- [56] R. Connelly and H. Servatius, Discrete Comput. Geom. 11, 193 (1994).
- [57] G. Garcea, G. Formica, and R. Casciaro, In. J. Numer. Meth. Engng 62, 979 (2005).
- [58] A. Ozkan and M. Sitharam, in Proceedings of BiCoB (New Orleans, 2011).
- [59] B. Buchberger and M. Kauers, Scholarpedia 5, 7763

(2010).

- [60] B. Dayton and Z. Zeng, in ISSAC’05, edited by N. Y. ACM (2005).
- [61] B. H. Dayton, T.-Y. Li, and Z. Zeng, Mathematics of Computation 80, 2143 (2011).
- [62] C. W. Wampler and A. J. Sommese, Acta Numerica 20, 469 (2011).
- [63] D. J. Bates, J. D. Hauenstein, A. J. Sommese, and C. W. Wampler, Numerically Solving Polynomial Systems with Bertini (SIAM, 2013).
- [64] R. S. Hoy, Phys. Rev. E 91, 012303 (2015).
- [65] K. Bezdek, Discrete Comput. Geom. 48, 298 (2012).
- [66] K. Bezdek and S. Reid, J. Geom. 104, 57 (2013).
- [67] A. Leykin, J. Verschelde, and A. Zhao, Theoretical Computer Science 359, 111 (2006).
- [68] B. McKay, Congressus Numerantium 30, 45 (1981).


![image 8](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile8.png>)

FIG. 8. Total number of clusters N(n), and the best-ﬁt curve 2.5(n − 5)!

Appendix

Data

This section contains more detailed statistical information about the set of clusters. The set of coordinates is listed on the author’s website [42].

Total number of clusters

Consider the ratios of total number of clusters N(n + 1)/N(n). Table II shows this appears to be multiplied by nearly n − 4.8 for each n. Therefore the total number grows roughly as (n − 5)!. We ﬁt the total number y =

- b · (n − 5)!. Minimizing the mean-square error in linear space over 5 ≤ n ≤ 14 gives b = 2.46. This does a very good job for the data computed, (see Figure 8), but will likely slightly underestimate for larger n.


Close-packing fragments

We determined whether a cluster was a close-packing fragment by choosing three mutually contacting spheres, and rotating this triangle to the seven triangles of a bipyrapid (two tetrahedra in contact.) For each rotation we checked whether all the z-coordinates of the cluster were integer multiples of 2/3, and if they were we checked whether each plane of spheres at constant z formed a hexagonal lattice. The data is shown in Table IV. This also identiﬁes the lattice type of clusters in Figure 3 in the main text.

Singular clusters

We computed the number of rigid clusters for which the Jacobian of (1) had at least one element in the null space. This data is shown in Table V. We also show the numbers of clusters which are both singular, and closepacking fragments.

Gaps

As n increases, the smallest gap between spheres not in contact decreases. This is one major diﬀerence between sphere packings and clusters with a smooth potential, and may be part of the explanation for the combinatorial rather than exponential growth in the number of clusters.

We checked that we are resolving the smallest gap by computing the minimum gap size over all clusters, where the gap for each cluster is the minimum pairwise distance between non-contacting spheres minus 1. (Recall that for n ≥ 15 not all clusters are computed.) The minimum gap decreases continually with n as follows:

n minimum gap

- 6 0.4142
- 7 0.05146
- 8 0.05146
- 9 0.05146
- 10 0.03296
- 11 0.02634
- 12 2.129e-3
- 13 5.768e-5
- 14 1.269e-5

- 15 0.004364
- 16 0.006154
- 17 0.006154
- 18 0.006154
- 19 0.006154


- At n = 13 there are 23, 9 clusters with gaps less than

10−3,10−4 respectively. These are all regular clusters with 3n − 6 contacts. The ten smallest gaps are 10−5× (5.768, 6.881, 7.339, 7.339, 7.361, 7.505, 7.507, 7.635, 7.694, 11.02).

- At n = 14 there are 929, 244, 34, 6 clusters


with gaps less than 10−3,10−4,5 × 10−5,2 × 10−5 respectively. All have 3n − 6 contacts, and all are regular except three of the ones with the largest gaps. The ten smallest gaps are 10−5 × (1.269,1.377,1.385,1.385,1.387,1.744,2.536,2.538,2.538,2.539).

The smallest gaps for n = 14 are close to our tolerance for adjacency (tolA = 10−5), but the gaps appear to approach the minimum smoothly, with a jump to tolA, so it is likely we have resolved the cutoﬀ. However, applying the algorithm for larger n will require changing the numerical parameters to resolve smaller gaps.

|n|# of contacts - 3n −9 −8 −7 −6 −5 −4 −3 −2 −1 0 +1 +2 +3|Total|
|---|---|---|
|6<br><br>7<br><br>8<br><br>9<br><br>10<br><br>11<br><br>12<br><br>13<br><br>14<br><br><br>|2 2.5 2.6 4 – 5.0 – – 18 6.2 6.7 –<br><br>5.5 8.2 7.2 8.7 8 – 7.9 8.3 8.2 7.5 12 8<br><br>– 7.3 8.6 9.1 7.9 9.1 9.9 –|2 2.5 2.6<br><br>4<br><br>5.1<br><br>6.3<br><br>7.2<br><br>8.2<br><br>9.1<br>|
|15<br>16<br>17<br>18<br>19<br>|8.7 9.9 13.8 –<br><br>10.1 12.1 10.3 –<br><br>11.7 12.7 10.6 –<br><br>12.1 12.8 15.2 –<br><br>12.4 16.0 19.0 –| |


TABLE II. Ratios of number of cluster of each type, to the number of the same type with one less sphere.

The cumulative gap size distributions are shown in Figure 9. These are a fascinating mixture of smooth distributions, plus sharp jumps when many clusters have the same minimum gap size.

Scaling of the maximum number of contacts

The “Combinatorial Kepler Problem” asks how M(n) behaves as n → ∞. We expect M(n) ∼ 6n to leading order as the cluster approaches a close-packing, but one can also include surface corrections, which scale as n2/3. Bezdek et al. [65, 66] proved that 6n−7.862n2/3 ≤ M(n) ≤ 6n−0.926n2/3, where the upper bound holds for all n and the lower bound holds for n = 6,19,...,k(2k2+ 1)/3, k ∈ N. We ﬁnd that M(n) = lower bound +1 for

- 6 ≤ n ≤ 19, (except n = 12 where the correction is 2), and the upper bound is more than double the maximum; this suggests the lower bound is closer to the correct scaling so the bounds could be strengthened. Table III shows the maximal number of contacts M(n) found by our algorithm, and the lower and upper bounds for M(n) as proven in [65, 66]. The upper bound is proven for all n and the lower bound for n = k(2k2 + 1)/3, k ∈ N.


![image 9](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile9.png>)

![image 10](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile10.png>)

![image 11](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile11.png>)

![image 12](<2014-holmescerfon-enumerating-rigid-sphere-packings_images/imageFile12.png>)

FIG. 9. Cumulative gap size distribution for n = 11, 12, 13, 14.

|n|5 6 7 8 9 10 11 12 13 14 15 16 17 18 19|
|---|---|
|ceil(6n − 7.862n2/3) M(n) ﬂoor(6n − 0.926n2/3)<br><br>|8 11 14 17 20 24 28 31 35 39 43 47 51 55 59<br>9 12 15 18 21 25 29 33 36 40 44 48 52 56 60 27 32 38 44 49 55 61 67 72 78 84 90 95 101 107<br>|


##### TABLE III. Upper and lower bounds for the combinatorial Kepler problem, and our data. The upper bound is proven for all n and the lower bound for n = k(2k2 + 1)/3, k ∈ N.

|n|# of close-packing fragments (total # of clusters)<br><br>3n − 7 3n − 8 3n − 7 3n − 6 3n − 5 3n − 4 3n − 3 3n − 2|
|---|---|
|5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>|1 (1)<br><br>1 (2)<br><br><br>1 (5) 4 (13) 11 (52) 0 (1) 33 (259) 3 (3)<br><br>0 (2) 4 (18) 103 (1618) 12 (20) 1 (1)<br><br>0 (11) 13 (148) 339 (11,638) 77 (174) 4 (8) 1 (1)<br><br>1 (87) 57 (1221) 1079 (95,810) 364 (1307) 42 (96) 5 (8)<br><br><br>0 (1) 6 (707) 242 (10,537) 3451 (872,992) 1622 (10,280) 298 (878) 35 (79) 2 (4)|


| |3n − 4 3n − 3 3n − 2 3n − 1 3n 3n + 1 3n + 2 3n + 3|
|---|---|
|15<br>16<br>17<br>18<br>19<br>|1748 (7675) 265 (782) 23 (55) 5 (6)<br><br>1997 (7895) 220 (664) 29 (62) 7 (8)<br><br>2036 (7796) 267 (798) 51 (85) 6 (6)<br><br>2451 (9629) 434 (1085) 59 (91) 5 (5)<br><br>3727 (13472) 681 (1458) 64 (95) 6 (7)|


|n<br><br>|Total close-packing fragments (Total clusters) % Close-packing fragments|
|---|---|
|5<br><br>6<br><br>7<br><br>8<br><br>9<br><br>10<br><br>11<br><br>12<br><br>13<br><br>14<br><br><br>|1(1) 100%<br>1(2) 50% 1(5) 20%<br><br><br>4 (13) 31% 11 (52) 21%<br><br>36 (263) 17%<br><br>120 (1659) 7.2% 434 (11,980) 3.6%<br><br>1548 (98,529) 1.6% 5656 (895,478) 0.63%|


n type

- 10 hcp, hcp, 2d
- 11 hcp
- 12 hcp
- 13 hcp, fcc, hcp, 2d, none, rcp, none, none
- 14 hcp, fcc, none, none
- 15 hcp, hcp, fcc, hcp, fcc, none
- 16 hcp, hcp, fcc, hcp, hcp, fcc, fcc, none
- 17 hcp, hcp, hcp, fcc, fcc, hcp
- 18 hcp, hcp, hcp, fcp, hcp
- 19 hcp, hcp, hcp, fcc, fcc, rcp, none


##### TABLE IV. Close-packing fragment data. Top: number of close-packing fragments, organized by number of contacts. The total number of clusters of each type is shown in brackets. Middle: total number of close-packing fragments for each n. Bottom: close-packing fragment type for ground-state clusters, in the order they are shown in Figure 3 (if shown). Here “fcc, hcp, rcp, 2d, none” stand for face-centered cubic, hexagonal close packing, random-stacking (neither fcc nor hcp), two-dimensional lattice fragment (undetermined), and defective respectively.

|n<br><br>|# of singular clusters (total # of clusters) 3n − 9 3n − 8 3n − 7 3n − 6 3n − 5 3n − 4 3n − 3 3n − 2|
|---|---|
|9<br>10<br>11<br>12<br>13<br>14<br>|1 (52)<br><br>1 (1) 4 (259) 0 (3)<br><br>2 (2) 18 (18) 28 (1618) 1 (20) 0 (1)<br><br>11 (11) 148 (148) 175 (11,638) 7 (174) 0 (8) 0 (1) 87 (87) 1221 (1221) 1311 (95,810) 50 (1307) 1 (96) 2 (8) 1(1) 707 (707) 10,537 (10,537) 10,390 (872,992) 416 (10,280) 4 (878) 3 (79) 0 (4)<br><br>|


| |3n − 4 3n − 3 3n − 2 3n − 1 3n 3n + 1 3n + 2 3n + 3|
|---|---|
|15<br>16<br>17<br>18<br>19<br>|54 (7675) 14 (782) 0 (55) 0 (6)<br><br>87 (7895) 0 (664) 0 (62) 0 (8)<br><br>10 (7796) 0 (798) 0 (85) 0 (6)<br><br>13 (9629) 0 (1085) 0 (91) 0 (5)<br><br>31 (13472) 0 (1458) 0 (95) 0 (7)|


|n<br><br>|Total singular (Total clusters) % Singular|
|---|---|
|9<br><br>10<br><br>11<br><br>12<br><br>13<br><br>14<br><br><br>|1 (52) 1.9% 5 (263) 1.9% 49 (1659) 2.95%<br><br>341 (11,980) 2.85% 2672 (98,529) 2.71%<br><br>22,058 (895,478) 2.46%|


|n close-packing&singular (total singular)<br><br>|%|
|---|---|
|9 1 (1)<br><br>10 2 (5)<br><br>11 13 (49)<br><br>12 40 (341)<br><br>13 174 (2672)<br><br>14 791 (22,058)<br><br><br>|100% 40% 26.5% 11.7% 6.5% 0.088%|


##### TABLE V. Singular cluster data. Top: number of singular clusters, organized by number of contacts, with the total number of clusters of each type shown in brackets. Middle: total number of singular clusters. Bottom: total numbers of clusters which are both close-packing fragments, and singular.

Numerical Algorithm

The numerical algorithm consists of three components: one to determine the dimension of the solution set to equation (1), (2), one to project onto the solution manifold, and one to walk along a one-dimensional the manifold. We describe these in turn, as well as the algorithm to store and compare clusters.

Determining the dimension of the solution set

Suppose we have an adjacency matrix A representing a set of m contacts, and a solution x

to the corresponding system of equations (1),(2). There is one equation for each pair of spheres (i,j) that are in contact, and the translational and rotational degrees of freedom are removed by ﬁxing the ﬁrst sphere at the origin, the second on the x-axis, and the third on the xy-plane. In practice, we choose three spheres that form a triangle of contacts, to avoid problems if the three spheres lie on a line. All clusters encountered contain at least one such triangle. We wish to determine the dimension of the solution set near x

¯

lies on a smooth manifold so this quantity is well-deﬁned. In particular, we wish to determine whether the dimension is 0, 1, or > 1.

, assuming that x ¯

¯

We do this in two ways. One is a semi-analytic method that determines the dimension via solvability conditions. This can be rigorously justiﬁed, but is not developed to handle every possible case that can appear in practice. The second is purely numerical, based on trying to move small distances in each of the candidate tangent directions. It produces an answer for all cases, and though it is not rigorous, it still worked extremely well in that it gave the correct dimension in cases we could verify with the semi-analytic method. However, it was orders of magnitude slower than the latter, which was necessary to apply our algorithm to larger values of n.

Both methods require looking at derivatives of (1). Let us look for an analytic motion of the sphere centers p

(t) parameterized by t ∈ R with p

¯

(0) = x ¯

. Diﬀerentiating

¯

(1) gives

= 0 (A.5) R(x

R(x ¯

)p’ ¯

= −R(p’ ¯

)p” ¯

)p’ ¯

(A.6)

¯

. . R(x

n

n k

(n−k+1) (A.7)

(n+1) −

(k))p ¯

)p ¯

R(p ¯

¯

k=1

where R(p ¯

) is the rigidity matrix. It is constructed so that (R(p

− p ¯j

) · (y ¯i

− y ¯j

)y ¯

)k = (p ¯i

) for any vector

¯

k

k

k

k

∈ R3n and each contact k, 1 ≤ k ≤ m. From the ﬁnal six equations we have Rm+j = eTs

y ¯

for 1 ≤ j ≤ 6, sj ∈ {1,2,3,5,6,9} for the constrained vertices, where es is

j

the vector with 1 in the sth position and zeros elsewhere. Let the right and left null spaces of the rigidity matrix be V, W respectively, with bases {vi}, {wi} and sizes nv = |V|, nw = |W|.

) is of full rank and the number of rows does not exceed the number of columns, then the solution set is regular, the Implicit Function Theorem applies, and the dimension of the solution set is nv. Otherwise, the solution set is singular, and we use the following numerical algorithms to determine its dimension.

If R(x ¯

Semi-analytic determination of dimension Let the tangent space to the solution to (1) have orthogonal basis B, and let D = |B| be its dimension. This method proceeds as follows:

- 1. If |V| = 0: the cluster is ﬁrst-order rigid. Return D = 0.
- 2. If |W| = 0: there are no solvability conditions on (A.5)–(A.7), so this system can be solved up to any order. Proceed to numerical method, or return D = nv.
- 3. Test for second-order rigidity. To solve (A.6) for


∈ V , where V ⊂ V is a linear subspace, the Fredholm Alternative requires that wTR(v)v = 0 for all w ∈ W, v ∈ V . When this does not hold for any subspace V , the cluster is second-order rigid [34].

p ¯

An arbitrary right and left null vector can be written as v = j ajvj, w = j bjwj, with a = (a1,...,an

), b = (b1,...,bn

). The RHS of (A.6)

v

w

can be written as − i,j aiajR(vi)vj. Taking the inner product with w yields the following:

aT bkQ(k) a = 0, Q(ijk) = wkTR(vi)vj. (A.8)

If we can ﬁnd a linear subspace of a-values such that this holds for all b ∈ Rn

, then we can solve (A.6), and the tangent space is contained in the space V spanned by ajvj. The negation requires showing that for every a ∈ Rn

w

, there is a b ∈ Rn

such that (A.8) is non-zero, and then the cluster is secondorder rigid. This is hard to show in general, but what is possible is to ﬁnd a b such that bkQ(k) is sign-deﬁnite. The left null vector w = j bjwj “blocks” all right null vectors and the cluster is called pre-stress stable. It is possible to ﬁnd such a b using semi-deﬁnite programming (SDP) methods, for example.

v

w

In practice, we only check the vectors bk = ek. If any matrix formed from these is sign-deﬁnite, return D = 0. Otherwise, continue to the next step. We do this because we got lucky: this test always agreed with our numerical algorithm (except for 7 clusters at n = 14 that we left out of

the dataset.) Enumerating larger n where unusual cases are more likely to occur will require implementing SDP methods.

4. If the dimension is still undetermined, continue to the numerical method.

It was shown in [34] that if the cluster is either ﬁrstorder-rigid or second-order rigid as described in the tests (1., 3.) above, then it is rigid, so these tests are suﬃcient to prove rigidity (up to numerical tolerance.) Unfortunately there is no equivalent notion of higher-order rigidity, because it could be that every analytic parameterization of cluster motion has p

(0) = 0, i.e. the cluster corresponds to a “cusp,” in which case there is a diﬀerent system of equations to solve [56, 57]. It would be useful to extend these solvability conditions to higher orders and cusps, even if they do not prove rigidity, because this would still provide useful information about a cluster’s stability.

¯

Numerical determination of dimension This method tries to estimate an orthogonal basis B for the tangent space by doing the following for each vj ∈ V:

- 1. Take a step of size ∆s0 in directions ±vj to obtain

x± = x ¯ ± ∆s0 vj

- 2. Project back onto the manifold of constraints to

obtain x ± = Proj(x±). Initially we also require (x ±−x±) ⊥ vj to prevent the projection from going back to the starting point, but if this fails we relax the condition.

- 3. Let vt = x ±−x ¯

be the estimated tangent vector. If |vt| > xTolMax or |vt| < xTolMin, reject the vector. Otherwise, project vt onto our current estimate of B, and let vt⊥/|vt| be orthogonal to the projection.

- 4. If |vt⊥| > vTol, then add vt⊥ to the basis B.


We use both methods to determine whether to follow a path or not, but only use the semi-analytic method to decide whether or not a cluster is rigid. Therefore all clusters we list are pre-stress stable up to numerical tolerance.

Projecting onto a manifold

to (1), we obtain a more accurate solution by solving (1) using Newton’s method with a given tolerance Tol. This is not an orthogonal projection, but we compared it with the orthogonal projection described in [22] which works for regular clusters, and found the two to be very close. We imposed a maximum step size of ∆xmax in each Newton’s iteration to avoid moving too far away from the solution.

If we have an approximate solution x’ ¯

This method suﬀers several drawbacks for singular clusters. First, Newton’s method loses its quadratic order of convergence, so it typically took an order of magnitude more iterations to converge, and occasionally it

never converged (this happened only very rarely – there were 1548 total projection errors of all types for n = 13.) Second, even though the constraints are satisﬁed to tolerance Tol, the actual solution is less accurate if it is singular. For example, if the equation x2 = 0 is satisﬁed to order , then we expect x ≈

√ . We tested the accuracy of the cluster coordinates by perturbing each cluster by some large amount and re-projecting, and found that all clusters tested (including the very hypostatic ones) appeared to be accurate to within √Tol. In general, one would expect to lose accuracy as the nature of the singularity worsens.

These concerns can be mitigated through the use of deﬂation techniques, see e.g. [60–62, 67]. We tried these, but found them not as useful for our study because they require doubling the number of variables at each deﬂation step. For many singular clusters we had to apply several deﬂation steps before we obtained quadratic convergence and linear accuracies, however for these clusters we achieved accuracies of √Tol anyways so the huge slowdown due to the extra variables was not worth the computational eﬀort.

Moving along a one-dimensional manifold

Once we determine that a solution set to (1) is onedimensional, we move along it as follows: ﬁrst, we extract the direction(s) that make the broken contacts increase in length. For each direction, we alternate between taking a step of size ∆s along the manifold in the tangent direction vk, and projecting back onto the manifold. After each projection we form the rigidity matrix in (A.5), compute its null space V, and ﬁnd the next tangent direction vk+1 by the least-squares projection of vk onto V. This ensures that we keep going in the same direction, i.e. we don’t accidentally start moving backwards along the manifold, and it provides an estimate of the single tangent direction when the path is singular.

After the ﬁrst step, we check the dimension as in section , and stop moving if this dimension has increased or decreased. For n = 13 it increased for 3851 paths and decreased for 23. We do not check the dimension after the ﬁrst step, as this is very time-consuming.

At each step we check whether two spheres initially not in contact are within some tolerance 1 + tolA0. The ﬁrst time this happens we back up one step and repeat the continuation with a smaller step size ∆s0, and again stop when spheres are within 1+tolA0. Then, we project onto this new set of constraints and check if the cluster is rigid, using a new tolerance tolA to determine whether two spheres are adjacent. If, as happens very occasionally, this projection fails (for example because tolA0 is deliberately chosen too big initially, to “catch” more pairs than are actually adjacent), we delete subsets of the new constraints until the projection succeeds. If it never suc-

ceeds we abandon the cluster. Note that tolA0 should be chosen comparable in magnitude to ∆s because sometimes spheres can come into contact tangentially.

Cluster isomorphism

We keep track of clusters through their adjacency matrices in a hash table. Each adjacency matrix has a canonical form that we compute using nauty [68]. This is converted to a binary vector a ∈ {0,1}n

2

and we deﬁne an ordering by setting a < b if ak < bk where k is the ﬁrst entry where they diﬀer.

Adjacency vectors are stored as a binary tree. Each leaf contains the indices of the clusters with that adjacency matrix, and the indices of the child adjacency vectors that are larger or smaller. To add an adjacency vector a we compare it to a leaf b on the tree, and move to the larger or smaller child depending on whether a > b or a < b. We add a as a child to the leaf at the end of the tree.

When we ﬁnd a new cluster, we compute the canonical form of the adjacency matrix and coordinates. If this adjacency matrix is already in the list, we compare the cluster and its reﬂection to those with the same adjacency matrices, by rotating so the same spheres on each are at the vertices of a given equilateral triangle. We use a tolerance tolD to determine if the coordinates are the same.

Numerical parameters

Here are the values of the numerical parameters used in most of the simulations. For n =11–13 we ran several simulations with diﬀerent choices of parameters, and combined data if necessary. Typically the datasets for n = 12,13 diﬀered by an O(1) number of clusters, while for n = 11 they were typically identical. All numerical computations were performed in double precision.

Parameter Value Description ∆s 5e-3 step size along path, in endgame ∆s0 5e-2 step size along path, initially Tol 9e − 16 tolerance for Newton’s method when

projecting / sharpening cluster coordinates

TolN 1e-6 tolerance on singular values for null

space of rigidity matrix ∆xmax 0.02 maximum step size in Newton’s method tolA 1e-5 tolerance for spheres being adjacent tolA0 1e-3 initial tolerance for spheres being adja-

cent, used to stop following path tolD 1e-5 tolerance for coordinates of a cluster being identical

xTolMax 10∆s upper bound on cluster displacement, to determine if a cluster has moved along tangent space xTolMin ∆s/8 lower bound on cluster displacement, to determine if a cluster has moved along tangent space

vTol 2∆s tolerance for determining whether a unit vector is orthogonal to the estimated tangent space: the part orthogonal to the projection must have at least this magnitude. Depends on step size ∆s used to move in tangent space, because of curvature of manifold.

The value of tolA was chosen to stay well away from the resolution of √Tol ≈ 3e − 8 of the coordinates of the singular clusters, to avoid computing junk clusters. For n ≥ 15 it will be unable to resolve the gaps of certain regular, non-hyperstatic clusters. These gaps may be resolvable in double precision for a few more values of n because tolA can be increased and still be larger than the numerical precision of the cluster coordinates. However, as n increases further the distances between non-contacting spheres are expected to become arbitrarily close to 1, so higher precision will be necessary.

