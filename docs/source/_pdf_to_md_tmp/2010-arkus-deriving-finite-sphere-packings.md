## arXiv:1011.5412v2[cond-mat.soft]13Nov2011

###### DERIVING FINITE SPHERE PACKINGS

NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER

Abstract. Sphere packing problems have a rich history in both mathematics and physics; yet, relatively few analytical analyses of sphere packings exist, and answers to seemingly simple questions are unknown. Here, we present an analytical method for deriving all packings of n spheres in R3 satisfying minimal rigidity constraints (≥ 3 contacts per sphere and ≥ 3n − 6 total contacts). We derive such packings for n ≤ 10, and provide a preliminary set of maximum contact packings for 10 < n ≤ 20. The resultant set of packings has some striking features, among them: (i) all minimally-rigid packings for n ≤ 9 have exactly 3n − 6 contacts, (ii) non-rigid packings satisfying minimal rigidity constraints arise for n ≥ 9, (iii) the number of ground states (i.e. packings with the maximum number of contacts) oscillates with respect to n, (iv) for 10 ≤ n ≤ 20 there are only a small number of packings with the maximum number of contacts, and for 10 ≤ n < 13 these are all commensurate with the HCP lattice. The general method presented here may have applications to other related problems in mathematics, such as the Erd¨s repeated distance problem and Euclidean distance matrix completion problems.

1. Introduction

We consider all conﬁgurations of n identical impenetrable spheres in R3 that maximize the number of contacts between the spheres.

Our interest in this problem arose through the following question: can one direct the selfassembly of colloidal particles into any desired structure simply by imposing a spherically symmetric binding speciﬁcity on those colloidal particles?1 Colloidal particles are small, (nanometer to micron sized) spherical particles in aqueous solution. In recent years a myriad of methods have been developed to control the binding of particles to each other, thus causing them to self-assemble into clusters [50, 41, 49, 10, 15, 24].

The interactions between the particles typically have a range much smaller than the particle size; the potential energy of such a cluster is then simply proportional to the number of contacts. Structures with maximum numbers of contacts are thus the minima of the potential energy, and correspond to what will form in thermodynamic equilibrium.

Controlling which structures will form thus becomes a problem of controlling which structures correspond to energetic minima, or equivalently to contact maxima. Although minimal-energy clusters have been catalogued for many diﬀerent potentials, e.g. the Lennard-Jones potential [21], they had not previously been calculated for hard (impenetrable) spheres. Thus there was no detailed understanding of what structures could self-assemble in this colloidal system.

The motivating question of how to control the self-assembly of a colloidal system could thus be broken up into 2 parts: (i) Determine what structures can self-assemble, (ii) Determine how to direct the self-assembly of the system such that only the desired structure(s) form. In this paper, we address (i). In [5, 6], we address (ii).

1By ‘spherically symmetric binding speciﬁcity’ we are referring to a situation in which colloidal particles bind isotropically, but not all colloidal particles can bind to one another. For example, imagine assigning labels to the colloidal particles; A, B, C, and so on. Particles sharing common labels will be able to bind to one another, but colloidal particles that do not share a common label can not bind.

1

It should be noted that, in addition to self-assembly, the structures of small clusters of atoms or particles bear directly on problems central to materials science and condensed matter physics, including nucleation, glass formation, and the statistical mechanics of clusters [18, 47, 44]. For instance, the ﬁrst step towards understanding the thermodynamics of a particular cluster system is to calculate the ground states as a function of particle number n [17].

The structures that can self-assemble in this colloidal system can be determined by solving the mathematical problem of which structures globally or locally maximize the number of contacts between n spheres in R3 – i.e. all structures in which either (i) no additional contacts between spheres can exist, or (ii) a contact must ﬁrst be broken in order to form an additional contact. We will refer to such structures as packings. We formulate our problem by focusing on enumerating only minimally-rigid sphere packings, which we deﬁne as packings with at least 3 contacts per particle and at least 3n − 6 total contacts. Minimal rigidity is necessary, but not suﬃcient, for a structure to be rigid. We previously detailed the ground states of these packings as well as some of their interesting features in [7]. Here, we present the results and method more completely. The method we introduce combines graph theory and geometry to analytically derive all minimallyrigid packings of n spheres. We perform this enumeration for n ≤ 10 spheres. Due to the large number of packings that must be evaluated, this analytical method is implemented computationally, and near n = 10 we reach the method’s computational limitations. Finding scalable methods for enumerating packings at higher n is a signiﬁcant challenge for the future.

Already by n = 10, a number of interesting features set in. For n ≤ 9, all minimally-rigid packings have exactly 3n − 6 contacts. The ﬁrst instance of a non-rigid sphere packing that satisﬁes minimal rigidity constraints occurs at n = 9, and more such non-rigid packings arise at n = 10. The ﬁrst instance of packings with greater than 3n − 6 contacts occurs at n = 10. We discuss the geometrical manner in which these maximum contact packings arise, and conjecture that maximum contact packings for all n in this system must contain octahedra. We provide preliminary evidence for this maximum contact conjecture for n ≤ 20, and we show that the putative maximum contact packings of 10 ≤ n ≤ 13 are commensurate with the hexagonal close packing (HCP) lattice, but that maximum contact packings of 14 ≤ n ≤ 20 are not. Furthermore, we show that the number of packings containing the maximum number of contacts is oscillatory with n, and we discuss the origins of these oscillations.

The set of packings we enumerate includes, as a subset, structures previously observed and described in the literature: for example, it includes all minimal-second-moment clusters reported by [48], packings observed experimentally through capillary driven assembly of colloidal spheres [34, 41], as well as the Janus particle structures observed by Hong et al. [29].

This problem is closely related to several unsolved problems in mathematics, such as the Erdo¨s unit distance problem (a.k.a. the Erd¨os repeated distance problem), Euclidean distance matrix and positive semideﬁnite matrix completion problems, and 3-dimensional graph rigidity. Thus the method and results presented here may have direct bearing on these problems.

The organization of this paper is as follows: In the next section we outline our mathematical formulation of the problem and describe our methodology for ﬁnding all minimally-rigid packings of a ﬁxed n. We combine graph theoretic enumeration of adjacency matrices with solving for their corresponding distance matrices. The elements of these distance matrices correspond to the relative distances between spheres in 3-dimensional Euclidean space, and thus yield the packings that correspond to those adjacency matrices. Analytical methods for solving such adjacency matrices that scale eﬃciently with n do not exist. Sections 3 and 4 thus derive a method with improved scaling: Section 3 derives geometrical rules that map patterns in adjacency matrices either (i)

to a conﬁguration of spheres, in which case the adjacency matrix is solved for its corresponding distance matrix or matrices; or (ii) to an unrealizable conﬁguration, in which case no real-valued embedding in 3-dimensional Euclidean space of that adjacency matrix exists in which spheres do not overlap. We show how these geometrical rules, combined with adjacency matrix enumeration, can lead to a complete set of minimally-rigid packings. Each time a new pattern is encountered, a new geometrical rule must be derived; thus this part of the method requires new derivations at each n, and does not scale eﬃciently2. In section 4, we derive a single geometrical rule (the triangular bipyramid rule) that can solve all iterative adjacency matrices. An iterative adjacency matrix is an n × n matrix in which all minimally-rigid m < n subgraphs also correspond to packings. This part of the method applies to any n, and thus scales eﬃciently for all n. Most adjacency matrices at small n are iterative; therefore, this greatly reduces the number of geometrical rules necessary to derive a complete set of packings. Section 5 describes the set of sphere packings we ﬁnd from our study. We provide analytical formulas for packings up to n = 7, and the set of packings for n = 8,9,10 are included in the supplementary information [8]. Section 6 summarizes notable properties of the packings, including how the number of contacts changes with n, the emergence of minimally-rigid structures that are not rigid, and the emergence of maximum contact packings that are commensurate with lattice packings. Section 7 summarizes the main roadblocks towards obtaining results at higher n and contains several ideas and conjectures therein, and also discusses extensions to dimensions other than 3, as well as relevance to other problems of mathematical interest. Section 8 provides some concluding remarks.

2. Mathematical Formulation

We begin by presenting a two-step method for enumerating a complete set of sphere packings that satisﬁes minimal rigidity constraints. The set of all packings of n spheres is a subset of all possible conﬁgurations of n spheres. Thus, to enumerate a complete set of sphere packings we (i) use graph theory to enumerate all n sphere conﬁgurations, and (ii) determine which of those conﬁgurations correspond to sphere packings. The sphere packings we consider here correspond to maxima (local or global) in the number of contacts3. Provided step (ii) is exact, this method will produce a complete set of packings. However, current analytical methods do not scale eﬃciently with n, and are therefore ill-suited for step (ii). Thus, in sections 3 and 4, we use basic geometry to derive an analytical method that can exactly determine which conﬁgurations correspond to sphere packings. Because the number of possible conﬁgurations grows exponentially with n, this analytical process must be implemented computationally. We focus our search to only those sphere packings satisfying minimal rigidity constraints (≥ 3 contacts per sphere, ≥ 3n−6 total contacts), because doing this guarantees that if a graph has an embedding in 3-dimensional Euclidean space, it corresponds to a sphere packing; whereas graphs that are not minimally-rigid can have 3dimensional embeddings without corresponding to packings due to a continuous degree of freedom that allows for the formation of another contact.

We also note that spheres can be thought of as points (Fig. 1a,b), where points correspond to the centers of spheres, and we measure the distance between spheres as the distance between their centers. Throughout this paper we will use the words sphere, point, and particle interchangeably.

- 2This method allowed us to enumerate packings up to n = 8, while standard methods in algebraic geometry (using the package SINGULAR) allowed us to enumerate up to n = 7.
- 3i.e. either the conﬁguration of spheres can not form an extra contact (global maxima), or if an extra contact can be formed, it ﬁrst requires the breaking of an existing contact (local maxima).


2.1. Graph Theory Produces the Set of Possible Packings. A conﬁguration of n spheres can be described by an n×n adjacency matrix, A, detailing which spheres are in contact: Aij = 1 if the ith and jth particles touch, and Aij = 0 if they do not. A system of n spheres has n(n−1)/2 interparticle distances; the 2 possibilities (touching or not touching) per distance thus leaves 2n(n−1)/2 diﬀerent ways of arranging contacts amongst the distances. There are thus 2n(n−1)/2 possible adjacency matrices, each of which potentially corresponds to a packing.

Adjacency Matrix to Distance Matrix Example



- 0 0 1 1 1 1

- 0 0 0 1 1 1
- 1 0 0 0 1 1


- 1 1 0 0 1 1


###### Adjacency Matrix to Distance Matrix Example

Adjacency Matrix to Distance Matrix Example

Figure 1 shows a packing of 6 particles, both as a sphere packing (Fig. 1a) and as points connected by line segments (Fig. 1b). The adjacency matrix corresponding to this packing is shown in ﬁgure 1c. The set of possible packings can be enumerated by considering all adjacency matrices. For n = 6, there are 215 = 32,768 diﬀerent adjacency matrices. Table 1 shows that the number of adjacency matrices grows rapidly with n, reaching 3.5184 × 1013 by n = 10; however, many of these correspond to the same structure due to particle labeling degeneracy. For example, switching labels 5 and 2 of ﬁgure 1 yields another adjacency matrix corresponding to the same structure.4 Adjacency matrices corresponding to the same structure are isomorphic to one another – meaning there will exist a permutation of rows and columns that can translate one matrix into the other5.

 

- 1 1 1 1 0 1
- 1 1 1 1 1 0



 

(1)

- 1 2 3 4 5 6






- 0 0 1 1 1 1

- 0 0 0 1 1 1
- 1 0 0 0 1 1


- 1 1 0 0 1 1


- 0 0 1 1 1 1

- 0 0 0 1 1 1
- 1 0 0 0 1 1


- 1 1 0 0 1 1


###### Adjacency Matrix to Distance Matrix Example

Adjacency Matrix to Distance Matrix Example

- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


 

 

- 1 1 1 1 0 1
- 1 1 1 1 1 0



 

(1)

- 1 2 3 4 5 6


- 1 1 1 1 0 1
- 1 1 1 1 1 0



 

(1)

- 1 2 3 4 5 6






- 0 0 1 1 1 1

- 0 0 0 1 1 1
- 1 0 0 0 1 1


- 1 1 0 0 1 1


- 0 0 1 1 1 1

- 0 0 0 1 1 1
- 1 0 0 0 1 1


- 1 1 0 0 1 1


- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


1 2 3 4 5 6

- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


To generate the complete set of possible packings, we need only enumerate nonisomorphic A’s. Such algorithms exist; examples include nauty and the SAGE package called nice [42, 3]. The number of nonisomorphic matrices is much smaller but still grows exponentially with n. Table 1 shows this growth also; for example at n = 6 the number of potential structures is 156, and at n = 10 it is 12,005,168.

 

 

- 1 1 1 1 0 1
- 1 1 1 1 1 0



 

(1)

- 1 2 3 4 5 6


- 1 1 1 1 0 1
- 1 1 1 1 1 0



 

(1)

- 1 2 3 4 5 6


1 2 3 4 5 6

1 2 3 4 5 6

- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


1 2 3 4 5 6

- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 1 0 r12 1 1 1 1
- 2 r12 0 r23 1 1 1
- 3 1 r23 0 r34 1 1
- 4 1 1 r34 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


(2)

Adjacency Matrix to Distance Matrix Example

(2)

![image 1](<2010-arkus-deriving-finite-sphere-packings_images/imageFile1.png>)

![image 2](<2010-arkus-deriving-finite-sphere-packings_images/imageFile2.png>)

4 1

- 4
- 5
- 6


1 2 3 4 5 6

1 2 3 4 5 6

1 2 3 4 5 6

1 2 3 4 5 6







- 0 r12 1 1 1 1

r12 0 r23 1 1 1

- 1 r23 0 r34 1 1 1 1 r34 0 1 1


- 1 0 r12 1 1 1 1
- 2 r12 0 r23 1 1 1
- 3 1 r23 0 r34 1 1
- 4 1 1 r34 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 1 0 r12 1 1 1 1
- 2 r12 0 r23 1 1 1
- 3 1 r23 0 r34 1 1
- 4 1 1 r34 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 0 0 1 1 1 1

- 0 0 0 1 1 1
- 1 0 0 0 1 1


- 1 1 0 0 1 1


- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


2

1

- 5
- 6


(3)

(3)

2

 

 

 

- 1 1 1 1 0 1
- 1 1 1 1 1 0


- 1 1 1 1 0 1
- 1 1 1 1 1 0



 

(1)

- 1 2 3 4 5 6


3

3









- 0 r12 1 1 1 1

r12 0 r23 1 1 1

- 1 r23 0 r34 1 1 1 1 r34 0 1 1


- 0 r12 1 1 1 1

r12 0 r23 1 1 1

- 1 r23 0 r34 1 1 1 1 r34 0 1 1


1 2 3 4 5 6

1 2 3 4 5 6

(a) (b) (c) (d)

- 1 0 r12 1 1 1 1
- 2 r12 0 r23 1 1 1
- 3 1 r23 0 r34 1 1
- 4 1 1 r34 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 1 0 r12 1 1 1 1
- 2 r12 0 r23 1 1 1
- 3 1 r23 0 r34 1 1
- 4 1 1 r34 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


1

(4)

(4)

 

 

(2)

 

 

- 1 1 1 1 0 1
- 1 1 1 1 1 0


- 1 1 1 1 0 1
- 1 1 1 1 1 0


###### Figure 1. Adjacency and Distance Matrix Representation of Packings.

(a) 6 particle polytetrahedral sphere packing. (b) The same 6-particle packing shown in point/line representation. (c) Corresponding 6 particle adjacency matrix, A. (d) Corresponding relative distance matrix, D.









- 0 r12 1 1 1 1

r12 0 r23 1 1 1

- 1 r23 0 r34 1 1 1 1 r34 0 1 1


- 0 r12 1 1 1 1

r12 0 r23 1 1 1

- 1 r23 0 r34 1 1 1 1 r34 0 1 1


1 2 3 4 5 6

1

1

- 1 0 0 1 1 1 1
- 2 0 0 0 1 1 1
- 3 1 0 0 0 1 1
- 4 1 1 0 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


(5)

(5)

 

 

 

 

(3)

- 1 1 1 1 0 1
- 1 1 1 1 1 0


The set of A’s (potential packings) can be further reduced by imposing rigidity constraints. Most structures with less than 3n − 6 total contacts or less than 3 contacts per particle will not correspond to a packing because there will exist a continuous degree of freedom through which the structure can form one or more bonds. Rigidity requires (i) there be at least 3 contacts per

- 1 1 1 1 0 1
- 1 1 1 1 1 0


1 2 3 4 5 6

1

1

- 1 0 r12 1 1 1 1
- 2 r12 0 r23 1 1 1
- 3 1 r23 0 r34 1 1
- 4 1 1 r34 0 1 1
- 5 1 1 1 1 0 1
- 6 1 1 1 1 1 0


- 4Note that this is purely an exercise in switching particle labels, it is not a statement about the symmetry of the structure - we are not saying that particles 2 and 5 have the same contact distribution. The point is that many matrices can lead to the same structure, because how you label the particles is an arbitrary factor.
- 5See [27] for a nice example of such a permutation.


(4)





- 0 r12 1 1 1 1

r12 0 r23 1 1 1

- 1 r23 0 r34 1 1 1 1 r34 0 1 1


(5)

 

 

- 1 1 1 1 0 1
- 1 1 1 1 1 0


1

(2)

(2)

(2)

(3)

(3)

(3)

(4)

(4)

(4)

(5)

(5)

(5)

particle, and (ii) there be at least as many contacts as internal degrees of freedom – thus there must be at least 3n − 6 contacts6

Table 1 shows how imposing minimal rigidity constraints restricts the number of adjacency matrices. For n ≤ 5 particles, this eliminates all but 1 adjacency matrix, thus identifying a unique packing for each of these n; the doublet, triangle, tetrahedron, and triangular bipyramid, respectively (section 5). For n ≤ 4, all relative distances within these packings are touching and are thus known. However, for n = 5, the packing contains one unknown relative distance, which must be determined. For n ≥ 6, more than one minimally-rigid A exists, and thus rigidity constraints alone are insuﬃcient to identify the number of sphere packings (or to solve for them, as more than 1 distance in each minimally-rigid A is unknown).

###### 2.2. Solving Potential Packings: Algebraic Formulation. To make further progress, we

reformulate our problem algebraically. Each adjacency matrix element, Aij, is associated with an interparticle distance,

rij = (xi − xj)2 + (yi − yj)2 + (zi − zj)2,

which is the distance between particles i and j whose centers are located at (xi,yi,zi),(xj,yj,zj), respectively. The distances are constrained by the adjacency matrix as follows:

- (1) Aij = 1 =⇒ rij = 2r
- (2) Aij = 0 =⇒ rij ≥ 2r


where r is the sphere radius7.

For adjacency matrices with 3n − 6 contacts, this leads to precisely as many equations as unknowns8. The task is thus to solve for the rij ≥ 2r given a particular set of rij = 2r. The particle conﬁguration encoded by each A is thus speciﬁed by a distance matrix, D, whose elements Dij = rij.

The fundamental question is to ﬁnd an eﬃcient, exact method for mapping A → D. If any Dij < 2r, this implies that particles i,j overlap; thus any D with Dij < 2r is unphysical. Figure

- 1d shows the distance matrix corresponding to an n = 6 packing. The interparticle distance between each of the particles that are touching is normalized to 1; for this packing, this leaves


three distances that need to be determined; r12,r23, and r34. In solving A for D, the following scenarios are possible:

- (1) Continuous set(s) of real-valued D correspond to a given A, in which case the structure(s) are not rigid.
- (2) No real-valued D exists that solves A, in which case the structure is unphysical.
- (3) Finite, real-valued D exist that solve A. In this case, the structure(s) correspond to rigid sphere packing(s) provided that all Dij ≥ 2r.


- 6Note that in restricting to structures with exactly 3n − 6 contacts, we will also ﬁnd structures with more than 3n−6 contacts. This is because when we solve for the packings as outlined below, the solutions can end up having more contacts than are assumed in the algebraic formulation.
- 7Strictly speaking, Aij = 0 implies that particles are not touching, and thus that rij > 2r. However, it is convenient to consider all solutions of A, which thus include the possibility rij = 2r for Aij = 0; in other words, a packing can be represented by multiple A’s with diﬀerent numbers of 1’s if the solution to Aij = 0 forces it to a 1.
- 8Without loss of generality, we can set one particle to reside at the origin, another to reside along a single axis (for example the y-axis), and a third to reside in one plane (such as the xy-plane). 6 coordinates are then ﬁxed, leaving 3n − 6 instead of 3n coordinates.


|n<br><br>|A’s|Non-Isomorphic A’s<br><br>|Minimally rigid A’s<br><br>|Iterative A’s|Non-Iterative A’s|
|---|---|---|---|---|---|
|1|1<br><br>|1|1<br><br>|1|0|
|2|2<br><br>|2|1|1<br><br>|0|
|3<br><br>|8|4<br><br>|1|1<br><br>|0|
|4<br><br>|64|11<br><br>|1<br><br>|1<br><br>|0|
|5|1,024<br><br>|34|1<br><br>|1|0|
|6<br><br>|32,768|156|4|3<br><br>|1|
|7<br><br>|2,097,152|1,044<br><br>|29<br><br>|26|3|
|8|268,435,456<br><br>|12,346<br><br>|438|437|1|
|9<br><br>|6.8719 ·1010|274,668|13,828|13,823<br><br>|5|
|10|3.5184 ·1013<br><br>|12,005,168<br><br>|750,352<br><br>|750,258<br><br>|94|


###### Table 1. The Growth of Adjacency Matrices with n.

The number of adjacency matrices (constructed by [42]) decreases rapidly as isomorphism and rigidity constraints are imposed. Iterative and non-iterative are deﬁned in the text. The classiﬁcation of whether an A is iterative or not is here shown after all rules for n−1 particles are applied; thus the non-iterative column shows nparticle non-iterative structures only, and does not include non-iterative structures of less than n particles. Also note that the classiﬁcation of whether an A is iterative or not is thus sensitive to which geometrical rules are used. The number of iterative and non-iterative A’s at n = 10 is diﬀerent from [7] because some modiﬁcations were made to the code since the publication of that paper. Please see the supplemental information [8] for exactly which modiﬁcations have been made.

For every nonisomorphic adjacency matrix, whether there exists a corresponding packing requires solving for D and asking whether the resulting rij’s satisfy these constraints.

2.3. Limitations of Existing Solution Methods. The issue now becomes one of solving a system of n(n−1)/2 constraints (3n−6 equations and n(n−1)/2−(3n−6) inequality constraints). Numerical approaches for solving such a system cannot be guaranteed to converge; for example, Newton’s method requires an accurate initial guess for guaranteed convergence. When a solution does not converge, we do not know if it is because a solution does not exist, or because the initial guess is not suﬃciently accurate9. Algebraic geometric methods (e.g. Gro¨bner bases) [11] are eﬀective, but these algorithms do not scale eﬃciently with n. Our own implementation10 of this method using the package SINGULAR [23] was only able to solve for structures up to n = 7.

In the following section, we use another approach and derive a diﬀerent geometrical method to eﬃciently solve for all sphere packings given a set of nonisomorphic, minimally-rigid A’s. We implement this method up to n = 10, at which point we begin to hit some practical roadblocks; these are discussed at the end of the paper, where we outline potential ways to overcome them.

2.3.1. Chiral Structures. Before proceeding further, it is worth remarking that structures with diﬀerent handedness will correspond to the same distance matrix. We can analyze each D, and

9Furthermore, convergence to an unphysical solution lying within numerical error is also a problem. 10At n = 8, using the software package SINGULAR [23], one matrix takes several hours to solve, and there are

a total of 438 minimally-rigid non-isomorphic A’s.

determine whether it corresponds to a structure that has a chiral counterpart (see section 3.5). We refer to chiral structures as the same packing but diﬀerent states – thus, a distance matrix having a left- and right-handed counterpart corresponds to 1 packing with 2 diﬀerent states. Note that according to our deﬁnition, a diﬀerent packing necessarily corresponds to a diﬀerent state. Thus, the total number of states is equal to the total number of packings plus the total number of chiral counterparts.

3. Geometrical rules solve for sphere packings

We now show how geometrical rules can be used to eﬀectively and analytically solve the class of polynomial equations that are generated by adjacency matrices. We use basic geometry to construct rules associating patterns of 1’s and 0’s in A’s with either a given relative distance, Dij, or an unphysical conformation (in which case no D ≥ 2r exists). There thus exist two types of rules: Elimination rules eliminate an A as unphysical, and distance rules solve an Aij for its corresponding Dij.

- 3.1. Neighbor Spheres and Intersection Circles. With each sphere of radius r, we can associate a neighbor sphere of radius R = 2r, whose surface deﬁnes where another sphere must lie if it is to touch the original sphere in question (Fig. 2a). When 2 spheres touch, their neighbor spheres intersect in an intersection circle (Fig. 2b). The radius of the intersection circle follows


√3

from straightforward geometry, and is

2 R (see supplemental information for derivation [8]).

![image 3](<2010-arkus-deriving-finite-sphere-packings_images/imageFile3.png>)

![image 4](<2010-arkus-deriving-finite-sphere-packings_images/imageFile4.png>)

(a) (b) Figure 2. The Neighbor Sphere.

(a) A particle and its neighbor sphere. 4 particles are shown touching the center particle, and it is seen that their centers lie on the surface of the particle’s neighbor sphere. (b) 2 touching particles. The associated neighbor spheres of the particles intersect in an intersection circle of radius (√3/2)R.

Now we can interpret each Aij = 1, in geometrical terms, as an intersection circle between spheres i and j. Minimal rigidity constraints imply that each particle is associated with at least

- 3 intersection circles. Intersection circles can be used to derive geometrical rules because, in general, a packing of n particles involves intersections of intersection circles, and intersections of


intersection circles deﬁne points in space. A particle touching m other particles will lie at the intersection of those m neighbor spheres. For example, a particle touching the dimer depicted in ﬁgure 2b will lie on the circumference of the associated intersection circle. The intersection of m ≥ 3 neighbor spheres are points – and by deﬁning points in space, basic trigonometry can be used to calculate the distances between those points, thus solving A’s for D’s.

3.2. Individual Geometrical Rules. Using intersection circles, we now derive several representative geometrical rules for eliminating and solving adjacency matrices. The supplementary information [8] contains the complete set of rules used to derive the results of this paper.

3.2.1. Rule 1. The simplest rule arises from the fact that intersection circles can intersect in either 2, 1 or 0 points, but never in more than 2 points. This geometrical fact implies that any A with the following property is unphysical: any 2 of the set {Ajk,Ajp,Akp} equal 1, and there exist more than 2 i’s for which Aij = Aik = Aip = 1.

Physically, this implies that no more than 2 spheres can simultaneously touch 3 connected spheres. Three spheres are connected if at least 2 contacts exist between them (Fig. 3). This in turn tells us how many identical spheres can mutually touch a trimer: 2. Figure 4 shows an example of an adjacency matrix that is unphysical for this reason: the blue highlighted section shows that spheres 4,5,6 make up a trimer; but the purple highlighted section shows that spheres 1,2,3 all touch the same trimer. This is impossible given the argument outlined above and hence this adjacency matrix does not correspond to a packing.

![image 5](<2010-arkus-deriving-finite-sphere-packings_images/imageFile5.png>)

Figure 3. No More than 2 Particles can Touch 3 Connected Particles. Schematic of 3 linearly connected particles and their associated intersection circles. The center of each intersection circle lies at the midpoint of the line segment connecting the associated points. There can never be more than 2 intersection points of these intersection circles, indicating that no more than 2 particles can touch the same 3 linearly connected particles.

- (a)

![image 6](<2010-arkus-deriving-finite-sphere-packings_images/imageFile6.png>)

![image 7](<2010-arkus-deriving-finite-sphere-packings_images/imageFile7.png>)

| |
|---|


(b)

![image 8](<2010-arkus-deriving-finite-sphere-packings_images/imageFile8.png>)

4 5

1

6

2, 3

![image 9](<2010-arkus-deriving-finite-sphere-packings_images/imageFile9.png>)

Figure 4. Example of an Unphysical Adjacency Matrix. (a) An adjacency matrix that is unphysical because it implies more than 2 intersections of intersection circles. The blue highlights show that particles 4,5,6 make up a trimer. The purple highlighted part shows that particles 1, 2, and 3 all touch the same trimer, 4,5,6.

- (b) A sphere packing corresponding to this unphysical adjacency matrix (shown in both sphere and point/line representations). For it to be realized, 2 particles must occupy the same point in space.


- 3.2.2. Rule 2. A trimer, a conﬁguration of 3 spheres forming an equilateral triangle, is associated with 3 mutually intersecting intersection circles (Fig. 5a). These 3 intersection circles intersect at


- 2 points (shown in red). Here we calculate the distance between these 2 intersection points. Note that a particle lying at one of the intersection points forms the 4-particle packing (the


tetrahedron). And that 2 particles, lying at each intersection point, form the 5-particle packing (the 5-point polytetrahedron). The distance between these 2 intersection points, h, is the only distance that is greater than R in the 5-particle packing (Fig. 6).

To calculate this distance, we note that the trimer and its associated intersection circles form the set of triangles shown in ﬁgure 5b (where the dashed line indicates an out-of-plane triangle). We calculate a by considering the right triangle with sides √3/2R − a,a,1/2R. Trigonometry then implies that a = R/(2√3), and h = 2 2/3R.

This implies that the solution to an adjacency matrix corresponding to the 5-particle packing is









- 0 1 1 1 1
- 1 0 1 1 1


- 0 1 1 1 1
- 1 0 1 1 1


- 1 1 0 1 1
- 1 1 1 0 2 23

- 1 1 1 2 23 0


−→

- 1 1 0 1 1
- 1 1 1 0 0 1 1 1 0 0


 

 

 

 

where the right matrix is the corresponding distance matrix, D, and without loss of generality we have let R = 1. For n = 5, there is only 1 non-isomorphic minimally-rigid A.

We can formalize this construction as a distance rule, which can be used whenever a submatrix of some A has the same structure as the 5-particle packing. Such submatrices can be identiﬁed with the following pattern: Aij = Aik = Akj = 1, and there exist 2 points p for which Api = Apj = Apk = 1. Whenever this pattern exists, the distance submatrix between the associated

√

3/2 R

h

1/2

![image 10](<2010-arkus-deriving-finite-sphere-packings_images/imageFile10.png>)

###### 3/2R-a

###### R

1/2 R

√3/2R-a

###### √

###### a a

R

1/2R

1/2 R

1/2R

R

(a) (b)

Figure 5. The Intersections of 3 Intersection Circles.

(a) A trimer and its corresponding intersection circles. The 3 intersection circles mutually intersect at 2 points, shown in red. (b) The triangles that relate the trimer to one of the points of intersection (red dot). The distance between this point and the center of the triangle is equivalent to half the distance between the 2 points of intersection (here denoted as h).

points corresponds to D for the 5-particle packing. In particular, this rule solves for the distance between the 2 points p, for example if p = l,m, then Dlm = 2 23R.

- 3.2.3. Rule 3. Another elimination rule follows directly from any distance rule, including Rule 2 derived above. Suppose we determine that for a given pattern of Aij, the contact distribution implies that Dkp > R. If it then happens that Akp = 1, then this implies that all of the geometrical constraints cannot be satisﬁed simultaneously, so that A is unphysical.

For example, if an A contained the intersection circle construction discussed in the previous section, that would imply that Dlm = 2 2/3R, but if the adjacency matrix also stated that Alm = 1, then that A would be unphysical.

- 3.2.4. Rule 4. We can derive another set of geometrical rules by ﬁnding the maximum number of points that can lie on an intersection circle – this corresponds to the maximum number of spheres that can touch a dimer. Figure 7 shows the dimer (top and bottom spheres), as well as points lying on their intersection circle.


The maximum number of spheres that can lie on an intersection circle is 5, and this can be calculated as follows: we divide the circumference of the entire intersection circle by the arc length swept out by 2 spheres lying a unit distance apart11 (see ﬁgure 7). This arc length is given by S = rθ, where r is the radius of the intersection circle, and θ is the angle between 2 radial line

11Without loss of generality, we refer to the distance between two touching spheres, R, as the unit distance.

![image 11](<2010-arkus-deriving-finite-sphere-packings_images/imageFile11.png>)

![image 12](<2010-arkus-deriving-finite-sphere-packings_images/imageFile12.png>)

h

Figure 6. The 2 Intersection Points of a Trimer Correspond to the 5Particle Packing. A 5-particle packing is shown with its point representation overlain. The center triangle of the point representation corresponds to a trimer, and the 2 points that contact the trimer correspond to the 2 intersection points of the trimer’s 3 intersection circles. The 2 intersection points are shown in red, and h corresponds to the distance between them.

segments. The law of cosines then implies that θ = cos−1

1 3

- (3) ,

so that the number of points a distance R apart that can ﬁt on an intersection circle is given by 2π

√3

2 R

√3

2 R cos−1 1

3

- (4) ≈ 5.1043.


This indicates that (i) any A implying that more than 5 points lie on an intersection circle, and (ii) any A implying a unit distance between all m ≤ 5 points lying on an intersection circle is unphysical. We can identify 5 points lying on an intersection circle by the following adjacency matrix pattern: Aij = 1, such that there are 5 points k for which Aik = Ajk = 1.

To solve for the structure of m ≤ 5 points lying on an intersection circle, we must compute the distances between the non-touching particles on the intersection circle (Fig. 7). Of these

![image 13](<2010-arkus-deriving-finite-sphere-packings_images/imageFile13.png>)

### 3

### 2 4

### θ

### S R

3/2R

√

### 1 5

###### Figure 7. 5 Points on an Intersection Circle.

The intersection circle shown in black corresponds to the dimer in the center. 5 points are shown lying on the intersection circle; this corresponds to 5 particles touching the center dimer. The radius of the intersection circle is (√3/2)R (shown as dashed black lines), and connects the center of the dimer (which is the origin of the intersection circle) to points 1–5 on the intersection circle. The arc length swept out by one pair of particles on the intersection circle is S. It can be seen that the 1st and 5th particles nearly touch. The space between them is not big enough to ﬁt another particle, and thus it can be seen that no more than 5 particles can touch a dimer.

distances, we have already calculated that between points 1 and 3 and shown that it is = 2 2/3R (section 3.2.2). All of these distances can be obtained by the isosceles triangle with equivalent lengths √3/2R (corresponding to the dashed black lines in ﬁgure 7 – note that only 2 such lines are shown, but that they exist between the midpoint of the dimer and every point along the intersection circle). The unique length of the isosceles triangle will be the unknown distance, rij, and the angle between the two √3/2R sides connecting particles i and j will be called φij. Thus, the unknown distances will all be given by

- 1

- 2rij


- 1

- 2


φij =

- (5) where

- φ13 = 2θ
- φ14 = 2π − 3θ
- φ15 = 2π − 4θ


where θ is given by equation 3, thus yielding

r13 = 2

- 2

- 3


- (6) R

r14 =

5 3

- (7) R

r15 =

4√6 9

- (8) R


sin

√3

2 R

These calculations apply to any adjacency matrix in which Aij = 1, there exist n points, k, for which Aik = Ajk = 1, and there also exist n − 1 instances where Apq = 1 amongst the n points, k; where n = 3,4,5 for r13,r14,r15, respectively. Then the distance between the two endpoints of the n particles is given by Dpk = r13,r14,r15, respectively. That is for

- n = 2: if k = p,q,l, then Apq = Aql = 1, and the distance Dpl = 2 23R.

- n = 3: if k = p,q,l,m, then Apq = Aql = Alm = 1, and the distance Dpm = 53R.

- n = 4: if k = p,q,l,m,z, then Apq = Aql = Alm = Amz = 1, and Dpz = 4


√6

9 R.

Note for n = 3, we have already identiﬁed this A pattern in section 3.2.2, whereas the n = 2,4 structures are new. Also note that, by symmetry, r13 = r24 = r35, and r14 = r25, and that these equivalences are identiﬁed by the above patterns in A.

- 3.3. Using Geometrical Rules to Derive a Complete Set of Sphere Packings. The aforementioned geometrical rules can be used, along with the set of nonisomorphic adjacency matrices, to derive a complete set of packings for a given n. To explain more clearly how this is done, we show as an example the derivation for n = 7 particle packings. For this n, there exist 29 minimally-rigid A’s, all of which potentially correspond to packings (table 1).


To these matrices, we apply the elimination rules just outlined, as well as those that appear in the supplementary information [8]. This immediately eliminates 24/29 A’s as unphysical. Figure 8 shows which of the matrices are eliminated. Table 2 shows which rules are used to eliminate the A’s. 17/24 of the matrices are eliminated because they imply more than 2 intersections of intersection circles. Three of the matrices are eliminated because of the relative distance rule for

n = 7 Adjacency Matrices with 3n − 6 Contacts and in Between 3 and 12 Contacts per Particle

141 NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER

X X X X X X X

1

1

1

1

1

0

0 0 0 0 1 1 1

- 0 0 0 0 1 1 1

- 0 0 0 0 1 1 1

- 0 0 0 0 1 1 1
- 1 1 1 1 0 1 1


- 1 1 1 1 1 0 1


- 1 1 1 1 1 1 0


C

C A

C

C

B @

C

- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 0 1 1


- 1 1 1 0 0 0 1


- 1 1 1 1 0 0 1


- 1 1 1 1 1 1 0




- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 0 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 0 1 1


- 1 0 1 0 0 1 1


- 1 1 1 1 1 0 1


- 1 1 1 1 1 1 0




- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 0 1 1 1

- 0 0 0 0 1 1 1
- 1 0 0 0 0 1 1


- 1 1 1 0 0 1 1


- 1 1 1 1 1 0 1


- 1 1 1 1 1 1 0




- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 0 1 1 1

- 0 0 0 0 1 1 1
- 1 0 0 0 1 1 1


- 1 1 1 1 0 0 1


- 1 1 1 1 0 0 1


- 1 1 1 1 1 1 0




X X X X X X

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 0 0 1


- 1 1 1 0 0 1 1


- 1 1 1 0 1 0 1


- 1 1 1 1 1 1 0


1

1

1

1

1

C

C

C

C

C A

- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 0 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 1 1 1


- 1 0 1 1 0 0 1


- 1 1 1 1 0 0 1


- 1 1 1 1 1 1 0




- A

- 0

B @

- 0 0 0 1 1 0 1

- 0 0 0 1 0 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 1 1 1


- 1 0 1 1 0 1 1


- 0 1 1 1 1 0 1


- 1 1 1 1 1 1 0




- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 1 1 1


- 1 1 1 1 0 0 1


- 1 1 1 1 0 0 0


- 1 1 1 1 1 0 0




- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 1 1 0


- 1 1 1 1 0 0 1


- 1 1 1 1 0 0 1


- 1 1 1 0 1 1 0




X X

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 0

- 0 0 0 0 1 1 1
- 1 1 0 0 1 1 1


- 1 1 1 1 0 0 1


- 1 1 1 1 0 0 1


- 1 0 1 1 1 1 0


1

1

1

1

1

C

C

C

C

C A

- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1
- 1 1 1 0 0 0 1


- 1 1 1 0 0 0 1


- 1 1 1 0 0 0 1


- 1 1 1 1 1 1 0




- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1
- 1 1 1 0 0 1 1


- 1 1 1 0 0 0 1


- 1 1 1 1 0 0 0


- 1 1 1 1 1 0 0




- A

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1

- 0 0 0 1 1 1 1
- 1 1 1 0 0 1 1


- 1 1 1 0 0 0 0


- 1 1 1 1 0 0 1


- 1 1 1 1 0 1 0




- A

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 0 1 1
- 1 0 0 0 1 1 1


- 0 1 0 0 0 1 1


- 1 0 1 0 0 1 1




- 1 1 1 1 1 0 1
- 1 1 1 1 1 1 0


X X

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 0 1 0 0 0 1 1


- 1 1 1 0 0 0 1


1

1

1

1

1

C

C

C

C

C A

- A

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 0 1 0 0 0 1 1


- 1 1 1 0 0 1 1




- A

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 0 1
- 1 0 0 0 1 1 1


- 0 1 0 0 0 1 1


- 1 1 1 0 0 1 1




- A

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 0 1 0 0 1 1 1


- 1 1 1 1 0 0 1




- A

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 0 1 0 0 1 1 0


- 1 1 1 1 0 0 1 1 1 1 1 0 0 1 1 1 1 0 1 1 0




- 1 1 1 1 0 0 1
- 1 1 1 1 1 1 0


- 1 1 0 1 1 0 1
- 1 1 1 1 1 1 0


- 1 0 1 1 1 0 1
- 1 1 1 1 1 1 0


- 1 1 1 1 0 0 0
- 1 1 1 1 1 0 0


X X X X

X X

- 0

B @

- 0 0 1 1 0 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 1


- 0 1 1 0 0 0 1
- 1 1 1 1 0 0 1


- 1 1 1 1 1 1 0


1

1

1

1

1

C

C

C

C

C A

- A

- 0

B @

- 0 0 1 1 0 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 1


- 0 1 1 0 0 1 1
- 1 1 1 1 1 0 0


- 1 1 1 1 1 0 0




- A

- 0

B @

- 0 0 1 1 1 0 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 1


- 1 1 1 0 0 0 1




- A

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 1


- 1 1 1 0 0 0 1




- A

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 0


- 1 1 1 0 0 0 1 1 1 1 1 0 0 1 1 1 1 0 1 1 0




- 0 1 1 1 0 0 1
- 1 1 1 1 1 1 0


- 1 1 1 1 0 0 0
- 1 1 1 1 1 0 0


X

1

1

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 1 1 0 0 0 1 1


- 1 1 1 0 0 1 1


1

1

C

C

C A

C

- A

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 0 1 1 1
- 1 0 0 1 1 1 1


- 1 0 1 0 0 1 0


- 1 1 1 0 0 0 1 1 1 1 1 0 0 1 1 1 1 0 1 1 0




- A

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 0 1 1 1
- 1 0 0 1 1 1 1


- 1 0 1 0 0 1 1


- 1 1 1 0 0 0 1




- A

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 0 1 1 1
- 1 0 0 1 1 1 1


- 1 0 1 0 0 1 1


- 1 1 1 0 0 0 0




- 1 1 1 1 0 0 1
- 1 1 1 1 0 1 0


- 1 1 0 1 1 0 0
- 1 1 1 1 1 0 0


- 1 1 1 1 0 0 0
- 1 1 1 1 1 0 0


Figure 8. Eliminating Adjacency Matrices. There are 29 non-isomorphic adjacency matrices satisfying minimal rigidity constraints for 7 particles. 24 out of the 29 A’s are eliminated by geometrical rules, which are shown here as color-coded X’s – see table 2 and appendix A [8] for the corresponding rules. See ﬁgure 9 for solutions to the 5 physically realizable A’s (which correspond to the matrices that appear here without an X).

three points on an intersection circle. Two matrices each are eliminated by rules acting on 5 rings and 4 rings, respectively. For the remaining ﬁve adjacency matrices, we apply distance rules to the A’s to solve for the corresponding D’s. Table 3 details which distance rules are used to solve for the packings corresponding to each A. The analytical solutions for the distance matrices as well as the associated packings are shown in ﬁgure 9; to each A (numbered by the order in which it appears in ﬁgure 8, in ascending order from left to right, and top to bottom, respectively), we apply the rules outlined in Table 3 to analytically solve for the packing.

This is the set of 7 particle sphere packings. Note that the packing corresponding to graph 17 (row 4 from the top) is the only one where distinct left and right handed structures are possible; thus it corresponds to 2 distinct states.

DERIVING FINITE SPHERE PACKINGS 15

Table 3. Rules Needed to Solve 7 Particle Packings.

The rules listed here correspond to distance rules. The rule number corresponds to the equation number in which the relevant distance was derived, either in the text or in appendix ??. (Note that rule 6 is the same as rules ?? and ??, rule 7 is the same as rule ??, and rule 8 is the same as rule ??). Graphs are numbered from left to right and top to bottom. These graphs correspond to the ones without X’s.

|Graph Number:<br><br>|Rules Used:|
|---|---|
|4|6, 7, and 8|
|8|6, and 7|
|17|6, 7, and ??|
|22|?? and ??|
|26<br><br>|?? and ??|


- 7 Particle Packings:

4 :

- 0

B @

- 0 0 0 1 1 1 1

- 0 0 0 1 0 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 0 1 1


- 1 0 1 0 0 1 1


- 1 1 1 1 1 0 1


- 1 1 1 1 1 1 0


1

C A

−→

0

B @

0 2q

2 3 2q

- 2

- 3 1 1 1 1


2 23 0 4

√6

9 1 53 1 1 2q

- 2

- 3 4


√6

9 0 53 1 1 1 1 1 53 0 2q 1 53 1 2q

- 2

- 3 1 1


- 2

- 3 0 1 1


- 1 1 1 1 1 0 1
- 1 1 1 1 1 1 0


1

C A

![image 14](<2010-arkus-deriving-finite-sphere-packings_images/imageFile14.png>)

- 8 :


DERIVING FINITE SPHERE PACKINGS 15

- 16 NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER
- 17 :


![image 15](<2010-arkus-deriving-finite-sphere-packings_images/imageFile15.png>)

- 16 NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER
- 17 :


![image 16](<2010-arkus-deriving-finite-sphere-packings_images/imageFile16.png>)

![image 17](<2010-arkus-deriving-finite-sphere-packings_images/imageFile17.png>)

- 0 2q 2q

- 2

- 3 1 53 1 1 1


- 2

- 3 0 53 1 1 1 1


- 1 53 0 13q


0

1

- 0 53 53 1 1 2q 5 3 0 53 1 2q 5 3

- 2

- 3 1


- 2

- 3 1 1


5 3 0 2q

- 2

- 3 1 1 1


- 1 1 2q 1 2q
- 2

- 3 0 1 1 1


0

1

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 0 1 0 0 0 1 1


- 1 1 1 0 0 1 1


1

- 0 2q 2q

- 2

- 3 1 53 1 1 1


- 2

- 3 0 53 1 1 1 1


- 1 53 0 13q


0

1

- 0

B @

- 0 0 0 1 1 0 1

- 0 0 0 1 0 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 1 1 1


- 1 0 1 1 0 1 1


- 0 1 1 1 1 0 1


- 1 1 1 1 1 1 0


1

3 1 2q

107

- 2

- 3 1


- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 0 1 0 0 0 1 1


- 1 1 1 0 0 1 1


1

3 0 2q 1 1 1 2q 1 1 2q 1 1 1 1 1 1 0

5 3 1 13q

−→

107

- 2

- 3 1 1


3 1 2q

−→

107

- 2

- 3 1


C A

- 2

- 3 0 1 1


3 0 2q 1 1 1 2q 1 1 2q 1 1 1 1 1 1 0

5 3 1 13q

- 1 1 0 1 1 0 1
- 1 1 1 1 1 1 0


C A

- 16 NATALIE ARKUS, N. MA AND P.
- 17 :


−→

107

- 2

- 3 1 1


B @

C A

- 2

- 3 1 1 0 1 1


- 16 NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER
- 17 :


- 2

- 3 1 1 0 1


2q 1 1 1 1 1 1 0

C A

B @

C A

- 2

- 3 0 1 1


- 2

- 3 1 1 1 1 0 1


![image 18](<2010-arkus-deriving-finite-sphere-packings_images/imageFile18.png>)

- 1 1 0 1 1 0 1
- 1 1 1 1 1 1 0


![image 19](<2010-arkus-deriving-finite-sphere-packings_images/imageFile19.png>)

B @

C A

- 2

- 3 1 1 0 1


2 1 1 q

0 q

0

1

3+√5

3+√5

2 1 1

- 0 2q 2q

- 2

- 3 1 53 1 1 1


- 2

- 3 0 53 1 1 1 1


- 1 53 0 13q


0

1

q

2 0 q

- 0 2q 2q

- 2

- 3 1 53 1 1 1


- 2

- 3 0 53 1 1 1 1


- 1 53 0 13q


0

1

- 0

B @

- 0 0 1 1 0 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 1


- 0 1 1 0 0 1 1
- 1 1 1 1 1 0 0


- 1 1 1 1 1 0 0


1

3+√5

3+√5

2 1 1 q

0 q

2 1 1 1 1 1 q

0

1

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 0 1 0 0 0 1 1


- 1 1 1 0 0 1 1


1

3+√5

3+√5

2 0 q

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 0 1 0 0 0 1 1


- 1 1 1 0 0 1 1


1

3+√5

3+√5

2 1 1

q

2 0 q

2 1 1 1 1 1 q

- 0

B @

- 0 0 1 1 0 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 1


- 0 1 1 0 0 1 1
- 1 1 1 1 1 0 0


- 1 1 1 1 1 0 0


1

3 1 2q

3+√5

3+√5

2 0 q

3 1 2q

3+√5

3+√5

2 1 1 1 1 1 q

107

- 2

- 3 1


−→

22 :

2 0 q

107

- 2

- 3 1


2 1 1

3 0 2q 1 1 1 2q 1 1 2q 1 1 1 1 1 1 0

5 3 1 13q

3+√5

3+√5

q

2 1 1 q

3 0 2q 1 1 1 2q 1 1 2q 1 1 1 1 1 1 0

5 3 1 13q

3+√5

3+√5

−→

2 1 1 1 1 1 q

C A

107

- 2

- 3 1 1


−→

2 0 q

107

- 2

- 3 1 1


2 0 1 1 1 1 1 1 1 0 q2 − √25 1 1 1 1 1 q2 − √25 0

3+√5

3+√5

C A

−→

22 :

2 1 1

C A

- 2

- 3 0 1 1


B @

C A

q

2 1 1 q

- 1 1 0 1 1 0 1
- 1 1 1 1 1 1 0


- 2

- 3 0 1 1


- 1 1 0 1 1 0 1
- 1 1 1 1 1 1 0


3+√5

3+√5

C A

B @

C A

2 0 1 1 1 1 1 1 1 0 q2 − √25 1 1 1 1 1 q2 − √25 0

B @

C A

- 2

- 3 1 1 0 1


- 2

- 3 1 1 0 1


B @

C A

![image 20](<2010-arkus-deriving-finite-sphere-packings_images/imageFile20.png>)

2 1 1 q

0 q

0

1

2 1 1 q

0 q

0

1

3+√5

3+√5

3+√5

3+√5

2 1 1

![image 21](<2010-arkus-deriving-finite-sphere-packings_images/imageFile21.png>)

2 1 1

q

2 0 q

- 0

B @

- 0 0 1 1 0 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 1


- 0 1 1 0 0 1 1
- 1 1 1 1 1 0 0


- 1 1 1 1 1 0 0


1

q

2 0 q

3+√5

3+√5

- 0

B @

- 0 0 1 1 0 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 1


- 0 1 1 0 0 1 1
- 1 1 1 1 1 0 0


- 1 1 1 1 1 0 0


1

3+√5

3+√5

2 1 1 1 1 1 q

2 1 1 1 1 1 q

2 0 q

2 0 q

3+√5

3+√5

3+√5

3+√5

2 1 1 1 1 1 q

2 1 1 1 1 1 q

2 0 q

2 0 q

3+√5

3+√5

3+√5

3+√5

−→

22 :

2 1 1

−→

22 :

2 1 1

q

2 1 1 q

q

2 1 1 q

3+√5

3+√5

C A

3+√5

3+√5

C A

2 0 1 1 1 1 1 1 1 0 q2 − √25 1 1 1 1 1 q2 − √25 0

2 0 1 1 1 1 1 1 1 0 q2 − √25 1 1 1 1 1 q2 − √25 0

![image 22](<2010-arkus-deriving-finite-sphere-packings_images/imageFile22.png>)

B @

C A

B @

C A

![image 23](<2010-arkus-deriving-finite-sphere-packings_images/imageFile23.png>)

![image 24](<2010-arkus-deriving-finite-sphere-packings_images/imageFile24.png>)

![image 25](<2010-arkus-deriving-finite-sphere-packings_images/imageFile25.png>)

√02 √02 √13 11 11 11 11 1 √3 0 √3 1 √3 1

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 1 1 0 0 0 1 1


- 1 1 1 0 0 1 1


1

0

1

√02 √02 √13 11 11 11 11 1 √3 0 √3 1 √3 1

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 1 1 0 0 0 1 1


- 1 1 1 0 0 1 1


1

0

1

- 1 1 √3 0 √2 1 1 1 1 1 √2 0 1 1

- 1 1 √3 1 1 0 √2 1 1 1 1 1 √2 0


−→

26 :

C A

B @

C A

- 1 1 √3 0 √2 1 1 1 1 1 √2 0 1 1

- 1 1 √3 1 1 0 √2 1 1 1 1 1 √2 0


- 1 1 0 1 1 0 0
- 1 1 1 1 1 0 0


−→

26 :

C A

B @

C A

![image 26](<2010-arkus-deriving-finite-sphere-packings_images/imageFile26.png>)

- 1 1 0 1 1 0 0
- 1 1 1 1 1 0 0


![image 27](<2010-arkus-deriving-finite-sphere-packings_images/imageFile27.png>)

3.4. Enantiomers and Chirality. Once all packings have been derived by solving all A’s for their corresponding D’s, we must determine how many states each packing has. If a packing is chiral, it will have more than one state. This will show up by a packing having diﬀerent ‘handedness;’ for example, a packing with a mirror image that is non-superimposable will have distinct left and right-handed structures, and thus have 2 distinct states. We will proceed with the following deﬁnitions: an enantiomer corresponds to a structure that has a non-superimposable mirror image (i.e. a non-superimposable reﬂection across the x,y, or z plane); a chiral structure

- 3.4. Enantiomers and Chirality. Once all packings have been derived by solving all A’s for their corresponding D’s, we must determine how many states each packing has. If a packing is chiral, it will have more than one state. This will show up by a packing having diﬀerent ‘handedness;’ for example, a packing with a mirror image that is non-superimposable will have distinct left and right-handed structures, and thus have 2 distinct states. We will proceed with the following deﬁnitions: an enantiomer corresponds to a structure that has a non-superimposable mirror image (i.e. a non-superimposable reﬂection across the x,y, or z plane); a chiral structure


###### Figure 9. 7-Particle Packings.

√02 √02 √13 11 11 11 11 1 √3 0 √3 1 √3 1

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 1 1 0 0 0 1 1


- 1 1 1 0 0 1 1


1

0

1

√02 √02 √13 11 11 11 11 1 √3 0 √3 1 √3 1

- 0

B @

- 0 0 1 1 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 1 1 0 0 0 1 1


- 1 1 1 0 0 1 1


1

0

1

###### These are the 5 possible packings of 7 particles. Graph numbers appear to the left – corresponding to a sequential numbering of the graphs appearing in ﬁgure 8 from left to right and top to bottom, respectively. Following the graph numbers are A, D, and a picture of the corresponding packing, respectively. Note that graph 17 is chiral – it has both a left-handed and a right-handed form (this can be seen by moving the top particle, currently shown on the left side, over to the right side).

- 1 1 √3 0 √2 1 1 1 1 1 √2 0 1 1

- 1 1 √3 1 1 0 √2 1 1 1 1 1 √2 0


- 1 1 √3 0 √2 1 1 1 1 1 √2 0 1 1

- 1 1 √3 1 1 0 √2 1 1 1 1 1 √2 0


−→

26 :

−→

26 :

C A

B @

C A

C A

B @

C A

- 1 1 0 1 1 0 0
- 1 1 1 1 1 0 0


- 1 1 0 1 1 0 0
- 1 1 1 1 1 0 0


- 3.4. tiomers and Chirality. Once all packings have been derived by solving all A’s for their corresp D’s, we must how many states each packing has. If a packing is chiral, it will have more than one state. This will show up by a packing having diﬀerent


- 3.4. Enantiomers and Chirality. Once all packings have been derived by solving all A’s for their corresponding D’s, we must determine how many states each packing has. If a packing is chiral, it will have more than one state. This will show up by a packing having diﬀerent ‘handedness;’ for example, a packing with a mirror image that is non-superimposable will have distinct left and right-handed structures, and thus have 2 distinct states. We will proceed with the following deﬁnitions: an enantiomer corresponds to a structure that has a non-superimposable mirror image (i.e. a non-superimposable reﬂection across the x,y, or z plane); a chiral structure


e for example, a packing with a mirror image that is non-superimposable will have left and right-handed ures, and thus have 2 distinct states. We will proceed with the following ns: an enantiomer corresponds to a st that has a erimposable

r image (i.e. a non-superimposable n the x,y, or z ; a chiral

- Table 2. Elimination Rules Used for 7-Particle Packings. Each rule appears in its own section either in the text or in appendix A [8], where the complete set of rules is included. The rule column thus lists in what section(s) the relevant rules can be found.

|Color:<br><br>|Unphysical Because:<br><br>|Rule:|
|---|---|---|
|X<br><br>|2 or more intersection circles intersect at more than 2 points|A.1 section 3.2.1<br><br>|
|X<br><br>|All relative distances between 3 points lying on an intersection circle = R|A.3<br><br>sections 3.2.2, 3.2.3 and 3.2.4<br><br>|
|X<br><br>|A closed 5 ring surrounds a circle of intersection<br><br>|A.14|
|X|2 points on opposite sides of a closed 4 ring touch<br><br>|A.15|


- Table 3. Rules Needed to Solve 7-Particle Packings. The rules listed here correspond to distance rules. Rule ‘A.#’ corresponds to rule # in appendix A [8], otherwise the relevant equation and section numbers are listed for rules found within the paper. (Note that rule 4, found in section 3.2.4 (eqn 6), is the same as rules 2 (section 3.2.2) and A.1, rule 4 (eqn 7) is the same as rule A.2, and rule 4 (eqn 8) is the same as rule A.4). Graphs are numbered in ascending order from left to right and top to bottom as they appear in ﬁgure 8. These graphs correspond to the ones without X’s.


|Graph Number:<br><br>|Rules Used:|
|---|---|
|4<br><br>|section 3.2.4 eqns 6, 7, and 8|
|8|section 3.2.4 eqns 6 and 7|
|17<br><br>|section 3.2.4 eqns 6, 7; and A.11|
|22<br><br>|A.7 and A.6|
|26|A.3 and A.9|


3.4. Non-Uniqueness of Geometrical Rules. Note that the geometrical rules described here are not unique in that (i) the rules themselves can be derived in diﬀerent ways, and (ii) a diﬀerent set of rules altogether could be derived/applied to solve for the same packings. This is simply one set of rules that works. One example of this is that either Rule 2 or Rule 4, equation 6 can be used to determine the unknown distance in a 5-particle packing. Another example of this is that all iterative packings can be solved using the triangular bipyramid rule that will be introduced in section 4 instead of using the aforementioned rules. There are undoubtedly many such examples, and the list of rules just presented were not derived with the goal of conciseness. They are complete in the sense that they allow one to solve all adjacency matrices for the n presented here. Beyond this however, they can only solve adjacency matrices containing the structure the rule identiﬁes. If an A contains an identiﬁable structure as well as a non-identiﬁable (not previously encountered) structure, then the rules will solve the identiﬁable part and only partially solve that A for its corresponding D. If an A contains no identiﬁable structure, then new rules must be derived to solve any part of it. It is because of these latter two cases that we continued to derive new geometrical rules as we increased in n. The triangular bipyramid rule in section 4 is a rule that we derived in order to have one general rule that could recognize a certain class of adjacency

matrix structures – the iterative class – for all n. Because it is a general rule, applicable to all n, its introduction makes the set of rules much more concise.

- 3.5. Chirality. Once all packings have been derived by solving all A’s for their corresponding D’s, we must determine how many states each packing has. If a packing is chiral, it will have more than one state. This will show up by a packing having a non-superimposable mirror image; for example a packing having diﬀerent ‘handedness,’ such as distinct left and right-handed structures.


One can calculate whether a packing is chiral as follows: The automorphism group of a packing, {α}, gives the set of self-isomorphisms – i.e. all possible permutations of the structure into itself. Each element of the automorphism group will thus correspond either to a rotation or to a reﬂection. Rotations are transformations with determinant = 1, and reﬂections are transformations with determinant = −1. Thus, one can construct the set of all isomorphic graphs, {D}, and construct the automorphism group for any one Di within the isomorphic set. If ∃ any matrix Dj ∈ {D} that is isomorphic to Di only through reﬂections and not through rotations – i.e. if the isomorphism group of Dj to Di corresponds to transformations that all have determinant -1, then the packing D is chiral.

A property related to chirality is the symmetry number, σ. This corresponds to the number of ways that a structure can be rotated into itself. The symmetry number is necessary for calculating the equilibrium probability distribution of packings [5, 43]. The symmetry number of a packing, D, will be equal to the number of transformations within the automorphism group of D that have determinant 1. Thus, if a packing has no reﬂections, then the symmetry number will simply equal the size of the automorphism group. If a packing has reﬂections, then the symmetry number will equal the size of the automorphism group divided by 2 (dividing by 2 will remove all automorphism mappings corresponding to reﬂections, and not rotations).

Related to both symmetry numbers and chirality are point groups. A point group is a group of symmetry operations which all leave at least one point unmoved. Point groups have been calculated for many structures – and there exist programs that allow one to enter in a set of coordinates and retrieve the point group corresponding to those coordinates [46]. Symmetry numbers and chirality can alternatively be calculated directly from the point group of a structure. For example, compounds in the Cm point group, where Cm is the cyclic group consisting of rotations by 360◦/m and all integer multiples (where m is an integer), are always chiral [25].

Point groups, symmetry numbers, and chirality of packings are included in the lists of packings appearing in section 5 and in the supplementary information [8]. The growth of chiral structures with n is interesting – surprisingly, over half of all 9-particle packings are chiral – see table 4.

4. One Geometrical Rule That Solves for all Iterative Packings: The Triangular Bipyramid Rule

In principle, these types of geometrical rules can be used to derive a complete set of sphere packings for any number of particles, n. However, in practice, the number of rules used here grows too quickly with n for this to be a practical method: at n = 5 spheres, only 1 rule is required, 3 rules are needed at n = 6, 12 rules at n = 7, and at n = 8, 14 rules solve 435/438 minimally-rigid non-isomorphic A’s. This leaves 3 unsolved A’s for which more geometrical rules must be derived; looking ahead at the 13,828 and 750,352 A’s that must be solved at n = 9,10, respectively, it becomes clear that deriving a rule or set of rules that does not grow signiﬁcantly with n is a necessary step. Here, we derive one geometrical rule that can solve one class of packings for any n, thereby greatly reducing the number of rules needed to derive a complete set of n sphere

![image 28](<2010-arkus-deriving-finite-sphere-packings_images/imageFile28.png>)

![image 29](<2010-arkus-deriving-finite-sphere-packings_images/imageFile29.png>)

(a) (b)

Figure 10. Iterative Packings. Two examples of iterative packings. (a) A 6 particle polytetrahedron (red) with one particle added to it (blue). This decomposes into a tetrahedron (blue) plus a 6 particle polytetrahedron (red), with a shared triangular base (purple). (b) 2 joined octahedra (one red and one blue, with a shared purple triangular base) forming a 9-particle packing.

packings. In section 7.2, we discuss how one geometrical rule can also be used to solve the other class of packings for all n.

Packings can be broken up into two types or classes: iterative and non-iterative, or new seeds. Iterative packings are n-particle packings that are solely combinations of packings of less than n particles (see Fig. 10). New seeds are n-particle packings that cannot be constructed solely out of packings of less than n particles – i.e. they contain within them (in part or in whole) an inherently new structure (Fig. 11). Put another way, iterative packings correspond to A’s for which all minimally-rigid m x m subgraphs, m < n, correspond to packings that have been identiﬁed at lower n.

![image 30](<2010-arkus-deriving-finite-sphere-packings_images/imageFile30.png>)

![image 31](<2010-arkus-deriving-finite-sphere-packings_images/imageFile31.png>)

![image 32](<2010-arkus-deriving-finite-sphere-packings_images/imageFile32.png>)

![image 33](<2010-arkus-deriving-finite-sphere-packings_images/imageFile33.png>)

![image 34](<2010-arkus-deriving-finite-sphere-packings_images/imageFile34.png>)

Continuous degrees of freedom

(a)

(b)

Figure 11. New Seeds. The octahedron is an example of a new seed. (a) The ‘base’ of an octahedron has a continuous degree of freedom through which a 5 particle polytetrahedron can form, and thus is not a packing. The continuous degrees of freedom are shown as dashed lines; bringing either of the pairs of particles connected by these dashed lines into contact forms the 5 particle polytetrahedron. (Note that the 5 particle structure shown in (a) is not minimally-rigid as it has fewer than 3n−6 = 9 contacts.) (b) Once a 6th particle is added, the octahedral structure can be stabilized, thereby forming a new seed. This ‘new seed’ is an inherently new structure.

4.1. Solving iterative structures. An iterative packing is a polyhedron containing solely packings of less than n particles12. Thus any iterative packing can be decomposed into 2 joined polyhedra (see Fig. 10 – the red and blue packings are the joined polyhedra). The 2 polyhedra are joined via a common base of particles (shown in purple)13. Because the joined polyhedra are less than n-particle packings, all of their intrapolyhedral distances are known from lower-order packings.

Thus, deriving one geometrical rule that can solve for all iterative packings requires solving the following geometrical problem: Given 2 joined polyhedra, where all intrapolyhedral distances are known, derive a general formula for the interpolyhedral distances. Note that the solution to this problem immediately extends to unphysical iterative structures as well, as they are composed of structures of less than n particles, where either (i) one or more of the joined structures is unphysical, or (ii) the particular combination of the structures is unphysical.

The geometrical problem is solved with the following observation: An explicit analytical formula for the distance between any 2 points can be derived if those 2 points can be related to a common triangular base. Let there exist two particles i,j whose interparticle distance, rij, is unknown. If there also exist 3 particles, k,p,q, with known interparticle distances (rkp, rkq, rpq), and if the distances between i, j and the 3 particle base (rip,rik,riq,rjp,rjk,rjq) are also known; then there exists an analytical relationship for the resulting rij. We call this the triangular bipyramid rule because the 5 points i,j,k,p,q together form a (potentially irregular) ditetrahedron or triangular bipyramid (see ﬁgure 19). We show the rule here, while a complete derivation can be found in the supplemental information (Appendix A [8]).

The dihedral angles A2 and A3 of ﬁgure 19 are given by: A3 = cos−1

cosa3 − cosb3 cosc3 sinc3 sinb3 A2 = cos−1

cosa2 − cosb2 cosc2 sinc2 sinb2 These formulas are essentially obtained using the spherical rule of cosines - see Appendix A for details [8].

The dihedral angle A1 will be either the sum or the diﬀerence of the dihedral angles A2 and A3 (see Fig. 19), depending on whether the points i,j lie on the same or on opposite sides of the base p,k,q. If i,j lie on the same side, then A1 = |A2 − A3|, and if i,j lie on opposite sides then A1 = A2 + A3.

The angle a1 is then given by

- (9) a1 = cos−1(sinc1 sinb1 cosA1 + cosb1 cosc1) and from the law of cosines, we can then calculate rij:
- (10) rij = rip2 + rpj2 − 2riprpj cosa1


Associated with each rij we have 2 possible A1, and thus 2 possible solutions (similar, in principle, to one having 2 possible solutions to a quadratic equation).

- 12An iterative A is an n × n graph composed solely of m × m (m < n) subgraphs, each of which correspond to minimally-rigid A’s of less than n spheres.
- 13Given the minimal rigidity constraints we have imposed, this common base will always consist of at least 3 particles.


![image 35](<2010-arkus-deriving-finite-sphere-packings_images/imageFile35.png>)

###### Figure 12. The Triangular Bipyramid.

The triangular bipyramid (or ditetrahedron) constructed in the triangular bipyramid rule. The center triangle (kpq), shown in red, corresponds to the common 3 particle base. Particles i and j are related to one another through the common base. The distance between i and j, rij, shown as the dash-dot blue line, is unknown. a1 corresponds to ∠jpi. A1 is the dihedral angle between ipk and jpk, A2 is the dihedral angle between ipk and kpq, and A3 is the dihedral angle between kpq and jpk. Points i and j can either both lie on the same side of the base kpq or each lie on opposite sides of the base (indicated by the dashed lines, that can either go into or come out of the plane). If i,j lie on the same side, then A1 is equal to the diﬀerence of A2 and A3, and if i,j lie on opposite sides of the base then A1 is equal to the sum of A2 and A3. When all distances other than rij are known, then an explicit analytical formula can be derived to solve rij.

- 4.2. Applying the triangular bipyramid rule. The triangular bipyramid rule can be used to solve all iterative packings as follows. We ﬁrst search for subgraphs of A corresponding to lower-n seeds. The elements of D corresponding to these lower-order structures are known and inserted appropriately. If A is iterative, all minimally-rigid subgraphs of m < n particles (i.e. m subgraphs with at least 3m − 6 contacts and at least 3 contacts per particle) will correspond to m-particle


packings. Once all lower-order seeds are inserted as appropriate, all unknown rij correspond to the distances between the spheres of diﬀerent known lower-order subpackings. The triangular bipyramid rule is then applied to each unknown element14 of D. For each unknown distance, rij, both solutions are potentially stored, as are all possible sets of unknown distances {rij}. Along

14If A is not iterative, there will exist unknown rij that do not correspond to distances between spheres of known subpackings. In this case, equation 32 will contain at least 1 unknown element on the right hand side and can not be applied directly.

the way, each rij solution is tested for consistency, and it is always possible that both, 1, or neither solution will be consistent. Once all locally consistent rij are stored, the resultant {rij} are tested for global consistency.

A solution will be inconsistent, and thus unphysical, for one of the following reasons:

- 1. It violates the triangle inequality (meaning that no real solution exists – this shows up as the absolute value of the argument of the inverse cosine being greater than 1).
- 2. One or more distance(s) are less than R.
- 3. Diﬀerent triangular bases lead to diﬀerent rij; this indicates that a structure is in conﬂict with itself. One part of it implies it should have one structure, whereas another part implies a diﬀerent structure. Such a structure is physically and mathematically inconsistent.


- Violation 2 arises within the 5 particles of one triangular bipyramid, and thus registers a physical

local inconsistency. Violation 1 occurs within individual triangular bipyramids, as each rij is determined, in which case it registers a local inconsistency; as well as over the entire set of triangular bipyramids, once all {rij} have been determined, in which case it registers a global inconsistency15.

- Violation 3 occurs when solutions are consistent within individual triangular bipyramids, and thus locally consistent, but inconsistent within combinations of triangular bipyramids – these solutions are thus globally inconsistent. This violation can be checked as follows: Figure 19 shows that the


dihedral angle, A1, is given by either the sum or the diﬀerence of A2 and A3, if particles i and j lie on opposite sides or on the same side of the triangular base, respectively (to within a 2π modulation of course). Test all possible 5 particle combinations of triangular bipyramids within the n particle structure, and if there exists a triangular bipyramid that does not satisfy

A2 + A3 |A2 − A3| 2π − (A2 + A3) 2π − |A2 − A3|

(11)

A1 =

the solution is globally inconsistent. (In calculating rij in equation 32, we need not consider the latter two A1 solutions, as cos(2π − x) = cos(x)).

There is one scenario in which 5 points need not satisfy this global consistency check, and that is when 3 or more of the 5 points lie in a line. In this case, the 3 or more points deﬁne a line and not a plane, and thus the dihedral angle is not deﬁned, and equation 11 can not be applied. This situation is encountered in certain structures that contain octahedra (for example, see graphs 5416 and 10664 at n = 9 in the supplementary information [8]). In this scenario, the following global check can be performed: for m points lying in a line, there must exist the following number of

15In this case, some triangular bipyramids are locally consistent, whereas others are not. All possible triangular bipyramids of a structure need not be tested to solve for all rij, thus it is important to check all bipyramids to ensure global consistency once {rij} have been determined. This violation is related to violation 3, except that here the violation is registered between the angles associated with the line segments, and in violation 3 the violation occurs within the dihedral angles.

line segments with a given minimum distance: Number of Line Segments Minimum Length of Line Segment

- m − 1 R
- m − 2 2R


. . . . . .

(12)

m − (m − 1) (m − 1)R

Note that the ﬁrst constraint, having m − 1 line segments with a minimum length of R, is automatically satisﬁed by the fact that we eliminate all solutions containing a distance < R. Up to n = 10, it turns out that performing this check for m = 3 alone is suﬃcient to ﬁnd all globally inconsistent solutions. We evaluate that 3 points lie in a line by identifying that the angle associated with those 3 points is 0 or π. We then check that there is at least one distance amongst the 3 points that is ≥ 2 (where once again, R = 1 without loss of generality). If this is not satisﬁed, then the packing is globally inconsistent and is eliminated. Note that the fact that some dihedral angles may not be deﬁned was overlooked in [7], and is the primary source of the diﬀerence in numbers reported here in tables 1 and 4 versus the numbers previously reported in [7].

- 4.3. The Growth of New Seeds. For new seeds, we have a structure that contains an inherently new polyhedron, and thus some or all intrapolyhedral distances are also unknown, i.e. one or more of the 9 distances within {rip,rik,riq,rjp,rjk,rjq,rpk,rpq,rkq} are unknown. Thus, deriving the equation for rij, as is done for iterative packings, will yield one equation with more than one unknown. The triangular bipyramid rule, therefore, can not be applied directly to new seeds, and new geometrical rules must be derived to analytically solve non-iterative A’s.


Using a general rule to solve for iterative A’s, and deriving individual geometrical rules for non-iterative A’s is feasible so long as the non-iterative A’s do not grow too quickly with n. Table 1 shows that this is the case for n ≤ 9, where the number of non-iterative A’s is 5 or less. However, at n = 10, there are 94 non-iterative A’s16. To sift through the 94 potential seeds at n = 10 requires inventing new geometrical rules, and the growth of such rules demonstrates that the method we have described does not scale eﬃciently with n. In section 7.2, we will discuss a potential extension of the triangular bipyramid rule, which might be able to break this bottleneck, at least computationally. Here, we present the packing results derived from a combination of the triangular bipyramid rule and individual geometrical rules. For n ≤ 9, we have analytically solved for all packings. At n = 10, we analytically solve for all iterative packings, and produce a preliminary list of new seeds, found by solving the non-iterative A’s numerically using Newton Iterations17.

- 16Note that the non-iterative and iterative A’s listed in this table are constructed after applying the geometrical rules for n ≤ 8 that appear in the text and in the supplementary information [8]. Thus, this reﬂects the number of iterative and non-iterative A’s with respect to these geometrical rules, and not the absolute number of iterative and non-iterative A’s
- 17Our runs of Newton Iterations used random initial guesses (between -5 and 5 for the coordinates of the particles). We performed 20 iterations of each initial guess, and approximately 150,000 total runs. Every matrix for which a solution was found, was found multiple times. We believe this to be a reasonably thorough search and that this preliminary list of new seeds at n = 10 might be complete. It is worth noting that the preliminary list of new seeds reported here found by Newton Iterations is the same as the list reported in [7] found by constructing the non-iterative A’s manually with the construction toy Geomags.


5. The Set of Sphere Packings

Here we present the list of sphere packings derived by this method18. In principle, the analytical method outlined here will yield a complete set of minimally-rigid packings. However, we have not implemented the triangular bipyramid rule symbolically, leading to the following practical issues, which could lead to numerical errors:

Numerical round-oﬀ error: All calculations involving the triangular bipyramid rule are subject to numerical precision. Our algorithm eliminates many packings by ﬁnding situations where the argument of the cos−1 term is larger than unity; this can also occur erroneously due to round-oﬀ error, causing packings to erroneously be recognized as unphysical. Similarly, round-oﬀ errors are possible when checking for the consistency of a packing; in checking the equivalence between dihedral angles, or checking that there exists at least one distance greater than or equal to 2 when 3 points lie in a line. Round-oﬀ issues could be improved by using general precision libraries such

- as gmp and mpfr [1, 2], or altogether avoided by doing all calculations symbolically. Thus, while the analytical method presented here should in principle yield a complete set of sphere packings, practical issues such as these are a source of error.

We present a complete set of sphere packings of n ≤ 9, save round-oﬀ error. At n = 10, we present a complete set of iterative packings and a preliminary list of new seeds. Packings of n ≤ 7 particles are included here, and packings of n ≤ 8 ≤ 10 particles are included in supplementary information [8]. All results are summarized in table 4.

In the list presented here, φ corresponds to the point group, and σ to the symmetry number. We have included the 2nd moment of each packing, and a ‘*’ appears next to the 2nd moment that corresponds to the minimum of the 2nd moment of n particles. The ‘special properties’ column denotes whether a structure is convex, a new seed, chiral, or non-rigid. If the special properties column is blank, then that packing contains none of these properties.

18The number of packings presented here for n = 9,10 diﬀers from the number we reported in [7]. This is primarily because our previous code did not run a check to ensure that the dihedral angle was well deﬁned when checking for global consistency. As mentioned in section 4.2, this can occur when the 3 points used to deﬁne a plane are collinear, occurring in some of the packings that contain octahedra. In our original code (used for [7]), the dihedral angle check was still being performed in such an instance and erroneously deemed some packings globally inconsistent. It was a personal communication with Rob Hoy, who extended this work in [30], that brought it to our attention that 2 packings were missed in our n = 9 list. In examining this discrepancy, we discovered that this issue with the dihedral angles was what caused these packings to be missed, and we have since made the relevant correction in the code. This caused 52 packings to be realized at n = 9 and many more packings to be realized

- at n = 10. We also made 2 more modiﬁcations to the code, such as further correcting for numerical round-oﬀ error, which further caused several more packings to be registered at n = 10. Please see supplemental information, Appendix C [8] for a complete list of the changes that were made to the code.


26 NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER

- 2 Particle Packings Packing 1 (Graph 1):

A : „

- 0 1
- 1 0


«

D : „

0 1 1 0

« R

C :

0

B @

0 0 0 0 −1 0

1

C A

R

![image 36](<2010-arkus-deriving-finite-sphere-packings_images/imageFile36.png>)

![image 37](<2010-arkus-deriving-finite-sphere-packings_images/imageFile37.png>)

|2nd Moment|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|∗0.5R2|D∞h|2<br><br>|New Seed Convex|


- 3 Particle Packings Packing 1 (Graph 1):

A :

- 0 @

- 0 1 1
- 1 0 1


- 1 1 0


1 A

D :

- 0 @

- 0 1 1
- 1 0 1


- 1 1 0


1 A R

C :

0

B @

0 0 0 0 −1

√30/2 −1/2 0

1

C A

R

![image 38](<2010-arkus-deriving-finite-sphere-packings_images/imageFile38.png>)

![image 39](<2010-arkus-deriving-finite-sphere-packings_images/imageFile39.png>)

|2nd Moment|φ|σ|Special Properties|
|---|---|---|---|
|∗1.0R2|D3h|6|Convex|


- 4 Particle Packings Packing 1 (Graph 1):


26 NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER

2 Particle Packings Packing 1 (Graph 1):

3 Particle Packings Packing 1 (Graph 1):

0

1

A : „

«

0 0 0 0 −1 0

0 1 1 0

C :

R

D : „

« R

B @

C A

0 1 1 0





|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|∗0.5R2|D∞h|2<br><br>|New Seed Convex|


0 @

1 A

0 1 1 1 0 1 1 1 0

A :

0 @

1 A R

0 1 1 1 0 1 1 1 0

D :

1

0

0 0 0 0 −1

C :

R

√30/2 −1/2 0

C A

B @

![image 42](<2010-arkus-deriving-finite-sphere-packings_images/imageFile42.png>)

![image 43](<2010-arkus-deriving-finite-sphere-packings_images/imageFile43.png>)

26 NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER

|2nd Moment<br><br>|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|∗1.0R2|D3h<br><br>|6|Convex|


4 Particle Packings Packing 1 (Graph 1):

DERIVING FINITE SPHERE PACKINGS 27

DERIVING FINITE SPHERE PACKINGS 27

- 0

B @

0 0 0 0 −1

√30/2 −1/2 0

- 1/(2√3)


1

- 0

B @

0 0 0 0 −1

√30/2 −1/2 0

- 1/(2√3)


1

- 0

B @

- 0 1 1 1
- 1 0 1 1


- 1 1 0 1 1 1 1 0


1 C A

- 0

B @

- 0 1 1 1
- 1 0 1 1


- 1 1 0 1 1 1 1 0


1 C A

A :

A :

C :

R

1 C A R

0 B @

- 0 1 1 1
- 1 0 1 1 1 1 0 1 1 1 1 0


C :

R

1 C A R

- 0

B @

0 1 1 1 1 0 1 1

- 1 1 0 1 1 1 1 0


D :

C A

D :

p−12//23

C A

p−12//23

![image 44](<2010-arkus-deriving-finite-sphere-packings_images/imageFile44.png>)

![image 45](<2010-arkus-deriving-finite-sphere-packings_images/imageFile45.png>)

![image 46](<2010-arkus-deriving-finite-sphere-packings_images/imageFile46.png>)

![image 47](<2010-arkus-deriving-finite-sphere-packings_images/imageFile47.png>)

|2nd Moment<br><br>| |φ|σ<br><br>|Special Properties| | | | |
|---|---|---|---|---|---|---|---|---|
|∗1.5R2|2nd|TMod<br><br>|men12|t<br><br>|φ|Convσ<br><br>|Specialex P|roperties|
| |∗1.5R2| | | |Td<br><br>|12|Convex| |


- 5 Particle Packings

- Packing 1 (Graph 1):

A :

- 0

B @

- 0 0 1 1 1

- 0 0 1 1 1
- 1 1 0 1 1


- 1 1 1 0 1


- 1 1 1 1 0


1

C A

D :

0

B @

0 2q 2q

- 2

- 3 1 1 1


- 2

- 3 0 1 1 1


- 1 1 0 1 1
- 1 1 1 0 1 1 1 1 1 0


1

C A

R

C :

0

B @

0 0 0 4/(3√3) −4/3 (2/3)p2/3 1/(2√3)

p−12//23 0 −1

√30/2 −1/2 0

1

C A

R

![image 48](<2010-arkus-deriving-finite-sphere-packings_images/imageFile48.png>)

![image 49](<2010-arkus-deriving-finite-sphere-packings_images/imageFile49.png>)

|2nd Moment| |φ<br><br>|σ|Special Properties| | | | |
|---|---|---|---|---|---|---|---|---|
|∗2.33333R|2nd2<br><br>|DMom3h|ent6<br><br>| |φ C<br><br>|onvσ|Specialex P<br><br>|roperties|
| |∗2.33333R2<br><br>| | | |D3h|6<br><br>|Convex| |


6 Particle Packings

- Packing 1 (Graph 2):




- 5 Particle Packings

- Packing 1 (Graph 1):

A :

- 0

B @

- 0 0 1 1 1

- 0 0 1 1 1
- 1 1 0 1 1


- 1 1 1 0 1


- 1 1 1 1 0


1

C A

D :

0

B @

0 2q 2q

- 2

- 3 1 1 1


- 2

- 3 0 1 1 1


- 1 1 0 1 1
- 1 1 1 0 1 1 1 1 1 0


1

C A

R

C :

0

B @

0 0 0 4/(3√3) −4/3 (2/3)p2/3 1/(2√3)

p−12//23 0 −1

√30/2 −1/2 0

1

C A

R

![image 50](<2010-arkus-deriving-finite-sphere-packings_images/imageFile50.png>)

![image 51](<2010-arkus-deriving-finite-sphere-packings_images/imageFile51.png>)

6 Particle Packings

- Packing 1 (Graph 2):




28 NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER

6 Particle Packings

- Packing 1 (Graph 2):

A :

- 0

B @

0 0 1 1 1 1 0 0 0 1 1 1 1 0 0 0 1 1 1 1 0 0 1 1

- 1 1 1 1 0 1 1 1 1 1 1 0


1

C A

D :

0

B @

0 2q 2q

- 2

- 3 1 1 1 1


2 3 0 35 1 1 1

1 53 0 2q 1 1 2q

- 2

- 3 1 1


- 2

- 3 0 1 1


1 1 1 1 0 1 1 1 1 1 1 0

1

C A

R

C :

0

B @

4/(3√3) 1/3 (2/3)p2/3 0 −1 0 20/(9√3) −4/9 (10/9)p2/3 0 0 0 1/(2√3)

p√−132///223 −1/2 0

1

C A

R

![image 52](<2010-arkus-deriving-finite-sphere-packings_images/imageFile52.png>)

![image 53](<2010-arkus-deriving-finite-sphere-packings_images/imageFile53.png>)

|2nd Moment|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|3.35185R2<br><br>|C2v<br><br>|2| |


DERIVING FINITE SPHERE PACKINGS 29

- Packing 2 (Graph 4):


1

0

0 0

- 0

B @

- 0 0 1 1 1 1

- 0 0 1 1 1 1
- 1 1 0 0 1 1


- 1 1 0 0 1 1


- 1 1 1 1 0 0 1 1 1 1 0 0


1

- 0
- 1


−1 0 0 −1

A :

C A

- 0
- 1 0


C :

R

√02 √02 11 11 11 11

1

0

- 1 1 0 √2 1 1 1 1 √2 0 1 1

- 1 1 1 1 0 √2 1 1 1 1 √2 0


- 0
- 1/2

√−12//22

- 1/2


D :

R

C A

B @

C A

B @

−1/2 −

√2/2

![image 54](<2010-arkus-deriving-finite-sphere-packings_images/imageFile54.png>)

![image 55](<2010-arkus-deriving-finite-sphere-packings_images/imageFile55.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|∗3.0R2<br><br>|Oh|24<br><br>|New Seed Convex|


DERIVING FINITE SPHERE PACKINGS 29

7 Particle Packings

- Packing 1 (Graph 4):

A :

- 0

B @

- 0 0 0 1 1 1 1 0 0 0 1 0 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 0 1 1 1 0 1 0 0 1 1


- 1 1 1 1 1 0 1


- 1 1 1 1 1 1 0


1

C A

D :

0

B @

0 2q

- 2

- 3 2q


2 3 1 1 1 1

2 23 0 4

√6

9 1 53 1 1 2q

2 3 4

√6

9 0 35 1 1 1 1 1 53 0 2q 1 53 1 2q

- 2

- 3 1 1


2 3 0 1 1

- 1 1 1 1 1 0 1
- 1 1 1 1 1 1 0


1

C A

R

C :

0

B @

0 0 0 4/(3√3) −4/3 (2/3)p2/3 20/(9√3) −4/9 (10/9)p2/3 0 −1

- 0

4√3/9

- 1/3


(2/√3)3p/22/3 −1/2 0 1/(2√3)

p−12//23

1

C A

R

![image 56](<2010-arkus-deriving-finite-sphere-packings_images/imageFile56.png>)

![image 57](<2010-arkus-deriving-finite-sphere-packings_images/imageFile57.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|NATALIE4.24868ARKUS,R2 V|CINOT2v<br><br>|HAN2|N. MANOHARAN|


30 NA AND MICHAEL P. BRENNER

- Packing 2 (Graph 8):


1

0

0 −1 0 −5/(18√3) 7/18 (10/9)p2/3 20/(9√3) −4/9 (10/9)p2/3 0 0

- 0

B @

- 0 0 0 1 1 0 1

- 0 0 0 1 0 1 1

- 0 0 0 0 1 1 1
- 1 1 0 0 1 1 1


- 1 0 1 1 0 1 1


- 0 1 1 1 1 0 1


- 1 1 1 1 1 1 0


1

A :

C A

- 0 53 53 1 1 2q 5 3 0 53 1 2q 5 3

- 2

- 3 1


- 2

- 3 1 1


5 3 0 2q

- 2

- 3 1 1 1


- 1 1 2q
- 2

- 3 0 1 1 1


0

1

C :

R

√30/2 −1/2

D :

R

- 0

4√3/9

- 1/3


1 2q

2 3 1 1 0 1 1

2q

(2/3)p2/3 1/(2√3)

B @

C A

2 3 1 1 1 1 0 1

C A

B @

1 1 1 1 1 1 0

p−12//23

![image 58](<2010-arkus-deriving-finite-sphere-packings_images/imageFile58.png>)

![image 59](<2010-arkus-deriving-finite-sphere-packings_images/imageFile59.png>)

|2nd Moment<br><br>|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|4.47619R2|C3v<br><br>|3| |


DERIVING FINITE SPHERE PACKINGS 31

- Packing 3 (Graph 17):

A :

- 0

B @

- 0 0 1 0 1 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 0 1


- 0 1 0 0 0 1 1


- 1 1 1 0 0 1 1


- 1 1 0 1 1 0 1
- 1 1 1 1 1 1 0


1

C A

D :

0

B @

0 2q 2q

- 2

- 3 1 53 1 1 1


2 3 0 53 1 1 1 1

1 35 0 13q

107

3 1 2q

2 3 1

5 3 1 13q

107

3 0 2q

2 3 1 1

1 1 1 2q 1 1 2q

- 2

- 3 0 1 1


2 3 1 1 0 1

1 1 1 1 1 1 0

1

C A

R

C :

0

B @

4√3/9 1/3 (2/3)p2/3 0 −1 0 20/(9√3) −4/9 (10/9)p2/3 −7/(6√3) −1/2

(2/√3)3p/22/3 −1/2 0 0 0 0 1/(2√3)

p−12//23

1

C A

R

![image 60](<2010-arkus-deriving-finite-sphere-packings_images/imageFile60.png>)

![image 61](<2010-arkus-deriving-finite-sphere-packings_images/imageFile61.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|4.64550R2|C2<br><br>|2|Chiral|


32 NATALIE ARKUS, VINOTHAN N. MANOHARAN AND MICHAEL P. BRENNER

- Packing 4 (Graph 22):


0

1

0 0 0

- 0

B @

- 0 0 1 1 0 1 1

- 0 0 0 1 1 1 1
- 1 0 0 0 1 1 1


- 1 1 0 0 0 1 1


- 0 1 1 0 0 1 1
- 1 1 1 1 1 0 0


- 1 1 1 1 1 0 0


1

(1/2)q(1/2)(5 + √5) (1/4)(−3 −

√5) 0

A :

(1/2)q(1/2)(5 + √5) (1/4)(−1 −

C A

√5)

0 0 −1 0

2 1 1 q

0 q

1

0

3+√5

3+√5

2 1 1

C :

R

q

2 0 q

3+√5

3+√5

(1/8)(q2(5 + √5) + q10(5 + √5)) −1/2 0 (5 + √5)3/2/(20√2)

2 1 1 1 1 1 q

2 0 q

3+√5

3+√5

2 1 1 1 1 1 q

2 0 q

3+√5

3+√5

D :

R

2 1 1

q

2 1 1 q

3+√5

3+√5

2 0 1 1 1 1 1 1 1 0 q2 − √25 1 1 1 1 1 q2 − √25 0

q(1/10)(5−1/2−

C A

B @

√5)

(5 + √5)3/2/(20√2) −1/2

B @

C A

−q(1/10)(5 −

√5)

![image 62](<2010-arkus-deriving-finite-sphere-packings_images/imageFile62.png>)

![image 63](<2010-arkus-deriving-finite-sphere-packings_images/imageFile63.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|∗4.17082R2<br><br>|D5h|10<br><br>|New Seed Convex|


DERIVING FINITE SPHERE PACKINGS 33

Packing 5 (Graph 26):

1

0

1 −1 0 0 0 0 3/2

0

1

0 0 1 1 1 1 1 0 0 0 1 1 1 1 1 0 0 0 1 0 1 1 1 0 0 0 1 1 1 1 1 0 0 1 1 1 1 0 1 1 0 0 1 1 1 1 1 0 0

A :

√−12//22 0 −1

B @

C A

C :

R

0

1

√02 √02 √13 11 11 11 11 1 √3 0 √3 1 √3 1

- 0
- 1 0 0


- 1 1 √3 0 √2 1 1 1 1 1 √2 0 1 1

- 1 1 √3 1 1 0 √2 1 1 1 1 1 √2 0


D :

R

1/2 −1/2 −

B @

C A

√2/2 1/2

B @

C A

√−12//22

![image 64](<2010-arkus-deriving-finite-sphere-packings_images/imageFile64.png>)

![image 65](<2010-arkus-deriving-finite-sphere-packings_images/imageFile65.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|4.28571R2|C3v<br><br>|3<br><br>|Convex|


6. Properties of Packings Here we highlight some interesting properties of packings.

###### 6. Properties of Packings Here we highlight some interesting properties of packings.

- 6.1. New Seeds. New seeds are interesting because they are inherently new structures of n particles. They are also ‘generating sets,’ i.e. once they exist at a given starting n = m, they are propagated iteratively for all n > m. Geometrically, new seeds are inherently global structures, stabilized exactly by the n particles for which that new seed arises. Iterative packings are geometrically locally stable, in that < n subsets of the packing also correspond to packings. Thus, new seeds are unique events for a given number of particles, n. Figure 14 shows all new seeds of n ≤ 10 particles (where the set of new seeds at n = 10 is putative). The proportion of new seeds to total packings is relatively small – this can be seen in table 4.
- 6.2. Rigidity. We have enumerated packings satisfying minimal rigidity constraints, these constraints are necessary, but not suﬃcient for rigidity, and thus we can ﬁnd non-rigid packings satisfying these constraints. For these packings, there exists a degree of freedom in which particles can move without breaking or forming additional contacts. The ﬁrst instance of a non-rigid packing occurs at n = 9, at which there is one. At n = 10, there are 4 non-rigid packings: 1 non-rigid new seed, and 3 iterative non-rigid packings that derive from the n = 9 non-rigid new seed (ﬁgs 15 and 16).


- 6.1. New Seeds. New seeds are interesting because they are inherently new structures of n particles. They are also ‘generating sets,’ i.e. once they exist at a given starting n = m, they are propagated iteratively for all n > m. Geometrically, new seeds are inherently global structures, stabilized exactly by the n particles for which that new seed arises. Iterative packings are geometrically locally stable, in that subsets of less than n particles within the packing also correspond to packings. Thus, new seeds are unique events for a given number of particles, n. Figure 13 shows all new seeds of n ≤ 10 particles (where the set of new seeds at n = 10 is putative). The proportion of new seeds to total packings is relatively small for small n, which can be seen in table 4.
- 6.2. Rigidity. We have enumerated packings satisfying minimal rigidity constraints; these constraints are necessary but not suﬃcient for rigidity, and thus we can ﬁnd non-rigid packings that satisfy these constraints. For these packings, there exists a degree of freedom in which particles can move without breaking or forming additional contacts. The ﬁrst instance of a non-rigid packing occurs at n = 9, at which there is one. At n = 10, there are 4 non-rigid packings: 1 non-rigid new seed, and 3 iterative non-rigid packings that derive from the n = 9 non-rigid new seed (Fig. 14 and 15).


These 10 particle non-rigid packings will produce at least m non-rigid packings at n = 11, and so on. All non-rigid packings shown here contain ≥ 2 deformable open square faces. We do

###### These 10 particle non-rigid packings will iteratively produce at least m ≥ 1 non-rigid packings at n = 11, and so on. All non-rigid packings enumerated thus far contain at least 2 deformable

|n|Packings from [27]|Total Packings (Current Study)<br><br>|New Seeds<br><br>|Non-Rigid Packings|Chiral<br><br>|Total States|
|---|---|---|---|---|---|---|
|2|1|1<br><br>|0<br><br>|0|0|1|
|3<br><br>|1<br><br>|1<br><br>|0|0|0<br><br>|1|
|4<br><br>|1<br><br>|1<br><br>|0|0|0|1|
|5<br><br>|1<br><br>|1<br><br>|0|0|0<br><br>|1|
|6<br><br>|2|2|1<br><br>|0|0<br><br>|2|
|7|4|5<br><br>|1|0|1<br><br>|6|
|8|10<br><br>|13<br><br>|1<br><br>|0<br><br>|3|16|
|9|32<br><br>|52<br><br>|4|1|28<br><br>|80|
|10|113<br><br>|262|8<br><br>|4<br><br>|201<br><br>|463|


###### Table 4. Packings.

Total number of packings found by the current study, compared to those found by Hoare and McInnes [27], who used only the tetrahedral (n = 4) and octahedral (n = 8) seeds to iteratively calculate hard sphere packings by adding one particle at a time to (n − 1)-particle packings. They include chiral structures within their list of packings, so that a left and right-handed structure are considered to be 2 packings. We distinguish between chiral structures and packings, such that a left and right-handed structure is considered to be 1 packing with 2 distinct states (for n ≤ 10, left/right-handedness is the only type of chiral packing encountered). The number of packings having chiral counterparts is included in the column marked ‘chiral.’ The total number of states per n is equal to the number of packings plus the number of chiral structures. This is included in the table, along with the number of packings corresponding to new seeds and to non-rigid structures. The number of packings and total states for n = 9,10 diﬀer from the numbers we previously reported in [7] primarily because in [7] we did not run a check to conﬁrm that the dihedral angle was deﬁned. Here we report 2 more packings (and 3 more states) at n = 9; and 39 more packings (and 70 more states) at n = 10. In a paper extending our work [30], Hoy and O’Hern reported 52 packings at n = 9 and 279 packings at n = 10. However, the 279 packings that they reported multiply counted the three 25 contact packings. When all instances of the same packing being counted more than once are removed, it yields 261 packings that were reported by Hoy and O’Hern in [30]. Please see supplementary information, Appendix B [8] for a list of exactly which packings are reported here but were not reported in [7] or in [30].

open square faces. We do not know whether or not at least 2 open square faces are a requisite of non-rigid packings that satisfy minimal rigidity constraints. The open square faces must be ‘connected’ for the extra degree of freedom to exist – in the packings encountered thus far, this manifests itself by the existence of half-octahedra sharing at least 1 vertex.

- 6.3. The Tree Nature of Packings. There is a distinct tree nature to packings. New seeds are the origin of a branch in the tree. Iterative packings continue the branch. All n particle iterative packings can be decomposed into combinations of less than n-particle packings, and this decomposition is often not unique. When the decomposition is not unique, the branches of the tree


|![image 66](<2010-arkus-deriving-finite-sphere-packings_images/imageFile66.png>)<br><br>n = 6|![image 67](<2010-arkus-deriving-finite-sphere-packings_images/imageFile67.png>)<br><br>*|
|---|---|
|n = 7|![image 68](<2010-arkus-deriving-finite-sphere-packings_images/imageFile68.png>)<br><br>![image 69](<2010-arkus-deriving-finite-sphere-packings_images/imageFile69.png>)<br><br>*|
|n = 8|![image 70](<2010-arkus-deriving-finite-sphere-packings_images/imageFile70.png>)<br><br>![image 71](<2010-arkus-deriving-finite-sphere-packings_images/imageFile71.png>)<br><br>*|
|n = 9<br><br>![image 72](<2010-arkus-deriving-finite-sphere-packings_images/imageFile72.png>)|![image 73](<2010-arkus-deriving-finite-sphere-packings_images/imageFile73.png>)<br><br>![image 74](<2010-arkus-deriving-finite-sphere-packings_images/imageFile74.png>)<br><br>![image 75](<2010-arkus-deriving-finite-sphere-packings_images/imageFile75.png>)<br><br>![image 76](<2010-arkus-deriving-finite-sphere-packings_images/imageFile76.png>)<br><br>![image 77](<2010-arkus-deriving-finite-sphere-packings_images/imageFile77.png>)<br><br>![image 78](<2010-arkus-deriving-finite-sphere-packings_images/imageFile78.png>)<br><br>![image 79](<2010-arkus-deriving-finite-sphere-packings_images/imageFile79.png>)<br><br>*|
|![image 80](<2010-arkus-deriving-finite-sphere-packings_images/imageFile80.png>)<br><br>![image 81](<2010-arkus-deriving-finite-sphere-packings_images/imageFile81.png>)<br><br>n = 10|![image 82](<2010-arkus-deriving-finite-sphere-packings_images/imageFile82.png>)<br><br>![image 83](<2010-arkus-deriving-finite-sphere-packings_images/imageFile83.png>)<br><br>![image 84](<2010-arkus-deriving-finite-sphere-packings_images/imageFile84.png>)<br><br>![image 85](<2010-arkus-deriving-finite-sphere-packings_images/imageFile85.png>)<br><br>![image 86](<2010-arkus-deriving-finite-sphere-packings_images/imageFile86.png>)<br><br>![image 87](<2010-arkus-deriving-finite-sphere-packings_images/imageFile87.png>)<br><br>![image 88](<2010-arkus-deriving-finite-sphere-packings_images/imageFile88.png>)<br><br>![image 89](<2010-arkus-deriving-finite-sphere-packings_images/imageFile89.png>)<br><br>![image 90](<2010-arkus-deriving-finite-sphere-packings_images/imageFile90.png>)<br><br>![image 91](<2010-arkus-deriving-finite-sphere-packings_images/imageFile91.png>)<br><br>![image 92](<2010-arkus-deriving-finite-sphere-packings_images/imageFile92.png>)<br><br>![image 93](<2010-arkus-deriving-finite-sphere-packings_images/imageFile93.png>)<br><br>![image 94](<2010-arkus-deriving-finite-sphere-packings_images/imageFile94.png>)<br><br>![image 95](<2010-arkus-deriving-finite-sphere-packings_images/imageFile95.png>)<br><br>*|


###### Figure 13. New Seeds.

All new seeds of n ≤ 10 particles shown in both sphere and point/line representation. There exists only 1 packing for each n of n ≤ 5 particles, that can each be constructed iteratively from a dimer; thus there exist no new seeds for n ≤ 5. n = 6 is the ﬁrst instance of a new seed. The set of new seeds reported for n = 10 is putative and thus represents a lower bound. New seeds with a ∗ appearing to the right correspond to minima of the second moment out of all packings for that n. It can be seen here that, for the packings we have analyzed, when more than 1 packing exists, the minimum of the second moment happens to correspond to a new seed.

converge. Figures 16 and 17 show examples of tree convergence. Figure 16 shows the 2 possible decompositions of one of the 10 particle 25 contact packings. This packing can be formed either by adding 1 particle to the 9 particle non-rigid new seed, or by combining two polytetrahedra with a 6 particle octahedron.

Figure 17 shows the tree structure of 2 ≤ n ≤ 8 packings. It can be seen that tree convergence occurs from n = 7 to n = 8, where multiple 7-particle packings produce the same 8-particle packing under the addition of another particle.

6.4. Minima of the Second Moment. The second moment measures the deviation of particles from their collective center (centroid), and is given by

n

n

|ri − c|2 =

(13) (xi − cx)2 + (yi − cy)2 + (zi − cz)2

M =

i=1

i=1

![image 96](<2010-arkus-deriving-finite-sphere-packings_images/imageFile96.png>)

![image 97](<2010-arkus-deriving-finite-sphere-packings_images/imageFile97.png>)

![image 98](<2010-arkus-deriving-finite-sphere-packings_images/imageFile98.png>)

![image 99](<2010-arkus-deriving-finite-sphere-packings_images/imageFile99.png>)

![image 100](<2010-arkus-deriving-finite-sphere-packings_images/imageFile100.png>)

![image 101](<2010-arkus-deriving-finite-sphere-packings_images/imageFile101.png>)

#### =

![image 102](<2010-arkus-deriving-finite-sphere-packings_images/imageFile102.png>)

![image 103](<2010-arkus-deriving-finite-sphere-packings_images/imageFile103.png>)

![image 104](<2010-arkus-deriving-finite-sphere-packings_images/imageFile104.png>)

#### (a) (b)

![image 105](<2010-arkus-deriving-finite-sphere-packings_images/imageFile105.png>)

![image 106](<2010-arkus-deriving-finite-sphere-packings_images/imageFile106.png>)

![image 107](<2010-arkus-deriving-finite-sphere-packings_images/imageFile107.png>)

![image 108](<2010-arkus-deriving-finite-sphere-packings_images/imageFile108.png>)

![image 109](<2010-arkus-deriving-finite-sphere-packings_images/imageFile109.png>)

![image 110](<2010-arkus-deriving-finite-sphere-packings_images/imageFile110.png>)

Figure 14. The 9 particle non-rigid new seed (grey) is shown in the top left-hand box. It is composed of two joined 5-point polytetrahedra (red) attached to two joined half octahedra (blue). The substructures are shown overlain – purple bonds and particles are shared by both substructures; whereas only red or blue bonds and particles belong to the polytetrahedral or octahedral structures alone, respectively. Two representative ways of forming this non-rigid structure are shown in (a) and (b). (a) Two 5-point polytetrahedra are joined by sharing one common point (on bottom). The two polytetrahedra are then fully attached to one another via the remaining 3 bonds ﬁrst shown in dashed black lines, as potential bonds, and then in solid white lines, as actualized bonds. These bonds form the two connected half octahedra. (b) 2 particles (red) are attached to the concave side faces of the 2 joined half octahedra (blue). The 2 red particles form the two 5-point polytetrahedral substructures once they are attached to the joined octahedra.

where ri is the x,y,z position of particle i; and c is the centroid, the average x,y,z position over all particles, given by

n

1 n

cx =

(14) xi and analogously given for cy and cz.

i=1

The minimum of the second moment corresponds to the packing with the smallest M. The 2nd moment is listed within the list of packings in section 5 and in appendix B [8], and a ‘∗’ signiﬁes the minimum of the 2nd moment for each n in ﬁgure 13. We conﬁrm that the minima of the 2nd moment reported by Sloane et al. [48] are correct (they proved the 2nd moment minima for n ≤ 4, but for n > 4 these were putative structures). For n ≤ 10, each minimum of the second moment corresponds to a new seed, if a new seed exists.

- 6.5. Ground States and the Maximum Number of Contacts. A fundamental question related to sphere packings is what is the maximum number of contacts that a packing of n spheres can have? Not only is this question of mathematical interest in its own right, but it is also


![image 111](<2010-arkus-deriving-finite-sphere-packings_images/imageFile111.png>)

![image 112](<2010-arkus-deriving-finite-sphere-packings_images/imageFile112.png>)

![image 113](<2010-arkus-deriving-finite-sphere-packings_images/imageFile113.png>)

![image 114](<2010-arkus-deriving-finite-sphere-packings_images/imageFile114.png>)

![image 115](<2010-arkus-deriving-finite-sphere-packings_images/imageFile115.png>)

(a) (b) (c)

![image 116](<2010-arkus-deriving-finite-sphere-packings_images/imageFile116.png>)

![image 117](<2010-arkus-deriving-finite-sphere-packings_images/imageFile117.png>)

![image 118](<2010-arkus-deriving-finite-sphere-packings_images/imageFile118.png>)

![image 119](<2010-arkus-deriving-finite-sphere-packings_images/imageFile119.png>)

![image 120](<2010-arkus-deriving-finite-sphere-packings_images/imageFile120.png>)

![image 121](<2010-arkus-deriving-finite-sphere-packings_images/imageFile121.png>)

![image 122](<2010-arkus-deriving-finite-sphere-packings_images/imageFile122.png>)

- Figure 15. Non-rigid packings of 9 and 10 spheres. (a) The non-rigid n = 9 packing, with non-rigid motion, corresponding to a twisting of the square faces, shown by black arrows. (b) Non-rigid n = 10 packings formed iteratively by adding one particle to the non-rigid n = 9 seed. The non-rigid motion of these structures is the same as in (a). (c) Non-rigid n = 10 seed. Non-rigid motion, corresponding to a twisting of the radially connected square faces, connected by the bottom particle, is shown by the black arrows. This twisting motion can be accomplished by, for example, twisting the top triangle.

|![image 123](<2010-arkus-deriving-finite-sphere-packings_images/imageFile123.png>)| |
|---|---|
|![image 124](<2010-arkus-deriving-finite-sphere-packings_images/imageFile124.png>)<br><br>![image 125](<2010-arkus-deriving-finite-sphere-packings_images/imageFile125.png>)<br><br>![image 126](<2010-arkus-deriving-finite-sphere-packings_images/imageFile126.png>)<br><br>![image 127](<2010-arkus-deriving-finite-sphere-packings_images/imageFile127.png>)<br><br>![image 128](<2010-arkus-deriving-finite-sphere-packings_images/imageFile128.png>)<br><br>![image 129](<2010-arkus-deriving-finite-sphere-packings_images/imageFile129.png>)<br><br>![image 130](<2010-arkus-deriving-finite-sphere-packings_images/imageFile130.png>)<br><br>![image 131](<2010-arkus-deriving-finite-sphere-packings_images/imageFile131.png>)<br><br>![image 132](<2010-arkus-deriving-finite-sphere-packings_images/imageFile132.png>)<br><br>![image 133](<2010-arkus-deriving-finite-sphere-packings_images/imageFile133.png>)<br><br>![image 134](<2010-arkus-deriving-finite-sphere-packings_images/imageFile134.png>)<br><br>![image 135](<2010-arkus-deriving-finite-sphere-packings_images/imageFile135.png>)<br><br>![image 136](<2010-arkus-deriving-finite-sphere-packings_images/imageFile136.png>)<br><br>![image 137](<2010-arkus-deriving-finite-sphere-packings_images/imageFile137.png>)<br><br>![image 138](<2010-arkus-deriving-finite-sphere-packings_images/imageFile138.png>)<br><br>![image 139](<2010-arkus-deriving-finite-sphere-packings_images/imageFile139.png>)<br><br>![image 140](<2010-arkus-deriving-finite-sphere-packings_images/imageFile140.png>)<br><br>![image 141](<2010-arkus-deriving-finite-sphere-packings_images/imageFile141.png>)<br><br>![image 142](<2010-arkus-deriving-finite-sphere-packings_images/imageFile142.png>)<br><br>![image 143](<2010-arkus-deriving-finite-sphere-packings_images/imageFile143.png>)<br><br>![image 144](<2010-arkus-deriving-finite-sphere-packings_images/imageFile144.png>)<br><br>![image 145](<2010-arkus-deriving-finite-sphere-packings_images/imageFile145.png>)<br><br>![image 146](<2010-arkus-deriving-finite-sphere-packings_images/imageFile146.png>)<br><br>![image 147](<2010-arkus-deriving-finite-sphere-packings_images/imageFile147.png>)<br><br>![image 148](<2010-arkus-deriving-finite-sphere-packings_images/imageFile148.png>)<br><br>![image 149](<2010-arkus-deriving-finite-sphere-packings_images/imageFile149.png>)<br><br>![image 150](<2010-arkus-deriving-finite-sphere-packings_images/imageFile150.png>)<br><br>![image 151](<2010-arkus-deriving-finite-sphere-packings_images/imageFile151.png>)<br><br>![image 152](<2010-arkus-deriving-finite-sphere-packings_images/imageFile152.png>)<br><br>![image 153](<2010-arkus-deriving-finite-sphere-packings_images/imageFile153.png>)<br><br>![image 154](<2010-arkus-deriving-finite-sphere-packings_images/imageFile154.png>)<br><br>![image 155](<2010-arkus-deriving-finite-sphere-packings_images/imageFile155.png>)<br><br>![image 156](<2010-arkus-deriving-finite-sphere-packings_images/imageFile156.png>)<br><br>![image 157](<2010-arkus-deriving-finite-sphere-packings_images/imageFile157.png>)<br><br>![image 158](<2010-arkus-deriving-finite-sphere-packings_images/imageFile158.png>)<br><br>![image 159](<2010-arkus-deriving-finite-sphere-packings_images/imageFile159.png>)<br><br>![image 160](<2010-arkus-deriving-finite-sphere-packings_images/imageFile160.png>)<br><br>![image 161](<2010-arkus-deriving-finite-sphere-packings_images/imageFile161.png>)<br><br>![image 162](<2010-arkus-deriving-finite-sphere-packings_images/imageFile162.png>)<br><br>![image 163](<2010-arkus-deriving-finite-sphere-packings_images/imageFile163.png>)<br><br>![image 164](<2010-arkus-deriving-finite-sphere-packings_images/imageFile164.png>)<br><br>![image 165](<2010-arkus-deriving-finite-sphere-packings_images/imageFile165.png>)<br><br>![image 166](<2010-arkus-deriving-finite-sphere-packings_images/imageFile166.png>)<br><br>![image 167](<2010-arkus-deriving-finite-sphere-packings_images/imageFile167.png>)<br><br>![image 168](<2010-arkus-deriving-finite-sphere-packings_images/imageFile168.png>)|![image 169](<2010-arkus-deriving-finite-sphere-packings_images/imageFile169.png>)<br><br>![image 170](<2010-arkus-deriving-finite-sphere-packings_images/imageFile170.png>)<br><br>![image 171](<2010-arkus-deriving-finite-sphere-packings_images/imageFile171.png>)<br><br>![image 172](<2010-arkus-deriving-finite-sphere-packings_images/imageFile172.png>)<br><br>![image 173](<2010-arkus-deriving-finite-sphere-packings_images/imageFile173.png>)<br><br>![image 174](<2010-arkus-deriving-finite-sphere-packings_images/imageFile174.png>)<br><br>![image 175](<2010-arkus-deriving-finite-sphere-packings_images/imageFile175.png>)<br><br>![image 176](<2010-arkus-deriving-finite-sphere-packings_images/imageFile176.png>)<br><br>![image 177](<2010-arkus-deriving-finite-sphere-packings_images/imageFile177.png>)<br><br>![image 178](<2010-arkus-deriving-finite-sphere-packings_images/imageFile178.png>)<br><br>![image 179](<2010-arkus-deriving-finite-sphere-packings_images/imageFile179.png>)<br><br>![image 180](<2010-arkus-deriving-finite-sphere-packings_images/imageFile180.png>)<br><br>![image 181](<2010-arkus-deriving-finite-sphere-packings_images/imageFile181.png>)<br><br>![image 182](<2010-arkus-deriving-finite-sphere-packings_images/imageFile182.png>)<br><br>![image 183](<2010-arkus-deriving-finite-sphere-packings_images/imageFile183.png>)<br><br>![image 184](<2010-arkus-deriving-finite-sphere-packings_images/imageFile184.png>)<br><br>![image 185](<2010-arkus-deriving-finite-sphere-packings_images/imageFile185.png>)<br><br>![image 186](<2010-arkus-deriving-finite-sphere-packings_images/imageFile186.png>)<br><br>![image 187](<2010-arkus-deriving-finite-sphere-packings_images/imageFile187.png>)<br><br>![image 188](<2010-arkus-deriving-finite-sphere-packings_images/imageFile188.png>)<br><br>![image 189](<2010-arkus-deriving-finite-sphere-packings_images/imageFile189.png>)<br><br>![image 190](<2010-arkus-deriving-finite-sphere-packings_images/imageFile190.png>)<br><br>![image 191](<2010-arkus-deriving-finite-sphere-packings_images/imageFile191.png>)<br><br>![image 192](<2010-arkus-deriving-finite-sphere-packings_images/imageFile192.png>)<br><br>![image 193](<2010-arkus-deriving-finite-sphere-packings_images/imageFile193.png>)<br><br>![image 194](<2010-arkus-deriving-finite-sphere-packings_images/imageFile194.png>)<br><br>![image 195](<2010-arkus-deriving-finite-sphere-packings_images/imageFile195.png>)<br><br>![image 196](<2010-arkus-deriving-finite-sphere-packings_images/imageFile196.png>)<br><br>![image 197](<2010-arkus-deriving-finite-sphere-packings_images/imageFile197.png>)<br><br>![image 198](<2010-arkus-deriving-finite-sphere-packings_images/imageFile198.png>)<br><br>![image 199](<2010-arkus-deriving-finite-sphere-packings_images/imageFile199.png>)<br><br>![image 200](<2010-arkus-deriving-finite-sphere-packings_images/imageFile200.png>)<br><br>![image 201](<2010-arkus-deriving-finite-sphere-packings_images/imageFile201.png>)<br><br>![image 202](<2010-arkus-deriving-finite-sphere-packings_images/imageFile202.png>)<br><br>![image 203](<2010-arkus-deriving-finite-sphere-packings_images/imageFile203.png>)<br><br>![image 204](<2010-arkus-deriving-finite-sphere-packings_images/imageFile204.png>)<br><br>![image 205](<2010-arkus-deriving-finite-sphere-packings_images/imageFile205.png>)<br><br>![image 206](<2010-arkus-deriving-finite-sphere-packings_images/imageFile206.png>)<br><br>![image 207](<2010-arkus-deriving-finite-sphere-packings_images/imageFile207.png>)<br><br>![image 208](<2010-arkus-deriving-finite-sphere-packings_images/imageFile208.png>)<br><br>![image 209](<2010-arkus-deriving-finite-sphere-packings_images/imageFile209.png>)<br><br>![image 210](<2010-arkus-deriving-finite-sphere-packings_images/imageFile210.png>)<br><br>![image 211](<2010-arkus-deriving-finite-sphere-packings_images/imageFile211.png>)<br><br>![image 212](<2010-arkus-deriving-finite-sphere-packings_images/imageFile212.png>)<br><br>![image 213](<2010-arkus-deriving-finite-sphere-packings_images/imageFile213.png>)<br><br>![image 214](<2010-arkus-deriving-finite-sphere-packings_images/imageFile214.png>)<br><br>![image 215](<2010-arkus-deriving-finite-sphere-packings_images/imageFile215.png>)|


- Figure 16. Tree Convergence in a 10-Particle Packing. An example of tree convergence in one of the 25 contact packings of 10 particles. This packing, shown in grey (top panel), can be decomposed into (bottom left panel) the 9 particle non-rigid new seed (red) plus one particle (blue) that rigidiﬁes the structure, or into (bottom right panel) an octahedron (blue) with 2 attached polytetrahedra (red). The red dashed line indicates an ‘implicit contact,’ a contact that automatically forms once the other contacts are in place (this corresponds to the 25th contact).


|![image 216](<2010-arkus-deriving-finite-sphere-packings_images/imageFile216.png>)<br><br>![image 217](<2010-arkus-deriving-finite-sphere-packings_images/imageFile217.png>)|
|---|


- n = 2
- n = 3
- n = 4
- n = 5


|![image 218](<2010-arkus-deriving-finite-sphere-packings_images/imageFile218.png>)<br><br>![image 219](<2010-arkus-deriving-finite-sphere-packings_images/imageFile219.png>)|
|---|


![image 220](<2010-arkus-deriving-finite-sphere-packings_images/imageFile220.png>)

![image 221](<2010-arkus-deriving-finite-sphere-packings_images/imageFile221.png>)

![image 222](<2010-arkus-deriving-finite-sphere-packings_images/imageFile222.png>)

![image 223](<2010-arkus-deriving-finite-sphere-packings_images/imageFile223.png>)

|![image 224](<2010-arkus-deriving-finite-sphere-packings_images/imageFile224.png>)<br><br>![image 225](<2010-arkus-deriving-finite-sphere-packings_images/imageFile225.png>)|
|---|


|![image 226](<2010-arkus-deriving-finite-sphere-packings_images/imageFile226.png>)<br><br>![image 227](<2010-arkus-deriving-finite-sphere-packings_images/imageFile227.png>)|
|---|


n = 6

| | |
|---|---|
|![image 228](<2010-arkus-deriving-finite-sphere-packings_images/imageFile228.png>)<br><br>![image 229](<2010-arkus-deriving-finite-sphere-packings_images/imageFile229.png>)| |


![image 230](<2010-arkus-deriving-finite-sphere-packings_images/imageFile230.png>)

- n = 7
- n = 8


|![image 231](<2010-arkus-deriving-finite-sphere-packings_images/imageFile231.png>)<br><br>![image 232](<2010-arkus-deriving-finite-sphere-packings_images/imageFile232.png>)|
|---|


![image 233](<2010-arkus-deriving-finite-sphere-packings_images/imageFile233.png>)

|![image 234](<2010-arkus-deriving-finite-sphere-packings_images/imageFile234.png>)<br><br>![image 235](<2010-arkus-deriving-finite-sphere-packings_images/imageFile235.png>)|
|---|


![image 236](<2010-arkus-deriving-finite-sphere-packings_images/imageFile236.png>)

![image 237](<2010-arkus-deriving-finite-sphere-packings_images/imageFile237.png>)

![image 238](<2010-arkus-deriving-finite-sphere-packings_images/imageFile238.png>)

![image 239](<2010-arkus-deriving-finite-sphere-packings_images/imageFile239.png>)

![image 240](<2010-arkus-deriving-finite-sphere-packings_images/imageFile240.png>)

![image 241](<2010-arkus-deriving-finite-sphere-packings_images/imageFile241.png>)

![image 242](<2010-arkus-deriving-finite-sphere-packings_images/imageFile242.png>)

![image 243](<2010-arkus-deriving-finite-sphere-packings_images/imageFile243.png>)

![image 244](<2010-arkus-deriving-finite-sphere-packings_images/imageFile244.png>)

![image 245](<2010-arkus-deriving-finite-sphere-packings_images/imageFile245.png>)

![image 246](<2010-arkus-deriving-finite-sphere-packings_images/imageFile246.png>)

![image 247](<2010-arkus-deriving-finite-sphere-packings_images/imageFile247.png>)

![image 248](<2010-arkus-deriving-finite-sphere-packings_images/imageFile248.png>)

![image 249](<2010-arkus-deriving-finite-sphere-packings_images/imageFile249.png>)

![image 250](<2010-arkus-deriving-finite-sphere-packings_images/imageFile250.png>)

![image 251](<2010-arkus-deriving-finite-sphere-packings_images/imageFile251.png>)

![image 252](<2010-arkus-deriving-finite-sphere-packings_images/imageFile252.png>)

![image 253](<2010-arkus-deriving-finite-sphere-packings_images/imageFile253.png>)

|![image 254](<2010-arkus-deriving-finite-sphere-packings_images/imageFile254.png>)<br><br>![image 255](<2010-arkus-deriving-finite-sphere-packings_images/imageFile255.png>)|
|---|


![image 256](<2010-arkus-deriving-finite-sphere-packings_images/imageFile256.png>)

![image 257](<2010-arkus-deriving-finite-sphere-packings_images/imageFile257.png>)

![image 258](<2010-arkus-deriving-finite-sphere-packings_images/imageFile258.png>)

![image 259](<2010-arkus-deriving-finite-sphere-packings_images/imageFile259.png>)

|![image 260](<2010-arkus-deriving-finite-sphere-packings_images/imageFile260.png>)<br><br>![image 261](<2010-arkus-deriving-finite-sphere-packings_images/imageFile261.png>)|
|---|


|![image 262](<2010-arkus-deriving-finite-sphere-packings_images/imageFile262.png>)<br><br>![image 263](<2010-arkus-deriving-finite-sphere-packings_images/imageFile263.png>)|
|---|


###### Figure 17. Tree Convergence for n ≤ 8.

An example of tree convergence for 2 ≤ n ≤ 8. Packings above which there is no arrow correspond to new seeds, and thus to the beginning of a new branch. The arrows then point to the n-particle packing or group of packings that form iteratively by adding one particle. It can be seen that even for the iterative case of adding one particle, there is tree convergence from n = 7 to n = 8 (shown by multiple arrows feeding into the same packing).

of signiﬁcant physical interest as such packings correspond to ground states. The number of packings that contain the maximum number of contacts in turn corresponds to the ground state degeneracy. Table 6.5 shows how the ground state degeneracy changes with n. Interestingly, this relation appears to be oscillatory.

For n ≤ 9, every packing has exactly 3n−6 contacts. Thus, at each ﬁxed n, n ≤ 9, all packings have the same potential energy. Table 6.5 shows that, for n ≤ 9, the ground state degeneracy increases exponentially. But at n = 10 this trend changes due to a small number of packings that can have 25 = 3n − 5 contacts (all other 10-particle packings have 3n − 6 contacts). There exist 3 such packings, each containing octahedra (Fig. 18a-c). These three structures are the ground states at n = 10.

![image 264](<2010-arkus-deriving-finite-sphere-packings_images/imageFile264.png>)

(a) (b) (c)

![image 265](<2010-arkus-deriving-finite-sphere-packings_images/imageFile265.png>)

![image 266](<2010-arkus-deriving-finite-sphere-packings_images/imageFile266.png>)

![image 267](<2010-arkus-deriving-finite-sphere-packings_images/imageFile267.png>)

![image 268](<2010-arkus-deriving-finite-sphere-packings_images/imageFile268.png>)

![image 269](<2010-arkus-deriving-finite-sphere-packings_images/imageFile269.png>)

(d) (e) (f)

![image 270](<2010-arkus-deriving-finite-sphere-packings_images/imageFile270.png>)

![image 271](<2010-arkus-deriving-finite-sphere-packings_images/imageFile271.png>)

![image 272](<2010-arkus-deriving-finite-sphere-packings_images/imageFile272.png>)

(g) (h) (i)

Figure 18. Maximum contact packings for 10 ≤ n ≤ 20. We are reasonably conﬁdent that the n = 10 packings shown here correspond to the maximum contact packings, but maximum contact packings of n > 10 are conjectured. (a)-(c) 10particle packings with 3n − 5 = 25 contacts. (a) can be formed either by adding one particle (red) to one of the open square faces (blue) or as otherwise detailed in ﬁgure 16. (b) can be formed by adding one particle (red) to the concave 4 particle face created by 2 joined octahedra (blue). (c) is formed by connecting 2 octahedra by one edge. (d) 11 particle maximum contact packing (3n − 4 = 29 contacts). This can be formed either by adding one particle (red) to the concave 4 particle face created by the 2 joined octahedra of (b), or by adding one particle to the one remaining open square face of (a). (e) 12 particle maximum contact packing (3n − 3 = 33 contacts). This is formed by adding one particle (red) to the concave 4 particle face created by 2 joined octahedra (blue). 13 particle maximum contact packings are constructed iteratively from this packing. (f) 14 particle maximum contact packing (3n − 2 = 40 contacts). This is formed by 3 radially connected octahedra (blue) and 2 particles (yellow) added to each of the concave 5 particle faces created by the 3 joined octahedra. (g) 15 and 16 particle maximum contact packings containing 3n − 1 and 3n contacts respectively. The 15-particle packing corresponds to the addition of only one of the red particles to the concave 4 particle face of (f), and the 16-particle packing includes both red particles. (h) 17 particle 3n contact packing formed by 4 radially connected octahedra (blue) and 2 particles (yellow) connected to the concave 6 particle faces created by the 4 joined octahedra. At 17 particles, 3n contact packings correspond to this packing as well as packings constructed iteratively from (g). (i) 18,19,20 particle maximum contact packings corresponding to 3n + 1, 3n + 2, and 3n + 3 contacts respectively. Each of these packings is constructed by adding a particle (red) to one of the concave 4 particle faces created by the joined octahedra – the 18-particle packing is constructed by adding one such particle to (h), 19 by adding 2, and 20 by adding 3.

For n ≥ 11, we conjecture as to what the maximum number of contacts are, and provide examples of such structures. The maximum contact packings at n = 10 arise because it becomes possible to add 4 contacts to minimally-rigid 9-particle packings; whereas all other iterative packings of n ≤ 10 spheres are formed by the addition of 3m contacts to a minimally-rigid n−m sphere packing. All maximum contact packings found thus far correspond to iterative packings. We have not determined whether this is true for all n, but we conjecture that it is, because new seeds tend to contain more empty space, and thus less contacts. We have found three types of structures that allow for the addition of more than 3m contacts: (i) m octahedra, where each pair of octahedra share one edge (as in Fig. 18c), (ii) an open square face created by half an octahedra (as shown in blue in ﬁgure 18a), and (iii) the concave m point face created by octahedra sharing 3 edges (as shown in blue in ﬁgure 18d,e). 4 point concave faces are shown, for example, in ﬁgure 18e; 5 point concave faces in ﬁgure 18f,g; and 6 point concave faces in ﬁgure 18h,i. To each m point concave face, it is possible to add one particle with m contacts; this is evidenced, for example, by the red particle with 4 contacts in ﬁgure 18e and the yellow particles with either 5 or 6 contacts in ﬁgure 18f-i. All structures leading to maximum contact packings that we have found thus far are related to octahedra, and we conjecture that this will be the case for all n. (Interestingly all non-rigid packings found thus far are also related to octahedra, in that they contain the open square faces created by half-octahedral structures; they all contain half-octahedra sharing at least 1 point).

There are many fewer ways of adding greater than 3m contacts to an n − m sphere packing than there are of adding 3m contacts, thus leading to a relatively small number of ground state packings when a new maximum number of contacts, as a function of n, is reached. Thus, each time a packing with a greater maximum number of contacts, as a function of n, is possible, we expect the ground state degeneracy to either decrease or to remain small. When the functional form for the maximum number of contacts remains constant, we expect the ground state degeneracy to grow rapidly, due in large part to the iterative growth of adding a particle with 3 contacts to packings. Table 6.5 for example, shows that for n ≤ 9 the ground state degeneracy increases exponentially because all packings have 3n−6 contacts. But at n = 10 this trend changes because packings with more than 3n − 6 contacts become possible. At n = 13 and at n = 17, rapid growth in the ground state degeneracy resumes as the functional form for the maximum number of contacts remains constant, but for all other n, the ground state degeneracy either decreases or remains constant, because a new maximum number of contacts, as a function of n, is possible.

At low temperatures, we expect the experimentally observable packings to be dominated by the maximum contact packings. Thus, for n = 10, and for any n in which either (i) the maximum number of contacts increases as a function of n or (ii) the maximum number of contacts does not remain constant for too long (≤ 3 particles), we expect that there are only a small number of packings that will be observable at low temperature. This trend can be seen in the conjectured ground state degeneracy for 9 < n ≤ 20 in Table 6.5, and we conjecture that a similar low amplitude oscillatory trend might also continue for n > 20.

- 6.6. Lattice Structure. The non-rigid new seeds at n = 9 and n = 10, as well as the maximum contact packings of n < 13 are all subunits of the hexagonally close-packed (HCP) lattice, being combinations of face-sharing tetrahedra and octahedra. Additionally, the structure shown in ﬁgure 18c is a subunit of either the HCP or face-centered cubic (FCC) lattice. The non-rigid packings are entropically favored, and we thus expect these to form with higher probability at higher temperatures; while the maximum contact packings are energetically favored, corresponding to the structures that will form with higher probability as the temperature, T → 0. For 14 ≤ n ≤ 20, the maximum contact packings are not HCP subunits (Fig. 18 f-i).


###### Table 5. Number of Contacts vs. Number of Particles.

The ﬁrst column corresponds to the number of particles, n, the 2nd column to the number of contacts that the ground state packing(s) have, and the 3rd column to the number of packings in the ground state. Note that for n ≥ 11 these are putative results and thus the number of packings with 3n − m contacts represents a lower bound, and the ground state number of contacts is conjectured (we have not encountered packings with more contacts, but we have not proved that they don’t exist).

|n<br><br>|Contacts|Ground State Packings|
|---|---|---|
|2<br><br>|3n − 6<br><br>|1|
|3|3n − 6<br><br>|1|
|4<br><br>|3n − 6|1|
|5<br><br>|3n − 6|1|
|6|3n − 6<br><br>|2|
|7<br><br>|3n − 6<br><br>|5|
|8|3n − 6<br><br>|13|
|9|3n − 6<br><br>|52|
|10<br><br>|3n − 5<br><br>|3|
|11|3n − 4|1|
|12<br><br>|3n − 3<br><br>|1|
|13|3n − 3|7|
|14|3n − 2|1|
|15<br><br>|3n − 1<br><br>|1|
|16|3n<br><br>|1|
|17<br><br>|3n<br><br>|8|
|18<br><br>|3n + 1|1|
|19|3n + 2|1|
|20<br><br>|3n + 3|1|


Frank predicted [20] that icosahedral short-range order would be a hallmark of liquid structure, and experimental studies have shown local cluster-like order in bulk atomic liquids and glasses [44, 47]. Results from a recent study suggest that structural arrest in condensed phases may be related to geometrical constraints at the scale of a few particles [45]. The propensity for icosahedra [28, 16] in longer-range systems is absent in ours. We have proven that the icosahedron is not the ground state at n = 12, nor is an icosahedron with a central sphere the ground state at n = 13. A 12-sphere icosahedron has only 3n − 6 = 30 contacts, and in a 13-sphere icosahedron the outer spheres would not be close enough to interact with each other.

It is possible, and perhaps even likely, that the lattice structures corresponding to ground state packings will be periodic with n. For example, although the ground states for 14 ≤ n ≤ 20 are not commensurate with HCP, the ground states for a ﬁnite range of higher n may be, and may then subsequently return to the lattice structure commensurate with 14 ≤ n ≤ 20. Detailing the structures of ground state packings for all n, and geometrical patterns contained therein, is a subject of future work. Furthermore, the appearance of crystalline order, such as HCP, at very low n may inﬂuence nucleation.

7. Extensions and Conjectures

- 7.1. The major roadblock for reaching higher n. The main roadblock to the analytical enumeration of sphere packings at higher n in the current work is deriving one analytical geometrical rule that can solve for all new seeds. In the next section, we outline a numerical method, based on the triangular bipyramid rule, that is capable of ﬁnding all solutions of A −→ D, and which can thus solve for all new seeds. However, the implementation of either this numerical scheme or the derivation of an analytical rule would only allow us to enumerate packings of up to about n = 14 spheres. This is because the real limitation of the current method arises from the enumeration of minimally-rigid, non-isomorphic adjacency matrices. For n < 10, the enumeration of such adjacency matrices using nauty [42] takes on the order of seconds. For n = 10,11, this enumeration takes minutes. For n = 12, enumerating all minimally-rigid, non-isomorphic A’s takes approximately 2 hours. Extrapolating, we expect the enumeration at n = 13,14 to take on the order of 2 days and 2 weeks, respectively. Thus, around n = 14, we begin to reach the computational limitations of this method, which is due to the enumeration of A’s.


Only a very small fraction of adjacency matrices correspond to sphere packings; for example, at n = 10, out of the 750,226 A’s, only 262 correspond to sphere packings. Thus, the enumeration of all A’s really is a brute force and wasteful step. Further advances in enumerating sphere packings will require overcoming this roadblock. In section 7.3, we propose one method that might be able to overcome this limitation.

- 7.2. Applying the Triangular Bipyramid Rule to New Seeds. The Triangular Bipyramid rule solves for iterative structures but does not work for noniterative ones, which we also showed increase rapidly starting at n = 10. Here, we discuss how the triangular bipyramid rule might also be applied to new seeds. In this case, the equations for the unknown interparticle distances,


rij, are implicit and thus must be solved numerically.

In a new seed, any triangular bipyramid that contains an unknown distance will contain more than one unknown distance. Thus, rij can not be determined one at a time, as with iterative packings; instead we must construct a system of equations to solve for the unknown distances19. Let us consider a general triangular bipyramid, like that shown in ﬁgure 19, but here all 10 distances are potentially unknown (Fig. 19). For m unknown rij, we construct m triangular bipyramids to solve for the rij (see Fig. 20, for example). Each triangular bipyramid yields one equation for an unknown distance, thus yielding m equations with m unknowns in total, making the system well deﬁned.

We assign a label, di, to each of the 10 distances within the triangular bipyramid (Fig. 19). Explicit formulas can always be obtained for d2 and d3. Thus, over all m triangular bipyramids, we place each unknown distance in location d2 or d3 at least once. New seeds are inherently global structures, thus the m triangular bipyramids should contain all n points amongst them in order to ensure that the solution space is suﬃciently constrained. Also, to avoid redundancy, each triangular bipyramid must contain a unique combination of 5 particles.

The equations for the rij are derived from the triangular bipyramid property that the dihedral angle A1 must equal either the sum or the diﬀerence of the dihedral angles A2 and A3 (as was detailed in section 4 and in Fig. 19). This equation is cumbersome, and it as well as its derivation can be found in Appendix A of the supplemental information [8]. As always with the triangular

19As can be seen in section 4 or in Appendix A of the supplemental information [8], the equation for an unknown distance is quadratic. Thus, this will be a quadratic system of equations.

p

![image 273](<2010-arkus-deriving-finite-sphere-packings_images/imageFile273.png>)

![image 274](<2010-arkus-deriving-finite-sphere-packings_images/imageFile274.png>)

![image 275](<2010-arkus-deriving-finite-sphere-packings_images/imageFile275.png>)

d10 d9 d3

![image 276](<2010-arkus-deriving-finite-sphere-packings_images/imageFile276.png>)

d8

![image 277](<2010-arkus-deriving-finite-sphere-packings_images/imageFile277.png>)

j q

![image 278](<2010-arkus-deriving-finite-sphere-packings_images/imageFile278.png>)

d7

d6

![image 279](<2010-arkus-deriving-finite-sphere-packings_images/imageFile279.png>)

![image 280](<2010-arkus-deriving-finite-sphere-packings_images/imageFile280.png>)

![image 281](<2010-arkus-deriving-finite-sphere-packings_images/imageFile281.png>)

![image 282](<2010-arkus-deriving-finite-sphere-packings_images/imageFile282.png>)

k d2

![image 283](<2010-arkus-deriving-finite-sphere-packings_images/imageFile283.png>)

![image 284](<2010-arkus-deriving-finite-sphere-packings_images/imageFile284.png>)

d1

![image 285](<2010-arkus-deriving-finite-sphere-packings_images/imageFile285.png>)

![image 286](<2010-arkus-deriving-finite-sphere-packings_images/imageFile286.png>)

d5

d4

![image 287](<2010-arkus-deriving-finite-sphere-packings_images/imageFile287.png>)

i

Figure 19. General Triangular Bipyramid. A triangular bipyramid where all distances, labeled d1 − d10, are potentially unknown. The particles, i,j,k,p,q correspond to the same labeling as in ﬁgure 19. This triangular bipyramid is used to derive the general equation for an unknown relative distance, rij (appendix A [8]).

bipyramid rule, due to the 2 possibilities of A1 equaling either the sum or the diﬀerence of A2 and A3, each unknown distance has 2 possible solutions.

For each set of rij that is to be solved, construct initial guesses between the bounds of the triangle inequality and no-overlap constraint, and iterate the initial guess with a step size less than or equal to the minimum diﬀerence between diﬀerent solutions (for rigid structures). There will always exist unknown rij ≤ 2R because each particle has at least 3 contacts20. These are the rij for which there exists a k satisfying Aik = Ajk = 1, Aij = 0. Thus, ﬁrst solve the set of R ≤ rij ≤ 2R. If unknown rij remain, then solve the set of rij that now have known triangle inequality bounds, due to the previously solved set of rij, repeat until all rij have been solved21.

7.3. The Bond Breakage Conjecture. A packing of n spheres can be formed by (i) taking an n − m sphere packing, breaking a contact (or bond), adding m new spheres, and forming the appropriate contacts to complete the packing, or by (ii) breaking one bond of an n sphere packing and reforming another. From this property, we propose the following theory.

Bond Breakage Conjecture: All packings of n spheres can be obtained by breaking one bond and reforming another in every possible way. For any packing, there exists an m step path, of breaking one contact and reforming another, that will form that packing out of another packing with 3n−6 contacts. Each of the m steps will correspond to an n-particle packing. The end points

20This also holds true when each particle has at least 2 contacts. 21We have tested this method on the new seed A’s for n ≤ 8, and have shown that it works; however, we have

not implemented it for up to n = 14.

![image 288](<2010-arkus-deriving-finite-sphere-packings_images/imageFile288.png>)

- 5
- 6


# d2’’ 1 4

# d1 = d2’ d2 = d1’ = d1’’

# 3 2

###### Figure 20. A New Seed and the General Triangular Bipyramid.

Here we show an example of how to apply the general triangular bipyramid to a new seed in order to determine its unknown distances. This new seed corresponds to the 6 particle octahedron. It has 3 unknown distances, r12, r34, and r56 (dashed black lines). The ﬁrst triangular bipyramid constructed consists of particles 1,2,3,4,5, and has unknown distances d1 and d2, corresponding to r34 and r12, respectively. Note that (d3 to d10 = R). The second triangular bipyramid consists of particles 1,2,3,4,6 and has unknown distances d 1,d 2 corresponding to r12,r34, respectively. The third triangular bipyramid consists of particles 1,2,4,5,6 and has unknown distances d 1,d 2 corresponding to r12,r56, respectively. Note that the ﬁrst two triangular bipyramids comprise 2 equations and 2 unknowns, and thus are alone suﬃcient to solve r12 and r34. Once these 2 distances are known, applying the third triangular bipyramid involves only 1 unknown distance, r56, and thus follows as applying the triangular bipyramid to an iterative packing.

of the path (i.e. which 3n−6 packing one begins with and which packing one ends up with) determine what value m takes. For every packing, there exists at least 1 other packing for which m = 1.

This suggests an alternative method for enumerating all packings of n spheres: construct just one 3n − 6 contact packing of n particles (this can easily be done, simply construct an n particle polytetrahedron for example), and then break and reform bonds in all possible ways. For each

packing, it is important to explore every combination of breaking and reforming a bond – i.e. to go down all paths, and not just one path.

We have conﬁrmed this conjecture up to as high as we have enumerated packings (n = 10) using the following algorithm: For every A that corresponds to a packing

1. For each 1 that appears in the A:

(a) Swap the 1 with an existing 0. Do this in every possible non-isomorphic way. (This is the mathematical analogue of physically breaking an existing bond and reforming a diﬀerent bond that was not present in that packing).

For each new A that is generated by swapping a 1 and a 0 (these are 1 bond away A’s, i.e. where m = 1),

- (i) Test for an isomorphism with the A’s of all other packings (i.e. all A’s other than the one being examined).
- (ii) If an isomorphism is found, stop the examination of this A, as it has been shown that there exists a 1 bond bath between the packing being examined and another packing22.


Thus implementing this algorithm computationally, we have proven that, for each n ≤ 10, every packing is a 1 bond distance away from at least 1 other packing of the same n. We have not proven this for n > 10, as we have not enumerated all packings of n > 10, but we suspect that this conjecture holds for all n.

Mapping out all possible 1 bond distances might be able to shed insight into the kinetic pathways of packings.

To implement the bond breakage conjecture into an improved method for enumerating sphere packings, the bonds must be broken and reformed intelligently, such that unphysical conformations are not explored. If all physical and unphysical conformations were to be explored, then we would simply return to the same computational problem we had with enumerating all non-isomorphic A’s. One should be able to break a bond and reform it only as is physically possible by calculating the 1 degree of freedom motion that is left over from the one broken bond. Furthermore, one can take advantage of symmetry to, a priori, not explore redundant (i.e. isomorphic) pathways of breaking and reforming bonds.

- 7.4. Extensions to Other Dimensions. The method presented here is, in large part, not dimension speciﬁc. The only step which is dimension speciﬁc is the set of geometrical rules used to solve A for D. However, at least for the triangular bipyramid rule (which solves for most of the packings), the geometrical rules can easily be modiﬁed to account for a diﬀerent number of dimensions, d. Once this is done, the same method can be used to solve for sphere packings of d = 3 dimensions.
- 7.5. ‘Lower Dimensional Packings’. While a packing of n spheres depends on the dimensionality of its embedding space, there exists a cutoﬀ number, m, for which the packing of n spheres remains constant for all d + i dimensions, i ≥ 1. For this m, the n spheres have accessed all dimensions possible to them, and so the embedding space becomes irrelevant. For example, for all d, the unique packing of 1 and 2 spheres is the singlet and doublet, respectively. For 3 spheres, the unique packing in 1 dimension is a linear connected chain of 3 spheres; whereas in 2 dimensions it


22If one is interested in examining all 1 bond paths that exist between all packings, then this same algorithm can be executed without this termination step to yield all possible 1 bond paths.

is the equilateral triangle. For d ≥ 2 however, the unique packing of 3 spheres remains the same, it is always the triangle. For 4 spheres, the unique packing in 2 dimensions is the di-triangle; whereas, in 3-dimensions it is the tetrahedron. It is generally true that packings of d + 1 particles remain the same for d or more dimensions23.

- 7.6. Patterns in Adjacencies and Distances. Does there exist a signature pattern in the A’s or D’s that signiﬁes a packing? In other words, is there a pattern in the distribution of adjacencies (i.e. number of contacts per particle and connections therein) and/or the distribution of distances that corresponds to packings? If such a pattern does exist, it could illuminate a more general method for solving for packings. It also might shed light on the spectrum of allowed solutions for the system of quadratic equations corresponding to the adjacency matrices – detailing which do and do not have real valued solutions in R3 satisfying D ≥ R.
- 7.7. Related Mathematical Problems.


- 7.7.1. Erd¨s Unit Distance Problem. The Erdo¨s unit distance problem (a.k.a. Erd¨os Repeated Distance Problem)24 was posed in 1946 by the Hungarian mathematician, Paul Erd¨os. It asks what the maximum number of unit (or repeated) distances that can connect n points in d dimensions is [19, 9]. This problem is still unsolved. Even in 2 and 3 dimensions, only upper and lower bounds are known [14, 26]. The solution to this problem in 3 dimensions, where the unit distance is also the minimum distance, would answer what the maximum number of contacts in any sphere packing is; thus giving the number of contacts corresponding to the ground state packing(s).
- 7.7.2. 3-Dimensional Rigidity. In solving adjacency matrices for both rigid and non-rigid packings that satisfy minimal rigidity constraints in 3-dimensions, this problem is directly related to determining whether a graph is rigid in 3-dimensions. Much work has been done in this ﬁeld [33, 13, 35, 12, 32, 22], as well as in other dimensions [40]. The existing work on rigidity may help to further inform sphere packings, and the work presented here may in addition be applicable to rigidity theory. In particular, it may allow for the development of a simple method for reading oﬀ whether a 3-dimensional graph is rigid or not. By the method presented here, a graph is determined to be non-rigid if there exists a continuum of solutions to A. However, if we can determine a signature pattern that corresponds to all non-rigid (but minimally-rigid) A’s, this would allow for a very simple determination of whether a 3D graph is rigid.
- 7.7.3. Solutions to Systems of Polynomial Equations. The method presented here is inherently solving a system of quadratic equations. Thus presenting an alternative analytical solution to this class of problems. Current standards in the ﬁeld for analytically solving systems of polynomial equations include Gr¨obner bases [11]; however, these are time-consuming and thus do not scale eﬃciently with the number of equations. The method presented here solves a certain class of polynomial equations eﬃciently for a relatively large number of equations. Is it possible to extend this method in order to more eﬃciently solve large systems of polynomial equations?


- 23We originally posed this as a question, but one of the reviewers of this paper pointed out that this was true

due to the fact that any d + 1 points are always contained in an aﬃne subspace of at most d dimensions (without loss of generality, one point can be taken to be the origin). Thus, the d + 1 points can only access d dimensions, and considering a higher than d dimensional space will not change the structures that they can form.

- 24Without loss of generality, a repeated distance can be called a unit distance, because one can always uniformly


rescale all distances such that the repeated distance is the unit distance. Put another way, ‘a unit’ can be given any value – here, the unit is simply given the value of the repeated distance.

7.7.4. Euclidean Distance Matrix Completion Problems. Given a symmetric matrix, M, where only certain elements are speciﬁed, the Euclidean distance matrix completion problem is to ﬁnd the unspeciﬁed elements of M that make M a Euclidean distance matrix. Euclidean distance matrix and positive semideﬁnite matrix completion problems are closely linked [36, 37, 38, 39, 31, 4]. In solving adjacency matrices for distance matrices, the method presented here is directly related and potentially directly applicable to the euclidean distance matrix completion problem and, by extension, to the positive semideﬁnite matrix completion problem.

8. Concluding Remarks

In this work, we present an analytical method for deriving all packings of n spheres. We carry out this derivation for n ≤ 10; where the set of n = 10 new seeds is preliminary, and all iterative packings of n = 10 spheres and all packings of n ≤ 9 spheres are potentially complete, save the numerical round-oﬀ error present from implementing this analytical method computationally.

We consider the derivation of these sphere packings to be the ﬁrst step in directing the selfassembly of spherical colloidal particles; where we have divided this problem up into 2 parts: (i) understanding what the system of colloids can self-assemble, (ii) deriving a mechanism to control that self-assembly. The derivation of all packings of n spheres gives us everything that a system of n colloidal particles can self-assemble, thus taking care of this ﬁrst step. Future work will detail the second step, which is the derivation of a mechanism that directs the self-assembly of the packings such that only one packing forms.

Beyond the problem of self-assembly, the results reported here are interesting in their own right. We ﬁnd many interesting properties from the sphere packings enumerated up to n = 10, as well as from the conjectured maximum contact packings of 11 ≤ n ≤ 20. Furthermore, the results are directly related to the physics of colloidal clusters, and may have applications to glassy systems and the nucleation of crystals. They are also directly related to unsolved problems in mathematics, such as the Erd¨os unit distance problem.

We thank John Lee for consultations in coding, and for writing code that (i) converted the packing output to latex format for appropriate display in appendix B, and (ii) interfaced the packing output with the rotational constant calculator website and with the mayavi2 graphing package so that the 10 particle point groups, symmetry numbers, and ﬁgures did not have to be generated manually. We also thank David Roach, Noam Elkies, and Marcus Roper for helpful discussions. We acknowledge support from the MRSEC program of the National Science Foundation under award number DMR-0820484, the NSF Division of Mathematical Sciences under grant number DMS-0907985, and DARPA under contract BAA 07-21.

References Cited

- [1] GNU Multiple Precision Arithmetic Library. http://gmplib.org/.
- [2] Multiple Precision Floating Point Computations with Correct Rounding. http://www.mpfr.org/.
- [3] Sage mathematical software, package entitled NICE. http://www.sagemath.org.
- [4] A. Y. Alfakih, A. Khandani, and H. Wolkowicz, Solving euclidean distance matrix completion problems via semideﬁnite programming, Comput. Optim. Appl, (1999).
- [5] N. Arkus, Theoretical approaches to self-assembly and biology, Unpublished PhD Thesis, Harvard University, (2009). http://people.seas.harvard.edu/∼narkus/assets/Thesis.pdf.zip.
- [6] N. Arkus, V. N. Manoharan, and M. P. Brenner, Directing the self-assembly of spherical colloidal nanoparticles, to be submitted to Nanoletters.
- [7] N. Arkus, V. N. Manoharan, and M. P. Brenner, Minimal energy clusters of hard spheres with short range attractions, Physical Review Letters, 103 (2009), p. 118303.
- [8] N. Arkus, V. N. Manoharan, and M. P. Brenner, Supplementary information, arXiv:1011.5412, (2011).
- [9] D. Avis, P. Erdos,¨ and J. Pach, Repeated distances in space, Graphs and Combinatorics, 4 (1988), pp. 207–217.
- [10] P. L. Biancaniello, A. J. Kim, and J. C. Crocker, Colloidal interactions and selfassembly using dna hybridization, Physical Review Letters, 94 (2005). 058302.
- [11] B. Buchberger, Grobner bases: A short introduction for systems theorists, Proceedings of EUROCAST, (2001), p. 1923.
- [12] R. Connelly, On generic global rigidity, in applied geometry and discrete mathematics, DIMACS Ser. Discrete Math. Theoret. Comput. Sci, (1991), pp. 147–155.
- [13] R. Connelly, E. D. Demaine, and G. Rote, Inﬁnitesimally locked self-touching linkages with applications to locked trees, in Physical Knots: Knotting, Linking, and Folding of Geometric Objects in 3-space, American Mathematical Society, 2002, pp. 287–311.
- [14] H. T. Croft, K. J. Falconer, and R. K. Guy, Problem Books in Mathematics: Unsolved Problems in Intuitive Mathematics, vol. II, Springer-Verlag, 1991.
- [15] A. D. Dinsmore, J. C. Crocker, and A. G. Yodh, Self-assembly of colloidal crystals, Current Opinion in Colloid and Interface Science, 3 (1998), pp. 5–11.
- [16] J. Doye and D. Wales, Structural consequences of the range of the interatomic potential

- a menagerie of clusters, J. Chem. Soc. Faraday Trans., 93 (1997), pp. 4233–4243.

- [17] J. P. K. Doye and F. Calvo, Entropic eﬀects on the structure of Lennard-Jones clusters, The Journal of Chemical Physics, 116 (2002), pp. 8307–8317.
- [18] J. P. K. Doye, A. A. Louis, I. Lin, L. R. Allen, E. G. Noya, A. W. Wilber, H. C. Kok, and R. Lyus, Controlling crystallization and its absence: proteins, colloids and patchy models, Physical Chemistry Chemical Physics, 9 (2007), pp. 2197–2205.
- [19] P. Erdos¨ , On sets of distances of n points, The American Mathematical Monthly, 77 (1970), pp. 738–740.
- [20] F. C. Frank, Supercooling of liquids, Proc. R. Soc. London, Ser. A, 215 (1952), pp. 43–46.
- [21] D. L. Freeman and J. D. Doll, Computational studies of clusters: Methods and results, Annual Review of Physical Chemistry, 47 (1996), pp. 43–80.
- [22] S. J. Gortler, A. D. Healy, and D. P. Thurston, Characterizing generic global rigidity, 2010.
- [23] G.-M. Greuel, G. Pfister, and H. Schonemann¨ , Singular 3-1-0 — A computer algebra system for polynomial computations, (2009). http://www.singular.uni-kl.de.


- [24] D. G. Grier, From dynamics to devices: Directed self-assembly of colloidal materials, Mrs Bulletin, 23 (1998), pp. 21–21.
- [25] R. B. Grossman, Point Groups. http://www.chem.uky.edu/research/grossman/stereo/ pointgroups.html.
- [26] L. Guth and N. H. Katz, On the erdos distinct distance problem in the plane, 2007. arXiv:1011.4105v1.
- [27] M. R. Hoare and J. McInnes, Statistical mechanics and morphology of very small atomic clusters, Faraday Disc. Chem. Soc., 61 (1976), pp. 12–24.
- [28] M. R. Hoare and P. Pal, Physical cluster mechanics - statistical thermodynamics and nucleation theory for monatomic systems, Adv. Phys., 24 (1975), pp. 645–678.
- [29] L. Hong, A. Cacciuto, E. Luijten, and S. Granick, Clusters of amphiphilic colloidal spheres, Langmuir, 24 (2008), pp. 621–625.
- [30] R. S. Hoy and C. S. O’Hern, Minimal energy packings and collapse of sticky tangent hard-sphere polymers, Physical Review Letters, 105 (2010), p. 068001.
- [31] H.-X. Huang, Z.-A. Liang, and P. M. Pardalos, Some properties for the euclidean distance matrix and positive semideﬁnite matrix completion problems, J. of Global Optimization, 25 (2003), pp. 3–21.
- [32] B. Jackson and T. Jordan´ , Connected rigidity matroids and unique realizations of graphs, Tech. Reports, (2003). www.cs.elte.hu/egres . ISSN 1587-4451.
- [33] B. Jackson and T. Jordan´ , The Dress conjectures on rank in the 3-dimensional rigidity matroid, Adv. Appl. Math., 35 (2005), pp. 355–367.
- [34] E. Lauga and M. P. Brenner, Evaporation-driven assembly of colloidal particles, Phys. Rev. Lett., 93 (2004).
- [35] M. Laurent, Cuts, matrix completions and graph rigidity, Mathematical Programming, 79

(1997), pp. 255–283.

- [36] M. Laurent, A connection between positive semideﬁnite and euclidean distance matrix completion problems, Linear Algebra and its Applications, 273 (1998), pp. 9–22.
- [37] M. Laurent, Polynomial instances of the positive semideﬁnite and euclidean distance matrix completion problems, SIAM J. Matrix Anal. Appl, 22 (1998), pp. 22–874.
- [38] M. Laurent, Matrix completion problems, in The Encyclopedia of Optimization, Kluwer, 2001, pp. 221–229.
- [39] M. Laurent, S. Poljak, and F. Rendl, Connections between semideﬁnite relaxations of the max-cut and stable set problems, Mathematical Programming, 77 (1995).
- [40] L. Lovasz and Y. Yemini, On generic rigidity in the plane, SIAM J. Algebraic Discrete Methods, 3 (1982), pp. 91–98.
- [41] V. N. Manoharan, M. T. Elsesser, and D. J. Pine, Dense packing and symmetry in small clusters of microspheres, Science, 301 (2003), pp. 483–487.
- [42] B. McKay, Practical graph isomorphism,, Congressus Numerantium, 30 (1981), pp. 45–87.
- [43] G. Meng, N. Arkus, M. P. Brenner, and V. N. Manoharan, The free energy landscape of clusters of attractive hard spheres, Science, 327 (2010), pp. 560–563.
- [44] H. Reichert, O. Klein, H. Dosch, M. Denk, V. Honklmaki, T. Lippmann, and G. Reiter, Observation of ﬁve-fold local symmetry in liquid lead, Nature, 408 (2000), pp. 839–841.
- [45] C. P. Royall, S. R. Williams, T. Ohtsuka, and H. Tanaka, Direct observation of a local structural mechanism for dynamic arrest, Nat. Mater., 7 (2008), pp. 556–561.


- [46] T. W. Shattuck, Rotational constant calculator, Colby College Chemistry. http://www.colby.edu/chemistry/PChem/scripts/ABC.html.
- [47] H. W. Sheng, W. K. Luo, F. M. Alamgir, J. M. Bai, and E. Ma, Atomic packing and short-to-medium-range order in metallic glasses, Nature, 439 (2006), pp. 419–425.
- [48] N. J. A. Sloane, R. H. Hardin, T. D. S. Duff, and J. H. Conway, Minimal-energy clusters of hard spheres, Disc. Comp. Geom., 14 (1995), pp. 237–259.
- [49] D. Y. Wang and H. Mohwald, Template-directed colloidal self-assembly - the route to ‘top-down’ nanochemical engineering, J. Materials Chem., 14 (2004), pp. 459–468.
- [50] G. M. Whitesides and B. Grzybowski, Self-assembly at all scales, Science, 295 (2002), pp. 2418–2421.


##### APPENDIX A: INDIVIDUAL GEOMETRICAL RULES

In this appendix, we derive the individual geometrical rules that were used to solve A for D. 1. Rules Sufficient to Solve All 6 Particle Packings

- Rule 1: The ﬁrst rule is the most simple; it states that any 2 intersection circles can not intersect in

> 2 points (ﬁg 2).

![image 289](<2010-arkus-deriving-finite-sphere-packings_images/imageFile289.png>)

(a) 2 intersections of intersection circles

![image 290](<2010-arkus-deriving-finite-sphere-packings_images/imageFile290.png>)

(b) 1 intersection of 2 intersection circles

![image 291](<2010-arkus-deriving-finite-sphere-packings_images/imageFile291.png>)

(c) 0 intersections of intersection circles

Figure 1. Intersecting Intersection Circles

This rule is identiﬁed by the following adjacency matrix pattern: Any 2 of the set {Ajk,Ajp,Akp} equal 1, and ∃ > 2 i’s for which Aij = Aik = Aip = 1.

- Rule 2: The 2nd rule calculates the distance between the 2 points of intersection of 3 mutually intersect-


ing intersection circles associated with a triplet (ﬁg 2). If a particle lies at one of the intersection points, this forms a 4 particle packing (the tetrahedron), for which all distances = R. If 2 particles lie at each of the intersection points, this forms a 5 particle packing – the distance between these 2 points is the only distance > R.

The non-unit distance (where the ‘unit distance’ is = R) of the 5 particle packing is calculated as follows (ﬁg 4): A trimer forms an equilateral triangle with sides of length R. The intersection circles have a radius of (√3/2)R, and the points, corresponding to the particles’ centers, lie on the circumference of these intersection circles. The centers of the intersection circles lie at the midpoint of each of the triangle sides (of length R). Thus, we can draw a line segment of length (√3/2)R emanating from the points of the equilateral triangle to the midpoints of the opposite line segment. (See ﬁgure 3). The intersection of these line segments corresponds to the in-plane location of where the intersection circles intersect – i.e. projecting the intersection points to the face of the equilateral triangle. For example, in the pentamer in ﬁgure 3b (i.e. the 5 particle packing), the center triangle corresponds to the in plane triangle we are considering, and the top and bottom points correspond to the 2 intersection points of the 3 intersection circles. As all of these line segments = R (as they represent particles touching each other), all of the triangles formed in this pentamer are equivalent equilateral triangles oriented diﬀerently in 3-dimensional space. Let us consider the 3rd triangle in ﬁgure 3a; using right triangle math, we can calculate what a is:

![image 292](<2010-arkus-deriving-finite-sphere-packings_images/imageFile292.png>)

Figure 2. The Intersections of 3 Intersection Circles

π 6

a

tan

=

- 1

- 2R


a

1 √3

=⇒

=

- 1

- 2R


1 2√3

=⇒ a =

R

Because all of the triangles in the pentamer are equivalent, we can use a to construct the triangle in ﬁgure 3b, where the (√3/2)R edge corresponds to the radius of one of the in-plane intersection circles. Thus, the (√3/2)R edge connects one of the in-plane triangle edges to the point of intersection of the 3 in-plane intersection circles. The 1/2h edge corresponds to the line segment connecting the point of intersection of the 3 circles of intersection to the in-plane projection of this intersection point; and therefore represents 1/2 the length between the 2 intersection points (as the in-plane trimer lies at the midpoint of the 2 intersection points). This forms a right triangle,

![image 293](<2010-arkus-deriving-finite-sphere-packings_images/imageFile293.png>)

(a)

![image 294](<2010-arkus-deriving-finite-sphere-packings_images/imageFile294.png>)

(b)

Figure 3. Calculating the Distance Between the 2 Points of Intersection of the 3 Intersection Circles of a Trimer (or Triplet).

and once again we can use right triangle math to solve for h:

√3 2

2

2

- 1

- 2√3


- 1

- 2


R

h

R

+

=

2

(15)

|h = 2<br><br>2<br><br>3<br><br><br>R|
|---|


=⇒

Thus, the solution to an adjacency matrix corresponding to a 5 particle packing, written in terms of a distance matrix, is









- 0 1 1 1 1
- 1 0 1 1 1


- 0 1 1 1 1
- 1 0 1 1 1 1 1 0 1 1 1 1 1 0 0 1 1 1 0 0


- 1 1 0 1 1
- 1 1 1 0 2 23

- 1 1 1 2 23 0


−→

 

 

 

 

This rule can be identiﬁed by the following adjacency matrix pattern: Aij = Aik = Akj = 1, and ∃ 2 p for which Api = Apj = Apk = 1. This rule solves for the distance

between those 2 p, for ex. if p = l,m, then Dlm = 2 23R.

![image 295](<2010-arkus-deriving-finite-sphere-packings_images/imageFile295.png>)

Figure 4. 4 Touching Points on an Intersection Circle

- Rule 3: This follows from rule 2, namely as we have calculated that the distance between the 2 inter-

section points of 3 mutually intersecting intersection circles is 2 2/3R, then that distance can not = R. Any adjacency matrix implying that distance = R is unphysical.

This rule can be identiﬁed by the following adjacency matrix pattern: Aij = Aik = Akj = 1, ∃ 2 p for which Api = Apj = Apk = 1 (i.e. the same pattern as in rule 2), and the A element associated with those 2 p’s is 1 (i.e. if p = q,z then Aqz = 1).

- Rule 4: This rule calculates the distance between the two end particles of a total of 4 particles that


lie on a circle of intersection, where particle i + 1 touches particle i (1 ≥ i ≤ 4). (See ﬁgure 4). From the ﬁgure, we can see that this scenario forms 3 equivalent isoscoles triangles, which we will be able to use to calculate the distance, r, between the 2 end particles (see ﬁgure 5). We can calculate θ from this triangle, either via the law of cosines

  

  

√3

√3

2

2

###### − R2 2

+

2 R

2 R

θ = cos−1

√3

√3

2 R

2 R

1 3

=⇒ θ = cos−1

or via right triangle math:

- 1

- 2


θ) =

sin(

- 1

- 2R


√3

2 R

=⇒ θ = 2sin−1

1 √3

![image 296](<2010-arkus-deriving-finite-sphere-packings_images/imageFile296.png>)

![image 297](<2010-arkus-deriving-finite-sphere-packings_images/imageFile297.png>)

Figure 5. Solving the Long Distance Between 4 Touching Points on an Intersection Circle

and both of these expressions for θ are equivalent (both ≈ 1.23096).

Using θ, we can calculate the desired distance, r. The new angle, φ, depicted in ﬁgure 5 is given by 2π − 3θ:

1 √3 and thus r is given by

1 3

= 2π − 6sin−1

φ = 2π − 3cos−1

- 1

- 2r


- 1

- 2


φ =

sin

√3

2 R

√3 2

1 √3

R sin π − 2sin−1

=⇒ r = 2

√

1 √3 and as

3R sin 3sin−1

=

5 3√3 r is given by

1 √3

sin 3sin−1

=

|r =<br><br>5 3<br><br>R|
|---|


(16) Therefore, the distance between particle 1 and 4, where particle i + 1 touches particle i for i = 1 to i = 4, and particles 1 to 4 all touch the same 2 particles is always 5/3R.

![image 298](<2010-arkus-deriving-finite-sphere-packings_images/imageFile298.png>)

Figure 6. 4 Intersection Circles Intersecting at 2 Points

The red points in the ﬁrst ﬁgure are the points of intersection of the 4 intersecting circles. The dashed parts of the circle indicate that part of the circle goes into the page, while the solid lines come out of the page. The second ﬁgure, drawn with one intersection circle not shown, is added for clarity, so that the intersection points of the intersection circles can become more apparent.

This rule can be identiﬁed by the following adjacency matrix pattern: Aij = 1, and ∃ 4 k for which Aik = Ajk = 1, and 3 Apq = 1 amongst the 4 k (i.e. if k = p,q,l,m, then Apq = Aql = Alm = 1), and the distance Dpm = 53R).

- Rule 5: Following from rule 4, we know that any adjacency matrix implying that the above distance

= R is unphysical. This rule can be identiﬁed by the following adjacency matrix pattern: The same pattern as in rule 4, where Apm = 1 also.

- Rule 6: This rule derives the distance between the 2 intersection points of the mutual intersection of 4


intersection circles associated with 4 points (ﬁg 6). As mentioned before, m intersection circles can intersect at 1, 2, or 0 points. As we can see from ﬁgure 6, when 4 intersection circles intersect at 2 points, they must be associated with a 2-dimensional square (in fact, we will see later that this is generally true - if it is possible for m intersection circles to intersect at 2 points, they will only intersect at 2 points when associated with a regular m-gon lying in a 2 dimensional plane. And 2 ≤ m ≤ 5, if m ≥ 6 the m associated intersection circles can intersect in at most 1 point (see rule 13). If 4 intersection circles are not associated with a square, then they can only intersect at 1 or at 0 points.

We can calculate the distance between the 2 points of intersection of 4 mutually intersecting circles by constructing an isosceles triangle that connects one of the intersection points to the center of 2 of the intersection circles - such a triangle is shown in ﬁgure 7. We know the lengths of all of the sides of this triangle, as the 2 equivalent lengths are the radius of the intersection circle, (√3/2)R, and the base length is the distance between 2 touching particles (or equivalently the radius of the neighbor sphere), R. The height of this triangle corresponds to half the distance between the 2 points of intersection, thus we can use right triangle math to calculate the desired

![image 299](<2010-arkus-deriving-finite-sphere-packings_images/imageFile299.png>)

Figure 7. Solving for the Distance Between 2 Intersection Points of 4 Mutually Intersecting Intersection Circles Associated with 4 Points.

distance:

- 1

- 2


R

2

+

- 1

- 2


h

2

=

√3 2

R

2

1 4

- 3

- 4


1 4

R2 +

h2 =

R2

3 4 −

1 4

=⇒ h = 4

R

|h =<br><br>√<br><br>2R|
|---|


=⇒

(17)

Thus, the distance between 2 points of intersection of 4 intersection circles must be √2R, if any adjacency matrix violates this property, by setting this distance = R, then it is physically impossible.

This rule can be identiﬁed by the following adjacency matrix pattern:

∃ a closed 4 ring, Aij = Ajk = Akp = Api = 1, where the cross particles don’t touch, Aik = Ajp = 0, and 2 particles touch all points in the 4 ring, Amj = Amk = Amp = Ami = 1 for two m’s. This rule then solves for the distance between those 2 m’s, i.e if m = z,s then Dzs = √2R.

The following adjacency matrix contains this pattern: 



0 0 1 1 1 1 0 0 1 1 1 1 1 1 0 0 1 1 1 1 0 0 1 1 1 1 1 1 0 0 1 1 1 1 0 0

 

 

###### Rule 7:

As just mentioned, following from rule 6, any adjacency matrix that implies the distance between the 2 intersection points of 4 mutually intersecting intersection circles = R is unphysical.

![image 300](<2010-arkus-deriving-finite-sphere-packings_images/imageFile300.png>)

Figure 8. 5 Points on an Intersection Circle. (The ‘?’ distance = the unknown distance r.)

This rule can be identiﬁed by the following adjacency matrix pattern: The same pattern as in rule 6, and the adjacency matrix element between those 2 m’s is 1 (i.e. if m = q,l, then Aql = 1 also).

2. Rules Sufficient for 7 Particle Packings

The following geometrical rules, in addition to the rules used to solve the 6 particle packings, are suﬃcient to solve for all 7 particle packings. Rule 8:

We have calculated the long distance between 4 and between 3 touching points on an intersection circle (rules 2 and 4); for 7 particle packings, we must also know the long distance between 5 touching points on an intersection circle (i.e. the distance between points 1 and 5, where point i + 1 touches point i for 1 ≤ i ≤ 5) - see ﬁgure 8.

We make this calculation as we did for the one with 4 touching points on an intersection circle, but here the relevant angle of the triangle that will allow us to calculate the distance r is

θ = 2π − 4cos−1

1 3

= 2π − 8sin−1

1 √3

and thus r is given by

- 1

- 2r


- 1

- 2


sin

θ =

√3

2 R sin π − 4sin−1

- 1

- 2r


1 √3

=

√3

2 R 4√2 9

- 1

- 2r


=

√3

2 R

|r =<br><br>4√6 9<br><br>R|
|---|


=⇒

- (18)

This rule can be identiﬁed by the following adjacency matrix pattern: Aij = 1, and ∃ 5 k for which Aik = Ajk = 1, and 4 Apq = 1 amongst the 5 k (i.e. if k = p,q,l,m,z, then Apq = Aql = Alm = Amz = 1). This rule solves Dpz = 4

√6

9 R.

- Rule 9: Following from rule 8, we can see that 5 particles can not touch the same 2 particles and all

touch each other, as the distance between the 4th and 5th points lying on an intersection circle is

= 4

√6

9 R ≈ 1.08866R, and for 5 particles to touch the same 2 particles, this distance would have to equal exactly R. Thus any A implying this distance = R is unphysical.

This rule can be identiﬁed by the following adjacency matrix pattern: The same pattern as in rule 8, but 5 Apq = 1 amongst the 5 k – i.e. Azp = 1 also.

- Rule 10: Also following from rule 8, we can see that no more than 5 points can ﬁt on an intersection


circle (i.e. no more than 5 points can mutually touch a dimer), as only slightly more than 5 points can ﬁt on an intersection circle, and 6 points can not ﬁt.

We can calculate exactly how many points a distance R apart can ﬁt on an intersection circle by dividing the circumference of the entire intersection circle by the arc length swept out by one of the isosceles triangles created by 2 particles lying on the intersection circle. (See ﬁgure 8). The formula for the arc length is

S = rθ

where r is the radius of the circle, θ the angle between 2 radial line segments, and S is the arc length. Thus the number of points a distance R apart that can ﬁt on an intersection circle is

2π

√3

2 R

√3

2 R cos−1 1

3

=

π cos−1 1

3

- (19) ≈ 5.1043


![image 301](<2010-arkus-deriving-finite-sphere-packings_images/imageFile301.png>)

Figure 9. Calculating the Distance Between 2 Intersection Points of 5 Mutually Intersecting Intersection Circles Associated with 5 Points.

(As an aside, cos−1(1/3) = 2sin−1(1/√3) = 2tan−1(√2/2), and we could have expressed the angle by any one of these).

Thus any A implying that > 5 points lie on an intersection circle is unphysical.

This rule can be identiﬁed by the following adjacency matrix pattern: Aij = 1, and ∃ > 5 k for which Aik = Ajk = 1.

###### Rule 11:

As we did previously with the mutual intersection of 4 intersection circles (rule 6), we will now calculate the distance between the 2 intersection points of 5 mutually intersecting intersection circles. 5 circles of intersection can only intersect at 2 points if they are associated with a 2-dimensional pentagon (see ﬁgure 9). To calculate the distance between these 2 points of intersection, we can construct the triangle that connects one of the points of intersection to the centers of one of the intersection circles (shown in the ﬁgure). The base of this constructed triangle, a, is the apothem of a regular pentagon. We can calculate the apothem of the regular pentagon via the right triangle depicted in ﬁgure 10 (the formula for the apothem is also well known, so one could alternatively simply look it up). The interior angle of the pentagon, φ (ﬁg 10), is given by

(n − 2)π n

3 5

φ =

=

π

and the angle associated with the right triangle used to calculate the apothem is φ/2. Therefore, the apothem, calculated via right triangle math, is given by

tan

3 10

π =

=⇒ a =

a

- 1

- 2R


1 + √5 2 10 − 2√5

R

![image 302](<2010-arkus-deriving-finite-sphere-packings_images/imageFile302.png>)

Figure 10. The Apothem and Interior Angle of the Pentagon.

Now that we know a, we can calculate the distance between the 2 points of intersection, h, via right triangle math:

√3 2

2

2

- 1

- 2


a2 +

h

R

=

1 + √5 2 10 − 2√5

2

3 4

1 4

h2 =

R2

R

+

1 + 2√5 + 5 10 − 2√5

- 3

- 4


1 4

1 4

h2 =

R2

R2 +

1 4

2 √5

1 4

- 3

- 4


R2 +

h2 =

R2

1 +

2 √5

- 3

- 4 −


1 4

=⇒ h = 4

1 +

R

(20)

=⇒

|h = 2 −<br><br>2 √5<br><br>R|
|---|


This rule can be identiﬁed by the following adjacency matrix pattern:

∃ a closed 5 ring, Aij = Ajk = Akp = Apz = Azi = 1, where the cross particles don’t touch, Aik = Ajp = Akz = Api = Ajz = 0, and 2 particles touch all points in the 5 ring, Amj = Amk = Amp = Amz = Ami = 1 for two m’s. This rule identiﬁes the distance between the

2 m’s (i.e. if m = l,y this rule gives Dly = 2 − √25R). Rule 12:

Related to rule 11, the distance between the vertices of the pentagon will be the distance between the non-touching pairs amongst the 5 particles that have intersection circles mutually intersecting at 2 points (Dik,Djp,Dkz,Dpi,Djz from rule 11). This distance can be calculated from the triangle in ﬁgure 11. We can solve for the distance, d, by using right triangle math or by using the law of

![image 303](<2010-arkus-deriving-finite-sphere-packings_images/imageFile303.png>)

Figure 11. A Triangle Within the Pentagon

cosines, here we’ll use the law of cosines:

3 5

d = R2 + R2 − 2R2 cos

π

√

1 4 −1 +

= R2 + R2 − 2R2 −

5

|d =<br><br>3 + √5 2<br><br>R|
|---|


=⇒

(21) This rule can be identiﬁed by the following adjacency matrix pattern: The same pattern as in rule 11, but this rule identiﬁes the distances between the cross particles; Dik = Djp = Dkz = Dpi = Djz = 3+

√5

2 R

- Rule 13: 6 or more mutually intersecting intersection circles can only intersect at one point. A regular


m-gon is the limiting case where m intersection circles will intersect at 2 points, if they can. For 3, 4, and 5 particles, this is possible. For ≥ 6 particles however, this is not. The longest distance between the non-touching particles of a regular hexagon, whose sides are length R, is 2R. (See ﬁgure 12). The interior angle of a regular n-gon is

(n − 2)π n Thus, φ here is

φ =

2 3

φ =

π

The angles associated with the equivalent sides of the isosceles triangles formed by the n-gon is ((n − 2)/2n)π, which implies that θ is given by

(n − 2)π n

θ = π −

1 3

=

π

![image 304](<2010-arkus-deriving-finite-sphere-packings_images/imageFile304.png>)

Figure 12. The Hexagon

(see ﬁg 12) and we can see that h is indeed equal to 2R, from right triangle math (we could also have done this, as usual, from the law of cosines):

- 1

- 2R


1 2

θ =

sin

- 1

- 2h


R h

1 6

π =

sin

R h

1 2

=

(22) =⇒ h = 2R

This distance is equal to twice the distance of 2 touching particles (i.e. to the diameter of the neighbor sphere), and thus we can see that one particle ﬁts right at the center of the regular hexagon, showing us that 6 mutually intersecting intersection circles can only intersect at one point (as only 1 point can touch all 6 points of the hexagon).

Put another way, we can calculate that the height of one of these isoscoles triangles is = (√3/2)R, thus implying that the distance from the center of an intersection circle associated with one of the hexagon edges is a distance √3R away from the center of an intersection circle associated with the opposite edge. Therefore, the distance between the center of the intersection circle and the intersection point of the intersection circles is (√3/2)R, and thus the ‘height between the 2 intersection’ points must be 0. On the other hand, we can see that the distance between the longest non-touching vertices of a regular septagon is > 2R (not shown here), and thus 7 in-plane intersection circles can not all intersect each other. Of course, once we allow 7 or more intersection circles to arrange themselves in 3 dimensional space, then they can mutually intersect at one point.

![image 305](<2010-arkus-deriving-finite-sphere-packings_images/imageFile305.png>)

![image 306](<2010-arkus-deriving-finite-sphere-packings_images/imageFile306.png>)

![image 307](<2010-arkus-deriving-finite-sphere-packings_images/imageFile307.png>)

(a) (b) (c) Figure 13. A Closed 5 Ring Constrained to Surround a Dimer

Thus, so far we have established that 6 or more intersection circles can mutually intersect at no more than 1 point. 13 intersection circles can not mutually intersect - this is the kissing number limit. Thus, 2-5 intersection circles can mutually intersect at 2 points, 6-12 intersection circles can mutually intersect at 1 point, and > 12 intersection circles can not mutually intersect.

In conclusion, this rule states that any adjacency matrix implying that ≥ 6 intersection circles mutually intersect at 2 points is unphysical. This rule can be identiﬁed by the following adjacency matrix pattern:

∃ 2 m for which Amj = 1 for ≥ 6 j where ≥ 6 adjacency matrix elements amongst the j = 1. For example, j = i,l,p,q,z,y and Ail = Alp = Apq = Aqz = Azy = Ayi = 1 (i.e. there are 6 j and a 6 ring is formed).

- Rule 14: This rule states that a closed 5 ring can not be conﬁned to surround a dimer. It is a more

general form of the rule stating that the 5 points of a closed 5 ring can not all touch the same dimer (rule 9). The diﬀerence is that this rule does not require that all 5 points be touching the dimer, simply that it make enough contacts with the dimer such that it is conﬁned to surround it; therefore forcing one distance to be < R, and thus implying particle overlap (see ﬁg 13).

This rule can be identiﬁed by the following adjacency matrix pattern: A violation occurs if

Akl = Alp = Apq = Aqm = Amk = 1 (closed 5 ring) and Aij = 1 (the dimer)

and one point in the dimer forms 3 contacts with the closed 5 ring, where 2 of the contacts are adjacent: Aiq = Aik = Ail = 1. And the other point in the dimer (here j) touches the 2 points of the 5 ring not touched by the other point (here i), Ajm = Ajp = 1; or touches one point not touched by i, and touches one of the adjacent contacts i makes, Ajm = Ajl = 1 or Ajk = Ajp = 1. (See ﬁgure 13). If these conditions are satisﬁed, then the 5 ring is constrained to surround the dimer, and the conformation is unphysical as it implies a distance < R.

- Rule 15:


![image 308](<2010-arkus-deriving-finite-sphere-packings_images/imageFile308.png>)

Figure 14. 2 Points Constrained to Opposite Sides of a Closed 4 Ring

2 points conﬁned to opposite sides of a closed 4 ring can not touch (see ﬁgure 14).

This rule can be identiﬁed by the following adjacency matrix pattern:

If Aki = Ail = Alj = Ajk = 1 (a closed 4 ring) and Akm = Aml = Ajp = Api = 1 (2 points, m and p, are constrained to opposite sides of the 4 ring)

=⇒ Dmp > R (i.e. Amp = 1 – the particles can not touch) If Amp = 1, this adjacency matrix is unphysical.

###### Rule 16:

This rule calculates the non-touching distances between one point added to an octahedron (See ﬁgure 15). This is the distance, for example, between points i and j, rij. Particles i, q, and j all lie on the p,k intersection circle, Ipk. Thus, we can calculate rij by determining the angle between rim and rjm, where m is the center of Ipk. We can determine this angle, θ, simply by summing θ1 and θ2. (We can simply sum the angles here because all of the relevent line segments, rim, rqm, rjm, and rij, necessarily lie in the same plane, as they all lie on the plane deﬁned by the p,k intersection circle).

θ1 is, as before, given by

1 3

θ1 = cos−1

(Note that this is the dihedral angle of a tetrahedron). θ2 is the dihedral angle of an octahedron, and is given by

Thus, θ is given by

1 3

θ2 = cos−1 −

θ = θ1 + θ2 = cos−1

= π

1 3

1 3

+ cos−1 −

![image 309](<2010-arkus-deriving-finite-sphere-packings_images/imageFile309.png>)

Figure 15. A Particle Added to an Octahedron Thus, rim and rmj form a straight line, and rij is simply the sum of these 2 line segments: rij = rim + rmj =

√3 2

√3 2

√

R +

R =

- (23) 3R


Note that, due to the symmetry of this structure, the distance between i and any point that i does not touch is = √3 (i.e. rij = the distance between i and both of the unlabeled points in the octahedron also).

This rule can be identiﬁed by the following adjacency matrix pattern: The same pattern as in rule 6 (keeping in mind that the dummy variables used there do not correspond to the dummy variables shown in ﬁg 15), and ∃ 1 particle, i, that touches any trimer within the octahedron – for example Aiq = Aik = Aip = 1 (where q,p,k can be identiﬁed as a trimer because Aqp = Aqk = Apk = 1). In this case Diz = √3R, where z are the 3 points that are not part of the trimer to which i is attached, i.e. z = j and the other 2 unmarked points in ﬁgure 15.

###### Rule 17:

The long distance, rij, between a particle added to the side of 3 connected tetrahedron (see ﬁgure 16) can be derived via spherical trigonometry. A spherical triangle is shown in ﬁgure 17. Just as in standard trigonometry, there are spherical analogues to the law of cosines and the law of sines. In the ﬁgure, we can see that triangles OAC, OAB, and OBC form the spherical triangle ABC. a is the arc length opposite the angle a (i.e. the arc length associated with the side BC), b is the arc opposite the angle b (i.e. associated with the side AC, and c is the arc length opposite c (associated with the side AB). a is the angle BOC (opposite vertice A), b is the angle AOC (opposite vertice B), and c is the angle BOA (opposite vertice C). The arc length, S, is by deﬁnition given by

S = rθ

![image 310](<2010-arkus-deriving-finite-sphere-packings_images/imageFile310.png>)

###### Figure 16. A Particle Added to the Side of 3 Connected Tetrahedron

![image 311](<2010-arkus-deriving-finite-sphere-packings_images/imageFile311.png>)

b

C

A

- b’ O
- c’ a’


c a

B

###### Figure 17. A Spherical Triangle

###### where r is radius of the sphere and θ is the angle swept out by the arc length. Therefore

- a = Ra
- b = Rb
- c = Rc


###### where R is the radius of the sphere, and O is the center of the sphere. Thus, R is equal to the line segments OA, OB, and OC. (Note that, by convention, R is often taken to = 1 without loss of generality, which sets the arc length equal to the angle – so that a = a and so on...). A, B, and C are taken both to be the vertices of the spherical triangle, as well as the dihedral angle between the relevant triangles, so that

- A is the dihedral angle between triangles OAC & OAB ( OAC and OAB)
- B is the dihedral angle between OAB & OBC
- C is the dihedral angle between OBC & OAC


j

i

P

q

k

Figure 18. The Spherical Triangles Associated with the Conformation in Figure 16

The conformation we are considering here forms 2 adjacent spherical triangles (see ﬁgure 18). We know the following arc lengths of the spherical triangles and their associated line segments: iq, qk, ik, jk. The only line segment we don’t know is ij, for which we aim to solve. We also know the following angles (∠): ∠ipq, ∠qpk, ∠kpj. The only angle we do not know is ∠ipj, which we will need in order to solve for rij.

We can use the spherical law of cosines to calculate the associated dihedral angles. We will use the following form of the spherical law of cosines

- (24) sinb sinc cosA = cosa − cosb cosc Ultimately, we need to calculate the dihedral angle between ipk and jpk, as this will allow us to back out what ∠ipj is, which we can then use to calculate the unknown distance rij. In spherical ikj, the dihedral angle between between ipk and jpk, ∠ipj, and rij are unknown. This corresponds to both A and a being unknown in the spherical rule of cosines (eqn 24). Thus


we can not immediately apply this equation to solve for rij. We can however use spherical jqk to calculate the dihedral angle between ipk and jpk, as this dihedral angle will = the dihedral angle between ipk and kpq + the dihedral angle between kpq and jpk, and spherical

jqk will allow us to calculate the dihedral angle between kpq and jpk. (We already know the dihedral angle between ipk and kpq; this is just twice the dihedral angle of a tetrahedron).

Thus, let us consider spherical jqk; here the vertices of the spherical triangle (ﬁg 17) correspond to the following points, A = k, B = j, C = q. Thus, A is the dihedral angle between jpk and kpq, a is ∠jpq, b is ∠kpq, and c is ∠jpk. We know all of these values except for A, they

are:

- a = ∠jpq =

π 3

- b = ∠kpq =

π 3

- c = ∠jpk = cos−1 −7 18


the ﬁrst two angles are π/3 as they are associated with equilateral triangles, and the last angle is derived from the isosceles jpk, where rjk = (5/3)R has been calculated earlier in rule 4, and rjp = rpk = R. So, from the spherical law of cosines for spherical jqk, we have

sin cos−1 −7 18

cos cos−1 −7

π 3

π 3 − cos

π 3

sin

cosA = cos

18 √3 2

5√11 18

−7 18

1 2 −

- 1

- 2


cosA =

5√33 36

−7 36

1 2 −

cosA =

25 · 36 36 · 5√33 A = cos−1

=⇒ A = cos−1

5 √33 ≈ .514806

This then implies that the dihedral angle between ipk and jpk, φ, is given by φ = 2cos−1

1 3

5 √33

+ cos−1

where 2cos−1(1/3) is the dihedral angle between kpq and ipk (which is double the dihedral angle of a tetrahedron). Now, we can calcualte ∠ipj from the spherical law of cosines for the spherical ikj, where the vertices of the spherical triangle (ﬁg 17) correspond to the following points, A = k, B = j, C = i. Thus,

- b = ∠ipk =

π 3

- c = ∠jpk = cos−1 −7 18


A = dihedral angle between ipk and jpk = φ = 2cos−1

1 3

+ cos−1

5 √33

###### and a = ∠ipj is unknown, and we will solve for it:

sin cos−1 −7 18

cos cos−1 −7

1 3

5 √33

π 3

π 3

cos 2cos−1

+ cos−1

= cosa − cos

sin

18 √3 2

5√11 18

7 36 5√33 36

5 √33

1 3

cos 2cos−1

+ cos−1

= cosa +

5 √33

1 3

7 36

+ cos−1

cos 2cos−1

= cosa +

53 54

=⇒ a = cos−1 −

≈ 2.94884

###### and so, now that we have ∠ipj, we can use the regular law of cosines to calculate rij:

###### 53 54

###### =⇒ rij = R2 + R2 − 2R2 cos cos−1 −

###### (25)

###### =⇒

- 53

- 54


###### = 2R2 − 2R2 −

###### 53 27

###### = 2 +

###### R

###### 107 27

###### =

###### R

|rij =<br><br>1 3<br><br>107 3<br><br>R|
|---|


###### This rule can be identiﬁed by the following adjacency matrix pattern:

###### Aij = 1, and ∃ 4 points that touch both i and j; Api = Apj = Aqi = Aqj = Ali = Alj = Ami = Amj = 1. Where 3 consecutive contacts are made amongst these 4 points; Apq = Aql = Alm = 1 (i.e. the same pattern as in rule 4). And ∃ another particle that touches the top or bottom of the left or right faces (i.e. that touches either trimer ilm, ipq, jlm, or jpq. Take, for example, the

###### particle z, where Aiz = Alz = Amz = 1, then this rule identiﬁes Dzp = 13 1073 R.

###### Note, this packing is an enantiomer: i.e. there exist left and right handed conﬁgurations of this structure, which are diﬀerent via chiral symmetry, but are not diﬀerent in terms of their distance matrices.

###### Rule 18: Following from rule 17, any adjacency matrix that implies rij = R is unphysical.

###### This rule can be identiﬁed by the following adjacency matrix pattern: The same pattern as in rule 17, but where Azp = 1 also.

3. Some Comments (Non-Uniqueness of Rules)

- • Rules 1 - 7 are suﬃcient to solve for packings of n ≤ 6. For n = 7, we also need rules 8-18. And in fact, only rules 1, 2, 4, and 6 were actually used to calculate the 6 particle packings (as the application of these rules alone were suﬃcient to either completely solve or eliminate as unphysical all adjacency matrices). And for 7 particles, only rules 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 16, and 17 were used (where some combination of rules 3, 5, and 9 were used – as the way we’ve implemented this in the computer code, it lumps these rules together in the output as ‘matrices were unphysical because they implied that there were > 2 points on an intersection circle that all touched each other’).
- • Rule 17 calculates the new distance generated by adding 1 particle to a packing of 6 particles that has already been solved. From derivations of this nature, it seems that it should be possible (and it would certainly be advantageous) to derive 1 general rule that solves for all unknown distances – at least in the most simple case of adding 1 particle to a packing of n particles that has already been solved. The triangular bipyramid rule derived in the paper is a general rule that can solve all iterative adjacency matrices (where an iterative matrix is one that contains only already encountered sub-matrices, i.e. contains no new structure). Thus, all iterative rules derived up until this point can be replaced by this rule - this is one example of the non-uniqueness of rules that can be used to derive packings; however, the non-iterative rules (those applied to physical as well as unphysical new seeds) must still be applied.
- • For n ≥ 8 the triangular bipyramid rule derived in the paper was used to solve for all iterative adjacency matrices and individual geometrical rules were derived for non-iterative adjacency matrices. The following table shows that iterative matrices account for most of the adjacency matrices, and that the number of non-iterative adjacency matrices does not become ‘too large’ until n = 10.

|Number of Particles|Number of Adjacency Matrices<br><br>|Iterative Adjacency Matrices|Non-Iterative Adjacency Matrices<br><br>|
|---|---|---|---|
|6|4<br><br>|3|1|
|7<br><br>|29|26<br><br>|3|
|8|438|437<br><br>|1|
|9<br><br>|13,828<br><br>|13,823|5|
|10|750,352|750,258|94|


At n = 10, there are 94 non-iterative adjacency matrices. We have solved for the packings that correspond to these matrices numerically, which is why the new seed list at n = 10 is only a preliminary list. Future work will derive a complete list of n = 10 new seeds, as well as go up to higher n. One way of accomplishing this is to apply the triangular bipyramid rule to new seeds.

- • New seed rules for n = 8 and 9 can be derived similarly. Please refer to the computer code for the relevant rules. The code can be downloaded from


http://people.seas.harvard.edu/~narkus/pubs.html

and is entitled ‘EvalAdjMats.c.’ In the code, solutions for 8 and 9 particle new seeds were input from Newton iterations to a precision of 16 decimal places.

4. Derivation of the Triangular Bipyramid Rule

We derive this rule as follows: In 3 dimensions, let the distance, rij, between 2 points, i and j, be unknown. The points i and j share a common 3 particle base, p,k,q. The 5 points i,j,k,p,q together form a (potentially irregular) ditetrahedron or triangular bipyramid (see ﬁgure 19). This triangular bipyramid can be decomposed into 3 related tetrahedra (see ﬁgure 20). Let us ﬁrst derive a formula that relates these dihedral angles (Al,Bl,Cl) to the angles (al,bl,cl); l = 1,2,3.

Consider the general (potentially irregular) tetrahedron depicted in ﬁgure 21. The dihedral angle, A, between planes AOB and AOC can be calculated using the dot product of the normals to the planes. The normals to the planes are given by the cross products of the vectors to the vertices. Thus, this dot product is given by

(OA × OB) · (OA × OC) = (|OA||OB|sinc)(|OA||OC|sinb)cosA

- (26) = |OA|2|OB||OC|sincsinbcosA. Using a well known vector identity, we also know that

(OA × OB) · (OA × OC) = OA · [OB × (OA × OC)]

= OA · [OA(OB · OC) − OC(OA · OB)]

= (OB · OC) − (OA · OC)(OA · OB)

= |OB||OC|cosa − |OA||OC|cosb|OA||OB|cosc

- (27) = |OB||OC|cosa − |OA|2|OC||OB|cosbcosc Setting eqn 26 = eqn 27, we thus have

|OA|2|OB||OC|sincsinbcosA = |OB||OC|cosa − |OA|2|OC||OB|cosb cosc We can divide by |OB| and |OC|, leaving us with

|OA|2 sincsinbcosA = cosa − |OA|2 cosbcosc and without loss of generality, we can always rescale things so that |OA| = 1, leaving us with

- (28) sincsinbcosA = cosa − cosbcosc

Note that this formula is simply the spherical rule of cosines; however, in this derivation we do not assume that all radial distances are equal, as is customary in the derivation of the spherical rule of cosines. This can analogously be derived for dihedral angles B and C, in which case we obtain

- (29) sincsinacosB = cosb − cosacosc
- (30) sinasinbcosC = cosc − cosacosb


To derive the general formula for rij, we begin with the 3rd tetrahedron of Fig. 20 (that with angles A3,B3,a3,b3, etc.) and write down the expression for A3 using eqn 28:

A3 = cos−1

cosa3 − cosb3 cosc3 sinc3 sinb3

![image 312](<2010-arkus-deriving-finite-sphere-packings_images/imageFile312.png>)

###### Figure 19. The Triangular Bipyramid.

The triangular bipyramid (or ditetrahedron) constructed in the triangular bipyramid rule. The center triangle (kpq), shown in red, corresponds to the common 3 particle base. Particles i and j are related to one another through the common base. The distance between i and j, rij, shown as the dash-dot blue line, is unknown. a1 corresponds to ∠jpi. A1 is the dihedral angle between ipk and jpk, A2 is the dihedral angle between ipk and kpq, and A3 is the dihedral angle between kpq and jpk. Points i and j can either both lie on the same side of the base kpq or each lie on opposite sides of the base (indicated by the dashed lines, that can either go into or come out of the plane). If i,j lie on the same side, then A1 is equal to the diﬀerence of A2 and A3, and if i,j lie on opposite sides of the base then A1 is equal to the sum of A2 and A3. When all distances other than rij are known, then an analytical formula can be derived to solve rij.

Analogously, for the 2nd tetrahedron, we have A2 = cos−1

cosa2 − cosb2 cosc2 sinc2 sinb2

A1 will be either the sum or the diﬀerence of the dihedral angles A2 and A3 (see ﬁg 19), depending on whether the points i,j lie on the same or on opposite sides of the base p,k,q (on the same side, A1 corresponds to the diﬀerence, and on opposite sides to the sum).

a1 is then given by

- (31) a1 = cos−1(sinc1 sinb1 cosA1 + cosb1 cosc1) and ﬁnally, from the law of cosines, we can calculate rij:
- (32) rij = rip2 + rpj2 − 2riprpj cosa1


![image 313](<2010-arkus-deriving-finite-sphere-packings_images/imageFile313.png>)

![image 314](<2010-arkus-deriving-finite-sphere-packings_images/imageFile314.png>)

![image 315](<2010-arkus-deriving-finite-sphere-packings_images/imageFile315.png>)

###### Figure 20. The Tetrahedra for the Triangular Bipyramid Rule. The 3 tetrahedra constructed for the triangular bipyramid rule. When applied to iterative packings, all of the sides of the tetrahedra are known except for side ij (corresponding to the distance rij). The known distances can be used to calculate A2 and A3, which in turn allows us to calculate A1, and thus to solve for rij.

A

a O c b

C

B

Figure 21. A General Tetrahedron.

A,B,C and O label the points of the tetrahedron. A is also used to correspond to the dihedral angle between AOB and AOC, B corresponds to the dihedral angle between AOB and BOC, and C corresponds to the dihedral angle between

BOC and AOC. a corresponds to ∠COA, b to ∠COB, and c to ∠AOB.

Associated with each rij we have 2 possible A1, and thus 2 possible solutions (similar, in principle, to one having 2 possible solutions to a quadratic equation). 4.1. Derivation of the Formula To be Used for New Seeds. From setting A1 either equal to the sum or the diﬀerence of A2 and A3, we have cos−1

cosa1 − cosb1 cosc1 sinc2 sinb2

cosa2 − cosb2 cosc2 sinc2 sinb2 ± cos−1

cosa3 − cosb3 cosc3 sinc3 sinb3

= cos−1

writing the angles ai,bi,ci in terms of their relevant distances, using the law of cosines, we then have

 

  = cos−1

 

 

d26+d24−d22

2 1+d26−d27

d21+d24−d25 2d1d4

2

- 1+d26−d27

- 2d1d6


d21+d28−d29 2d1d8

d26+d28−d210

2d6d4 − d

2d6d8 − d

2d1d6

cos−1

2 1+d26−d27)2

2 1+d24−d25)2

2 1+d26−d27)2

2 1+d28−d29)2

1 − (d

4d21d26 1 − (d

1 − (d

4d21d26 1 − (d

4d21d24

4d21d28

 

 

d24+d28−d23

2

- 1+d24−d25

- 2d1d4


d21+d28−d29 2d1d8

2d4d8 − d

±cos−1

2 1+d24−d25)2

2 1+d28−d29)2

1 − (d

4d21d24 1 − (d

4d21d28

and solving for d2 then yields

  cos−1

  

  

2 1+d2

6−d2

7)(d2

1+d2

8−d2

d2

6+d2

8−d2

−(d

9) 4d2

10 2d6d8

2 1+d26−d27)2

2 1+d24−d25)2

−2d6d4 1 − (d

4d21d26 1 − (d

1d6d8 1−(d

4d21d24 cos

2 1+d2

6−d2

2 1+d2

8−d2

7)2 4d2

9)2 4d2

1−(d

1d2

1d2

6

8

d2 =

  

   − (d

  

2 1+d2

4−d2

5)(d2

d2

1+d2

4+d2

8−d2

8−d2

−(d

9) 4d2

3 2d4d8

2 1+d26−d27)(d21+d24−d25)

1d4d8 1−(d

± cos−1

2d21 + d26 + d24

2 1+d2

4−d2

2 1+d2

8−d2

5)2 4d2

9)2 4d2

1−(d

1d2

1d2

4

8

##### APPENDIX B: PACKINGS OF 8 ≤ n ≤ 10 SPHERES

Here we include the complete set of packings for 8 ≤ n ≤ 10 particles, derived via the method speciﬁed in the paper. (Packings of n ≤ 7 particles can be found in the paper). Throughout, R corresponds to twice the radius of the particles, and without loss of generality can be normalized to 1, if desired. In all instances, a ‘∗’ appears in front of the 2nd moment that corresponds to the minimum of the 2nd moment of n particles. If a packing is denoted as chiral, then it has 2 distinct states.

Note that the code used to generate these results as well as the raw output from the code (in which case the results are output to 16 decimal places instead of the 4 d.p. shown here) can be downloaded from the following website: http://people.seas.harvard.edu/∼narkus/.

Notation: A: Adjacency Matrix. D: Distance Matrix. C: Coordinates of a packing. φ: Point group of a packing. σ: Symmetry number of a packing.

1. Packings of n = 8 Particles

Here, we include the 13 packings of n = 8 particles. The ‘Special Properties’ column denotes whether the packing is chiral or corresponds to a new seed. If the special properties column is blank, then the packing is neither. 1 of these packings (packing 13) corresponds to a new seed, and 3 of the packings are chiral. The minimum of the 2nd moment corresponds to packing 13, graph 408.

Packing 1 (Graph 27):





- 0 0 0 0 1 1 1 0

- 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 1 1 1 1 1 0 1 1 0 1 1
- 1 0 1 1 1 1 0 1


- 0 1 1 1 1 1 1 0


A :

 

 





- 0 1.6667 1.6667 1.6667 1 1 1 1.6330

1.6667 0 1.6667 1.6667 1 1 1.6330 1 1.6667 1.6667 0 1.6667 1 1.6330 1 1 1.6667 1.6667 1.6667 0 1.6330 1 1 1

- 1 1 1 1.6330 0 1 1 1 1 1 1.6330 1 1 0 1 1 1 1.6330 1 1 1 1 0 1


D :

R

 

 

1.6330 1 1 1 1 1 1 0

![image 316](<2010-arkus-deriving-finite-sphere-packings_images/imageFile316.png>)

![image 317](<2010-arkus-deriving-finite-sphere-packings_images/imageFile317.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|5.66667R2<br><br>|Td|12| |






0 0 0 0 −1.6667 0 −1.4434 −0.8333 0 −0.4811 −0.8333 −1.3608 −0.4811 −0.8333 0.2722 0 −0.8333 −0.5443 −0.7698 −0.3333 −0.5443

C :

R

- −0.7698
- −1.3333 −0.5443


 

 

Packing 2 (Graph 77):





- 0 0 0 1 0 1 1 1

- 0 0 0 0 1 1 1 1

- 0 0 0 0 1 0 1 1
- 1 0 0 0 0 1 0 1


- 0 1 1 0 0 0 1 1


- 1 1 0 1 0 0 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 1 0


A :

 

 





- 0 1.6330 1.0887 1 1.6667 1 1 1

1.6330 0 1.6330 1.6667 1 1 1 1 1.0887 1.6330 0 1.7249 1 1.6667 1 1

- 1 1.6667 1.7249 0 1.9907 1 1.6330 1


D :

R

1.6667 1 1 1.9907 0 1.6330 1 1 1 1 1.6667 1 1.6330 0 1 1 1 1 1 1.6330 1 1 0 1 1 1 1 1 1 1 1 0

 

 

![image 318](<2010-arkus-deriving-finite-sphere-packings_images/imageFile318.png>)

![image 319](<2010-arkus-deriving-finite-sphere-packings_images/imageFile319.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|5.64043R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.0264 0.3629 0 −0.4811 0.2722 0.8333 0.9623 1.3608 −0.0000 −0.5774 0.8165 0 0.2887 0.8165 −0.5000 0.2887 0.8165 0.5000

C :

R

 

 

Packing 3 (Graph 82):





0 0 0 1 0 1 1 1 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 1 1 1 1 1 0 0 1 0 1 1 1 0 1 1 1 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.6330 1 1 1 1.6667 0 1.6667 1.9907 1 1 1.6330 1 1.6667 1.6667 0 1.0887 1 1.6330 1 1
- 1 1.9907 1.0887 0 1.6667 1.6330 1 1


D :

R

1.6330 1 1 1.6667 0 1 1 1 1 1 1.6330 1.6330 1 0 1 1 1 1.6330 1 1 1 1 0 1 1 1 1 1 1 1 1 0

 

 

![image 320](<2010-arkus-deriving-finite-sphere-packings_images/imageFile320.png>)

![image 321](<2010-arkus-deriving-finite-sphere-packings_images/imageFile321.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|5.61574R2|C1<br><br>|1|chiral|






0 0 0 0 1.6667 0 1.4434 0.8333 0 0.9302 −0.0556 −0.3629 0.7698 1.3333 0.5443 −0.0962 0.8333 0.5443 0.7698 0.3333 0.5443 0.4811 0.8333 −0.2722

C :

R

 

 

Packing 4 (Graph 107):





0 0 0 1 0 1 1 1 0 0 0 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 1 1 1 1 1 1 0 1 0 1 1 1 1 0 1 1 1 0 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.6330 1 1 1 1.6667 0 1.6667 1.9907 1 1 1 1.6330 1.6667 1.6667 0 1.9907 1 1 1.6330 1
- 1 1.9907 1.9907 0 1.6667 1.6330 1 1


D :

R

1.6330 1 1 1.6667 0 1 1 1 1 1 1 1.6330 1 0 1 1 1 1 1.6330 1 1 1 0 1 1 1.6330 1 1 1 1 1 0

 

 

![image 322](<2010-arkus-deriving-finite-sphere-packings_images/imageFile322.png>)

![image 323](<2010-arkus-deriving-finite-sphere-packings_images/imageFile323.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|5.96296R2<br><br>|Cs|1| |






0 0 0 0 1.6667 0 −1.4434 0.8333 0 0 −0.0556 −0.9979 −0.7698 1.3333 −0.5443 −0.4811 0.8333 0.2722 0 0.8333 −0.5443 −0.7698 0.3333 −0.5443

C :

R

 

 

Packing 5 (Graph 204):





0 0 0 1 1 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 0 0 1 1 0 1 1 1 0 1 0 0 1 1 1 0 1 1 0 0 1 1 1 1 1 0 1 1 0 1 0 1 1 1 1 1 1 0

A :

 

 





0 1.7321 1.7321 1 1 1 1 1.4142

1.7321 0 1.4142 1.7321 1 1.7321 1 1 1.7321 1.4142 0 1.7321 1.7321 1 1 1

1 1.7321 1.7321 0 1 1 1.4142 1 1 1 1.7321 1 0 1.4142 1 1 1 1.7321 1 1 1.4142 0 1 1 1 1 1 1.4142 1 1 0 1

D :

R

 

 

1.4142 1 1 1 1 1 1 0

![image 324](<2010-arkus-deriving-finite-sphere-packings_images/imageFile324.png>)

![image 325](<2010-arkus-deriving-finite-sphere-packings_images/imageFile325.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|5.50000R2|C2v<br><br>|2| |






0 0 0 0 −1.7321 0 1.2910 −1.1547 0 0.1291 −0.2887 0.9487 −0.3873 −0.8660 0.3162 0.9037 −0.2887 0.3162 0.3873 −0.8660

C :

R

- −0.3162 0.5164
- −1.1547 0.6325


 

 

Packing 6 (Graph 224):





0 0 0 1 1 0 1 1 0 0 0 1 0 1 1 1 0 0 0 0 1 1 1 1 1 1 0 0 0 0 1 1 1 0 1 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 1 1 1 0 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1 1.9868 1 1 1.6330 0 1.0887 1 1.6667 1 1 1 1.6330 1.0887 0 1.6667 1 1 1 1
- 1 1 1.6667 0 1.6330 1.6859 1 1 1 1.6667 1 1.6330 0 1.6859 1 1


D :

R

1.9868 1 1 1.6859 1.6859 0 1.6059 1 1 1 1 1 1 1.6059 0 1 1 1 1 1 1 1 1 0

 

 

![image 326](<2010-arkus-deriving-finite-sphere-packings_images/imageFile326.png>)

![image 327](<2010-arkus-deriving-finite-sphere-packings_images/imageFile327.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|5.61891R2<br><br>|Cs|1| |






0 0 0 0 1.6330 0 −1.0264 1.2701 0 0.5774 0.8165 0 −0.9623 0.2722 0 −0.6077 1.7189 −0.7895 −0.2887 0.8165 0.5000 −0.2887 0.8165 −0.5000

C :

R

 

 

Packing 7 (Graph 271):





0 0 0 1 1 0 1 1 0 0 0 1 0 1 0 1 0 0 0 0 1 1 1 1 1 1 0 0 0 1 1 1 1 0 1 0 0 0 1 1 0 1 1 1 0 0 1 1 1 0 1 1 1 1 0 0 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.6779 1.6180 1 1 1.6180 1 1 1.6779 0 1.6779 1 1.9843 1 1.6532 1 1.6180 1.6779 0 1.6180 1 1 1 1
- 1 1 1.6180 0 1.6180 1 1 1 1 1.9843 1 1.6180 0 1.6180 1 1


D :

R

1.6180 1 1 1 1.6180 0 1 1 1 1.6532 1 1 1 1 0 1.0515 1 1 1 1 1 1 1.0515 0

 

 

![image 328](<2010-arkus-deriving-finite-sphere-packings_images/imageFile328.png>)

![image 329](<2010-arkus-deriving-finite-sphere-packings_images/imageFile329.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|5.56215R2|Cs<br><br>|1| |






0 0 0 0 −1.6779 0 −1.4175 −0.7801 0 0.1090 −0.8390 −0.5331 −0.9435 0 0.3295 −0.7671 −1.3211 −0.5331 −0.7459 −0.3226 −0.5827 −0.4617 −0.8390 0.2880

C :

R

 

 

Packing 8 (Graph 294):





0 0 0 1 1 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 1 1 1 1 0 0 0 1 1 1 1 0 1 0 0 1 1 1 1 1 0 1 1 0 0 1 1 0 1 1 1 0 0 1 0 1 1 1 1 1 1 0

A :

 

 





0 1.7321 1.7321 1 1 1 1 1.4142

1.7321 0 2.0000 1 1.7321 1 1.7321 1 1.7321 2.0000 0 1.7321 1 1.7321 1 1

1 1 1.7321 0 1.4142 1 1 1 1 1.7321 1 1.4142 0 1 1 1 1 1 1.7321 1 1 0 1.4142 1 1 1.7321 1 1 1 1.4142 0 1

D :

R

 

 

1.4142 1 1 1 1 1 1 0

![image 330](<2010-arkus-deriving-finite-sphere-packings_images/imageFile330.png>)

![image 331](<2010-arkus-deriving-finite-sphere-packings_images/imageFile331.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|5.75000R2|C2v<br><br>|2| |






0 0 0 0 −1.7321 0 −1.6330 −0.5774 0 −0.0000 −0.8660 −0.5000 −0.8165 −0.2887 0.5000 −0.0000 −0.8660 0.5000 −0.8165 −0.2887 −0.5000 −0.8165 −1.1547 0

C :

R

 

 

Packing 9 (Graph 358):





- 0 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 1 1 0 1
- 0 1 0 0 0 0 1 1


A :

- 1 0 1 0 0 0 1 1
- 1 1 1 0 0 0 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 1 1 0


 

 





- 0 1.7321 1 1.9149 1 1 1 1.4142 1.7321 0 1.7321 1 1.7321 1 1 1
- 1 1.7321 0 1.9149 1 1 1.4142 1


1.9149 1 1.9149 0 1.4142 1.6330 1 1 1 1.7321 1 1.4142 0 1.4142 1 1 1 1 1 1.6330 1.4142 0 1 1 1 1 1.4142 1 1 1 0 1

D :

R

 

 

1.4142 1 1 1 1 1 1 0

![image 332](<2010-arkus-deriving-finite-sphere-packings_images/imageFile332.png>)

![image 333](<2010-arkus-deriving-finite-sphere-packings_images/imageFile333.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|5.62500R2|Cs<br><br>|1| |






0 0 0 0 1.7321 0 −0.9574 0.2887 0 −0.0290 1.6358 0.9949 −0.4352 0.2887 0.8528 −0.2611 0.8660 −0.4264 0.2611 0.8660 0.4264 −0.6963 1.1547 0.4264

C :

R

 

 

Packing 10 (Graph 366):





0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 0 1 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 1 0 1 0 0 1 1 1 1 1 0 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





0 1.6330 1 1.6667 1 1 1 1 1.6330 0 1.6667 1 1.9907 1 1 1 1 1.6667 0 1.9907 1 1.6330 1 1

1.6667 1 1.9907 0 1.7778 1 1.6330 1 1 1.9907 1 1.7778 0 1.6667 1.6330 1 1 1 1.6330 1 1.6667 0 1 1 1 1 1 1.6330 1.6330 1 0 1 1 1 1 1 1 1 1 0

D :

R

 

 

![image 334](<2010-arkus-deriving-finite-sphere-packings_images/imageFile334.png>)

![image 335](<2010-arkus-deriving-finite-sphere-packings_images/imageFile335.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.01080R2<br><br>|Cs|1| |






0 0 0 0 1.6330 0 −0.9623 0.2722 0 0.4811 1.3608 0.8333 −0.5453 −0.0907 0.8333 0.5774 0.8165 −0.0000 −0.2887 0.8165 −0.5000 −0.2887 0.8165 0.5000

C :

R

 

 

Packing 11 (Graph 374):





0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 0 1 0 0 0 1 1 0 1 0 1 0 0 0 0 1 1 1 0 1 0 0 1 1 1 1 1 1 0 1 0 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1 1.6667 1 1 1 1 1.6330 0 1.6667 1 1.9907 1 1 1
- 1 1.6667 0 1.9907 1 1.6330 1 1 1.6667 1 1.9907 0 2.4369 1 1 1.6330 1 1.9907 1 2.4369 0 1.6667 1.6330 1 1 1 1.6330 1 1.6667 0 1 1 1 1 1 1 1.6330 1 0 1 1 1 1 1.6330 1 1 1 0


D :

R

 

 

![image 336](<2010-arkus-deriving-finite-sphere-packings_images/imageFile336.png>)

![image 337](<2010-arkus-deriving-finite-sphere-packings_images/imageFile337.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.35802R2|C1|1|chiral|






0 0 0 0 1.6330 0 −0.9623 0.2722 0 0.4811 1.3608 −0.8333 −0.5453 −0.0907 0.8333 0.5774 0.8165 0 −0.2887 0.8165 −0.5000 −0.2887 0.8165 0.5000

C :

R

 

 

Packing 12 (Graph 397):





0 0 1 0 1 1 1 1 0 0 0 1 1 1 1 1 1 0 0 0 1 0 1 0 0 1 0 0 0 1 0 1 1 1 1 0 0 0 1 1 1 1 0 1 0 0 1 1 1 1 1 0 1 1 0 0 1 1 0 1 1 1 0 0

A :

 

 





- 0 1.4142 1 1.7321 1 1 1 1 1.4142 0 1.7321 1 1 1 1 1
- 1 1.7321 0 2.4495 1 1.7321 1 1.7321


1.7321 1 2.4495 0 1.7321 1 1.7321 1 1 1 1 1.7321 0 1.4142 1 1 1 1 1.7321 1 1.4142 0 1 1 1 1 1 1.7321 1 1 0 1.4142 1 1 1.7321 1 1 1 1.4142 0

D :

R

 

 

![image 338](<2010-arkus-deriving-finite-sphere-packings_images/imageFile338.png>)

![image 339](<2010-arkus-deriving-finite-sphere-packings_images/imageFile339.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|6.00000R2|D3d<br><br>|6| |






0 0 0 0 −1.4142 0 1.0000 0 0 −1.0000 −1.4142 −0.0000 0.5000 −0.7071 0.5000 −0.5000 −0.7071 −0.5000 0.5000 −0.7071 −0.5000 −0.5000 −0.7071 0.5000

C :

R

 

 

Packing 13 (Graph 408):





0 0 1 0 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 1 1 0 1 0 1 0 0 0 1 1 1 1 1 1 0 0 0 1 1 1 0 1 1 0 0 1 1 1 1 0 1 1 1 0 0 0 1 1 1 1 1 0 0

A :

 

 





- 0 1.7199 1 1.7199 1 1 1 1.5130 1.7199 0 1.7199 1 1 1.5130 1 1
- 1 1.7199 0 1.7199 1 1 1.5130 1


1.7199 1 1.7199 0 1.5130 1 1 1 1 1 1 1.5130 0 1.2892 1 1 1 1.5130 1 1 1.2892 0 1 1 1 1 1.5130 1 1 1 0 1.2892

D :

R

 

 

1.5130 1 1 1 1 1 1.2892 0

![image 340](<2010-arkus-deriving-finite-sphere-packings_images/imageFile340.png>)

![image 341](<2010-arkus-deriving-finite-sphere-packings_images/imageFile341.png>)

|2nd Moment<br><br>|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|∗5.28917R2<br><br>|D2d|4|new seed|






0 0 0 0 1.7199 0 0.9568 0.2907 0 0 1.4292 −0.9527 0.2613 0.8600 0.4384 0.3752 0.4852 −0.7898 −0.4124 0.8600 −0.3006 0.8211 1.2347 −0.3006

C :

R

 

 

2. Packings of n = 9 Particles

Here, we include the 52 packings of n = 9 particles. The ‘Special Properties’ column denotes whether the packing is chiral, non-rigid, or corresponds to a new seed. If the special properties column is blank, then the packing is none of these. 28 of these packings are chiral, 4 of these packings correspond to new seeds (graphs 8901, 8926, 12811, and 13380), and 1 of them is non-rigid (graph 8901). The minimum of the 2nd moment corresponds to packing 47, graph 13380. A star, ‘*’, appears in front of packings that are reported here but were not reported in our last paper (PRL, 103, 118303).

Packing 1 (Graph 406):





- 0 0 0 0 1 0 1 1 1

- 0 0 0 0 0 1 1 1 0

- 0 0 0 0 0 1 1 0 1

- 0 0 0 0 0 1 0 1 1
- 1 0 0 0 0 0 0 1 1


- 0 1 1 1 0 0 1 1 1


- 1 1 1 0 0 1 0 1 1


- 1 1 0 1 1 1 1 0 1 1 0 1 1 1 1 1 1 0


A :

 

 



- 0 1.6667 1.6667 1.6667 1 1.6330 1 1 1

1.6667 0 1.6667 1.6667 1.9907 1 1 1 1.6330 1.6667 1.6667 0 1.6667 1.9907 1 1 1.6330 1 1.6667 1.6667 1.6667 0 1.0887 1 1.6330 1 1

- 1 1.9907 1.9907 1.0887 0 1.6667 1.6330 1 1


D :

1.6330 1 1 1 1.6667 0 1 1 1 1 1 1 1.6330 1.6330 1 0 1 1 1 1 1.6330 1 1 1 1 0 1 1 1.6330 1 1 1 1 1 1 0

 



R

 

![image 342](<2010-arkus-deriving-finite-sphere-packings_images/imageFile342.png>)

![image 343](<2010-arkus-deriving-finite-sphere-packings_images/imageFile343.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.98765R2|C1h<br><br>|1| |






0 0 0 0 1.6667 0 1.4434 0.8333 0 0.4811 0.8333 −1.3608 −0.0321 −0.0556 −0.9979 0.7698 1.3333 −0.5443 0.4811 0.8333 0.2722 −0.0962 0.8333 −0.5443 0.7698 0.3333 −0.5443

C :

R

 

 

Packing 2 (Graph 756):





0 0 0 0 1 1 1 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1.6330 1 1 1 1 1

1.6330 0 1.7778 1.0887 1 1.9907 1 1.6667 1 1.6330 1.7778 0 1.0887 1.9907 1 1.6667 1 1 1.6330 1.0887 1.0887 0 1.6667 1.6667 1 1 1

- 1 1 1.9907 1.6667 0 1.6667 1 1.6330 1 1 1.9907 1 1.6667 1.6667 0 1.6330 1 1 1 1 1.6667 1 1 1.6330 0 1 1 1 1.6667 1 1 1.6330 1 1 0 1 1 1 1 1 1 1 1 1 0


D :

R

 

 

![image 344](<2010-arkus-deriving-finite-sphere-packings_images/imageFile344.png>)

![image 345](<2010-arkus-deriving-finite-sphere-packings_images/imageFile345.png>)

|2nd Moment|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.85322R2<br><br>|Cs|1| |






0 0 0 0 −1.6330 0 −1.4913 −0.6653 0

- −0.8242
- −1.2701 0.6118 0.4636


C :

−0.8165 −0.3441 −0.9345 0 −0.3441 0 −0.8165 0.5735 −0.7726 −0.2722 0.5735 −0.5298 −0.8165 −0.2294

R

 

 

Packing 3 (Graph 971):





0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 0 0 1 1 0 0 0 1 1 1 1 1 0 1 0 0 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1.0887 1 1.6667 1 1 1 1.6330 0 1.0887 1.9959 1 1.7249 1 1.6667 1 1.6330 1.0887 0 1.6330 1.6667 1 1 1 1 1.0887 1.9959 1.6330 0 1.7249 1 1.6667 1 1
- 1 1 1.6667 1.7249 0 1.9907 1 1.6330 1


D :

R

1.6667 1.7249 1 1 1.9907 0 1.6330 1 1 1 1 1 1.6667 1 1.6330 0 1 1 1 1.6667 1 1 1.6330 1 1 0 1 1 1 1 1 1 1 1 1 0

 

 

![image 346](<2010-arkus-deriving-finite-sphere-packings_images/imageFile346.png>)

![image 347](<2010-arkus-deriving-finite-sphere-packings_images/imageFile347.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.85688R2<br><br>|C2|2<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.0264 −1.2701 0 −0.6272 0 0.8889 0.5774 −0.8165

C :

R

- −0.0000
- −1.2295 −0.7560


0.8333 −0.2887 −0.8165 −0.5000 −0.9623 −0.2722 −0.0000 −0.2887 −0.8165 0.5000

 

 

Packing 4 (Graph 991):





0 0 0 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 1 0 0 1 1 0 0 0 1 1 1 1 1 0 1 0 0 1 1 1 0 1 1 1 1 1 0 1 0 1 1 1 1 1 1 1 0

A :

 

 





0 1.6667 1.6667 1.7249 1 1.9907 1 1 1.6330

1.6667 0 1.6667 1.7249 1 1.9907 1 1.6330 1 1.6667 1.6667 0 1.6330 1.6330 1 1 1 1 1.7249 1.7249 1.6330 0 1.0887 1 1.6667 1 1

D :

1 1 1.6330 1.0887 0 1.6667 1 1 1

R

1.9907 1.9907 1 1 1.6667 0 1.6330 1 1 1 1 1 1.6667 1 1.6330 0 1 1 1 1.6330 1 1 1 1 1 0 1

 

 

1.6330 1 1 1 1 1 1 1 0

![image 348](<2010-arkus-deriving-finite-sphere-packings_images/imageFile348.png>)

![image 349](<2010-arkus-deriving-finite-sphere-packings_images/imageFile349.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.03155R2|Cs<br><br>|1| |






0 0 0 0 1.6667 0 −1.4434 0.8333 0 −0.5880 0.8333 −1.3911 0 0.8333 −0.5443 −1.5075 0.8333 −0.9979 −0.4811 0.8333 0.2722 −0.7698 0.3333 −0.5443 −0.7698 1.3333 −0.5443

C :

R

 

 

Packing 5 (Graph 1039):





0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 1 0 0 1 1 0 0 1 1 1 1 0 1 0 1 1 0 1 1 0 1 0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.0887 1.9907 1 1.6667 1 1.6330 1 1.6667 0 1.9907 1.0887 1 1.6667 1.6330 1 1 1.0887 1.9907 0 1.6667 1.6667 1 1 1.6330 1 1.9907 1.0887 1.6667 0 1.6667 1 1.6330 1 1
- 1 1 1.6667 1.6667 0 1.6330 1 1 1 1.6667 1.6667 1 1 1.6330 0 1 1 1


D :

R

1 1.6330 1 1.6330 1 1 0 1 1 1.6330 1 1.6330 1 1 1 1 0 1

 

 

1 1 1 1 1 1 1 1 0

![image 350](<2010-arkus-deriving-finite-sphere-packings_images/imageFile350.png>)

![image 351](<2010-arkus-deriving-finite-sphere-packings_images/imageFile351.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|6.81070R2<br><br>|C2v|2| |






0 0 0 0 −1.6667 0 −1.0887

- −0.0000 0
- −1.0887 −1.6667 −0.0000


0.2722

C :

- −0.8333 0.4811
- −1.3608 −0.8333


R

0.4811 −0.5443 −0.3333 0.7698 −0.5443 −1.3333 0.7698 −0.5443 −0.8333 −0.0962

 

 

Packing 6 (Graph 1050):





0 0 0 0 1 0 1 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 1 0 0 1 1 0 0 1 1 1 1 0 1 0 1 1 0 1 1 1 1 0 1 1 1 1 0 1 0 1 1 1 1 1 1 1 0

A :

 

 





0 1.6667 1.9907 1.9907 1 1.6667 1 1 1.6330

1.6667 0 1.9907 1.0887 1 1.6667 1.6330 1 1 1.9907 1.9907 0 1.6667 1.6667 1 1 1.6330 1 1.9907 1.0887 1.6667 0 1.6667 1 1.6330 1 1

D :

1 1 1.6667 1.6667 0 1.6330 1 1 1

R

1.6667 1.6667 1 1 1.6330 0 1 1 1 1 1.6330 1 1.6330 1 1 0 1 1 1 1 1.6330 1 1 1 1 0 1

 

 

1.6330 1 1 1 1 1 1 1 0

![image 352](<2010-arkus-deriving-finite-sphere-packings_images/imageFile352.png>)

![image 353](<2010-arkus-deriving-finite-sphere-packings_images/imageFile353.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.11934R2<br><br>|C2|2|chiral|






0 0 0 0 −1.6667 0 1.8079

- −0.8333 0

0.6556

- −1.6667 0.8692


0.2202 −0.8333 −0.5070 1.2036 −0.8333 0.7967 0.9424 −0.3333 −0.0290 0.2510 −0.8333 0.4925 0.9424 −1.3333 −0.0290

C :

R

 

 

Packing 7 (Graph 1427):





0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 1 0

A :

 

 





0 1.6330 1.6859 1.6859 1 1 1.6667 1 1 1.6330 0 1.6859 1.6859 1 1.6667 1 1 1 1.6859 1.6859 0 1.5789 1.9868 1 1 1 1.6059 1.6859 1.6859 1.5789 0 1.9868 1 1 1.6059 1 1 1 1.9868 1.9868 0 1.6330 1.6330 1 1 1 1.6667 1 1 1.6330 0 1.0887 1 1

D :

R

1.6667 1 1 1 1.6330 1.0887 0 1 1 1 1 1 1.6059 1 1 1 0 1 1 1 1.6059 1 1 1 1 1 0

 

 

![image 354](<2010-arkus-deriving-finite-sphere-packings_images/imageFile354.png>)

![image 355](<2010-arkus-deriving-finite-sphere-packings_images/imageFile355.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.96165R2|C2v<br><br>|2| |






0 0 0 0 −1.6330 0 −1.4749 −0.8165 0 −0.6298 −0.8165 −1.3337 0.4877 −0.8165 0.3090 −0.8128 −0.2722 −0.5151

C :

R

- −0.8128
- −1.3608 −0.5151 −0.5115 −0.8165


0.2678 0 −0.8165 −0.5769

 

 

Packing 8 (Graph 1946):





0 0 0 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 1 1 0 0 1 1 1 1 1 1 0 1 1 0 0 1 1 1 0 1 1 1 0 0 1 0 1 1 1 0 1 1 1 0

A :

 

 





0 1.6180 1.6779 1.6779 1 1 1 1 1.6180

- 1.6180 0 1.6779 1.6779 1 1.6180 1 1 1 1.6779 1.6779 0 1.6482 1.9843 1 1 1.6532 1 1.6779 1.6779 1.6482 0 1.9843 1 1.6532 1 1

1 1 1.9843 1.9843 0 1.6180 1 1 1.6180 1 1.6180 1 1 1.6180 0 1 1 1 1 1 1 1.6532 1 1 0 1.0515 1 1 1 1.6532 1 1 1 1.0515 0 1

- 1.6180 1 1 1 1.6180 1 1 1 0


D :

R

 

 

![image 356](<2010-arkus-deriving-finite-sphere-packings_images/imageFile356.png>)

![image 357](<2010-arkus-deriving-finite-sphere-packings_images/imageFile357.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|6.94612R2|C2v<br><br>|2| |






0 0 0 0 −1.6180 0 −1.4700 −0.8090 0 −0.5461 −0.8090 −1.3648 0.4867 −0.8090 0.3295 −0.7876 −0.3090 −0.5331 −0.5124 −0.8090 0.2880 0 −0.8090 −0.5827 −0.7876 −1.3090 −0.5331

C :

R

 

 

Packing 9 (Graph 2196):





0 0 0 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 0 1 0 1 0 0 1 1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 1 1 0 1 0 1 1 1 1 1 1 1 0

A :

 

 





0 1.7321 1.7321 1.7321 1 1 1 1 1.4142

1.7321 0 2.0000 1.4142 1 1.7321 1 1.7321 1 1.7321 2.0000 0 1.4142 1.7321 1 1.7321 1 1 1.7321 1.4142 1.4142 0 1.7321 1.7321 1 1 1

D :

1 1 1.7321 1.7321 0 1 1 1.4142 1 1 1.7321 1 1.7321 1 0 1.4142 1 1 1 1 1.7321 1 1 1.4142 0 1 1 1 1.7321 1 1 1.4142 1 1 0 1

R

 

 

1.4142 1 1 1 1 1 1 1 0

![image 358](<2010-arkus-deriving-finite-sphere-packings_images/imageFile358.png>)

![image 359](<2010-arkus-deriving-finite-sphere-packings_images/imageFile359.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.88889R2|Cs|1| |






0 0 0 0 −1.7321 0 1.6330 −0.5774 0 0.8165 −1.1547 1.0000 −0.0000 −0.8660 −0.5000 0.8165 −0.2887 −0.5000 −0.0000 −0.8660 0.5000 0.8165 −0.2887 0.5000 0.8165 −1.1547 0

C :

R

 

 

Packing 10 (Graph 3313):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 1 1 0 1 1 0 0 1 1 1 1 1 0 0 1 1 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.6667 1 1 1 1 1.6330 0 1.0887 1.6667 1 1.6667 1 1 1 1.6330 1.0887 0 1.9907 1.7249 1 1.6667 1 1
- 1 1.6667 1.9907 0 1.0887 1.6667 1 1.6330 1


D :

1.6667 1 1.7249 1.0887 0 1.9907 1 1.6330 1 1 1.6667 1 1.6667 1.9907 0 1.6330 1 1 1 1 1.6667 1 1 1.6330 0 1 1 1 1 1 1.6330 1.6330 1 1 0 1 1 1 1 1 1 1 1 1 0

R

 

 

![image 360](<2010-arkus-deriving-finite-sphere-packings_images/imageFile360.png>)

![image 361](<2010-arkus-deriving-finite-sphere-packings_images/imageFile361.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|6.83265R2|C1<br><br>|1|chiral|






0 0 0 0 −1.6330 0 1.0264 −1.2701 0 −0.4811 −0.2722 −0.8333

- −0.4811
- −1.3608 −0.8333


C :

R

0.9623 −0.2722 0 −0.5774 −0.8165 0 0.2887 −0.8165 0.5000 0.2887 −0.8165 −0.5000

 

 

Packing 11 (Graph 3326):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 1 1 0 1 1 0 0 1 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.6667 1 1 1 1 1.6330 0 1.0887 1.6667 1 1.6667 1 1 1 1.6330 1.0887 0 1.9907 1.7249 1 1.6667 1 1
- 1 1.6667 1.9907 0 1.9907 1.6667 1 1 1.6330


D :

1.6667 1 1.7249 1.9907 0 1.9907 1 1.6330 1 1 1.6667 1 1.6667 1.9907 0 1.6330 1 1 1 1 1.6667 1 1 1.6330 0 1 1 1 1 1 1 1.6330 1 1 0 1 1 1 1 1.6330 1 1 1 1 0

R

 

 

![image 362](<2010-arkus-deriving-finite-sphere-packings_images/imageFile362.png>)

![image 363](<2010-arkus-deriving-finite-sphere-packings_images/imageFile363.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|7.14129R2|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.0264 1.2701 0 0.4811 0.2722 −0.8333 0.4811 1.3608 0.8333 −0.9623 0.2722 0 0.5774 0.8165 0 −0.2887 0.8165 −0.5000 −0.2887 0.8165 0.5000

C :

R

 

 

Packing 12 (Graph 3850):





0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 1 1 1 1 1 0 0 0 1 1 1 1 0 1 1 0 1 0 0 1 1 1 0 1 1 1 0 0 1 0 1 1 1 1 1 1 1 0

A :

 

 





0 1.7321 1.7321 1 1.9149 1 1 1 1.4142

1.7321 0 1.4142 1.7321 1 1 1.7321 1 1 1.7321 1.4142 0 1.7321 1.9149 1 1 1.7321 1

1 1.7321 1.7321 0 1.4142 1.4142 1 1 1

D :

1.9149 1 1.9149 1.4142 0 1.6330 1.9149 1 1 1 1 1 1.4142 1.6330 0 1 1 1 1 1.7321 1 1 1.9149 1 0 1.4142 1 1 1 1.7321 1 1 1 1.4142 0 1

R

 

 

1.4142 1 1 1 1 1 1 1 0

![image 364](<2010-arkus-deriving-finite-sphere-packings_images/imageFile364.png>)

![image 365](<2010-arkus-deriving-finite-sphere-packings_images/imageFile365.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.96296R2<br><br>|C1|1|chiral|






0 0 0 0 −1.7321 0 1.2910 −1.1547 0 0.1291 −0.2887 0.9487 −0.3012 −1.6358 0.9487 0.3873 −0.8660 −0.3162 0.9037 −0.2887 0.3162 −0.3873 −0.8660 0.3162 0.5164 −1.1547 0.6325

C :

R

 

 

Packing 13 (Graph 4537):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 1 1 1 1 0 0 1 0 0 1 1 1 1 1 0 0 1 1 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.6667 1 1 1 1 1.6330 0 1.0887 1.9907 1 1.6667 1 1 1 1.6330 1.0887 0 1.6667 1.7249 1 1.6667 1 1
- 1 1.9907 1.6667 0 1.7778 1 1.6667 1.6330 1


D :

1.6667 1 1.7249 1.7778 0 1.9907 1 1.6330 1 1 1.6667 1 1 1.9907 0 1.6330 1 1 1 1 1.6667 1.6667 1 1.6330 0 1 1 1 1 1 1.6330 1.6330 1 1 0 1 1 1 1 1 1 1 1 1 0

R

 

 

![image 366](<2010-arkus-deriving-finite-sphere-packings_images/imageFile366.png>)

![image 367](<2010-arkus-deriving-finite-sphere-packings_images/imageFile367.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.05213R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.0264 −1.2701 0

- −0.5453 0

0.8333 0.4811

- −1.3608 0.8333


C :

R

−0.9623 −0.2722 −0.0000 0.5774 −0.8165 0 −0.2887 −0.8165 −0.5000 −0.2887 −0.8165 0.5000

 

 

Packing 14 (Graph 4549):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 1 1 1 1 0 0 1 0 0 1 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.6667 1 1 1 1 1.6330 0 1.0887 1.9907 1 1.6667 1 1 1 1.6330 1.0887 0 1.6667 1.7249 1 1.6667 1 1
- 1 1.9907 1.6667 0 2.4369 1 1.6667 1 1.6330


D :

1.6667 1 1.7249 2.4369 0 1.9907 1 1.6330 1 1 1.6667 1 1 1.9907 0 1.6330 1 1 1 1 1.6667 1.6667 1 1.6330 0 1 1 1 1 1 1 1.6330 1 1 0 1 1 1 1 1.6330 1 1 1 1 0

R

 

 

![image 368](<2010-arkus-deriving-finite-sphere-packings_images/imageFile368.png>)

![image 369](<2010-arkus-deriving-finite-sphere-packings_images/imageFile369.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.36077R2<br><br>|C1|1|chiral|






0 0 0 0 1.6330 0 −1.0264 1.2701 0 −0.5453 −0.0907 −0.8333 0.4811 1.3608 0.8333 −0.9623 0.2722 0 0.5774 0.8165 −0.0000 −0.2887 0.8165 −0.5000 −0.2887 0.8165 0.5000

C :

R

 

 

Packing 15 (Graph 4564):





0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 0 1 1 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1.7249 1 1.6667 1 1 1.0887 0 1.6330 1.7249 1 1.6667 1 1 1 1.6330 1.6330 0 1.6667 1.6667 1 1 1 1
- 1 1.7249 1.6667 0 1.8144 1 1.9907 1.6330 1 1.7249 1 1.6667 1.8144 0 1.9907 1 1.6330 1


D :

R

1 1.6667 1 1 1.9907 0 1.6330 1 1

1.6667 1 1 1.9907 1 1.6330 0 1 1 1 1 1 1.6330 1.6330 1 1 0 1 1 1 1 1 1 1 1 1 0

 

 

![image 370](<2010-arkus-deriving-finite-sphere-packings_images/imageFile370.png>)

![image 371](<2010-arkus-deriving-finite-sphere-packings_images/imageFile371.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.08871R2<br><br>|Cs|1| |






0 0 0 0 1.0887 0 −1.5396 0.5443 0 −0.4170 −0.3629 −0.8333 −0.4170 1.4515 −0.8333 −0.9623 −0.2722 −0.0000 −0.9623 1.3608 −0.0000 −0.6736 0.5443 0.5000 −0.6736 0.5443 −0.5000

C :

R

 

 

Packing 16 (Graph 4574):





0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1.7249 1 1.6667 1 1 1.0887 0 1.6330 1.7249 1 1.6667 1 1 1 1.6330 1.6330 0 1.6667 1.6667 1 1 1 1
- 1 1.7249 1.6667 0 2.4637 1 1.9907 1 1.6330 1.7249 1 1.6667 2.4637 0 1.9907 1 1.6330 1


D :

R

1 1.6667 1 1 1.9907 0 1.6330 1 1

1.6667 1 1 1.9907 1 1.6330 0 1 1 1 1 1 1 1.6330 1 1 0 1 1 1 1 1.6330 1 1 1 1 0

 

 

![image 372](<2010-arkus-deriving-finite-sphere-packings_images/imageFile372.png>)

![image 373](<2010-arkus-deriving-finite-sphere-packings_images/imageFile373.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.39735R2<br><br>|C2|2|chiral|






0 0 0 0 −1.0887 0 1.5396

- −0.5443 0

0.4170 0.3629 0.8333 0.4170

- −1.4515 −0.8333


C :

R

0.9623 0.2722 −0.0000 0.9623 −1.3608 −0.0000 0.6736 −0.5443 0.5000 0.6736 −0.5443 −0.5000

 

 

Packing 17 (Graph 4811):





0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 1 1 0 1 1 0 0 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 0 0 1 1 0 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1 1.6330 1 1 1.6667 0 1.6667 1.9907 1 1.6330 1 1 1 1.6667 1.6667 0 1.9907 1.9907 1 1 1 1.6330 1 1.9907 1.9907 0 1.7778 1 1.6667 1.6330 1 1.9907 1 1.9907 1.7778 0 1.6667 1 1.6330 1
- 1 1.6330 1 1 1.6667 0 1 1 1


D :

R

1.6330 1 1 1.6667 1 1 0 1 1 1 1 1 1.6330 1.6330 1 1 0 1 1 1 1.6330 1 1 1 1 1 0

 

 

![image 374](<2010-arkus-deriving-finite-sphere-packings_images/imageFile374.png>)

![image 375](<2010-arkus-deriving-finite-sphere-packings_images/imageFile375.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.47051R2|Cs|1| |






0 0 0 0 −1.6667 0 −1.4434 −0.8333 0 0 0

- −0.9979 0
- −1.7222 −0.9979 −0.7698 −0.3333 −0.5443 −0.7698 −1.3333 −0.5443 −0.4811 −0.8333


C :

R

0.2722 0 −0.8333 −0.5443

 

 

Packing 18 (Graph 4816):





0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 1 1 0 1 1 0 0 1 1 1 0 1 1 0 1 1 0 1 1 1 1 0 1 0 1 1 0 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1 1.6330 1 1 1.6667 0 1.6667 1.9907 1 1.6330 1 1 1 1.6667 1.6667 0 1.9907 1.0887 1 1 1.6330 1
- 1 1.9907 1.9907 0 2.4369 1 1.6667 1 1.6330 1.9907 1 1.0887 2.4369 0 1.6667 1 1.6330 1


D :

R

1 1.6330 1 1 1.6667 0 1 1 1

1.6330 1 1 1.6667 1 1 0 1 1 1 1 1.6330 1 1.6330 1 1 0 1 1 1 1 1.6330 1 1 1 1 0

 

 

![image 376](<2010-arkus-deriving-finite-sphere-packings_images/imageFile376.png>)

![image 377](<2010-arkus-deriving-finite-sphere-packings_images/imageFile377.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.47051R2<br><br>|C1|1|chiral|






0 0 0 0 −1.6667 0 1.4434 −0.8333 0 −0.0321 0 −0.9979 0.9302 −1.7222 0.3629 0.7698 −0.3333 −0.5443 0.7698 −1.3333 −0.5443 −0.0962 −0.8333 −0.5443 0.4811 −0.8333 0.2722

C :

R

 

 

Packing 19 (Graph 5093):





0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1 1.6667 1 1 1 1.6330 0 1.6330 1.7622 1 1 1.9868 1 1 1.0887 1.6330 0 1.6667 1.6667 1 1 1 1
- 1 1.7622 1.6667 0 1.1471 1.9956 1 1.6859 1 1 1 1.6667 1.1471 0 1.6330 1.6859 1 1


D :

R

1.6667 1 1 1.9956 1.6330 0 1.6859 1 1 1 1.9868 1 1 1.6859 1.6859 0 1.6059 1 1 1 1 1.6859 1 1 1.6059 0 1 1 1 1 1 1 1 1 1 0

 

 

![image 378](<2010-arkus-deriving-finite-sphere-packings_images/imageFile378.png>)

![image 379](<2010-arkus-deriving-finite-sphere-packings_images/imageFile379.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.88607R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.0264 −0.3629 0 0.3494 −0.1719 −0.9211 0.5774 −0.8165 0

C :

R

- −0.9623
- −1.3608 −0.0000 −0.6077


0 −0.7895 −0.2887 −0.8165 0.5000 −0.2887 −0.8165 −0.5000

 

 

Packing 20 (Graph 5098):





0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1 1.9868 1 1 1 1.6330 0 1.0887 1.9907 1 1 1.6667 1 1 1.6330 1.0887 0 1.6667 1.6667 1 1 1 1
- 1 1.9907 1.6667 0 1.6667 1.8113 1 1.6330 1 1 1 1.6667 1.6667 0 1.6859 1.6330 1 1


D :

R

1.9868 1 1 1.8113 1.6859 0 1.6859 1.6059 1 1 1.6667 1 1 1.6330 1.6859 0 1 1 1 1 1 1.6330 1 1.6059 1 0 1 1 1 1 1 1 1 1 1 0

 

 

![image 380](<2010-arkus-deriving-finite-sphere-packings_images/imageFile380.png>)

![image 381](<2010-arkus-deriving-finite-sphere-packings_images/imageFile381.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.04635R2|C1<br><br>|1|chiral|






0 0 0 0 −1.6330 0 −1.0264 −1.2701 0 −0.5453 0 −0.8333 0.5774 −0.8165 0 −0.6077 −1.7189 −0.7895 −0.9623 −0.2722 −0.0000 −0.2887 −0.8165 0.5000 −0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 21 (Graph 5101):





0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 1 1 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 1 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1 1.6667 1 1 1 1.0887 0 1.6330 1.7249 1 1 1.6667 1 1 1.6330 1.6330 0 1.6667 1.9868 1 1 1 1
- 1 1.7249 1.6667 0 1.1471 1.9907 1 1.6330 1 1 1 1.9868 1.1471 0 1.6859 1.6859 1.6059 1


D :

R

1.6667 1 1 1.9907 1.6859 0 1.6330 1 1 1 1.6667 1 1 1.6859 1.6330 0 1 1 1 1 1 1.6330 1.6059 1 1 0 1 1 1 1 1 1 1 1 1 0

 

 

![image 382](<2010-arkus-deriving-finite-sphere-packings_images/imageFile382.png>)

![image 383](<2010-arkus-deriving-finite-sphere-packings_images/imageFile383.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.84997R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.0887 0 1.5396 0.5443 0 0.4170 −0.3629 −0.8333 −0.2836 0.5443 −0.7895 0.9623 1.3608 0 0.9623 −0.2722 −0.0000 0.6736 0.5443 0.5000 0.6736 0.5443 −0.5000

C :

R

 

 

Packing 22 (Graph 5112):





0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 1 1 1 1 1 1 1 0 1 0 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1 1.9868 1 1 1 1.6330 0 1.0887 1.9907 1 1 1.6667 1 1 1.6330 1.0887 0 1.6667 1.6667 1 1 1 1
- 1 1.9907 1.6667 0 1.6667 2.4315 1 1 1.6330 1 1 1.6667 1.6667 0 1.6859 1.6330 1 1


D :

R

1.9868 1 1 2.4315 1.6859 0 1.6859 1.6059 1 1 1.6667 1 1 1.6330 1.6859 0 1 1 1 1 1 1 1 1.6059 1 0 1 1 1 1 1.6330 1 1 1 1 0

 

 

![image 384](<2010-arkus-deriving-finite-sphere-packings_images/imageFile384.png>)

![image 385](<2010-arkus-deriving-finite-sphere-packings_images/imageFile385.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.33875R2<br><br>|C1|1|chiral|






0 0 0 0 −1.6330 0 1.0264 −1.2701 0 0.5453 0 −0.8333 −0.5774 −0.8165

C :

R

- −0.0000 0.6077
- −1.7189 0.7895 0.9623


−0.2722 0 0.2887 −0.8165 −0.5000 0.2887 −0.8165 0.5000

 

 

Packing 23 (Graph 5116):





0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 1 1 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1 1.6667 1 1 1 1.0887 0 1.6330 1.7249 1 1 1.6667 1 1 1.6330 1.6330 0 1.6667 1.9868 1 1 1 1
- 1 1.7249 1.6667 0 1.9868 1.9907 1 1 1.6330 1 1 1.9868 1.9868 0 1.6859 1.6859 1.6059 1


D :

R

1.6667 1 1 1.9907 1.6859 0 1.6330 1 1 1 1.6667 1 1 1.6859 1.6330 0 1 1 1 1 1 1 1.6059 1 1 0 1 1 1 1 1.6330 1 1 1 1 0

 

 

![image 386](<2010-arkus-deriving-finite-sphere-packings_images/imageFile386.png>)

![image 387](<2010-arkus-deriving-finite-sphere-packings_images/imageFile387.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|7.14237R2|C1|1<br><br>|chiral|






0 0 0 0 −1.0887 0 1.5396 −0.5443 0 0.4170 0.3629 −0.8333 −0.2836

C :

- −0.5443 0.7895 0.9623
- −1.3608 −0.0000


R

0.9623 0.2722 −0.0000 0.6736 −0.5443 −0.5000 0.6736 −0.5443 0.5000

 

 

Packing 24 (Graph 5399):





0 0 0 1 1 0 1 0 1 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 0 1 1 0 1 1 0 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.7778 1 1 1.9907 1 1.6667 1 1.6330 0 1.6330 1.6667 1 1 1 1 1 1.7778 1.6330 0 1.8178 1.6667 1 1.9907 1 1
- 1 1.6667 1.8178 0 1.6330 1.7778 1 1.9907 1 1 1 1.6667 1.6330 0 1.6330 1 1 1


D :

R

1.9907 1 1 1.7778 1.6330 0 1.6667 1 1

1 1 1.9907 1 1 1.6667 0 1.6330 1 1.6667 1 1 1.9907 1 1 1.6330 0 1

 

 

1 1 1 1 1 1 1 1 0

![image 388](<2010-arkus-deriving-finite-sphere-packings_images/imageFile388.png>)

![image 389](<2010-arkus-deriving-finite-sphere-packings_images/imageFile389.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.43987R2|C2<br><br>|2|chiral|






0 0 0 0 1.6330 0 −1.4913 0.9677 0 −0.1104 0.2722 −0.9559 0 0.8165 0.5735 −0.9345 1.7237 −0.3441 0.4636 0.8165 −0.3441 −0.7726 1.3608 0.5735 −0.5298 0.8165 −0.2294

C :

R

 

 

###### *Packing 25 (Graph 5416):





0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 0 1 1 0 0 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.4142 1.4142 1 1 1.7321 1 1 1 1.4142 0 1.6330 1.7321 1 1 1 1 1 1.4142 1.6330 0 1.7321 1.9149 1 1.9149 1 1
- 1 1.7321 1.7321 0 1.7321 2.0000 1 1.7321 1 1 1 1.9149 1.7321 0 1.7321 1 1 1.4142


D :

R

1.7321 1 1 2.0000 1.7321 0 1.7321 1 1 1 1 1.9149 1 1 1.7321 0 1.4142 1 1 1 1 1.7321 1 1 1.4142 0 1 1 1 1 1 1.4142 1 1 1 0

 

 

![image 390](<2010-arkus-deriving-finite-sphere-packings_images/imageFile390.png>)

![image 391](<2010-arkus-deriving-finite-sphere-packings_images/imageFile391.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|7.11111R2|C1|1<br><br>|chiral|






0 0 0 0 −1.4142 0 1.3333

- −0.4714 0 0 0
- −1.0000 −0.5000 −0.7071


C :

R

0.5000 1.0000 −1.4142 −0.0000 −0.5000 −0.7071 −0.5000 0.5000 −0.7071 0.5000 0.5000 −0.7071 −0.5000

 

 

Packing 26 (Graph 5544):





0 0 0 1 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 0 0 1 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.6779 1.6779 1 1 1.9843 1 1.6532 1 1.6779 0 1.6180 1.9889 1 1 1.6180 1 1 1.6779 1.6180 0 1.1220 1.6180 1 1 1 1
- 1 1.9889 1.1220 0 1.6330 1.7566 1 1.7007 1 1 1 1.6180 1.6330 0 1.6180 1 1 1


D :

R

1.9843 1 1 1.7566 1.6180 0 1.6180 1 1

1 1.6180 1 1 1 1.6180 0 1 1 1.6532 1 1 1.7007 1 1 1 0 1.0515 1 1 1 1 1 1 1 1.0515 0

 

 

![image 392](<2010-arkus-deriving-finite-sphere-packings_images/imageFile392.png>)

![image 393](<2010-arkus-deriving-finite-sphere-packings_images/imageFile393.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.81739R2<br><br>|C1|1|chiral|






0 0 0 0 1.6779 0 1.4175 0.8978 0 0.9282 −0.0418 −0.3697 −0.1090 0.8390 0.5331 0.9435 1.7143 −0.3295 0.7671 0.3568 0.5331 0.7459 1.3554 0.5827 0.4617 0.8390 −0.2880

C :

R

 

 

Packing 27 (Graph 5835):





0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 1 1 1 1 0 1 1 0 1 0 1 1 1 1 0 0 1 1 1 0 0 1 1 1 1 1 1 1 0 0

A :

 

 





0 1.6180 1.6779 1 1 1.6180 1 1 1

- 1.6180 0 1.6779 1.9843 1 1 1.6180 1 1 1.6779 1.6779 0 1.1220 1.9843 1 1 1.6532 1

1 1.9843 1.1220 0 1.6779 1.6779 1 1.6532 1 1 1 1.9843 1.6779 0 1.6180 1.6180 1 1

- 1.6180 1 1 1.6779 1.6180 0 1 1 1 1 1.6180 1 1 1.6180 1 0 1 1 1 1 1.6532 1.6532 1 1 1 0 1.0515 1 1 1 1 1 1 1 1.0515 0


D :

R

 

 

![image 394](<2010-arkus-deriving-finite-sphere-packings_images/imageFile394.png>)

![image 395](<2010-arkus-deriving-finite-sphere-packings_images/imageFile395.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.78418R2|Cs|1| |






0 0 0 0 −1.6180 0 1.4700 −0.8090 0 0.9239 0 −0.3697 −0.4867 −0.8090 −0.3295 0.7876 −1.3090 0.5331 0.7876 −0.3090 0.5331 −0.0770 −0.8090 0.5827 0.5124 −0.8090 −0.2880

C :

R

 

 

Packing 28 (Graph 6031):





0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 1 1 0 0 0 0 1 1 0 0 1 1 0 0 0 1 1 1 1 1 1 0 1 1 0 0 1 1 1 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 0

A :

 

 





- 0 1.6180 1.6779 1 1 1.6180 1 1 1 1.6180 0 1.6779 1.9843 1 1 1 1 1.6180 1.6779 1.6779 0 1.9938 1.9843 1 1 1.6532 1
- 1 1.9843 1.9938 0 1.6779 1.6779 1.6532 1 1 1 1 1.9843 1.6779 0 1.6180 1 1 1.6180


D :

R

1.6180 1 1 1.6779 1.6180 0 1 1 1 1 1 1 1.6532 1 1 0 1.0515 1 1 1 1.6532 1 1 1 1.0515 0 1 1 1.6180 1 1 1.6180 1 1 1 0

 

 

![image 396](<2010-arkus-deriving-finite-sphere-packings_images/imageFile396.png>)

![image 397](<2010-arkus-deriving-finite-sphere-packings_images/imageFile397.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.08600R2<br><br>|C2|2|chiral|






0 0 0 0 1.6180 0 1.4700 0.8090 0 −0.0000 −0.0987 0.9951 −0.4867 0.8090 −0.3295 0.7876 1.3090 0.5331 0.5124 0.8090 −0.2880 −0.0770 0.8090 0.5827 0.7876 0.3090 0.5331

C :

R

 

 

Packing 29 (Graph 8901):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.4142 1.4142 1 1.7321 1 1 1 1 1.4142 0 1.6330 1.7321 1 1 1.9149 1 1 1.4142 1.6330 0 1.7321 1 1.9149 1 1 1
- 1 1.7321 1.7321 0 2.0000 1 1 1.7321 1


D :

1.7321 1 1 2.0000 0 1.7321 1.7321 1 1 1 1 1.9149 1 1.7321 0 1.6330 1.4142 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 1 1 1 1 1.7321 1 1.4142 1.4142 0 1 1 1 1 1 1 1 1 1 0

R

 

 

![image 398](<2010-arkus-deriving-finite-sphere-packings_images/imageFile398.png>)

![image 399](<2010-arkus-deriving-finite-sphere-packings_images/imageFile399.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.07407R2<br><br>|C2v|2<br><br>|non-rigid new seed|






0 0 0 0 1.4141 0 1.3335 0.4715 0 0 −0.0001 −1.0000 1.0000 1.4142 −0.0000

C :

R

- −0.4999 0.7070

−0.5002 0.8334 −0.2358 −0.4998 0.5001 0.7070 0.5000 0.5001 0.7070

- −0.5000


 

 

Packing 30 (Graph 8926):





0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 1 0 1 1 1 1 1 1 1 0

A :

 

 





0 1.6796 1.1832 1 1.7496 1 1 1 1.1272

1.6796 0 1.6330 1.6938 1 1 1.9667 1 1 1.1832 1.6330 0 1.6667 1 1.6667 1 1 1

1 1.6938 1.6667 0 1.9838 1 1 1.5920 1

D :

1.7496 1 1 1.9838 0 1.6330 1.7167 1 1 1 1 1.6667 1 1.6330 0 1.5920 1 1 1 1.9667 1 1 1.7167 1.5920 0 1.5345 1 1 1 1 1.5920 1 1 1.5345 0 1

R

 

 

1.1272 1 1 1 1 1 1 1 0

![image 400](<2010-arkus-deriving-finite-sphere-packings_images/imageFile400.png>)

![image 401](<2010-arkus-deriving-finite-sphere-packings_images/imageFile401.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.83165R2<br><br>|C1|1|chiral new seed<br><br>|






0 0 0 0 1.6796 0 1.0890 0.4628 0 −0.2939 0.2835 −0.9128 0.9716 1.4534 0 −0.5303 0.8398 −0.1162 0.6487 −0.0139 −0.7609 0.2860 0.8398 0.4615 0.3760 0.9204 −0.5312

C :

R

 

 

Packing 31 (Graph 8943):





0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 1 0 1 0 1 1 1 1 1 1 1 0

A :

 

 





0 1.7321 1.7321 1 2.2361 1 1 1 1.4142

1.7321 0 1.4142 1.7321 1 1 1.7321 1 1 1.7321 1.4142 0 1.7321 1 1.7321 1 1 1

1 1.7321 1.7321 0 2.0000 1 1 1.4142 1

D :

2.2361 1 1 2.0000 0 1.7321 1.7321 1.4142 1 1 1 1.7321 1 1.7321 0 1.4142 1 1 1 1.7321 1 1 1.7321 1.4142 0 1 1 1 1 1 1.4142 1.4142 1 1 0 1

R

 

 

1.4142 1 1 1 1 1 1 1 0

![image 402](<2010-arkus-deriving-finite-sphere-packings_images/imageFile402.png>)

![image 403](<2010-arkus-deriving-finite-sphere-packings_images/imageFile403.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.11111R2|Cs|1| |






0 0 0 0 1.7321 0 1.2910 1.1547 0 0.1291 0.2887 −0.9487 0.9037 2.0207 −0.3162 −0.3873 0.8660 −0.3162 0.9037 0.2887 −0.3162 0.3873 0.8660 0.3162 0.5164 1.1547 −0.6325

C :

R

 

 

Packing 32 (Graph 8955):





0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 0 0 1 1 1 0 1 0 1 1 1 1 1 1 1 0

A :

 

 





0 1.7321 1.9149 1 1.9149 1 1 1 1.4142

1.7321 0 1.7321 1.7321 1 1 1.7321 1 1 1.9149 1.7321 0 1.6330 1 1.9149 1 1.4142 1

1 1.7321 1.6330 0 1.9149 1 1 1.4142 1

D :

1.9149 1 1 1.9149 0 1.6330 1.4142 1 1 1 1 1.9149 1 1.6330 0 1.4142 1 1 1 1.7321 1 1 1.4142 1.4142 0 1 1 1 1 1.4142 1.4142 1 1 1 0 1

R

 

 

1.4142 1 1 1 1 1 1 1 0

![image 404](<2010-arkus-deriving-finite-sphere-packings_images/imageFile404.png>)

![image 405](<2010-arkus-deriving-finite-sphere-packings_images/imageFile405.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.00000R2<br><br>|C1|1|chiral|






0 0 0 0 1.7321 0 1.5957 1.0585 0 0.4352 0.2887 0.8528 0.8994 1.6358 −0.4264 −0.2611 0.8660 0.4264 0.9574 0.2887 −0.0000 0.2611 0.8660 −0.4264 0.6963 1.1547 0.4264

C :

R

 

 

Packing 33 (Graph 8959):





0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 1 0 1 1 0 0 0 1 1 0 1 1 0 1 1 1 0 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6859 1 1.9868 1 1 1.6059 1 1.6859 0 1.6330 1.9770 1 1 1.6667 1 1 1.6859 1.6330 0 1.9770 1 1.6667 1 1 1
- 1 1.9770 1.9770 0 2.3778 1 1 1.5789 1.6059


D :

1.9868 1 1 2.3778 0 1.6330 1.6330 1 1 1 1 1.6667 1 1.6330 0 1.0887 1 1 1 1.6667 1 1 1.6330 1.0887 0 1 1

R

 

 

1.6059 1 1 1.5789 1 1 1 0 1 1 1 1 1.6059 1 1 1 1 0

![image 406](<2010-arkus-deriving-finite-sphere-packings_images/imageFile406.png>)

![image 407](<2010-arkus-deriving-finite-sphere-packings_images/imageFile407.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.38824R2|Cs|1| |






0 0 0 0 1.6859 0 −1.4287 0.8950 0 0 −0.0197 0.9997 −0.9505 1.7171 −0.3090 0.1555 0.8429 0.5151 −0.7969 0.3157 0.5151 −0.7259 1.3112 0.5769 −0.4666 0.8429 −0.2678

C :

R

 

 

Packing 34 (Graph 9352):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 1 1 1 0 0 0 0 1 0 0 1 1 1 0 0 0 0 1 1 0 0 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 1 1 0 1 1 0 1 0 1 0 0 1 1 1 1 0 1 1 0 0 1 1 1 1 0 1 0 1 1 0

A :

 

 





- 0 1.4142 1.4142 1 1.7321 1 1 1 1 1.4142 0 1.6330 1.7321 1 1 1 1 1 1.4142 1.6330 0 2.3805 1 1.9149 1.9149 1 1
- 1 1.7321 2.3805 0 2.4495 1 1 1.7321 1.7321 1.7321 1 1 2.4495 0 1.7321 1.7321 1 1


D :

R

- 1 1 1.9149 1 1.7321 0 1 1 1.4142
- 1 1 1.9149 1 1.7321 1 0 1.4142 1 1 1 1 1.7321 1 1 1.4142 0 1 1 1 1 1.7321 1 1.4142 1 1 0


 

 

![image 408](<2010-arkus-deriving-finite-sphere-packings_images/imageFile408.png>)

![image 409](<2010-arkus-deriving-finite-sphere-packings_images/imageFile409.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.62963R2|Cs<br><br>|1| |






0 0 0 0 −1.4142 0 −1.3333

- −0.4714 0

1.0000 0 0

- −1.0000 −1.4142


C :

R

0 0.5000 −0.7071 −0.5000 0.5000 −0.7071 0.5000 −0.5000 −0.7071 −0.5000 −0.5000 −0.7071 0.5000

 

 

Packing 35 (Graph 9503):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 1 0 1 1 1 1 0 0 1 0 0 1 1 1 0 1 1 0 0 0 1 1 1 0 1 0 1 1 1 0 0 1 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.6779 1.6180 1 1.6180 1 1 1 1 1.6779 0 1.6779 1.8155 1 1 1.9843 1.6532 1 1.6180 1.6779 0 1.6779 1 1.6180 1 1 1
- 1 1.8155 1.6779 0 1.9843 1.6779 1 1.6532 1


D :

1.6180 1 1 1.9843 0 1 1.6180 1 1 1 1 1.6180 1.6779 1 0 1.6180 1 1 1 1.9843 1 1 1.6180 1.6180 0 1 1 1 1.6532 1 1.6532 1 1 1 0 1.0515 1 1 1 1 1 1 1 1.0515 0

R

 

 

![image 410](<2010-arkus-deriving-finite-sphere-packings_images/imageFile410.png>)

![image 411](<2010-arkus-deriving-finite-sphere-packings_images/imageFile411.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.01052R2|Cs|1| |






0 0 0 0 1.6779 0 −1.4175 0.7801 0 −0.1979 0.1548 −0.9679 −0.7671 1.3211 0.5331 0.1090 0.8390 0.5331 −0.9435 −0.0364 −0.3295 −0.7459 0.3226 0.5827 −0.4617 0.8390 −0.2880

C :

R

 

 

Packing 36 (Graph 9520):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 1 0 1 1 1 1 0 0 1 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 1 1 0 0 1 0 1 1 1 1 1 0 0

A :

 

 





- 0 1.6779 1.6180 1 1.6180 1 1 1 1 1.6779 0 1.6779 2.4520 1 1 1.9843 1 1.6532 1.6180 1.6779 0 1.6779 1 1.6180 1 1 1
- 1 2.4520 1.6779 0 1.9843 1.6779 1 1.6532 1


D :

1.6180 1 1 1.9843 0 1 1.6180 1 1 1 1 1.6180 1.6779 1 0 1.6180 1 1 1 1.9843 1 1 1.6180 1.6180 0 1 1 1 1 1 1.6532 1 1 1 0 1.0515 1 1.6532 1 1 1 1 1 1.0515 0

R

 

 

![image 412](<2010-arkus-deriving-finite-sphere-packings_images/imageFile412.png>)

![image 413](<2010-arkus-deriving-finite-sphere-packings_images/imageFile413.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.31234R2<br><br>|C2|2|chiral|






0 0 0 0 1.6779 0 1.4175 0.7801 0 0.6434 −0.6546 −0.3969 0.7671 1.3211 −0.5331 −0.1090 0.8390 −0.5331 0.9435 −0.0364 0.3295 0.4617 0.8390 0.2880 0.7459 0.3226 −0.5827

C :

R

 

 

Packing 37 (Graph 10279):





0 0 0 1 0 1 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 1 0 1 1 1 1 0 0 1 0 1 1 0 1 1 0 1 0 1 0 0 1 1 0 1 1 1 1 0 0 1 0 1 1 1 1 0 1 1 0

A :

 

 





0 1.7199 1.9591 1 1.7199 1 1 1 1.5130

- 1.7199 0 1.7221 1.7199 1 1 1 1.5130 1 1.9591 1.7221 0 1.5224 1 1.7204 1.8799 1 1

1 1.7199 1.5224 0 1.7199 1.5130 1 1 1

- 1.7199 1 1 1.7199 0 1 1.5130 1 1 1 1 1.7204 1.5130 1 0 1 1 1.2892 1 1 1.8799 1 1.5130 1 0 1.2892 1 1 1.5130 1 1 1 1 1.2892 0 1


D :

R

 

 

1.5130 1 1 1 1 1.2892 1 1 0

![image 414](<2010-arkus-deriving-finite-sphere-packings_images/imageFile414.png>)

![image 415](<2010-arkus-deriving-finite-sphere-packings_images/imageFile415.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|6.76986R2|C1|1<br><br>|chiral|






0 0 0 0 −1.7199 0 1.6118 −1.1135 0 0.5810 −0.2907 −0.7602 0.8106 −1.4292 0.5083 −0.0115 −0.8600 0.5102 −0.1897 −0.8600 −0.4738 0.8554 −0.4852 0.1815 0.7374 −1.2347 −0.4699

C :

R

 

 

###### *Packing 38 (Graph 10664):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 1 1 1 1 1 1 0 0 1 0 1 1 0 1 0 1 0 1 1 0 0 1 1 1 0 1 1 1 0 0 1 1 0 1 1 1 0 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 1.4142 1 1 1 1 1.7321 0 2.0000 2.0000 1 1 1.7321 1 1.7321 1.7321 2.0000 0 2.0000 1 1.7321 1 1.7321 1
- 1 2.0000 2.0000 0 1.7321 1.7321 1.7321 1 1


D :

1.4142 1 1 1.7321 0 1 1 1 1 1 1 1.7321 1.7321 1 0 1 1 1.4142 1 1.7321 1 1.7321 1 1 0 1.4142 1 1 1 1.7321 1 1 1 1.4142 0 1 1 1.7321 1 1 1 1.4142 1 1 0

R

 

 

![image 416](<2010-arkus-deriving-finite-sphere-packings_images/imageFile416.png>)

![image 417](<2010-arkus-deriving-finite-sphere-packings_images/imageFile417.png>)

|2nd Moment<br><br>|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|7.33333R2<br><br>|C3v|3| |






0 0 0 0 −1.7321 0 −1.6330 −0.5774 0 0 −0.0000 1.0000 −0.8165 −1.1547 −0.0000 0 −0.8660 −0.5000 −0.8165 −0.2887 −0.5000 −0.0000 −0.8660 0.5000 −0.8165 −0.2887 0.5000

C :

R

 

 

Packing 39 (Graph 10989):





0 0 0 1 0 0 1 1 1 0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 1 0 1 0 0 1 1 0 1 0 0 0 1 1 1 0 1 0 0 0 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1.4142 1 1.9149 1.9149 1 1 1 1.6330 0 1.4142 1.6667 1 1 1 1 1 1.4142 1.4142 0 1.9149 1 1 1.7321 1 1
- 1 1.6667 1.9149 0 2.3333 1.9437 1 1.6330 1 1.9149 1 1 2.3333 0 1 1.7321 1 1.4142 1.9149 1 1 1.9437 1 0 1.7321 1.4142 1 1 1 1.7321 1 1.7321 1.7321 0 1 1 1 1 1 1.6330 1 1.4142 1 0 1 1 1 1 1 1.4142 1 1 1 0


D :

R

 

 

![image 418](<2010-arkus-deriving-finite-sphere-packings_images/imageFile418.png>)

![image 419](<2010-arkus-deriving-finite-sphere-packings_images/imageFile419.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|7.37037R2|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.1547 0.8165 0 0.4811 0.2722 0.8333 −0.8660 1.6330 −0.5000 −0.8660 1.6330 0.5000 0.5774 0.8165 −0.0000 −0.2887 0.8165 −0.5000 −0.2887 0.8165 0.5000

C :

R

 

 

Packing 40 (Graph 10997):





0 0 0 1 0 0 1 1 1 0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 1 0 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 1 0 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.7778 1 1.6667 1.9907 1 1 1 1.6330 0 1.6330 1.6667 1 1 1 1 1 1.7778 1.6330 0 2.5035 1 1 1.9907 1.6667 1
- 1 1.6667 2.5035 0 1.9907 2.4369 1 1 1.6330


D :

1.6667 1 1 1.9907 0 1 1.6330 1 1 1.9907 1 1 2.4369 1 0 1.6667 1.6330 1

R

1 1 1.9907 1 1.6330 1.6667 0 1 1 1 1 1.6667 1 1 1.6330 1 0 1 1 1 1 1.6330 1 1 1 1 0

 

 

![image 420](<2010-arkus-deriving-finite-sphere-packings_images/imageFile420.png>)

![image 421](<2010-arkus-deriving-finite-sphere-packings_images/imageFile421.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.07773R2<br><br>|C1|1|chiral|






0 0 0 0 −1.6330 0 1.4913 −0.9677 0 −0.8830 −0.2722 −0.3824 0.7726 −1.3608 −0.5735 0.9345 −1.7237 0.3441 −0.4636 −0.8165 0.3441 −0.0662 −0.8165 −0.5735 0.5298 −0.8165 0.2294

C :

R

 

 

Packing 41 (Graph 11229):





0 0 0 1 0 0 1 1 1 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 1 1 1 0 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 1 1 1 0

A :

 

 





- 0 1.6779 1.6779 1 1.6532 1.9843 1 1 1 1.6779 0 1.6180 1.9889 1 1 1 1.6180 1 1.6779 1.6180 0 1.9889 1 1 1.6180 1 1
- 1 1.9889 1.9889 0 1.6482 2.4047 1 1 1.6330 1.6532 1 1 1.6482 0 1 1 1 1.0515 1.9843 1 1 2.4047 1 0 1.6180 1.6180 1 1 1 1.6180 1 1 1.6180 0 1 1 1 1.6180 1 1 1 1.6180 1 0 1 1 1 1 1.6330 1.0515 1 1 1 0


D :

R

 

 

![image 422](<2010-arkus-deriving-finite-sphere-packings_images/imageFile422.png>)

![image 423](<2010-arkus-deriving-finite-sphere-packings_images/imageFile423.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.39711R2|Cs|1| |






0 0 0 0 −1.6779 0 1.4175

- −0.8978 0

−0.0230 0 0.9989 0.7459 −1.3554 0.5827 0.9435

- −1.7143 −0.3295 −0.1090 −0.8390


C :

R

0.5331 0.7671 −0.3568 0.5331 0.4617 −0.8390 −0.2880

 

 

Packing 42 (Graph 11245):





0 0 0 1 0 0 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 1 1 0 1 0 1 1 0 1 0 0 1 1 1 1 0 1 1 0 0 1 1 1 1 0 1 0 1 1 0 1 1 0 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 2.0000 1 1.7321 1.7321 1 1 1 1.7321 0 1.7321 1.4142 1 1 1 1 1.4142 2.0000 1.7321 0 2.5166 1 1 1.7321 1.7321 1
- 1 1.4142 2.5166 0 1.9149 1.9149 1 1 1.6330


D :

- 1.7321 1 1 1.9149 0 1 1 1.4142 1
- 1.7321 1 1 1.9149 1 0 1.4142 1 1 1 1 1.7321 1 1 1.4142 0 1 1 1 1 1.7321 1 1.4142 1 1 0 1 1 1.4142 1 1.6330 1 1 1 1 0


R

 

 

![image 424](<2010-arkus-deriving-finite-sphere-packings_images/imageFile424.png>)

![image 425](<2010-arkus-deriving-finite-sphere-packings_images/imageFile425.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.48148R2|Cs<br><br>|1| |






0 0 0 0 −1.7321 0 −1.6330 −1.1547 0 0.8165 −0.5774 −0.0000 −0.8165 −1.4434 −0.5000 −0.8165 −1.4434 0.5000 0 −0.8660 −0.5000 −0.0000 −0.8660 0.5000 −0.8165 −0.5774 −0.0000

C :

R

 

 

Packing 43 (Graph 11633):





0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 0 1 0 1 1 0 0 1 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 0 1 0 0 1 1 1 1 0 0 1 1 1 0 0 1 0 1 1 1 1 1 0 0

A :

 

 





- 0 1.7321 1.7321 1 1.4142 1 1 1 1 1.7321 0 1.4142 2.4495 1 1.7321 1 1 1.7321 1.7321 1.4142 0 2.0000 1 1.7321 1 1.7321 1
- 1 2.4495 2.0000 0 1.7321 1 1.7321 1.7321 1


D :

1.4142 1 1 1.7321 0 1 1 1 1 1 1.7321 1.7321 1 1 0 1.4142 1 1 1 1 1 1.7321 1 1.4142 0 1 1 1 1 1.7321 1.7321 1 1 1 0 1.4142 1 1.7321 1 1 1 1 1 1.4142 0

R

 

 

![image 426](<2010-arkus-deriving-finite-sphere-packings_images/imageFile426.png>)

![image 427](<2010-arkus-deriving-finite-sphere-packings_images/imageFile427.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.33333R2|Cs|1| |






0 0 0 0 −1.7321 0 1.2910 −1.1547 0 0.5164 0.5774 −0.6325 0.5164 −1.1547 −0.6325 0.1291 −0.2887 −0.9487 0.3873 −0.8660 0.3162 −0.3873 −0.8660 −0.3162 0.9037 −0.2887 −0.3162

C :

R

 

 

Packing 44 (Graph 11998):





0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 1 0 1 0 1 1 0 0 1 0 0 0 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 1 1 1 0 0 1 1 0 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1 1.6667 1 1 1 1.6330 0 1.6330 1.6667 1.9907 1 1 1 1 1.0887 1.6330 0 1.7249 1.1529 1 1.6667 1 1
- 1 1.6667 1.7249 0 1 1.9907 1 1.6330 1 1 1.9907 1.1529 1 0 1.7778 1.6330 1.6667 1


D :

R

1.6667 1 1 1.9907 1.7778 0 1.6330 1 1 1 1 1.6667 1 1.6330 1.6330 0 1 1 1 1 1 1.6330 1.6667 1 1 0 1 1 1 1 1 1 1 1 1 0

 

 

![image 428](<2010-arkus-deriving-finite-sphere-packings_images/imageFile428.png>)

![image 429](<2010-arkus-deriving-finite-sphere-packings_images/imageFile429.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|6.89118R2|C1<br><br>|1|chiral|






0 0 0 0 −1.6330 0 1.0264 −0.3629 0 −0.4811

- −0.2722 0.8333 0.4491

0 0.8889 0.9623

- −1.3608 −0.0000 −0.5774 −0.8165


C :

R

0 0.2887 −0.8165 −0.5000 0.2887 −0.8165 0.5000

 

 

Packing 45 (Graph 12163):





0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 0 1 0 0 0 1 0 0 1 1 0 0 0 1 0 1 1 1 1 0 0 1 0 1 1 1 1 0 1 1 0 1 0 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1 1.6667 1 1 1 1.6330 0 1.6330 1.6667 1.9907 1 1 1 1 1.0887 1.6330 0 1.7249 2.0718 1 1 1.6667 1
- 1 1.6667 1.7249 0 1 1.9907 1.6330 1 1 1 1.9907 2.0718 1 0 2.4369 1.6667 1 1.6330


D :

R

1.6667 1 1 1.9907 2.4369 0 1 1.6330 1 1 1 1 1.6330 1.6667 1 0 1 1 1 1 1.6667 1 1 1.6330 1 0 1 1 1 1 1 1.6330 1 1 1 0

 

 

![image 430](<2010-arkus-deriving-finite-sphere-packings_images/imageFile430.png>)

![image 431](<2010-arkus-deriving-finite-sphere-packings_images/imageFile431.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|7.52904R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.0264 −0.3629 0 −0.4811 −0.2722 −0.8333 −0.9943 0 −0.0556 0.9623 −1.3608 0 0.2887 −0.8165 0.5000 −0.5774 −0.8165 −0.0000 0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 46 (Graph 12180):





0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 0 1 0 0 0 0 1 0 1 1 0 0 0 1 1 1 1 1 1 0 0 1 0 1 1 1 1 0 1 0 1 1 0 1 1 0 1 1 1 1 1 1 0

A :

 

 





0 1.6667 1.6667 1 1 1.6330 1 1 1 1.6667 0 1.6667 1.9907 2.4369 1 1 1 1.6330 1.6667 1.6667 0 1.9907 1.7778 1 1 1.6330 1 1 1.9907 1.9907 0 1 1.6667 1.6330 1 1 1 2.4369 1.7778 1 0 1.9907 1.6667 1.6330 1

D :

R

1.6330 1 1 1.6667 1.9907 0 1 1 1 1 1 1 1.6330 1.6667 1 0 1 1 1 1 1.6330 1 1.6330 1 1 0 1 1 1.6330 1 1 1 1 1 1 0

 

 

![image 432](<2010-arkus-deriving-finite-sphere-packings_images/imageFile432.png>)

![image 433](<2010-arkus-deriving-finite-sphere-packings_images/imageFile433.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|7.68999R2<br><br>|C1|1|chiral|






0 0 0 0 1.6667 0 −1.4434 0.8333 0 0 −0.0556 −0.9979 −0.5880 −0.6481 −0.4838 −0.7698 1.3333 −0.5443 −0.4811 0.8333 0.2722 0 0.8333 −0.5443 −0.7698 0.3333 −0.5443

C :

R

 

 

Packing 47 (Graph 12239):





0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 0 0 0 1 0 1 0 1 1 0 0 1 0 0 0 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 0 1 0 1 1 1 0 1 0 1 1 1 0 1 0 1 1 1 1 1 1 1 0

A :

 

 





0 1.9149 1.9149 1 1 1.7321 1 1 1.4142

1.9149 0 1.6667 1.4142 1.9149 1 1 1.6330 1 1.9149 1.6667 0 1.9149 1.4142 1 1.6330 1 1

1 1.4142 1.9149 0 1 1.7321 1 1.4142 1 1 1.9149 1.4142 1 0 1.7321 1.4142 1 1

D :

R

1.7321 1 1 1.7321 1.7321 0 1 1 1 1 1 1.6330 1 1.4142 1 0 1 1 1 1.6330 1 1.4142 1 1 1 0 1

 

 

1.4142 1 1 1 1 1 1 1 0

![image 434](<2010-arkus-deriving-finite-sphere-packings_images/imageFile434.png>)

![image 435](<2010-arkus-deriving-finite-sphere-packings_images/imageFile435.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|6.97531R2|Cs|1| |






0 0 0 0 1.9149 0 1.5006 1.1895 0 −0.2188 0.6963 0.6836 0.6816 0.2611 0.6836 0.7152 1.4797 −0.5469 −0.0926 0.9574 −0.2734 0.8078 0.5222 −0.2734 0.5890 1.2185 0.4102

C :

R

 

 

Packing 48 (Graph 12811):





0 0 0 1 1 0 1 0 1 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 1 0 0 1 1 0 1 1 1 0 0 1 1 1 1 1 1 0 0 0

A :

 

 





- 0 1.6071 1.6981 1 1 1.9707 1 1.6426 1 1.6071 0 1.6071 1 1.5827 1 1 1 1 1.6981 1.6071 0 1.9707 1 1 1.6426 1 1
- 1 1 1.9707 0 1.6071 1.6981 1 1.6426 1 1 1.5827 1 1.6071 0 1.6071 1 1 1


D :

R

1.9707 1 1 1.6981 1.6071 0 1.6426 1 1

1 1 1.6426 1 1 1.6426 0 1 1.0853 1.6426 1 1 1.6426 1 1 1 0 1.0853 1 1 1 1 1 1 1.0853 1.0853 0

 

 

![image 436](<2010-arkus-deriving-finite-sphere-packings_images/imageFile436.png>)

![image 437](<2010-arkus-deriving-finite-sphere-packings_images/imageFile437.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|6.72417R2|C2v<br><br>|2<br><br>|new seed|






0 0 0 0 1.6071 0 −1.4418 0.8971 0 0.5000 0.8035 0.3230 −0.7913 0.3353 −0.5112 −0.9418 1.7007 0.3230 0 0.8035 −0.5886 −0.7601 1.3319 −0.5886 −0.5000 0.8035 0.3230

C :

R

 

 

Packing 49 (Graph 13380):





0 0 0 1 1 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 1 1 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 0 1 1 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0

A :

 

 





0 1.7247 1.7247 1 1 1.6507 1 1 1.6507

1.7247 0 1.7247 1 1.6507 1 1 1.6507 1 1.7247 1.7247 0 1.6507 1 1 1.6507 1 1

1 1 1.6507 0 1.4142 1 1 1 1.4142 1 1.6507 1 1.4142 0 1.4142 1 1 1

D :

R

1.6507 1 1 1 1.4142 0 1.4142 1 1 1 1 1.6507 1 1 1.4142 0 1.4142 1 1 1.6507 1 1 1 1 1.4142 0 1.4142

 

 

1.6507 1 1 1.4142 1 1 1 1.4142 0

![image 438](<2010-arkus-deriving-finite-sphere-packings_images/imageFile438.png>)

![image 439](<2010-arkus-deriving-finite-sphere-packings_images/imageFile439.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|∗6.47474R2|D3h<br><br>|6<br><br>|new seed|






0 0 0 0 −1.7247 0 −1.4937 −0.8624 0 0 −0.8624 0.5000 −0.7866 −0.3624 −0.5000 −0.7866 −1.3624 0.5000 0 −0.8624 −0.5000 −0.7866 −0.3624 0.5000 −0.7866 −1.3624 −0.5000

C :

R

 

 

Packing 50 (Graph 13521):





0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 1 0 1 0 0 0 1 1 1 1 1 1 0 0 0 1 1 1 1 0 0 1 1 1 0 1 0 0 1 1 1 1 1 1 0

A :

 

 





0 1.6330 1 1.9149 1 1.9149 1 1 1.4142 1.6330 0 1.9149 1 1.9149 1 1 1 1.4142 1 1.9149 0 1.6330 1 1.9149 1 1.4142 1

1.9149 1 1.6330 0 1.9149 1 1 1.4142 1 1 1.9149 1 1.9149 0 1.6330 1.4142 1 1

D :

R

1.9149 1 1.9149 1 1.6330 0 1.4142 1 1 1 1 1 1 1.4142 1.4142 0 1 1 1 1 1.4142 1.4142 1 1 1 0 1

 

 

1.4142 1.4142 1 1 1 1 1 1 0

![image 440](<2010-arkus-deriving-finite-sphere-packings_images/imageFile440.png>)

![image 441](<2010-arkus-deriving-finite-sphere-packings_images/imageFile441.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.00000R2|D3h<br><br>|6<br><br>|new seed|






0 0 0 0 −1.6330 0 −1.0000 0 0 −1.0000 −1.6330 0 −0.5000 0 0.8660 −0.5000 −1.6330 0.8660 −0.5000 −0.8165 −0.2887 −0.0000

C :

R

- −0.8165 0.5774
- −1.0000 −0.8165


 

 

0.5774

Packing 51 (Graph 13576):





0 0 1 0 1 0 1 1 1 0 0 0 1 0 1 1 1 1 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 1 1 0 1 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 1 1 0 1 0 0 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 1 0

A :

 

 





- 0 1.6330 1 1.6667 1 1.9907 1 1 1 1.6330 0 1.6667 1 1.9907 1 1 1 1
- 1 1.6667 0 1.9907 1 2.4369 1 1.6330 1 1.6667 1 1.9907 0 2.4369 1 1.6330 1 1


D :

1 1.9907 1 2.4369 0 2.5402 1 1.6667 1.6330 1.9907 1 2.4369 1 2.5402 0 1.6667 1 1.6330 1 1 1 1.6330 1 1.6667 0 1 1 1 1 1.6330 1 1.6667 1 1 0 1 1 1 1 1 1.6330 1.6330 1 1 0

R

 

 

![image 442](<2010-arkus-deriving-finite-sphere-packings_images/imageFile442.png>)

![image 443](<2010-arkus-deriving-finite-sphere-packings_images/imageFile443.png>)

|2nd Moment|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|8.40695R2|C2|2<br><br>|chiral|






0 0 0 0 −1.6330 0 −0.9623 −0.2722 0 0.4811 −1.3608 0.8333 −0.5453 0 −0.8333 0.9943 −1.7237 0 −0.2887 −0.8165 −0.5000 0.5774 −0.8165 −0.0000 −0.2887 −0.8165 0.5000

C :

R

 

 

Packing 52 (Graph 13700):





0 0 1 0 1 1 0 1 1 0 0 0 1 0 1 1 1 0 1 0 0 0 1 0 1 1 1 0 1 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 1 0 1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 0 0

A :

 

 





0 1.7199 1 1.7199 1 1 1.5130 1 1

- 1.7199 0 1.7199 1 2.3494 1 1 1 1.5130 1 1.7199 0 1.7199 1 1.5130 1 1 1
- 1.7199 1 1.7199 0 1.9998 1 1 1.5130 1 1 2.3494 1 1.9998 0 1.7221 1.7221 1.7204 1 1 1 1.5130 1 1.7221 0 1.2892 1 1


D :

R

1.5130 1 1 1 1.7221 1.2892 0 1 1 1 1 1 1.5130 1.7204 1 1 0 1.2892 1 1.5130 1 1 1 1 1 1.2892 0

 

 

![image 444](<2010-arkus-deriving-finite-sphere-packings_images/imageFile444.png>)

![image 445](<2010-arkus-deriving-finite-sphere-packings_images/imageFile445.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.08037R2|Cs<br><br>|1| |






0 0 0 0 −1.7199 0 −0.9568 −0.2907 0 −0.0883 −1.4292 −0.9527 −0.6605 0.4539 −0.5981 0.4124 −0.8600 −0.3006 −0.8211 −1.2347 −0.3006 −0.2613 −0.8600 0.4384 −0.3752 −0.4852 −0.7898

C :

R

 

 

3. Packings of n = 10 Particles

Here we include the 262 10 particle packings25. The ‘special properties’ column denotes whether a packing is chiral, corresponds to a new seed, to a non-rigid structure, or to a packing with > 3n−6 contacts. If this column is blank, then that packing has none of these properties. There are 201 chiral packings, 8 new seeds (graphs 308923, 618718, 622587, 629072, 665570, 679397, 714961, and 749808), 4 non-rigid packings (Graph 665570 corresponds to the packing that is both a new seed and a non-rigid structure, and graphs 286981, 457749, and 593702 (packings 84, 145, and 197) correspond to the 10 particle non-rigid packings that are derived from the 9 particle non-rigid new seed; 9 particle graph 8901)26, and 3 packings with 3n − 5 = 25 contacts (packings 259-262). The minimum of the 2nd moment corresponds to packing 257, graph 749808.

Note that for the 25 contact packings, we have included all graphs that lead to these packings; thus multiple graphs are listed under the same packing header. Because of this, we have listed all 25 contact packings at the end; these are the only packings that are listed out of chronological graph order. For these graphs, we have included their associated distance matrix and coordinates, as these can be diﬀerent up to particle labeling degeneracy (i.e. they can be isomorphic but not identical), but we have only included the table with the 2nd moment, φ, σ, and the special properties once, as this will always be identical.

A star, ‘*’, appears in front of packings that are reported here but were not reported in our last paper (PRL, 103, 118303). A double star, ‘**’, appears in front of packings that are reported here but were not reported previously by us or by Hoy and O’Hern (PRL, 105, 068001). We have also included markings next to the relevant graphs that correspond to 25 contact packings which were not found in these papers; however, note that this did not aﬀect the number of packings reported in either of these papers as multiple graphs lead to the same 25 contact packings, and in both papers all 3 25 contact packings were found. In front of these graphs, a ‘*’ appears for ones not found in (PRL, 103, 118303), and a ‘+’ appears for ones not found in (PRL, 105, 068001)27.

- 25Note that for these 10 particle packings, the packing ﬁgures were generated by code that John Lee wrote that

interfaces the packing output with the mayavi2 graphing package. And the point groups and symmetry numbers were also obtained via code that John Lee wrote that interfaces the packing output with the rotational constant calculator website (http://www.colby.edu/chemistry/PChem/scripts/ABC.html) that calculates these numbers.

- 26Note that while the 3 non-rigid packings based on the 9 particle non-rigid new seed were reported in (PRL,


103, 118303) and the PhD Thesis (http://people.seas.harvard.edu/∼narkus/assets/Thesis.pdf.zip), they were not found by the old code. We had reported them because we had already solved for their coordinates. We made a note of this where the packings were listed, and mentioned that we suspected these 3 packings had been missed due to round-oﬀ error, which we knew to be an issue. Thus, while a star does not appear next to these packings because they were previously reported, if one were to compare raw output of the old and new code, these 3 matrices would also lie in the category that the old code misses and the new modiﬁed code picks up.

27Rob Hoy sent us the raw data he used for the paper (PRL, 105, 068001). It was comparing this data to our data that allowed us to determine which graphs (ones that uniquely or redundantly correspond to packings) appear here but were not reported in (PRL, 105, 068001).

Packing 1 (Graph 4471):





- 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 1

- 0 0 0 0 0 0 1 1 1 0

- 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 1
- 0 0 1 1 1 0 0 1 1 1


- 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 1 1 0 1


- 1 1 0 1 1 1 1 1 1 0


A :

 

 





- 0 1.6667 1.9907 1.0887 1.9907 1 1.6667 1 1.6330 0

1.6667 0 1.9907 1.9907 1.0887 1 1.6667 1.6330 1 0 1.9907 1.9907 0 1.6667 1.6667 1.6667 1 1 1 0 1.0887 1.9907 1.6667 0 1.6667 1.6667 1 1 1.6330 0 1.9907 1.0887 1.6667 1.6667 0 1.6667 1 1.6330 1 0

- 1 1 1.6667 1.6667 1.6667 0 1.6330 1 1 0


D :

R

1.6667 1.6667 1 1 1 1.6330 0 1 1 0 1 1.6330 1 1 1.6330 1 1 0 1 0 1.6330 1 1 1.6330 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 446](<2010-arkus-deriving-finite-sphere-packings_images/imageFile446.png>)

![image 447](<2010-arkus-deriving-finite-sphere-packings_images/imageFile447.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.32222R2|Cs<br><br>|1| |






0 0 0 0 1.6667 0 1.8079 0.8333 0 0.6556 −0.0000 −0.8692 0.6556 1.6667 −0.8692 0.2202 0.8333 0.5070 1.2036 0.8333 −0.7967 0.9424 0.3333 0 0.9424 1.3333 0 0.2510 0.8333 −0.4925

C :

R

 

 

###### *Packing 2 (Graph 12803):





0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 0 1 0 1 1 0 0 1 1 0 1 0 1 1 1 0 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1.7321 1.7321 1 1 1 1 0 1.7321 0 1.4142 1.4142 2.0000 1 1.7321 1 1.7321 0 1.7321 1.4142 0 2.0000 1.4142 1 1.7321 1.7321 1 0 1.7321 1.4142 2.0000 0 1.4142 1.7321 1 1 1.7321 0 1.7321 2.0000 1.4142 1.4142 0 1.7321 1 1.7321 1 0
- 1 1 1 1.7321 1.7321 0 1.4142 1 1 0 1 1.7321 1.7321 1 1 1.4142 0 1 1 0 1 1 1.7321 1 1.7321 1 1 0 1.4142 0 1 1.7321 1 1.7321 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 448](<2010-arkus-deriving-finite-sphere-packings_images/imageFile448.png>)

![image 449](<2010-arkus-deriving-finite-sphere-packings_images/imageFile449.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.20000R2|C4v|4| |






0 0 0 0 −1.7321 0 −1.2910 −1.1547 0 0.2582 −1.1547 1.2649 −1.0328 −0.5774 1.2649 −0.3873 −0.8660 −0.3162 −0.1291 −0.2887 0.9487 0.3873 −0.8660 0.3162 −0.9037 −0.2887 0.3162 −0.5164 −1.1547 0.6325

C :

R

 

 

Packing 3 (Graph 17438):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 1 0 1 1 1 0 1 0 1 1

A :

 

 

- 0 1 1 1 0 1 1 1 0 1
- 1 1 0 1 1 1 1 1 1 0






- 0 1.6667 1.6667 1.6667 1 1.9907 1 1 1.6330 0 1.6667 0 1.6667 1.6667 1.9907 1 1 1.6330 1 0 1.6667 1.6667 0 1.6667 1.9907 1.9907 1 1 1 0 1.6667 1.6667 1.6667 0 1.0887 1.0887 1.6330 1 1 0
- 1 1.9907 1.9907 1.0887 0 1.7778 1.6330 1 1.6667 0


D :

R

1.9907 1 1.9907 1.0887 1.7778 0 1.6330 1.6667 1 0 1 1 1 1.6330 1.6330 1.6330 0 1 1 0 1 1.6330 1 1 1 1.6667 1 0 1 0

 

 

1.6330 1 1 1 1.6667 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 450](<2010-arkus-deriving-finite-sphere-packings_images/imageFile450.png>)

![image 451](<2010-arkus-deriving-finite-sphere-packings_images/imageFile451.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.36049R2|Cs<br><br>|1| |






0 0 0 0 −1.6667 0 −1.4434 −0.8333 0 −0.4811

- −0.8333 1.3608

0 0 0.9979 0

- −1.7222 0.9979


C :

R

−0.4811 −0.8333 −0.2722 −0.7698 −0.3333 0.5443 −0.7698 −1.3333 0.5443 0 −0.8333 0.5443

 

 

Packing 4 (Graph 18823):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 1 0 1 0 1 0 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1.6667 1 1.9907 1 1 1.6330 0 1.6667 0 1.6667 1.6667 1.0887 1 1.6330 1 1 0 1.6667 1.6667 0 1.6667 1.9907 1.9907 1 1 1 0 1.6667 1.6667 1.6667 0 1.9907 1.0887 1 1.6330 1 0
- 1 1.0887 1.9907 1.9907 0 1.7249 1.6330 1 1.6667 0


D :

R

1.9907 1 1.9907 1.0887 1.7249 0 1.6667 1.6330 1 0 1 1.6330 1 1 1.6330 1.6667 0 1 1 0 1 1 1 1.6330 1 1.6330 1 0 1 0

 

 

1.6330 1 1 1 1.6667 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 452](<2010-arkus-deriving-finite-sphere-packings_images/imageFile452.png>)

![image 453](<2010-arkus-deriving-finite-sphere-packings_images/imageFile453.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.34198R2|C1|1<br><br>|chiral|






0 0 0 0 1.6667 0 −1.4434 0.8333 0 −0.4811 0.8333 −1.3608 0.5132 0.7778 0.3629 0 1.7222 −0.9979 −0.7698 0.3333 −0.5443 −0.4811 0.8333 0.2722 −0.7698 1.3333 −0.5443 0 0.8333 −0.5443

C :

R

 

 

Packing 5 (Graph 23979):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 0 1 0 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1.6667 1 1.9907 1 1.6330 1 0 1.6667 0 1.6667 1.6667 1.9907 1 1.6330 1 1 0 1.6667 1.6667 0 1.6667 1.0887 1.9907 1 1 1 0 1.6667 1.6667 1.6667 0 1.9907 1.0887 1 1 1.6330 0
- 1 1.9907 1.0887 1.9907 0 2.4369 1 1.6667 1 0 1.9907 1 1.9907 1.0887 2.4369 0 1.6667 1 1.6330 0 1 1.6330 1 1 1 1.6667 0 1 1 0


D :

R

1.6330 1 1 1 1.6667 1 1 0 1 0 1 1 1 1.6330 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 454](<2010-arkus-deriving-finite-sphere-packings_images/imageFile454.png>)

![image 455](<2010-arkus-deriving-finite-sphere-packings_images/imageFile455.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.63827R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 −1.6667 0 1.4434 −0.8333 0 0.4811 −0.8333 1.3608 0.9302 0 −0.3629

C :

R

- −0.0321
- −1.7222 0.9979 0.7698


- −0.3333 0.5443 0.7698
- −1.3333 0.5443 0.4811


−0.8333 −0.2722 −0.0962 −0.8333 0.5443

 

 

Packing 6 (Graph 26619):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1 0 1 1 0 1 1 1 0 1 0 1 1 1 1 1 0 1 1 0 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1.0887 1 1 1.6667 1 1 0 1.6330 0 1.0887 1.9959 1.9907 1 1.7249 1.6667 1 0 1.6330 1.0887 0 1.6330 1.6667 1.6667 1 1 1 0 1.0887 1.9959 1.6330 0 1.7249 1.7249 1 1 1.6667 0
- 1 1.9907 1.6667 1.7249 0 1.6667 1.9907 1 1 0 1 1 1.6667 1.7249 1.6667 0 1.9907 1.6330 1 0


D :

R

1.6667 1.7249 1 1 1.9907 1.9907 0 1 1.6330 0 1 1.6667 1 1 1 1.6330 1 0 1 0 1 1 1 1.6667 1 1 1.6330 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 456](<2010-arkus-deriving-finite-sphere-packings_images/imageFile456.png>)

![image 457](<2010-arkus-deriving-finite-sphere-packings_images/imageFile457.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.38354R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.0264 −1.2701 0 −0.6272 0 −0.8889 −0.5453 0 0.8333 0.5774 −0.8165 0 −1.2295 −0.7560 −0.8333 −0.9623 −0.2722 −0.0000 −0.2887 −0.8165 0.5000 −0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 7 (Graph 26632):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6667 1.6667 1 1 1.6330 1 1 0 1.6330 0 1.7249 1.7249 1.9907 1 1.0887 1.6667 1 0 1.6667 1.7249 0 1.6667 1.9907 1.9907 1 1 1 0 1.6667 1.7249 1.6667 0 1.0887 1.9907 1 1 1.6330 0
- 1 1.9907 1.9907 1.0887 0 1.6667 1.6667 1 1.6330 0 1 1 1.9907 1.9907 1.6667 0 1.6667 1.6330 1 0


D :

R

1.6330 1.0887 1 1 1.6667 1.6667 0 1 1 0 1 1.6667 1 1 1 1.6330 1 0 1 0 1 1 1 1.6330 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 458](<2010-arkus-deriving-finite-sphere-packings_images/imageFile458.png>)

![image 459](<2010-arkus-deriving-finite-sphere-packings_images/imageFile459.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.36173R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.4853 0.7560 0 −0.5503 0.7560 −1.3796 0 −0.0907 −0.9957 0.4779 0.8165 0.3239 −0.8496 1.2701 −0.5759 −0.7965 0.2722 −0.5399 −0.5195 0.8165 0.2519 0 0.8165 −0.5759

C :

R

 

 

Packing 8 (Graph 29760):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 1 0 1 1 1 0 0 0 1 1 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6859 1.6859 1 1 1.6667 1 1 0 1.6330 0 1.6859 1.6859 1.9907 1 1 1.6667 1 0 1.6859 1.6859 0 1.5789 1.9868 1.9868 1 1 1 0 1.6859 1.6859 1.5789 0 1.1471 1.9868 1 1 1.6059 0
- 1 1.9907 1.9868 1.1471 0 1.6667 1.7249 1 1.6330 0 1 1 1.9868 1.9868 1.6667 0 1.6330 1.6330 1 0


D :

R

1.6667 1 1 1 1.7249 1.6330 0 1.0887 1 0 1 1.6667 1 1 1 1.6330 1.0887 0 1 0 1 1 1 1.6059 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 460](<2010-arkus-deriving-finite-sphere-packings_images/imageFile460.png>)

![image 461](<2010-arkus-deriving-finite-sphere-packings_images/imageFile461.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.33007R2|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.4749 0.8165 0 0.6298 0.8165 1.3337 0 −0.0907 0.9958 −0.4877 0.8165 −0.3090 0.8128 1.3608 0.5151 0.8128 0.2722 0.5151 0.5115 0.8165 −0.2678 −0.0238 0.8165 0.5769

C :

R

 

 

Packing 9 (Graph 31998):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 1 0 1 1 1 0 0 0 1 1 1 0 0 1 1 1 0 1 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.9907 1.9907 1 1 1.6667 1.6330 1 0 1.0887 0 1.6667 1.6667 1.6667 1 1 1.6330 1 0 1.9907 1.6667 0 1.6667 1.6667 2.4315 1 1 1 0 1.9907 1.6667 1.6667 0 1.6667 1.8113 1 1 1.6330 0
- 1 1.6667 1.6667 1.6667 0 1.6859 1.6330 1 1 0 1 1 2.4315 1.8113 1.6859 0 1.6859 1.9868 1.6059 0


D :

R

1.6667 1 1 1 1.6330 1.6859 0 1 1 0 1.6330 1.6330 1 1 1 1.9868 1 0 1 0

 

 

1 1 1 1.6330 1 1.6059 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 462](<2010-arkus-deriving-finite-sphere-packings_images/imageFile462.png>)

![image 463](<2010-arkus-deriving-finite-sphere-packings_images/imageFile463.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.72924R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.0887 0 1.6667 1.0887 0 0.8333 1.0887 −1.4434 0.8333 −0.2722 −0.4811 −0.6404 0.5443 −0.5419 0.8333 1.3608 −0.4811 1.3333 0.5443 −0.7698 0.8333 0.5443 0 0.3333 0.5443 −0.7698

C :

R

 

 

Packing 10 (Graph 32015):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1 0 0 1 1 1 0 1 0 1 1 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.7249 1.7249 1 1 1.6667 1.0887 1 0 1.6330 0 1.6667 1.6667 1.9868 1 1 1.6330 1 0 1.7249 1.6667 0 1.6667 1.9868 1.9907 1 1 1 0 1.7249 1.6667 1.6667 0 1.1471 1.9907 1 1 1.6330 0
- 1 1.9868 1.9868 1.1471 0 1.6859 1.6859 1 1.6059 0 1 1 1.9907 1.9907 1.6859 0 1.6330 1.6667 1 0


D :

R

1.6667 1 1 1 1.6859 1.6330 0 1 1 0 1.0887 1.6330 1 1 1 1.6667 1 0 1 0

 

 

1 1 1 1.6330 1.6059 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 464](<2010-arkus-deriving-finite-sphere-packings_images/imageFile464.png>)

![image 465](<2010-arkus-deriving-finite-sphere-packings_images/imageFile465.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.37576R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.4853 −0.8770 0 −0.5503 −0.8770 −1.3796 −0.0602 0 −0.9945 0.4779 −0.8165 0.3239 −0.7965 −1.3608 −0.5399 −0.8496 −0.3629 −0.5759 −0.5195 −0.8165 0.2519 0 −0.8165 −0.5759

C :

R

 

 

Packing 11 (Graph 34257):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 1 0 0 1 1 1 0 0 1 1 0 1 1 1 1 1 0 0

A :

 

 





0 1.6180 1.6779 1.6779 1 1 1.6180 1 1 0

- 1.6180 0 1.6779 1.6779 1.9843 1 1 1.6180 1 0 1.6779 1.6779 0 1.6482 1.9938 1.9843 1 1 1 0 1.6779 1.6779 1.6482 0 1.1220 1.9843 1 1 1.6532 0

1 1.9843 1.9938 1.1220 0 1.6779 1.6779 1 1.6532 0 1 1 1.9843 1.9843 1.6779 0 1.6180 1.6180 1 0

- 1.6180 1 1 1 1.6779 1.6180 0 1 1 0 1 1.6180 1 1 1 1.6180 1 0 1 0 1 1 1 1.6532 1.6532 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 466](<2010-arkus-deriving-finite-sphere-packings_images/imageFile466.png>)

![image 467](<2010-arkus-deriving-finite-sphere-packings_images/imageFile467.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.30509R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6180 0 1.4700 0.8090 0 0.5461 0.8090 −1.3648 −0.0000 −0.0987 −0.9951 −0.4867 0.8090 0.3295 0.7876 1.3090 −0.5331 0.7876 0.3090 −0.5331 0.5124 0.8090 0.2880 −0.0770 0.8090 −0.5827

C :

R

 

 

Packing 12 (Graph 40878):





0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 1 0 0 1 1 1 1 0 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1.7321 1 1 1 1 1 0 1.7321 0 2.0000 1.4142 2.0000 1 1.7321 1 1.7321 0 1.7321 2.0000 0 1.4142 2.0000 1.7321 1 1.7321 1 0 1.7321 1.4142 1.4142 0 1.4142 1.7321 1.7321 1 1 0
- 1 2.0000 2.0000 1.4142 0 1.7321 1.7321 1 1 0 1 1 1.7321 1.7321 1.7321 0 1 1 1.4142 0 1 1.7321 1 1.7321 1.7321 1 0 1.4142 1 0 1 1 1.7321 1 1 1 1.4142 0 1 0 1 1.7321 1 1 1 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 468](<2010-arkus-deriving-finite-sphere-packings_images/imageFile468.png>)

![image 469](<2010-arkus-deriving-finite-sphere-packings_images/imageFile469.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.40000R2|C3v|3| |






0 0 0 0 1.7321 0 −1.6330 0.5774 0 −0.8165 1.1547 1.0000 −0.0000 0 1.0000 0 0.8660 −0.5000 −0.8165 0.2887 −0.5000 0 0.8660 0.5000 −0.8165 0.2887 0.5000 −0.8165 1.1547 −0.0000

C :

R

 

 

###### *Packing 13 (Graph 53546):





0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 1 0 0 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





0 1.7321 1.7321 1.7321 1 1 1 1 1 0 1.7321 0 1.4142 2.0000 2.4495 1 1 1.7321 1.7321 0

- 1.7321 1.4142 0 1.4142 2.0000 1.7321 1 1.7321 1 0
- 1.7321 2.0000 1.4142 0 1.4142 1.7321 1.7321 1 1 0 1 2.4495 2.0000 1.4142 0 1.7321 1.7321 1 1 0 1 1 1.7321 1.7321 1.7321 0 1 1 1.4142 0 1 1 1 1.7321 1.7321 1 0 1.4142 1 0 1 1.7321 1.7321 1 1 1 1.4142 0 1 0 1 1.7321 1 1 1 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 470](<2010-arkus-deriving-finite-sphere-packings_images/imageFile470.png>)

![image 471](<2010-arkus-deriving-finite-sphere-packings_images/imageFile471.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.60000R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 −1.7321 0 1.2910 −1.1547 0 1.0328 −0.5774 −1.2649 0.5164 0.5774 −0.6325 −0.3873 −0.8660 −0.3162 0.3873 −0.8660 0.3162 0.1291 −0.2887 −0.9487 0.9037 −0.2887 −0.3162 0.5164 −1.1547 −0.6325

C :

R

 

 

Packing 14 (Graph 57812):





0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 1 1 0 1 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1.0887 1 1.6667 1.6667 1 1 0 1.6330 0 1.6330 1.6330 1.6667 1 1 1 1 0 1.0887 1.6330 0 1.7778 1.7249 1 1.9907 1 1.6667 0 1.0887 1.6330 1.7778 0 1.7249 1.9907 1 1.6667 1 0
- 1 1.6667 1.7249 1.7249 0 1.9907 1.9907 1 1 0 1.6667 1 1 1.9907 1.9907 0 1.6667 1 1.6330 0 1.6667 1 1.9907 1 1.9907 1.6667 0 1.6330 1 0


D :

R

1 1 1 1.6667 1 1 1.6330 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 472](<2010-arkus-deriving-finite-sphere-packings_images/imageFile472.png>)

![image 473](<2010-arkus-deriving-finite-sphere-packings_images/imageFile473.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.40000R2|Cs|1| |






0 0 0 0 −1.6330 0 −1.0264 −0.3629 0 0.5132 −0.3629 −0.8889 0.4811 −0.2722 0.8333 −0.9623 −1.3608 −0.0000 0.4811 −1.3608 −0.8333 −0.2887 −0.8165 0.5000 0.5774 −0.8165 0 −0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 15 (Graph 62297):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 1 0 1 1 1 0 0 0 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6859 1.5789 1 1.9868 1 1 1.6059 0 1.6859 0 1.6330 1.6859 1.9956 1 1 1.6667 1 0 1.6859 1.6330 0 1.6859 1.1471 1 1.6667 1 1 0 1.5789 1.6859 1.6859 0 1.9770 1.9868 1 1 1 0
- 1 1.9956 1.1471 1.9770 0 1.7622 1.6667 1 1.6859 0


D :

R

1.9868 1 1 1.9868 1.7622 0 1.6330 1.6330 1 0 1 1 1.6667 1 1.6667 1.6330 0 1.0887 1 0 1 1.6667 1 1 1 1.6330 1.0887 0 1 0

 

 

1.6059 1 1 1 1.6859 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 474](<2010-arkus-deriving-finite-sphere-packings_images/imageFile474.png>)

![image 475](<2010-arkus-deriving-finite-sphere-packings_images/imageFile475.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.35868R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6859 0 −1.4287 0.8950 0 −0.4093 0.7394 1.3337 −0.9102 −0.0416 −0.4120 −0.9505 1.7171 −0.3090 0.1555 0.8429 0.5151 −0.7969 0.3157 0.5151 −0.7259 1.3112 0.5769 −0.4666 0.8429 −0.2678

C :

R

 

 

Packing 16 (Graph 65350):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 1 1 0 0 1 1 0 1 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1.6330 1 1.6667 1 1 1 0 1.6330 0 1.6330 1.0887 1.9907 1 1 1.6667 1 0 1.0887 1.6330 0 1.9959 1.1529 1 1.6667 1.7249 1 0 1.6330 1.0887 1.9959 0 1.6667 1.7249 1 1 1.6667 0
- 1 1.9907 1.1529 1.6667 0 1.7778 1.6330 1 1.6667 0


D :

R

1.6667 1 1 1.7249 1.7778 0 1.6330 1.9907 1 0 1 1 1.6667 1 1.6330 1.6330 0 1 1 0 1 1.6667 1.7249 1 1 1.9907 1 0 1.6330 0 1 1 1 1.6667 1.6667 1 1 1.6330 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 476](<2010-arkus-deriving-finite-sphere-packings_images/imageFile476.png>)

![image 477](<2010-arkus-deriving-finite-sphere-packings_images/imageFile477.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.13868R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.0264 −0.3629 0 0.5132 −1.2701 0.8889 −0.4491 0 0.8889 −0.9623 −1.3608 0 0.5774 −0.8165 −0.0000 0.4811 −0.2722 0.8333 −0.2887 −0.8165 −0.5000 −0.2887 −0.8165 0.5000

C :

R

 

 

Packing 17 (Graph 65352):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 1 1 0 0 1 1 0 1 0 0 1 0 1 1 1 0 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.9959 1.6330 1 1.7249 1 1 1.6667 0 1.0887 0 1.6330 1.6330 1.7249 1 1 1.6667 1 0 1.9959 1.6330 0 1.0887 1.7874 1 1.6667 1.7249 1 0 1.6330 1.6330 1.0887 0 1.6667 1.6667 1 1 1 0
- 1 1.7249 1.7874 1.6667 0 1.8144 1.6330 1 1.9907 0


D :

R

1.7249 1 1 1.6667 1.8144 0 1.6330 1.9907 1 0 1 1 1.6667 1 1.6330 1.6330 0 1 1 0 1 1.6667 1.7249 1 1 1.9907 1 0 1.6330 0

 

 

1.6667 1 1 1 1.9907 1 1 1.6330 0 0 0 0 0 0 0 0 0 0 0 0

![image 478](<2010-arkus-deriving-finite-sphere-packings_images/imageFile478.png>)

![image 479](<2010-arkus-deriving-finite-sphere-packings_images/imageFile479.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.35816R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.0887 0 −1.6319 −1.1491 0 −1.2912 −0.5443 −0.8386 −0.8036 0.3629 0.4717 −0.8036 −1.4515 0.4717 −0.2925 −0.5443 −0.7862 −0.8070 0.2722 −0.5241 −0.8070 −1.3608 −0.5241 −0.8372 −0.5443 0

C :

R

 

 

Packing 18 (Graph 65490):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 1 1 0 0 1 1 0 1 0 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.7249 1.6667 1 1.9907 1 1 1.6330 0 1.6667 0 1.6330 1.6667 1.9907 1 1 1.6330 1 0 1.7249 1.6330 0 1.7249 1.1529 1 1.6667 1.0887 1 0 1.6667 1.6667 1.7249 0 1.9907 1.9907 1 1 1 0
- 1 1.9907 1.1529 1.9907 0 1.7778 1.6330 1 1.6667 0


D :

R

1.9907 1 1 1.9907 1.7778 0 1.6330 1.6667 1 0 1 1 1.6667 1 1.6330 1.6330 0 1 1 0 1 1.6330 1.0887 1 1 1.6667 1 0 1 0

 

 

1.6330 1 1 1 1.6667 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 480](<2010-arkus-deriving-finite-sphere-packings_images/imageFile480.png>)

![image 481](<2010-arkus-deriving-finite-sphere-packings_images/imageFile481.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.41440R2|C1|1<br><br>|chiral|






0 0 0 0 1.6667 0 1.4553 0.9259 0 0.4242 0.8333 1.3796 0.9445 −0.0556 −0.3239 0.9445 1.7222 −0.3239 −0.1188 0.8333 0.5399 0.7465 0.3333 0.5759 0.7465 1.3333 0.5759 0.4920 0.8333 −0.2519

C :

R

 

 

Packing 19 (Graph 69229):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 2.0000 1.4142 1 1.7321 1 1.7321 1 0

- 1.7321 0 1.7321 1.7321 1.9149 1 1 1 1 0
- 2.0000 1.7321 0 1.4142 1.7321 1 1.7321 1 1.7321 0 1.4142 1.7321 1.4142 0 1.9149 1.7321 1 1 1.7321 0


- 1 1.9149 1.7321 1.9149 0 1.4142 1.6330 1.9149 1 0 1.7321 1 1 1.7321 1.4142 0 1.4142 1 1 0


D :

R

1 1 1.7321 1 1.6330 1.4142 0 1 1 0

1.7321 1 1 1 1.9149 1 1 0 1.4142 0 1 1 1.7321 1.7321 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 482](<2010-arkus-deriving-finite-sphere-packings_images/imageFile482.png>)

![image 483](<2010-arkus-deriving-finite-sphere-packings_images/imageFile483.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.36667R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.7321 0 1.6330 1.1547 0 0.8165 0.5774 1.0000 0.5443 0 −0.8333 0.8165 1.4434 −0.5000 0 0.8660 0.5000 0.8165 1.4434 0.5000 −0.0000 0.8660 −0.5000 0.8165 0.5774 −0.0000

C :

R

 

 

Packing 20 (Graph 69305):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 1 0 1 1 1 0 0 1 1 0 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6779 1.6779 1.6482 1 1.9843 1 1.6532 1 0 1.6779 0 1.6180 1.6779 1.9889 1 1 1 1 0 1.6779 1.6180 0 1.6779 1.1220 1 1.6180 1 1 0 1.6482 1.6779 1.6779 0 1.9915 1.9843 1 1 1.6532 0
- 1 1.9889 1.1220 1.9915 0 1.7566 1.6330 1.7007 1 0 1.9843 1 1 1.9843 1.7566 0 1.6180 1 1 0


D :

R

1 1 1.6180 1 1.6330 1.6180 0 1 1 0

1.6532 1 1 1 1.7007 1 1 0 1.0515 0 1 1 1 1.6532 1 1 1 1.0515 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 484](<2010-arkus-deriving-finite-sphere-packings_images/imageFile484.png>)

![image 485](<2010-arkus-deriving-finite-sphere-packings_images/imageFile485.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.33407R2|C1|1<br><br>|chiral|






0 0 0 0 1.6779 0 −1.4175 0.8978 0 −0.4455 0.8094 −1.3648 −0.9282 −0.0418 0.3697 −0.9435 1.7143 0.3295 0.1090 0.8390 −0.5331 −0.7459 1.3554 −0.5827 −0.4617 0.8390 0.2880 −0.7671 0.3568 −0.5331

C :

R

 

 

Packing 21 (Graph 75933):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 0 1 1 1 0 0 1 0 0 0 1 1 0 1 1 1 0 1 0 0 1 1 1 1 0 1 0 0 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.7778 1.0887 1 1.9907 1 1.6667 1 0 1.6330 0 1.6330 1.6330 1.6667 1 1 1 1 0 1.7778 1.6330 0 1.0887 1.8178 1 1.9907 1 1.6667 0 1.0887 1.6330 1.0887 0 1.7249 1.6667 1.6667 1 1 0
- 1 1.6667 1.8178 1.7249 0 1.7778 1 1.9907 1.6330 0 1.9907 1 1 1.6667 1.7778 0 1.6667 1 1.6330 0


D :

R

1 1 1.9907 1.6667 1 1.6667 0 1.6330 1 0

1.6667 1 1 1 1.9907 1 1.6330 0 1 0 1 1 1.6667 1 1.6330 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 486](<2010-arkus-deriving-finite-sphere-packings_images/imageFile486.png>)

![image 487](<2010-arkus-deriving-finite-sphere-packings_images/imageFile487.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.35267R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.4913 0.9677 0 0.8242 0.3629 −0.6118 0.1104 0.2722 0.9559 0.9345 1.7237 0.3441 −0.4636 0.8165 0.3441 0.7726 1.3608 −0.5735 −0.0662 0.8165 −0.5735 0.5298 0.8165 0.2294

C :

R

 

 

Packing 22 (Graph 76012):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 1 0 0 1 0 0 0 1 1 0 1 1 1 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.7778 1.0887 1 1.9907 1 1.6667 1 0 1.6330 0 1.6330 1.6330 1.6667 1 1 1 1 0 1.7778 1.6330 0 1.0887 2.5035 1 1.9907 1 1.6667 0 1.0887 1.6330 1.0887 0 1.7249 1.6667 1.6667 1 1 0
- 1 1.6667 2.5035 1.7249 0 2.4369 1 1.9907 1 0 1.9907 1 1 1.6667 2.4369 0 1.6667 1 1.6330 0 1 1 1.9907 1.6667 1 1.6667 0 1.6330 1 0


D :

R

1.6667 1 1 1 1.9907 1 1.6330 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 488](<2010-arkus-deriving-finite-sphere-packings_images/imageFile488.png>)

![image 489](<2010-arkus-deriving-finite-sphere-packings_images/imageFile489.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.92675R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.4913 −0.9677 0 −0.8242 −0.3629 0.6118 0.8830 −0.2722 0.3824 −0.9345 −1.7237 −0.3441 0.4636 −0.8165 −0.3441 −0.7726 −1.3608 0.5735 0 −0.8165 0.5735 −0.5298 −0.8165 −0.2294

C :

R

 

 

Packing 23 (Graph 78584):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1.6330 1 1.6667 1 1 1 0 1.6330 0 1.6330 1.0887 1.9907 1 1.6667 1 1 0 1.0887 1.6330 0 1.9959 2.0718 1 1.7249 1 1.6667 0 1.6330 1.0887 1.9959 0 1.6667 1.7249 1 1.6667 1 0
- 1 1.9907 2.0718 1.6667 0 2.4369 1 1.6667 1 0


D :

R

1.6667 1 1 1.7249 2.4369 0 1.9907 1 1.6330 0 1 1.6667 1.7249 1 1 1.9907 0 1.6330 1 0 1 1 1 1.6667 1.6667 1 1.6330 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 490](<2010-arkus-deriving-finite-sphere-packings_images/imageFile490.png>)

![image 491](<2010-arkus-deriving-finite-sphere-packings_images/imageFile491.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.71276R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.0264 −0.3629 0 −0.5132 −1.2701 −0.8889 −0.9943 0 −0.0556 0.9623 −1.3608 −0.0000 −0.4811 −0.2722 −0.8333 0.2887 −0.8165 0.5000 −0.5774 −0.8165 −0.0000 0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 24 (Graph 78598):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 1 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1.6330 1 1.6330 1 1 1 0 1.6667 0 1.6667 1.7249 2.4369 1 1.9907 1 1 0 1.6667 1.6667 0 1.7249 1.7778 1 1.9907 1 1.6330 0 1.6330 1.7249 1.7249 0 1.6667 1.0887 1 1.6667 1 0
- 1 2.4369 1.7778 1.6667 0 1.9907 1 1.6667 1.6330 0


D :

R

1.6330 1 1 1.0887 1.9907 0 1.6667 1 1 0 1 1.9907 1.9907 1 1 1.6667 0 1.6330 1 0 1 1 1 1.6667 1.6667 1 1.6330 0 1 0 1 1 1.6330 1 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 492](<2010-arkus-deriving-finite-sphere-packings_images/imageFile492.png>)

![image 493](<2010-arkus-deriving-finite-sphere-packings_images/imageFile493.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.75679R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6667 0 −1.4434 −0.8333 0 −0.4277 −0.7407 −1.3911 −0.5880 0.6481 −0.4838 −0.7698 −1.3333 −0.5443 0 0 −0.9979 −0.4811 −0.8333 0.2722 0 −0.8333 −0.5443 −0.7698 −0.3333 −0.5443

C :

R

 

 

Packing 25 (Graph 78941):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 0 1 1 1 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.0887 1.9959 1.6330 1 1.7249 1 1.6667 1 0 1.0887 0 1.6330 1.6330 1.7249 1 1.6667 1 1 0 1.9959 1.6330 0 1.0887 2.4815 1 1.7249 1 1.6667 0 1.6330 1.6330 1.0887 0 1.6667 1.6667 1 1 1 0
- 1 1.7249 2.4815 1.6667 0 2.4637 1 1.9907 1 0 1.7249 1 1 1.6667 2.4637 0 1.9907 1 1.6330 0 1 1.6667 1.7249 1 1 1.9907 0 1.6330 1 0


D :

R

1.6667 1 1 1 1.9907 1 1.6330 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 494](<2010-arkus-deriving-finite-sphere-packings_images/imageFile494.png>)

![image 495](<2010-arkus-deriving-finite-sphere-packings_images/imageFile495.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.93224R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.0887 0 1.6319 −1.1491 0 1.2912 −0.5443 −0.8386 −0.1042 0.3629 −0.9260 0.8036 −1.4515 0.4717 0.8070 0.2722 −0.5241 0.8070 −1.3608 −0.5241 0.2925 −0.5443 −0.7862 0.8372 −0.5443 0

C :

R

 

 

Packing 26 (Graph 78955):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 1 1 0 1 1 1 0 1 0 0 1 1 1 1 0 1 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7249 1.7249 1.6330 1 1.0887 1 1.6667 1 0 1.7249 0 1.6667 1.6667 2.4637 1 1.9907 1 1 0 1.7249 1.6667 0 1.6667 1.8144 1 1.9907 1 1.6330 0 1.6330 1.6667 1.6667 0 1.6667 1.6330 1 1 1 0
- 1 2.4637 1.8144 1.6667 0 1.7249 1 1.9907 1.6330 0 1.0887 1 1 1.6330 1.7249 0 1.6667 1 1 0


D :

R

1 1.9907 1.9907 1 1 1.6667 0 1.6330 1 0

1.6667 1 1 1 1.9907 1 1.6330 0 1 0 1 1 1.6330 1 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 496](<2010-arkus-deriving-finite-sphere-packings_images/imageFile496.png>)

![image 497](<2010-arkus-deriving-finite-sphere-packings_images/imageFile497.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.80288R2|C1|1<br><br>|chiral|






0 0 0 0 −1.7249 0 −1.4593 −0.9197 0 −0.4581 −0.8302 −1.3295 −0.6167 0.6072 −0.5010 −0.5055 −0.9161 0.3006 −0.0020 −0.0036 −1.0000 −0.7602 −1.3778 −0.5491 0 −0.8625 −0.4971 −0.7804 −0.3793 −0.4971

C :

R

 

 

Packing 27 (Graph 80933):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 0 1 1 0 1 0 1 1 0 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 0 1 1 0 1 1 0

A :

 

 





- 0 1.4142 1.9149 1.7321 1 1.7321 1 1 1.4142 0 1.4142 0 1.6667 1.9149 1.9149 1 1.9149 1 1.6330 0 1.9149 1.6667 0 1.9149 1.4142 1 1.9149 1.6330 1 0 1.7321 1.9149 1.9149 0 1.7321 1.4142 1 1 1 0
- 1 1.9149 1.4142 1.7321 0 1.7321 1 1.4142 1 0


D :

R

1.7321 1 1 1.4142 1.7321 0 1.7321 1 1 0 1 1.9149 1.9149 1 1 1.7321 0 1 1 0 1 1 1.6330 1 1.4142 1 1 0 1 0

 

 

1.4142 1.6330 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 498](<2010-arkus-deriving-finite-sphere-packings_images/imageFile498.png>)

![image 499](<2010-arkus-deriving-finite-sphere-packings_images/imageFile499.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.41111R2|Cs<br><br>|1| |






0 0 0 0 −1.4142 0 1.6197 −1.0214 0 0.6288 −0.4714 1.5435 0.9718 0.2357 0 0.8575 −1.4142 0.5145 0.4573 0.2357 0.8575 0.1715 −0.7071 0.6860 1.1433 −0.4714 0.6860 0.6860 −0.7071 −0.1715

C :

R

 

 

Packing 28 (Graph 81151):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 1 1 1 0 1 1 1 0 1 1 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.6667 1.7249 1.6667 1 1.9907 1 1.6330 1 0 1.6667 0 1.6330 1.6667 1.9907 1 1.6330 1 1 0 1.7249 1.6330 0 1.7249 2.0718 1 1.0887 1 1.6667 0 1.6667 1.6667 1.7249 0 1.0887 1.9907 1 1 1 0
- 1 1.9907 2.0718 1.0887 0 2.4369 1 1.6667 1 0 1.9907 1 1 1.9907 2.4369 0 1.6667 1 1.6330 0 1 1.6330 1.0887 1 1 1.6667 0 1 1 0


D :

R

1.6330 1 1 1 1.6667 1 1 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 500](<2010-arkus-deriving-finite-sphere-packings_images/imageFile500.png>)

![image 501](<2010-arkus-deriving-finite-sphere-packings_images/imageFile501.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.71070R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6667 0 1.4553 −0.9259 0 0.4242 −0.8333 −1.3796 −0.0735 0 −0.9957 0.9445 −1.7222 0.3239 0.7465 −0.3333 −0.5759 0.7465 −1.3333 −0.5759 −0.1188 −0.8333 −0.5399 0.4920 −0.8333 0.2519

C :

R

 

 

Packing 29 (Graph 81182):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 0 1 1 1 0 1 1 0 1 1 1 1 0 1 0 1 1 1 0 1 1 0 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.9907 1.9907 1.6667 1 1.6667 1 1.6330 1 0 1.9907 0 1.6667 1.0887 2.4369 1 1.6667 1 1 0 1.9907 1.6667 0 1.9907 1.7778 1 1.6667 1 1.6330 0 1.6667 1.0887 1.9907 0 1.9907 1.6667 1 1 1 0
- 1 2.4369 1.7778 1.9907 0 1.9907 1 1.6667 1.6330 0 1.6667 1 1 1.6667 1.9907 0 1.6330 1 1 0


D :

R

1 1.6667 1.6667 1 1 1.6330 0 1 1 0

1.6330 1 1 1 1.6667 1 1 0 1 0 1 1 1.6330 1 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 502](<2010-arkus-deriving-finite-sphere-packings_images/imageFile502.png>)

![image 503](<2010-arkus-deriving-finite-sphere-packings_images/imageFile503.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.95432R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.9907 0 −1.5136 1.2930 0 0.2744 1.3954 −0.8692 −0.8047 −0.2450 −0.5408 −0.6646 1.4419 0.5070 −0.2530 0.5488 −0.7967 −0.6518 1.4140 −0.4925 0 0.9954 0 −0.8164 0.5768 0

C :

R

 

 

Packing 30 (Graph 82672):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 1 1 0 0 1 1 0 1 0 1 1 0 1 1 1 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.9907 1.9907 1.6667 1 1.6667 1 1 1.6330 0 1.9907 0 1.6667 1.9907 2.4369 1 1 1.6667 1 0 1.9907 1.6667 0 1.0887 1.7778 1 1.6330 1.6667 1 0 1.6667 1.9907 1.0887 0 1.0887 1.6667 1.6330 1 1 0
- 1 2.4369 1.7778 1.0887 0 1.9907 1.6330 1 1.6667 0


D :

R

1.6667 1 1 1.6667 1.9907 0 1 1.6330 1 0 1 1 1.6330 1.6330 1.6330 1 0 1 1 0 1 1.6667 1.6667 1 1 1.6330 1 0 1 0

 

 

1.6330 1 1 1 1.6667 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 504](<2010-arkus-deriving-finite-sphere-packings_images/imageFile504.png>)

![image 505](<2010-arkus-deriving-finite-sphere-packings_images/imageFile505.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.67654R2|C1|1<br><br>|chiral|






0 0 0 0 1.9907 0 1.5136 1.2930 0 1.2392 0.6977 0.8692 0.8047 −0.2450 0.5408 0.6646 1.4419 −0.5070 −0.0918 0.9954 −0.0290 0.2530 0.5488 0.7967 0.6518 1.4140 0.4925 0.8164 0.5768 −0.0290

C :

R

 

 

Packing 31 (Graph 93924):





0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 1 0 0 1 1 1 0 1 0 1 1 0 0 1 1 1 1 0 1 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.9907 1.6667 1.0887 1 1.6330 1.6667 1 1 0 1.9907 0 1.9907 1.6667 2.4369 1 1 1.6667 1 0 1.6667 1.9907 0 1.9907 1.0887 1 1.6667 1 1.6330 0 1.0887 1.6667 1.9907 0 1.7249 1.6330 1 1.6667 1 0
- 1 2.4369 1.0887 1.7249 0 1.6667 1.9907 1 1.6330 0 1.6330 1 1 1.6330 1.6667 0 1 1 1 0 1.6667 1 1.6667 1 1.9907 1 0 1.6330 1 0


D :

R

1 1.6667 1 1.6667 1 1 1.6330 0 1 0 1 1 1.6330 1 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 506](<2010-arkus-deriving-finite-sphere-packings_images/imageFile506.png>)

![image 507](<2010-arkus-deriving-finite-sphere-packings_images/imageFile507.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.65802R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.9907 0 1.5136 −0.6977 0 −0.2744 −0.5954 0.8692 0.9693 0.2450 0 0.8164 −1.4140 −0.0290 0.2530 −1.4419 0.7967 0.6646 −0.5488 −0.5070 −0.0918 −0.9954 −0.0290 0.6518 −0.5768 0.4925

C :

R

 

 

Packing 32 (Graph 93930):





0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 1 0 0 1 1 1 0 1 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.9907 1.6667 1.0887 1 1.6330 1.6667 1 1 0 1.9907 0 1.9907 1.6667 1.7778 1 1 1.6667 1.6330 0 1.6667 1.9907 0 1.9907 1.9907 1 1.6667 1 1 0 1.0887 1.6667 1.9907 0 1.7249 1.6330 1 1.6667 1 0
- 1 1.7778 1.9907 1.7249 0 1.6667 1.9907 1 1.6330 0 1.6330 1 1 1.6330 1.6667 0 1 1 1 0 1.6667 1 1.6667 1 1.9907 1 0 1.6330 1 0


D :

R

1 1.6667 1 1.6667 1 1 1.6330 0 1 0 1 1.6330 1 1 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 508](<2010-arkus-deriving-finite-sphere-packings_images/imageFile508.png>)

![image 509](<2010-arkus-deriving-finite-sphere-packings_images/imageFile509.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.65802R2|C1|1<br><br>|chiral|






0 0 0 0 −1.9907 0 −1.5136 −0.6977 0 0.2744 −0.5954 −0.8692 0.2698 −0.4527 0.8498 −0.8164 −1.4140 0 −0.2530 −1.4419 −0.7967 −0.6646 −0.5488 0.5070 −0.6518 −0.5768 −0.4925 0 −0.9954 0

C :

R

 

 

Packing 33 (Graph 93942):





0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 1 0 0 1 1 1 0 1 0 1 1 0 0 1 1 1 0 0 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.9907 1.6667 1.0887 1 1.6330 1.6667 1 1 0 1.9907 0 1.0887 1.6667 2.4369 1 1 1.6667 1.6330 0 1.6667 1.0887 0 1.9907 1.9907 1 1.6667 1 1.6330 0 1.0887 1.6667 1.9907 0 1.7249 1.6330 1 1.6667 1 0
- 1 2.4369 1.9907 1.7249 0 1.6667 1.9907 1 1 0 1.6330 1 1 1.6330 1.6667 0 1 1 1 0 1.6667 1 1.6667 1 1.9907 1 0 1.6330 1 0


D :

R

1 1.6667 1 1.6667 1 1 1.6330 0 1 0 1 1.6330 1.6330 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 510](<2010-arkus-deriving-finite-sphere-packings_images/imageFile510.png>)

![image 511](<2010-arkus-deriving-finite-sphere-packings_images/imageFile511.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.65802R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.9907 0 0.9114 1.3954 0 −0.9114 0.5954 −0.0000 0.2734 −0.2450 0.9302 0.2734 1.4140 0.7698 −0.6836 1.4419 0.4811 0.6836 0.5488 0.4811 −0.2734 0.5768 0.7698 −0.0000 0.9954 −0.0962

C :

R

 

 

Packing 34 (Graph 94152):





0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 1 1 0 1 0 1 0 1 0 1 0 1 1 1 1 0 1 0 0 1 1 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.9907 1.0887 1.6667 1 1.6667 1.6330 1 1 0 1.9907 0 1.6667 1.0887 1.7778 1 1 1.6330 1.6667 0 1.0887 1.6667 0 1.9907 1.7249 1 1.6330 1 1.6667 0 1.6667 1.0887 1.9907 0 1.0887 1.6667 1 1.6330 1 0
- 1 1.7778 1.7249 1.0887 0 1.9907 1.6667 1.6330 1 0 1.6667 1 1 1.6667 1.9907 0 1 1 1.6330 0 1.6330 1 1.6330 1 1.6667 1 0 1 1 0


D :

R

1 1.6330 1 1.6330 1.6330 1 1 0 1 0 1 1.6667 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 512](<2010-arkus-deriving-finite-sphere-packings_images/imageFile512.png>)

![image 513](<2010-arkus-deriving-finite-sphere-packings_images/imageFile513.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.10247R2|C1|1<br><br>|chiral|






0 0 0 0 −1.9907 0 −0.9114 −0.5954 0 0.9114 −1.3954 −0.0000 0.7292 −0.4527 0.5132 −0.6836 −1.4419 −0.4811 0.2734 −1.4140 −0.7698 −0.2734 −0.5768 −0.7698 0.6836 −0.5488 −0.4811 −0.0000 −0.9954 0

C :

R

 

 

###### *Packing 35 (Graph 94932):





0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1 1 0 1 0 1 0 1 0 1 0 0 1 1 1 1 1 0 1 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.4142 1.4142 1 1.7321 1.7321 1 1 0

- 1.7321 0 1.7321 1.7321 1.4142 1 1 1 1 0 1.4142 1.7321 0 2.0000 1.9149 1 1.7321 1 1.7321 0 1.4142 1.7321 2.0000 0 1.9149 1.7321 1 1.7321 1 0

1 1.4142 1.9149 1.9149 0 1.9149 1.9149 1 1 0

- 1.7321 1 1 1.7321 1.9149 0 1 1 1.4142 0 1.7321 1 1.7321 1 1.9149 1 0 1.4142 1 0


- 1 1 1 1.7321 1 1 1.4142 0 1 0 1 1 1.7321 1 1 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 514](<2010-arkus-deriving-finite-sphere-packings_images/imageFile514.png>)

![image 515](<2010-arkus-deriving-finite-sphere-packings_images/imageFile515.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.43333R2|Cs<br><br>|1| |






0 0 0 0 −1.7321 0 1.2910 −0.5774 0 −0.2582 −0.5774 1.2649 −0.5164

- −0.5774 −0.6325

0.9037 −1.4434 0.3162 0.1291

- −1.4434 0.9487 0.3873


C :

R

−0.8660 −0.3162 −0.3873 −0.8660 0.3162 0.5164 −0.5774 0.6325

 

 

Packing 36 (Graph 112224):





0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 1 1 0 0 0 1 1 1 0 1 0 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 0 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6779 1.6779 1.6482 1 1.9843 1.6532 1 1 0 1.6779 0 1.6180 1.6779 1.9889 1 1 1 1 0 1.6779 1.6180 0 1.6779 1.9889 1 1 1 1.6180 0 1.6482 1.6779 1.6779 0 1.0383 1.9843 1 1.6532 1 0
- 1 1.9889 1.9889 1.0383 0 2.4047 1.6482 1.6330 1 0 1.9843 1 1 1.9843 2.4047 0 1 1 1.6180 0 1.6532 1 1 1 1.6482 1 0 1.0515 1 0


D :

R

1 1 1 1.6532 1.6330 1 1.0515 0 1 0 1 1 1.6180 1 1 1.6180 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 516](<2010-arkus-deriving-finite-sphere-packings_images/imageFile516.png>)

![image 517](<2010-arkus-deriving-finite-sphere-packings_images/imageFile517.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.56699R2|C2v|2| |






0 0 0 0 −1.6779 0 −1.4175 −0.8978 0 −0.4455 −0.8094 −1.3648 0 0 −0.9989 −0.9435 −1.7143 0.3295 −0.7459 −1.3554 −0.5827 −0.4617 −0.8390 0.2880 0.1090 −0.8390 −0.5331 −0.7671 −0.3568 −0.5331

C :

R

 

 

Packing 37 (Graph 113048):





0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 1 1 1 0 0 1 1 1 0 1 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 0 1 1 0 1 1 1 0

A :

 

 





- 0 1.7321 2.0000 1.4142 1 1.7321 1.7321 1 1 0 1.7321 0 1.7321 1.7321 1.4142 1 1 1 1.4142 0 2.0000 1.7321 0 1.4142 2.5166 1 1 1.7321 1 0 1.4142 1.7321 1.4142 0 1.9149 1.7321 1 1.7321 1 0
- 1 1.4142 2.5166 1.9149 0 1.9149 1.9149 1 1.6330 0 1.7321 1 1 1.7321 1.9149 0 1 1 1 0 1.7321 1 1 1 1.9149 1 0 1.4142 1 0


D :

R

1 1 1.7321 1.7321 1 1 1.4142 0 1 0 1 1.4142 1 1 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 518](<2010-arkus-deriving-finite-sphere-packings_images/imageFile518.png>)

![image 519](<2010-arkus-deriving-finite-sphere-packings_images/imageFile519.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.70000R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.7321 0 1.6330 −1.1547 0 0.8165 −0.5774 −1.0000

- −0.8165

- −0.5774 0

0.8165

- −1.4434 0.5000 0.8165


- −1.4434 −0.5000 −0.0000 −0.8660


C :

R

0.5000 0.8165 −0.5774 0 0 −0.8660 −0.5000

 

 

Packing 38 (Graph 118632):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 0 1 1 1 0 0 0 1 0 0 0 0 1 0 1 1 1 0 0 0 1 1 1 1 1 1 0 0 0 1 0 1 1 1 1 0 1 1 0 1 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1.6667 1 1 1.6330 1 1 0 1.6667 0 1.6667 1.6667 1.9907 2.4369 1 1 1 0 1.6667 1.6667 0 1.6667 1.9907 1.7778 1 1 1.6330 0 1.6667 1.6667 1.6667 0 1.0887 1.7249 1 1.6330 1 0
- 1 1.9907 1.9907 1.0887 0 1 1.6667 1.6330 1 0 1 2.4369 1.7778 1.7249 1 0 1.9907 1.6667 1.6330 0


D :

R

1.6330 1 1 1 1.6667 1.9907 0 1 1 0 1 1 1 1.6330 1.6330 1.6667 1 0 1 0 1 1 1.6330 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 520](<2010-arkus-deriving-finite-sphere-packings_images/imageFile520.png>)

![image 521](<2010-arkus-deriving-finite-sphere-packings_images/imageFile521.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.73704R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6667 0 −1.4434 −0.8333 0 −0.4811 −0.8333 −1.3608 0 0 −0.9979 −0.5880 0.6481 −0.4838 −0.7698 −1.3333 −0.5443 −0.4811 −0.8333 0.2722 0 −0.8333 −0.5443 −0.7698 −0.3333 −0.5443

C :

R

 

 

Packing 39 (Graph 119213):





0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1 1 1 1 0 1 0 1 0 1 1 1 1 0 1 0 1 1 1 0 1 0 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.4142 1.9149 1.9149 1 1 1.7321 1 1 0 1.4142 0 1.6667 1.6667 1.9149 1.9149 1 1 1 0 1.9149 1.6667 0 1.6667 1.4142 1.9149 1 1 1.6330 0 1.9149 1.6667 1.6667 0 1.9149 1.4142 1 1.6330 1 0
- 1 1.9149 1.4142 1.9149 0 1 1.7321 1 1.4142 0 1 1.9149 1.9149 1.4142 1 0 1.7321 1.4142 1 0


D :

R

1.7321 1 1 1 1.7321 1.7321 0 1 1 0 1 1 1 1.6330 1 1.4142 1 0 1 0 1 1 1.6330 1 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 522](<2010-arkus-deriving-finite-sphere-packings_images/imageFile522.png>)

![image 523](<2010-arkus-deriving-finite-sphere-packings_images/imageFile523.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.33333R2|C3v|3| |






0 0 0 0 −1.4142 0 1.6197 −1.0214 0 0.7622 −1.0214 1.4292 0.9718 0.2357

- −0.0000 0.4573 0.2357 0.8575 0.8575
- −1.4142 0.5145 0.6860


C :

R

−0.7071 −0.1715 0.1715 −0.7071 0.6860 1.1433 −0.4714 0.6860

 

 

###### *Packing 40 (Graph 138747):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 1 0 1 0 1 1 0 0 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 0 0 0 1 0 1 1 1 1 1 1 0 0

A :

 

 





0 1.7199 1.5224 1.9591 1 1 1.5130 1.7199 1 0

- 1.7199 0 1.7221 1.7221 1.7199 1 1 1 1 0 1.5224 1.7221 0 1.5203 1.9591 1 1.7204 1 1.8799 0 1.9591 1.7221 1.5203 0 1.5224 1.7204 1 1 1.8799 0

1 1.7199 1.9591 1.5224 0 1.5130 1 1.7199 1 0 1 1 1 1.7204 1.5130 0 1.2892 1 1 0

1.5130 1 1.7204 1 1 1.2892 0 1 1 0

- 1.7199 1 1 1 1.7199 1 1 0 1.5130 0 1 1 1.8799 1.8799 1 1 1 1.5130 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 524](<2010-arkus-deriving-finite-sphere-packings_images/imageFile524.png>)

![image 525](<2010-arkus-deriving-finite-sphere-packings_images/imageFile525.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.18554R2|Cs|1| |






0 0 0 0 −1.7199 0 −1.3662 −0.6716 0 −0.8595 −1.1135 −1.3635 0.3333 −0.2907 −0.8969 −0.4255

C :

R

- −0.8600 0.2818

0

- −1.2347 −0.8744 −0.8623 −1.4292 −0.4147


0.5019 −0.8600 −0.0922 −0.6097 −0.4852 −0.6268

 

 

Packing 41 (Graph 165946):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 0 1 0 1 1 1 0 0 0 1 1 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 0 1 1 1 0 0 1 1 0 1 1 1 1 1 0 0

A :

 

 





- 0 1.6180 1.6779 1.6779 1 1.6180 1 1 1 0 1.6180 0 1.6779 1.6779 1.6779 1 1 1.6180 1 0 1.6779 1.6779 0 1.6482 2.4520 1 1.9843 1 1 0 1.6779 1.6779 1.6482 0 1.8155 1 1.9843 1 1.6532 0
- 1 1.6779 2.4520 1.8155 0 1.9843 1 1.6779 1.6532 0


D :

R

1.6180 1 1 1 1.9843 0 1.6180 1 1 0 1 1 1.9843 1.9843 1 1.6180 0 1.6180 1 0 1 1.6180 1 1 1.6779 1 1.6180 0 1 0 1 1 1 1.6532 1.6532 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 526](<2010-arkus-deriving-finite-sphere-packings_images/imageFile526.png>)

![image 527](<2010-arkus-deriving-finite-sphere-packings_images/imageFile527.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.71249R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6180 0 1.4700 0.8090 0 0.5461 0.8090 −1.3648 −0.8837 0.2480 −0.3969 0.7876 1.3090 −0.5331 −0.4867 0.8090 0.3295 0.7876 0.3090 −0.5331 0.5124 0.8090 0.2880 −0.0770 0.8090 −0.5827

C :

R

 

 

Packing 42 (Graph 180999):





0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 0 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6859 1.6859 1 1 1 1.6667 1 0 1.6330 0 1.6859 1.6859 1.6667 1 1.6667 1 1 0 1.6859 1.6859 0 1.5789 2.4315 1.9868 1 1 1 0 1.6859 1.6859 1.5789 0 1.8113 1.9868 1 1 1.6059 0
- 1 1.6667 2.4315 1.8113 0 1 1.6667 1.9907 1.6330 0 1 1 1.9868 1.9868 1 0 1.6330 1.6330 1 0 1 1.6667 1 1 1.6667 1.6330 0 1.0887 1 0


D :

R

1.6667 1 1 1 1.9907 1.6330 1.0887 0 1 0 1 1 1 1.6059 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 528](<2010-arkus-deriving-finite-sphere-packings_images/imageFile528.png>)

![image 529](<2010-arkus-deriving-finite-sphere-packings_images/imageFile529.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.70330R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.4749 −0.8165 0 −0.6298 −0.8165 −1.3337 0.8525 −0.2722 −0.4464 0.4877 −0.8165 0.3090 −0.8128 −0.2722 −0.5151 −0.8128 −1.3608 −0.5151 −0.5115 −0.8165 0.2678 0 −0.8165 −0.5769

C :

R

 

 

Packing 43 (Graph 184811):





0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 1 0 0 1 1 1 0 1 0 1 1 0 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6532 1.6532 1.6532 1 1 1 1 1 0 1.6532 0 1.8155 1.1220 1.6779 1 1.6779 1.9843 1 0 1.6532 1.8155 0 1.1220 1.6779 1.9843 1 1 1.6779 0 1.6532 1.1220 1.1220 0 1.9843 1.6779 1 1.6779 1 0
- 1 1.6779 1.6779 1.9843 0 1 1.6180 1 1.6180 0 1 1 1.9843 1.6779 1 0 1.6180 1.6180 1 0 1 1.6779 1 1 1.6180 1.6180 0 1 1 0 1 1.9843 1 1.6779 1 1.6180 1 0 1.6180 0 1 1 1.6779 1 1.6180 1 1 1.6180 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 530](<2010-arkus-deriving-finite-sphere-packings_images/imageFile530.png>)

![image 531](<2010-arkus-deriving-finite-sphere-packings_images/imageFile531.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.09140R2|Cs<br><br>|1| |






0 0 0 0 1.6532 0 1.5173 0.6563 0 0.8360 1.2724 −0.6443 0.1823 0.2775 0.9433 −0.4249 0.8266 0.3690 0.7806 0.2775 −0.5601 0.9274 −0.0619 0.3690 −0.0552 0.8266 −0.5601 0.5640 0.8585 0.2245

C :

R

 

 

###### *Packing 44 (Graph 187508):





0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 1 0 0 1 1 0 0 1 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 0 1 0 1 1 1 0 0 1 1 1 0 1 0 1 1 0 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1.7321 1 1 1 1 1 0 1.7321 0 2.0000 1.4142 2.0000 1 1.7321 1.7321 1 0 1.7321 2.0000 0 1.4142 2.0000 1.7321 1 1 1.7321 0 1.7321 1.4142 1.4142 0 2.4495 1.7321 1 1.7321 1 0
- 1 2.0000 2.0000 2.4495 0 1 1.7321 1 1.7321 0 1 1 1.7321 1.7321 1 0 1.4142 1 1 0 1 1.7321 1 1 1.7321 1.4142 0 1 1 0 1 1.7321 1 1.7321 1 1 1 0 1.4142 0 1 1 1.7321 1 1.7321 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 532](<2010-arkus-deriving-finite-sphere-packings_images/imageFile532.png>)

![image 533](<2010-arkus-deriving-finite-sphere-packings_images/imageFile533.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.80000R2|Cs|1| |






0 0 0 0 −1.7321 0 1.6330 −0.5774 0 0.8165 −1.1547 1.0000 0 −0.0000 −1.0000 0 −0.8660 −0.5000 0.8165 −0.2887 0.5000 0.8165 −0.2887 −0.5000 −0.0000

C :

R

- −0.8660 0.5000 0.8165
- −1.1547 0


 

 

Packing 45 (Graph 200848):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1.0887 1 1 1.6667 1 1 0 1.6330 0 1.8353 1.6330 1 1.7622 1 1.9868 1 0 1.6330 1.8353 0 1.6330 1.7622 1 1.7622 1 1.9868 0 1.0887 1.6330 1.6330 0 1.6667 1.6667 1 1 1 0
- 1 1 1.7622 1.6667 0 1.1471 1.6330 1.6859 1 0 1 1.7622 1 1.6667 1.1471 0 1.9956 1 1.6859 0


D :

R

1.6667 1 1.7622 1 1.6330 1.9956 0 1.6859 1 0 1 1.9868 1 1 1.6859 1 1.6859 0 1.6059 0 1 1 1.9868 1 1 1.6859 1 1.6059 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 534](<2010-arkus-deriving-finite-sphere-packings_images/imageFile534.png>)

![image 535](<2010-arkus-deriving-finite-sphere-packings_images/imageFile535.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.38343R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.5181 0.6016 0 −0.2465 0.3629 −0.9964 0.1387 0.8165 0.5604 −0.8102 0.1719 0.5604 −0.2311 1.3608 −0.9341 −0.9123 −0.0859 −0.4003 0.4160 0.8165 −0.4003 −0.5547 0.8165 −0.1601

C :

R

 

 

Packing 46 (Graph 200863):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 1 0 1 1 0 0 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1.6330 1 1 1.9868 1 1 0 1.6330 0 1.7778 1.0887 1 1.9907 1 1.6667 1 0 1.6330 1.7778 0 1.0887 1.9907 1 1.2115 1 1.6667 0 1.6330 1.0887 1.0887 0 1.6667 1.6667 1 1 1 0
- 1 1 1.9907 1.6667 0 1.6667 1.6859 1.6330 1 0 1 1.9907 1 1.6667 1.6667 0 1.8113 1 1.6330 0


D :

R

1.9868 1 1.2115 1 1.6859 1.8113 0 1.6859 1.6059 0 1 1.6667 1 1 1.6330 1 1.6859 0 1 0 1 1 1.6667 1 1 1.6330 1.6059 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 536](<2010-arkus-deriving-finite-sphere-packings_images/imageFile536.png>)

![image 537](<2010-arkus-deriving-finite-sphere-packings_images/imageFile537.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.16381R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.4913 −0.6653 0 −0.8242 −1.2701 0.6118 0.4636 −0.8165 −0.3441 −0.9345 0 −0.3441 −0.9585 −1.7189 −0.2717 −0.7726 −0.2722 0.5735 0 −0.8165 0.5735 −0.5298 −0.8165 −0.2294

C :

R

 

 

Packing 47 (Graph 200875):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 0 1 0 0 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1.6330 1 1 1.6667 1 1 0 1.0887 0 1.9959 1.6330 1 1.7249 1 1.6667 1 0 1.6330 1.9959 0 1.0887 1.7622 1 1.7249 1 1.6667 0 1.6330 1.6330 1.0887 0 1.9868 1.6667 1 1 1 0
- 1 1 1.7622 1.9868 0 1.1471 1.6859 1.6859 1.6059 0 1 1.7249 1 1.6667 1.1471 0 1.9907 1 1.6330 0


D :

R

1.6667 1 1.7249 1 1.6859 1.9907 0 1.6330 1 0 1 1.6667 1 1 1.6859 1 1.6330 0 1 0 1 1 1.6667 1 1.6059 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 538](<2010-arkus-deriving-finite-sphere-packings_images/imageFile538.png>)

![image 539](<2010-arkus-deriving-finite-sphere-packings_images/imageFile539.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.13435R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.0887 0 −1.6319 −0.0605 0 −1.2912 0.5443 −0.8386 −0.1922 0.5443 0.8166 −0.8036 −0.3629 0.4717 −0.8070 1.3608 −0.5241 −0.8070 −0.2722 −0.5241 −0.2925 0.5443 −0.7862 −0.8372 0.5443 0

C :

R

 

 

Packing 48 (Graph 200880):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6330 1.6330 1 1 1.6667 1 1 0 1.6859 0 1.8193 1.6859 1 1.8113 1 1.9868 1.6059 0 1.6330 1.8193 0 1.0887 1.9907 1 1.7249 1 1.6667 0 1.6330 1.6859 1.0887 0 1.6667 1.6667 1 1 1 0
- 1 1 1.9907 1.6667 0 1.6667 1.0887 1.6330 1 0 1 1.8113 1 1.6667 1.6667 0 1.9907 1 1.6330 0


D :

R

1.6667 1 1.7249 1 1.0887 1.9907 0 1.6330 1 0 1 1.9868 1 1 1.6330 1 1.6330 0 1 0 1 1.6059 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 540](<2010-arkus-deriving-finite-sphere-packings_images/imageFile540.png>)

![image 541](<2010-arkus-deriving-finite-sphere-packings_images/imageFile541.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.32950R2|C1|1<br><br>|chiral|






0 0 0 0 1.6859 0 1.4971 0.6521 0 1.0409 0.7909 0.9787 −0.4661 0.8429 0.2687 0.8181 0.1665 −0.5505 0.2278 1.3702 0.9211 0.9042 −0.0312 0.4260 0.1337 0.3746 0.9175 0.5234 0.8429 0.1245

C :

R

 

 

Packing 49 (Graph 201011):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 1 1 0 1 1 0

A :

 

 





- 0 1.6330 1.6330 1.6330 1 1 1.9868 1 1 0 1.6330 0 1.7778 1.0887 1 1.9907 1 1.6667 1 0 1.6330 1.7778 0 1.0887 1.9907 1 2.0676 1 1.6667 0 1.6330 1.0887 1.0887 0 1.6667 1.6667 1 1 1 0
- 1 1 1.9907 1.6667 0 1.6667 1.6859 1.6330 1 0 1 1.9907 1 1.6667 1.6667 0 2.4315 1 1.6330 0


D :

R

1.9868 1 2.0676 1 1.6859 2.4315 0 1.6859 1 0 1 1.6667 1 1 1.6330 1 1.6859 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 542](<2010-arkus-deriving-finite-sphere-packings_images/imageFile542.png>)

![image 543](<2010-arkus-deriving-finite-sphere-packings_images/imageFile543.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.70767R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.4913 −0.6653 0 0.8242 −1.2701 −0.6118 −0.4636 −0.8165 0.3441 0.9345 0 0.3441 0 −1.7189 −0.9961 0.7726 −0.2722 −0.5735 −0.0662 −0.8165 −0.5735 0.5298 −0.8165 0.2294

C :

R

 

 

Packing 50 (Graph 201013):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1.6330 1 1 1.6667 1 1 0 1.0887 0 1.9959 1.6330 1 1.7249 1 1.6667 1 0 1.6330 1.9959 0 1.0887 2.4315 1 1.7249 1 1.6667 0 1.6330 1.6330 1.0887 0 1.9868 1.6667 1 1 1 0
- 1 1 2.4315 1.9868 0 1.9868 1.6859 1.6859 1 0 1 1.7249 1 1.6667 1.9868 0 1.9907 1 1.6330 0


D :

R

1.6667 1 1.7249 1 1.6859 1.9907 0 1.6330 1 0 1 1.6667 1 1 1.6859 1 1.6330 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 544](<2010-arkus-deriving-finite-sphere-packings_images/imageFile544.png>)

![image 545](<2010-arkus-deriving-finite-sphere-packings_images/imageFile545.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.67821R2|C1|1<br><br>|chiral|






0 0 0 0 1.0887 0 1.6319 −0.0605 0 1.2912 0.5443 −0.8386 −0.6679 0.5443 −0.5076 0.8036 −0.3629 0.4717 0.8070 1.3608 −0.5241 0.8070 −0.2722 −0.5241 0.2925 0.5443 −0.7862 0.8372 0.5443 0

C :

R

 

 

Packing 51 (Graph 201014):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1.6859 1 1 1.6667 1 1 0 1.6330 0 1.7778 1.6859 1 1.9907 1 1.6667 1 0 1.6330 1.7778 0 1.6859 1.9907 1 1.1529 1 1.6667 0 1.6859 1.6859 1.6859 0 1.9868 1.9868 1 1 1 0
- 1 1 1.9907 1.9868 0 1.6667 1.6330 1.6330 1 0 1 1.9907 1 1.9868 1.6667 0 1.7249 1 1.6330 0


D :

R

1.6667 1 1.1529 1 1.6330 1.7249 0 1.0887 1 0 1 1.6667 1 1 1.6330 1 1.0887 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 546](<2010-arkus-deriving-finite-sphere-packings_images/imageFile546.png>)

![image 547](<2010-arkus-deriving-finite-sphere-packings_images/imageFile547.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.40206R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.4913 0.6653 0 0.5298 0.8165 −1.3765 −0.4636 0.8165 0.3441 0.9345 −0.0907 0.3441 0.7726 1.3608 −0.5735 0.7726 0.2722 −0.5735 −0.0662 0.8165 −0.5735 0.5298 0.8165 0.2294

C :

R

 

 

Packing 52 (Graph 201015):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6330 1.6330 1 1 1.6667 1 1 0 1.6859 0 2.4732 1.6859 1 2.4315 1 1.9868 1 0 1.6330 2.4732 0 1.0887 1.9907 1 1.7249 1 1.6667 0 1.6330 1.6859 1.0887 0 1.6667 1.6667 1 1 1 0
- 1 1 1.9907 1.6667 0 1.6667 1.0887 1.6330 1 0 1 2.4315 1 1.6667 1.6667 0 1.9907 1 1.6330 0


D :

R

1.6667 1 1.7249 1 1.0887 1.9907 0 1.6330 1 0 1 1.9868 1 1 1.6330 1 1.6330 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 548](<2010-arkus-deriving-finite-sphere-packings_images/imageFile548.png>)

![image 549](<2010-arkus-deriving-finite-sphere-packings_images/imageFile549.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.87336R2|C1|1<br><br>|chiral|






0 0 0 0 1.6859 0 −1.6230 −0.1804 0 −1.3658 0.7909 0.4191 −0.0024 0.8429 −0.5380 −0.7533 −0.6140 −0.2358 −0.9130 1.3702 −0.2586 −0.8181 −0.0312 0.5743 −0.3675 0.8429 0.3929 −0.8632 0.3746 −0.3385

C :

R

 

 

Packing 53 (Graph 201576):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1.0887 1 1 1.6667 1 1 0 1.6330 0 1.7778 1.6330 1 1.9907 1 1.6667 1 0 1.6330 1.7778 0 1.7372 1.6667 1 1.8178 1 1.9907 0 1.0887 1.6330 1.7372 0 1.6667 1.1529 1 1.7249 1 0
- 1 1 1.6667 1.6667 0 1.6330 1.6330 1 1 0 1 1.9907 1 1.1529 1.6330 0 1.7778 1 1.6667 0


D :

R

1.6667 1 1.8178 1 1.6330 1.7778 0 1.9907 1 0 1 1.6667 1 1.7249 1 1 1.9907 0 1.6330 0 1 1 1.9907 1 1 1.6667 1 1.6330 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 550](<2010-arkus-deriving-finite-sphere-packings_images/imageFile550.png>)

![image 551](<2010-arkus-deriving-finite-sphere-packings_images/imageFile551.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.39108R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.4913 0.6653 0 0.1177 0.3629 −1.0196 −0.0662 0.8165 0.5735 0.9345 −0.0907 −0.3441 0.1104 1.3608 −0.9559 0.7726 0.2722 0.5735 −0.4636 0.8165 −0.3441 0.5298 0.8165 −0.2294

C :

R

 

 

Packing 54 (Graph 203132):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.1471 1.9956 1 1 1.6667 1.6859 1 0 1.6330 0 1.9956 1.1471 1 1.6667 1 1.6859 1 0 1.1471 1.9956 0 1.6330 1.7622 1 1.6667 1 1.6859 0 1.9956 1.1471 1.6330 0 1.7622 1.6667 1 1 1.6859 0
- 1 1 1.7622 1.7622 0 1.6330 1.6330 1.9868 1 0 1 1.6667 1 1.6667 1.6330 0 1.0887 1 1 0


D :

R

1.6667 1 1.6667 1 1.6330 1.0887 0 1 1 0 1.6859 1.6859 1 1 1.9868 1 1 0 1.6059 0

 

 

1 1 1.6859 1.6859 1 1 1 1.6059 0 0 0 0 0 0 0 0 0 0 0 0

![image 552](<2010-arkus-deriving-finite-sphere-packings_images/imageFile552.png>)

![image 553](<2010-arkus-deriving-finite-sphere-packings_images/imageFile553.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.16647R2|Cs|1| |






0 0 0 0 −1.6330 0 1.1471 0 0 1.1471 −1.6330 −0.0000 −0.3441 −0.8165 −0.4636 0.5735 −0.2722 0.7726 0.5735 −1.3608 0.7726 1.3765 −0.8165 0.5298 −0.2294 −0.8165 0.5298 0.5735 −0.8165 −0.0662

C :

R

 

 

Packing 55 (Graph 203149):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 1 0 0 0 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6667 1.9907 1 1 1.6667 1.6330 1 0 1.0887 0 1.9907 1.6667 1 1.6667 1 1.6330 1 0 1.6667 1.9907 0 1.0887 1.8113 1 1.6667 1 1.6330 0 1.9907 1.6667 1.0887 0 1.8113 1.6667 1 1 1.6330 0
- 1 1 1.8113 1.8113 0 1.6859 1.6859 1.9868 1.6059 0 1 1.6667 1 1.6667 1.6859 0 1.6330 1 1 0


D :

R

1.6667 1 1.6667 1 1.6859 1.6330 0 1 1 0 1.6330 1.6330 1 1 1.9868 1 1 0 1 0

 

 

1 1 1.6330 1.6330 1.6059 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 554](<2010-arkus-deriving-finite-sphere-packings_images/imageFile554.png>)

![image 555](<2010-arkus-deriving-finite-sphere-packings_images/imageFile555.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.30682R2|Cs<br><br>|1| |






0 0 0 0 1.0887 0 −1.6667 −0.0000 0 −1.6667 1.0887 −0.0000 −0.1491 0.5443 0.8255 −0.8333 −0.2722 −0.4811 −0.8333 1.3608 −0.4811 −1.3333 0.5443 −0.7698 −0.3333 0.5443 −0.7698 −0.8333 0.5443 0

C :

R

 

 

Packing 56 (Graph 203153):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 0 0 0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6667 1.9907 1 1 1.6667 1.6330 1 0 1.6859 0 1.8113 1.1471 1 1.9868 1 1.6859 1.6059 0 1.6667 1.8113 0 1.0887 1.9907 1 1.6667 1 1.6330 0 1.9907 1.1471 1.0887 0 1.7249 1.6667 1 1 1.6330 0
- 1 1 1.9907 1.7249 0 1.6330 1.0887 1.6667 1 0 1 1.9868 1 1.6667 1.6330 0 1.6330 1 1 0


D :

R

1.6667 1 1.6667 1 1.0887 1.6330 0 1 1 0 1.6330 1.6859 1 1 1.6667 1 1 0 1 0

 

 

1 1.6059 1.6330 1.6330 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 556](<2010-arkus-deriving-finite-sphere-packings_images/imageFile556.png>)

![image 557](<2010-arkus-deriving-finite-sphere-packings_images/imageFile557.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.13008R2|C1|1<br><br>|chiral|






0 0 0 0 1.6859 0 1.5154 0.6938 0 1.0877 1.6280 0.3597 −0.4470 0.8429 0.2994 0.9308 −0.0312 0.3642 0.2892 1.3702 0.9037 1.1043 0.7909 0.9064 0.1951 0.3746 0.9064 0.5306 0.8429 0

C :

R

 

 

Packing 57 (Graph 203204):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 0 1 0 0 1 1 0 1 1 0 1 1 1 1 1 0 1 1 0 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6667 1.7622 1 1 1.9868 1.6330 1 0 1.6330 0 1.7249 1.6667 1 1.6667 1 1.0887 1 0 1.6667 1.7249 0 1.7622 1.9907 1 1.9868 1 1 0 1.7622 1.6667 1.7622 0 1.9956 1.1471 1 1 1.6859 0
- 1 1 1.9907 1.9956 0 1.6330 1.6859 1.6667 1 0 1 1.6667 1 1.1471 1.6330 0 1.6859 1 1 0


D :

R

1.9868 1 1.9868 1 1.6859 1.6859 0 1 1.6059 0 1.6330 1.0887 1 1 1.6667 1 1 0 1 0

 

 

1 1 1 1.6859 1 1 1.6059 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 558](<2010-arkus-deriving-finite-sphere-packings_images/imageFile558.png>)

![image 559](<2010-arkus-deriving-finite-sphere-packings_images/imageFile559.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.44100R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.4853 −0.7560 0 −0.4684 −0.9168 1.4302 0.4779 −0.8165 −0.3239 −0.7965 −0.2722 0.5399 −0.0602 −1.7189 0.9945 −0.8496 −1.2701 0.5759 −0.5195 −0.8165 −0.2519 0 −0.8165 0.5759

C :

R

 

 

Packing 58 (Graph 203235):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6667 1.9907 1 1 1.6667 1.6330 1 0 1.0887 0 1.9907 1.6667 1 1.6667 1 1.6330 1 0 1.6667 1.9907 0 1.9907 2.4315 1 1.6667 1 1 0 1.9907 1.6667 1.9907 0 1.8113 1.6667 1 1 1.6330 0
- 1 1 2.4315 1.8113 0 1.6859 1.6859 1.9868 1.6059 0 1 1.6667 1 1.6667 1.6859 0 1.6330 1 1 0


D :

R

1.6667 1 1.6667 1 1.6859 1.6330 0 1 1 0 1.6330 1.6330 1 1 1.9868 1 1 0 1 0

 

 

1 1 1 1.6330 1.6059 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 560](<2010-arkus-deriving-finite-sphere-packings_images/imageFile560.png>)

![image 561](<2010-arkus-deriving-finite-sphere-packings_images/imageFile561.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.84776R2|C1|1<br><br>|chiral|






0 0 0 0 −1.0887 0 −1.6667 −0.0000 0 −0.8333 −1.0887 −1.4434 0.6404 −0.5443 −0.5419 −0.8333 0.2722 −0.4811 −0.8333 −1.3608 −0.4811 −1.3333 −0.5443 −0.7698 −0.8333 −0.5443 0 −0.3333 −0.5443 −0.7698

C :

R

 

 

Packing 59 (Graph 203248):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 1 0 0 1 1 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6667 1.9907 1 1 1.6667 1.6330 1 0 1.0887 0 1.9907 1.6667 1 1.6667 1 1.6330 1 0 1.6667 1.9907 0 1.0887 2.4315 1 1.6667 1 1.6330 0 1.9907 1.6667 1.0887 0 2.4315 1.6667 1 1 1.6330 0
- 1 1 2.4315 2.4315 0 1.6859 1.6859 1.9868 1 0 1 1.6667 1 1.6667 1.6859 0 1.6330 1 1 0


D :

R

1.6667 1 1.6667 1 1.6859 1.6330 0 1 1 0 1.6330 1.6330 1 1 1.9868 1 1 0 1 0

 

 

1 1 1.6330 1.6330 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 562](<2010-arkus-deriving-finite-sphere-packings_images/imageFile562.png>)

![image 563](<2010-arkus-deriving-finite-sphere-packings_images/imageFile563.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.83314R2|Cs<br><br>|1| |






0 0 0 0 −1.0887 0 −1.6667 −0.0000 0 −1.6667 −1.0887 −0.0000 0.6404 −0.5443 0.5419

C :

R

- −0.8333 0.2722 0.4811

−0.8333 −1.3608 0.4811

- −1.3333 −0.5443


0.7698 −0.3333 −0.5443 0.7698 −0.8333 −0.5443 −0.0962

 

 

Packing 60 (Graph 203249):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 1 0 0 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6667 1.9907 1 1 1.6667 1.6330 1 0 1.6859 0 2.4315 1.9868 1 1.9868 1 1.6859 1 0 1.6667 2.4315 0 1.0887 1.9907 1 1.6667 1 1.6330 0 1.9907 1.9868 1.0887 0 1.7249 1.6667 1 1 1.6330 0
- 1 1 1.9907 1.7249 0 1.6330 1.0887 1.6667 1 0 1 1.9868 1 1.6667 1.6330 0 1.6330 1 1 0


D :

R

1.6667 1 1.6667 1 1.0887 1.6330 0 1 1 0 1.6330 1.6859 1 1 1.6667 1 1 0 1 0

 

 

1 1 1.6330 1.6330 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 564](<2010-arkus-deriving-finite-sphere-packings_images/imageFile564.png>)

![image 565](<2010-arkus-deriving-finite-sphere-packings_images/imageFile565.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.65640R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6859 0 −1.6644 0 0 −1.7131 −0.8476 0.5567 0 −0.8429 0.5379 −0.8328 0

C :

R

- −0.5526 −0.9059 −1.3702

0.2825

- −1.3764 −0.7909 −0.3832 −0.3777 −0.8429 −0.3832 −0.8540 −0.3746


 

 

0.3611

Packing 61 (Graph 203255):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 0 1 0 1 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6667 1.9907 1 1 1.6667 1.6330 1 0 1.6859 0 2.4315 1.1471 1 1.9868 1 1.6859 1.6059 0 1.6667 2.4315 0 1.9907 1.9907 1 1.6667 1 1 0 1.9907 1.1471 1.9907 0 1.7249 1.6667 1 1 1.6330 0
- 1 1 1.9907 1.7249 0 1.6330 1.0887 1.6667 1 0 1 1.9868 1 1.6667 1.6330 0 1.6330 1 1 0


D :

R

1.6667 1 1.6667 1 1.0887 1.6330 0 1 1 0 1.6330 1.6859 1 1 1.6667 1 1 0 1 0

 

 

1 1.6059 1 1.6330 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 566](<2010-arkus-deriving-finite-sphere-packings_images/imageFile566.png>)

![image 567](<2010-arkus-deriving-finite-sphere-packings_images/imageFile567.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.67102R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6859 0 1.6644 0 0 0.9193 −1.6280 0.6836 −0.0117 −0.8429 −0.5379 0.8328 0 0.5526 0.9059 −1.3702 −0.2825 1.3764 −0.7909 0.3832 0.8540 −0.3746 −0.3611 0.3777 −0.8429 0.3832

C :

R

 

 

Packing 62 (Graph 203262):





0 0 0 0 1 1 0 0 0 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6859 1.9868 1.8113 1 1 1.9868 1.6859 1.6059 0 1.6859 0 1.9907 1.6667 1 1.6667 1 1.6330 1 0 1.9868 1.9907 0 1.9907 1.7249 1 1.6667 1 1 0 1.8113 1.6667 1.9907 0 1.9907 1.6667 1 1 1.6330 0
- 1 1 1.7249 1.9907 0 1.0887 1.6330 1.6667 1 0 1 1.6667 1 1.6667 1.0887 0 1.6330 1 1 0


D :

R

1.9868 1 1.6667 1 1.6330 1.6330 0 1 1 0 1.6859 1.6330 1 1 1.6667 1 1 0 1 0 1.6059 1 1 1.6330 1 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 568](<2010-arkus-deriving-finite-sphere-packings_images/imageFile568.png>)

![image 569](<2010-arkus-deriving-finite-sphere-packings_images/imageFile569.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.67102R2|C1|1<br><br>|chiral|






0 0 0 0 1.6859 0 1.8013 0.8383 0 0.4446 0.9921 1.4487 0.1551 0.8429 −0.5152 0.9488 0.3157 0 0.6213 1.7171 0.7830 1.1905 0.8950 0.7898 0.9238 1.3112 −0.0794 0.2408 0.8429 0.4811

C :

R

 

 

Packing 63 (Graph 204149):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.4142 1.6330 1.4142 1 1 1.7321 1 1 0 1.4142 0 1.4142 1.6330 1 1.7321 1 1 1 0 1.6330 1.4142 0 1.9437 1.9149 1 1.7321 1 1.9149 0 1.4142 1.6330 1.9437 0 1.9149 1.7321 1 1.9149 1 0
- 1 1 1.9149 1.9149 0 1.7321 1.7321 1 1 0 1 1.7321 1 1.7321 1.7321 0 2.0000 1 1.7321 0


D :

R

1.7321 1 1.7321 1 1.7321 2.0000 0 1.7321 1 0 1 1 1 1.9149 1 1 1.7321 0 1.4142 0 1 1 1.9149 1 1 1.7321 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 570](<2010-arkus-deriving-finite-sphere-packings_images/imageFile570.png>)

![image 571](<2010-arkus-deriving-finite-sphere-packings_images/imageFile571.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.57778R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 −1.4142 0 1.3333 −0.9428 0 −0.0000 −0.4714 1.3333 −0.5000 −0.7071 −0.5000 1.0000 0 −0.0000 0 −1.4142 1.0000 0.5000 −0.7071 −0.5000 −0.5000 −0.7071 0.5000 0.5000 −0.7071 0.5000

C :

R

 

 

Packing 64 (Graph 204201):





0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 0 1 1 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 1 1 0 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6180 1.6779 1.7566 1 1 1.9843 1 1 0 1.6180 0 1.6779 1.6330 1 1.6180 1 1 1 0 1.6779 1.6779 0 1.7292 1.9843 1 1.9938 1 1.6532 0 1.7566 1.6330 1.7292 0 1.9889 1.1220 1 1.7007 1 0
- 1 1 1.9843 1.9889 0 1.6180 1.6779 1 1 0 1 1.6180 1 1.1220 1.6180 0 1.6779 1 1 0


D :

R

1.9843 1 1.9938 1 1.6779 1.6779 0 1.6532 1 0 1 1 1 1.7007 1 1 1.6532 0 1.0515 0 1 1 1.6532 1 1 1 1 1.0515 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 572](<2010-arkus-deriving-finite-sphere-packings_images/imageFile572.png>)

![image 573](<2010-arkus-deriving-finite-sphere-packings_images/imageFile573.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.36234R2|C1|1<br><br>|chiral|






0 0 0 0 −1.6180 0 −1.4700 −0.8090 0 −0.4737 −0.9385 1.4073 0.4867 −0.8090 −0.3295 −0.7876 −0.3090 0.5331 0 −1.7168 0.9951 −0.5124 −0.8090 −0.2880 0 −0.8090 0.5827 −0.7876 −1.3090 0.5331

C :

R

 

 

Packing 65 (Graph 209891):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 0 1 0 1 1 0 1 1 1 0 1 1 1 1 0 1 1 1 0 1 0

A :

 

 





- 0 1.5920 1.6330 1.7159 1 1 1.6667 1 1 0 1.5920 0 1.7167 1.5109 1 1.9667 1 1 1.5345 0 1.6330 1.7167 0 1.6715 1.9838 1 1 1.7496 1 0 1.7159 1.5109 1.6715 0 1.9443 1.9901 1 1 1 0
- 1 1 1.9838 1.9443 0 1.6938 1.6667 1 1.5920 0 1 1.9667 1 1.9901 1.6938 0 1.6330 1.6796 1 0


D :

R

1.6667 1 1 1 1.6667 1.6330 0 1.1832 1 0 1 1 1.7496 1 1 1.6796 1.1832 0 1 0 1 1.5345 1 1 1.5920 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 574](<2010-arkus-deriving-finite-sphere-packings_images/imageFile574.png>)

![image 575](<2010-arkus-deriving-finite-sphere-packings_images/imageFile575.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.28937R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.5920 0 1.4716 −0.7079 0 0.4744 −1.0038 −1.3084 −0.4743 −0.7960 0.3761 0.9564 0.1047 0.2726 0.8586 −1.3543 −0.4543 −0.1772 −0.7960 −0.5788 0.7278 −0.3706 −0.5771 0.5231 −0.7960 0.3045

C :

R

 

 

###### *Packing 66 (Graph 238324):





0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 1 1 1 0 1 0 1 1 0 0 0 1 1 0 1 1 0 1 1 0 0 1 0 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.7204 1.5130 1.7204 1 1 1 1 1 0 1.7204 0 1.9998 1.2992 1 2.3494 1 1.7221 1.7221 0 1.5130 1.9998 0 1.5224 1.7199 1 1.7199 1 1 0 1.7204 1.2992 1.5224 0 1.7221 1.9591 1 1.8799 1 0
- 1 1 1.7199 1.7221 0 1.7199 1 1 1.5130 0 1 2.3494 1 1.9591 1.7199 0 1.7199 1 1 0 1 1 1.7199 1 1 1.7199 0 1.5130 1 0 1 1.7221 1 1.8799 1 1 1.5130 0 1.2892 0 1 1.7221 1 1 1.5130 1 1 1.2892 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 576](<2010-arkus-deriving-finite-sphere-packings_images/imageFile576.png>)

![image 577](<2010-arkus-deriving-finite-sphere-packings_images/imageFile577.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.40267R2|C1|1<br><br>|chiral|






0 0 0 0 1.7204 0 −1.4687 0.3633 0 −0.6938 1.2299 −0.9829 0.1001 0.8602 0.5000 −0.8914 −0.4532 0 0.1001 0.8602 −0.5000 −0.7078 0.2889 0.6446 −0.7078 0.2889 −0.6446 −0.7443 1.0526 0

C :

R

 

 

###### *Packing 67 (Graph 240312):





0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 0 1 1 0 0 0 1 0 1 1 1 0 0 1 1 1 0

A :

 

 





- 0 1.6071 1.6071 1.6985 1 1 1 1 1 0 1.6071 0 1.6981 1.6584 1 1.9707 1 1.6426 1 0 1.6071 1.6981 0 1.6584 1.9707 1 1.6426 1 1 0 1.6985 1.6584 1.6584 0 1.9853 1.9853 1 1 1.6997 0
- 1 1 1.9707 1.9853 0 1.6981 1 1.6426 1 0 1 1.9707 1 1.9853 1.6981 0 1.6426 1 1 0 1 1 1.6426 1 1 1.6426 0 1 1.0853 0 1 1.6426 1 1 1.6426 1 1 0 1.0853 0 1 1 1 1.6997 1 1 1.0853 1.0853 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 578](<2010-arkus-deriving-finite-sphere-packings_images/imageFile578.png>)

![image 579](<2010-arkus-deriving-finite-sphere-packings_images/imageFile579.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.26747R2|Cs<br><br>|1| |






0 0 0 0 1.6071 0 −1.4418 0.7099 0 −0.5261 0.8454 −1.3760 0.5000 0.8035 0.3230 −0.9418 −0.0936 0.3230 0 0.8035 −0.5886 −0.7601 0.2752 −0.5886 −0.5000 0.8035 0.3230 −0.7913 1.2717 −0.5112

C :

R

 

 

Packing 68 (Graph 266450):





0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.5789 1.6859 1.6859 1 1.9868 1 1 1 0 1.5789 0 1.6859 1.6859 1 1.9868 1 1 1.6059 0 1.6859 1.6859 0 1.6330 2.0628 1 1 1.6667 1 0 1.6859 1.6859 1.6330 0 1.9904 1 1.6667 1 1 0
- 1 1 2.0628 1.9904 0 2.4320 1.0935 1 1.6448 0


D :

R

1.9868 1.9868 1 1 2.4320 0 1.6330 1.6330 1 0 1 1 1 1.6667 1.0935 1.6330 0 1.0887 1 0 1 1 1.6667 1 1 1.6330 1.0887 0 1 0 1 1.6059 1 1 1.6448 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 580](<2010-arkus-deriving-finite-sphere-packings_images/imageFile580.png>)

![image 581](<2010-arkus-deriving-finite-sphere-packings_images/imageFile581.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.63929R2|Cs|1| |






0 0 0 0 1.5789 0 1.4896 0.7895 0 0.5945 0.7895 1.3658 −0.5571 0.7895 −0.2576 1.5249 0.7895 0.9994 0.5356 0.7895 −0.2998 −0.0612 0.7895 0.6107 0.8006 0.2895 0.5247 0.8006 1.2895 0.5247

C :

R

 

 

Packing 69 (Graph 272310):





0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 0 1 1 1 1 0 0 0 0 0 1 1 1 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 1 1 0 0 1 0 1 0 0 0 1 0 1 1 1 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0

A :

 

 





- 0 1.6180 1.6779 1.7030 1 1.9889 1 1 1 0 1.6180 0 1.6779 1.7030 1 1.9889 1 1 1.6180 0 1.6779 1.6779 0 1.6330 1.6532 1 1 1.9843 1 0 1.7030 1.7030 1.6330 0 1.0383 1 1.6667 2.0186 1 0
- 1 1 1.6532 1.0383 0 1.6482 1.0515 1 1 0


D :

R

1.9889 1.9889 1 1 1.6482 0 1.6330 2.4047 1 0 1 1 1 1.6667 1.0515 1.6330 0 1 1 0 1 1 1.9843 2.0186 1 2.4047 1 0 1.6180 0 1 1.6180 1 1 1 1 1 1.6180 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 582](<2010-arkus-deriving-finite-sphere-packings_images/imageFile582.png>)

![image 583](<2010-arkus-deriving-finite-sphere-packings_images/imageFile583.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.59719R2|Cs<br><br>|1| |






0 0 0 0 1.6180 0 1.4700 0.8090 0 0.5919 0.8090 1.3768 −0.0770 0.8090 0.5827 1.5177 0.8090 0.9989 0.5124 0.8090 −0.2880 −0.4867 0.8090 −0.3295 0.7876 0.3090 0.5331 0.7876 1.3090 0.5331

C :

R

 

 

Packing 70 (Graph 282787):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 0 0 0 1 1 0 0 0 1 0 1 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 0 0 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.4142 1.6330 1.0887 1 1.6667 1 1 1 0 1.4142 0 1.4142 1.9437 1 1.9149 1 1.7321 1 0 1.6330 1.4142 0 1.6330 1.9149 1 1.9149 1 1 0 1.0887 1.9437 1.6330 0 1.9907 1 1.4782 1 1.6667 0
- 1 1 1.9149 1.9907 0 2.3333 1 1.7321 1 0


D :

R

1.6667 1.9149 1 1 2.3333 0 1.9437 1 1.6330 0 1 1 1.9149 1.4782 1 1.9437 0 1.7321 1.4142 0 1 1.7321 1 1 1.7321 1 1.7321 0 1 0 1 1 1 1.6667 1 1.6330 1.4142 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 584](<2010-arkus-deriving-finite-sphere-packings_images/imageFile584.png>)

![image 585](<2010-arkus-deriving-finite-sphere-packings_images/imageFile585.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.58889R2|C1|1<br><br>|chiral|






0 0 0 0 −1.4142 0 1.3333 −0.9428 0 0.5926 0.2095 −0.8889 −0.5000 −0.7071 0.5000 1.3889 −0.3928 −0.8333 −0.5000 −0.7071 −0.5000 1.0000 0 0 0.5000 −0.7071 0.5000 0.5000 −0.7071 −0.5000

C :

R

 

 

Packing 71 (Graph 282820):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 0 1 0 1 1 0 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6667 1.6667 1 1.6330 1 1 1 0 1.6330 0 2.5035 1.8178 1 1.7778 1 1.9907 1.6667 0 1.6667 2.5035 0 1.6667 1.9907 1 2.4369 1 1 0 1.6667 1.8178 1.6667 0 1.9907 1 1.7778 1 1.6330 0
- 1 1 1.9907 1.9907 0 1.6667 1 1.6330 1 0


D :

R

1.6330 1.7778 1 1 1.6667 0 1.9907 1 1 0 1 1 2.4369 1.7778 1 1.9907 0 1.6667 1.6330 0 1 1.9907 1 1 1.6330 1 1.6667 0 1 0 1 1.6667 1 1.6330 1 1 1.6330 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 586](<2010-arkus-deriving-finite-sphere-packings_images/imageFile586.png>)

![image 587](<2010-arkus-deriving-finite-sphere-packings_images/imageFile587.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.43498R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.6475 −0.2520 0 0.9432 0.6552 1.2078 0 0.8165 −0.5732 1.4506 0.6653 0.3461 −0.5308 0.8165 0.2271 0.8291 −0.0907 0.5516 0.8847 0.2722 −0.3786 0.4621 0.8165 0.3461

C :

R

 

 

Packing 72 (Graph 282980):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 0 0 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 1 0 1 0 1 1 1 0 1 0 1 1 1 1 0

A :

 

 





0 1.4142 1.6667 1.6667 1 1.6330 1 1 1 0 1.4142 0 1.9149 1.9149 1 1.4142 1 1.7321 1 0 1.6667 1.9149 0 1.6667 1.9437 1 2.3333 1 1 0 1.6667 1.9149 1.6667 0 2.3333 1 1.9437 1 1.6330 0

- 1 1 1.9437 2.3333 0 1.9149 1 1.7321 1 0

1.6330 1.4142 1 1 1.9149 0 1.9149 1 1 0

- 1 1 2.3333 1.9437 1 1.9149 0 1.7321 1.4142 0 1 1.7321 1 1 1.7321 1 1.7321 0 1 0 1 1 1 1.6330 1 1 1.4142 1 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 588](<2010-arkus-deriving-finite-sphere-packings_images/imageFile588.png>)

![image 589](<2010-arkus-deriving-finite-sphere-packings_images/imageFile589.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.04444R2|Cs|1| |






0 0 0 0 1.4142 0 1.6197 0.3928 0 0.7622 0.3928 1.4292 −0.1715 0.7071 −0.6860 1.1433 0.9428 0.6860 −0.6860 0.7071 0.1715 0.8575 0 0.5145 0.6860 0.7071 −0.1715 0.1715 0.7071 0.6860

C :

R

 

 

Packing 73 (Graph 283029):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 0 1 1 1 0 0 1 0 0 0 1 0 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 0 1 1 1 1 0 1 1 0

A :

 

 





- 0 1.6330 1.6330 1.0887 1 1.6667 1 1 1 0 1.6330 0 1.7778 2.4856 1 2.5035 1 1.9907 1 0 1.6330 1.7778 0 1.6330 1.6667 1 1.9907 1 1 0 1.0887 2.4856 1.6330 0 1.7249 1 2.0718 1 1.6667 0
- 1 1 1.6667 1.7249 0 1.9907 1 1.6330 1 0


D :

R

1.6667 2.5035 1 1 1.9907 0 2.4369 1 1.6330 0 1 1 1.9907 2.0718 1 2.4369 0 1.6667 1 0 1 1.9907 1 1 1.6330 1 1.6667 0 1 0 1 1 1 1.6667 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 590](<2010-arkus-deriving-finite-sphere-packings_images/imageFile590.png>)

![image 591](<2010-arkus-deriving-finite-sphere-packings_images/imageFile591.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.57750R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.4913 0.6653 0 −0.7151

- −0.7123 0.4079

0 0.8165 0.5735

- −1.6025 −0.2520


C :

R

0.3824 0.4636 0.8165 −0.3441 −0.9345 −0.0907 −0.3441 −0.5298 0.8165 −0.2294 −0.7726 0.2722 0.5735

 

 

Packing 74 (Graph 283324):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 0 0 0 1 0 0 1 1 1 1 0 0 1 1 1 0 1 0 1 1 0 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.9907 1.9907 1 1.6667 1 1.6330 1 0 1.6330 0 2.0718 1.1529 1 1.7249 1 1.0887 1.6667 0 1.9907 2.0718 0 1.6667 1.6667 1 2.4369 1 1 0 1.9907 1.1529 1.6667 0 1.6667 1 1.7778 1 1.6330 0
- 1 1 1.6667 1.6667 0 1.6330 1 1 1 0 1.6667 1.7249 1 1 1.6330 0 1.9907 1 1 0 1 1 2.4369 1.7778 1 1.9907 0 1.6667 1.6330 0


D :

R

1.6330 1.0887 1 1 1 1 1.6667 0 1 0 1 1.6667 1 1.6330 1 1 1.6330 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 592](<2010-arkus-deriving-finite-sphere-packings_images/imageFile592.png>)

![image 593](<2010-arkus-deriving-finite-sphere-packings_images/imageFile593.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.74362R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.8576 0.7157 0 −0.7604 1.6229 −0.8665

- −0.2736 0.8165 0.5084
- −1.2539 0.7560


C :

R

−0.7962 0.5771 0.8165 −0.0173 −1.0259 1.2701 0 −0.9618 0.2722 0 −0.3035 0.8165 −0.4911

 

 

Packing 75 (Graph 283448):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 1 1 0 1 1 0 0 1 0 0 0 0 1 0 0 1 1 1 1 0 0 1 1 1 0 1 1 1 1 0 1 0 1 1 1 1 0 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1.6667 1.7249 1 1.9907 1 1.6330 1 0 1.6330 0 1.7249 1.7874 1 2.0718 1 1.0887 1.6667 0 1.6667 1.7249 0 1.6330 1.6330 1 1.9907 1 1 0 1.7249 1.7874 1.6330 0 1.0887 1 2.0718 1 1 0
- 1 1 1.6330 1.0887 0 1.6667 1 1 1 0 1.9907 2.0718 1 1 1.6667 0 2.4369 1 1 0 1 1 1.9907 2.0718 1 2.4369 0 1.6667 1.6330 0


D :

R

1.6330 1.0887 1 1 1 1 1.6667 0 1 0 1 1.6667 1 1 1 1 1.6330 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 594](<2010-arkus-deriving-finite-sphere-packings_images/imageFile594.png>)

![image 595](<2010-arkus-deriving-finite-sphere-packings_images/imageFile595.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.78532R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.4853 −0.7560 0 −0.6576 −0.7493 1.4076 0 −0.8165 0.5759 −1.5682 −0.7157 0.9957 0.4779 −0.8165 −0.3239 −0.8496 −1.2701 0.5759 −0.7965 −0.2722 0.5399 −0.5195 −0.8165 −0.2519

C :

R

 

 

Packing 76 (Graph 283463):





0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 0 0 1 1 0 0 1 1 1 1 0 0 1 1 1 0 1 0 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.7778 2.4369 1 1.9907 1 1.6667 1 0 1.6667 0 2.4369 1.7778 1 1.9907 1 1.6667 1.6330 0 1.7778 2.4369 0 1.6667 1.6667 1 1.9907 1 1 0 2.4369 1.7778 1.6667 0 1.6667 1 1.9907 1 1.6330 0
- 1 1 1.6667 1.6667 0 1.6330 1 1 1 0 1.9907 1.9907 1 1 1.6330 0 1.6667 1 1 0 1 1 1.9907 1.9907 1 1.6667 0 1.6330 1 0


D :

R

1.6667 1.6667 1 1 1 1 1.6330 0 1 0 1 1.6330 1 1.6330 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 596](<2010-arkus-deriving-finite-sphere-packings_images/imageFile596.png>)

![image 597](<2010-arkus-deriving-finite-sphere-packings_images/imageFile597.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|9.34938R2<br><br>|C2v|2| |






0 0 0 0 −1.6667 0 1.7778 0 0 1.7778 −1.6667 −0.0000 0.3889 −0.8333 −0.3928 1.7222 −0.8333 0.5500 0 −0.8333 0.5500 1.3889 −0.8333 −0.3928 0.8889 −0.3333 0.3143 0.8889 −1.3333 0.3143

C :

R

 

 

Packing 77 (Graph 285359):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 0 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.5842 1.6330 1.0887 1 1.6667 1 1 1 0 1.5842 0 1.8341 1.6722 1 1.8200 1.6977 1 1.9819 0 1.6330 1.8341 0 1.6330 1.6667 1 1 1.9868 1 0 1.0887 1.6722 1.6330 0 1.7249 1 1.6667 1 1 0
- 1 1 1.6667 1.7249 0 1.9907 1 1.1471 1.6330 0


D :

R

1.6667 1.8200 1 1 1.9907 0 1.6330 1.6859 1 0 1 1.6977 1 1.6667 1 1.6330 0 1.6859 1 0 1 1 1.9868 1 1.1471 1.6859 1.6859 0 1.6059 0 1 1.9819 1 1 1.6330 1 1 1.6059 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 598](<2010-arkus-deriving-finite-sphere-packings_images/imageFile598.png>)

![image 599](<2010-arkus-deriving-finite-sphere-packings_images/imageFile599.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.34426R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.5842 0 −1.5295 0.5721 0 −0.2814 0.2836 −1.0127 0 0.7921 0.6103 −1.2197 0.6234 −0.9494 −0.7977 0.1980 0.5697 0.3880 0.7921 −0.4711 −0.9211 −0.1320 −0.3662 −0.5755 0.7921 −0.2034

C :

R

 

 

Packing 78 (Graph 285374):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 0 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.5842 1.0887 1.6330 1 1.6667 1 1 1 0 1.5842 0 1.9935 1.1882 1 1.7878 1.6977 1 1.6977 0 1.0887 1.9935 0 1.6330 1.6667 1 1 1.6667 1 0 1.6330 1.1882 1.6330 0 1.7622 1 1.9868 1 1 0
- 1 1 1.6667 1.7622 0 1.9956 1 1.1471 1.6859 0


D :

R

1.6667 1.7878 1 1 1.9956 0 1.6859 1.6330 1 0 1 1.6977 1 1.9868 1 1.6859 0 1.6859 1.6059 0 1 1 1.6667 1 1.1471 1.6330 1.6859 0 1 0 1 1.6977 1 1 1.6859 1 1.6059 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 600](<2010-arkus-deriving-finite-sphere-packings_images/imageFile600.png>)

![image 601](<2010-arkus-deriving-finite-sphere-packings_images/imageFile601.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.18309R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.5842 0 −1.0851 −0.0880 0 −0.6425 1.1882

- −0.9177 0.2088 0.7921 0.5735
- −1.4188 0.6601


C :

R

−0.5735 −0.5622 0.1980 0.8030 0.2088 0.7921 −0.5735 −0.5622 0.1980 −0.8030 −0.6104 0.7921 −0.0000

 

 

Packing 79 (Graph 286096):





0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 0 1 1 0 1 0 1 0 1 0 0 0 1 0 1 1 0 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1.7934 1 1.9907 1 1.8113 1.6330 0 1.6667 0 1.6667 1.6667 1 1.0887 1.6330 1 1 0 1.6667 1.6667 0 1.1471 1.6330 1 1 1.6859 1 0 1.7934 1.6667 1.1471 0 1.9956 1 1.7622 1 1.6859 0
- 1 1 1.6330 1.9956 0 1.6667 1 1.6859 1 0 1.9907 1.0887 1 1 1.6667 0 1.6330 1 1 0


D :

R

1 1.6330 1 1.7622 1 1.6330 0 1.9868 1 0 1.8113 1 1.6859 1 1.6859 1 1.9868 0 1.6059 0 1.6330 1 1 1.6859 1 1 1 1.6059 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 602](<2010-arkus-deriving-finite-sphere-packings_images/imageFile602.png>)

![image 603](<2010-arkus-deriving-finite-sphere-packings_images/imageFile603.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.36569R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6667 0 −1.4434 0.8333 0 −1.0635 0.9649 −1.0743 0 0.8333 0.5443 −1.0264 1.6667 −0.3629 −0.7698 0.3333 0.5443 −0.2380 1.5175 −0.9597 −0.7698 1.3333 0.5443 −0.4811 0.8333 −0.2722

C :

R

 

 

Packing 80 (Graph 286101):





0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 0 1 1 0 1 0 1 0 1 0 0 1 1 0 1 0 0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.1471 1.8144 1 1.7249 1 1.9907 1.6330 0 1.6667 0 1.9868 1.6667 1 1.6330 1.6330 1 1 0 1.1471 1.9868 0 1.1471 1.6859 1 1 1.6859 1.6059 0 1.8144 1.6667 1.1471 0 1.9907 1 1.7249 1 1.6330 0
- 1 1 1.6859 1.9907 0 1.6667 1 1.6330 1 0 1.7249 1.6330 1 1 1.6667 0 1.0887 1 1 0


D :

R

1 1.6330 1 1.7249 1 1.0887 0 1.6667 1 0 1.9907 1 1.6859 1 1.6330 1 1.6667 0 1 0 1.6330 1 1.6059 1.6330 1 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 604](<2010-arkus-deriving-finite-sphere-packings_images/imageFile604.png>)

![image 605](<2010-arkus-deriving-finite-sphere-packings_images/imageFile605.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.16405R2<br><br>|Cs|1| |






0 0 0 0 −1.6667 0 −1.1462 −0.0439 0 −1.3983 −0.9877 −0.6013 0.2615 −0.8333 0.4870 −1.4002 −0.9259 0.3968 −0.5612 −0.3333 0.7576 −0.9970 −1.7222 −0.0541 −0.5612 −1.3333 0.7576 −0.5421 −0.8333 −0.1082

C :

R

 

 

Packing 81 (Graph 286126):





0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 0 1 1 0 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 1 0 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 2.5073 1 1.9907 1 2.4315 1 0 1.6667 0 1.6667 1.6667 1 1.0887 1.6330 1 1 0 1.6667 1.6667 0 1.1471 1.6330 1 1 1.6859 1 0 2.5073 1.6667 1.1471 0 1.9956 1 1.7622 1 1.6859 0
- 1 1 1.6330 1.9956 0 1.6667 1 1.6859 1 0


D :

R

- 1.9907 1.0887 1 1 1.6667 0 1.6330 1 1 0 1 1.6330 1 1.7622 1 1.6330 0 1.9868 1 0
- 2.4315 1 1.6859 1 1.6859 1 1.9868 0 1.6059 0 1 1 1 1.6859 1 1 1 1.6059 0 0 0 0 0 0 0 0 0 0 0 0


 

 

![image 606](<2010-arkus-deriving-finite-sphere-packings_images/imageFile606.png>)

![image 607](<2010-arkus-deriving-finite-sphere-packings_images/imageFile607.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.93587R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6667 0 1.4434 −0.8333 0 1.5953 −1.8860 −0.4297 −0.0962 −0.8333

- −0.5443 1.0264
- −1.6667 0.3629 0.7698

−0.3333 −0.5443 0.6938

- −2.3070 −0.3295


C :

R

0.4811 −0.8333 0.2722 0.7698 −1.3333 −0.5443

 

 

Packing 82 (Graph 286157):





0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 0 1 1 0 1 0 1 0 1 0 0 1 1 1 1 0 0 1 1 1 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.9868 2.4637 1 1.7249 1 1.9907 1 0 1.6667 0 1.9868 1.6667 1 1.6330 1.6330 1 1 0 1.9868 1.9868 0 1.1471 1.6859 1 1 1.6859 1.6059 0 2.4637 1.6667 1.1471 0 1.9907 1 1.7249 1 1.6330 0
- 1 1 1.6859 1.9907 0 1.6667 1 1.6330 1 0 1.7249 1.6330 1 1 1.6667 0 1.0887 1 1 0


D :

R

1 1.6330 1 1.7249 1 1.0887 0 1.6667 1 0

1.9907 1 1.6859 1 1.6330 1 1.6667 0 1 0 1 1 1.6059 1.6330 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 608](<2010-arkus-deriving-finite-sphere-packings_images/imageFile608.png>)

![image 609](<2010-arkus-deriving-finite-sphere-packings_images/imageFile609.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.70498R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6667 0 1.8036 −0.8333 0 1.5709 −1.8210 −0.5350 0.1986 −0.8333 0.5159 1.2141 −0.9259 −0.8025 0.9403 −0.3333 0 0.6093 −1.7222 −0.7910 0.2716 −0.8333 −0.4815 0.9403 −1.3333 0

C :

R

 

 

Packing 83 (Graph 286160):





0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 0 1 1 0 1 0 1 0 1 0 0 1 1 0 1 1 0 1 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.9868 1.8144 1 1.7249 1 1.9907 1.6330 0 1.6667 0 1.9868 1.6667 1 1.6330 1.6330 1 1 0 1.9868 1.9868 0 1.9868 1.6859 1 1 1.6859 1 0 1.8144 1.6667 1.9868 0 1.9907 1 1.7249 1 1.6330 0
- 1 1 1.6859 1.9907 0 1.6667 1 1.6330 1 0 1.7249 1.6330 1 1 1.6667 0 1.0887 1 1 0


D :

R

1 1.6330 1 1.7249 1 1.0887 0 1.6667 1 0 1.9907 1 1.6859 1 1.6330 1 1.6667 0 1 0 1.6330 1 1 1.6330 1 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 610](<2010-arkus-deriving-finite-sphere-packings_images/imageFile610.png>)

![image 611](<2010-arkus-deriving-finite-sphere-packings_images/imageFile611.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.69036R2|Cs<br><br>|1| |






0 0 0 0 1.6667 0 1.8036 0.8333 0 0.4563 0.9877 1.4521 0.1986 0.8333 −0.5159 1.2141 0.9259 0.8025 0.9403 0.3333 −0.0688 0.6093 1.7222 0.7910 0.9403 1.3333 −0.0688 0.2716 0.8333 0.4815

C :

R

 

 

Packing 84 (Graph 286981):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.4142 1.4142 1 1.7321 1 1 1 0 1.6330 0 1.9437 1.4142 1 1.7321 1.6667 1 1.9149 0 1.4142 1.9437 0 1.6330 1.7321 1 1 1.9149 1 0 1.4142 1.4142 1.6330 0 1.7321 1 1.9149 1 1 0
- 1 1 1.7321 1.7321 0 2.0000 1 1 1.7321 0


D :

R

1.7321 1.7321 1 1 2.0000 0 1.7321 1.7321 1 0 1 1.6667 1 1.9149 1 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1.9149 1 1 1.7321 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 612](<2010-arkus-deriving-finite-sphere-packings_images/imageFile612.png>)

![image 613](<2010-arkus-deriving-finite-sphere-packings_images/imageFile613.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.45551R2<br><br>|C1|1<br><br>|chiral non-rigid|






0 0 0 0 1.6330 0 −1.3877 0.2720 0 −0.3203 0.8168 −1.1094 0.1602 0.8165 0.5547 −1.2811 0.8165 −0.8319 −0.6671 0.2722 0.6934 0.4003 0.8165 −0.4161 −0.7205 0 −0.6935 −0.5605 0.8165 −0.1386

C :

R

 

 

Packing 85 (Graph 287098):





0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6796 1.6796 1.1832 1 1.7496 1 1 1 0 1.6796 0 1.8689 1.6330 1 1.8362 1.6938 1 1.9667 0 1.6796 1.8689 0 1.6330 1.6938 1 1 1.9667 1 0 1.1832 1.6330 1.6330 0 1.6667 1 1.6667 1 1 0
- 1 1 1.6938 1.6667 0 1.9838 1 1 1.5920 0


D :

R

1.7496 1.8362 1 1 1.9838 0 1.6330 1.7167 1 0 1 1.6938 1 1.6667 1 1.6330 0 1.5920 1 0 1 1 1.9667 1 1 1.7167 1.5920 0 1.5345 0 1 1.9667 1 1 1.5920 1 1 1.5345 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 614](<2010-arkus-deriving-finite-sphere-packings_images/imageFile614.png>)

![image 615](<2010-arkus-deriving-finite-sphere-packings_images/imageFile615.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.35737R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6796 0 −1.5530 −0.6398 0 −0.3098 −0.4628 1.0440 0 −0.8398 −0.5414 −1.2640 −0.7474 0.9513 −0.7915 −0.2835 −0.5414 0.3610 −0.8398 0.4054 −0.9140 0 0.4054 −0.6162 −0.9204 0.2093

C :

R

 

 

Packing 86 (Graph 287190):





0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6796 1.1832 1.6796 1 1.7496 1 1 1 0 1.6796 0 1.9944 1.1739 1 1.7790 1.6938 1 1.6938 0 1.1832 1.9944 0 1.6330 1.6667 1 1 1.6667 1 0 1.6796 1.1739 1.6330 0 1.6938 1 1.9667 1 1 0
- 1 1 1.6667 1.6938 0 1.9838 1 1 1.5920 0


D :

R

1.7496 1.7790 1 1 1.9838 0 1.7167 1.6330 1 0 1 1.6938 1 1.9667 1 1.7167 0 1.5920 1.5345 0 1 1 1.6667 1 1 1.6330 1.5920 0 1 0 1 1.6938 1 1 1.5920 1 1.5345 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 616](<2010-arkus-deriving-finite-sphere-packings_images/imageFile616.png>)

![image 617](<2010-arkus-deriving-finite-sphere-packings_images/imageFile617.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.15643R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6796 0 1.1810 −0.0725 0 0.5802 −1.2694 −0.9345 −0.2115 −0.8398 0.5000 1.4157 −0.8090 −0.6345 0.5753 −0.2835 0.7672 −0.2115 −0.8398 −0.5000 0.5753 −0.2835 −0.7672 0.6508 −0.9204 0

C :

R

 

 

Packing 87 (Graph 287227):





0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 0 1 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1.7321 1 2.2361 1 1 1 0 1.7321 0 2.0000 1.4142 1 1.7321 1.7321 1 1.7321 0 1.7321 2.0000 0 1.4142 1.7321 1 1 1.7321 1 0 1.7321 1.4142 1.4142 0 1.7321 1 1.7321 1 1 0
- 1 1 1.7321 1.7321 0 2.0000 1 1 1.4142 0


D :

R

2.2361 1.7321 1 1 2.0000 0 1.7321 1.7321 1.4142 0 1 1.7321 1 1.7321 1 1.7321 0 1.4142 1 0 1 1 1.7321 1 1 1.7321 1.4142 0 1 0 1 1.7321 1 1 1.4142 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 618](<2010-arkus-deriving-finite-sphere-packings_images/imageFile618.png>)

![image 619](<2010-arkus-deriving-finite-sphere-packings_images/imageFile619.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.50000R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.7321 0 −1.6330 0.5774 0 −0.8165 1.1547 −1.0000 −0.0000 0.8660 0.5000 −1.6330 1.4434 −0.5000 −0.8165 0.2887 0.5000 0 0.8660 −0.5000 −0.8165 0.2887 −0.5000 −0.8165 1.1547 −0.0000

C :

R

 

 

Packing 88 (Graph 287262):





0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 0 0 1 0 1 1 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





0 1.7321 1.9149 1.7321 1 1.9149 1 1 1 0 1.7321 0 1.9149 1.4142 1 1.9149 1.7321 1 1.7321 0

- 1.9149 1.9149 0 1.7321 1.6330 1 1 1.9149 1.4142 0 1.7321 1.4142 1.7321 0 1.7321 1 1.7321 1 1 0

1 1 1.6330 1.7321 0 1.9149 1 1 1.4142 0

- 1.9149 1.9149 1 1 1.9149 0 1.4142 1.6330 1 0 1 1.7321 1 1.7321 1 1.4142 0 1.4142 1 0 1 1 1.9149 1 1 1.6330 1.4142 0 1 0 1 1.7321 1.4142 1 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 620](<2010-arkus-deriving-finite-sphere-packings_images/imageFile620.png>)

![image 621](<2010-arkus-deriving-finite-sphere-packings_images/imageFile621.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.43333R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7321 0 1.7078 −0.8660 0 0.4880 −1.1547 −1.1952 0.1464 −0.8660 0.4781 1.4151 −0.8660 −0.9562 0.9271 −0.2887 0.2390 −0.1464 −0.8660 −0.4781 0.6343 −0.2887 −0.7171 0.7807 −1.1547 −0.2390

C :

R

 

 

Packing 89 (Graph 287270):





0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 0 1 1 0 1 1 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6859 1.9770 1.9770 1 2.3778 1 1 1.5789 0 1.6859 0 1.9956 1.1471 1 1.7622 1.6667 1 1.6859 0 1.9770 1.9956 0 1.6330 1.6859 1 1 1.6667 1 0 1.9770 1.1471 1.6330 0 1.6859 1 1.6667 1 1 0
- 1 1 1.6859 1.6859 0 1.9868 1 1 1.6059 0


D :

R

2.3778 1.7622 1 1 1.9868 0 1.6330 1.6330 1 0 1 1.6667 1 1.6667 1 1.6330 0 1.0887 1 0 1 1 1.6667 1 1 1.6330 1.0887 0 1 0

 

 

1.5789 1.6859 1 1 1.6059 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 622](<2010-arkus-deriving-finite-sphere-packings_images/imageFile622.png>)

![image 623](<2010-arkus-deriving-finite-sphere-packings_images/imageFile623.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.63597R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6859 0 −1.7985 −0.8210 0 −0.6961 −1.6119 0.9087 −0.1897 −0.8429 −0.5035 −1.6506 −1.5988 0.6109 −0.9425 −0.3157 −0.1095 −0.2076 −0.8429 0.4964 −1.1642 −0.7394 0.7688 −0.9270 −1.3112 −0.0166

C :

R

 

 

Packing 90 (Graph 287539):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 0 1 1 1 1 1 0 1 0 1 1 0 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6938 1.6667 1.6938 1 1.9838 1 1 1.5920 0 1.6938 0 1.8000 1.6156 1 1.9885 1.9667 1 1 0 1.6667 1.8000 0 1.6330 1.1832 1 1 1.6667 1 0 1.6938 1.6156 1.6330 0 1.6796 1 1.9667 1 1 0
- 1 1 1.1832 1.6796 0 1.7496 1 1 1 0


D :

R

1.9838 1.9885 1 1 1.7496 0 1.7167 1.6330 1 0 1 1.9667 1 1.9667 1 1.7167 0 1.5920 1.5345 0 1 1 1.6667 1 1 1.6330 1.5920 0 1 0

 

 

1.5920 1 1 1 1 1 1.5345 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 624](<2010-arkus-deriving-finite-sphere-packings_images/imageFile624.png>)

![image 625](<2010-arkus-deriving-finite-sphere-packings_images/imageFile625.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.38470R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6938 0 1.5077 0.7104 0 0.5532 0.9233 −1.3078 0.3895 0.8469 0.3621 1.4983 0.8414 −0.9913 0.9211 0 0.3894 −0.0674 0.8469 −0.5275 0.8176 1.2999 −0.4200 0.7755 0.3093 −0.5504

C :

R

 

 

###### *Packing 91 (Graph 287604):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0 0 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 1 1 0 1 1 0 1 1 0 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1.7321 1 2.0000 1 1 1.4142 0 1.7321 0 2.0000 1.4142 1 2.2361 1.7321 1 1 0 1.7321 2.0000 0 1.4142 1.7321 1 1 1.7321 1 0 1.7321 1.4142 1.4142 0 1.7321 1 1.7321 1 1 0
- 1 1 1.7321 1.7321 0 2.2361 1 1 1 0


D :

R

2.0000 2.2361 1 1 2.2361 0 1.7321 1.7321 1.4142 0 1 1.7321 1 1.7321 1 1.7321 0 1.4142 1 0 1 1 1.7321 1 1 1.7321 1.4142 0 1 0

 

 

1.4142 1 1 1 1 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 626](<2010-arkus-deriving-finite-sphere-packings_images/imageFile626.png>)

![image 627](<2010-arkus-deriving-finite-sphere-packings_images/imageFile627.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.70000R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.7321 0 −1.6330 0.5774 0 −0.8165 1.1547 −1.0000 0 0.8660 0.5000 −1.6330 0.5774 −1.0000 −0.8165 0.2887 0.5000 −0.0000 0.8660 −0.5000 −0.8165 1.1547 0 −0.8165 0.2887 −0.5000

C :

R

 

 

Packing 92 (Graph 287669):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 1 0 1 1 1 0 1 1 0 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6448 1.6859 1.6859 1 1.9868 1 1 1.6059 0 1.6448 0 1.7428 1.6564 1 1.9915 1.0935 1 1 0 1.6859 1.7428 0 1.6330 1.9770 1 1 1.6667 1 0 1.6859 1.6564 1.6330 0 1.9770 1 1.6667 1 1 0
- 1 1 1.9770 1.9770 0 2.3778 1 1 1.5789 0


D :

R

1.9868 1.9915 1 1 2.3778 0 1.6330 1.6330 1 0 1 1.0935 1 1.6667 1 1.6330 0 1.0887 1 0 1 1 1.6667 1 1 1.6330 1.0887 0 1 0

 

 

1.6059 1 1 1 1.5789 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 628](<2010-arkus-deriving-finite-sphere-packings_images/imageFile628.png>)

![image 629](<2010-arkus-deriving-finite-sphere-packings_images/imageFile629.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.58472R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6448 0 −1.5033 0.7631 0 −0.5710 0.8523 1.3378 0.4396 0.8224 −0.3612 −1.5110 0.8167 0.9985 −0.5581 0.7629 −0.3265 0 0.8224 0.5654 −0.8094 1.3024 0.4772 −0.7910 0.3040 0.5310

C :

R

 

 

###### *Packing 93 (Graph 287714):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 1 1 0 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1.6330 1 1.9149 1 1 1.4142 0 1.7321 0 2.0000 1.7321 1 1.7321 1.7321 1 1 0 1.7321 2.0000 0 1.7321 1.7321 1 1 1.7321 1 0 1.6330 1.7321 1.7321 0 1.9149 1 1.9149 1 1.4142 0
- 1 1 1.7321 1.9149 0 1.9149 1 1 1 0


D :

R

1.9149 1.7321 1 1 1.9149 0 1.6330 1.4142 1 0 1 1.7321 1 1.9149 1 1.6330 0 1.4142 1 0 1 1 1.7321 1 1 1.4142 1.4142 0 1 0

 

 

1.4142 1 1 1.4142 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 630](<2010-arkus-deriving-finite-sphere-packings_images/imageFile630.png>)

![image 631](<2010-arkus-deriving-finite-sphere-packings_images/imageFile631.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.50000R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.7321 0 −1.6330 −0.5774 0 −0.5443 −0.7698 −1.3333

- −0.0000 −0.8660

0.5000 −1.3608

- −1.0585 −0.8333 −0.8165 −0.2887


C :

R

0.5000 0 −0.8660 −0.5000 −0.8165 −1.1547 −0.0000 −0.8165 −0.2887 −0.5000

 

 

Packing 94 (Graph 287739):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 1 0 1 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.6330 1.7321 1 1.9149 1 1 1.4142 0 1.7321 0 2.3805 1.4142 1 1.9149 1.7321 1 1 0 1.6330 2.3805 0 1.7321 1.9149 1 1 1.9149 1.4142 0 1.7321 1.4142 1.7321 0 1.7321 1 1.7321 1 1 0
- 1 1 1.9149 1.7321 0 1.9149 1 1 1 0


D :

R

1.9149 1.9149 1 1 1.9149 0 1.4142 1.6330 1 0 1 1.7321 1 1.7321 1 1.4142 0 1.4142 1 0 1 1 1.9149 1 1 1.6330 1.4142 0 1 0

 

 

1.4142 1 1.4142 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 632](<2010-arkus-deriving-finite-sphere-packings_images/imageFile632.png>)

![image 633](<2010-arkus-deriving-finite-sphere-packings_images/imageFile633.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.63333R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7321 0 1.6330 0 0 0.8165 −1.1547 1.0000 0 −0.8660 −0.5000 1.6330 −0.8660 0.5000 0.8165 −0.2887 −0.5000 −0.0000 −0.8660 0.5000 0.8165 −1.1547 0 0.8165 −0.2887 0.5000

C :

R

 

 

Packing 95 (Graph 290619):





0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 0 1 1 0 1 0 1 0 0 0 1 1 0 1 1 1 0 1 0 0 1 1 1 1 1 0 1 0 1 1 0 0 0 1 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.6779 1.6779 2.5113 1 2.4520 1 1.9843 1 0 1.6779 0 1.6180 1.1220 1 1.6779 1.6180 1 1 0 1.6779 1.6180 0 1.6330 1.6180 1 1 1 1 0 2.5113 1.1220 1.6330 0 1.7566 1 1.9889 1 1.7007 0
- 1 1 1.6180 1.7566 0 1.9843 1 1.6180 1 0 2.4520 1.6779 1 1 1.9843 0 1.6779 1 1.6532 0 1 1.6180 1 1.9889 1 1.6779 0 1.6180 1 0


D :

R

1.9843 1 1 1 1.6180 1 1.6180 0 1 0 1 1 1 1.7007 1 1.6532 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 634](<2010-arkus-deriving-finite-sphere-packings_images/imageFile634.png>)

![image 635](<2010-arkus-deriving-finite-sphere-packings_images/imageFile635.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.89768R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6779 0 −1.4175 0.8978 0

- −0.7929 2.3430 0.4334 0.1090 0.8390 0.5331
- −1.6264 1.7916 0.3969


C :

R

−0.7671 0.3568 0.5331 −0.9435 1.7143 −0.3295 −0.4617 0.8390 −0.2880 −0.7459 1.3554 0.5827

 

 

Packing 96 (Graph 291717):





0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 0 1 1 0 1 0 1 1 1 0 0 1 1 1 0 1 0 1 1 1 1 0 0 0 1 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.9938 1.6779 2.4520 1 1.9843 1 1.6779 1 0 1.9938 0 1.9843 1.1220 1 1.6779 1.6779 1 1.6532 0 1.6779 1.9843 0 1.6779 1.6180 1 1 1.6180 1 0 2.4520 1.1220 1.6779 0 1.6779 1 1.9843 1 1.6532 0
- 1 1 1.6180 1.6779 0 1.6180 1 1 1 0 1.9843 1.6779 1 1 1.6180 0 1.6180 1 1 0 1 1.6779 1 1.9843 1 1.6180 0 1.6180 1 0


D :

R

1.6779 1 1.6180 1 1 1 1.6180 0 1 0 1 1.6532 1 1.6532 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 636](<2010-arkus-deriving-finite-sphere-packings_images/imageFile636.png>)

![image 637](<2010-arkus-deriving-finite-sphere-packings_images/imageFile637.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.63469R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.9938 0

- −1.5177 −0.7155

0 −0.9487

- −2.1890 0.5664


0 −0.9969 −0.0214 −1.2926 −1.2783 0.7954 −0.6722 −0.5416 −0.5048 −0.3079 −1.4522 0.7822 −0.6624 −0.5623 0.4950 −0.8236 −1.4315 −0.0744

C :

R

 

 

Packing 97 (Graph 291725):





0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 0 1 1 0 1 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 1 0 0 1 0 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.9938 1.6779 1.8155 1 1.9843 1 1.6779 1.6532 0 1.9938 0 1.9843 1.9938 1 1.6779 1.6779 1 1 0 1.6779 1.9843 0 1.6779 1.6180 1 1 1.6180 1 0 1.8155 1.9938 1.6779 0 1.6779 1 1.9843 1 1.6532 0
- 1 1 1.6180 1.6779 0 1.6180 1 1 1 0 1.9843 1.6779 1 1 1.6180 0 1.6180 1 1 0


D :

R

1 1.6779 1 1.9843 1 1.6180 0 1.6180 1 0 1.6779 1 1.6180 1 1 1 1.6180 0 1 0 1.6532 1 1 1.6532 1 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 638](<2010-arkus-deriving-finite-sphere-packings_images/imageFile638.png>)

![image 639](<2010-arkus-deriving-finite-sphere-packings_images/imageFile639.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.63469R2|Cs<br><br>|1| |






0 0 0 0 1.9938 0 −1.5177 0.7155 0 −0.6962 0.8265 1.4588 0 0.9969 −0.0214 −1.2926 1.2783 0.7954 −0.6722 0.5416 −0.5048 −0.3079 1.4522 0.7822 −0.8236 1.4315 −0.0744 −0.6624 0.5623 0.4950

C :

R

 

 

Packing 98 (Graph 291912):





0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 1 1 0 0 1 1 0 1 0 1 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 1 1 1 0 1 1 0

A :

 

 





- 0 1.6779 1.6180 1.1220 1 1.6779 1 1.6180 1 0 1.6779 0 1.6779 1.8276 1 1.8155 1.6532 1 1.9843 0 1.6180 1.6779 0 1.6330 1.6180 1 1 1 1 0 1.1220 1.8276 1.6330 0 1.7566 1 1.7007 1.9889 1 0
- 1 1 1.6180 1.7566 0 1.9843 1 1 1.6180 0 1.6779 1.8155 1 1 1.9843 0 1.6532 1.6779 1 0


D :

R

1 1.6532 1 1.7007 1 1.6532 0 1 1 0

1.6180 1 1 1.9889 1 1.6779 1 0 1.6180 0 1 1.9843 1 1 1.6180 1 1 1.6180 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 640](<2010-arkus-deriving-finite-sphere-packings_images/imageFile640.png>)

![image 641](<2010-arkus-deriving-finite-sphere-packings_images/imageFile641.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.32942R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6779 0 1.4175 −0.7801 0 0.3065 −0.2188 1.0570 −0.1090 −0.8390 −0.5331 1.1809 −0.6958 0.9679 0.7459 −0.3226 −0.5827 0.7671 −1.3211 −0.5331 0.9435 0 0.3295 0.4617 −0.8390 0.2880

C :

R

 

 

Packing 99 (Graph 291998):





0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 1 1 0 0 1 1 0 1 0 1 0 0 1 1 0 1 1 1 1 1 0 0 1 0 1 1 1 1 1 0 1 1 0

A :

 

 





- 0 2.0000 1.7321 1.7321 1 2.0000 1 1.7321 1 0 2.0000 0 1.7321 1.7321 1 2.0000 1.7321 1 1.7321 0 1.7321 1.7321 0 1.6330 1.4142 1 1 1 1 0 1.7321 1.7321 1.6330 0 1.4142 1 1.9149 1.9149 1 0
- 1 1 1.4142 1.4142 0 1.7321 1 1 1 0 2.0000 2.0000 1 1 1.7321 0 1.7321 1.7321 1 0 1 1.7321 1 1.9149 1 1.7321 0 1 1 0


D :

R

1.7321 1 1 1.9149 1 1.7321 1 0 1.4142 0 1 1.7321 1 1 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 642](<2010-arkus-deriving-finite-sphere-packings_images/imageFile642.png>)

![image 643](<2010-arkus-deriving-finite-sphere-packings_images/imageFile643.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.70000R2|Cs<br><br>|1| |






0 0 0 0 2.0000 0 −1.4142 1.0000 0 −0.4714 1.0000 −1.3333

- −0.0000 1.0000

−0.0000 −1.4142 1.0000

- −1.0000 −0.7071


C :

R

0.5000 0.5000 −0.7071 1.5000 0.5000 −0.7071 0.5000 −0.5000 −0.7071 1.5000 −0.5000

 

 

Packing 100 (Graph 292451):





0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 1 1 1 0 1 0 1 1 0 1 0 1 1 0 0 1 1 0 1 1 1 0 0 1 1 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.6667 1.1220 1.9889 1 1.7566 1 1.6330 1.7007 0 1.6667 0 1.9889 1.1220 1 1.7566 1.6330 1 1.7007 0 1.1220 1.9889 0 1.6180 1.6779 1 1 1.6180 1 0 1.9889 1.1220 1.6180 0 1.6779 1 1.6180 1 1 0
- 1 1 1.6779 1.6779 0 1.9843 1 1 1.6532 0 1.7566 1.7566 1 1 1.9843 0 1.6180 1.6180 1 0


D :

R

1 1.6330 1 1.6180 1 1.6180 0 1 1 0 1.6330 1 1.6180 1 1 1.6180 1 0 1 0 1.7007 1.7007 1 1 1.6532 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 644](<2010-arkus-deriving-finite-sphere-packings_images/imageFile644.png>)

![image 645](<2010-arkus-deriving-finite-sphere-packings_images/imageFile645.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.09937R2<br><br>|Cs|1| |






0 0 0 0 −1.6667 0 1.1218 −0.0243 0 1.1218 −1.6424 0 −0.2661 −0.8333 −0.4845 1.4727 −0.8333 0.4715 0.5539 −0.3333 −0.7629 0.5539 −1.3333 −0.7629 1.3866 −0.8333 −0.5248 0.5431 −0.8333 0.1030

C :

R

 

 

###### *Packing 101 (Graph 294195):





0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 0 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 1 1 1 0 0 1 1 0 1 1 0 0 1 0 1 1 0 1 1 1 0 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.9149 1.7321 1 1.9149 1 1.4142 1.6330 0 1.6667 0 1.9149 1.7321 1 1.4142 1.6330 1.9149 1 0 1.9149 1.9149 0 1.7321 1.7321 1 1 1 1 0 1.7321 1.7321 1.7321 0 2.0000 1 1.7321 1 1.7321 0
- 1 1 1.7321 2.0000 0 1.7321 1 1.7321 1 0 1.9149 1.4142 1 1 1.7321 0 1.4142 1 1 0


D :

R

1 1.6330 1 1.7321 1 1.4142 0 1 1 0 1.4142 1.9149 1 1 1.7321 1 1 0 1.4142 0 1.6330 1 1 1.7321 1 1 1 1.4142 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 646](<2010-arkus-deriving-finite-sphere-packings_images/imageFile646.png>)

![image 647](<2010-arkus-deriving-finite-sphere-packings_images/imageFile647.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.47778R2|C1v|1| |






0 0 0 0 1.6667 0 1.7240 0.8333 0 0.6606 0.8333 −1.3672 0 0.8333 0.5469 1.1923 1.3333 −0.6836 0.9023 0.3333 0.2734 1.1923 0.3333 −0.6836 0.9023 1.3333 0.2734 0.3706 0.8333 −0.4102

C :

R

 

 

###### *Packing 102 (Graph 294321):





0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 0 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 1 1 1 0 0 1 1 0 1 1 0 0 1 1 1 1 0 1 1 1 0 0 1 0 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.4142 2.5166 1 1.9149 1 1.9149 1 0 1.6667 0 1.9149 1.7321 1 1.4142 1.6330 1.9149 1 0 1.4142 1.9149 0 1.7321 1.7321 1 1 1 1 0 2.5166 1.7321 1.7321 0 2.0000 1 1.7321 1 1.7321 0
- 1 1 1.7321 2.0000 0 1.7321 1 1.7321 1 0 1.9149 1.4142 1 1 1.7321 0 1.4142 1 1 0


D :

R

1 1.6330 1 1.7321 1 1.4142 0 1 1 0

1.9149 1.9149 1 1 1.7321 1 1 0 1.4142 0 1 1 1 1.7321 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 648](<2010-arkus-deriving-finite-sphere-packings_images/imageFile648.png>)

![image 649](<2010-arkus-deriving-finite-sphere-packings_images/imageFile649.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.81111R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6667 0 −1.3744 0.3333 0 −1.4956 1.8333 −0.8575 0.2021 0.8333 −0.5145 −1.3744 1.3333 0 −0.6468 0.3333 −0.6860 −1.4956 0.8333 −0.8575 −0.5255 0.8333 0.1715 −0.6468 1.3333 −0.6860

C :

R

 

 

Packing 103 (Graph 294347):





0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 0 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 0 1 0 1 0 1 0 0 1 1 1 0 0 1 1 0 1 1 0 0 1 0 1 1 1 1 1 1 0 0 1 1 1 0 1 1 0 1 1 1 0

A :

 

 





- 0 1.6667 1.9889 1.9889 1 2.4047 1 1.6482 1.6330 0 1.6667 0 1.9889 1.1220 1 1.7566 1.6330 1.7007 1 0 1.9889 1.9889 0 1.6180 1.6779 1 1 1 1 0 1.9889 1.1220 1.6180 0 1.6779 1 1.6180 1 1 0
- 1 1 1.6779 1.6779 0 1.9843 1 1.6532 1 0 2.4047 1.7566 1 1 1.9843 0 1.6180 1 1 0


D :

R

1 1.6330 1 1.6180 1 1.6180 0 1 1 0 1.6482 1.7007 1 1 1.6532 1 1 0 1.0515 0 1.6330 1 1 1 1 1 1 1.0515 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 650](<2010-arkus-deriving-finite-sphere-packings_images/imageFile650.png>)

![image 651](<2010-arkus-deriving-finite-sphere-packings_images/imageFile651.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.62111R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6667 0 1.8059 −0.8333 0 0.7077 −1.6424 0.8704 0.2080 −0.8333 −0.5121 1.6615 −1.6424 0.5698 0.9414 −0.3333 −0.0515 1.2103 −0.7805 0.8015 0.9414 −1.3333 −0.0515 0.2627 −0.8333 0.4864

C :

R

 

 

Packing 104 (Graph 297050):





0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 1 1 0 1 1 1 0 1 0 1 0 0 1 0 0 1 1 1 1 1 0 0 1 0 1 1 1 1 1 0 1 1 0

A :

 

 





- 0 1.4142 1.7321 2.3805 1 2.4495 1 1 1.7321 0 1.4142 0 1.7321 1.7321 1 2.0000 1.7321 1 1.7321 0 1.7321 1.7321 0 1.6330 1.4142 1 1 1 1 0 2.3805 1.7321 1.6330 0 1.4142 1 1.9149 1.9149 1 0
- 1 1 1.4142 1.4142 0 1.7321 1 1 1 0


D :

R

2.4495 2.0000 1 1 1.7321 0 1.7321 1.7321 1 0 1 1.7321 1 1.9149 1 1.7321 0 1 1 0 1 1 1 1.9149 1 1.7321 1 0 1.4142 0

 

 

1.7321 1.7321 1 1 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

![image 652](<2010-arkus-deriving-finite-sphere-packings_images/imageFile652.png>)

![image 653](<2010-arkus-deriving-finite-sphere-packings_images/imageFile653.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.96667R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.4142 0 −1.5811 0.7071 0 −1.1595 1.6499 1.2649 −0.3162 0.7071 0.6325 −1.8974 1.4142 0.6325 −0.9487 0 0.3162 −0.6325 0.7071 −0.3162 −1.2649 0.7071 0.9487 −0.9487 1.4142 0.3162

C :

R

 

 

###### *Packing 105 (Graph 298453):





0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 0 0 0 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 1 1 0 1 0 1 1 0 1 1 0 0 1 0 1 1 0 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 0

A :

 

 





- 0 1.7221 1.7199 1.5224 1 1.7199 1 1 1.5130 0 1.7221 0 1.9591 1.8909 1 1.5224 1.7204 1.8799 1 0 1.7199 1.9591 0 1.7221 1.7199 1 1 1 1 0 1.5224 1.8909 1.7221 0 1.9591 1 1.8799 1 1.7204 0
- 1 1 1.7199 1.9591 0 1.7199 1 1.5130 1 0


D :

R

1.7199 1.5224 1 1 1.7199 0 1.5130 1 1 0 1 1.7204 1 1.8799 1 1.5130 0 1 1 0 1 1.8799 1 1 1.5130 1 1 0 1.2892 0

 

 

1.5130 1 1 1.7204 1 1 1 1.2892 0 0 0 0 0 0 0 0 0 0 0 0

![image 654](<2010-arkus-deriving-finite-sphere-packings_images/imageFile654.png>)

![image 655](<2010-arkus-deriving-finite-sphere-packings_images/imageFile655.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.31195R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.7221 0 1.6098 −0.6056 0 0.5310 −0.4959 −1.3378 −0.0134 −0.8611 0.5083 1.1331 −1.0470 −0.7602 0.8090 −0.2920 0.5102 0.8717 −0.1253 −0.4738 0.8545 −1.2354 0.1815 0.1944 −0.8611 −0.4699

C :

R

 

 

Packing 106 (Graph 308923):





0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 1 1 0 0 0 1 1 1 0 1 1 1 0 0

A :

 

 





- 0 1.6236 1.6809 1.6809 1 1.9853 1 1 1 0 1.6236 0 1.6809 1.6809 1 1.9853 1 1 1.6362 0 1.6809 1.6809 0 1.6236 1.9853 1 1 1.6362 1 0 1.6809 1.6809 1.6236 0 1.9853 1 1.6362 1 1 0
- 1 1 1.9853 1.9853 0 2.3956 1 1 1.6236 0


D :

R

1.9853 1.9853 1 1 2.3956 0 1.6236 1.6236 1 0 1 1 1 1.6362 1 1.6236 0 1.0330 1 0 1 1 1.6362 1 1 1.6236 1.0330 0 1 0 1 1.6362 1 1 1.6236 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 656](<2010-arkus-deriving-finite-sphere-packings_images/imageFile656.png>)

![image 657](<2010-arkus-deriving-finite-sphere-packings_images/imageFile657.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.54661R2|D2d<br><br>|4|new seed|






0 0 0 0 −1.6236 0 1.4719 −0.8118 0 0.5764 −0.8118 1.3544 −0.4871 −0.8118 −0.3221 1.5112 −0.8118 0.9992 0.5121 −0.8118 −0.2806 −0.0576 −0.8118 0.5811 0.7969 −0.2953 0.5269 0.7969 −1.3283 0.5269

C :

R

 

 

Packing 107 (Graph 310808):





0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 0 0 0 1 1 0 0 0 1 0 1 1 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 0 1 1 0 0 1 0 1 1 0 1 1 1 0 0

A :

 

 





- 0 1.6330 1.4142 1.4142 1 1.7321 1 1 1 0 1.6330 0 1.4142 2.7080 1 2.3805 1 1.9149 1 0 1.4142 1.4142 0 1.6330 1.7321 1 1 1 1 0 1.4142 2.7080 1.6330 0 2.3805 1 1.9149 1 1.9149 0
- 1 1 1.7321 2.3805 0 2.4495 1 1.7321 1 0 1.7321 2.3805 1 1 2.4495 0 1.7321 1 1.7321 0


D :

R

- 1 1 1 1.9149 1 1.7321 0 1.4142 1 0 1 1.9149 1 1 1.7321 1 1.4142 0 1 0
- 1 1 1 1.9149 1 1.7321 1 1 0 0 0 0 0 0 0 0 0 0 0 0


 

 

![image 658](<2010-arkus-deriving-finite-sphere-packings_images/imageFile658.png>)

![image 659](<2010-arkus-deriving-finite-sphere-packings_images/imageFile659.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|9.66667R2|C2h<br><br>|2| |






0 0 0 0 1.6330 0 1.1547 0.8165 0 1.1547 −0.8165 0 −0.5774 0.8165 −0.0000 1.7321 −0.0000 −0.0000 0.2887 0.8165 0.5000 0.8660 −0.0000 −0.5000 0.2887 0.8165 −0.5000 0.8660 −0.0000 0.5000

C :

R

 

 

Packing 108 (Graph 317168):





0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 1 0 0 1 1 0 0 1 1 0 0 1 1 1 1 0 0 1 1 1 0 1 0 1 1 1 1 0 0 0 1 0 1 1 1 1 1 0 0

A :

 

 





- 0 1.4142 2.0000 2.4495 1 1.7321 1 1.7321 1 0 1.4142 0 2.4495 2.0000 1 1.7321 1 1.7321 1.7321 0 2.0000 2.4495 0 1.4142 1.7321 1 1.7321 1 1 0 2.4495 2.0000 1.4142 0 1.7321 1 1.7321 1 1.7321 0
- 1 1 1.7321 1.7321 0 1.4142 1 1 1 0 1.7321 1.7321 1 1 1.4142 0 1 1 1 0


D :

R

- 1 1 1.7321 1.7321 1 1 0 1.4142 1 0


1.7321 1.7321 1 1 1 1 1.4142 0 1 0 1 1.7321 1 1.7321 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 660](<2010-arkus-deriving-finite-sphere-packings_images/imageFile660.png>)

![image 661](<2010-arkus-deriving-finite-sphere-packings_images/imageFile661.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.00000R2|D2h<br><br>|4| |






0 0 0 0 1.4142 0 2.0000 −0.0000 0 2.0000 1.4142 −0.0000 0.5000 0.7071 0.5000 1.5000 0.7071 −0.5000 0.5000 0.7071 −0.5000 1.5000 0.7071 0.5000 1.0000 0 0 1.0000 1.4142 −0.0000

C :

R

 

 

###### *Packing 109 (Graph 318627):





0 0 0 0 1 0 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 1 0 1 0 1 1 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 1 1 0 0 0 1 0 1 1 1 1 1 0 0

A :

 

 





- 0 1.7221 1.5224 1.7199 1 1.7199 1 1 1 0 1.7221 0 2.5620 1.5224 1 1.9591 1.7204 1 1.8799 0 1.5224 2.5620 0 1.7221 1.9591 1 1 1.8799 1 0 1.7199 1.5224 1.7221 0 1.7199 1 1.5130 1 1 0
- 1 1 1.9591 1.7199 0 1.7199 1 1 1.5130 0


D :

R

1.7199 1.9591 1 1 1.7199 0 1 1.5130 1 0 1 1.7204 1 1.5130 1 1 0 1.2892 1 0 1 1 1.8799 1 1 1.5130 1.2892 0 1 0 1 1.8799 1 1 1.5130 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 662](<2010-arkus-deriving-finite-sphere-packings_images/imageFile662.png>)

![image 663](<2010-arkus-deriving-finite-sphere-packings_images/imageFile663.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.61080R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 −1.7221 0 −1.4763 0.3718 0 −1.0461 −1.0470 0.8761 −0.0406 −0.8611 −0.5069 −1.6007 −0.6056 0.1707 −0.8585 −0.2920 −0.4215 −0.1435 −0.8611 0.4878 −0.8165 −0.1253 0.5636 −0.8689 −1.2354 −0.0899

C :

R

 

 

###### *Packing 110 (Graph 319641):





0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 0 1 0 1 1 0 0 1 1 0 1 0 1 1 1 0 0 1 1 0 1 1 0 1 1 1 1 0 0 1 0 0 1 1 1 1 1 0 0

A :

 

 





- 0 2.0000 2.0000 2.0000 1 1.7321 1 1.7321 1.7321 0 2.0000 0 2.0000 2.0000 1 1.7321 1.7321 1 1 0 2.0000 2.0000 0 2.0000 1.7321 1 1 1.7321 1 0 2.0000 2.0000 2.0000 0 1.7321 1 1.7321 1 1.7321 0
- 1 1 1.7321 1.7321 0 1.4142 1 1 1 0 1.7321 1.7321 1 1 1.4142 0 1 1 1 0


D :

R

1 1.7321 1 1.7321 1 1 0 1.4142 1 0 1.7321 1 1.7321 1 1 1 1.4142 0 1 0 1.7321 1 1 1.7321 1 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 664](<2010-arkus-deriving-finite-sphere-packings_images/imageFile664.png>)

![image 665](<2010-arkus-deriving-finite-sphere-packings_images/imageFile665.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.00000R2|Td<br><br>|12| |






0 0 0 0 2.0000 0 −1.7321 1.0000 0 −0.5774 1.0000 −1.6330 −0.0000 1.0000 −0.0000 −1.1547 1.0000 −0.8165 −0.8660 0.5000 −0.0000 −0.2887 1.5000 −0.8165 −0.8660 1.5000 −0.0000 −0.2887 0.5000 −0.8165

C :

R

 

 

Packing 111 (Graph 364071):





0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 0 1 0 1 1 0 0 0 1 1 1 1 1 1 0 1 0 1 0 0 1 1 1 0 1 0 1 1 0 0 1 0 1 1 1 0 0 1 1 1 0

A :

 

 





- 0 1.2892 1.7221 1.7221 1 1 1 1 1 0 1.2892 0 1.7221 1.7221 1 1 1.5130 1 1 0 1.7221 1.7221 0 1.5203 1.9998 2.3494 1 1 1.7204 0 1.7221 1.7221 1.5203 0 2.3494 1.9998 1 1.7204 1 0
- 1 1 1.9998 2.3494 0 1 1.7199 1 1.5130 0 1 1 2.3494 1.9998 1 0 1.7199 1.5130 1 0 1 1.5130 1 1 1.7199 1.7199 0 1 1 0 1 1 1 1.7204 1 1.5130 1 0 1.2892 0 1 1 1.7204 1 1.5130 1 1 1.2892 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 666](<2010-arkus-deriving-finite-sphere-packings_images/imageFile666.png>)

![image 667](<2010-arkus-deriving-finite-sphere-packings_images/imageFile667.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.74446R2|C2v|2| |






0 0 0 0 1.2892 0 1.5969 0.6446 0 0.8733 0.6446 1.3370 −0.2706 0.6446 −0.7150 −0.7466 0.6446 0.1644 0.8702 0.1446 0.4710 0.6684 0.6446 −0.3712 0 0.6446 0.7626 0.8702 1.1446 0.4710

C :

R

 

 

Packing 112 (Graph 379658):





0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 0 1 0 1 0 1 0 0 1 0 1 0 1 1 1 0 0 0 1 1 1 0 1 1 0 1 1 1 0 0 0 1 1 0 1 1 0 1 0 0 1 1 0 1 1 0 1 1 0 1 0

A :

 

 





- 0 1.7247 1.7247 1.6507 1 1 1.6507 1.6507 1 0 1.7247 0 1.7247 1.6507 1 1.6507 1 1 1 0 1.7247 1.7247 0 1.6507 1.6507 1 1 1 1.6507 0 1.6507 1.6507 1.6507 0 1.9060 1.9060 1 1.9060 1 0
- 1 1 1.6507 1.9060 0 1 1.4142 1 1 0 1 1.6507 1 1.9060 1 0 1.4142 1 1.4142 0


D :

R

1.6507 1 1 1 1.4142 1.4142 0 1 1 0 1.6507 1 1 1.9060 1 1 1 0 1.4142 0

 

 

1 1 1.6507 1 1 1.4142 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

![image 668](<2010-arkus-deriving-finite-sphere-packings_images/imageFile668.png>)

![image 669](<2010-arkus-deriving-finite-sphere-packings_images/imageFile669.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.03459R2<br><br>|C3v|3| |






0 0 0 0 1.7247 0 1.4937 0.8624 0 0.4979 0.8624 1.3165 −0.0795 0.8624 −0.5000 0.7866 0.3624 −0.5000 0.7866 1.3624 0.5000 0.7866 1.3624 −0.5000 −0.0795 0.8624 0.5000 0.7866 0.3624 0.5000

C :

R

 

 

Packing 113 (Graph 394490):





0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 1 1 0 1 1 0 1 0 0 1 1 0 1 1 0 1 1 0 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 1.9149 1.9149 1 1 1 0 1.7321 0 1.4142 1.7321 1 1.9149 1 1 1.7321 0 1.7321 1.4142 0 1.7321 1.9149 1 1 1.7321 1 0
- 1 1.7321 1.7321 0 1.4142 1.4142 1.4142 1 1 0 1.9149 1 1.9149 1.4142 0 1.8856 1.6330 1 1.9149 0 1.9149 1.9149 1 1.4142 1.8856 0 1.6330 1.9149 1 0


D :

R

1 1 1 1.4142 1.6330 1.6330 0 1 1 0 1 1 1.7321 1 1 1.9149 1 0 1.4142 0 1 1.7321 1 1 1.9149 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 670](<2010-arkus-deriving-finite-sphere-packings_images/imageFile670.png>)

![image 671](<2010-arkus-deriving-finite-sphere-packings_images/imageFile671.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.48889R2|Cs<br><br>|1| |






0 0 0 0 1.7321 0 −1.2910 1.1547 0 −0.1291 0.2887 0.9487 0.3012 1.6358 0.9487 −1.4201 0.8660 0.9487 −0.3873 0.8660 −0.3162 0.3873 0.8660 0.3162 −0.9037 0.2887 0.3162 −0.5164 1.1547 0.6325

C :

R

 

 

Packing 114 (Graph 394589):





0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 1 1 0 1 1 0 1 0 1 1 1 0 1 1 0 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1.9907 1 1 1 0 1.6667 0 1.6667 1.9907 1 1.9907 1 1 1.6330 0 1.6667 1.6667 0 1.9907 1.9907 1 1 1.6330 1 0
- 1 1.9907 1.9907 0 1.7778 1.7778 1.6330 1 1 0 1.9907 1 1.9907 1.7778 0 1.7778 1.6330 1 1.6667 0 1.9907 1.9907 1 1.7778 1.7778 0 1.6330 1.6667 1 0


D :

R

1 1 1 1.6330 1.6330 1.6330 0 1 1 0 1 1 1.6330 1 1 1.6667 1 0 1 0 1 1.6330 1 1 1.6667 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 672](<2010-arkus-deriving-finite-sphere-packings_images/imageFile672.png>)

![image 673](<2010-arkus-deriving-finite-sphere-packings_images/imageFile673.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.99259R2<br><br>|C3v|3| |






0 0 0 0 −1.6667 0 −1.4434 −0.8333 0 0 0 −0.9979 0 −1.7222 −0.9979 −1.5075 −0.8333 −0.9979 −0.4811 −0.8333 0.2722 0 −0.8333 −0.5443 −0.7698 −0.3333 −0.5443 −0.7698 −1.3333 −0.5443

C :

R

 

 

Packing 115 (Graph 396368):





0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 1

A :

- 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 1 0 0 0 1 1 0 1
- 1 1 1 1 1 1 1 1 1 0


 

 





- 0 1.6330 1.0887 1 1.9907 1.7249 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.6667 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.7249 0 1.7778 1.8144 1 1.9907 1.6330 0 1.9907 1 1.6667 1.7778 0 1.0887 1.6667 1 1.6330 0 1.7249 1.6667 1 1.8144 1.0887 0 1.9907 1 1.6330 0


D :

R

1 1 1.6667 1 1.6667 1.9907 0 1.6330 1 0

1.6667 1 1 1.9907 1 1 1.6330 0 1 0 1 1 1 1.6330 1.6330 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 674](<2010-arkus-deriving-finite-sphere-packings_images/imageFile674.png>)

![image 675](<2010-arkus-deriving-finite-sphere-packings_images/imageFile675.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.33292R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.0264 −0.3629 0 0.4811 −0.2722 −0.8333 −0.5453 −1.7237 −0.8333 −1.2295 −0.8770 −0.8333 0.5774 −0.8165 0 −0.9623 −1.3608 −0.0000 −0.2887 −0.8165 0.5000 −0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 116 (Graph 396440):





0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 1 1 0 0 1 1 0 1 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1.7249 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.6667 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.7249 0 2.4369 2.4637 1 1.9907 1 0 1.9907 1 1.6667 2.4369 0 1.0887 1.6667 1 1.6330 0 1.7249 1.6667 1 2.4637 1.0887 0 1.9907 1 1.6330 0


D :

R

1 1 1.6667 1 1.6667 1.9907 0 1.6330 1 0

1.6667 1 1 1.9907 1 1 1.6330 0 1 0 1 1 1 1 1.6330 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 676](<2010-arkus-deriving-finite-sphere-packings_images/imageFile676.png>)

![image 677](<2010-arkus-deriving-finite-sphere-packings_images/imageFile677.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.88848R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.0264 0.3629 0 0.4811 0.2722 −0.8333 −0.5453 1.7237 0.8333 −1.2295 0.8770 0.8333 0.5774 0.8165 −0.0000 −0.9623 1.3608 0 −0.2887 0.8165 −0.5000 −0.2887 0.8165 0.5000

C :

R

 

 

Packing 117 (Graph 396446):





0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1.7249 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.6667 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.7249 0 2.4369 1.8144 1 1.9907 1.6330 0 1.9907 1 1.6667 2.4369 0 1.9907 1.6667 1 1 0 1.7249 1.6667 1 1.8144 1.9907 0 1.9907 1 1.6330 0


D :

R

1 1 1.6667 1 1.6667 1.9907 0 1.6330 1 0

1.6667 1 1 1.9907 1 1 1.6330 0 1 0 1 1 1 1.6330 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 678](<2010-arkus-deriving-finite-sphere-packings_images/imageFile678.png>)

![image 679](<2010-arkus-deriving-finite-sphere-packings_images/imageFile679.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.88848R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.0264 0.3629 0 0.4811 0.2722 −0.8333 −0.5453 1.7237 0.8333 −1.2295 0.8770 −0.8333 0.5774 0.8165 0 −0.9623 1.3608 −0.0000 −0.2887 0.8165 0.5000 −0.2887 0.8165 −0.5000

C :

R

 

 

Packing 118 (Graph 396466):





0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 1 0 0 1 1 1 0 1 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1.7249 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.6667 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.7249 0 1.7778 2.4637 1 1.9907 1.6330 0 1.9907 1 1.6667 1.7778 0 1.9907 1.6667 1 1.6330 0 1.7249 1.6667 1 2.4637 1.9907 0 1.9907 1 1 0


D :

R

1 1 1.6667 1 1.6667 1.9907 0 1.6330 1 0

1.6667 1 1 1.9907 1 1 1.6330 0 1 0 1 1 1 1.6330 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 680](<2010-arkus-deriving-finite-sphere-packings_images/imageFile680.png>)

![image 681](<2010-arkus-deriving-finite-sphere-packings_images/imageFile681.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.88848R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.0264 −0.3629 0 0.4811 −0.2722 0.8333 −0.5453 −1.7237 0.8333 −1.2295 −0.8770 −0.8333 0.5774 −0.8165 0 −0.9623 −1.3608 −0.0000 −0.2887 −0.8165 −0.5000 −0.2887 −0.8165 0.5000

C :

R

 

 

Packing 119 (Graph 396840):





0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 1 1 1 1 0 1 0 0 1 1 0 1 1 0 1 1 0 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1.0887 1 1 1.6330 0 1.6667 0 1.6667 1.0887 1 1.9907 1 1.6330 1 0 1.6667 1.6667 0 1.9907 1.0887 1 1.6330 1 1 0
- 1 1.0887 1.9907 0 1.7249 1.7249 1 1.6330 1.6667 0 1.9907 1 1.0887 1.7249 0 1.7249 1.6330 1.6667 1 0 1.0887 1.9907 1 1.7249 1.7249 0 1.6667 1 1.6330 0


D :

R

1 1 1.6330 1 1.6330 1.6667 0 1 1 0 1 1.6330 1 1.6330 1.6667 1 1 0 1 0

 

 

1.6330 1 1 1.6667 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 682](<2010-arkus-deriving-finite-sphere-packings_images/imageFile682.png>)

![image 683](<2010-arkus-deriving-finite-sphere-packings_images/imageFile683.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.10370R2|C3<br><br>|3<br><br>|chiral|






0 0 0 0 −1.6667 0 −1.4434 −0.8333 0 0.5132 −0.7778 0.3629 −0.9302 −1.7222 0.3629 −1.0264 0 0.3629 0 −0.8333 −0.5443 −0.7698 −0.3333 −0.5443 −0.7698 −1.3333 −0.5443 −0.4811 −0.8333 0.2722

C :

R

 

 

Packing 120 (Graph 396933):





0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 0 0 1 1 0 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1.9907 1 1 1.6330 0 1.6667 0 1.6667 1.0887 1 1.9907 1 1.6330 1 0 1.6667 1.6667 0 1.9907 1.0887 1 1.6330 1 1 0
- 1 1.0887 1.9907 0 1.7249 2.4369 1 1.6330 1.6667 0 1.9907 1 1.0887 1.7249 0 1.7249 1.6330 1.6667 1 0 1.9907 1.9907 1 2.4369 1.7249 0 1.6667 1 1 0


D :

R

1 1 1.6330 1 1.6330 1.6667 0 1 1 0 1 1.6330 1 1.6330 1.6667 1 1 0 1 0

 

 

1.6330 1 1 1.6667 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 684](<2010-arkus-deriving-finite-sphere-packings_images/imageFile684.png>)

![image 685](<2010-arkus-deriving-finite-sphere-packings_images/imageFile685.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.67778R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6667 0 −1.4434 0.8333 0 0.5132 0.7778 −0.3629 −0.9302 1.7222 −0.3629 −1.5075 0.8333 0.9979 0 0.8333 0.5443 −0.7698 0.3333 0.5443 −0.7698 1.3333 0.5443 −0.4811 0.8333 −0.2722

C :

R

 

 

Packing 121 (Graph 398930):





0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 1 1 0 1 0 1 1 0 1 1 0 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1.9907 1 1.6330 1 0 1.6667 0 1.6667 1.9907 1 1.9907 1 1 1 0 1.6667 1.6667 0 1.9907 1.0887 1 1.6330 1 1 0
- 1 1.9907 1.9907 0 2.4369 1.7778 1 1.6667 1.6330 0 1.9907 1 1.0887 2.4369 0 1.7249 1.6330 1 1 0 1.9907 1.9907 1 1.7778 1.7249 0 1.6667 1 1.6330 0


D :

R

1 1 1.6330 1 1.6330 1.6667 0 1 1 0

1.6330 1 1 1.6667 1 1 1 0 1 0 1 1 1 1.6330 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 686](<2010-arkus-deriving-finite-sphere-packings_images/imageFile686.png>)

![image 687](<2010-arkus-deriving-finite-sphere-packings_images/imageFile687.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.97407R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6667 0 −1.4434 −0.8333 0 0 0 0.9979 −0.9302 −1.7222 −0.3629 −1.5075 −0.8333 0.9979 0 −0.8333 0.5443 −0.7698 −1.3333 0.5443 −0.4811 −0.8333 −0.2722 −0.7698 −0.3333 0.5443

C :

R

 

 

Packing 122 (Graph 401472):





0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 1 0 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 0 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 1.4142 1.9149 1 1 1 0 1.7321 0 1.4142 1.7321 1 1.9149 1 1.7321 1 0 1.7321 1.4142 0 1.7321 1.9149 1 1.7321 1 1 0
- 1 1.7321 1.7321 0 1.9149 1.4142 1 1 1.4142 0 1.4142 1 1.9149 1.9149 0 2.5166 1 1.9149 1 0 1.9149 1.9149 1 1.4142 2.5166 0 1.9149 1 1.6330 0


D :

R

1 1 1.7321 1 1 1.9149 0 1.4142 1 0 1 1.7321 1 1 1.9149 1 1.4142 0 1 0 1 1 1 1.4142 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 688](<2010-arkus-deriving-finite-sphere-packings_images/imageFile688.png>)

![image 689](<2010-arkus-deriving-finite-sphere-packings_images/imageFile689.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.76667R2<br><br>|C2|2<br><br>|chiral|






0 0 0 0 1.7321 0 1.2910 1.1547 0 0.1291 0.2887 −0.9487 −0.5164 1.1547 0.6325 1.4201 0.8660 −0.9487 −0.3873 0.8660 −0.3162 0.9037 0.2887 −0.3162 0.3873 0.8660 0.3162 0.5164 1.1547 −0.6325

C :

R

 

 

Packing 123 (Graph 420068):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.7622 1 1 1.9868 1 0 1.6330 0 1.0887 1.6667 1 1.6667 1 1 1 0 1.6330 1.0887 0 1.9907 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.9907 0 1.1994 1.6667 1 1.8113 1.6330 0


1.7622 1 1.6667 1.1994 0 1.9956 1.1471 1 1.6859 0 1 1.6667 1 1.6667 1.9956 0 1.6330 1.6859 1 0 1 1 1.6667 1 1.1471 1.6330 0 1.6859 1 0

D :

R

1.9868 1 1 1.8113 1 1.6859 1.6859 0 1.6059 0 1 1 1 1.6330 1.6859 1 1 1.6059 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 690](<2010-arkus-deriving-finite-sphere-packings_images/imageFile690.png>)

![image 691](<2010-arkus-deriving-finite-sphere-packings_images/imageFile691.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.18791R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.0264 −1.2701 0 0.4811 −0.2722 −0.8333 0.3494 −1.4611 −0.9211 −0.9623 −0.2722 0 0.5774 −0.8165 0 −0.6077 −1.7189 −0.7895 −0.2887 −0.8165 0.5000 −0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 124 (Graph 420079):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1.7249 1 1 1.6667 1 0 1.0887 0 1.6330 1.6667 1 1.6667 1 1 1 0 1.6330 1.6330 0 1.7622 1.6667 1 1.9868 1 1 0
- 1 1.6667 1.7622 0 1.7315 1.1471 1 1.9956 1.6859 0


1.7249 1 1.6667 1.7315 0 1.9907 1.1471 1 1.6330 0 1 1.6667 1 1.1471 1.9907 0 1.6859 1.6330 1 0 1 1 1.9868 1 1.1471 1.6859 0 1.6859 1.6059 0

D :

R

1.6667 1 1 1.9956 1 1.6330 1.6859 0 1 0 1 1 1 1.6859 1.6330 1 1.6059 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 692](<2010-arkus-deriving-finite-sphere-packings_images/imageFile692.png>)

![image 693](<2010-arkus-deriving-finite-sphere-packings_images/imageFile693.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.16712R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.0887 0 1.5396

- −0.5443 0

0.2785 0.2722 0.9211 0.4170

- −1.4515 0.8333 0.9623 0.2722


C :

R

−0.0000 −0.2836 −0.5443 0.7895 0.9623 −1.3608 0 0.6736 −0.5443 −0.5000 0.6736 −0.5443 0.5000

 

 

Packing 125 (Graph 420083):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.9868 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.7249 0 1.7778 1.1471 1 1.9907 1.6330 0


1.9907 1 1.6667 1.7778 0 1.8113 1.6667 1 1.6330 0 1 1.9868 1 1.1471 1.8113 0 1.6859 1.6859 1.6059 0 1 1 1.6667 1 1.6667 1.6859 0 1.6330 1 0

D :

R

1.6667 1 1 1.9907 1 1.6859 1.6330 0 1 0 1 1 1 1.6330 1.6330 1.6059 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 694](<2010-arkus-deriving-finite-sphere-packings_images/imageFile694.png>)

![image 695](<2010-arkus-deriving-finite-sphere-packings_images/imageFile695.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.32762R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.0264 −0.3629 0 −0.4811 −0.2722 0.8333 0.5453 −1.7237 0.8333 0.6077 0 0.7895 −0.5774 −0.8165 0 0.9623 −1.3608 0 0.2887 −0.8165 −0.5000 0.2887 −0.8165 0.5000

C :

R

 

 

Packing 126 (Graph 420106):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 1 1 0 1 1 0 0 1 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.7622 1 1 1.9868 1 0 1.6330 0 1.0887 1.6667 1 1.6667 1 1 1 0 1.6330 1.0887 0 1.9907 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.9907 0 2.1234 1.6667 1 2.4315 1 0


1.7622 1 1.6667 2.1234 0 1.9956 1.1471 1 1.6859 0 1 1.6667 1 1.6667 1.9956 0 1.6330 1.6859 1 0 1 1 1.6667 1 1.1471 1.6330 0 1.6859 1 0

D :

R

1.9868 1 1 2.4315 1 1.6859 1.6859 0 1.6059 0 1 1 1 1 1.6859 1 1 1.6059 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 696](<2010-arkus-deriving-finite-sphere-packings_images/imageFile696.png>)

![image 697](<2010-arkus-deriving-finite-sphere-packings_images/imageFile697.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.75809R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.0264 1.2701 0 −0.4811 0.2722 0.8333 −0.3494 1.4611 −0.9211 0.9623 0.2722 −0.0000 −0.5774 0.8165 0 0.6077 1.7189 −0.7895 0.2887 0.8165 0.5000 0.2887 0.8165 −0.5000

C :

R

 

 

Packing 127 (Graph 420160):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 1 1 0 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1.7249 1 1 1.6667 1 0 1.0887 0 1.6330 1.6667 1 1.6667 1 1 1 0 1.6330 1.6330 0 1.7622 1.6667 1 1.9868 1 1 0
- 1 1.6667 1.7622 0 2.4634 1.1471 1 1.9956 1.6859 0


1.7249 1 1.6667 2.4634 0 1.9907 1.9868 1 1 0 1 1.6667 1 1.1471 1.9907 0 1.6859 1.6330 1 0 1 1 1.9868 1 1.9868 1.6859 0 1.6859 1.6059 0

D :

R

1.6667 1 1 1.9956 1 1.6330 1.6859 0 1 0 1 1 1 1.6859 1 1 1.6059 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 698](<2010-arkus-deriving-finite-sphere-packings_images/imageFile698.png>)

![image 699](<2010-arkus-deriving-finite-sphere-packings_images/imageFile699.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.73730R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.0887 0 1.5396 0.5443 0 0.2785 −0.2722 0.9211 0.4170 1.4515 −0.8333 0.9623 −0.2722 −0.0000 −0.2836 0.5443 0.7895 0.9623 1.3608 0 0.6736 0.5443 −0.5000 0.6736 0.5443 0.5000

C :

R

 

 

Packing 128 (Graph 420180):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 1 0 0 1 1 0 1 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.9868 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.7249 0 2.4369 1.9868 1 1.9907 1 0


1.9907 1 1.6667 2.4369 0 1.8113 1.6667 1 1.6330 0 1 1.9868 1 1.9868 1.8113 0 1.6859 1.6859 1.6059 0 1 1 1.6667 1 1.6667 1.6859 0 1.6330 1 0

D :

R

1.6667 1 1 1.9907 1 1.6859 1.6330 0 1 0 1 1 1 1 1.6330 1.6059 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 700](<2010-arkus-deriving-finite-sphere-packings_images/imageFile700.png>)

![image 701](<2010-arkus-deriving-finite-sphere-packings_images/imageFile701.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.86855R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.0264 −0.3629 0 0.4811 −0.2722 −0.8333 −0.5453 −1.7237 0.8333 −0.6077 0 0.7895 0.5774 −0.8165 −0.0000 −0.9623 −1.3608 −0.0000 −0.2887 −0.8165 −0.5000 −0.2887 −0.8165 0.5000

C :

R

 

 

Packing 129 (Graph 420187):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.9868 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.7249 0 2.4369 1.1471 1 1.9907 1.6330 0


1.9907 1 1.6667 2.4369 0 2.4315 1.6667 1 1 0 1 1.9868 1 1.1471 2.4315 0 1.6859 1.6859 1.6059 0 1 1 1.6667 1 1.6667 1.6859 0 1.6330 1 0

D :

R

1.6667 1 1 1.9907 1 1.6859 1.6330 0 1 0 1 1 1 1.6330 1 1.6059 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 702](<2010-arkus-deriving-finite-sphere-packings_images/imageFile702.png>)

![image 703](<2010-arkus-deriving-finite-sphere-packings_images/imageFile703.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.86855R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.0264 −0.3629 0 −0.4811 −0.2722 −0.8333 0.5453 −1.7237 0.8333 0.6077 0 −0.7895 −0.5774 −0.8165 −0.0000 0.9623 −1.3608 −0.0000 0.2887 −0.8165 0.5000 0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 130 (Graph 420198):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 0 1 1 1 0 1 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.9868 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1 1.6667 1 1 0
- 1 1.6667 1.7249 0 1.7778 1.9868 1 1.9907 1.6330 0


1.9907 1 1.6667 1.7778 0 2.4315 1.6667 1 1.6330 0 1 1.9868 1 1.9868 2.4315 0 1.6859 1.6859 1 0 1 1 1.6667 1 1.6667 1.6859 0 1.6330 1 0

D :

R

1.6667 1 1 1.9907 1 1.6859 1.6330 0 1 0 1 1 1 1.6330 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 704](<2010-arkus-deriving-finite-sphere-packings_images/imageFile704.png>)

![image 705](<2010-arkus-deriving-finite-sphere-packings_images/imageFile705.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.85393R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.0264 0.3629 0 −0.4811 0.2722 −0.8333 0.5453 1.7237 −0.8333 0.6077 −0.0859 0.7895 −0.5774 0.8165 −0.0000 0.9623 1.3608 0 0.2887 0.8165 0.5000 0.2887 0.8165 −0.5000

C :

R

 

 

Packing 131 (Graph 422919):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 0 0 0 1 1 1 0 0 1 1 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.6180 1.6779 1 1.9843 1 1 1.6180 1 0 1.6180 0 1.6779 1.6779 1 1.6180 1 1 1 0 1.6779 1.6779 0 1.8155 1.1220 1 1.9843 1 1.6532 0
- 1 1.6779 1.8155 0 1.8155 1.6779 1 1.9843 1.6532 0


1.9843 1 1.1220 1.8155 0 1.6779 1.6779 1 1.6532 0 1 1.6180 1 1.6779 1.6779 0 1.6180 1 1 0 1 1 1.9843 1 1.6779 1.6180 0 1.6180 1 0

D :

R

1.6180 1 1 1.9843 1 1 1.6180 0 1 0 1 1 1.6532 1.6532 1.6532 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 706](<2010-arkus-deriving-finite-sphere-packings_images/imageFile706.png>)

![image 707](<2010-arkus-deriving-finite-sphere-packings_images/imageFile707.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.29511R2|Cs<br><br>|1| |






0 0 0 0 −1.6180 0 −1.4700 −0.8090 0 −0.0402 −0.2480 −0.9679 −0.9239 −1.7168 −0.3697 −0.7876 −0.3090 0.5331 0.4867 −0.8090 −0.3295 −0.7876 −1.3090 0.5331 0 −0.8090 0.5827 −0.5124 −0.8090 −0.2880

C :

R

 

 

Packing 132 (Graph 423191):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 1 0 0 1 1 1 0 0 1 1 0 1 1 1 1 1 0 0

A :

 

 





- 0 1.6180 1.6779 1 1.9843 1 1 1.6180 1 0 1.6180 0 1.6779 1.6779 1 1.6180 1 1 1 0 1.6779 1.6779 0 2.4520 1.9938 1 1.9843 1 1 0
- 1 1.6779 2.4520 0 1.8155 1.6779 1 1.9843 1.6532 0


1.9843 1 1.9938 1.8155 0 1.6779 1.6779 1 1.6532 0 1 1.6180 1 1.6779 1.6779 0 1.6180 1 1 0 1 1 1.9843 1 1.6779 1.6180 0 1.6180 1 0

D :

R

1.6180 1 1 1.9843 1 1 1.6180 0 1 0 1 1 1 1.6532 1.6532 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 708](<2010-arkus-deriving-finite-sphere-packings_images/imageFile708.png>)

![image 709](<2010-arkus-deriving-finite-sphere-packings_images/imageFile709.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.83839R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6180 0 1.4700 0.8090 0 −0.8837 0.2480 0.3969 −0.0000 1.7168 0.9951 0.7876 0.3090 0.5331 −0.4867 0.8090 −0.3295 0.7876 1.3090 0.5331 0.5124 0.8090 −0.2880 −0.0770 0.8090 0.5827

C :

R

 

 

Packing 133 (Graph 423197):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 0 1 0 1 1 1 0 0 1 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.6180 1.6779 1 1.9843 1 1 1.6180 1 0 1.6180 0 1.6779 1.6779 1 1.6180 1 1 1 0 1.6779 1.6779 0 2.4520 1.1220 1 1.9843 1 1.6532 0
- 1 1.6779 2.4520 0 2.4520 1.6779 1 1.9843 1 0


1.9843 1 1.1220 2.4520 0 1.6779 1.6779 1 1.6532 0 1 1.6180 1 1.6779 1.6779 0 1.6180 1 1 0 1 1 1.9843 1 1.6779 1.6180 0 1.6180 1 0

D :

R

1.6180 1 1 1.9843 1 1 1.6180 0 1 0 1 1 1.6532 1 1.6532 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 710](<2010-arkus-deriving-finite-sphere-packings_images/imageFile710.png>)

![image 711](<2010-arkus-deriving-finite-sphere-packings_images/imageFile711.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.83839R2|Cs<br><br>|1| |






0 0 0 0 −1.6180 0 1.4700 −0.8090 0 −0.8837 −0.2480 −0.3969 0.9239 −1.7168 0.3697 0.7876 −0.3090 −0.5331 −0.4867 −0.8090 0.3295 0.7876 −1.3090 −0.5331 −0.0770 −0.8090 −0.5827 0.5124 −0.8090 0.2880

C :

R

 

 

Packing 134 (Graph 424068):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 1 1 1 0 0 1 0 1 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.6667 1 1 1 1 0 1.6330 0 1.7778 1.9907 1 1.9907 1 1 1.6667 0 1.6330 1.7778 0 1.9907 1.8178 1 1.6667 1.9907 1 0
- 1 1.9907 1.9907 0 2.4369 1.6667 1 1.6667 1 0


1.6667 1 1.8178 2.4369 0 1.7778 1.6330 1 1.9907 0 1 1.9907 1 1.6667 1.7778 0 1.6330 1.6667 1 0 1 1 1.6667 1 1.6330 1.6330 0 1 1 0 1 1 1.9907 1.6667 1 1.6667 1 0 1.6330 0 1 1.6667 1 1 1.9907 1 1 1.6330 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 712](<2010-arkus-deriving-finite-sphere-packings_images/imageFile712.png>)

![image 713](<2010-arkus-deriving-finite-sphere-packings_images/imageFile713.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.20453R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.4913 −0.6653 0

- −0.0589 0

0.9941 0.1104

- −1.3608 −0.9559


C :

R

0.9345 0 −0.3441 −0.0662 −0.8165 0.5735 −0.4636 −0.8165 −0.3441 0.7726 −0.2722 0.5735 0.5298 −0.8165 −0.2294

 

 

Packing 135 (Graph 424259):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 1 0 1 1 1 0 0 1 0 1 0 1 0 1 1 1 0 1 1 0 1 0 1 1 1 1 1 0 1 1 0 1 0

A :

 

 





- 0 1.4142 1.6330 1 1.7321 1 1 1 1 0 1.4142 0 1.4142 1.7321 1 1.7321 1 1 1 0 1.6330 1.4142 0 1.9149 1.7321 1 1.9149 1.9149 1 0
- 1 1.7321 1.9149 0 2.4495 1.4142 1 1.7321 1.7321 0


1.7321 1 1.7321 2.4495 0 2.0000 1.7321 1 1 0 1 1.7321 1 1.4142 2.0000 0 1.7321 1.7321 1 0 1 1 1.9149 1 1.7321 1.7321 0 1 1.4142 0 1 1 1.9149 1.7321 1 1.7321 1 0 1 0 1 1 1 1.7321 1 1 1.4142 1 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 714](<2010-arkus-deriving-finite-sphere-packings_images/imageFile714.png>)

![image 715](<2010-arkus-deriving-finite-sphere-packings_images/imageFile715.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.76667R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.4142 0 1.3333 −0.9428 0 0 0 −1.0000 −0.0000 −1.4142 1.0000 1.0000 0 0 −0.5000 −0.7071 −0.5000 −0.5000 −0.7071 0.5000 0.5000 −0.7071 0.5000 0.5000 −0.7071 −0.5000

C :

R

 

 

###### *Packing 136 (Graph 427393):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 0 1 1 0 1 1 0 1 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 0 1 1 0 1 1 0

A :

 

 





- 0 1.4142 1.6330 1 1.7321 1 1 1 1 0 1.4142 0 1.4142 1.7321 1 1.7321 1 1 1 0 1.6330 1.4142 0 2.5166 1.7321 1 1.9149 1.9149 1 0
- 1 1.7321 2.5166 0 2.0000 2.0000 1 1 1.7321 0


1.7321 1 1.7321 2.0000 0 2.0000 1.7321 1 1.7321 0 1 1.7321 1 2.0000 2.0000 0 1.7321 1.7321 1 0 1 1 1.9149 1 1.7321 1.7321 0 1 1 0 1 1 1.9149 1 1 1.7321 1 0 1.4142 0 1 1 1 1.7321 1.7321 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 716](<2010-arkus-deriving-finite-sphere-packings_images/imageFile716.png>)

![image 717](<2010-arkus-deriving-finite-sphere-packings_images/imageFile717.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.03333R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.4142 0 −1.3333 0.9428 0 1.0000 −0.0000 0 −0.0000 1.4142 1.0000 −1.0000 −0.0000 −0.0000 0.5000 0.7071 −0.5000 0.5000 0.7071 0.5000 −0.5000 0.7071 −0.5000 −0.5000 0.7071 0.5000

C :

R

 

 

###### *Packing 137 (Graph 445153):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1 1 1 0 1 1 0 1 0 0 1 1 0 1 1 0 1 1 0 0 0 1 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.7204 1.5130 1 1.5203 1 1.2892 1 1 0 1.7204 0 1.5224 1.7221 1 1.9591 1 1 1.8799 0 1.5130 1.5224 0 1.7199 1.9623 1 1 1.7199 1 0
- 1 1.7221 1.7199 0 1.9587 1.7199 1 1 1 0 1.5203 1 1.9623 1.9587 0 1.8907 1.6330 1 2.1580 0 1 1.9591 1 1.7199 1.8907 0 1.5130 1.7199 1 0


D :

R

1.2892 1 1 1 1.6330 1.5130 0 1 1 0 1 1 1.7199 1 1 1.7199 1 0 1.5130 0 1 1.8799 1 1 2.1580 1 1 1.5130 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 718](<2010-arkus-deriving-finite-sphere-packings_images/imageFile718.png>)

![image 719](<2010-arkus-deriving-finite-sphere-packings_images/imageFile719.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.48256R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.7204 0 1.2503 0.8520 0 −0.0645 0.2889 0.9552 −0.5459 1.2413 −0.6873 0.8913 0 −0.4521 0.4629 1.0526 0.5828 −0.4538 0.8602 0.2326 0.8311 0.1237 0.5422 0.3293 0.8602 −0.3893

C :

R

 

 

Packing 138 (Graph 449382):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.6667 1 1 1 1 0 1.6330 0 1.8144 1.6667 1 1.7249 1 1.9907 1 0 1.6330 1.8144 0 1.6667 2.5470 1 1.7249 1 1.9907 0
- 1 1.6667 1.6667 0 1.9907 1.6330 1.6330 1 1 0


1.6667 1 2.5470 1.9907 0 2.0718 1 2.4369 1 0 1 1.7249 1 1.6330 2.0718 0 1.0887 1 1.6667 0 1 1 1.7249 1.6330 1 1.0887 0 1.6667 1 0 1 1.9907 1 1 2.4369 1 1.6667 0 1.6330 0 1 1 1.9907 1 1 1.6667 1 1.6330 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 720](<2010-arkus-deriving-finite-sphere-packings_images/imageFile720.png>)

![image 721](<2010-arkus-deriving-finite-sphere-packings_images/imageFile721.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.29232R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.5087 −0.6250 0 −0.1818 −0.2722 0.9449 0.9092 −1.3608 −0.3150 −0.7961 −0.2117 −0.5669 0.1091 −0.8165 −0.5669 −0.9214 0 0.3780 0.4364 −0.8165 0.3780 −0.5455 −0.8165 0.1890

C :

R

 

 

Packing 139 (Graph 449396):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 0 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1.4142 1 1.6667 1 1 1 1 0 1.6330 0 1.4142 1.9149 1 1.9149 1 1.9149 1 0 1.4142 1.4142 0 1.7321 1.9149 1 1.7321 1 1 0
- 1 1.9149 1.7321 0 1.4530 1.7321 1.4142 1 1.7321 0


1.6667 1 1.9149 1.4530 0 2.3333 1 1.9437 1.6330 0 1 1.9149 1 1.7321 2.3333 0 1.7321 1 1 0 1 1 1.7321 1.4142 1 1.7321 0 1.7321 1 0 1 1.9149 1 1 1.9437 1 1.7321 0 1.4142 0 1 1 1 1.7321 1.6330 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 722](<2010-arkus-deriving-finite-sphere-packings_images/imageFile722.png>)

![image 723](<2010-arkus-deriving-finite-sphere-packings_images/imageFile723.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.61111R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.1547 0.8165 0 0 −0.0000 −1.0000 0.4811 1.3608 −0.8333 −0.8660 0 0.5000 0.5774 0.8165 −0.0000 −0.8660 −0.0000 −0.5000 −0.2887 0.8165 0.5000 −0.2887 0.8165 −0.5000

C :

R

 

 

Packing 140 (Graph 449426):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.6667 1 1 1 1 0 1.6330 0 1.7778 1.7249 1 1.6667 1 1.9907 1 0 1.6330 1.7778 0 1.6667 2.5035 1 1.9907 1 1.6667 0
- 1 1.7249 1.6667 0 2.0718 1.6330 1.0887 1 1.6667 0


1.6667 1 2.5035 2.0718 0 1.9907 1 2.4369 1 0 1 1.6667 1 1.6330 1.9907 0 1.6330 1 1 0 1 1 1.9907 1.0887 1 1.6330 0 1.6667 1 0 1 1.9907 1 1 2.4369 1 1.6667 0 1.6330 0 1 1 1.6667 1.6667 1 1 1 1.6330 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 724](<2010-arkus-deriving-finite-sphere-packings_images/imageFile724.png>)

![image 725](<2010-arkus-deriving-finite-sphere-packings_images/imageFile725.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.23745R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.4913 −0.6653 0 0.2036 −0.2117 0.9559 −0.8830 −1.3608 −0.3824 0.7726 −0.2722 −0.5735 −0.4636 −0.8165 0.3441 0.9345 0 0.3441 −0.0662 −0.8165 −0.5735 0.5298 −0.8165 0.2294

C :

R

 

 

Packing 141 (Graph 449737):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 0 1 1 1 1 0 0 1 1 0 1 1 1 1 0 1 1 1 0 1 0

A :

 

 





- 0 1.6330 1.4142 1 1.6667 1 1 1 1 0 1.6330 0 1.4142 1.9149 1 1.9149 1 1.9149 1 0 1.4142 1.4142 0 1.7321 1.9149 1 1.7321 1 1 0
- 1 1.9149 1.7321 0 2.3333 1.7321 1.4142 1 1 0


1.6667 1 1.9149 2.3333 0 1.9437 1 2.3333 1.6330 0 1 1.9149 1 1.7321 1.9437 0 1.7321 1 1.4142 0 1 1 1.7321 1.4142 1 1.7321 0 1.7321 1 0 1 1.9149 1 1 2.3333 1 1.7321 0 1 0 1 1 1 1 1.6330 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 726](<2010-arkus-deriving-finite-sphere-packings_images/imageFile726.png>)

![image 727](<2010-arkus-deriving-finite-sphere-packings_images/imageFile727.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.94444R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.1547 0.8165 0 −0.0000 −0.0000 1.0000 −0.4811 1.3608 −0.8333 0.8660 0 −0.5000 −0.5774 0.8165 0 0.8660 −0.0000 0.5000 0.2887 0.8165 0.5000 0.2887 0.8165 −0.5000

C :

R

 

 

Packing 142 (Graph 449787):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.6330 1 1.6667 1 1 1 1 0 1.6330 0 1.7778 1.9907 1 1.9907 1 1.6667 1 0 1.6330 1.7778 0 1.9907 2.5035 1 1.9907 1 1.6667 0
- 1 1.9907 1.9907 0 1.7778 1.6667 1.6667 1 1 0


1.6667 1 2.5035 1.7778 0 2.4369 1 1.9907 1 0 1 1.9907 1 1.6667 2.4369 0 1.6667 1 1.6330 0 1 1 1.9907 1.6667 1 1.6667 0 1.6330 1 0 1 1.6667 1 1 1.9907 1 1.6330 0 1 0 1 1 1.6667 1 1 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 728](<2010-arkus-deriving-finite-sphere-packings_images/imageFile728.png>)

![image 729](<2010-arkus-deriving-finite-sphere-packings_images/imageFile729.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.50082R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.4913 −0.6653 0 0 0 −0.9941 0.8830 −1.3608 −0.3824 −0.9345 0 0.3441 0.4636 −0.8165 0.3441 −0.7726 −0.2722 −0.5735 0 −0.8165 −0.5735 −0.5298 −0.8165 0.2294

C :

R

 

 

###### *Packing 143 (Graph 454720):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 1 1 0 0 1 0 0 1 1 0 1 1 0 1 1 0 1 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 0 1 0 1 1 0

A :

 

 





- 0 1.4142 1.6330 1 1.7321 1 1 1 1 0 1.4142 0 1.4142 1.7321 1 1.7321 1 1 1 0 1.6330 1.4142 0 1.9149 2.3805 1 1.9149 1.9149 1 0
- 1 1.7321 1.9149 0 2.0000 1.4142 1.7321 1 1.7321 0


1.7321 1 2.3805 2.0000 0 2.4495 1 1 1.7321 0 1 1.7321 1 1.4142 2.4495 0 1.7321 1.7321 1 0 1 1 1.9149 1.7321 1 1.7321 0 1 1 0 1 1 1.9149 1 1 1.7321 1 0 1.4142 0 1 1 1 1.7321 1.7321 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 730](<2010-arkus-deriving-finite-sphere-packings_images/imageFile730.png>)

![image 731](<2010-arkus-deriving-finite-sphere-packings_images/imageFile731.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.03333R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.4142 0 1.3333 −0.9428 0 0 0 −1.0000 −1.0000 −1.4142 −0.0000 1.0000 0 0 −0.5000 −0.7071 0.5000 −0.5000 −0.7071 −0.5000 0.5000 −0.7071 0.5000 0.5000 −0.7071 −0.5000

C :

R

 

 

Packing 144 (Graph 456547):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1.7249 1 1.6667 1.1529 1 0 1.0887 0 1.6330 1.6217 1 1.6667 1 1 1 0 1.6330 1.6330 0 1.8132 1.6667 1 1 1.9907 1 0
- 1 1.6217 1.8132 0 1.6753 1.2300 1.9894 1 1.7083 0 1.7249 1 1.6667 1.6753 0 1.9907 1 1 1.6330 0


D :

R

1 1.6667 1 1.2300 1.9907 0 1.6330 1.7778 1 0 1.6667 1 1 1.9894 1 1.6330 0 1.6330 1 0 1.1529 1 1.9907 1 1 1.7778 1.6330 0 1.6667 0

 

 

1 1 1 1.7083 1.6330 1 1 1.6667 0 0 0 0 0 0 0 0 0 0 0 0

![image 732](<2010-arkus-deriving-finite-sphere-packings_images/imageFile732.png>)

![image 733](<2010-arkus-deriving-finite-sphere-packings_images/imageFile733.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.21339R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.0887 0 −1.5396 0.5443 0 −0.1954 −0.2043 −0.9592 −0.4170 1.4515 −0.8333 −0.9623 −0.2722 0 −0.9623 1.3608 0 0.2352 0.6955 −0.8889 −0.6736 0.5443 0.5000 −0.6736 0.5443 −0.5000

C :

R

 

 

Packing 145 (Graph 457749):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 0 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.4142 1.6330 1 1.7321 1 1.9149 1 1 0 1.4142 0 1.4142 1.7321 1 1.7321 1 1 1 0 1.6330 1.4142 0 1.9149 1.7321 1 1 1.9149 1 0
- 1 1.7321 1.9149 0 1.4142 1.4142 1.9149 1 1.7321 0 1.7321 1 1.7321 1.4142 0 2.0000 1 1 1.7321 0


D :

R

1 1.7321 1 1.4142 2.0000 0 1.7321 1.7321 1 0

1.9149 1 1 1.9149 1 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1 1 1.7321 1.7321 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 734](<2010-arkus-deriving-finite-sphere-packings_images/imageFile734.png>)

![image 735](<2010-arkus-deriving-finite-sphere-packings_images/imageFile735.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.40000R2|C1v|1<br><br>|non-rigid|






0 0 0 0 −1.4141 0 −1.3335

- −0.9426 0

−0.0002 0 −1.0000 −0.0002 −1.4142

- −1.0000 −1.0000


C :

R

0 −0.0000 −0.8334 −1.6498 −0.4998 0.4999 −0.7070 −0.5002 −0.5001 −0.7070 0.5000 −0.5001 −0.7070 −0.5000

 

 

Packing 146 (Graph 457823):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.1832 1.6330 1 1.6667 1 1.6667 1 1 0 1.1832 0 1.6796 1.7496 1 1.7496 1 1 1 0 1.6330 1.6796 0 1.8362 1.6938 1 1 1.9667 1 0
- 1 1.7496 1.8362 0 1.6330 1.2689 1.9838 1 1.7167 0 1.6667 1 1.6938 1.6330 0 1.9838 1 1 1.5920 0


D :

R

1 1.7496 1 1.2689 1.9838 0 1.6330 1.7167 1 0

1.6667 1 1 1.9838 1 1.6330 0 1.5920 1 0 1 1 1.9667 1 1 1.7167 1.5920 0 1.5345 0 1 1 1 1.7167 1.5920 1 1 1.5345 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 736](<2010-arkus-deriving-finite-sphere-packings_images/imageFile736.png>)

![image 737](<2010-arkus-deriving-finite-sphere-packings_images/imageFile737.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.20770R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.1832 0 1.5458 0.5264 0 0.1906 −0.2794 0.9411 0.3758 1.3429 0.9128 0.9577 −0.2794 −0.0697 0.9803 1.3429 0.1162 −0.2665 0.5916 0.7609 0.6611 0.5916 −0.4615 0.7000 0.4773 0.5312

C :

R

 

 

Packing 147 (Graph 457894):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6796 1.6330 1 1.6938 1 1.9667 1 1 0 1.6796 0 1.1832 1.7496 1 1.7496 1 1 1 0 1.6330 1.1832 0 1.9907 1.6667 1 1 1.6667 1 0
- 1 1.7496 1.9907 0 1.1739 1.6667 1.8019 1 1.6330 0 1.6938 1 1.6667 1.1739 0 1.9838 1 1 1.5920 0


D :

R

1 1.7496 1 1.6667 1.9838 0 1.7167 1.6330 1 0

1.9667 1 1 1.8019 1 1.7167 0 1.5920 1.5345 0 1 1 1.6667 1 1 1.6330 1.5920 0 1 0 1 1 1 1.6330 1.5920 1 1.5345 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 738](<2010-arkus-deriving-finite-sphere-packings_images/imageFile738.png>)

![image 739](<2010-arkus-deriving-finite-sphere-packings_images/imageFile739.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.15785R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6796 0 −1.0890 1.2169 0 0.3888 0.2262 0.8931 0.2939 1.3962 0.9128 −0.9716 0.2262 −0.0697 −0.6487 1.6935 0.7609 0.5303 0.8398 0.1162 −0.2860 0.8398 −0.4615 −0.3760 0.7592 0.5312

C :

R

 

 

Packing 148 (Graph 458045):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 1 0 1 0 1 0 1 1 0 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6796 1.6330 1 1.6938 1 1.9667 1 1 0 1.6796 0 1.1832 1.6156 1 1.7496 1 1 1 0 1.6330 1.1832 0 1.9907 1.6667 1 1 1.6667 1 0
- 1 1.6156 1.9907 0 1.9838 1.6667 2.3462 1 1 0 1.6938 1 1.6667 1.9838 0 1.9838 1 1 1.5920 0 1 1.7496 1 1.6667 1.9838 0 1.7167 1.6330 1 0


D :

R

1.9667 1 1 2.3462 1 1.7167 0 1.5920 1.5345 0 1 1 1.6667 1 1 1.6330 1.5920 0 1 0 1 1 1 1 1.5920 1 1.5345 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 740](<2010-arkus-deriving-finite-sphere-packings_images/imageFile740.png>)

![image 741](<2010-arkus-deriving-finite-sphere-packings_images/imageFile741.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.59425R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6796 0 −1.0890 −1.2169 0 0.5389 −0.3605 0.7614 0.2939 −1.3962 −0.9128 −0.9716 −0.2262 0 −0.6487 −1.6935 −0.7609 0.5303 −0.8398 −0.1162 −0.2860 −0.8398 0.4615 −0.3760 −0.7592 −0.5312

C :

R

 

 

Packing 149 (Graph 458120):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 0 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 1 1 0 0 1 1 0 1 1 0 1 0 1 1 1 1 1 0

A :

 

 





0 1.7321 1.4142 1 1.7321 1 1.7321 1 1 0

- 1.7321 0 1.7321 1.4142 1 2.2361 1 1 1 0 1.4142 1.7321 0 1.9149 1.7321 1 1 1.7321 1 0

1 1.4142 1.9149 0 1.9149 1.9149 1.9149 1 1 0

- 1.7321 1 1.7321 1.9149 0 2.0000 1 1 1.4142 0 1 2.2361 1 1.9149 2.0000 0 1.7321 1.7321 1.4142 0


D :

R

1.7321 1 1 1.9149 1 1.7321 0 1.4142 1 0 1 1 1.7321 1 1 1.7321 1.4142 0 1 0 1 1 1 1 1.4142 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 742](<2010-arkus-deriving-finite-sphere-packings_images/imageFile742.png>)

![image 743](<2010-arkus-deriving-finite-sphere-packings_images/imageFile743.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.63333R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.7321 0 1.2910 −0.5774 0 −0.5164

- −0.5774 −0.6325

0.1291 −1.4434 0.9487 0.9037 0.2887 0.3162 0.9037

- −1.4434 0.3162


C :

R

−0.3873 −0.8660 0.3162 0.3873 −0.8660 −0.3162 0.5164 −0.5774 0.6325

 

 

Packing 150 (Graph 458161):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 1 1 0 1 1 0 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 1.7321 1 1.7321 1 1 0 1.7321 0 1.6330 1.9149 1 1.9149 1 1 1 0 1.7321 1.6330 0 2.3333 1.9149 1 1 1.9149 1 0
- 1 1.9149 2.3333 0 1.4142 1.6667 1.9149 1 1.6330 0 1.7321 1 1.9149 1.4142 0 1.9149 1 1 1.4142 0


D :

R

1 1.9149 1 1.6667 1.9149 0 1.4142 1.6330 1 0

1.7321 1 1 1.9149 1 1.4142 0 1.4142 1 0 1 1 1.9149 1 1 1.6330 1.4142 0 1 0 1 1 1 1.6330 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 744](<2010-arkus-deriving-finite-sphere-packings_images/imageFile744.png>)

![image 745](<2010-arkus-deriving-finite-sphere-packings_images/imageFile745.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.62222R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7321 0 −1.4402 −0.9623 0 0.5658 −0.0962 −0.8189 0.1543 −1.4434 −0.9449 −0.9773 −0.0962 −0.1890 −0.7715 −1.4434 −0.5669 0.4629 −0.8660 −0.1890 −0.4629 −0.8660 0.1890 −0.3086 −0.5774 −0.7559

C :

R

 

 

Packing 151 (Graph 458198):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6330 1 1.9770 1 1.6667 1 1 0 1.6859 0 1.6859 1.9868 1 1.9868 1 1 1.6059 0 1.6330 1.6859 0 1.9907 1.9770 1 1 1.6667 1 0
- 1 1.9868 1.9907 0 1.7384 1.6667 1.7249 1 1 0 1.9770 1 1.9770 1.7384 0 2.3778 1 1 1.5789 0 1 1.9868 1 1.6667 2.3778 0 1.6330 1.6330 1 0


D :

R

1.6667 1 1 1.7249 1 1.6330 0 1.0887 1 0 1 1 1.6667 1 1 1.6330 1.0887 0 1 0 1 1.6059 1 1 1.5789 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 746](<2010-arkus-deriving-finite-sphere-packings_images/imageFile746.png>)

![image 747](<2010-arkus-deriving-finite-sphere-packings_images/imageFile747.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.88464R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6859 0 −1.4287 −0.7909 0 0 0 −0.9958 0 −1.7056 −0.9997 −0.9505 0 0.3090 −0.7969 −1.3702 −0.5151 0.1555 −0.8429 −0.5151 −0.7259 −0.3746 −0.5769 −0.4666 −0.8429 0.2678

C :

R

 

 

Packing 152 (Graph 459996):





0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 0 1 0 0 1 1 0 1 1 0 1 1 1 1 0 0 1 1 1 1 0 1 1 1 0 0

A :

 

 





- 0 1.6779 1.6779 1 2.4520 1 1.9843 1 1.6532 0 1.6779 0 1.6180 1.1220 1 1.6180 1 1 1 0 1.6779 1.6180 0 1.9889 1.6779 1 1 1.6180 1 0
- 1 1.1220 1.9889 0 2.1063 1.6330 1.7566 1 1.7007 0 2.4520 1 1.6779 2.1063 0 1.9843 1 1.6779 1 0


D :

R

1 1.6180 1 1.6330 1.9843 0 1.6180 1 1 0 1.9843 1 1 1.7566 1 1.6180 0 1.6180 1 0

1 1 1.6180 1 1.6779 1 1.6180 0 1 0 1.6532 1 1 1.7007 1 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 748](<2010-arkus-deriving-finite-sphere-packings_images/imageFile748.png>)

![image 749](<2010-arkus-deriving-finite-sphere-packings_images/imageFile749.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.71068R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0

- −1.6779 0

1.4175 −0.8978 0 −0.5319 −0.7618 0.3697 0.6434

- −2.3326 −0.3969


C :

R

0.7671 −0.3568 −0.5331 0.9435 −1.7143 0.3295 −0.1090 −0.8390 −0.5331 0.7459 −1.3554 −0.5827 0.4617 −0.8390 0.2880

 

 

###### *Packing 153 (Graph 460165):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 0 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.4142 1.4142 1 1.9149 1 1.7321 1 1 0 1.4142 0 1.6330 1.7321 1 1.9149 1 1.9149 1 0 1.4142 1.6330 0 1.7321 1.6667 1 1 1 1 0
- 1 1.7321 1.7321 0 1.7321 1.7321 2.0000 1 1.7321 0 1.9149 1 1.6667 1.7321 0 2.3333 1 1.9437 1.6330 0


D :

R

1 1.9149 1 1.7321 2.3333 0 1.7321 1 1 0

1.7321 1 1 2.0000 1 1.7321 0 1.7321 1 0 1 1.9149 1 1 1.9437 1 1.7321 0 1.4142 0 1 1 1 1.7321 1.6330 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 750](<2010-arkus-deriving-finite-sphere-packings_images/imageFile750.png>)

![image 751](<2010-arkus-deriving-finite-sphere-packings_images/imageFile751.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.83333R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.4142 0 −1.3333 −0.4714 0 0 0 −1.0000 −0.5000 −1.6499 −0.8333

C :

R

- −0.8333 0.2357 0.5000
- −1.0000 −1.4142


0 −0.8333 0.2357 −0.5000 −0.5000 −0.7071 0.5000 −0.5000 −0.7071 −0.5000

 

 

Packing 154 (Graph 460203):





0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 0 1 1 0 1 1 1 0 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7778 1.6330 1 2.5035 1 1.9907 1 1.6667 0 1.7778 0 1.6330 1.8178 1 1.6667 1 1.9907 1 0 1.6330 1.6330 0 1.6667 1.6667 1 1 1 1 0
- 1 1.8178 1.6667 0 2.5727 1.6330 1.7778 1 1.9907 0 2.5035 1 1.6667 2.5727 0 1.9907 1 2.4369 1 0


D :

R

1 1.6667 1 1.6330 1.9907 0 1.6330 1 1 0 1.9907 1 1 1.7778 1 1.6330 0 1.6667 1 0

1 1.9907 1 1 2.4369 1 1.6667 0 1.6330 0 1.6667 1 1 1.9907 1 1 1 1.6330 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 752](<2010-arkus-deriving-finite-sphere-packings_images/imageFile752.png>)

![image 753](<2010-arkus-deriving-finite-sphere-packings_images/imageFile753.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.81907R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7778 0 1.3699 −0.8889 0 0.1682 −0.2407 0.9559 0.7090 −2.3704 −0.3824 0.7210 −0.3889 −0.5735 0.9373 −1.7222 0.3441 0.9373 −0.0556 0.3441 0.7210 −1.3889 −0.5735 0.3965 −0.8889 0.2294

C :

R

 

 

Packing 155 (Graph 460314):





0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 0 1 1 0 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7778 1.6330 1 2.5035 1 1.9907 1 1.6667 0 1.7778 0 1.6330 1.1529 1 1.9907 1 1.6667 1 0 1.6330 1.6330 0 1.6667 1.6667 1 1 1 1 0
- 1 1.1529 1.6667 0 1.8239 1.6330 1.7249 1 1.0887 0 2.5035 1 1.6667 1.8239 0 2.4369 1 1.9907 1 0


D :

R

1 1.9907 1 1.6330 2.4369 0 1.6667 1 1.6330 0 1.9907 1 1 1.7249 1 1.6667 0 1.6330 1 0

1 1.6667 1 1 1.9907 1 1.6330 0 1 0 1.6667 1 1 1.0887 1 1.6330 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 754](<2010-arkus-deriving-finite-sphere-packings_images/imageFile754.png>)

![image 755](<2010-arkus-deriving-finite-sphere-packings_images/imageFile755.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.99602R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.7778 0

- −1.3699 −0.8889

0 0.1923 −0.7963 −0.5735 −0.7090

- −2.3704 −0.3824 −0.9373 −0.0556


C :

R

0.3441 −0.9373 −1.7222 0.3441 −0.7210 −0.3889 −0.5735 −0.7210 −1.3889 −0.5735 −0.3965 −0.8889 0.2294

 

 

###### *Packing 156 (Graph 460524):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 0 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 0 1 1 1 1 0 0 1 1 0 1 1 1 1 0 1 1 1 0 1 0

A :

 

 





- 0 1.4142 1.4142 1 1.9149 1 1.7321 1 1 0 1.4142 0 1.6330 1.7321 1 1.9149 1 1.9149 1 0 1.4142 1.6330 0 1.7321 1.6667 1 1 1 1 0
- 1 1.7321 1.7321 0 2.5166 1.7321 2.0000 1 1 0 1.9149 1 1.6667 2.5166 0 1.9437 1 2.3333 1.6330 0 1 1.9149 1 1.7321 1.9437 0 1.7321 1 1.4142 0


D :

R

1.7321 1 1 2.0000 1 1.7321 0 1.7321 1 0 1 1.9149 1 1 2.3333 1 1.7321 0 1 0 1 1 1 1 1.6330 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 756](<2010-arkus-deriving-finite-sphere-packings_images/imageFile756.png>)

![image 757](<2010-arkus-deriving-finite-sphere-packings_images/imageFile757.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.16667R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.4142 0 1.3333 −0.4714 0 −0.0000 0 −1.0000 0.5000 −1.6499 0.8333 0.8333 0.2357 0.5000 1.0000 −1.4142 −0.0000 0.8333 0.2357 −0.5000 0.5000 −0.7071 −0.5000 0.5000 −0.7071 0.5000

C :

R

 

 

###### *Packing 157 (Graph 460588):





0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 0 0 1 1 1 1 0 1 1 0 1 1 1 1 1 0 1 1 0 1 0

A :

 

 





- 0 1.7566 1.6180 1 2.4686 1 1.9843 1 1.6180 0 1.7566 0 1.6330 1.1220 1 1.9889 1 1.7007 1 0 1.6180 1.6330 0 1.6180 1.6667 1 1 1 1 0
- 1 1.1220 1.6180 0 1.7463 1.6180 1.6779 1 1 0 2.4686 1 1.6667 1.7463 0 2.4344 1 1.9945 1 0


D :

R

1 1.9889 1 1.6180 2.4344 0 1.6779 1 1.6180 0 1.9843 1 1 1.6779 1 1.6779 0 1.6532 1 0

1 1.7007 1 1 1.9945 1 1.6532 0 1 0 1.6180 1 1 1 1 1.6180 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 758](<2010-arkus-deriving-finite-sphere-packings_images/imageFile758.png>)

![image 759](<2010-arkus-deriving-finite-sphere-packings_images/imageFile759.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.88489R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.7566 0 1.3678 −0.8645 0 −0.1430 −0.8046 −0.5764 0.6978 −2.3283 −0.4315 0.9337 −0.0370 0.3562 0.9473 −1.7144 0.3175 0.7424 −0.3397 −0.5775 0.7024 −1.3389 −0.5764 0.4019 −0.8783 0.2589

C :

R

 

 

Packing 158 (Graph 462814):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 0 0 0 1 0 1 1 0 1 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 1 1 0 1 1 0 0 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.4142 1 1.7321 1 1.7321 1 1 0 1.7321 0 1.7321 1.9149 1 2.2361 1 1 1 0 1.4142 1.7321 0 1.9149 1.7321 1 1 1 1.7321 0
- 1 1.9149 1.9149 0 1.4142 1.4142 1.9149 1.6330 1 0 1.7321 1 1.7321 1.4142 0 2.0000 1 1.4142 1 0


D :

R

- 1 2.2361 1 1.4142 2.0000 0 1.7321 1.4142 1.7321 0


1.7321 1 1 1.9149 1 1.7321 0 1 1.4142 0 1 1 1 1.6330 1.4142 1.4142 1 0 1 0 1 1 1.7321 1 1 1.7321 1.4142 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 760](<2010-arkus-deriving-finite-sphere-packings_images/imageFile760.png>)

![image 761](<2010-arkus-deriving-finite-sphere-packings_images/imageFile761.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.46667R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7321 0 −1.2910 −0.5774 0 0.3012 −0.0962 −0.9487 −0.1291 −1.4434 −0.9487 −0.9037 0.2887 −0.3162 −0.9037 −1.4434 −0.3162 −0.3873 −0.8660 0.3162 0.3873 −0.8660 −0.3162 −0.5164 −0.5774 −0.6325

C :

R

 

 

Packing 159 (Graph 463479):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 0 0 1 0 1 1 1 0 1 0 0 1 1 1 0 0 1 1 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.6779 1.6180 1 1.9889 1 1.6180 1 1 0 1.6779 0 1.6779 1.1220 1 1.9843 1 1 1.6532 0 1.6180 1.6779 0 1.9843 1.1220 1 1 1.6180 1 0
- 1 1.1220 1.9843 0 1.7463 1.6779 1.6779 1 1.6532 0 1.9889 1 1.1220 1.7463 0 1.7566 1 1.6330 1.7007 0


D :

R

1 1.9843 1 1.6779 1.7566 0 1.6180 1.6180 1 0

1.6180 1 1 1.6779 1 1.6180 0 1 1 0 1 1 1.6180 1 1.6330 1.6180 1 0 1 0 1 1.6532 1 1.6532 1.7007 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 762](<2010-arkus-deriving-finite-sphere-packings_images/imageFile762.png>)

![image 763](<2010-arkus-deriving-finite-sphere-packings_images/imageFile763.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.09666R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6779 0 −1.4175 −0.7801 0 0.5319 −0.7618 −0.3697 −0.9282 −1.7197 −0.3697 −0.9435 0 −0.3295 −0.7671 −1.3211 0.5331 0.1090 −0.8390 0.5331 −0.7459 −0.3226 0.5827 −0.4617 −0.8390 −0.2880

C :

R

 

 

###### *Packing 160 (Graph 463835):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 0 0 1 0 1 1 1 0 1 1 0 1 1 1 0 0 1 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.6779 1.6180 1 1.9889 1 1.6180 1 1 0 1.6779 0 1.6779 1.9938 1 1.9843 1 1 1.6532 0 1.6180 1.6779 0 1.9843 1.1220 1 1 1.6180 1 0
- 1 1.9938 1.9843 0 2.4527 1.6779 1.6779 1 1 0 1.9889 1 1.1220 2.4527 0 1.7566 1 1.6330 1.7007 0 1 1.9843 1 1.6779 1.7566 0 1.6180 1.6180 1 0


D :

R

1.6180 1 1 1.6779 1 1.6180 0 1 1 0 1 1 1.6180 1 1.6330 1.6180 1 0 1 0 1 1.6532 1 1 1.7007 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 764](<2010-arkus-deriving-finite-sphere-packings_images/imageFile764.png>)

![image 765](<2010-arkus-deriving-finite-sphere-packings_images/imageFile765.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.66493R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6779 0 1.4175 −0.7801 0

- −0.0865 0

−0.9951 0.9282 −1.7197 0.3697 0.9435 0 0.3295 0.7671

- −1.3211 −0.5331 −0.1090 −0.8390 −0.5331


C :

R

0.7459 −0.3226 −0.5827 0.4617 −0.8390 0.2880

 

 

Packing 161 (Graph 464807):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 1 0 1 0 1 1 1 0 0 1 0 1 1 1 0 1 1 0 1 0 1 0 0 1 1 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.7566 1.6180 1 1.8432 1 1.9843 1.6180 1 0 1.7566 0 1.6330 1.1220 1 1.9889 1 1 1.7007 0 1.6180 1.6330 0 1.6180 1.6667 1 1 1 1 0
- 1 1.1220 1.6180 0 1.7463 1.6180 1.6779 1 1 0 1.8432 1 1.6667 1.7463 0 1.7971 1 1.6330 2.0381 0


D :

R

1 1.9889 1 1.6180 1.7971 0 1.6779 1.6180 1 0 1.9843 1 1 1.6779 1 1.6779 0 1 1.6532 0 1.6180 1 1 1 1.6330 1.6180 1 0 1 0

 

 

1 1.7007 1 1 2.0381 1 1.6532 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 766](<2010-arkus-deriving-finite-sphere-packings_images/imageFile766.png>)

![image 767](<2010-arkus-deriving-finite-sphere-packings_images/imageFile767.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.36314R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.7566 0 −1.3678 0.8645 0 0.1430 0.8046 −0.5764 −0.1972 1.5607 0.9606 −0.9337 0 0.3562 −0.9473 1.7144 0.3175 −0.7024 1.3389 −0.5764 −0.7424 0.3397 −0.5775 −0.4019 0.8783 0.2589

C :

R

 

 

Packing 162 (Graph 466085):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 0 1 0 1 1 0 1 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.9956 1.6330 1 2.4634 1 1.6667 1.6859 1 0 1.9956 0 1.1471 1.6667 1 1.7622 1 1 1.6859 0 1.6330 1.1471 0 1.6667 1.7622 1 1 1.6859 1 0
- 1 1.6667 1.6667 0 1.7249 1.6330 1.0887 1 1 0 2.4634 1 1.7622 1.7249 0 2.4792 1 1 1.9868 0


D :

R

1 1.7622 1 1.6330 2.4792 0 1.6330 1.9868 1 0 1.6667 1 1 1.0887 1 1.6330 0 1 1 0 1.6859 1 1.6859 1 1 1.9868 1 0 1.6059 0

 

 

1 1.6859 1 1 1.9868 1 1 1.6059 0 0 0 0 0 0 0 0 0 0 0 0

![image 768](<2010-arkus-deriving-finite-sphere-packings_images/imageFile768.png>)

![image 769](<2010-arkus-deriving-finite-sphere-packings_images/imageFile769.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.98837R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.9956 0

- −0.9386
- −1.3363 0

0.3129 −0.5524 0.7726 0.2294

- −2.2676 0.9345


C :

R

−0.7509 −0.4703

- −0.4636 −0.3129 −1.4432

0.7726 0.6571

- −1.4593 0.5298


−0.6571 −0.5363 0.5298 0 −0.9978 −0.0662

 

 

Packing 163 (Graph 466132):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 0 1 0 1 1 0 1 0 0 1 1 1 0 1 0 1 1 0 1 0 1 1 1 0 1 1 0 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.9907 1.0887 1 2.4369 1 1.6667 1.6330 1 0 1.9907 0 1.6667 1.6667 1 1.8113 1 1 1.6330 0 1.0887 1.6667 0 1.6667 1.9907 1 1 1.6330 1 0
- 1 1.6667 1.6667 0 1.9907 1.6859 1.6330 1 1 0 2.4369 1 1.9907 1.9907 0 2.5259 1 1 1.6667 0


D :

R

1 1.8113 1 1.6859 2.5259 0 1.6859 1.9868 1.6059 0 1.6667 1 1 1.6330 1 1.6859 0 1 1 0 1.6330 1 1.6330 1 1 1.9868 1 0 1 0

 

 

1 1.6330 1 1 1.6667 1.6059 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 770](<2010-arkus-deriving-finite-sphere-packings_images/imageFile770.png>)

![image 771](<2010-arkus-deriving-finite-sphere-packings_images/imageFile771.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.21059R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.9907 0 −0.9114 −0.5954 0 0.6836 −0.5488 0.4811 −0.2734 −2.2357 0.9302 −0.3742 −0.4225 −0.8255 −0.6836 −1.4419 0.4811 0.2734 −1.4140 0.7698 −0.2734 −0.5768 0.7698 −0.0000 −0.9954 −0.0962

C :

R

 

 

Packing 164 (Graph 466155):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 0 1 0 1 1 0 1 0 1 1 1 0 1 0 0 1 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7249 1.6330 1 2.0718 1 1.6667 1.0887 1 0 1.7249 0 1.6667 1.1471 1 1.9907 1 1 1.6330 0 1.6330 1.6667 0 1.9868 1.9907 1 1 1.6330 1 0
- 1 1.1471 1.9868 0 1.7622 1.6859 1.6859 1 1.6059 0 2.0718 1 1.9907 1.7622 0 2.4369 1 1 1.6667 0


D :

R

1 1.9907 1 1.6859 2.4369 0 1.6330 1.6667 1 0 1.6667 1 1 1.6859 1 1.6330 0 1 1 0 1.0887 1 1.6330 1 1 1.6667 1 0 1 0

 

 

1 1.6330 1 1.6059 1.6667 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 772](<2010-arkus-deriving-finite-sphere-packings_images/imageFile772.png>)

![image 773](<2010-arkus-deriving-finite-sphere-packings_images/imageFile773.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.73929R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7249 0 1.4062 −0.8302 0 −0.5550 −0.7709 −0.3126 −0.0074 −1.8168 0.9957 0.9461 −0.0036 −0.3239 0.7668 −1.3778 0.5399 −0.1195 −0.9161 0.5759 0.7242 −0.3793 0.5759 0.4390 −0.8625 −0.2519

C :

R

 

 

Packing 165 (Graph 466323):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 0 0 1 1 0 1 0 0 1 1 1 0 1 0 1 1 0 1 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 1 1 0 0 1 1 1 0

A :

 

 





- 0 1.9907 1.0887 1 2.4369 1 1.6667 1.6330 1 0 1.9907 0 1.6667 1.6667 1 2.4315 1 1 1.6330 0 1.0887 1.6667 0 1.6667 1.9907 1 1 1.6330 1 0
- 1 1.6667 1.6667 0 1.9907 1.6859 1.6330 1 1 0 2.4369 1 1.9907 1.9907 0 2.5604 1 1 1.6667 0


D :

R

- 1 2.4315 1 1.6859 2.5604 0 1.6859 1.9868 1 0 1.6667 1 1 1.6330 1 1.6859 0 1 1 0 1.6330 1 1.6330 1 1 1.9868 1 0 1 0


 

 

1 1.6330 1 1 1.6667 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 774](<2010-arkus-deriving-finite-sphere-packings_images/imageFile774.png>)

![image 775](<2010-arkus-deriving-finite-sphere-packings_images/imageFile775.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.49129R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.9907 0 −0.9114 0.5954 0 0.6836 0.5488 −0.4811 −0.2734 2.2357 −0.9302 −0.8059 −0.2384 −0.5419 −0.6836 1.4419 −0.4811 0.2734 1.4140 −0.7698 −0.2734 0.5768 −0.7698 −0.0000 0.9954 0

C :

R

 

 

Packing 166 (Graph 466327):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 1 1 1 0 1 0 1 1 0 1 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.7249 1.6330 1 2.0718 1 1.6667 1.0887 1 0 1.7249 0 1.6667 1.9868 1 1.9907 1 1 1.6330 0 1.6330 1.6667 0 1.9868 1.9907 1 1 1.6330 1 0
- 1 1.9868 1.9868 0 1.8113 1.6859 1.6859 1 1 0 2.0718 1 1.9907 1.8113 0 2.4369 1 1 1.6667 0


D :

R

1 1.9907 1 1.6859 2.4369 0 1.6330 1.6667 1 0 1.6667 1 1 1.6859 1 1.6330 0 1 1 0 1.0887 1 1.6330 1 1 1.6667 1 0 1 0

 

 

1 1.6330 1 1 1.6667 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 776](<2010-arkus-deriving-finite-sphere-packings_images/imageFile776.png>)

![image 777](<2010-arkus-deriving-finite-sphere-packings_images/imageFile777.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.01999R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7249 0 −1.4062 −0.8302 0 0.1046 −0.0081 −0.9945 0 −1.8168 −0.9957 −0.9461 −0.0036 0.3239 −0.7668 −1.3778 −0.5399 0.1195 −0.9161 −0.5759 −0.7242 −0.3793 −0.5759 −0.4390 −0.8625 0.2519

C :

R

 

 

Packing 167 (Graph 466457):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 1 0 0 0 1 1 0 1 1 1 1 0 1 1 0 0 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 1.7321 1 1.7321 1 1 0 1.7321 0 1.9149 1.9149 1 1.9149 1 1 1 0 1.7321 1.9149 0 1.9437 1.6330 1 1 1.4142 1.9149 0
- 1 1.9149 1.9437 0 1.4142 1.6667 1.9149 1.6330 1 0 1.7321 1 1.6330 1.4142 0 1.9149 1 1.4142 1 0


D :

R

1 1.9149 1 1.6667 1.9149 0 1.4142 1 1.6330 0

1.7321 1 1 1.9149 1 1.4142 0 1 1.4142 0 1 1 1.4142 1.6330 1.4142 1 1 0 1 0 1 1 1.9149 1 1 1.6330 1.4142 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 778](<2010-arkus-deriving-finite-sphere-packings_images/imageFile778.png>)

![image 779](<2010-arkus-deriving-finite-sphere-packings_images/imageFile779.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.45556R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.7321 0 1.5957 −0.6736 0 0 −0.0962 −0.9949 0.4352 −1.4434 −0.8528 0.8994 −0.0962 0.4264 0.9574 −1.4434 0 0.2611 −0.8660 0.4264 −0.2611 −0.8660 −0.4264 0.6963 −0.5774 −0.4264

C :

R

 

 

###### *Packing 168 (Graph 466903):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 0 0 1 1 0 1 1 1 1 0 1 1 0 0 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6330 1 1.9770 1 1.6667 1 1 0 1.6859 0 1.6859 1.1471 1 1.9868 1 1.6059 1 0 1.6330 1.6859 0 1.9907 1.9770 1 1 1 1.6667 0
- 1 1.1471 1.9907 0 1.7791 1.6667 1.7249 1.6330 1 0 1.9770 1 1.9770 1.7791 0 2.3778 1 1.5789 1 0


D :

R

1 1.9868 1 1.6667 2.3778 0 1.6330 1 1.6330 0

1.6667 1 1 1.7249 1 1.6330 0 1 1.0887 0 1 1.6059 1 1.6330 1.5789 1 1 0 1 0 1 1 1.6667 1 1 1.6330 1.0887 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 780](<2010-arkus-deriving-finite-sphere-packings_images/imageFile780.png>)

![image 781](<2010-arkus-deriving-finite-sphere-packings_images/imageFile781.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.63580R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6859 0 1.4287 0.7909 0 −0.5185 0.7493 −0.4120 −0.0109 1.7056 0.9997 0.9505 −0.0312 −0.3090 0.7969 1.3702 0.5151 0.7259 0.3746 0.5769 −0.1555 0.8429 0.5151 0.4666 0.8429 −0.2678

C :

R

 

 

Packing 169 (Graph 466969):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 0 0 1 1 0 1 0 0 1 1 1 1 0 1 0 0 1 1 0 0 1 1 1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 0

A :

 

 





- 0 1.6779 1.6180 1 1.9889 1 1.6180 1 1 0 1.6779 0 1.6779 1.1220 1 1.9843 1 1.6532 1 0 1.6180 1.6779 0 1.9843 1.9889 1 1 1 1 0
- 1 1.1220 1.9843 0 1.7463 1.6779 1.6779 1.6532 1 0 1.9889 1 1.9889 1.7463 0 2.4047 1 1.6482 1.6330 0 1 1.9843 1 1.6779 2.4047 0 1.6180 1 1 0


D :

R

1.6180 1 1 1.6779 1 1.6180 0 1 1 0 1 1.6532 1 1.6532 1.6482 1 1 0 1.0515 0 1 1 1 1 1.6330 1 1 1.0515 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 782](<2010-arkus-deriving-finite-sphere-packings_images/imageFile782.png>)

![image 783](<2010-arkus-deriving-finite-sphere-packings_images/imageFile783.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.61841R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6779 0 −1.4175 0.7801 0 0.5319 0.7618 0.3697 0 1.7197 −0.9989 −0.9435 −0.0364 0.3295 −0.7671 1.3211 −0.5331 −0.7459 0.3226 −0.5827 −0.4617 0.8390 0.2880 0.1090 0.8390 −0.5331

C :

R

 

 

Packing 170 (Graph 467170):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 0 1 0 1 1 0 0 1 1 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7778 1.6330 1 1.8178 1 1.9907 1.6667 1 0 1.7778 0 1.6330 1.8178 1 1.6667 1 1 1.9907 0 1.6330 1.6330 0 1.6667 1.6667 1 1 1 1 0
- 1 1.8178 1.6667 0 1.2963 1.6330 1.7778 1.9907 1 0 1.8178 1 1.6667 1.2963 0 1.9907 1 1.6330 1.7778 0


D :

R

1 1.6667 1 1.6330 1.9907 0 1.6330 1 1 0 1.9907 1 1 1.7778 1 1.6330 0 1 1.6667 0 1.6667 1 1 1.9907 1.6330 1 1 0 1.6330 0

 

 

1 1.9907 1 1 1.7778 1 1.6667 1.6330 0 0 0 0 0 0 0 0 0 0 0 0

![image 784](<2010-arkus-deriving-finite-sphere-packings_images/imageFile784.png>)

![image 785](<2010-arkus-deriving-finite-sphere-packings_images/imageFile785.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.75117R2<br><br>|Cs|1| |






0 0 0 0 −1.7778 0 1.3699 −0.8889 0 0.1682 −0.2407 −0.9559 0.1682 −1.5370 −0.9559 0.7210 −0.3889 0.5735 0.9373 −1.7222 −0.3441 0.7210 −1.3889 0.5735 0.9373 −0.0556 −0.3441 0.3965 −0.8889 −0.2294

C :

R

 

 

Packing 171 (Graph 467260):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 0 1 0 1 1 0 0 1 1 0 1 0 1 1 0 1 0 1 0 1 0 1 1 1 1 1 1 1 1 0 1 0

A :

 

 





- 0 1.6779 1.6779 1 1.8155 1 1.9843 1.6532 1 0 1.6779 0 1.6180 1.1220 1 1.6180 1 1 1 0 1.6779 1.6180 0 1.9889 1.6779 1 1 1 1.6180 0
- 1 1.1220 1.9889 0 1.2125 1.6330 1.7566 1.7007 1 0 1.8155 1 1.6779 1.2125 0 1.9843 1 1.6532 1.6779 0


D :

R

1 1.6180 1 1.6330 1.9843 0 1.6180 1 1 0 1.9843 1 1 1.7566 1 1.6180 0 1 1.6180 0 1.6532 1 1 1.7007 1.6532 1 1 0 1 0

 

 

1 1 1.6180 1 1.6779 1 1.6180 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 786](<2010-arkus-deriving-finite-sphere-packings_images/imageFile786.png>)

![image 787](<2010-arkus-deriving-finite-sphere-packings_images/imageFile787.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.14241R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6779 0 1.4175 −0.8978 0 −0.5319 −0.7618 −0.3697 0.1979 −1.5231 −0.9679 0.7671 −0.3568 0.5331 0.9435 −1.7143 −0.3295 0.7459 −1.3554 0.5827 −0.1090 −0.8390 0.5331 0.4617 −0.8390 −0.2880

C :

R

 

 

Packing 172 (Graph 472149):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 0 0 1 1 0 1 0 0 1 1 1 1 1 1 0 0 1 1 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 0

A :

 

 





- 0 1.6779 1.6180 1 1.9889 1 1.6180 1 1 0 1.6779 0 1.6779 1.9938 1 1.9843 1 1 1.6532 0 1.6180 1.6779 0 1.9843 1.9889 1 1 1 1 0
- 1 1.9938 1.9843 0 1.7685 1.6779 1.6779 1.6532 1 0 1.9889 1 1.9889 1.7685 0 2.4047 1 1.6330 1.6482 0 1 1.9843 1 1.6779 2.4047 0 1.6180 1 1 0


D :

R

1.6180 1 1 1.6779 1 1.6180 0 1 1 0 1 1 1 1.6532 1.6330 1 1 0 1.0515 0 1 1.6532 1 1 1.6482 1 1 1.0515 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 788](<2010-arkus-deriving-finite-sphere-packings_images/imageFile788.png>)

![image 789](<2010-arkus-deriving-finite-sphere-packings_images/imageFile789.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.89785R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6779 0 −1.4175 0.7801 0 0 −0.0476 0.9951 0 1.7197 0.9989 −0.9435 −0.0364 −0.3295 −0.7671 1.3211 0.5331 −0.4617 0.8390 −0.2880 −0.7459 0.3226 0.5827 0.1090 0.8390 0.5331

C :

R

 

 

Packing 173 (Graph 473525):





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 0 1 1 0 1 1 1 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 0 1 0 1 1 1 1 0

A :

 

 





- 0 2.0000 1.7321 1 2.5166 1 1.7321 1.7321 1 0 2.0000 0 1.7321 1.7321 1 1.7321 1 1 1.7321 0 1.7321 1.7321 0 1.9149 1.4142 1 1 1 1 0
- 1 1.7321 1.9149 0 2.3333 1.6330 1.4142 1.9149 1 0 2.5166 1 1.4142 2.3333 0 1.9149 1 1 1.9149 0


D :

R

1 1.7321 1 1.6330 1.9149 0 1.4142 1 1 0 1.7321 1 1 1.4142 1 1.4142 0 1 1 0 1.7321 1 1 1.9149 1 1 1 0 1.4142 0

 

 

1 1.7321 1 1 1.9149 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

![image 790](<2010-arkus-deriving-finite-sphere-packings_images/imageFile790.png>)

![image 791](<2010-arkus-deriving-finite-sphere-packings_images/imageFile791.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.07778R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −2.0000 0 −1.4142 −1.0000 0 0.2357 −0.5000 −0.8333 −0.9428 −2.3333 −0.0000 −0.7071 −0.5000 0.5000 −0.7071 −1.5000 −0.5000 −0.7071 −1.5000 0.5000 −0.7071 −0.5000 −0.5000 0 −1.0000 0

C :

R

 

 

###### *Packing 174 (Graph 479299):





0 0 0 1 0 1 1 1 0 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 0 1 1 0 1 1 0 1 0 0 1 0 1 1 0 1 1 1 0 0 1 1 0 1 1 1 1 0 1 1 0

A :

 

 





- 0 1.7199 1.7221 1 1.7199 1 1 1 1.5130 0 1.7199 0 1.9591 1.9591 1 1.7199 1 1 1 0 1.7221 1.9591 0 1.9657 1.5224 1 1.7204 1.8799 1 0
- 1 1.9591 1.9657 0 1.5224 1.7221 1.7204 1 1.8799 0


1.7199 1 1.5224 1.5224 0 1.7199 1.5130 1 1 0 1 1.7199 1 1.7221 1.7199 0 1 1.5130 1 0 1 1 1.7204 1.7204 1.5130 1 0 1 1 0 1 1 1.8799 1 1 1.5130 1 0 1.2892 0

D :

R

 

 

1.5130 1 1 1.8799 1 1 1 1.2892 0 0 0 0 0 0 0 0 0 0 0 0

![image 792](<2010-arkus-deriving-finite-sphere-packings_images/imageFile792.png>)

![image 793](<2010-arkus-deriving-finite-sphere-packings_images/imageFile793.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.34082R2<br><br>|Cs|1| |






0 0 0 0 1.7199 0 −1.6118 0.6064 0 −0.0184 0 −0.9992 −0.5810 1.4292 −0.7602 −0.8106 0.2907 0.5083 0 0.8600 0.5102 0.1897 0.8600 −0.4738 −0.8554 1.2347 0.1815 −0.7374 0.4852 −0.4699

C :

R

 

 

###### *Packing 175 (Graph 493558):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 1 1 0 0 1 1 1 0 0 1 0 0 1 1 1 1 1 0 0

A :

 

 





- 0 1.7199 1.7221 1 1.7199 1 1 1.5130 1 0 1.7199 0 1.5224 1.9591 1 1.7199 1 1 1 0 1.7221 1.5224 0 2.4850 1.9591 1 1.8799 1 1 0
- 1 1.9591 2.4850 0 1.5224 1.7221 1 1.8799 1.7204 0


1.7199 1 1.9591 1.5224 0 1.7199 1 1 1.5130 0 1 1.7199 1 1.7221 1.7199 0 1.5130 1 1 0 1 1 1.8799 1 1 1.5130 0 1.2892 1 0

D :

R

1.5130 1 1 1.8799 1 1 1.2892 0 1 0 1 1 1 1.7204 1.5130 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 794](<2010-arkus-deriving-finite-sphere-packings_images/imageFile794.png>)

![image 795](<2010-arkus-deriving-finite-sphere-packings_images/imageFile795.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.57195R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 −1.7199 0 −1.3662 −1.0484 0 0.8355 −0.0350 −0.5484 0.3333 −1.4292 −0.8969 −0.8623 −0.2907 −0.4147 0.5019 −0.8600 −0.0922 −0.6097 −1.2347 −0.6268 −0.4255 −0.8600 0.2818 0 −0.4852 −0.8744

C :

R

 

 

###### *Packing 176 (Graph 506514):





0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 1 0 1 0 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 0 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.7204 1.5130 1 1.8479 1 1 1 1 0 1.7204 0 1.5224 1.7221 1 1.9591 1.8799 1 1 0 1.5130 1.5224 0 1.7199 1.9623 1 1 1.7199 1 0
- 1 1.7221 1.7199 0 1.2992 1.7199 1 1 1.5130 0


1.8479 1 1.9623 1.2992 0 2.3924 1.8851 1 1.6330 0 1 1.9591 1 1.7199 2.3924 0 1 1.7199 1 0 1 1.8799 1 1 1.8851 1 0 1.5130 1.2892 0 1 1 1.7199 1 1 1.7199 1.5130 0 1 0 1 1 1 1.5130 1.6330 1 1.2892 1 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 796](<2010-arkus-deriving-finite-sphere-packings_images/imageFile796.png>)

![image 797](<2010-arkus-deriving-finite-sphere-packings_images/imageFile797.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.48256R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.7204 0 −1.2503 0.8520 0 0 0.2889 −0.9552 0.3232 1.5620 −0.9330 −0.8913 0 0.4521 −0.8311 0.1237 −0.5422 0.4538 0.8602 −0.2326 −0.3293 0.8602 0.3893 −0.4629 1.0526 −0.5828

C :

R

 

 

Packing 177 (Graph 506611):





0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 1 0 1 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 0 0 1 1 0 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6532 1.6532 1 1.6482 1 1 1 1 0 1.6532 0 1.8155 1.6779 1 1.6779 1.9843 1 1 0 1.6532 1.8155 0 1.6779 2.5231 1 1 1.9843 1.6779 0
- 1 1.6779 1.6779 0 1.9889 1.6180 1 1 1.6180 0


1.6482 1 2.5231 1.9889 0 1.9889 2.4047 1 1 0 1 1.6779 1 1.6180 1.9889 0 1 1.6180 1 0 1 1.9843 1 1 2.4047 1 0 1.6180 1.6180 0 1 1 1.9843 1 1 1.6180 1.6180 0 1 0 1 1 1.6779 1.6180 1 1 1.6180 1 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 798](<2010-arkus-deriving-finite-sphere-packings_images/imageFile798.png>)

![image 799](<2010-arkus-deriving-finite-sphere-packings_images/imageFile799.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.15375R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6532 0 1.5173 0.6563 0 0.1823 0.2775 −0.9433 −0.8841 1.3457 0.3518 0.7806 0.2775 0.5601 0.9274 −0.0619 −0.3690 −0.4249 0.8266 −0.3690 −0.0552 0.8266 0.5601 0.5640 0.8585 −0.2245

C :

R

 

 

Packing 178 (Graph 508571):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.6667 1 1.6667 1 1 0 1.6330 0 1.6330 1.6667 1 1.9907 1 1 1 0 1.0887 1.6330 0 1.7249 1.9907 1.1529 1 1.6667 1 0
- 1 1.6667 1.7249 0 1.9907 1 1.9907 1 1.6330 0 1.6667 1 1.9907 1.9907 0 2.4369 1.6667 1 1 0


D :

R

1 1.9907 1.1529 1 2.4369 0 1.7778 1.6330 1.6667 0

1.6667 1 1 1.9907 1.6667 1.7778 0 1.6330 1 0 1 1 1.6667 1 1 1.6330 1.6330 0 1 0 1 1 1 1.6330 1 1.6667 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 800](<2010-arkus-deriving-finite-sphere-packings_images/imageFile800.png>)

![image 801](<2010-arkus-deriving-finite-sphere-packings_images/imageFile801.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.71070R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.0264 0.3629 0 0.4811 0.2722 −0.8333 0.4811 1.3608 0.8333 −0.4491 −0.0907 −0.8889 −0.9623 1.3608 −0.0000 0.5774 0.8165 0 −0.2887 0.8165 0.5000 −0.2887 0.8165 −0.5000

C :

R

 

 

Packing 179 (Graph 508895):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 0 0 1 1 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 1 1 0 1 1 0 0 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.6667 1 1.6667 1 1 0 1.6330 0 1.6330 1.6667 1 1.9907 1 1 1 0 1.0887 1.6330 0 1.7249 1.9907 1.1529 1 1 1.6667 0
- 1 1.6667 1.7249 0 1.0887 1 1.9907 1.6330 1 0 1.6667 1 1.9907 1.0887 0 1.7249 1.6667 1.6330 1 0


D :

R

1 1.9907 1.1529 1 1.7249 0 1.7778 1.6667 1.6330 0

1.6667 1 1 1.9907 1.6667 1.7778 0 1 1.6330 0 1 1 1 1.6330 1.6330 1.6667 1 0 1 0 1 1 1.6667 1 1 1.6330 1.6330 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 802](<2010-arkus-deriving-finite-sphere-packings_images/imageFile802.png>)

![image 803](<2010-arkus-deriving-finite-sphere-packings_images/imageFile803.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.13663R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.0264 −0.3629 0 −0.4811 −0.2722 −0.8333 −0.4811 −1.3608 −0.8333 0.4491 0 −0.8889 0.9623 −1.3608 0 0.2887 −0.8165 0.5000 −0.5774 −0.8165 0 0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 180 (Graph 508946):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 0 0 1 1 1 0 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.6667 1 1.6667 1 1 0 1.6330 0 1.6330 1.6667 1 1.9907 1 1 1 0 1.0887 1.6330 0 1.7249 1.9907 2.0718 1 1 1.6667 0
- 1 1.6667 1.7249 0 1.0887 1 1.9907 1.6330 1 0 1.6667 1 1.9907 1.0887 0 1.7249 1.6667 1.6330 1 0


D :

R

1 1.9907 2.0718 1 1.7249 0 2.4369 1.6667 1 0

1.6667 1 1 1.9907 1.6667 2.4369 0 1 1.6330 0 1 1 1 1.6330 1.6330 1.6667 1 0 1 0 1 1 1.6667 1 1 1 1.6330 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 804](<2010-arkus-deriving-finite-sphere-packings_images/imageFile804.png>)

![image 805](<2010-arkus-deriving-finite-sphere-packings_images/imageFile805.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.71070R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.0264 0.3629 0 0.4811 0.2722 0.8333 0.4811 1.3608 0.8333 0.9943 −0.0907 0 −0.9623 1.3608 −0.0000 −0.2887 0.8165 −0.5000 0.5774 0.8165 −0.0000 −0.2887 0.8165 0.5000

C :

R

 

 

Packing 181 (Graph 509963):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 0 1 0 1 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 1 1 0 1 1 1 0 1 0 1 0 1 1 1 1 1 1 0 0 1 1 0 1 1 1 0 1 1 1 0 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.6667 1 1.6667 1 1 0 1.6330 0 1.6330 1.6667 1 1.9907 1 1 1 0 1.0887 1.6330 0 1.7249 1.9907 2.0718 1 1 1 0
- 1 1.6667 1.7249 0 1.9907 1 1.9907 1.6330 1 0 1.6667 1 1.9907 1.9907 0 1.7778 1.6667 1 1.6330 0 1 1.9907 2.0718 1 1.7778 0 2.4369 1.6667 1.6330 0


D :

R

1.6667 1 1 1.9907 1.6667 2.4369 0 1 1 0 1 1 1 1.6330 1 1.6667 1 0 1 0 1 1 1 1 1.6330 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 806](<2010-arkus-deriving-finite-sphere-packings_images/imageFile806.png>)

![image 807](<2010-arkus-deriving-finite-sphere-packings_images/imageFile807.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.00700R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.0264 −0.3629 0 −0.4811 −0.2722 0.8333 −0.4811 −1.3608 −0.8333

C :

R

- −0.9943 0 0

0.9623

- −1.3608 0


0.2887 −0.8165 −0.5000 0.2887 −0.8165 0.5000 −0.5774 −0.8165 0

 

 

Packing 182 (Graph 510336):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 0 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.9907 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1.1529 1.6667 1 1 0
- 1 1.6667 1.7249 0 1.7778 1 1 1.9907 1.6330 0


1.9907 1 1.6667 1.7778 0 1.8178 1.6667 1 1.6330 0 1 1.9907 1.1529 1 1.8178 0 1.6330 1.7778 1.6667 0 1 1 1.6667 1 1.6667 1.6330 0 1.6330 1 0

D :

R

1.6667 1 1 1.9907 1 1.7778 1.6330 0 1 0 1 1 1 1.6330 1.6330 1.6667 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 808](<2010-arkus-deriving-finite-sphere-packings_images/imageFile808.png>)

![image 809](<2010-arkus-deriving-finite-sphere-packings_images/imageFile809.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.36708R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.0264 0.3629 0 0.4811 0.2722 −0.8333 −0.5453 1.7237 −0.8333 −0.4491 −0.0907 −0.8889 0.5774 0.8165 0 −0.9623 1.3608 0 −0.2887 0.8165 0.5000 −0.2887 0.8165 −0.5000

C :

R

 

 

Packing 183 (Graph 510412):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1 1 1.6667 1 0 1.6330 0 1.6330 1.6667 1 1.9907 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 1.1529 1.6667 1 1 0
- 1 1.6667 1.7249 0 2.4369 1 1 1.9907 1.6330 0


1.9907 1 1.6667 2.4369 0 2.5035 1.6667 1 1 0 1 1.9907 1.1529 1 2.5035 0 1.6330 1.7778 1.6667 0 1 1 1.6667 1 1.6667 1.6330 0 1.6330 1 0

D :

R

1.6667 1 1 1.9907 1 1.7778 1.6330 0 1 0 1 1 1 1.6330 1 1.6667 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 810](<2010-arkus-deriving-finite-sphere-packings_images/imageFile810.png>)

![image 811](<2010-arkus-deriving-finite-sphere-packings_images/imageFile811.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.94115R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.0264 −0.3629 0 −0.4811 −0.2722 −0.8333 0.5453 −1.7237 0.8333 0.4491 0 −0.8889 −0.5774 −0.8165 −0.0000 0.9623 −1.3608 0 0.2887 −0.8165 0.5000 0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 184 (Graph 512851):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 1 0 0 0 0 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 1 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 1 0 1 0 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1 1 1.6330 1 0 1.6667 0 1.6667 1.9907 1 2.4369 1 1 1.6330 0 1.6667 1.6667 0 1.9907 1.0887 1.7778 1.6330 1 1 0
- 1 1.9907 1.9907 0 2.4369 1 1 1.6667 1 0


1.9907 1 1.0887 2.4369 0 2.5402 1.6330 1 1.6667 0 1 2.4369 1.7778 1 2.5402 0 1.6330 1.9907 1 0 1 1 1.6330 1 1.6330 1.6330 0 1 1 0

D :

R

1.6330 1 1 1.6667 1 1.9907 1 0 1 0 1 1.6330 1 1 1.6667 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 812](<2010-arkus-deriving-finite-sphere-packings_images/imageFile812.png>)

![image 813](<2010-arkus-deriving-finite-sphere-packings_images/imageFile813.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.51934R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6667 0 1.4434 0.8333 0 −0.0321 −0.0556 −0.9979 0.9302 1.7222 0.3629 0.5880 −0.6481 −0.4838 −0.0962 0.8333 −0.5443 0.7698 1.3333 −0.5443 0.7698 0.3333 −0.5443 0.4811 0.8333 0.2722

C :

R

 

 

Packing 185 (Graph 514295):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1.7249 1 1 1.6667 1 0 1.0887 0 1.6330 1.7249 1 1.1529 1.6667 1 1 0 1.6330 1.6330 0 1.6667 1.6667 1.9907 1 1 1 0
- 1 1.7249 1.6667 0 1.8144 1 1 1.9907 1.6330 0


1.7249 1 1.6667 1.8144 0 1.2445 1.9907 1 1.6330 0 1 1.1529 1.9907 1 1.2445 0 1.6330 1.7778 1.6667 0 1 1.6667 1 1 1.9907 1.6330 0 1.6330 1 0

D :

R

1.6667 1 1 1.9907 1 1.7778 1.6330 0 1 0 1 1 1 1.6330 1.6330 1.6667 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 814](<2010-arkus-deriving-finite-sphere-packings_images/imageFile814.png>)

![image 815](<2010-arkus-deriving-finite-sphere-packings_images/imageFile815.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.22442R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.0887 0 −1.5396 0.5443 0 −0.4170 −0.3629 −0.8333 −0.4170 1.4515 −0.8333 0.2352 0.3931 −0.8889 −0.9623 −0.2722 −0.0000 −0.9623 1.3608 −0.0000 −0.6736 0.5443 0.5000 −0.6736 0.5443 −0.5000

C :

R

 

 

###### *Packing 186 (Graph 514375):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1.7249 1 1 1.6667 1 0 1.0887 0 1.6330 1.7249 1 1.1529 1.6667 1 1 0 1.6330 1.6330 0 1.6667 1.6667 1.9907 1 1 1 0
- 1 1.7249 1.6667 0 2.4637 1 1 1.9907 1.6330 0


1.7249 1 1.6667 2.4637 0 2.1241 1.9907 1 1 0 1 1.1529 1.9907 1 2.1241 0 1.6330 1.7778 1.6667 0 1 1.6667 1 1 1.9907 1.6330 0 1.6330 1 0

D :

R

1.6667 1 1 1.9907 1 1.7778 1.6330 0 1 0 1 1 1 1.6330 1 1.6667 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 816](<2010-arkus-deriving-finite-sphere-packings_images/imageFile816.png>)

![image 817](<2010-arkus-deriving-finite-sphere-packings_images/imageFile817.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.79849R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.0887 0 −1.5396 −0.5443 0 −0.4170 0.3629 0.8333 −0.4170 −1.4515 −0.8333 0.2352 −0.3931 0.8889 −0.9623 0.2722 0 −0.9623 −1.3608 −0.0000 −0.6736 −0.5443 −0.5000 −0.6736 −0.5443 0.5000

C :

R

 

 

Packing 187 (Graph 516148):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 0 0 1 0 1 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1 1 1.6330 1 0 1.6667 0 1.6667 1.9907 1 1.7778 1.6330 1 1 0 1.6667 1.6667 0 1.0887 1.9907 1.7249 1 1 1.6330 0
- 1 1.9907 1.0887 0 2.4369 1 1 1.6667 1.6330 0


1.9907 1 1.9907 2.4369 0 2.5035 1.6667 1 1 0 1 1.7778 1.7249 1 2.5035 0 1.6330 1.9907 1.6667 0 1 1.6330 1 1 1.6667 1.6330 0 1 1 0

D :

R

1.6330 1 1 1.6667 1 1.9907 1 0 1 0 1 1 1.6330 1.6330 1 1.6667 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 818](<2010-arkus-deriving-finite-sphere-packings_images/imageFile818.png>)

![image 819](<2010-arkus-deriving-finite-sphere-packings_images/imageFile819.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.20453R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6667 0 1.4434 −0.8333 0 0.9302 0 −0.3629 −0.0321 −1.7222 0.9979 0.1711 −0.1852 −0.9677 0.7698 −0.3333 0.5443 0.7698 −1.3333 0.5443 −0.0962 −0.8333 0.5443 0.4811 −0.8333 −0.2722

C :

R

 

 

Packing 188 (Graph 516292):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 0 1 0 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1 1 1.6330 1 0 1.6667 0 1.6667 1.9907 1 1.7778 1.6330 1 1 0 1.6667 1.6667 0 1.9907 1.0887 2.4369 1 1 1 0
- 1 1.9907 1.9907 0 2.4369 1 1 1.6667 1.6330 0


1.9907 1 1.0887 2.4369 0 2.5035 1.6667 1 1 0 1 1.7778 2.4369 1 2.5035 0 1.6330 1.9907 1.6667 0 1 1.6330 1 1 1.6667 1.6330 0 1 1 0

D :

R

1.6330 1 1 1.6667 1 1.9907 1 0 1 0 1 1 1 1.6330 1 1.6667 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 820](<2010-arkus-deriving-finite-sphere-packings_images/imageFile820.png>)

![image 821](<2010-arkus-deriving-finite-sphere-packings_images/imageFile821.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.50082R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6667 0 −1.4434 −0.8333 0 0 0 0.9979 −0.9302 −1.7222 −0.3629 0.8553 −0.1852 0.4838 −0.7698 −0.3333 0.5443 −0.7698 −1.3333 0.5443 −0.4811 −0.8333 −0.2722 0 −0.8333 0.5443

C :

R

 

 

Packing 189 (Graph 516323):





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 0 0 1 1 1 0 1 0 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.9149 1.4142 1 2.3333 1 1 1.7321 1 0 1.9149 0 1.6667 1.9149 1 1.4142 1.6330 1 1 0 1.4142 1.6667 0 1.9149 1.9907 1.9149 1 1 1 0
- 1 1.9149 1.9149 0 1.9437 1 1 1.7321 1.4142 0


2.3333 1 1.9907 1.9437 0 1.9149 1.6667 1 1.6330 0 1 1.4142 1.9149 1 1.9149 0 1.4142 1.7321 1 0 1 1.6330 1 1 1.6667 1.4142 0 1 1 0

D :

R

1.7321 1 1 1.7321 1 1.7321 1 0 1 0 1 1 1 1.4142 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 822](<2010-arkus-deriving-finite-sphere-packings_images/imageFile822.png>)

![image 823](<2010-arkus-deriving-finite-sphere-packings_images/imageFile823.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.80741R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.9149 0 1.1962 −0.7543 0 −0.4433 −0.2611 0.8575 0.1196 −2.1179 0.9718 −0.7177 −0.6963 −0.0000 0.5066 −0.5222 0.6860 0.7389 −1.4797 0.5145 0.2322 −0.9574 −0.1715 −0.2111 −1.2185 0.6860

C :

R

 

 

Packing 190 (Graph 516437):





0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 0 1 1 1 0 0 1 0 0 0 1 0 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 0 1 1 0 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.9149 1.9149 1 2.3333 1 1 1 1.7321 0 1.9149 0 1.6667 1.9149 1 1.4142 1.6330 1 1 0 1.9149 1.6667 0 1.4142 1.0887 1.9149 1 1.6330 1 0
- 1 1.9149 1.4142 0 1.9437 1 1 1.4142 1.7321 0


2.3333 1 1.0887 1.9437 0 1.9149 1.6667 1.6330 1 0 1 1.4142 1.9149 1 1.9149 0 1.4142 1 1.7321 0 1 1.6330 1 1 1.6667 1.4142 0 1 1 0 1 1 1.6330 1.4142 1.6330 1 1 0 1 0

D :

R

 

 

1.7321 1 1 1.7321 1 1.7321 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 824](<2010-arkus-deriving-finite-sphere-packings_images/imageFile824.png>)

![image 825](<2010-arkus-deriving-finite-sphere-packings_images/imageFile825.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.52963R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.9149 0 1.5006 −1.1895 0 0.6816 −0.2611 −0.6836 0.9620 −2.1179 −0.1823 −0.2188 −0.6963 −0.6836 0.8078 −0.5222 0.2734

C :

R

- −0.0926 −0.9574

0.2734 0.7152 −1.4797 0.5469 0.5890

- −1.2185 −0.4102


 

 

Packing 191 (Graph 520931):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 0 1 0 0 0 1 0 0 0 1 1 0 1 0 0 0 1 1 1 1 0 1 0 1 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 1 1 0

A :

 

 





- 0 1.6330 1.0887 1 1.9907 1 1.6667 1 1 0 1.6330 0 1.6330 1.6667 1 1.9907 1 1 1 0 1.0887 1.6330 0 1.7249 1.6667 2.0718 1 1.6667 1 0
- 1 1.6667 1.7249 0 2.4369 1 1.9907 1 1.6330 0 1.9907 1 1.6667 2.4369 0 2.5402 1 1.6667 1 0


D :

R

1 1.9907 2.0718 1 2.5402 0 2.4369 1 1.6667 0

1.6667 1 1 1.9907 1 2.4369 0 1.6330 1 0 1 1 1.6667 1 1.6667 1 1.6330 0 1 0 1 1 1 1.6330 1 1.6667 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 826](<2010-arkus-deriving-finite-sphere-packings_images/imageFile826.png>)

![image 827](<2010-arkus-deriving-finite-sphere-packings_images/imageFile827.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.53374R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.0264 0.3629 0 0.4811 0.2722 −0.8333 −0.5453 1.7237 0.8333 0.9943 −0.0907 −0.0556 −0.9623 1.3608 −0.0000 0.5774 0.8165 0 −0.2887 0.8165 0.5000 −0.2887 0.8165 −0.5000

C :

R

 

 

Packing 192 (Graph 521137):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 0 1 0 0 0 1 0 0 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 1 1 0

A :

 

 





- 0 1.0887 1.6330 1 1.7249 1 1.6667 1 1 0 1.0887 0 1.6330 1.7249 1 2.0718 1 1.6667 1 0 1.6330 1.6330 0 1.6667 1.6667 1.9907 1 1 1 0
- 1 1.7249 1.6667 0 2.4637 1 1.9907 1 1.6330 0 1.7249 1 1.6667 2.4637 0 2.5831 1 1.9907 1 0


D :

R

- 1 2.0718 1.9907 1 2.5831 0 2.4369 1 1.6667 0


1.6667 1 1 1.9907 1 2.4369 0 1.6330 1 0 1 1.6667 1 1 1.9907 1 1.6330 0 1 0 1 1 1 1.6330 1 1.6667 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 828](<2010-arkus-deriving-finite-sphere-packings_images/imageFile828.png>)

![image 829](<2010-arkus-deriving-finite-sphere-packings_images/imageFile829.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.58861R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.0887 0 −1.5396 −0.5443 0 −0.4170 0.3629 0.8333 −0.4170 −1.4515 −0.8333 −0.2459 0.9677 0 −0.9623 −1.3608 −0.0000 −0.9623 0.2722 0 −0.6736 −0.5443 −0.5000 −0.6736 −0.5443 0.5000

C :

R

 

 

Packing 193 (Graph 521334):





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 0 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 1 0 0 1 1 0 1 1 0 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6667 1.6667 1 1.9907 1 1.6330 1 1 0 1.6667 0 1.6667 1.9907 1 2.4369 1 1 1 0 1.6667 1.6667 0 1.0887 1.9907 1.7249 1 1.6330 1 0
- 1 1.9907 1.0887 0 2.4369 1 1.6667 1.6330 1 0 1.9907 1 1.9907 2.4369 0 2.5402 1 1 1.6330 0 1 2.4369 1.7249 1 2.5402 0 1.9907 1.6667 1.6330 0


D :

R

1.6330 1 1 1.6667 1 1.9907 0 1 1 0 1 1 1.6330 1.6330 1 1.6667 1 0 1 0 1 1 1 1 1.6330 1.6330 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 830](<2010-arkus-deriving-finite-sphere-packings_images/imageFile830.png>)

![image 831](<2010-arkus-deriving-finite-sphere-packings_images/imageFile831.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.50082R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6667 0 1.4434 0.8333 0 0.9302 −0.0556 −0.3629 −0.0321 1.7222 0.9979 0.6522 −0.6481 0.3931 0.7698 1.3333 0.5443 −0.0962 0.8333 0.5443 0.4811 0.8333 −0.2722 0.7698 0.3333 0.5443

C :

R

 

 

###### *Packing 194 (Graph 550941):





0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 0 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 0 0 0 0 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.7199 1.7221 1 1.7199 1 1 1 1 0 1.7199 0 1.5224 2.3494 1 1 1.5130 1.7199 1 0 1.7221 1.5224 0 1.9998 1.9591 1 1.7204 1 1.8799 0
- 1 2.3494 1.9998 0 1.9998 1.7204 1 1 1.7221 0


1.7199 1 1.9591 1.9998 0 1.5130 1 1.7199 1 0 1 1 1 1.7204 1.5130 0 1.2892 1 1 0 1 1.5130 1.7204 1 1 1.2892 0 1 1 0 1 1.7199 1 1 1.7199 1 1 0 1.5130 0 1 1 1.8799 1.7221 1 1 1 1.5130 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 832](<2010-arkus-deriving-finite-sphere-packings_images/imageFile832.png>)

![image 833](<2010-arkus-deriving-finite-sphere-packings_images/imageFile833.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.63380R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7199 0 −1.3662 −1.0484 0 −0.3360 0.4539 0.8253 0.3333 −1.4292 0.8969 −0.4255 −0.8600 −0.2818 0 −0.4852 0.8744 −0.8623 −0.2907 0.4147 0.5019 −0.8600 0 −0.6097 −1.2347 0.6268

C :

R

 

 

Packing 195 (Graph 590324):





0 0 0 1 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 1 0 0 0 0 1 1 1 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 1 0

A :

 

 





- 0 1.6779 1.6180 1 1.9889 1 1 1 1.6180 0 1.6779 0 1.6779 2.4520 1 1.6532 1 1.9843 1 0 1.6180 1.6779 0 1.6779 1.9889 1 1 1 1 0
- 1 2.4520 1.6779 0 2.5385 1 1.6532 1 1.9843 0


1.9889 1 1.9889 2.5385 0 1.6482 1.6330 2.4047 1 0 1 1.6532 1 1 1.6482 0 1.0515 1 1 0 1 1 1 1.6532 1.6330 1.0515 0 1 1 0 1 1.9843 1 1 2.4047 1 1 0 1.6180 0

D :

R

 

 

1.6180 1 1 1.9843 1 1 1 1.6180 0 0 0 0 0 0 0 0 0 0 0 0

![image 834](<2010-arkus-deriving-finite-sphere-packings_images/imageFile834.png>)

![image 835](<2010-arkus-deriving-finite-sphere-packings_images/imageFile835.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.43319R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6779 0 −1.4175 −0.7801 0 −0.6434 0.6546 0.3969 0 −1.7197 0.9989 −0.7459 −0.3226 0.5827 −0.4617 −0.8390 −0.2880 −0.9435 0 −0.3295 −0.7671 −1.3211 0.5331 0.1090 −0.8390 0.5331

C :

R

 

 

Packing 196 (Graph 593645):





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 2.2361 1 1 2.2361 1 0 1.7321 0 1.4142 1.7321 1 1.7321 1 1 1 0 1.7321 1.4142 0 1.7321 1.7321 1 1.7321 1 1 0
- 1 1.7321 1.7321 0 1.7321 1 1 2.0000 1.4142 0


2.2361 1 1.7321 1.7321 0 2.0000 1.4142 1 1.7321 0 1 1.7321 1 1 2.0000 0 1.4142 1.7321 1 0 1 1 1.7321 1 1.4142 1.4142 0 1.7321 1 0

D :

R

2.2361 1 1 2.0000 1 1.7321 1.7321 0 1.4142 0 1 1 1 1.4142 1.7321 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 836](<2010-arkus-deriving-finite-sphere-packings_images/imageFile836.png>)

![image 837](<2010-arkus-deriving-finite-sphere-packings_images/imageFile837.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.70000R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7321 0

- −1.2910 −1.1547

0 −0.1291 −0.2887 0.9487 −0.1291 −2.0207 0.9487 −0.9037 −0.2887 0.3162 0.3873 −0.8660 0.3162 −0.9037

- −2.0207 0.3162


C :

R

−0.3873 −0.8660 −0.3162 −0.5164 −1.1547 0.6325

 

 

Packing 197 (Graph 593702):





0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 1 0 0 1 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.4142 1.4142 1 1.9149 1 1 1.7321 1 0 1.4142 0 1.6330 1.7321 1 1.9149 1 1 1 0 1.4142 1.6330 0 1.7321 1.6667 1 1.9149 1 1 0
- 1 1.7321 1.7321 0 2.5166 1 1 2.0000 1.7321 0


1.9149 1 1.6667 2.5166 0 2.3333 1.9149 1 1 0 1 1.9149 1 1 2.3333 0 1.6330 1.7321 1.4142 0 1 1 1.9149 1 1.9149 1.6330 0 1.7321 1.4142 0

D :

R

1.7321 1 1 2.0000 1 1.7321 1.7321 0 1 0 1 1 1 1.7321 1 1.4142 1.4142 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 838](<2010-arkus-deriving-finite-sphere-packings_images/imageFile838.png>)

![image 839](<2010-arkus-deriving-finite-sphere-packings_images/imageFile839.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.12227R2<br><br>|C1|1|chiral non-rigid<br><br>|






0 0 0 0 −1.4144 0 −1.3332 −0.4713 0 0 −0.0002 −1.0000 −0.5000 −1.6500 0.8333 −0.8332 0.2356 −0.5002 0.5001 −0.7072 −0.4998 −1.0000 −1.4142 −0.0000 −0.4999 −0.7072 0.5000

C :

R

- −0.4999 −0.7072
- −0.5000


 

 

Packing 198 (Graph 593729):





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.1832 1.6796 1 1.8676 1 1 1.7496 1 0 1.1832 0 1.6330 1.6667 1 1.6667 1 1 1 0 1.6796 1.6330 0 1.6938 1.6667 1 1.9667 1 1 0
- 1 1.6667 1.6938 0 1.8095 1 1 1.9838 1.5920 0


1.8676 1 1.6667 1.8095 0 1.9907 1.2689 1 1.6330 0 1 1.6667 1 1 1.9907 0 1.5920 1.6330 1 0 1 1 1.9667 1 1.2689 1.5920 0 1.7167 1.5345 0

D :

R

1.7496 1 1 1.9838 1 1.6330 1.7167 0 1 0 1 1 1 1.5920 1.6330 1 1.5345 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 840](<2010-arkus-deriving-finite-sphere-packings_images/imageFile840.png>)

![image 841](<2010-arkus-deriving-finite-sphere-packings_images/imageFile841.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.22647R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.1832 0 −1.5458 0.6569 0 −0.3758 −0.1596 −0.9128 −0.4440 1.6429 −0.7691 −0.9803 −0.1596 −0.1162 0.2665 0.5916 −0.7609 −0.9577 1.4626 0 −0.6611 0.5916 0.4615 −0.7000 0.7060 −0.5312

C :

R

 

 

Packing 199 (Graph 593782):





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 0 0 1 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6796 1.1832 1 2.1060 1 1 1.7496 1 0 1.6796 0 1.6330 1.6938 1 1.9667 1 1 1 0 1.1832 1.6330 0 1.6667 1.6667 1 1.6667 1 1 0
- 1 1.6938 1.6667 0 1.8263 1 1 1.9838 1.5920 0


2.1060 1 1.6667 1.8263 0 1.8767 1.6667 1 1.6330 0 1 1.9667 1 1 1.8767 0 1.5920 1.7167 1.5345 0 1 1 1.6667 1 1.6667 1.5920 0 1.6330 1 0

D :

R

1.7496 1 1 1.9838 1 1.7167 1.6330 0 1 0 1 1 1 1.5920 1.6330 1.5345 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 842](<2010-arkus-deriving-finite-sphere-packings_images/imageFile842.png>)

![image 843](<2010-arkus-deriving-finite-sphere-packings_images/imageFile843.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.39996R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6796 0 1.0890 0.4628 0 −0.2939 0.2835 −0.9128 0.6124 1.8624 −0.7691 0.6487 −0.0139 −0.7609 −0.5303 0.8398 −0.1162 0.9716 1.4534 0 0.2860 0.8398 0.4615 0.3760 0.9204 −0.5312

C :

R

 

 

Packing 200 (Graph 593834):





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 0 0 1 1 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.9149 1 2.3333 1 1 1.9149 1 0 1.7321 0 1.7321 1.7321 1 1.7321 1 1 1 0 1.9149 1.7321 0 1.6330 1.4142 1 1.9149 1 1.4142 0
- 1 1.7321 1.6330 0 1.9437 1 1 1.9149 1.4142 0


2.3333 1 1.4142 1.9437 0 1.9149 1.6667 1 1.6330 0 1 1.7321 1 1 1.9149 0 1.4142 1.4142 1 0 1 1 1.9149 1 1.6667 1.4142 0 1.6330 1 0

D :

R

1.9149 1 1 1.9149 1 1.4142 1.6330 0 1 0 1 1 1.4142 1.4142 1.6330 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 844](<2010-arkus-deriving-finite-sphere-packings_images/imageFile844.png>)

![image 845](<2010-arkus-deriving-finite-sphere-packings_images/imageFile845.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.63333R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.7321 0 1.5957 1.0585 0 0.4352 0.2887 0.8528 0.8027 2.1490 0.4264 0.9574 0.2887 −0.0000 −0.2611 0.8660 0.4264 0.8994 1.6358 −0.4264 0.2611 0.8660 −0.4264 0.6963 1.1547 0.4264

C :

R

 

 

Packing 201 (Graph 593842):





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 0 0 1 1 1 0 1 0 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.9149 1.7321 1 2.3805 1 1 1.9149 1 0 1.9149 0 1.7321 1.6330 1 1.9149 1 1 1.4142 0 1.7321 1.7321 0 1.7321 1.4142 1 1.7321 1 1 0
- 1 1.6330 1.7321 0 1.9149 1 1 1.9149 1.4142 0


2.3805 1 1.4142 1.9149 0 1.9149 1.7321 1 1.7321 0 1 1.9149 1 1 1.9149 0 1.4142 1.6330 1 0 1 1 1.7321 1 1.7321 1.4142 0 1.4142 1 0

D :

R

1.9149 1 1 1.9149 1 1.6330 1.4142 0 1 0 1 1.4142 1 1.4142 1.7321 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 846](<2010-arkus-deriving-finite-sphere-packings_images/imageFile846.png>)

![image 847](<2010-arkus-deriving-finite-sphere-packings_images/imageFile847.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.70000R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.9149 0 1.4434 0.9574 0 −0.0000 0.5222 0.8528 0.8660 2.1760 0.4264 0.8660 0.2611 0.4264 −0.2887 0.9574 −0.0000 0.8660 1.6537 −0.4264 0.5774 0.6963 −0.4264 0.5774 1.2185 0.4264

C :

R

 

 

Packing 202 (Graph 593847):





0 0 0 1 0 1 1 0 0 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 0 1 1 0 0 1 1 1 0 1 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6859 1 1.8113 1 1 1.9868 1.6059 0 1.6859 0 1.6330 1.9770 1 1.6667 1 1 1 0 1.6859 1.6330 0 1.9770 1.6667 1 1.6667 1 1 0
- 1 1.9770 1.9770 0 2.5036 1 1 2.3778 1.5789 0


1.8113 1 1.6667 2.5036 0 1.9907 1.6667 1 1.6330 0 1 1.6667 1 1 1.9907 0 1.0887 1.6330 1 0 1 1 1.6667 1 1.6667 1.0887 0 1.6330 1 0

D :

R

1.9868 1 1 2.3778 1 1.6330 1.6330 0 1 0 1.6059 1 1 1.5789 1.6330 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 848](<2010-arkus-deriving-finite-sphere-packings_images/imageFile848.png>)

![image 849](<2010-arkus-deriving-finite-sphere-packings_images/imageFile849.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.12279R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6859 0 −1.4287 −0.8950 0 0 0 0.9997 −0.2189 −1.5194 −0.9614 −0.7969 −0.3157 0.5151 0.1555 −0.8429 0.5151 −0.9505 −1.7171 −0.3090 −0.7259 −1.3112 0.5769 −0.4666 −0.8429 −0.2678

C :

R

 

 

Packing 203 (Graph 594036):





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 1 1 0 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.1832 1.6796 1 1.7427 1 1 1.7496 1 0 1.1832 0 1.6330 1.6667 1 1.6667 1 1 1 0 1.6796 1.6330 0 1.6938 1.6667 1 1.9667 1 1 0
- 1 1.6667 1.6938 0 2.4149 1 1 1.9838 1.5920 0


1.7427 1 1.6667 2.4149 0 1.9907 1.9667 1 1 0 1 1.6667 1 1 1.9907 0 1.5920 1.6330 1 0 1 1 1.9667 1 1.9667 1.5920 0 1.7167 1.5345 0

D :

R

1.7496 1 1 1.9838 1 1.6330 1.7167 0 1 0 1 1 1 1.5920 1 1 1.5345 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 850](<2010-arkus-deriving-finite-sphere-packings_images/imageFile850.png>)

![image 851](<2010-arkus-deriving-finite-sphere-packings_images/imageFile851.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.66288R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.1832 0 1.5458 −0.6569 0 0.3758 0.1596 −0.9128 0.3791 −1.4523 0.8854 0.9803 0.1596 −0.1162 −0.2665 −0.5916 −0.7609 0.9577 −1.4626 0 0.6611 −0.5916 0.4615 0.7000 −0.7060 −0.5312

C :

R

 

 

###### *Packing 204 (Graph 594112):





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 1 0 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.6796 1.1832 1 1.9961 1 1 1.7496 1 0 1.6796 0 1.6330 1.6938 1 1.9667 1 1 1 0 1.1832 1.6330 0 1.6667 1.6667 1 1.6667 1 1 0
- 1 1.6938 1.6667 0 2.4275 1 1 1.9838 1.5920 0


1.9961 1 1.6667 2.4275 0 2.4041 1.6667 1 1 0 1 1.9667 1 1 2.4041 0 1.5920 1.7167 1.5345 0 1 1 1.6667 1 1.6667 1.5920 0 1.6330 1 0

D :

R

1.7496 1 1 1.9838 1 1.7167 1.6330 0 1 0 1 1 1 1.5920 1 1.5345 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 852](<2010-arkus-deriving-finite-sphere-packings_images/imageFile852.png>)

![image 853](<2010-arkus-deriving-finite-sphere-packings_images/imageFile853.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.83636R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6796 0 −1.0890 0.4628 0 0.2939 0.2835 −0.9128 −0.4624 1.7282 0.8854 −0.6487 −0.0139 −0.7609 0.5303 0.8398 −0.1162 −0.9716 1.4534 0 −0.2860 0.8398 0.4615 −0.3760 0.9204 −0.5312

C :

R

 

 

Packing 205 (Graph 594189):





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 0 1 1 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.9149 1 1.9437 1 1 1.9149 1 0 1.7321 0 1.7321 1.7321 1 1.7321 1 1 1 0 1.9149 1.7321 0 1.6330 1.9149 1 1.9149 1 1.4142 0
- 1 1.7321 1.6330 0 2.3333 1 1 1.9149 1.4142 0


1.9437 1 1.9149 2.3333 0 1.9149 1.6667 1 1 0 1 1.7321 1 1 1.9149 0 1.4142 1.4142 1 0 1 1 1.9149 1 1.6667 1.4142 0 1.6330 1 0

D :

R

1.9149 1 1 1.9149 1 1.4142 1.6330 0 1 0 1 1 1.4142 1.4142 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 854](<2010-arkus-deriving-finite-sphere-packings_images/imageFile854.png>)

![image 855](<2010-arkus-deriving-finite-sphere-packings_images/imageFile855.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.80000R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.7321 0 1.5957 1.0585 0 0.4352 0.2887 0.8528 0 1.6679 −0.9949 0.9574 0.2887 −0.0000 −0.2611 0.8660 0.4264 0.8994 1.6358 −0.4264 0.2611 0.8660 −0.4264 0.6963 1.1547 0.4264

C :

R

 

 

Packing 206 (Graph 594241):





0 0 0 1 0 1 1 0 0 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6859 1 2.4315 1 1 1.9868 1.6059 0 1.6859 0 1.6330 1.9770 1 1.6667 1 1 1 0 1.6859 1.6330 0 1.9770 1.6667 1 1.6667 1 1 0
- 1 1.9770 1.9770 0 2.4748 1 1 2.3778 1.5789 0


2.4315 1 1.6667 2.4748 0 1.9907 1.6667 1 1 0 1 1.6667 1 1 1.9907 0 1.0887 1.6330 1 0 1 1 1.6667 1 1.6667 1.0887 0 1.6330 1 0

D :

R

1.9868 1 1 2.3778 1 1.6330 1.6330 0 1 0 1.6059 1 1 1.5789 1 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 856](<2010-arkus-deriving-finite-sphere-packings_images/imageFile856.png>)

![image 857](<2010-arkus-deriving-finite-sphere-packings_images/imageFile857.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.37163R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6859 0 1.4287 0.8950 0 −0.0109 −0.0197 −0.9997 0.6510 2.2998 −0.4464 0.7969 0.3157 −0.5151 −0.1555 0.8429 −0.5151 0.9505 1.7171 0.3090 0.7259 1.3112 −0.5769 0.4666 0.8429 0.2678

C :

R

 

 

###### *Packing 207 (Graph 594872):





0 0 0 1 0 1 1 1 0 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 1 1 0 1 1 0 0 1 0 1 0 0 1 0 1 1 1 0 1 1 0 0 1 1 1 1 0 1 1 0 1 1 0

A :

 

 





- 0 1.5130 1.7204 1 1.7221 1 1 1 1.2892 0 1.5130 0 1.5224 1.7199 1 1.7199 1 1 1 0 1.7204 1.5224 0 1.7221 1.7389 1 1.8799 1.9591 1 0
- 1 1.7199 1.7221 0 2.3494 1 1 1.7199 1 0


1.7221 1 1.7389 2.3494 0 1.9998 1.7204 1 1.7221 0 1 1.7199 1 1 1.9998 0 1.5130 1.7199 1 0 1 1 1.8799 1 1.7204 1.5130 0 1 1 0 1 1 1.9591 1.7199 1 1.7199 1 0 1.5130 0

D :

R

 

 

1.2892 1 1 1 1.7221 1 1 1.5130 0 0 0 0 0 0 0 0 0 0 0 0

![image 858](<2010-arkus-deriving-finite-sphere-packings_images/imageFile858.png>)

![image 859](<2010-arkus-deriving-finite-sphere-packings_images/imageFile859.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.53626R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.5130 0 1.4218 −0.9688 0 0.2751 −0.1094 −0.9552 0 −1.4061 0.9923 0.9664 −0.1094 −0.2326 −0.3657 −0.7565 −0.5422 −0.4726 −0.7565 0.4521 0.6092 −0.9753 −0.5828 0.5255 −0.7565 0.3893

C :

R

 

 

Packing 208 (Graph 601365):





0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 0 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 1 0 0 0 1 0 1 1 1 0 0 1 0 0 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 0 1 0 1 1 0 0 1 1 1 1 0 1 1 1 0 0

A :

 

 





- 0 1.4142 1.6330 1 1.7321 1 1 1 1 0 1.4142 0 1.4142 1.9149 1 1.7321 1 1 1 0 1.6330 1.4142 0 1.6667 2.3805 1 1.9149 1 1.9149 0
- 1 1.9149 1.6667 0 2.3805 1 1.4142 1.6330 1.9149 0


1.7321 1 2.3805 2.3805 0 2.4495 1 1.7321 1 0 1 1.7321 1 1 2.4495 0 1.7321 1 1.7321 0 1 1 1.9149 1.4142 1 1.7321 0 1.4142 1 0 1 1 1 1.6330 1.7321 1 1.4142 0 1 0 1 1 1.9149 1.9149 1 1.7321 1 1 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 860](<2010-arkus-deriving-finite-sphere-packings_images/imageFile860.png>)

![image 861](<2010-arkus-deriving-finite-sphere-packings_images/imageFile861.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.21111R2<br><br>|Cs|1| |






0 0 0 0 −1.4142 0 1.3333 −0.9428 0 0.5000 0.2357 −0.8333 −1.0000 −1.4142 −0.0000 1.0000 0 −0.0000 −0.5000 −0.7071 −0.5000 0.5000 −0.7071 0.5000 −0.5000 −0.7071 0.5000 0.5000 −0.7071 −0.5000

C :

R

 

 

###### *Packing 209 (Graph 606541):





0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 1 0 0 0 1 0 1 1 1 0 0 1 0 0 1 1 0 1 1 1 0 0 1 1 0 0 1 1 1 0 1 1 0 1 0 0 1 0 1 1 1 0 1 0 1 1 0

A :

 

 





- 0 1.5130 1.7204 1 1.7221 1 1 1 1 0 1.5130 0 1.5224 1.7199 1 1.7199 1 1 1 0 1.7204 1.5224 0 1.7221 2.4520 1 1.9591 1 1.8799 0
- 1 1.7199 1.7221 0 1.9998 1 1.7199 1.5130 1 0


1.7221 1 2.4520 1.9998 0 2.3494 1 1.7204 1 0 1 1.7199 1 1 2.3494 0 1.7199 1 1.5130 0 1 1 1.9591 1.7199 1 1.7199 0 1 1 0 1 1 1 1.5130 1.7204 1 1 0 1.2892 0 1 1 1.8799 1 1 1.5130 1 1.2892 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 862](<2010-arkus-deriving-finite-sphere-packings_images/imageFile862.png>)

![image 863](<2010-arkus-deriving-finite-sphere-packings_images/imageFile863.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.83511R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.5130 0 −1.4218 −0.9688 0 −0.2751 −0.1094 0.9552 0.9886 −1.4061 0.1062 −0.9664 −0.1094 0.2326 0.4726 −0.7565 −0.4521 −0.5255 −0.7565 −0.3893 0.3657 −0.7565 0.5422 −0.6092 −0.9753 0.5828

C :

R

 

 

Packing 210 (Graph 607008):





0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 1 0 1 0 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 0 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 1.4142 1 1 1 1 0 1.7321 0 2.0000 2.4495 1 1.7321 1 1.7321 1 0 1.7321 2.0000 0 1.4142 2.5166 1 1.7321 1 1.7321 0
- 1 2.4495 1.4142 0 2.3805 1 1.7321 1 1.7321 0


1.4142 1 2.5166 2.3805 0 1.9149 1 1.9149 1 0 1 1.7321 1 1 1.9149 0 1.4142 1 1 0 1 1 1.7321 1.7321 1 1.4142 0 1 1 0 1 1.7321 1 1 1.9149 1 1 0 1.4142 0 1 1 1.7321 1.7321 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 864](<2010-arkus-deriving-finite-sphere-packings_images/imageFile864.png>)

![image 865](<2010-arkus-deriving-finite-sphere-packings_images/imageFile865.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.30000R2<br><br>|Cs|1| |






0 0 0 0 −1.7321 0 −1.6330 −0.5774 0 −0.8165 0.5774 0 0.8165 −1.1547 −0.0000 −0.8165 −0.2887 −0.5000 −0.0000 −0.8660 0.5000 −0.8165 −0.2887 0.5000 −0.0000 −0.8660 −0.5000 −0.8165 −1.1547 −0.0000

C :

R

 

 

Packing 211 (Graph 610105):





0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 1 0 0 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 1 0 0 0 1 0 1 0 1 1 0 1 0 0 0 1 1 1 1 1 0 0 1 0 0 1 1 0 1 1 0 1 0 1 1 0 0 1 1 1 1 0 1 1 1 0 0

A :

 

 





- 0 1.4142 1.6330 1 2.3805 1 1.9149 1 1.9149 0 1.4142 0 1.4142 1.9149 1 1.7321 1 1 1 0 1.6330 1.4142 0 1.6667 1.7321 1 1 1 1 0
- 1 1.9149 1.6667 0 2.7285 1 1.9437 1.6330 2.3333 0 2.3805 1 1.7321 2.7285 0 2.4495 1 1.7321 1 0


D :

R

1 1.7321 1 1 2.4495 0 1.7321 1 1.7321 0 1.9149 1 1 1.9437 1 1.7321 0 1.4142 1 0

1 1 1 1.6330 1.7321 1 1.4142 0 1 0 1.9149 1 1 2.3333 1 1.7321 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 866](<2010-arkus-deriving-finite-sphere-packings_images/imageFile866.png>)

![image 867](<2010-arkus-deriving-finite-sphere-packings_images/imageFile867.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.74444R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.4142 0 −1.3333 0.9428 0 −0.5000 −0.2357 0.8333 −0.3333 2.3570 0 −1.0000 0 −0.0000 −0.8333 1.6499 0.5000 −0.5000 0.7071 −0.5000 −0.8333 1.6499 −0.5000 −0.5000 0.7071 0.5000

C :

R

 

 

Packing 212 (Graph 610977):





0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 1 0 1 0 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 1 0 1 0 0 0 1 0 1 1 0 1 1 1 0 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.7778 1.6330 1 2.5035 1 1.9907 1 1.6667 0 1.7778 0 1.6330 2.5035 1 1.6667 1 1.9907 1 0 1.6330 1.6330 0 1.6667 1.6667 1 1 1 1 0
- 1 2.5035 1.6667 0 2.9630 1 2.4369 1 1.9907 0 2.5035 1 1.6667 2.9630 0 1.9907 1 2.4369 1 0


D :

R

1 1.6667 1 1 1.9907 0 1.6330 1 1 0 1.9907 1 1 2.4369 1 1.6330 0 1.6667 1 0

1 1.9907 1 1 2.4369 1 1.6667 0 1.6330 0 1.6667 1 1 1.9907 1 1 1 1.6330 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 868](<2010-arkus-deriving-finite-sphere-packings_images/imageFile868.png>)

![image 869](<2010-arkus-deriving-finite-sphere-packings_images/imageFile869.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|10.60919R2<br><br>|Cs|1| |






0 0 0 0 −1.7778 0 1.3699 −0.8889 0 0.7090 0.5926 −0.3824 0.7090 −2.3704 −0.3824 0.7210 −0.3889 −0.5735 0.9373 −1.7222 0.3441 0.9373 −0.0556 0.3441 0.7210 −1.3889 −0.5735 0.3965 −0.8889 0.2294

C :

R

 

 

Packing 213 (Graph 613779):





0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 1 0 1 0 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 0 1 1 0 1 1 0 0 1 0 1 1 0 1 1 1 0 0 1 1 1 0 0 0 1 1 1 1 0

A :

 

 





- 0 2.0000 1.7321 1 2.5166 1 1.7321 1 1.7321 0 2.0000 0 1.7321 2.5166 1 1.7321 1 1.7321 1 0 1.7321 1.7321 0 1.4142 1.4142 1 1 1 1 0
- 1 2.5166 1.4142 0 2.6667 1 1.9149 1 1.9149 0 2.5166 1 1.4142 2.6667 0 1.9149 1 1.9149 1 0


D :

R

- 1 1.7321 1 1 1.9149 0 1.4142 1 1 0 1.7321 1 1 1.9149 1 1.4142 0 1 1 0
- 1 1.7321 1 1 1.9149 1 1 0 1.4142 0 1.7321 1 1 1.9149 1 1 1 1.4142 0 0


 

 

0 0 0 0 0 0 0 0 0 0

![image 870](<2010-arkus-deriving-finite-sphere-packings_images/imageFile870.png>)

![image 871](<2010-arkus-deriving-finite-sphere-packings_images/imageFile871.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|9.57778R2|C2v|2| |






0 0 0 0 2.0000 0 1.4142 1.0000 0 0.9428 −0.3333 0 0.9428 2.3333 0 0.7071 0.5000 −0.5000 0.7071 1.5000 0.5000 0.7071 0.5000 0.5000 0.7071 1.5000 −0.5000 0 1.0000 −0.0000

C :

R

 

 

Packing 214 (Graph 618645):





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 0 1 0 1 1 0 0 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.8689 1 1 1.8362 1.6938 1 1.9667 0 1.6330 0 1.6330 1.6667 1 1 1.6667 1 1 0 1.8689 1.6330 0 1.6938 1.8362 1 1 1.9667 1 0
- 1 1.6667 1.6938 0 1.6330 1.9838 1 1 1.5920 0 1 1 1.8362 1.6330 0 1.2689 1.9838 1 1.7167 0


D :

R

1.8362 1 1 1.9838 1.2689 0 1.6330 1.7167 1 0 1.6938 1.6667 1 1 1.9838 1.6330 0 1.5920 1 0

1 1 1.9667 1 1 1.7167 1.5920 0 1.5345 0 1.9667 1 1 1.5920 1.7167 1 1 1.5345 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 872](<2010-arkus-deriving-finite-sphere-packings_images/imageFile872.png>)

![image 873](<2010-arkus-deriving-finite-sphere-packings_images/imageFile873.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.67307R2<br><br>|Cs|1| |






0 0 0 0 −1.6330 0 1.5327 −1.0695 0 0.3399 −0.2722 −0.9002 −0.2039 −0.8165 0.5401 0.8367 −1.5426 0.5401 1.1600 −0.8444 −0.9002 −0.3658 −0.8165 −0.4467 0.8926 −1.6946 −0.4467 0.5697 −0.8165 −0.0935

C :

R

 

 

Packing 215 (Graph 618718):





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 1 1 1 1 1 1 1 1 0 1 0

A :

 

 





- 0 1.4452 1.9301 1 1 1.9297 1.4460 1 1.7311 0 1.4452 0 1.6330 1.0887 1 1 1.6667 1 1 0 1.9301 1.6330 0 1.6330 1.9301 1 1 2.2913 1 0
- 1 1.0887 1.6330 0 1.4452 1.6667 1 1 1 0 1 1 1.9301 1.4452 0 1.4460 1.9297 1 1.7311 0


D :

R

1.9297 1 1 1.6667 1.4460 0 1.6330 1.9121 1 0 1.4460 1.6667 1 1 1.9297 1.6330 0 1.9121 1 0

1 1 2.2913 1 1 1.9121 1.9121 0 1.6767 0 1.7311 1 1 1 1.7311 1 1 1.6767 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 874](<2010-arkus-deriving-finite-sphere-packings_images/imageFile874.png>)

![image 875](<2010-arkus-deriving-finite-sphere-packings_images/imageFile875.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.52721R2|Cs<br><br>|1|new seed|






0 0 0 0 1.4452 0 1.5936 1.0888 0 0.1959 0.6585 −0.7266 −0.1800 0.7226 0.6674 0.8858 1.6650 0.4087 1.1797 0.4849 −0.6812 −0.6584 0.7226 −0.2107 0.8296 1.4135 −0.5575 0.6751 0.7226 0.1488

C :

R

 

 

Packing 216 (Graph 618763):





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1 1 0 1 0

A :

 

 





0 1.6180 1.7566 1 1 1.9843 1.2019 1 1.6180 0

- 1.6180 0 1.6330 1.6180 1 1 1.9843 1 1 0 1.7566 1.6330 0 1.1220 1.9889 1 1 1.7007 1 0

1 1.6180 1.1220 0 1.6180 1.6779 1 1 1 0 1 1 1.9889 1.6180 0 1.6779 1.8055 1 1.6180 0

1.9843 1 1 1.6779 1.6779 0 1.6927 1.6532 1 0 1.2019 1.9843 1 1 1.8055 1.6927 0 1.7258 1.5940 0

1 1 1.7007 1 1 1.6532 1.7258 0 1 0

- 1.6180 1 1 1 1.6180 1 1.5940 1 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

![image 876](<2010-arkus-deriving-finite-sphere-packings_images/imageFile876.png>)

![image 877](<2010-arkus-deriving-finite-sphere-packings_images/imageFile877.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.13829R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6180 0 1.4849 −0.9385 0 0.7565 −0.3090 0.5764 −0.4676 −0.8090 −0.3562 0.9431 −1.7168 −0.3175 1.1643 −0.0387 −0.2958 −0.1095 −0.8090 0.5775 0.7565 −1.3090 0.5764 0.5277 −0.8090 −0.2589

C :

R

 

 

Packing 217 (Graph 618802):





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 1 1 0 1 1 0 0 1 1 1 0 1 1 1 1 1 1 1 0 1 1 0

A :

 

 





- 0 1.6330 1.7778 1 1 1.9907 1.9746 1 1.6667 0 1.6330 0 1.6330 1.6667 1 1 1.9746 1 1 0 1.7778 1.6330 0 1.1529 1.9907 1 1 1.6667 1 0
- 1 1.6667 1.1529 0 1.6330 1.7249 1 1 1.0887 0 1 1 1.9907 1.6330 0 1.6667 2.3745 1 1.6330 0


D :

R

1.9907 1 1 1.7249 1.6667 0 1.7089 1.6330 1 0 1.9746 1.9746 1 1 2.3745 1.7089 0 1.6219 1 0

1 1 1.6667 1 1 1.6330 1.6219 0 1 0 1.6667 1 1 1.0887 1.6330 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 878](<2010-arkus-deriving-finite-sphere-packings_images/imageFile878.png>)

![image 879](<2010-arkus-deriving-finite-sphere-packings_images/imageFile879.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.64354R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 1.4913 −0.9677 0 0.7726 −0.2722 −0.5735 −0.4636 −0.8165 0.3441 0.9345 −1.7237 0.3441 1.5017 −0.8165 −0.9884 −0.0662 −0.8165 −0.5735 0.7726 −1.3608 −0.5735 0.5298 −0.8165 0.2294

C :

R

 

 

Packing 218 (Graph 618803):





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 0 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 0 0 1 1 1 0 1 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1.9956 1 1 2.4249 1.6859 1 1.6667 0 1.6330 0 1.1471 1.6667 1 1 1.6859 1 1 0 1.9956 1.1471 0 1.6667 1.7622 1 1 1.6859 1 0
- 1 1.6667 1.6667 0 1.6330 2.0624 1 1 1.0887 0 1 1 1.7622 1.6330 0 1.9819 1.9868 1 1.6330 0


D :

R

2.4249 1 1 2.0624 1.9819 0 1.6977 1.6977 1 0 1.6859 1.6859 1 1 1.9868 1.6977 0 1.6059 1 0

1 1 1.6859 1 1 1.6977 1.6059 0 1 0 1.6667 1 1 1.0887 1.6330 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 880](<2010-arkus-deriving-finite-sphere-packings_images/imageFile880.png>)

![image 881](<2010-arkus-deriving-finite-sphere-packings_images/imageFile881.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.73109R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.1471

- −1.6330 0

−0.5735 −0.2722 −0.7726 0.3441 −0.8165 0.4636 −0.5735

- −2.3107 −0.4601 −1.3765 −0.8165 −0.5298


C :

R

0.2294 −0.8165 −0.5298 −0.5735 −1.3608 −0.7726 −0.5735 −0.8165 0

 

 

###### **Packing 219 (Graph 618804):





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 0 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 2.4487 1 1 1.9907 1.6859 1 1.6667 0 1.6330 0 1.6977 1.6667 1 1 1.6859 1 1 0 2.4487 1.6977 0 1.7539 2.4249 1 1 1.9819 1 0
- 1 1.6667 1.7539 0 1.6330 1.7249 1 1 1.0887 0 1 1 2.4249 1.6330 0 1.6667 1.9868 1 1.6330 0


D :

R

1.9907 1 1 1.7249 1.6667 0 1.1471 1.6330 1 0 1.6859 1.6859 1 1 1.9868 1.1471 0 1.6059 1 0

1 1 1.9819 1 1 1.6330 1.6059 0 1 0 1.6667 1 1 1.0887 1.6330 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 882](<2010-arkus-deriving-finite-sphere-packings_images/imageFile882.png>)

![image 883](<2010-arkus-deriving-finite-sphere-packings_images/imageFile883.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.89226R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.6922 1.7700 0 0.8737 0.2722 0.4032 −0.5242 0.8165 −0.2419 0.8443 1.7237 −0.5281 1.4620 0.8165 −0.1947 0 0.8165 0.5750 0.8737 1.3608 0.4032 0.4716 0.8165 −0.3330

C :

R

 

 

Packing 220 (Graph 619044):





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 1 0 0 1 0

A :

 

 





- 0 1.6180 1.7566 1 1 1.9843 1.9843 1 1.6180 0 1.6180 0 1.6330 1.6180 1 1 1.9843 1 1 0 1.7566 1.6330 0 1.1220 1.9889 1 1 1.7007 1 0
- 1 1.6180 1.1220 0 1.6180 1.6779 1 1 1 0 1 1 1.9889 1.6180 0 1.6779 2.3985 1 1.6180 0


D :

R

1.9843 1 1 1.6779 1.6779 0 1.6927 1.6532 1 0 1.9843 1.9843 1 1 2.3985 1.6927 0 1.6781 1 0

1 1 1.7007 1 1 1.6532 1.6781 0 1 0 1.6180 1 1 1 1.6180 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 884](<2010-arkus-deriving-finite-sphere-packings_images/imageFile884.png>)

![image 885](<2010-arkus-deriving-finite-sphere-packings_images/imageFile885.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.62060R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6180 0 −1.4849 0.9385 0 −0.7565 0.3090 0.5764 0.4676 0.8090 −0.3562 −0.9431 1.7168 −0.3175 −1.5168 0.8090 0.9911 0.1095 0.8090 0.5775 −0.7565 1.3090 0.5764 −0.5277 0.8090 −0.2589

C :

R

 

 

Packing 221 (Graph 619047):





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 0 1 0

A :

 

 





- 0 1.6180 2.4256 1 1 1.9843 1.6779 1 1.6180 0 1.6180 0 1.6927 1.6180 1 1 1.6779 1 1 0 2.4256 1.6927 0 1.6927 2.4256 1 1 1.9910 1 0
- 1 1.6180 1.6927 0 1.6180 1.6779 1 1 1 0 1 1 2.4256 1.6180 0 1.6779 1.9843 1 1.6180 0


D :

R

1.9843 1 1 1.6779 1.6779 0 1.1220 1.6532 1 0 1.6779 1.6779 1 1 1.9843 1.1220 0 1.6532 1 0

1 1 1.9910 1 1 1.6532 1.6532 0 1 0 1.6180 1 1 1 1.6180 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 886](<2010-arkus-deriving-finite-sphere-packings_images/imageFile886.png>)

![image 887](<2010-arkus-deriving-finite-sphere-packings_images/imageFile887.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.80603R2|Cs<br><br>|1| |






0 0 0 0 −1.6180 0 −1.6882 −1.7417 0 −0.8713 −0.3090 −0.3813 0.5385

- −0.8090 0.2357

−0.8414 −1.7168 0.5313

- −1.4456 −0.8090


C :

R

0.2669 −0.0300 −0.8090 −0.5870 −0.8713 −1.3090 −0.3813 −0.4516 −0.8090 0.3762

 

 

Packing 222 (Graph 619264):





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 1 0 1 1 0 0 0 0 1 1 1 0 0 1 1 0 0 0 0 1 1 1 1 0 1 0 1 0 0 1 1 0 0 1 1 0 1 1 1 0 0 1 1 1 1 1 1 1 1 0 0

A :

 

 





- 0 1.1220 1.9843 1 1 1.6779 1.6779 1 1.6532 0 1.1220 0 1.6779 1.6779 1 1 1.9843 1 1.6532 0 1.9843 1.6779 0 1.6180 1.8414 1 1 1.6180 1 0
- 1 1.6779 1.6180 0 1.6927 1.6180 1 1 1 0 1 1 1.8414 1.6927 0 1.6927 1.8414 1.5940 2.0314 0


D :

R

1.6779 1 1 1.6180 1.6927 0 1.6180 1 1 0 1.6779 1.9843 1 1 1.8414 1.6180 0 1.6180 1 0

1 1 1.6180 1 1.5940 1 1.6180 0 1 0 1.6532 1.6532 1 1 2.0314 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 888](<2010-arkus-deriving-finite-sphere-packings_images/imageFile888.png>)

![image 889](<2010-arkus-deriving-finite-sphere-packings_images/imageFile889.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.32372R2<br><br>|Cs|1| |






0 0 0 0 1.1220 0 −1.6768 1.0610 0 −0.8486 −0.2480 −0.4674 −0.1063 0.5610 0.8210 −0.8486 1.3700 −0.4674 −1.6768 0 −0.0000 −0.3366 0.5610 −0.7563 −1.3359 0.5610 −0.7961 −0.8191 0.5610 0.1197

C :

R

 

 

###### *Packing 223 (Graph 622056):





0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 0 0 1 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.6330 1.4142 1 1 1.9149 1 1 1 0 1.6330 0 1.4142 2.5166 1 1 1.9149 1 1.9149 0 1.4142 1.4142 0 1.7321 1.7321 1 1 1 1 0
- 1 2.5166 1.7321 0 2.0000 2.5166 1 1.7321 1 0 1 1 1.7321 2.0000 0 1.7321 1.7321 1 1.7321 0


D :

R

1.9149 1 1 2.5166 1.7321 0 1.6330 1.4142 1.9149 0 1 1.9149 1 1 1.7321 1.6330 0 1.4142 1 0 1 1 1 1.7321 1 1.4142 1.4142 0 1 0 1 1.9149 1 1 1.7321 1.9149 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 890](<2010-arkus-deriving-finite-sphere-packings_images/imageFile890.png>)

![image 891](<2010-arkus-deriving-finite-sphere-packings_images/imageFile891.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.16667R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.1547 −0.8165 0 −0.5774 0.8165 −0.0000 0.5774 −0.8165 0 −0.8660 −1.6330 −0.5000 −0.8660 0 −0.5000 −0.2887 −0.8165 0.5000 −0.8660 0 0.5000 −0.2887 −0.8165 −0.5000

C :

R

 

 

Packing 224 (Graph 622541):





0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 0 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.1832 1.6796 1 1 1.7496 1 1 1 0 1.1832 0 1.6330 1.6667 1 1 1.6667 1 1 0 1.6796 1.6330 0 1.6938 2.3501 1 1 1.9667 1 0
- 1 1.6667 1.6938 0 1.7159 1.9838 1 1 1.5920 0 1 1 2.3501 1.7159 0 1.9633 1.9443 1 1.5109 0


D :

R

1.7496 1 1 1.9838 1.9633 0 1.6330 1.7167 1 0 1 1.6667 1 1 1.9443 1.6330 0 1.5920 1 0 1 1 1.9667 1 1 1.7167 1.5920 0 1.5345 0 1 1 1 1.5920 1.5109 1 1 1.5345 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 892](<2010-arkus-deriving-finite-sphere-packings_images/imageFile892.png>)

![image 893](<2010-arkus-deriving-finite-sphere-packings_images/imageFile893.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.55170R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.1832 0 −1.5458 0.6569 0 −0.3758 −0.1596 −0.9128 0.8019 0.5916 0 −0.9577 1.4626 0 −0.9803 −0.1596 −0.1162 0.2665 0.5916 −0.7609 −0.6611 0.5916 0.4615 −0.7000 0.7060 −0.5312

C :

R

 

 

Packing 225 (Graph 622587):





0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 1 1 1 1 0 1 1 1 0 1 0

A :

 

 





- 0 1.4325 1.7317 1 1 1.9053 1 1 1.3951 0 1.4325 0 1.6330 1.4730 1 1 1.6667 1 1 0 1.7317 1.6330 0 1.7318 1.9907 1 1 2.1334 1 0
- 1 1.4730 1.7318 0 1.6667 1.9237 1 1 1 0 1 1 1.9907 1.6667 0 1.6668 1.7246 1 1.6328 0


D :

R

1.9053 1 1 1.9237 1.6668 0 1.6330 1.8846 1 0 1 1.6667 1 1 1.7246 1.6330 0 1.6328 1 0 1 1 2.1334 1 1 1.8846 1.6328 0 1.3524 0

 

 

1.3951 1 1 1 1.6328 1 1 1.3524 0 0 0 0 0 0 0 0 0 0 0 0

![image 894](<2010-arkus-deriving-finite-sphere-packings_images/imageFile894.png>)

![image 895](<2010-arkus-deriving-finite-sphere-packings_images/imageFile895.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.33646R2<br><br>|C1|1|chiral new seed<br><br>|






0 0 0 0 −1.4325 0 −1.5187 −0.8322 0 −0.1604 −0.3080 −0.9378 0.3807 −0.7163 0.5849 −0.9577 −1.6343 0.2051 −0.9349 −0.0958 −0.3418 0.5744 −0.7163 −0.3962 −0.7254 −1.0466 −0.5699 −0.5948 −0.7163 0.3649

C :

R

 

 

###### *Packing 226 (Graph 627354):





0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 1 0 0 1 1 0 0 1 1 0 1 1 1 0 0 1 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.5224 1.7199 1 1 1.7199 1 1 1.5130 0 1.5224 0 1.7221 1.9591 1 1 1.8799 1 1.7204 0 1.7199 1.7221 0 1.7199 1.9995 1 1 1.5130 1 0
- 1 1.9591 1.7199 0 1.8733 1.7199 1 1 1 0 1 1 1.9995 1.8733 0 1.7176 1.7243 1.2737 2.0579 0


D :

R

1.7199 1 1 1.7199 1.7176 0 1.5130 1 1 0 1 1.8799 1 1 1.7243 1.5130 0 1.2892 1 0 1 1 1.5130 1 1.2737 1 1.2892 0 1 0

 

 

1.5130 1.7204 1 1 2.0579 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 896](<2010-arkus-deriving-finite-sphere-packings_images/imageFile896.png>)

![image 897](<2010-arkus-deriving-finite-sphere-packings_images/imageFile897.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.32168R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.5224 0 1.5435 −0.7587 0 0.4079 0.1709 0.8969 −0.3870 −0.7612 −0.5204 0.9023 −1.4043 0.4147 0.9932 0 0 0.1665 −0.7612 0.6268 1.1100 −0.5409 0.8744 0.5841 −0.7612 −0.2818

C :

R

 

 

Packing 227 (Graph 629072):





0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 1 0 0 1 1 1 1 0 1 1 0 0 1 0 0 1 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.5723 1.6848 1 1 1.9490 1 1.4722 1 0 1.5723 0 1.6330 1.6881 1 1 1.9006 1 1 0 1.6848 1.6330 0 1.3774 1.9788 1 1 1 1.7800 0
- 1 1.6881 1.3774 0 1.6881 1.8602 1 1 1 0 1 1 1.9788 1.6881 0 1.7032 1.7283 1.5723 1 0


D :

R

1.9490 1 1 1.8602 1.7032 0 1.7314 1 1.6942 0 1 1.9006 1 1 1.7283 1.7314 0 1.3859 1.6042 0

1.4722 1 1 1 1.5723 1 1.3859 0 1 0 1 1 1.7800 1 1 1.6942 1.6042 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 898](<2010-arkus-deriving-finite-sphere-packings_images/imageFile898.png>)

![image 899](<2010-arkus-deriving-finite-sphere-packings_images/imageFile899.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.14597R2<br><br>|C1|1|chiral new seed<br><br>|






0 0 0 0 −1.5723 0 1.4600 −0.8408 0 0.5508 −0.1980 0.8108 −0.4791 −0.7862 −0.3904 0.9653 −1.6761 −0.2397 0.9977 0 −0.0502 0.7053 −1.1574 0.5747 −0.2232 −0.7862 0.5763 0.5194 −0.7862 −0.3350

C :

R

 

 

Packing 228 (Graph 630908):





0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 0 1 1 0 0 1 1 0 0 1 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.6330 1.5920 1 1 1.6667 1 1 1 0 1.6330 0 1.7167 2.4736 1 1 1.9838 1 1.7496 0 1.5920 1.7167 0 1.6938 1.9667 1 1 1.5345 1 0
- 1 2.4736 1.6938 0 1.9971 2.1333 1 1.6938 1 0 1 1 1.9667 1.9971 0 1.6330 1.6938 1 1.6796 0


D :

R

1.6667 1 1 2.1333 1.6330 0 1.6667 1 1.1832 0 1 1.9838 1 1 1.6938 1.6667 0 1.5920 1 0 1 1 1.5345 1.6938 1 1 1.5920 0 1 0 1 1.7496 1 1 1.6796 1.1832 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 900](<2010-arkus-deriving-finite-sphere-packings_images/imageFile900.png>)

![image 901](<2010-arkus-deriving-finite-sphere-packings_images/imageFile901.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.77019R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 −1.4346 0.6901 0 −0.5932 −0.7508 −0.2905 0.5090 0.8165 0.2726 −0.8483 1.3608 −0.4543 −0.9229 −0.0823 0.3761 −0.0184 0.8165 −0.5771 −0.7941 0.1854 −0.5788 −0.4905 0.8165 0.3045

C :

R

 

 

###### *Packing 229 (Graph 631053):





0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 0 1 0 1 0 0 1 1 1 0 0 1 1 1 1 1 1 1 0 0 0

A :

 

 





- 0 1.6071 1.6071 1 1 1.5827 1 1 1 0 1.6071 0 1.6981 1.8040 1 1 1.9707 1 1.6426 0 1.6071 1.6981 0 1.6851 1.9707 1 1 1.6426 1 0
- 1 1.8040 1.6851 0 1.1894 1.9778 1 1.7373 1.6655 0 1 1 1.9707 1.1894 0 1.6071 1.6981 1 1.6426 0


D :

R

1.5827 1 1 1.9778 1.6071 0 1.6071 1 1 0 1 1.9707 1 1 1.6981 1.6071 0 1.6426 1 0 1 1 1.6426 1.7373 1 1 1.6426 0 1 0 1 1.6426 1 1.6655 1.6426 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 902](<2010-arkus-deriving-finite-sphere-packings_images/imageFile902.png>)

![image 903](<2010-arkus-deriving-finite-sphere-packings_images/imageFile903.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.07299R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6071 0 −1.4418 −0.7099 0 −0.2074 −0.1021 0.9729 0.5000 −0.8035 0.3230 −0.7913 −1.2717 −0.5112 −0.9418 0 0.3230 0 −0.8035 −0.5886 −0.7601 −0.2752 −0.5886 −0.5000 −0.8035 0.3230

C :

R

 

 

Packing 230 (Graph 632638):





0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 1 1 0 1 1 0 0 1 1 0 0 1 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.7167 1.5920 1 1 1.9667 1 1.5345 1 0 1.7167 0 1.6330 2.5151 1 1 1.9838 1 1.7496 0 1.5920 1.6330 0 1.6938 1.6667 1 1 1 1 0
- 1 2.5151 1.6938 0 1.8000 2.4704 1 1.9667 1 0 1 1 1.6667 1.8000 0 1.6330 1.6667 1 1.1832 0


D :

R

1.9667 1 1 2.4704 1.6330 0 1.6938 1 1.6796 0 1 1.9838 1 1 1.6667 1.6938 0 1.5920 1 0

1.5345 1 1 1.9667 1 1 1.5920 0 1 0 1 1.7496 1 1 1.1832 1.6796 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 904](<2010-arkus-deriving-finite-sphere-packings_images/imageFile904.png>)

![image 905](<2010-arkus-deriving-finite-sphere-packings_images/imageFile905.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.97114R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7167 0 1.3647 −0.8199 0 0.6600 0.6928 0.2905 −0.2384 −0.8584 0.4543 0.9619 −1.6936 −0.2726 0.9266 −0.0034 −0.3761 0.6722 −1.2529 0.5771 0.7736 −0.2580 0.5788 0.4129 −0.8584 −0.3045

C :

R

 

 

Packing 231 (Graph 632698):





0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 0 1 0 1 0 1 0 1 1 0 0 1 1 1 1 1 1 1 0 0 0

A :

 

 





- 0 1.6981 1.6071 1 1 1.9707 1 1.6426 1 0 1.6981 0 1.6071 1.8625 1 1 1.9707 1 1.6426 0 1.6071 1.6071 0 1.6851 1.5827 1 1 1 1 0
- 1 1.8625 1.6851 0 1.6851 1.8625 1 2.0561 1.6655 0 1 1 1.5827 1.6851 0 1.6071 1.6071 1 1 0


D :

R

1.9707 1 1 1.8625 1.6071 0 1.6981 1 1.6426 0 1 1.9707 1 1 1.6071 1.6981 0 1.6426 1 0

1.6426 1 1 2.0561 1 1 1.6426 0 1 0 1 1.6426 1 1.6655 1 1.6426 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 906](<2010-arkus-deriving-finite-sphere-packings_images/imageFile906.png>)

![image 907](<2010-arkus-deriving-finite-sphere-packings_images/imageFile907.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.31359R2|Cs<br><br>|1| |






0 0 0 0 −1.6981 0 −1.3645 −0.8490 0 −0.1963 −0.1221 0.9729 0.1334 −0.8490 −0.5112 −0.9464 −1.6981 0.3230 −0.9464 0 0.3230 −0.7292 −1.3490 −0.5886 −0.7292 −0.3490 −0.5886 −0.4181 −0.8490 0.3230

C :

R

 

 

Packing 232 (Graph 632806):





0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 1 0 1 0 1 1 1 0 1 1 0 0 1 1 1 0 1 1 1 0 0 0

A :

 

 





- 0 1.6981 1.6071 1 1 1.9707 1 1.6426 1 0 1.6981 0 1.6071 2.4548 1 1 1.9707 1 1.6426 0 1.6071 1.6071 0 1.6851 1.5827 1 1 1 1 0
- 1 2.4548 1.6851 0 1.6851 2.4548 1 1.9899 1 0 1 1 1.5827 1.6851 0 1.6071 1.6071 1 1 0


D :

R

1.9707 1 1 2.4548 1.6071 0 1.6981 1 1.6426 0 1 1.9707 1 1 1.6071 1.6981 0 1.6426 1 0

1.6426 1 1 1.9899 1 1 1.6426 0 1 0 1 1.6426 1 1 1 1.6426 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 908](<2010-arkus-deriving-finite-sphere-packings_images/imageFile908.png>)

![image 909](<2010-arkus-deriving-finite-sphere-packings_images/imageFile909.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.79829R2<br><br>|Cs|1| |






0 0 0 0 −1.6981 0 −1.3645 −0.8490 0 −0.6648 0.6309 −0.4000 0.1334 −0.8490 −0.5112 −0.9464 −1.6981 0.3230 −0.9464 0 0.3230 −0.7292 −1.3490 −0.5886 −0.7292 −0.3490 −0.5886 −0.4181 −0.8490 0.3230

C :

R

 

 

###### *Packing 233 (Graph 633829):





0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 0 1 1 1 0 0 1 1 1 0 0 1 1 0 0 1 1 0 1 1 1 0 0 1 1 1 0 1 1 1 1 0 0

A :

 

 





- 0 1.7176 1.7199 1 1 1.7199 1 1 1.5130 0 1.7176 0 1.6453 2.1910 1 1 1.9552 1.2737 1.8398 0 1.7199 1.6453 0 1.7199 1.9591 1 1 1.5130 1 0
- 1 2.1910 1.7199 0 1.7221 1.7199 1 1 1 0 1 1 1.9591 1.7221 0 1.5224 1.7204 1 1.8799 0


D :

R

1.7199 1 1 1.7199 1.5224 0 1.5130 1 1 0 1 1.9552 1 1 1.7204 1.5130 0 1.2892 1 0 1 1.2737 1.5130 1 1 1 1.2892 0 1 0

 

 

1.5130 1.8398 1 1 1.8799 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 910](<2010-arkus-deriving-finite-sphere-packings_images/imageFile910.png>)

![image 911](<2010-arkus-deriving-finite-sphere-packings_images/imageFile911.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.32168R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 1.7176 0 −1.4456 0.9320 0 −0.5054 −0.2475 −0.8266 0.5121 0.8588 0 −0.7793 1.4288 −0.5561 −0.9993 0 −0.0050 −0.1404 0.6776 −0.7219 −1.1211 0.5398 −0.8608 −0.4695 0.8588 0.2049

C :

R

 

 

Packing 234 (Graph 663203):





0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 1 1 0 0 1 1 0 0 0 0 1 1 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 1 0 0 0 1 0 1 1 0 1 1 1 0 0 0 1 0 1 1 0 1 1 1 0 0

A :

 

 





- 0 1.7247 1.7247 1 1 1.6507 1 1 1.6507 0 1.7247 0 1.7247 1.9937 1 1 1.6507 1 1 0 1.7247 1.7247 0 1.9937 1.6507 1 1 1.6507 1 0
- 1 1.9937 1.9937 0 1.7321 1.6507 1.7321 1 2.1736 0 1 1 1.6507 1.7321 0 1.4142 1 1 1 0


D :

R

- 1.6507 1 1 1.6507 1.4142 0 1.4142 1 1 0 1 1.6507 1 1.7321 1 1.4142 0 1.4142 1 0 1 1 1.6507 1 1 1 1.4142 0 1.4142 0
- 1.6507 1 1 2.1736 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0


 

 

![image 912](<2010-arkus-deriving-finite-sphere-packings_images/imageFile912.png>)

![image 913](<2010-arkus-deriving-finite-sphere-packings_images/imageFile913.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.26717R2<br><br>|Cs|1| |






0 0 0 0 1.7247 0 1.4937 0.8624 0 −0.0000 −0.0000 −1.0000 −0.0795 0.8624 0.5000 0.7866 1.3624 −0.5000 0.7866 0.3624 0.5000 −0.0795 0.8624 −0.5000 0.7866 1.3624 0.5000 0.7866 0.3624 −0.5000

C :

R

 

 

Packing 235 (Graph 665570):





0 0 0 1 1 0 0 0 1 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 0 0 1 0 1 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 1 1 1 0 1 0 1 0 0 0 1 1 1 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.4144 2.0000 1 1 1.7321 1.7321 1.7321 1 0 1.4144 0 1.4140 1.7321 1 1 1 1.7321 1 0 2.0000 1.4140 0 1.7321 1.7321 1 1 1 1.7321 0
- 1 1.7321 1.7321 0 1.7321 1.4140 2.0000 1 1 0 1 1 1.7321 1.7321 0 1.7321 1 2.0000 1.4140 0


D :

R

1.7321 1 1 1.4140 1.7321 0 1.4144 1 1 0 1.7321 1 1 2.0000 1 1.4144 0 1.7321 1.7321 0 1.7321 1.7321 1 1 2.0000 1 1.7321 0 1.4144 0

 

 

1 1 1.7321 1 1.4140 1 1.7321 1.4144 0 0 0 0 0 0 0 0 0 0 0 0

![image 914](<2010-arkus-deriving-finite-sphere-packings_images/imageFile914.png>)

![image 915](<2010-arkus-deriving-finite-sphere-packings_images/imageFile915.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.40000R2<br><br>|C3v|3<br><br>|new seed non-rigid|






0 0 0 0 1.4145 0 −1.4140 1.4145 0 −0.7070 0 0.7072 0 0.7072 −0.7070 −0.7070 1.4142 0.7072 −0.7070 1.4142 −0.7072 −1.4142 0.7072 0.7070 0 0.7072 0.7070 −0.7070 0.7072 0

C :

R

 

 

###### *Packing 236 (Graph 668570):





0 0 0 1 1 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 0 1 0 1 1 0 0 1 1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 0 1 1 1 1 1 0 1 0

A :

 

 





- 0 1.7204 1.9998 1 1 1.7221 1.7221 2.3494 1 0 1.7204 0 1.5130 1.8479 1 1 1 1 1 0 1.9998 1.5130 0 1.7359 1.7199 1 1 1 1.7199 0
- 1 1.8479 1.7359 0 1.6330 1.2992 1.9587 2.2105 1 0 1 1 1.7199 1.6330 0 1.5130 1 1.7199 1 0


D :

R

1.7221 1 1 1.2992 1.5130 0 1.2892 1 1 0

- 1.7221 1 1 1.9587 1 1.2892 0 1 1.5130 0
- 2.3494 1 1 2.2105 1.7199 1 1 0 1.7199 0 1 1 1.7199 1 1 1 1.5130 1.7199 0 0 0 0 0 0 0 0 0 0 0 0


 

 

![image 916](<2010-arkus-deriving-finite-sphere-packings_images/imageFile916.png>)

![image 917](<2010-arkus-deriving-finite-sphere-packings_images/imageFile917.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.62289R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.7204 0 1.4687 −1.3572 0 0.5296 −0.1585 0.8333 −0.1001

- −0.8602 −0.5000

0.7078 −1.4315 0.6446 0.7078

- −1.4315 −0.6446

0.8914

- −2.1737 0


C :

R

−0.1001 −0.8602 0.5000 0.7443 −0.6678 0

 

 

###### *Packing 237 (Graph 679344):





0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 1 0 1 1 0 0 0 1 0 0 1 1 0 1 1 0 0 0 1 1 1 0 1 0 1 1 0 0 1 1 0 1 0 1 1 0 1 1 0

A :

 

 





- 0 1.5130 1.9998 1 1 1.7199 1 1.7199 1 0 1.5130 0 1.7204 1.7221 1 1 1 1 1 0 1.9998 1.7204 0 2.6277 1.7221 1 2.3494 1 1.7221 0
- 1 1.7221 2.6277 0 1.7204 1.9998 1 2.3494 1 0 1 1 1.7221 1.7204 0 1.5130 1 1 1.2892 0


D :

R

- 1.7199 1 1 1.9998 1.5130 0 1.7199 1 1 0 1 1 2.3494 1 1 1.7199 0 1.7199 1 0
- 1.7199 1 1 2.3494 1 1 1.7199 0 1.5130 0 1 1 1.7221 1 1.2892 1 1 1.5130 0 0 0 0 0 0 0 0 0 0 0 0


 

 

![image 918](<2010-arkus-deriving-finite-sphere-packings_images/imageFile918.png>)

![image 919](<2010-arkus-deriving-finite-sphere-packings_images/imageFile919.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.20380R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 1.5130 0 1.6701 1.0999 0 −0.6409 0.1069 −0.7602 0.1105 0.7565 0.6446 0.8591 1.4036 −0.5000 −0.6540 0.7565 0 0.8591 1.4036 0.5000 0.1105 0.7565 −0.6446 0.8431 0.5377 −0.0000

C :

R

 

 

Packing 238 (Graph 679397):





0 0 0 1 1 0 1 0 0 1 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 1 0 0 1 1 0 1 1 0 0 0 1 0 1 1 1 0 1 1 0 0 1 1 0 1 1 1 0 0 1 1 0

A :

 

 





- 0 1.7055 1.9735 1 1 2.2941 1 1.7319 1.5476 0 1.7055 0 1.5476 1.7055 1 1 1 1 1 0 1.9735 1.5476 0 1.5895 1.7055 1 1.8339 1 1 0
- 1 1.7055 1.5895 0 1.5476 1.9735 1 1.8339 1 0 1 1 1.7055 1.5476 0 1.7055 1 1 1.3951 0


D :

R

2.2941 1 1 1.9735 1.7055 0 1.7319 1 1 0

1 1 1.8339 1 1 1.7319 0 1.5711 1 0 1.7319 1 1 1.8339 1 1 1.5711 0 1.2278 0 1.5476 1 1 1 1.3951 1 1 1.2278 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 920](<2010-arkus-deriving-finite-sphere-packings_images/imageFile920.png>)

![image 921](<2010-arkus-deriving-finite-sphere-packings_images/imageFile921.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.28961R2<br><br>|C2|2<br><br>|chiral new seed|






0 0 0 0 −1.7055 0 −1.4915 −1.2924 0 −0.5398 −0.2932 0.7891 0 −0.8527 −0.5172 −0.9129 −2.1025 0 0.2255 −0.8527 0.4711 −0.7291 −1.4389 −0.6304 −0.6800 −1.2618 0.5836 −0.8072 −0.5753 −0.1323

C :

R

 

 

Packing 239 (Graph 685049):





0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 0 1 1 0 0 0 0 1 1 1 0 0 1 1 1 0 0 0 0 1 1 1 0 1 1 1 0 0

A :

 

 





- 0 1.4142 1.9300 1 1 1.6507 1 1 1 0 1.4142 0 1.7321 1.6507 1 1 1.4142 1 1 0 1.9300 1.7321 0 1.5000 2.3874 1 1 1.9300 1.7321 0
- 1 1.6507 1.5000 0 1.7247 1.7247 1 1 1.6507 0 1 1 2.3874 1.7247 0 1.7247 1.6507 1 1 0


D :

R

1.6507 1 1 1.7247 1.7247 0 1 1.6507 1 0 1 1.4142 1 1 1.6507 1 0 1.4142 1 0 1 1 1.9300 1 1 1.6507 1.4142 0 1.4142 0 1 1 1.7321 1.6507 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 922](<2010-arkus-deriving-finite-sphere-packings_images/imageFile922.png>)

![image 923](<2010-arkus-deriving-finite-sphere-packings_images/imageFile923.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.26717R2|Cs<br><br>|1| |






0 0 0 0 1.4142 0 −1.6723 0.9633 0 −0.6838 0 0.7231 0.6988 0.7071 −0.1083 −0.8707 1.3169 −0.4821 −0.9100 0.3536 −0.2167 0.1083 0.7071 0.6988 −0.1083 0.7071 −0.6988 −0.8016 1.0607 0.4821

C :

R

 

 

Packing 240 (Graph 714961):





0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 1 0 0 1 0 1 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 0 1 0 1 0 1 0 1 1 0 0 0 1 1 1 1 1 1 0 0 0

A :

 

 





- 0 1.6492 1.6492 1 1.6034 1 1 1 1 0 1.6492 0 1.7200 1.7200 1 1 1.9241 1 1.6492 0 1.6492 1.7200 0 1.7200 1 1.9241 1 1.6492 1 0
- 1 1.7200 1.7200 0 1.9241 1 1 1.6492 1.6492 0


1.6034 1 1 1.9241 0 1.5710 1.5710 1 1 0 1 1 1.9241 1 1.5710 0 1.5710 1 1.6034 0 1 1.9241 1 1 1.5710 1.5710 0 1.6034 1 0 1 1 1.6492 1.6492 1 1 1.6034 0 1 0 1 1.6492 1 1.6492 1 1.6034 1 1 0 0 0 0 0 0 0 0 0 0 0 0

D :

R

 

 

![image 924](<2010-arkus-deriving-finite-sphere-packings_images/imageFile924.png>)

![image 925](<2010-arkus-deriving-finite-sphere-packings_images/imageFile925.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|7.95849R2<br><br>|C3v|3<br><br>|new seed|






0 0 0 0 −1.6492 0 1.4676 −0.7524 0 0.1411 −0.2309 −0.9627 0.7950 −1.3009 0.4967 −0.4166 −0.8246 −0.3827 0.9239 −0.0054 −0.3827 −0.0820 −0.8246 0.5597 0.7712 −0.3032 0.5597 0.5760 −0.9425 −0.4109

C :

R

 

 

Packing 241 (Graph 730317):





0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 1 0 0 0 0 0 1 1 0 0 0 1 1 0 0 1 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 1 0 1 1 0 1 1 0 1 0 1 1 0 0 1 1 1 0 0 1 1 1 0 0

A :

 

 





- 0 1.7221 1.7221 1 2.3494 1.9998 1 1 1.7204 0 1.7221 0 1.2892 1.9587 1 1 1 1.5130 1 0 1.7221 1.2892 0 1.9587 1 1 1.5130 1 1 0
- 1 1.9587 1.9587 0 2.4498 2.5054 1 1 1.5203 0 2.3494 1 1 2.4498 0 1 1.7199 1.7199 1 0 1.9998 1 1 2.5054 1 0 1.7199 1.7199 1.5130 0


D :

R

1 1 1.5130 1 1.7199 1.7199 0 1 1 0 1 1.5130 1 1 1.7199 1.7199 1 0 1 0

 

 

1.7204 1 1 1.5203 1 1.5130 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 926](<2010-arkus-deriving-finite-sphere-packings_images/imageFile926.png>)

![image 927](<2010-arkus-deriving-finite-sphere-packings_images/imageFile927.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.16529R2|Cs<br><br>|1| |






0 0 0 0 −1.7221 0 −1.1955 −1.2396 0 −0.0151 −0.0375 0.9992 −0.8772 −2.1732 0.1644 −0.6990 −1.7318 −0.7150 0.1916 −0.8611 0.4710 −0.7357 −0.4868 0.4710 −0.5772 −1.4301 0.7626 −0.3476 −0.8611 −0.3712

C :

R

 

 

Packing 242 (Graph 735131):





0 0 0 1 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 0 0 1 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.6330 1.4142 1 1 1.9149 1 1.9149 1 0 1.6330 0 1.4142 1.6667 1.9907 1 1 1 1 0 1.4142 1.4142 0 1.9149 1.4530 1 1.7321 1 1 0
- 1 1.6667 1.9149 0 1 2.3333 1 1.9437 1.6330 0 1 1.9907 1.4530 1 0 2.2526 1.6330 1.8156 1.6667 0


D :

R

1.9149 1 1 2.3333 2.2526 0 1.7321 1 1 0 1 1 1.7321 1 1.6330 1.7321 0 1.7321 1 0

1.9149 1 1 1.9437 1.8156 1 1.7321 0 1.4142 0 1 1 1 1.6330 1.6667 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 928](<2010-arkus-deriving-finite-sphere-packings_images/imageFile928.png>)

![image 929](<2010-arkus-deriving-finite-sphere-packings_images/imageFile929.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.92222R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6330 0 1.1547 0.8165 0 −0.4811 0.2722 −0.8333 0.4491 −0.0907 −0.8889 0.8660 1.6330 0.5000 −0.5774 0.8165 −0.0000 0.8660 1.6330 −0.5000 0.2887 0.8165 0.5000 0.2887 0.8165 −0.5000

C :

R

 

 

Packing 243 (Graph 735240):





0 0 0 1 1 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 1 0 1 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 0 1 0 0 0 1 1 1 0 1 1 1 1 0 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.7778 1 1 1.6667 1 1.9907 1 0 1.6330 0 1.6330 1.6667 1.9907 1 1 1 1 0 1.7778 1.6330 0 2.5035 2.2002 1 1.9907 1 1.6667 0
- 1 1.6667 2.5035 0 1 1.9907 1 2.4369 1 0 1 1.9907 2.2002 1 0 1.7778 1.6330 2.5035 1 0


D :

R

1.6667 1 1 1.9907 1.7778 0 1.6330 1 1 0 1 1 1.9907 1 1.6330 1.6330 0 1.6667 1 0

1.9907 1 1 2.4369 2.5035 1 1.6667 0 1.6330 0 1 1 1.6667 1 1 1 1 1.6330 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 930](<2010-arkus-deriving-finite-sphere-packings_images/imageFile930.png>)

![image 931](<2010-arkus-deriving-finite-sphere-packings_images/imageFile931.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.93759R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 1.6330 0 1.4913 0.9677 0 −0.8830 0.2722 −0.3824 −0.1692 −0.0907 −0.9814 0.7726 1.3608 −0.5735 −0.4636 0.8165 0.3441 0.9345 1.7237 0.3441 −0.0662 0.8165 −0.5735 0.5298 0.8165 0.2294

C :

R

 

 

###### *Packing 244 (Graph 736264):





0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 0 1 1 0 0 1 0 0 0 1 0 0 0 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 1 1 0 0 0 1 1 1 1 1 0 0 0 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 1 2.2361 1 1 1 0 1.7321 0 1.4142 1.7321 2.4495 1 1 1.7321 1 0 1.7321 1.4142 0 1.7321 2.0000 1 1.7321 1 1 0
- 1 1.7321 1.7321 0 1 2.0000 1 1 1.4142 0 1 2.4495 2.0000 1 0 2.6458 1.7321 1 1.7321 0


D :

R

2.2361 1 1 2.0000 2.6458 0 1.7321 1.7321 1.4142 0 1 1 1.7321 1 1.7321 1.7321 0 1.4142 1 0 1 1.7321 1 1 1 1.7321 1.4142 0 1 0 1 1 1 1.4142 1.7321 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 932](<2010-arkus-deriving-finite-sphere-packings_images/imageFile932.png>)

![image 933](<2010-arkus-deriving-finite-sphere-packings_images/imageFile933.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.30000R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.7321 0 1.2910 1.1547 0 0.1291 0.2887 0.9487 0.5164 −0.5774 0.6325 0.9037 2.0207 0.3162 −0.3873 0.8660 0.3162 0.9037 0.2887 0.3162 0.3873 0.8660 −0.3162 0.5164 1.1547 0.6325

C :

R

 

 

Packing 245 (Graph 736370):





0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 1 0 1 1 0 1 1 0 0 1 0 0 0 1 0 0 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 1 0 1 1 1 0 0 0 1 1 1 1 0 0 0 1 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.9149 1 1 1.9149 1 1 1 0 1.7321 0 1.7321 1.7321 2.4495 1 1 1.7321 1 0 1.9149 1.7321 0 1.6330 1.9149 1 1.9149 1 1.4142 0
- 1 1.7321 1.6330 0 1 1.9149 1 1 1.4142 0 1 2.4495 1.9149 1 0 2.3805 1.7321 1 1.7321 0


D :

R

1.9149 1 1 1.9149 2.3805 0 1.6330 1.4142 1 0 1 1 1.9149 1 1.7321 1.6330 0 1.4142 1 0 1 1.7321 1 1 1 1.4142 1.4142 0 1 0 1 1 1.4142 1.4142 1.7321 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 934](<2010-arkus-deriving-finite-sphere-packings_images/imageFile934.png>)

![image 935](<2010-arkus-deriving-finite-sphere-packings_images/imageFile935.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.03333R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.7321 0 −1.5957 −1.0585 0 −0.4352 −0.2887 −0.8528 −0.6963 0.5774 −0.4264 −0.8994 −1.6358 0.4264 0.2611 −0.8660 −0.4264 −0.9574 −0.2887 −0.0000 −0.2611 −0.8660 0.4264 −0.6963 −1.1547 −0.4264

C :

R

 

 

Packing 246 (Graph 736396):





0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 0 0 1 0 0 1 0 0 0 1 0 0 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 1 0 1 1 1 0 0 0 1 1 0 1 1 0 0 1 1 1 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.6859 1.6859 1 1 1.9868 1 1 1.6059 0 1.6859 0 1.6330 1.9770 2.4617 1 1 1.6667 1 0 1.6859 1.6330 0 1.9770 1.8421 1 1.6667 1 1 0
- 1 1.9770 1.9770 0 1 2.3778 1 1 1.5789 0 1 2.4617 1.8421 1 0 2.5356 1.6667 1 1.9770 0


D :

R

1.9868 1 1 2.3778 2.5356 0 1.6330 1.6330 1 0 1 1 1.6667 1 1.6667 1.6330 0 1.0887 1 0 1 1.6667 1 1 1 1.6330 1.0887 0 1 0

 

 

1.6059 1 1 1.5789 1.9770 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

![image 936](<2010-arkus-deriving-finite-sphere-packings_images/imageFile936.png>)

![image 937](<2010-arkus-deriving-finite-sphere-packings_images/imageFile937.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.49054R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.6859 0 1.4287 0.8950 0 −0.0109 −0.0197 0.9997 0.5691 −0.6578 0.4934 0.9505 1.7171 −0.3090 −0.1555 0.8429 0.5151 0.7969 0.3157 0.5151 0.7259 1.3112 0.5769 0.4666 0.8429 −0.2678

C :

R

 

 

Packing 247 (Graph 740549):





0 0 0 1 1 0 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 1 0 1 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 1 1 0 1 1 1 0 0 1 1 0 0 1 1 1 0 1 1 0 1 0 0 1 1 1 1 0 0 1 0 1 1 0

A :

 

 





- 0 1.4142 1.4142 1 1 1.7321 1 1 1 0 1.4142 0 1.6330 1.7321 1.9149 1 1 1 1 0 1.4142 1.6330 0 2.3805 2.1344 1 1.9149 1 1.9149 0
- 1 1.7321 2.3805 0 1 2.4495 1 1.7321 1 0 1 1.9149 2.1344 1 0 2.3805 1.6330 1.9149 1 0


D :

R

1.7321 1 1 2.4495 2.3805 0 1.7321 1 1.7321 0 1 1 1.9149 1 1.6330 1.7321 0 1 1 0 1 1 1 1.7321 1.9149 1 1 0 1.4142 0 1 1 1.9149 1 1 1.7321 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 938](<2010-arkus-deriving-finite-sphere-packings_images/imageFile938.png>)

![image 939](<2010-arkus-deriving-finite-sphere-packings_images/imageFile939.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.38889R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 −1.4142 0 −1.3333

- −0.4714 0

1.0000 0 0 0.5000 0.2357 0.8333

- −1.0000 −1.4142 −0.0000


C :

R

0.5000 −0.7071 −0.5000 −0.5000 −0.7071 −0.5000 0.5000 −0.7071 0.5000 −0.5000 −0.7071 0.5000

 

 

###### *Packing 248 (Graph 740809):





0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 1 0 1 0 1 0 1 0 0 1 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 1 1 0 1 1 1 0 0 1 1 0 0 1 0 1 0 1 1 1 1 0 0 1 1 0 1 0 1 1 0 1 1 0

A :

 

 





- 0 1.6426 1.6584 1 1 1.6426 1 1 1.0853 0 1.6426 0 1.6851 1.6981 1.9707 1 1 1 1 0 1.6584 1.6851 0 2.4108 1.9930 1 1.9778 1 1.6655 0
- 1 1.6981 2.4108 0 1 1.9707 1 1.6426 1 0 1 1.9707 1.9930 1 0 1.6981 1.6071 1.6426 1 0


D :

R

1.6426 1 1 1.9707 1.6981 0 1.6071 1 1 0 1 1 1.9778 1 1.6071 1.6071 0 1 1 0 1 1 1 1.6426 1.6426 1 1 0 1.0853 0

 

 

1.0853 1 1.6655 1 1 1 1 1.0853 0 0 0 0 0 0 0 0 0 0 0 0

![image 940](<2010-arkus-deriving-finite-sphere-packings_images/imageFile940.png>)

![image 941](<2010-arkus-deriving-finite-sphere-packings_images/imageFile941.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|8.55769R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6426 0 1.4559 −0.7941 0 −0.8432 −0.2480 0.4770 −0.0454 0 0.9974 0.7978 −1.3382 0.5204 −0.5034 −0.8213 −0.2685 0.4966 −0.8213 −0.2809 −0.0811 −0.8754 0.6363 0.7593 −0.3395 0.5551

C :

R

 

 

Packing 249 (Graph 743234):





0 0 0 1 1 0 0 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 0 0 1 0 1 1 0 0 1 0 0 0 1 0 0 0 1 1 0 0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 0 0 1 1 1 0

A :

 

 





- 0 1.6330 1.4142 1 1 1.9149 1.9149 1 1 0 1.6330 0 1.4142 1.6667 1.9907 1 1 1 1 0 1.4142 1.4142 0 1.9149 2.3333 1 1 1.7321 1 0
- 1 1.6667 1.9149 0 1 2.3333 1.9437 1 1.6330 0 1 1.9907 2.3333 1 0 2.5963 2.5748 1 1.6667 0


D :

R

1.9149 1 1 2.3333 2.5963 0 1 1.7321 1 0 1.9149 1 1 1.9437 2.5748 1 0 1.7321 1.4142 0

1 1 1.7321 1 1 1.7321 1.7321 0 1 0 1 1 1 1.6330 1.6667 1 1.4142 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 942](<2010-arkus-deriving-finite-sphere-packings_images/imageFile942.png>)

![image 943](<2010-arkus-deriving-finite-sphere-packings_images/imageFile943.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.75556R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.1547 −0.8165 0 0.4811 −0.2722 0.8333 0.9943 0 0 −0.8660 −1.6330 −0.5000 −0.8660 −1.6330 0.5000 0.5774 −0.8165 0 −0.2887 −0.8165 −0.5000 −0.2887 −0.8165 0.5000

C :

R

 

 

Packing 250 (Graph 743263):





0 0 0 1 1 0 0 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1 0 0 1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 1 0 0 0 1 0 1 1 0 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 1 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.6330 1.7778 1 1 1.6667 1.9907 1 1 0 1.6330 0 1.6330 1.6667 1.9907 1 1 1 1 0 1.7778 1.6330 0 2.5035 2.6108 1 1 1.9907 1.6667 0
- 1 1.6667 2.5035 0 1 1.9907 2.4369 1 1 0 1 1.9907 2.6108 1 0 2.4369 2.5402 1 1.6330 0


D :

R

1.6667 1 1 1.9907 2.4369 0 1 1.6330 1 0 1.9907 1 1 2.4369 2.5402 1 0 1.6667 1.6330 0

1 1 1.9907 1 1 1.6330 1.6667 0 1 0 1 1 1.6667 1 1.6330 1 1.6330 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 944](<2010-arkus-deriving-finite-sphere-packings_images/imageFile944.png>)

![image 945](<2010-arkus-deriving-finite-sphere-packings_images/imageFile945.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|10.43141R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6330 0 −1.4913 −0.9677 0 0.8830 −0.2722 −0.3824 0.8315 0 0.5480 −0.7726 −1.3608 −0.5735 −0.9345 −1.7237 0.3441 0.4636 −0.8165 0.3441 0 −0.8165 −0.5735 −0.5298 −0.8165 0.2294

C :

R

 

 

Packing 251 (Graph 744210):





0 0 0 1 1 0 0 1 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 0 0 1 0 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 0 0 1 1 1 0 0 1 1 0 0 1 0 0 0 1 1 1 0 1 0 1 0 0 1 1 1 0 1 0 1 1 0 1 0 1 0 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.9205 1.9205 1 1 1.7309 2.3129 1 1 0 1.9205 0 1.6180 1.4388 1.9205 1 1 1 1.6180 0 1.9205 1.6180 0 1.9205 1.4388 1 1 1.6180 1 0
- 1 1.4388 1.9205 0 1 1.7611 1.9317 1 1.4142 0 1 1.9205 1.4388 1 0 1.7611 1.9317 1.4142 1 0


D :

R

1.7309 1 1 1.7611 1.7611 0 1 1 1 0 2.3129 1 1 1.9317 1.9317 1 0 1.6180 1.6180 0

1 1 1.6180 1 1.4142 1 1.6180 0 1 0 1 1.6180 1 1.4142 1 1 1.6180 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 946](<2010-arkus-deriving-finite-sphere-packings_images/imageFile946.png>)

![image 947](<2010-arkus-deriving-finite-sphere-packings_images/imageFile947.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.51001R2|Cs<br><br>|1| |






0 0 0 0 1.9205 0 −1.4675 1.2388 0 0.2347 0.6816 −0.6930 −0.6722 0.2604 −0.6930 −0.6874 1.4799 0.5774 −0.9720 2.0927 −0.1598 0.1053 0.9602 0.2586 −0.8016 0.5390 0.2586 −0.5669 1.2206 −0.4344

C :

R

 

 

Packing 252 (Graph 744235):





0 0 0 1 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1 0 0 1 1 0 1 0 0 1 0 0 0 0 1 0 0 1 1 0 0 0 1 1 1 1 0 1 1 0 0 1 0 0 0 1 1 1 0 1 0 1 0 0 1 1 1 0 0 1 1 1 0 1 0 1 1 1 1 0 0 1 1 1 1 0

A :

 

 





- 0 1.6667 1.7249 1 1 1.6330 1.9907 1 1 0 1.6667 0 1.6330 1.9907 2.4369 1 1 1 1.6330 0 1.7249 1.6330 0 2.0718 1.8772 1 1 1.6667 1.0887 0
- 1 1.9907 2.0718 0 1 1.6667 2.4369 1 1 0 1 2.4369 1.8772 1 0 1.9907 2.5402 1.6330 1 0


D :

R

1.6330 1 1 1.6667 1.9907 0 1 1 1 0 1.9907 1 1 2.4369 2.5402 1 0 1.6330 1.6667 0

1 1 1.6667 1 1.6330 1 1.6330 0 1 0 1 1.6330 1.0887 1 1 1 1.6667 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 948](<2010-arkus-deriving-finite-sphere-packings_images/imageFile948.png>)

![image 949](<2010-arkus-deriving-finite-sphere-packings_images/imageFile949.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|9.60837R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 −1.6667 0 1.4553 −0.9259 0 −0.0735 0 −0.9957 0.5674 0.6481 −0.5079 0.7465 −1.3333 −0.5759 0.9445 −1.7222 0.3239 −0.1188 −0.8333 −0.5399 0.7465 −0.3333 −0.5759 0.4920 −0.8333 0.2519

C :

R

 

 

Packing 253 (Graph 744255):





0 0 0 1 1 0 0 1 1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 0 0 1 0 1 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 1 1 0 1 0 1 1 0 0 1 0 0 1 0 1 1 0 1 0 1 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 0 1 1 1 1 0 1 1 0

A :

 

 





- 0 1.6779 1.6779 1 1 1.6532 1.9843 1 1 0 1.6779 0 1.6180 1.9889 2.4344 1 1 1 1 0 1.6779 1.6180 0 1.9889 1.7971 1 1 1.6180 1 0
- 1 1.9889 1.9889 0 1 1.6482 2.4047 1 1.6330 0 1 2.4344 1.7971 1 0 1.9915 2.5048 1.6330 1.6667 0


D :

R

1.6532 1 1 1.6482 1.9915 0 1 1 1.0515 0 1.9843 1 1 2.4047 2.5048 1 0 1.6180 1 0

1 1 1.6180 1 1.6330 1 1.6180 0 1 0 1 1 1 1.6330 1.6667 1.0515 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 950](<2010-arkus-deriving-finite-sphere-packings_images/imageFile950.png>)

![image 951](<2010-arkus-deriving-finite-sphere-packings_images/imageFile951.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.44142R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 −1.6779 0 1.4175

- −0.8978 0

- −0.0230 0

0.9989 0.6051 0.6289 0.4882 0.7459

- −1.3554 0.5827 0.9435


- −1.7143 −0.3295 −0.1090 −0.8390


C :

R

0.5331 0.4617 −0.8390 −0.2880 0.7671 −0.3568 0.5331

 

 

Packing 254 (Graph 744305):





0 0 0 1 1 0 0 1 1 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1 0 0 1 0 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 0 0 1 1 0 1 0 1 1 0 0 1 0 0 1 1 1 1 0 1 0 1 0 0 1 1 1 1 0 0 1 0 1 1 0 1 0 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 2.3805 1 1 1.9149 1.9149 1 1 0 1.6330 0 1.7321 1.9149 1.9149 1 1 1 1 0 2.3805 1.7321 0 1.9149 1.9149 1 1 1.7321 1.7321 0
- 1 1.9149 1.9149 0 1 1.6330 1.9149 1 1.4142 0 1 1.9149 1.9149 1 0 1.9149 1.6330 1.4142 1 0


D :

R

1.9149 1 1 1.6330 1.9149 0 1 1 1.4142 0 1.9149 1 1 1.9149 1.6330 1 0 1.4142 1 0

1 1 1.7321 1 1.4142 1 1.4142 0 1 0 1 1 1.7321 1.4142 1 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 952](<2010-arkus-deriving-finite-sphere-packings_images/imageFile952.png>)

![image 953](<2010-arkus-deriving-finite-sphere-packings_images/imageFile953.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|8.80000R2<br><br>|Cs|1| |






0 0 0 0 1.6330 0 −1.7321 1.6330 0 −0.8660 −0.0000 −0.5000 −0.8660 −0.0000 0.5000 −0.8660 1.6330 −0.5000 −0.8660 1.6330 0.5000 −0.2887 0.8165 −0.5000

C :

R

- −0.2887 0.8165 0.5000
- −1.1547 0.8165


 

 

0

Packing 255 (Graph 744993):





0 0 0 1 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 0 0 0 1 1 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 1 1 1 0 0 1 1 0 0 1 0 1 0 1 1 1 0 0 0 1 1 0 1 1 1 0 1 1 0 1 0 1 0 1 1 0 1 1 1 0 1 1 1 0

A :

 

 





- 0 2.0000 1.7321 1 1 1.7321 1.7321 1 1 0 2.0000 0 1.7321 2.5166 2.5604 1 1 1 1.7321 0 1.7321 1.7321 0 1.4142 1.9149 1 1 1.4142 1 0
- 1 2.5166 1.4142 0 1 1.9149 1.9149 1.6330 1 0 1 2.5604 1.9149 1 0 2.3333 1.9437 1.6667 1.6330 0


D :

R

1.7321 1 1 1.9149 2.3333 0 1 1 1 0 1.7321 1 1 1.9149 1.9437 1 0 1 1.4142 0

1 1 1.4142 1.6330 1.6667 1 1 0 1 0 1 1.7321 1 1 1.6330 1 1.4142 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 954](<2010-arkus-deriving-finite-sphere-packings_images/imageFile954.png>)

![image 955](<2010-arkus-deriving-finite-sphere-packings_images/imageFile955.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|9.52222R2|C1<br><br>|1<br><br>|chiral|






0 0 0 0 2.0000 0 −1.4142 1.0000 0 −0.9428 −0.3333 −0.0000 −0.3928 −0.3889 0.8333 −0.7071 1.5000 −0.5000 −0.7071 1.5000 0.5000 −0.0000 1.0000 0 −0.7071 0.5000 −0.5000 −0.7071 0.5000 0.5000

C :

R

 

 

Packing 256 (Graph 745020):





0 0 0 1 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1 0 0 0 1 1 1 0 0 1 0 0 0 0 1 0 0 1 1 0 0 0 1 1 1 1 0 1 1 0 0 1 0 1 0 1 1 1 0 0 0 1 1 0 1 1 1 0 0 1 1 1 0 1 0 1 1 0 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.9907 1.9907 1 1 1.6330 1.6667 1 1 0 1.9907 0 1.6667 2.4369 2.5402 1 1 1 1.6667 0 1.9907 1.6667 0 1.7778 2.5035 1 1 1.6330 1.6667 0
- 1 2.4369 1.7778 0 1 1.6667 1.9907 1.6330 1 0 1 2.5402 2.5035 1 0 1.9907 2.4369 1.6667 1 0


D :

R

1.6330 1 1 1.6667 1.9907 0 1 1 1 0 1.6667 1 1 1.9907 2.4369 1 0 1 1.6330 0

1 1 1.6330 1.6330 1.6667 1 1 0 1 0 1 1.6667 1.6667 1 1 1 1.6330 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 956](<2010-arkus-deriving-finite-sphere-packings_images/imageFile956.png>)

![image 957](<2010-arkus-deriving-finite-sphere-packings_images/imageFile957.png>)

|2nd Moment<br><br>|φ|σ|Special Properties|
|---|---|---|---|
|10.02757R2<br><br>|C1|1<br><br>|chiral|






0 0 0 0 1.9907 0 −1.5136 1.2930 0 −0.8047 −0.2450 −0.5408 0.1113 −0.3742 −0.9207 −0.6518 1.4140 −0.4925 −0.6646 1.4419 0.5070 0 0.9954 0 −0.2530 0.5488 −0.7967 −0.8164 0.5768 0

C :

R

 

 

Packing 257 (Graph 749808):





0 0 0 1 1 0 1 0 0 1 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 1 0 0 0 1 0 1 1 0 1 1 1 0 0 0 1 0 1 1 1 0 0 1 0 0

A :

 

 





- 0 1.7019 1.7019 1 1 2.2551 1 1.7019 1.7019 0 1.7019 0 1.4142 1 1.5538 1 1 1 1 0 1.7019 1.4142 0 1.5538 1 1 1.5538 1 1 0
- 1 1 1.5538 0 1.4142 1.7019 1 1 1.5538 0 1 1.5538 1 1.4142 0 1.7019 1 1.5538 1 0


D :

R

2.2551 1 1 1.7019 1.7019 0 1.7019 1 1 0

1 1 1.5538 1 1 1.7019 0 1.5538 1 0 1.7019 1 1 1 1.5538 1 1.5538 0 1.4142 0 1.7019 1 1 1.5538 1 1 1 1.4142 0 0

 

 

0 0 0 0 0 0 0 0 0 0

![image 958](<2010-arkus-deriving-finite-sphere-packings_images/imageFile958.png>)

![image 959](<2010-arkus-deriving-finite-sphere-packings_images/imageFile959.png>)

|2nd Moment<br><br>|φ<br><br>|σ<br><br>|Special Properties|
|---|---|---|---|
|*7.95697R2<br><br>|D4d|8<br><br>|new seed|






0 0 0 0 −1.7019 0 1.2864 −1.1143 0 −0.1610 −0.8509 −0.5000 0.7486 −0.4354 0.5000 0.9370 −2.0512 0 −0.1610 −0.8509 0.5000 0.6432 −1.4081 −0.7071 0.6432 −1.4081 0.7071 0.7486 −0.4354 −0.5000

C :

R

 

 

Packing 258 (Graph 750016):





0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 0 1 1 0 1 0 0 0 1 0 1 1 0 1 0 1 0 0 0 1 0 1 0 1 1 0 1 0 0 0 1 0 1 1 0 1 0 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 1 0 1 0 0 1 1 1 1 0 1 1 0

A :

 

 





- 0 1.6330 1 1.9149 1 1.9149 1 1 1 0 1.6330 0 1.9149 1 1.9149 1 2.5166 1 1 0
- 1 1.9149 0 1.6330 1 1.9149 1 1 1.4142 0 1.9149 1 1.6330 0 1.9149 1 2.5166 1 1.4142 0


- 1 1.9149 1 1.9149 0 1.6330 1 1.4142 1 0


D :

R

1.9149 1 1.9149 1 1.6330 0 2.5166 1.4142 1 0 1 2.5166 1 2.5166 1 2.5166 0 1.7321 1.7321 0 1 1 1 1 1.4142 1.4142 1.7321 0 1 0 1 1 1.4142 1.4142 1 1 1.7321 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 960](<2010-arkus-deriving-finite-sphere-packings_images/imageFile960.png>)

![image 961](<2010-arkus-deriving-finite-sphere-packings_images/imageFile961.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|9.40000R2<br><br>|C3v|3| |






0 0 0 0 −1.6330 0 −1.0000 −0.0000 0 −1.0000 −1.6330 0 −0.5000 0 −0.8660 −0.5000 −1.6330 −0.8660 −0.5000 0.8165 −0.2887 −0.5000 −0.8165 0.2887 −0.0000 −0.8165 −0.5774 −1.0000 −0.8165 −0.5774

C :

R

 

 

Packing 259 (Graph 750276):





0 0 1 0 1 0 1 1 1 1 0 0 0 1 0 1 0 1 1 1 1 0 0 0 1 0 1 0 1 1 0 1 0 0 0 1 0 1 1 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 0 0 1 1 1 1 1 1 0 0 0 1 0 1 1 1 1 0 1 0 0 1 1 0

A :

 

 





- 0 1.6330 1 1.6667 1 1.9907 1 1 1 0 1.6330 0 1.6667 1 1.9907 1 2.4369 1 1 0
- 1 1.6667 0 1.9907 1 2.4369 1 1.6330 1 0 1.6667 1 1.9907 0 2.4369 1 2.5402 1 1 0


1 1.9907 1 2.4369 0 2.5402 1 1.6667 1.6330 0

D :

R

1.9907 1 2.4369 1 2.5402 0 2.9650 1 1.6330 0 1 2.4369 1 2.5402 1 2.9650 0 1.9907 1.6667 0 1 1 1.6330 1 1.6667 1 1.9907 0 1 0 1 1 1 1 1.6330 1.6330 1.6667 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 962](<2010-arkus-deriving-finite-sphere-packings_images/imageFile962.png>)

![image 963](<2010-arkus-deriving-finite-sphere-packings_images/imageFile963.png>)

|2nd Moment<br><br>|φ|σ<br><br>|Special Properties|
|---|---|---|---|
|10.92524R2|C2<br><br>|2<br><br>|chiral|






0 0 0 0 1.6330 0 0.9623 0.2722 0 −0.4811 1.3608 0.8333 0.5453 −0.0907 −0.8333 −0.9943 1.7237 0 0.7163 −0.6955 −0.0556 −0.5774 0.8165 −0.0000 0.2887 0.8165 0.5000 0.2887 0.8165 −0.5000

C :

R

 

 

Packing 260 (Graph 164942):





0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 1 0 1 1 1 0 0 0 0 1 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 1 0 0 0 1 1 1 1 1 0 0 1 1 1 0 1 0 1 0 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.6330 1.9149 1 1.9149 1 1 1 0 1.7321 0 1.7321 1.7321 1.7321 1 1 1.7321 1 0 1.6330 1.7321 0 1 1.9149 1 1.9149 1 1 0 1.9149 1.7321 1 0 1.6330 1 1.9149 1 1.4142 0
- 1 1.7321 1.9149 1.6330 0 1.9149 1 1 1.4142 0


D :

R

1.9149 1 1 1 1.9149 0 1.6330 1.4142 1 0 1 1 1.9149 1.9149 1 1.6330 0 1.4142 1 0 1 1.7321 1 1 1 1.4142 1.4142 0 1 0 1 1 1 1.4142 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 964](<2010-arkus-deriving-finite-sphere-packings_images/imageFile964.png>)

![image 965](<2010-arkus-deriving-finite-sphere-packings_images/imageFile965.png>)

|2nd Moment<br><br>|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.20000R2<br><br>|C2v|2<br><br>|25 contacts|






0 0 0 0 −1.7321 0 1.4402 −0.7698 0 1.2859 −1.0585 −0.9449 −0.1543 −0.2887 −0.9449 0.9773 −1.6358 −0.1890 −0.4629 −0.8660 −0.1890 0.7715 −0.2887 −0.5669 0.4629 −0.8660 0.1890 0.3086 −1.1547 −0.7559

C :

R

 

 

The other graphs that lead to the same 25 contact packing (packing 260), with their corresponding distance matrices and coordinates: The table containing the minimum of the 2nd moment, etc., as well as the pictures will be the same, and thus is not included in the list.

Graph 458233:





0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 1 0 1 1 1 0 1 1 0 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.9149 1.7321 1 1.6330 1 1.9149 1 1.4142 0 1.9149 0 1.7321 1.6330 1 1.9149 1 1 1 0 1.7321 1.7321 0 1.7321 1.7321 1 1 1.7321 1 0
- 1 1.6330 1.7321 0 1.9149 1 1.9149 1 1 0 1.6330 1 1.7321 1.9149 0 1.9149 1 1 1.4142 0


D :

R

1 1.9149 1 1 1.9149 0 1.6330 1.4142 1 0 1.9149 1 1 1.9149 1 1.6330 0 1.4142 1 0

1 1 1.7321 1 1 1.4142 1.4142 0 1 0 1.4142 1 1 1 1.4142 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

Graph 520761:





- 0 0 0 1 0 1 0 1 1 0

- 0 0 0 0 1 0 1 1 1 0

- 0 0 0 0 0 0 1 0 1 1
- 1 0 0 0 0 1 0 1 0 1


- 0 1 0 0 0 0 1 1 0 1


- 1 0 0 1 0 0 0 0 1 1


A :

- 0 1 1 0 1 0 0 0 1 1
- 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 1 1 0 1 0 0 1 1 1 1 1 1 1 0


 

 





- 0 1.6330 1.7321 1 1.9149 1 1.9149 1 1 0

1.6330 0 1.7321 1.9149 1 1.9149 1 1 1 0 1.7321 1.7321 0 1.7321 1.7321 1 1 1.7321 1 0

- 1 1.9149 1.7321 0 1.6330 1 1.9149 1 1.4142 0


1.9149 1 1.7321 1.6330 0 1.9149 1 1 1.4142 0 1 1.9149 1 1 1.9149 0 1.6330 1.4142 1 0

D :

R

1.9149 1 1 1.9149 1 1.6330 0 1.4142 1 0 1 1 1.7321 1 1 1.4142 1.4142 0 1 0 1 1 1 1.4142 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 





0 0 0 0 −1.9149 0 −1.4434 −0.9574 0 0 −0.5222 0.8528 0 −1.3926 −0.8528 −0.8660 −0.2611 0.4264 −0.8660 −1.6537 −0.4264 0.2887 −0.9574 0 −0.5774 −1.2185 0.4264 −0.5774 −0.6963 −0.4264

C :

R

 

 





0 0 0 0 −1.6330 0 −1.5275 −0.8165 0 −0.3273 0 0.9449 −0.3273 −1.6330 0.9449 −0.9820 0 0.1890

C :

R

- −0.9820
- −1.6330 0.1890 0.1091


−0.8165 0.5669 −0.5455 −0.8165 −0.1890 −0.8729 −0.8165 0.7559

 

 

Graph 561797 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 −1.6330 0 1.5275 −0.8165 0 0.3273 0 −0.9449 0.3273 −1.6330 −0.9449 0.5455 −0.8165 0.1890 0.8729 −0.8165 −0.7559 0.9820 0 −0.1890 0.9820 −1.6330 −0.1890 −0.1091 −0.8165 −0.5669





0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 1 0 1 1 0 1 1 0 0 0

A :

 

 

- 0 1 1 0 1 1 1 0 0 0
- 1 1 0 1 1 1 1 0 0 0


C :

R





- 0 1.6330 1.7321 1 1.9149 1 1.4142 1 1.9149 0 1.6330 0 1.7321 1.9149 1 1 1.4142 1.9149 1 0 1.7321 1.7321 0 1.7321 1.7321 1 1 1 1 0
- 1 1.9149 1.7321 0 1.6330 1.4142 1 1 1.9149 0 1.9149 1 1.7321 1.6330 0 1.4142 1 1.9149 1 0


D :

R

1 1 1 1.4142 1.4142 0 1.0000 1 1 0 1.4142 1.4142 1 1 1 1.0000 0 1 1 0

1 1.9149 1 1 1.9149 1 1 0 1.6330 0 1.9149 1 1 1.9149 1 1 1 1.6330 0 0

 

 

0 0 0 0 0 0 0 0 0 0

 

 

Graph 594218:





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 0 1 1 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.9149 1.7321 1 1.6330 1 1 1.9149 1 0 1.9149 0 1.7321 1.6330 1 1.9149 1 1 1.4142 0 1.7321 1.7321 0 1.7321 1.7321 1 1.7321 1 1 0
- 1 1.6330 1.7321 0 1.9149 1 1 1.9149 1.4142 0


1.6330 1 1.7321 1.9149 0 1.9149 1 1 1 0 1 1.9149 1 1 1.9149 0 1.4142 1.6330 1 0 1 1 1.7321 1 1 1.4142 0 1.4142 1 0

D :

R

1.9149 1 1 1.9149 1 1.6330 1.4142 0 1 0 1 1.4142 1 1.4142 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 





0 0 0 0 −1.9149 0 −1.4434 −0.9574 0 −0.0000 −0.5222 0.8528 0 −1.3926 −0.8528 −0.8660 −0.2611 0.4264 0.2887 −0.9574 −0.0000 −0.8660 −1.6537 −0.4264 −0.5774 −0.6963 −0.4264 −0.5774 −1.2185 0.4264

C :

R

 

 

Graph 609155 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 1.6330 0 1.5275 0.8165 0 0.3273 −0.0000 −0.9449 0.3273 1.6330 −0.9449 0.9820 −0.0000 −0.1890 0.9820 1.6330 −0.1890 −0.1091 0.8165 −0.5669 0.5455 0.8165 0.1890 0.8729 0.8165 −0.7559





0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 0 0 1 1 1 1 1 1 1 0

A :

 

 

C :

R





- 0 1.6330 1.7321 1 1.9149 1 1.9149 1 1 0 1.6330 0 1.7321 1.9149 1 1.9149 1 1 1 0 1.7321 1.7321 0 1.7321 1.7321 1 1 1.7321 1 0
- 1 1.9149 1.7321 0 1.6330 1 1.9149 1 1.4142 0 1.9149 1 1.7321 1.6330 0 1.9149 1 1 1.4142 0


D :

R

1 1.9149 1 1 1.9149 0 1.6330 1.4142 1 0

1.9149 1 1 1.9149 1 1.6330 0 1.4142 1 0 1 1 1.7321 1 1 1.4142 1.4142 0 1 0 1 1 1 1.4142 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

 

 

Graph 609244 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 1.6330 0 −1.5275 0.8165 0 −0.3273 −0.0000 −0.9449 −0.3273 1.6330 −0.9449 −0.9820 −0.0000 −0.1890 −0.9820 1.6330 −0.1890 0.1091 0.8165 −0.5669 −0.5455 0.8165 0.1890 −0.8729 0.8165 −0.7559





0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 0 0 1 1 1 1 1 1 1 0

A :

 

 

C :

R





- 0 1.6330 1.7321 1 1.9149 1 1.9149 1 1 0 1.6330 0 1.7321 1.9149 1 1.9149 1 1 1 0 1.7321 1.7321 0 1.7321 1.7321 1 1 1.7321 1 0
- 1 1.9149 1.7321 0 1.6330 1 1.9149 1 1.4142 0 1.9149 1 1.7321 1.6330 0 1.9149 1 1 1.4142 0


D :

R

1 1.9149 1 1 1.9149 0 1.6330 1.4142 1 0

1.9149 1 1 1.9149 1 1.6330 0 1.4142 1 0 1 1 1.7321 1 1 1.4142 1.4142 0 1 0 1 1 1 1.4142 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

 

 

Graph 609350:





0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 0 0 0 1 1 1 0 1 0 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.6330 1.7321 1 1.9149 1 1.9149 1 1 0 1.6330 0 1.7321 1.9149 1 1.9149 1 1 1 0 1.7321 1.7321 0 1.7321 1.7321 1 1 1.7321 1 0
- 1 1.9149 1.7321 0 1.6330 1 1.9149 1 1.4142 0 1.9149 1 1.7321 1.6330 0 1.9149 1 1 1.4142 0


D :

R

1 1.9149 1 1 1.9149 0 1.6330 1.4142 1 0

1.9149 1 1 1.9149 1 1.6330 0 1.4142 1 0 1 1 1.7321 1 1 1.4142 1.4142 0 1 0 1 1 1 1.4142 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

Graph 609376:





0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 1 1 0 0 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 0 1 0 0 1 1 1 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





0 1.9149 1.7321 1 1.6330 1 1.9149 1 1 0

- 1.9149 0 1.7321 1.6330 1 1.9149 1 1 1.4142 0 1.7321 1.7321 0 1.7321 1.7321 1 1 1.7321 1 0

1 1.6330 1.7321 0 1.9149 1 1.9149 1 1.4142 0 1.6330 1 1.7321 1.9149 0 1.9149 1 1 1 0

1 1.9149 1 1 1.9149 0 1.6330 1.4142 1 0

- 1.9149 1 1 1.9149 1 1.6330 0 1.4142 1 0 1 1 1.7321 1 1 1.4142 1.4142 0 1 0 1 1.4142 1 1.4142 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 





0 0 0 0 −1.6330 0 −1.5275 −0.8165 0 −0.3273 −0.0000 −0.9449 −0.3273 −1.6330 −0.9449 −0.9820 0 −0.1890 −0.9820 −1.6330 −0.1890 0.1091 −0.8165 −0.5669 −0.5455 −0.8165 0.1890 −0.8729 −0.8165 −0.7559

C :

R

 

 





0 0 0 0 −1.9149 0 −1.4434 −0.9574 0 0

- −0.5222 0.8528

0

- −1.3926 −0.8528 −0.8660 −0.2611


C :

R

0.4264 −0.8660 −1.6537 −0.4264 0.2887 −0.9574 −0.0000 −0.5774 −0.6963 −0.4264

- −0.5774
- −1.2185 0.4264


 

 

Packing 261 (Graph 362694):





0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 0 0 1 0 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 1 1 1 1 0 1 0 1 1 0 1 1 1 0 1 0 1 1 1 1 0

A :

 

 





- 0 1.4142 1.7321 1.7321 1 1 1 1.7321 1 0 1.4142 0 1.7321 1.7321 1 1 1.7321 1 1 0 1.7321 1.7321 0 1 2.0000 2.2361 1 1 1 0 1.7321 1.7321 1 0 2.2361 2.0000 1 1 1.4142 0
- 1 1 2.0000 2.2361 0 1 1.7321 1.7321 1 0 1 1 2.2361 2.0000 1 0 1.7321 1.7321 1.4142 0 1 1.7321 1 1 1.7321 1.7321 0 1.4142 1 0


D :

R

1.7321 1 1 1 1.7321 1.7321 1.4142 0 1 0 1 1 1 1.4142 1 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 966](<2010-arkus-deriving-finite-sphere-packings_images/imageFile966.png>)

![image 967](<2010-arkus-deriving-finite-sphere-packings_images/imageFile967.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.50000R2|D2h<br><br>|4|25 contacts|






0 0 0 0 1.4142 0 −1.5811 0.7071 0 −1.2649 0.7071 −0.9487 0.3162 0.7071 0.6325 0.6325 0.7071 −0.3162 −0.9487 −0.0000 −0.3162 −0.9487 1.4142 −0.3162 −0.6325 0.7071 0.3162 −0.3162 0.7071 −0.6325

C :

R

 

 

The other graphs that lead to the same 25 contact packing (packing 261), with their corresponding distance matrices and coordinates: The table containing the minimum of the 2nd moment, etc., as well as the pictures will be the same, and thus is not included in the list.

Graph 593947:





0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 1 0 1 1 1 0 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 2.0000 1 1 2.2361 1 0 1.7321 0 1.4142 1.7321 1 1.7321 1 1 1 0 1.7321 1.4142 0 1.7321 1 1 1.7321 1 1 0
- 1 1.7321 1.7321 0 2.2361 1 1 2.0000 1.4142 0


2.0000 1 1 2.2361 0 1.7321 1.7321 1 1 0 1 1.7321 1 1 1.7321 0 1.4142 1.7321 1 0 1 1 1.7321 1 1.7321 1.4142 0 1.7321 1 0

D :

R

2.2361 1 1 2.0000 1 1.7321 1.7321 0 1.4142 0 1 1 1 1.4142 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 





0 0 0 0 1.7321 0 −1.2910 1.1547 0 −0.1291 0.2887 0.9487 −0.7746 1.7321 −0.6325 −0.9037 0.2887 0.3162 0.3873 0.8660 0.3162 −0.9037 2.0207 0.3162 −0.3873 0.8660 −0.3162 −0.5164 1.1547 0.6325

C :

R

 

 

Graph 726649 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 1.7321 0 −1.2910 1.1547 0 −0.1291 0.2887 0.9487 −0.7746 1.7321 −0.6325 −0.9037 2.0207 0.3162 0.3873 0.8660 0.3162 −0.9037 0.2887 0.3162 −0.3873 0.8660 −0.3162 −0.5164 1.1547 0.6325





0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 1 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 1 1 1 0 1 0 1 0 0 1 0 1 1 1 0 1 1 1 1 0

A :

 

 

C :

R





0 1.7321 1.7321 1 2.0000 2.2361 1 1 1 0

- 1.7321 0 1.4142 1.7321 1 1 1 1.7321 1 0 1.7321 1.4142 0 1.7321 1 1 1.7321 1 1 0

1 1.7321 1.7321 0 2.2361 2.0000 1 1 1.4142 0 2.0000 1 1 2.2361 0 1 1.7321 1.7321 1 0

- 2.2361 1 1 2.0000 1 0 1.7321 1.7321 1.4142 0 1 1 1.7321 1 1.7321 1.7321 0 1.4142 1 0 1 1.7321 1 1 1.7321 1.7321 1.4142 0 1 0 1 1 1 1.4142 1 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0


D :

R

 

 

 

 

Graph 726751:





0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 1 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 1 0 0 0 1 1 0 1 0 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 2.2361 2.0000 1 1 1 0 1.7321 0 1.4142 1.7321 1 1 1 1.7321 1 0 1.7321 1.4142 0 1.7321 1 1 1.7321 1 1 0
- 1 1.7321 1.7321 0 2.0000 2.2361 1 1 1.4142 0 2.2361 1 1 2.0000 0 1 1.7321 1.7321 1.4142 0 2.0000 1 1 2.2361 1 0 1.7321 1.7321 1 0


D :

R

1 1 1.7321 1 1.7321 1.7321 0 1.4142 1 0 1 1.7321 1 1 1.7321 1.7321 1.4142 0 1 0 1 1 1 1.4142 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 





0 0 0 0 −1.7321 0 1.2910 −1.1547 0 0.1291 −0.2887 −0.9487 0.9037 −2.0207 −0.3162 0.7746 −1.7321 0.6325 −0.3873 −0.8660 −0.3162 0.9037 −0.2887 −0.3162 0.3873 −0.8660 0.3162 0.5164 −1.1547 −0.6325

C :

R

 

 

Graph 726815 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 −1.7321 0 −1.2910 −1.1547 0 −0.1291 −0.2887 −0.9487 −0.7746 −1.7321 0.6325 −0.9037 −2.0207 −0.3162 0.3873 −0.8660 −0.3162 −0.9037 −0.2887 −0.3162 −0.3873 −0.8660 0.3162 −0.5164 −1.1547 −0.6325





0 0 0 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 0 1 1 0 0 1 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 1 0 1 0 1 1 0 0 0 1 1 1 0 1 1 1 0 0

A :

 

 

C :

R





- 0 1.7321 1.7321 1 2.0000 2.2361 1 1 1 0 1.7321 0 1.4142 1.7321 1 1 1 1.7321 1 0 1.7321 1.4142 0 1.7321 1 1 1.7321 1 1 0
- 1 1.7321 1.7321 0 2.2361 2.0000 1 1 1.4142 0 2.0000 1 1 2.2361 0 1 1.7321 1.7321 1 0 2.2361 1 1 2.0000 1 0 1.7321 1.7321 1.4142 0


D :

R

1 1 1.7321 1 1.7321 1.7321 0 1.4142 1 0 1 1.7321 1 1 1.7321 1.7321 1.4142 0 1 0 1 1 1 1.4142 1 1.4142 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 

 

 

Graph 735230:





0 0 0 1 1 0 1 0 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 0 0 1 0 0 0 1 1 1 1 0 1 1 1 0 0 1 0 1 1 1 1 0 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1 1 2.0000 1 2.2361 1 0 1.7321 0 1.4142 1.7321 1.7321 1 1 1 1 0 1.7321 1.4142 0 1.7321 1 1 1.7321 1 1 0
- 1 1.7321 1.7321 0 1 2.2361 1 2.0000 1.4142 0 1 1.7321 1 1 0 1.7321 1.4142 1.7321 1 0


D :

R

2.0000 1 1 2.2361 1.7321 0 1.7321 1 1 0 1 1 1.7321 1 1.4142 1.7321 0 1.7321 1 0

2.2361 1 1 2.0000 1.7321 1 1.7321 0 1.4142 0 1 1 1 1.4142 1 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 





0 0 0 0 1.7321 0 1.2910 1.1547 0 0.1291 0.2887 −0.9487 0.9037 0.2887 −0.3162 0.7746 1.7321 0.6325 −0.3873 0.8660 −0.3162 0.9037 2.0207 −0.3162 0.3873 0.8660 0.3162 0.5164 1.1547 −0.6325

C :

R

 

 

Packing 262 (*Graph 209285):





0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.4142 1.6330 1.7321 1 1 1.9149 1 1 0 1.4142 0 1.4142 1 1 1.7321 1 1 1 0 1.6330 1.4142 0 1.7321 1.9149 1 1 1.9149 1 0 1.7321 1 1.7321 0 1.7321 2.0000 1 1 1.7321 0
- 1 1 1.9149 1.7321 0 1.7321 1.9149 1 1 0 1 1.7321 1 2.0000 1.7321 0 1.7321 1.7321 1 0


D :

R

1.9149 1 1 1 1.9149 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1 1 1.7321 1 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

![image 968](<2010-arkus-deriving-finite-sphere-packings_images/imageFile968.png>)

![image 969](<2010-arkus-deriving-finite-sphere-packings_images/imageFile969.png>)

|2nd Moment|φ<br><br>|σ|Special Properties|
|---|---|---|---|
|8.30000R2|C1v|1<br><br>|25 contacts|






0 0 0 0 −1.4142 0 −1.3333 −0.9428 0 −0.0000 −1.4142 1.0000 0.5000 −0.7071 −0.5000 −1.0000 0 0 −0.8333 −1.6499 0.5000 0.5000 −0.7071 0.5000 −0.5000 −0.7071 −0.5000 −0.5000 −0.7071 0.5000

C :

R

 

 

The other graphs that lead to the same 25 contact packing (packing 262), with their corresponding distance matrices and coordinates: The table containing the minimum of the 2nd moment, etc., as well as the pictures will be the same, and thus is not included in the list.

Graph 287036:





0 0 0 0 1 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 0 1 1 1 0 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.7321 1.7321 1.7321 1 2.0000 1 1 1.7321 0 1.7321 0 1.9149 1 1 1.7321 1.9149 1 1 0 1.7321 1.9149 0 1.6330 1.4142 1 1 1.9149 1 0 1.7321 1 1.6330 0 1.4142 1 1.9149 1 1 0
- 1 1 1.4142 1.4142 0 1.7321 1 1 1 0


D :

R

2.0000 1.7321 1 1 1.7321 0 1.7321 1.7321 1 0 1 1.9149 1 1.9149 1 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0

 

 

1.7321 1 1 1 1 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

Graph 287247:





- 0 0 0 0 1 0 1 1 1 0

- 0 0 0 0 1 0 0 1 0 1

- 0 0 0 0 0 1 1 0 1 1

- 0 0 0 0 0 1 0 1 0 1
- 1 1 0 0 0 0 1 1 0 1


- 0 0 1 1 0 0 0 0 1 1


- 1 0 1 0 1 0 0 0 1 1


- 1 1 0 1 1 0 0 0 1 1 1 0 1 0 0 1 1 1 0 1 0 1 1 1 1 1 1 1 1 0


A :

 

 





- 0 1.7321 1.7321 1.9149 1 1.9149 1 1 1 0

1.7321 0 2.0000 1 1 1.7321 1.7321 1 1.7321 0 1.7321 2.0000 0 1.7321 1.7321 1 1 1.7321 1 0 1.9149 1 1.7321 0 1.6330 1 1.9149 1 1.4142 0

- 1 1 1.7321 1.6330 0 1.9149 1 1 1.4142 0


D :

R

1.9149 1.7321 1 1 1.9149 0 1.6330 1.4142 1 0 1 1.7321 1 1.9149 1 1.6330 0 1.4142 1 0 1 1 1.7321 1 1 1.4142 1.4142 0 1 0 1 1.7321 1 1.4142 1.4142 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0

 

 





0 0 0 0 −1.7321 0 1.5957 −0.6736 0 0.4353 −1.4432 −0.8530 0.2612 −0.8660 0.4264 1.3927 −1.1546 −0.8529 0.8994 −0.0962 0.4264 −0.2611 −0.8660 −0.4264 0.9574 −1.4434 −0.0002 0.6963 −0.5773 −0.4265

C :

R

 

 





0 0 0 0 −1.7321 0 1.6330

- −0.5774 0

0.5443

- −1.6358


0.8333 −0.0000 −0.8660

- −0.5000

1.3608

- −1.0585 0.8333 0.8165


C :

R

−0.2887 −0.5000 0 −0.8660 0.5000 0.8165

- −0.2887 0.5000 0.8165
- −1.1547 −0.0000


 

 

###### *Graph 457764:





0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 1 0 1 0 0 0 1 1 1 1 0 1 1 1 1 1 0

A :

 

 





- 0 1.4142 1.6330 1 1.7321 1 1.9149 1 1 0 1.4142 0 1.4142 1 1 1.7321 1 1 1 0 1.6330 1.4142 0 1.9149 1.7321 1 1 1.9149 1 0
- 1 1 1.9149 0 1.7321 1.7321 1.9149 1 1 0 1.7321 1 1.7321 1.7321 0 2.0000 1 1 1.7321 0 1 1.7321 1 1.7321 2.0000 0 1.7321 1.7321 1 0


D :

R

1.9149 1 1 1.9149 1 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1 1 1 1.7321 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

Graph 467227:





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 1

A :

- 0 1 1 0 1 0 0 1 1 1

- 0 1 1 0 0 1 1 0 0 1
- 1 0 1 1 0 1 1 0 0 1


- 1 1 0 1 1 1 1 1 1 0


 

 





- 0 2.0000 1.7321 1 1.7321 1 1.7321 1.7321 1 0 2.0000 0 1.7321 1.7321 1 1.7321 1 1 1.7321 0 1.7321 1.7321 0 1.9149 1.9149 1 1 1 1 0
- 1 1.7321 1.9149 0 1 1.6330 1.4142 1.9149 1 0 1.7321 1 1.9149 1 0 1.9149 1 1.6330 1.4142 0


D :

R

1 1.7321 1 1.6330 1.9149 0 1.4142 1 1 0 1.7321 1 1 1.4142 1 1.4142 0 1 1 0 1.7321 1 1 1.9149 1.6330 1 1 0 1.4142 0

 

 

1 1.7321 1 1 1.4142 1 1 1.4142 0 0 0 0 0 0 0 0 0 0 0 0





0 0 0 0 −1.4143 0 −1.3332 −0.9429 0 0.5001 −0.7070 −0.5001 0 −1.4142 1.0000 −1.0000 −0.0001 0 −0.8333 −1.6500 0.5001 0.5001 −0.7072 0.4999 −0.4999 −0.7072 −0.5000 −0.4999 −0.7072 0.5000

C :

R

 

 





0 0 0 0 −2.0000 0 −1.4142 −1.0000 0 0.2357 −0.5000

- −0.8333 0.2357
- −1.5000 −0.8333 −0.7071 −0.5000


C :

R

0.5000 −0.7071 −1.5000 −0.5000

- −0.7071
- −1.5000 0.5000


−0.7071 −0.5000 −0.5000 −0.0000 −1.0000 0

 

 

###### *Graph 467242:





0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 1 0 1 0 0 1 0 1 0 1 1 0 0 1 1 0 1 1 1 1 0 1 1 0 0 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 





- 0 1.9149 1.7321 1 1.6330 1 1.9149 1.4142 1 0 1.9149 0 1.7321 1.7321 1 1.9149 1 1 1 0 1.7321 1.7321 0 2.0000 1.7321 1 1 1 1.7321 0
- 1 1.7321 2.0000 0 1 1.7321 1.7321 1.7321 1 0 1.6330 1 1.7321 1 0 1.9149 1 1.4142 1 0


D :

R

1 1.9149 1 1.7321 1.9149 0 1.6330 1 1.4142 0 1.9149 1 1 1.7321 1 1.6330 0 1 1.4142 0 1.4142 1 1 1.7321 1.4142 1 1 0 1 0

 

 

1 1 1.7321 1 1 1.4142 1.4142 1 0 0 0 0 0 0 0 0 0 0 0 0

###### *Graph 618663:





0 0 0 1 1 0 0 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 





- 0 1.4142 1.4142 1 1 1.7321 1 1 1 0 1.4142 0 1.6330 1.7321 1 1 1.9149 1 1 0 1.4142 1.6330 0 1.7321 1.9149 1 1 1.9149 1 0
- 1 1.7321 1.7321 0 1.7321 2.0000 1 1 1.7321 0 1 1 1.9149 1.7321 0 1.7321 1.9149 1 1 0


D :

R

1.7321 1 1 2.0000 1.7321 0 1.7321 1.7321 1 0 1 1.9149 1 1 1.9149 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1 1 1.7321 1 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 





0 0 0 0 −1.9149 0 −1.4434 −0.9574 0 0.2887 −0.4352 0.8528 0 −1.3926 0.8528 −0.8660 −0.2611 −0.4264 −0.8660 −1.6537 0.4264 −0.5774 −1.2185 −0.4264 0.2887 −0.9574 −0.0000 −0.5774 −0.6963 0.4264

C :

R

 

 





0 0 0 0 1.4142 0 1.3333 0.4714 0 0 −0.0000 −1.0000 −0.5000 0.7071 0.5000 1.0000 1.4142 0 0.8335 −0.2356 −0.5002 −0.5000 0.7071 −0.5000 0.5000 0.7071 0.5000 0.5000 0.7071 −0.5000

C :

R

 

 

Graph 618805 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 1.7321 0 −1.6330 1.1547 0 −0.5443 0 0.8333 −0.0000 0.8660 −0.5000 −0.8165 1.4434 −0.5000 −1.3608 0.6736 0.8333 −0.0000 0.8660 0.5000 −0.8165 1.4434 0.5000 −0.8165 0.5774 0





0 0 0 1 1 0 0 1 0 1 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0

A :

 

 

C :

R





- 0 1.7321 2.0000 1 1 1.7321 1.7321 1 1.7321 0 1.7321 0 1.7321 1.9149 1 1 1.9149 1 1 0 2.0000 1.7321 0 1.7321 1.7321 1 1 1.7321 1 0
- 1 1.9149 1.7321 0 1.6330 1.9149 1 1 1.4142 0 1 1 1.7321 1.6330 0 1.0000 1.9149 1 1.4142 0


D :

R

1.7321 1 1 1.9149 1.0000 0 1.6330 1.4142 1 0 1.7321 1.9149 1 1 1.9149 1.6330 0 1.4142 1 0

1 1 1.7321 1 1 1.4142 1.4142 0 1 0 1.7321 1 1 1.4142 1.4142 1 1 1 0 0

 

 

0 0 0 0 0 0 0 0 0 0

 

 

Graph 622325 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 1.4142 0 −1.3333 0.4714 0 0 0 −1.0000 0.5000 0.7071 0.5000 −1.0000 1.4142 −0.0000 −0.8333 −0.2357 −0.5000 0.5000 0.7071 −0.5000 −0.5000 0.7071 0.5000 −0.5000 0.7071 −0.5000





0 0 0 1 1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 1 1 1 0

A :

 

 

C :

R





- 0 1.4142 1.4142 1 1 1.7321 1 1 1 0 1.4142 0 1.6330 1.7321 1 1 1.9149 1 1 0 1.4142 1.6330 0 1.7321 1.9149 1 1 1.9149 1 0
- 1 1.7321 1.7321 0 1.7321 2.0000 1 1 1.7321 0 1 1 1.9149 1.7321 0 1.7321 1.9149 1 1 0


D :

R

1.7321 1 1 2.0000 1.7321 0 1.7321 1.7321 1 0 1 1.9149 1 1 1.9149 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1 1 1.7321 1 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

 

 

Graph 622375 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 −1.4142 0 1.3333 −0.4714 0 0 −0.0000 −1.0000 −0.5000 −0.7071 0.5000 1.0000 −1.4142 −0.0000 0.8333 0.2357 −0.5000 −0.5000 −0.7071 −0.5000 0.5000 −0.7071 0.5000 0.5000 −0.7071 −0.5000





0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 1 0 0

A :

 

 

C :

R





- 0 1.4142 1.4142 1 1 1.7321 1 1 1 0 1.4142 0 1.6330 1.7321 1 1 1.9149 1 1 0 1.4142 1.6330 0 1.7321 1.9149 1 1 1.9149 1 0
- 1 1.7321 1.7321 0 1.7321 2.0000 1 1 1.7321 0 1 1 1.9149 1.7321 0 1.7321 1.9149 1 1 0


D :

R

1.7321 1 1 2.0000 1.7321 0 1.7321 1.7321 1 0 1 1.9149 1 1 1.9149 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1 1 1.7321 1 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

 

 

Graph 622382 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 −1.4142 0 1.3333





0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 1 0 1 0

- −0.4714 0 0 0
- −1.0000 −0.5000 −0.7071


A :

 

 

0.5000 1.0000 −1.4142 0 0.8333 0.2357 −0.5000 −0.5000 −0.7071 −0.5000 0.5000 −0.7071 0.5000 0.5000 −0.7071 −0.5000

C :

R





- 0 1.4142 1.4142 1 1 1.7321 1 1 1 0 1.4142 0 1.6330 1.7321 1 1 1.9149 1 1 0 1.4142 1.6330 0 1.7321 1.9149 1 1 1.9149 1 0
- 1 1.7321 1.7321 0 1.7321 2.0000 1 1 1.7321 0 1 1 1.9149 1.7321 0 1.7321 1.9149 1 1 0


D :

R

1.7321 1 1 2.0000 1.7321 0 1.7321 1.7321 1 0 1 1.9149 1 1 1.9149 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1 1 1.7321 1 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

 

 

###### *Graph 622387:





0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 1 0 1 1 0

A :

 

 





- 0 1.4142 1.4142 1 1 1.7321 1 1 1 0 1.4142 0 1.6330 1.7321 1 1 1.9149 1 1 0 1.4142 1.6330 0 1.7321 1.9149 1 1 1.9149 1 0
- 1 1.7321 1.7321 0 1.7321 2.0000 1 1 1.7321 0 1 1 1.9149 1.7321 0 1.7321 1.9149 1 1 0


D :

R

1.7321 1 1 2.0000 1.7321 0 1.7321 1.7321 1 0 1 1.9149 1 1 1.9149 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1 1 1.7321 1 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 

###### *Graph 622390:





0 0 0 1 1 0 1 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 1 1 0

A :

 

 





- 0 1.4142 1.4142 1 1 1.7321 1 1 1 0 1.4142 0 1.6330 1.7321 1 1 1.9149 1 1 0 1.4142 1.6330 0 1.7321 1.9149 1 1 1.9149 1 0
- 1 1.7321 1.7321 0 1.7321 2.0000 1 1 1.7321 0 1 1 1.9149 1.7321 0 1.7321 1.9149 1 1 0


D :

R

1.7321 1 1 2.0000 1.7321 0 1.7321 1.7321 1 0 1 1.9149 1 1 1.9149 1.7321 0 1.6330 1.4142 0 1 1 1.9149 1 1 1.7321 1.6330 0 1.4142 0 1 1 1 1.7321 1 1 1.4142 1.4142 0 0 0 0 0 0 0 0 0 0 0 0

 

 





0 0 0 0 1.4142 0 1.3333 0.4714 0 −0.0000 −0.0000 −1.0000 −0.5000 0.7071 0.5000 1.0000 1.4142 −0.0000 0.8333 −0.2357 −0.5000 −0.5000 0.7071 −0.5000 0.5000 0.7071 0.5000 0.5000 0.7071 −0.5000

C :

R

 

 





0 0 0 0 1.4142 0 −1.3333 0.4714 0 −0.0000 −0.0000 1.0000 0.5000 0.7071 −0.5000 −1.0000 1.4142 −0.0000 −0.8333 −0.2357 0.5000 0.5000 0.7071 0.5000 −0.5000 0.7071 −0.5000 −0.5000 0.7071 0.5000

C :

R

 

 

###### +Graph 665605 (note that as a 24 contact A this is a non-iterative graph, but as a 25 contact packing (D) it is iterative):





0 0 0 0 1.7321 0 1.6329 1.1549 0 0.5443 0 −0.8333 −0.0001 0.8660 0.5000 0.8164 1.4434 −0.5002 0.8164 1.4434 0.5002 1.3609 0.6736 −0.8333 −0.0001 0.8660 −0.5000 0.8164 0.5774 −0.0000





0 0 0 1 1 0 0 0 1 1 0 0 0 0 1 1 1 0 1 0 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 0 1 1 1

A :

- 0 1 1 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 1 1 1 0 1 1 1 0 0 0 1
- 1 0 1 1 1 1 1 1 1 0


 

 

C :

R





- 0 1.7321 2.0000 1 1 1.7321 1.7321 1.7321 1 0 1.7321 0 1.7319 1.9148 1 1 1 1.9149 1 0 2.0000 1.7319 0 1.7321 1.7321 1 1 1 1.7321 0
- 1 1.9148 1.7321 0 1.6330 1.4141 1.9149 1 1 0 1 1 1.7321 1.6330 0 1.4143 1 1.9149 1 0


D :

R

1.7321 1 1 1.4141 1.4143 0 1.0003 1 1 0 1.7321 1 1 1.9149 1 1.0003 0 1.6331 1.4143 0 1.7321 1.9149 1 1 1.9149 1 1.6331 0 1.4143 0

 

 

1 1 1.7321 1 1 1 1.4143 1.4143 0 0 0 0 0 0 0 0 0 0 0 0

 

 

##### APPENDIX C: PSEUDO CODE

Here we include a list of changes that were made in the code since our last paper (PRL, 103, 118303). The entire code, both old and new versions of it, can be downloaded from the following website: http://people.seas.harvard.edu/∼narkus/. We also include the algorithm for the triangular bipyramid rule, as applied to iterative packings, in which case equation 10 of the main text can be applied directly:

1. Changes Made to Code

- 1. In rare cases, for some of the triangular bipyramids, there are dihedral angles that are not deﬁned. This occurs when >= 3 points lie on a line. This occurs in certain packings that contain octahedra. In these cases, the global consistency check that is normally performed and checks for the sum and diﬀerences of dihedral angles is not valid. In the old code, running this check when the dihedral angle was not deﬁned caused some physical packings to be erroneously ruled out as globally inconsistent and thus unphysical. Now, the global consistency check (in the function ‘global consistency check’) ﬁrst checks to see that all dihedral angles are well deﬁned - if they are, the check proceeds as normal, if they’re not then a special global consistency check for 3 points lying in a line (as was described in section 4.2 of the main text of the paper) is performed. Making this correction caused 2 more packings to be realized at n = 9 and the bulk of the 39 more packings that were found at n = 10 to be realized.

- 2. ‘round numi’ and ‘preci,’ where ‘i’ is a number, has been entered in various functions as an easier way to control the round-oﬀ numbers. Some of the round-oﬀ numbers have been changed so that less error is introduced as a result of these numbers. This only aﬀects the number of packings found at n = 10, and accounts for around 2 more packings being found.

In particular, ‘prec2’ in the function ‘check round’ has been changed from -6 to -10. This means that the precision to which we check that a certain quantity = 0 is performed to 10−10 instead of 10−6.

- 3. All functions that check for 9 particle physical new seeds now ﬁrst check to see that the distance between 2 particles, rij, is unknown before writing in the distance corresponding to the appropriate rij of that seed. (This prevents any already known distances being overwritten). In the old code, only 1 of the 9 particle new seed functions performed this check. For the functions that did not perform this check, occasionally an already known distance was erroneously overwritten and this in some cases caused a physical packing to be erroneously ruled out as unphysical. Correcting this error also only aﬀects the number of packings found at n = 10; it also accounts for several more packings being found.


2. Algorithm

- 1. Loop through A. Each Aij = 0 corresponds to an unknown rij. Keep track of which distances are unknown.
- 2. For each unknown rij (a) Construct each possible ditetrahedron until one with all 9 distances in −→r is found.


- (i) Calculate rij using the triangular bipyramid rule.

- (A) If a solution exists, rij will fall out immediately. If rij < R, discard the solution as it is unphysical.
- (B) If a solution does not exist, this A is unphysical – move on to the next A. A solution will not exist if the triangle inequality is violated – this will show up as the absolute value of the argument of cos−1 being > 1, which is undeﬁned (yielding NaN).


- (ii) Store all physically consistent rij. (These are locally consistent solutions, global consistency must still be checked).


(b) If no ditetrahedron with known −→r exists, move on to the next rij and repeat step 2a. 3. If any unknown rij remain, repeat step 2a. (This will be repeated until all rij are solved).

4. Check for global consistency. The dihedral angle A1 is given by

 

A2 + A3 |A2 − A3|

A1 =

2π − (A2 + A3) 2π − |A2 − A3|



(In calculating rij in equation 15 of the main text, we need not consider the latter two A1 solutions as cos(2π − x) = cos(x)).

For each potential set of solutions rij, construct all possible ditetrahedra in the structure. If ∃ ditetrahedra where A1 is not satisﬁed by one of the above formulas, then the solution set is globally inconsistent, and should be discarded.

For each iterative packing, all rij can be solved via this algorithm.

###### School of Engineering and Applied Sciences, Harvard University, Cambridge, MA 02138

