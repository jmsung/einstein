### Topological modes bound to dislocations in mechanical metamaterials

Jayson Paulose, Bryan Gin-ge Chen, and Vincenzo Vitelli∗

Instituut-Lorentz, Universiteit Leiden, 2300 RA Leiden, The Netherlands

# arXiv:1406.3323v2[cond-mat.soft]23Apr2015

Mechanical metamaterials are artiﬁcial structures with unusual properties, such as negative Poisson ratio, bistability or tunable vibrational properties, that originate in the geometry of their unit cell [1–5]. At the heart of such unusual behaviour is often a soft mode: a motion that does not signiﬁcantly stretch or compress the links between constituent elements. When activated by motors or external ﬁelds, soft modes become the building blocks of robots and smart materials. Here, we demonstrate the existence of topological soft modes that can be positioned at desired locations in a metamaterial while being robust against a wide range of structural deformations or changes in material parameters [6–10]. These protected modes, localized at dislocations in deformed kagome and square lattices, are the mechanical analogue of topological states bound to defects in electronic systems [11–14]. We create physical realizations of the topological modes in prototypes of kagome lattices built out of rigid triangular plates. We show mathematically that they originate from the interplay between two Berry phases: the Burgers vector of the dislocation and the topological polarization of the lattice. Our work paves the way towards engineering topologically protected nano-mechanical structures for molecular robotics or information storage and read-out.

Central to our approach is a simple insight: mechanical structures on length scales ranging from the molecular to the architectural can often be viewed as networks of nodes connected by links [15]. Whether the linking components are chemical bonds or metal beams, mechanical stability depends crucially on the number of constraints relative to the degrees of freedom. When the degrees of freedom exceed the constraints, the structure displays excess zero (potential) energy modes. Conversely, when the constraints exceed the degrees of freedom, there are excess states of self-stress—balanced combinations of tensions and compressions of the links with no resultant force on the nodes. The generalized Maxwell relation [16] stipulates that the index ν given by the diﬀerence between the number of zero modes, nm, and the number of states of self-stress, nss, is equal to the number of degrees of freedom Ndf minus the number of constraints Nc

ν ≡ nm − nss = Ndf − Nc. (1)

∗ vitelli@lorentz.leidenuniv.nl

A trivial way to position a zero-energy mode in the interior of a generic rigid lattice is to remove some bonds, locally reducing the number of constraints. Consider, instead, a network that satisﬁes everywhere the local isostatic condition Ndf = Nc (which precludes bond removal). In this case, zero modes can only be present in conjunction with an equal number of states of selfstress, invisible partners from the perspective of motion. Isostaticity by itself, however, does not dictate how the modes are distributed spatially. Kane and Lubensky [6] recently introduced a special class of isostatic lattices that possesses an additional feature called topological polarization. Much as an electrically polarized material can localize positive and negative charges at opposite boundaries, a topologically polarized lattice can harbour zero modes or states of self-stress at sample edges (whose outward normal is respectively aligned or anti-aligned with the polarization). The edge mode distribution is biased even though both boundaries are indistinguishable on the basis of local constraint counting. Furthermore, this bias is insensitive to local variations in bond lengths, spring constants, or node masses, provided no bonds are cut and the lattice remains rigid in the bulk [6].

In this Letter, we harness the topological polarization to place zero modes in the interior of an isostatic lattice where topological defects called dislocations are positioned. Dislocations are termination points of incomplete lattice rows that have an edge-like character. They are characterized by a topological charge called the Burgers vector, b, that measures the deﬁcit in any circuit surrounding the dislocation, see Figs. 1a and 1c. A dislocation is composed of a dipole of under-coordinated (green) and over-coordinated (orange) points (Fig. 1a) or plaquettes (Fig. 1b–d), whose orientation is obtained upon rotating b by π/2. The dipole moment d, a vector connecting the under-coordinated point/plaquette to the over-coordinated one, points outward from the added strip of material that terminates at the dislocation and has a magnitude equal to the strip width. Therefore, d quantiﬁes the orientation and size of the eﬀective “edge” created by the dislocation.

To localize topological modes at these eﬀective edges, we need to incorporate the dislocations into polarized lattices without modifying the local constraint count (i.e. trivial zero modes must be excluded). We demonstrate this construction for two polarized lattices: a deformed kagome lattice introduced in Ref. 6 and a deformed square lattice. As shown in Fig. 1, both lattices are obtained by decorating a 2D crystal lattice (regular hexagonal and square, with primitive vectors {a1,a2} indicated in Figs. 1a and 1c respectively) with a multi-atom basis at each unit cell. In the absence of defects, the unit cell

![image 1](<2014-paulose-topological-modes-bound-dislocations_images/imageFile1.png>)

![image 2](<2014-paulose-topological-modes-bound-dislocations_images/imageFile2.png>)

a b

PT

- a1

- a2


b d

d

c

d

![image 3](<2014-paulose-topological-modes-bound-dislocations_images/imageFile3.png>)

![image 4](<2014-paulose-topological-modes-bound-dislocations_images/imageFile4.png>)

PT

b

d d

a2

a1

- FIG. 1. Dislocations in polarized isostatic lattices. a, Hexag-


onal lattice with primitive vectors {a1, a2}. The lattice includes an elementary dislocation, consisting of a ﬁve-coordinated point (green) connected to a seven-coordinated point (orange) in an otherwise six-coordinated lattice (blue points). The Burgers vector b = −a2 is the deﬁcit in a circuit (black dashed line) that would have been closed in a defect-free lattice. Rotating this vector by π/2 gives the corresponding dipole moment vector d, which connects the ﬁve-coordinated point to the sevencoordinated point. Decorating each unit cell with a three-atom basis (yellow points and magenta bonds) produces a dislocated deformed kagome lattice which contains only four-coordinated points. Three copies of the three-atom basis are shown; solid bonds connect points within the same unit cell whereas dashed bonds connect points belonging to diﬀerent cells. b, Deformed kagome lattice obtained from decorating the triangular lattice in

- a, thus incorporating a dislocation with the same dipole moment d. The ﬁve- and seven-coordinated points in the underlying triangular lattice translate into plaquettes bordered by ﬁve (green) and seven (orange) bonds respectively, whereas all other points in the triangular lattice translate to plaquettes bordered by six bonds (blue) in the decorated lattice. The topological polarization PT = a1, calculated in Ref. 6, is also shown. c, Square lattice with primitive vectors {a1, a2} (black arrows) which incorporates a dislocation, consisting of a three-coordinated plaquette (bordered by green bonds) adjacent to a ﬁve-coordinated plaquette (bordered by orange and green bonds), with Burgers vector
- b = −(a1 + a2). The associated dipole moment d connects the three- and ﬁve-coordinated plaquettes. Decorating each point with the four-point unit cell (yellow points and magenta bonds) gives the distorted square lattice in d which incorporates a dislocation of the same dipole moment, and has a nonzero topological polarization PT = a1 − a2.


determines the topological polarization PT of the bulk lattice. In Appendix A we show that PT = a1 − a2 for the deformed square lattice while it was shown in Ref. 6 that PT = a1 for the deformed kagome lattice. Dislocations in the undecorated lattice carry over to the polarized lattice and, when appropriately chosen, produce a lattice that is four-coordinated everywhere (Figs. 1b and 1d). See Appendix B for more details of the construction.

Having constructed polarized lattices with dislocations, we numerically compute their vibrational spectrum by treating each bond as a harmonic spring. Results are shown in Figs. 2a and 2b for deformed kagome and square networks respectively. We use periodic boundary conditions, which preserves isostaticity everywhere but requires a net Burgers vector of zero. As a result, dislocations appear in pairs with equal and opposite dipole moment. In both networks, the dipole moments of the dislocation on the left (dL = (2/√3)(a1 − a2/2) for the kagome network and dL = a1 − a2 for the square network) and on the right (dR = −dL) are respectively aligned with and against the lattice polarization. The left dislocation has an associated soft mode in both cases, labeled by arrows, whose energy decreases with system size. The opposite dislocation is associated with an approximate state of self-stress, labeled by colored and thickened bonds following Ref. 6. (See Appendix C for computational details.) These observations are consistent with the intuitive interpretation of dislocations as edges oriented by their dipole moment.

To assess whether these modes can be observed in metamaterials with realistic bonds, joints and boundary conditions, we have built prototypes of the deformed kagome lattice, composed of rigid triangles laser-cut out of 3 mm thick PMMA sheets. The corner of the triangles are connected by plastic bolts that act as hinges. The boundary points are pinned to a ﬂat base by screws, but can pivot freely. The design ensures that each internal vertex has as many constraints as degrees of freedom, satisfying the local isostatic condition away from the boundary. Fig. 2c shows such a prototype mimicking the dislocation conﬁguration of the computer model from Fig. 2a. Theoretically, the boundary pinning and the use of rigid triangles push the phonon gap to inﬁnity, so that only zero modes can be observed. In practice, the prototype has some compliance and mechanical play at the pivots. Nonetheless, it is rigid in the bulk, as can be veriﬁed by unsuccessfully trying to move the (white) triangles far from the dislocations, see Supplementary Movie 1.

Despite the diﬀerences between the two systems, the soft mode observed in the simulated harmonic network survives in the real-world prototype as a collective motion of points near the left dislocation. The motion is easily activated by pushing the hinge joints of the triangles that make up the dislocation (inset to ﬁgure 2c and Supplementary Movie 2). The motion is not a strict zero mode because it interacts with the pinned boundary of the ﬁnite system, but the structural compliance is suﬃcient

- a
- b


|PT|
|---|


dL

dR

a2

a1

|PT|
|---|


|dR|
|---|


|dL|
|---|


a2

a1

c

![image 5](<2014-paulose-topological-modes-bound-dislocations_images/imageFile5.png>)

dL dR

|![image 6](<2014-paulose-topological-modes-bound-dislocations_images/imageFile6.png>)|
|---|


- FIG. 2. Mechanical modes localized at defects. a, Visualization in a deformed kagome lattice of a numerically-obtained low-energy soft mode (red arrows, showing direction and relative amplitude of allowed displacements) and an approximate state of self-stress (thickened bonds, showing bond forces in magenta (+) and blue (-) that cancel each other) associated with a pair of dislocations with


equal and opposite dipole moments dL and dR. The dislocations are in the interior of a lattice with periodic boundary conditions that is perfectly isostatic. Only a small region of the lattice is shown. Each dislocation consists of a ﬁve-coordinated plaquette (enclosed by green triangles) adjacent to a seven-coordinated plaquette (enclosed by green and orange triangles). b, Section of a deformed square lattice of a numerically-obtained low-energy soft mode and a state of self-stress associated with a pair of dislocations with equal and opposite dipole moments dL and dR. The visualization method is similar to that in a. The dislocations are in the interior of a lattice with periodic boundary conditions that is perfectly isostatic. Each dislocation consists of a three-coordinated plaquette (enclosed by cyan plaquettes) near a ﬁve-coordinated plaquette (enclosed by cyan and yellow plaquettes). All other plaquettes are four-sided. c, Plastic prototype of a deformed kagome network, built as described in the text. The interior contains two dislocations which reproduce the conﬁguration from the computer model show in a. Scale bar 5 cm. Inset, Superposition of three conﬁgurations that span the range of the free motion associated with the left dislocation.

for the remnant soft motion to be observed. In contrast, the dislocation on the right does not admit displacements in its vicinity and remains rigid (Supplementary Movie 3), consistent with the simulations.

To quantify the number and type of modes associated with a dislocation, an electrostatic analogy proves useful. Once the connectivity of a locally isostatic lattice is ﬁxed, the index ν in equation (1) can be viewed as a topological charge, invariant under smooth deformations of the lattice. Just as Gauss’s law yields the net charge enclosed in a region from the ﬂux of the electric polarization through its boundary, the net value of ν in an arbitrary portion of an isostatic lattice is given by the ﬂux of the topological polarization through its boundary [6]. Upon evaluating the ﬂux of PT on a contour encircling an isolated dislocation, we obtain

1 Vcell

PT · d, (2)

ν =

where Vcell is the unit cell area. In Appendix D, we present a detailed derivation of equation (2) that accounts for the elastic strains around the dislocation. Here, we simply comment on its physical interpretation.

The topologically protected modes arise from a delicate interplay between a Berry phase associated with cycles in the Brillouin zone, embedded in PT [6], and the Berry phase of a topological defect in real space, represented by its Burgers vector (or dipole d). A similar interplay dictates the existence of localized electronic modes at dislocations in conventional topological insulators [12, 13]. Equation (2) gives ν = +1(−1) for the left (right) dislocation in the deformed kagome lattice, and ν = +2(−2) in the deformed square lattice. The sign of ν distinguishes zero modes (+) from states of self-stress (−), while its magnitude gives their numbers. For instance, we correctly predict that the square lattice of Fig. 2b admits two soft modes localized to the left dislocation (as veriﬁed in Supplementary Figure S1).

The soft modes investigated here have unusual local-

ization properties as shown in Fig. 3. The mode amplitude falls oﬀ exponentially along most rays originating at the core of the left dislocation, but the decay length depends on the direction of the ray relative to the underlying lattice. There are two special directions in each lattice (one of which is highlighted by red circles in both Fig. 3a and Fig. 3b) along which the localization is weak. In all other directions, the mode decays over much shorter length scales of order a few lattice constants (green circles and symbols in Fig. 3). In Appendix E, we show that the weak localization directions track lines in momentum space along which the acoustic modes vary quadratically, rather than linearly, with the momentum. The localization of the approximate state of self-stress behaves similarly, with weak directions that are the opposite of those for the soft mode.

The topologically protected modes we have identiﬁed could have applications across a wide range of systems and length scales. At macroscopic scales, isostatic origami structures exist whose deformations are restricted to rotations of hinged triangles much as in the kagome lattice [17]. At the microscale, dislocations could be used for robust information storage, with a bit encoded by the presence (+) or absence (-) of a topological soft mode, in turn controlled by the orientation of the Burgers vector. Such protected bits could be hardwired into microscopic “punch cards” which can be read out mechanically by probing the region around dislocations for soft motions (or lack thereof). We also envision molecular robots and smart metamaterials that exploit the protected modes as activated mechanisms.

Acknowledgements: We thank J. C. Y. Teo, R.J. Slager, and A. Turner for helpful discussions, the Leiden University Fine Mechanics Department, and the anonymous referees for detailed feedback. This work was funded by FOM and by the D-ITP consortium, a program of the Netherlands Organisation for Scientiﬁc Research (NWO) that is funded by the Dutch Ministry of Education, Culture and Science (OCW).

- [1] Babaee, S., Shim, J., Weaver, J. C., Patel, N. & Bertoldi, K. 3d soft metamaterials with negative poisson’s ratio. Advanced Materials 25, 5044–5049 (2013).
- [2] Schenk, M. & Guest, S. D. Geometry of miura-folded metamaterials. Proceedings of the National Academy of Sciences 110, 3276–3281 (2013).
- [3] Wei, Z. Y., Guo, Z. V., Dudte, L., Liang, H. Y. & Mahadevan, L. Geometric mechanics of periodic pleated origami. Phys. Rev. Lett. 110, 215501 (2013).
- [4] Sun, K., Souslov, A., Mao, X. & Lubensky, T. C. Surface phonons, elastic response, and conformal invariance in twisted kagome lattices. Proceedings of the National Academy of Sciences 109, 12369–12374 (2012).
- [5] Shan, S. et al. Harnessing Multiple Folding Mecha-


- nisms in Soft Periodic Structures for Tunable Control of Elastic Waves. Advanced Functional Materials (Early View) (2014). URL http://doi.wiley.com/10.1002/ adfm.201400665. DOI: 10.1002/adfm.201400665.
- [6] Kane, C. L. & Lubensky, T. C. Topological boundary modes in isostatic lattices. Nature Physics 10, 39–45

(2014). URL http://www.nature.com/doifinder/10. 1038/nphys2835.

- [7] Prodan, E. & Prodan, C. Topological Phonon Modes and Their Role in Dynamic Instability of Microtubules. Physical Review Letters 103, 248101 (2009). URL http:// link.aps.org/doi/10.1103/PhysRevLett.103.248101.
- [8] Vitelli, V. Topological soft matter: Kagome lattices with a twist. Proceedings of the National Academy of Sciences


a b

|![image 7](<2014-paulose-topological-modes-bound-dislocations_images/imageFile7.png>)|
|---|


|![image 8](<2014-paulose-topological-modes-bound-dislocations_images/imageFile8.png>)|
|---|


10-1

10-1

Amplitude

Amplitude

10-2

10-2

10-3

10-3

0 5 10 15 20 25 30 35

0 10 20 30 40 50 60 70 80

| |
|---|


| |
|---|


| |
|---|


| |
|---|


Distance from dislocation core

Distance from dislocation core

| |
|---|


| |
|---|


| |
|---|


- FIG. 3. Anisotropic localization of the soft mode. a, Amplitude of the soft mode associated with the left dislocation in the kagome lattice shown in ﬁgure 2a, visualized as blue disks whose area is scaled by the displacement magnitude at each lattice point. The


dipole moment vectors dL and dR (solid arrows) indicate the position and orientation of the dislocations. Inset, Soft mode amplitude as a function of distance from the left dislocation, along two directions (indicated by red and green circles in the main panel which enclose the lattice points sampled in the red and green curves respectively). b, Same as in a for the soft mode associated with the left dislocation shown in ﬁgure 2b.

109, 12266–12267 (2012).

- [9] Chen, B. G.-g., Upadhyaya, N. & Vitelli, V. Nonlinear conduction via solitons in a topological mechanical insulator. Proceedings of the National Academy of Sciences of the United States of America 111, 13004–9 (2014). URL http://www.pubmedcentral.nih.gov/articlerender. fcgi?artid=2154402&tool=pmcentrez&rendertype= abstracthttp://arxiv.org/abs/1404.2263http: //www.ncbi.nlm.nih.gov/pubmed/25157161. 1404.2263.
- [10] Vitelli, V., Upadhyaya, N. & Chen, B. G.-g. Topological mechanisms as classical spinor ﬁelds. arXiv preprint arXiv:1407.2890 (2014). URL http://arxiv.org/abs/ 1407.2890v2.
- [11] Stern, A. Anyons and the quantum Hall eﬀectA pedagogical review. Annals of Physics 323, 204–249 (2008). URL http://linkinghub.elsevier.com/retrieve/ pii/S0003491605000394http://linkinghub.elsevier. com/retrieve/pii/S0003491607001674.
- [12] Ran, Y., Zhang, Y. & Vishwanath, A. One-dimensional topologically protected modes in topological insulators with lattice dislocations. Nature Physics 5, 298–303

(2009). URL http://www.nature.com/doifinder/10. 1038/nphys1220.

- [13] Teo, J. C. Y. & Kane, C. L. Topological defects and gapless modes in insulators and superconductors. Physical Review B 82, 115120 (2010). URL http://link.aps. org/doi/10.1103/PhysRevB.82.115120.
- [14] Juricˇi´c, V., Mesaros, A., Slager, R.-J. & Zaanen, J. Universal Probes of Two-Dimensional Topological Insulators: Dislocation and π Flux. Physical Review Letters 108, 106403 (2012). URL http://link.aps.org/doi/


- 10.1103/PhysRevLett.108.106403.
- [15] Maxwell, J. C. On the calculation of the equilibrium and stiﬀness of frames. Philosophical Magazine 27, 294–299

(1864).

- [16] Calladine, C. Buckminster Fuller’s Tensegrity structures and Clerk Maxwell’s rules for the construction of stiﬀ frames. International Journal of Solids and Structures 14, 161–172 (1978). URL http://linkinghub. elsevier.com/retrieve/pii/0020768378900525.
- [17] Tachi, T. Designing freeform origami tessellations by generalizing Resch’s patterns. Journal of Mechanical Design 135, 111006 (2013).
- [18] Graver, J. E., Servatius, B. & Servatius, H. Combinatorial rigidity, vol. 2 (American Mathematical Soc., 1993).
- [19] Seung, H. & Nelson, D. Defects in ﬂexible membranes with crystalline order. Physical Review A 38, 1005– 1018 (1988). URL http://link.aps.org/doi/10.1103/ PhysRevA.38.1005.
- [20] Kapko, V., Treacy, M. M., Thorpe, M. F. & Guest, S. On the collapse of locally isostatic networks. Proceedings of the Royal Society A: Mathematical, Physical and Engineering Science 465, 3517–3530 (2009).
- [21] Landau, L. D. & Lifshitz, E. M. Theory of Elasticity (Butterworth Heinemann (Oxford)), 3 edn.


Appendix A: Calculation of the topological polarization

Here we summmarize the calculation of the topological polarization following Ref. 6. The topological polarization is calculated from the rigidity, or compatibility, matrix R that relates bond extensions ei = Rijuj to site displacements ui [16, 18]. The ﬁrst step is to calculate the Fourier-transformed rigidity matrix R(k) whose determinant is complex: detR(k) ≡ |detR(k)|eiφ(k) (done with a choice of unit cell consistent with the calculations in Ref. 6). Next, the winding numbers, ni = {n1,n2}, of φ(k) are evaluated using

- 1

- 2π C


ni = −

i

dk · ∇kφ(k) (A1)

along the two cycles {C1,C2} of the Brillouin zone parallel to the reciprocal lattice directions (b1,b2), deﬁned by ai·bj = 2πδij [6]. The winding numbers are invariants of the gapped lattice; smooth deformations of the triangle shape do not change ni unless the sites in the lattice lie in a special position and cause the phonon gap to close. We deﬁne the topological polarization to be

PT =

i

niai. (A2)

This deﬁnition of PT diﬀers from that of Ref. 6 by a factor of Vcell (theirs is strictly speaking a polarization density). Our PT is equal to RT in Ref. 6 since the correction r0 = d i sites pi − j bonds pj (where pa is the position of site / bond a) is equal to zero for our choices of unit cells. For the deformed square lattice used in the main text, the Fourier-transformed rigidity matrix is calculated from the unit cell site positions (given in section B2) and bond assignments, and the numericallyobtained winding numbers are n1 = 1,n2 = −1. Thus the resulting lattice is characterized by the topological polarization PT = a1 − a2 in terms of the primitive vectors ai indicated in Fig. 1c of the main text.

Appendix B: Constructing isostatic networks with dislocations

The basic principle for constructing isostatic networks with dislocations was outlined in the main text and Fig. 1. Here we provide more details about the procedure for constructing the lattices used in numerical calculations and the real-world prototypes.

##### 1. Deformed kagome lattice

Following Ref. 6, deformed kagome lattices with nontrivial polarization are obtained by decorating a regular hexagonal lattice with a unit cell consisting of three

points and six bonds. The underlying hexagonal lattice is built from the primitive lattice vectors a1 = axˆ, a2 = (a/2)ˆx + (√3a/2)ˆy where a is the lattice constant and x,ˆ yˆ are unit vectors. Decorating a hexagonal lattice with N points and 3N bonds produces a deformed kagome lattice with 3N points and 6N bonds. We use the parametrization of the unit cell introduced in Ref. 6 to describe deformed kagome lattices with no asymmetry in the constituent triangles: three numbers (x1,x2,x3) quantify the distortion of the lines of bonds away from the straight lines in a regular kagome lattice (xi = 0). Any set of three values xi speciﬁes the positions of the three points in the unit cell. Equivalently, each bond in the hexagonal lattice is associated with a single point in the kagome lattice. Therefore, for any set of xi, each bond in a hexagonal lattice can be replaced with a point whose position is calculated from the bond endpoints and the xi values. Linking up these new points following the bond assignments dictated by the kagome lattice unit cell produces the required deformed kagome lattice as a decoration of the hexagonal lattice.

Numerical lattices with dislocations are prepared starting from a defect-free hexagonal lattice with points connected by harmonic springs of length a and spring constant k under periodic boundary conditions (the system is a rectangular box with dimensions speciﬁed to match the size of the ﬁnite hexagonal lattice). Using local bond reassignments, a dislocation pair with net zero Burgers vector can be prepared at any location; the individual dislocations can then be moved around independently of each other through a combination of glide and climb steps to obtain the desired separation. The presence of defects necessarily introduces strains in the lattice. Between each glide and climb step, the network of points and springs is relaxed to their (local) minimum energy conﬁguration using a conjugate gradient algorithm. This procedure approximates the elastic strains in a membrane with 2D Young’s modulus 2k/√3 and Poisson ratio 1/3 [19]. Fig. 1a (main text) shows such an equilibrium conﬁguration around a dislocation in a hexagonal lattice.

Once a relaxed hexagonal lattice with dislocations in the required locations has been created, the decoration described above is carried out. Far away from the defects, the resulting lattice reproduces the relative point positions and bond lengths of the deformed kagome lattice parametrized by the xi. However, in the strained regions of the lattice close to the dislocations, the decorated lattice necessarily has triangles that are distorted from their ideal strain-free shape prescribed by the xi. The dynamical modes of this lattice made out of non-equal triangles can still be numerically calculated (following section C) under the assumption that every bond is tension-free (i.e. by assigning the bond rest lengths to be exactly equal to the point separations in the decorated lattice), and the resulting spectrum includes approximate zero modes and states of self-stress that follow the count of equation (2), main text. The modes shown in Fig. S3 are calculated using this method, which guarantees that the unit cell

matches the expectation from the xi far away from the defects but at the cost of having irregular triangles near the defect cores.

As mentioned above, elastic distortions of some unit cells are unavoidable when preparing kagome networks from hexagonal lattices with defects under periodic boundary conditions. However, we can reduce the distortions in the triangles making up the kagome network, to bring their shapes closer to the ideal shape in a defectfree lattice and make them visually similar to the physical prototypes which have of triangles of identical shape. We do this via the following steps:

- 1. Decorate the numerically relaxed hexagonal lattice as described above, replacing each bond with a

point calculated using the choice of xi and linking neighbours according to the kagome lattice bond assignment. There is no ambiguity in assigning neighbours to the points near the core of the dislocation, and this assignment satisﬁes the local constraint count of four neighbours to each site and matches the connectivity of the perfect kagome lattice away from the defect.

- 2. Assign to each bond in the decorated lattice a rest length that matches the rest length in a defect-free

deformed kagome lattice parametrized by xi. This can be unambiguously done for all bonds in the dislocated kagome lattice except for the edges of a single triangle at the core of each dislocation. For this triangle, we make the following choice: we assign bond lengths to its edges in such a way that the ordered bond length assignment in all six-sided plaquettes surrounding the triangle matches that of six-sided plaquettes in the defect-free lattice.

- 3. Relax the network of springs to an equilibrium conﬁguration by minimizing the total harmonic spring energy using a conjugate gradient method. Unlike the hexagonal lattice, the kagome lattice has a large space of low-energy deformations that manifest as rotations of the constituent triangles with minimal stretching of the springs, including the soft mode due to the dislocation as well as the long wavelength phonon modes with anomalously low energy described in section E. These modes dominate the relaxation of the network, leading to large sections of the lattice with self-intersecting triangles or conﬁgurations that deviate signiﬁcantly from the uniform kagome lattice even far away from the defect. To reduce the inﬂuence of the soft modes on the relaxation, we relax the network under a macroscopic strain imposed by increasing the size of the rectangular box, which has the eﬀect of stiﬀening the network response. For the system shown in Fig. 2a, a strain of 10% along the x direction was imposed during the relaxation step.
- 4. The kagome lattice after the spring relaxation step has less shape variation among the constituent tri-


angles and six-sided plaquettes when compared to the lattice before the relaxation step. However, the imposition of a macroscopic strain deforms the unit cell away from the original unit cell deﬁned by the xi. Part of the deformation can be reversed by applying an overall aﬃne deformation to the network that reverses the uniform strain applied in the previous step, returning the periodic box dimensions to their values before the relaxation step. Far away from the dislocations, the network approaches a deformed kagome lattice still built on a hexagonal lattice with primitive vectors a1,a2 unchanged from before, but parametrized by a new set of values x˜i that are close to the original xi.

Upon following the above steps, we obtain a deformed kagome lattice that accommodates the strains required by the dislocations without drastic diﬀerences in the shapes of the constituent triangles. The network used for the numerical calculations in Fig. 2a had (x1,x2,x3) = (0.1,−0.1,−0.1) before the relaxation step, which resulted in a deformed kagome lattice parametrized by (˜x1,x˜2,x˜3) ≈ (0.12,−0.06,−0.06) away from the dislocation after all steps were followed. The changes in the unit cell due to the relaxation are too small to aﬀect the topological polarization, which depends only on the sign of the xi [6]. Therefore, we have a reliable procedure to numerically generate deformed kagome lattices, incorporating dislocations under periodic boundary conditions, with a desired topological polarization within the class of lattices introduced in Ref. 6. As Fig. 2a shows, triangles in the network are still distorted by a small amount near the dislocations, because the strains around dislocations in a periodic system cannot be fully accommodated by triangle rotations alone. To calculate the approximate zero modes and states of self-stress, we again redeﬁne the rest lengths of the bonds to match the separations between points in the relaxed conﬁguration so that the network is free of tensions.

Generating deformed kagome networks with dislocations out of near-identical triangles is more straightforward in the physical prototypes. We start with identical laser-cut acrylic triangles with circular holes at the corners. The center-to-center distances of the holes are equal to the bond lengths in a deformed kagome lattice parametrized by (x1,x2,x3) = (0.1,−0.1,−0.1). We join pairs of triangles at corners with plastic fasteners, which act as hinges. Dislocations can be wired in without diﬃculty, because of the numerous extra degrees of freedom introduced by the free boundary of the system. These additional degrees of freedom make the structure very ﬂoppy, with many unconstrained rotations of triangles about their corner pivots available to accommodate the dislocations. The ﬂoppiness is removed from the prototypes by pinning down the boundary points, ultimately producing an overconstrained system. In Fig. 2c, the eﬀect of the dislocations on the network is seen in the (bond length-preserving) distortions of unit cells. The small size of the ﬁnite prototype means that the distor-

tions are seen all the way to the boundary, but their amplitude is expected to fall oﬀ exponentially over a length scale set by the separation between the dislocations of equal and opposite Burgers vector. A sample many times larger than that constructed could be made to approach a distortion-free kagome lattice at the boundary.

##### 2. Deformed square lattice

Square lattices are another example of isostatic lattices in two dimensions. The regular square lattice, although locally isostatic, does not harbour topologically protected modes since it does not have a gapped phonon spectrum. The presence of straight lines of bonds extending across the lattice gives rise to 2L states of self-stress in an L × L system, and 2L corresponding zero modes according to equation (1). These show up as lines of zero modes along kx = 0 and ky = 0 in Fourier space. However, the gap can be opened up everywhere except at k = 0 by decorating the square lattice with a suitable 2 × 2 unit cell that breaks up the straight lines of bonds. The topologically nontrivial deformed square lattice we use in the main text was obtained by randomly perturbing a regular 2 × 2 unit cell on a regular square lattice with primitive vectors a1 = axˆ, a2 = ayˆ. The positions of the four points in the unit cell, deﬁned modulo shifts by Bravais lattice vectors, are [(0,0),(0.51a,−0.27a),(0.63a,0.58a),(−0.07a,0.42a)]. We have checked numerically that the phonon gap for this particular unit cell closes only at k = 0, which makes PT a well-deﬁned quantity. See section A for details of the calculation of the polarization vector PT.

The elementary dislocation in a square lattice (with Burgers vector equal to ±ai) can be viewed as a bound pair of two disclinations (defects in lattice orientational order): a lattice point with ﬁve-fold symmetry adjacent to a plaquette with three-fold symmetry. The three-fold lattice point disrupts the isostaticity of the Bravais lattice, and also of the resulting crystal lattice after decoration with the 2×2 basis. To prepare dislocations that do not change the local balance between degrees of freedom and constraints, we instead use pairs of disclinations centered on interstitial regions (plaquettes) rather than on lattice points; an example is shown in Fig. 1c of the main text. Since no lattice point disclinations are used, every lattice point still has exactly four bonds emanating from it. Dislocations constructed in this manner have one of four possible Burgers vectors b = ±(a1 ± a2), oriented along diagonals of the square plaquettes of the principal lattice. A square lattice incorporating such a dislocation can be decorated with a 2 × 2 basis to obtain a lattice that maintains isostaticity at each point.

As with the deformed kagome lattices, we numerically create square lattices with dislocation pairs by starting from a defect-free regular lattice, creating a dislocation pair, and separating the pair using glide and climb steps. Between each step we relax the network to its equilibrium

structure. To do this, we ﬁrst ﬁll in the next-nearestneighbour bonds in the structure so that the network has non-zero bulk and shear moduli. The result is a regular square lattice with elastic strains surrounding the dislocations, as shown in Fig. 1c. Upon decorating this lattice with the 2×2 unit cell while ignoring the strains, we again obtain distorted unit cells close to the defects. We reduce the distortions by following the steps 1–4 outlined for the kagome lattice in the previous section, relaxing the network under external strain after assigning rest lengths to bonds that match the rest lengths in a defect-free lattice with the same 2 × 2 basis. The unit cell does not deﬁne the rest lengths of the bonds traversing the edge shared by the three-fold and the ﬁve-fold plaquettes in the base lattice; we arbitrarily reuse rest lengths from the defect-free lattice for these bonds. For the square lattice reported in the main text, we used a macroscopic strain of 5% in both directions during the relaxation step.

Appendix C: Numerically obtaining and visualizing the soft mode and self-stress

The soft mode plotted in Fig. 2a is obtained by constructing and numerically diagonalizing the dynamical matrix associated with the network. The construction of the network itself follows section B1. We start with a hexagonal network of 8,317 nodes in a periodic box of size 128a0 × 32√3a0 which incorporates two dislocations with Burgers vectors ±(a1 − a2), separated by roughly seven lattice constants. We then decorate and relax the lattice to produce a deformed kagome lattice with (x1,x2,x3) ≈ (0.12,−0.06,−0.06) in the parametrization of Ref. 6, which has a topological polarization PT = a1. We obtain a network with 24,951 points and twice as many bonds. Figure 2a is a zoomed-in view of a subset of the relaxed network.

The vibrational modes of the structure around this equilibrium are eigenvalues of the dynamical matrix D = R†R, where the rigidity matrix R relates bond extension ei (one per bond) with node displacement uj (two per node) via ei = Rijuj. The rigidity matrix is calculated from the point positions in the equilibrium conﬁguration (spring constants and node masses are set to 1.) The lowest several eigenvalues (squared frequencies) in order of increasing magnitude and the corresponding eigenvectors of the dynamical matrix are obtained through sparse matrix diagonalization routines implemented in the Python programming language. The two lowest eigenvalue modes (with eigenvalues zero up to machine precision) are the trivial translations available to the network under periodic boundary conditions. The ﬁrst nontrivial eigenvalue (third eigenvalue overall in magnitude) is the proposed topological soft mode associated with the dislocation with dipole moment dA.

Note that the “collapse mode” identiﬁed in periodic locally isostatic networks by Ref. 20 does not show up as a zero mode in the numerical spectra of the ﬁnite networks.

This is because the collapse mode is associated with a change in the shape of the unit cell, and therefore in the shape of the periodic box accommodating a ﬁxed number of unit cells. The numerical calculations are carried out assuming a periodic box of ﬁxed dimensions. Deforming the ﬁnite lattice according to a collapse mode would not deform any of the internal bonds of the structure, but it would deform boundary-crossing bonds connecting edge nodes with periodic images of the primary structure. As a result, the collapse mode has a ﬁnite energy. If in contrast the periodic box in the simulations were allowed to change its shape, the collapse mode of Ref. 20 would be present in the numerical spectra.

In an inﬁnite system, the topological mode would show up as an eigenvector with eigenvalue zero; in the ﬁnite system, it has a ﬁnite frequency due to interactions with the other dislocation and with its periodic images. However, it is well-separated in energy from the succeeding modes. The association of the mode with the dislocation on the left is even more apparent in the structure of the corresponding eigenvector, which has its highest amplitude at nodes in a small region of the lattice primarily near the dislocation. In contrast, the eigenvectors of the fourth and higher-frequency modes have the structure of periodic acoustic modes that extend over the entire lattice.

The eigenvector corresponding to each eigenvalue gives a displacement (a two-dimensional vector) at each point; the magnitude of each displacement vector corresponds to the relative amplitude of the mode at that point. (The absolute magnitude of the displacements has no physical signiﬁcance.) In ﬁgures 2a–b, we have plotted these displacements for the eigenvector corresponding to the third eigenvalue as red arrows, each indicating the direction and scaled in size by the relative magnitude of the displacement of the point at its base. (Red dots replace arrows whose length is less than the dot diameter.)

Whereas the eigenvectors of the dynamical matrix correspond to normal modes, the eigenvectors of its “supersymmetric partner” D˜ = RR† [6] correspond to tensions and compressions experienced by the individual bonds when the system is driven with the normal modes. Each component of the eigenvector translates to a tension on a particular bond. States of self-stress are eigenvectors of the partner matrix with eigenvalue zero; the eigenvector corresponding to the smallest eigenvalue of the partner matrix is localized (i.e. has appreciable tension values) to bonds in the vicinity of the dislocation with dipole moment dB. This eigenvector is visualized in ﬁgure 2b by increasing the width of each bond (linearly over the range w to 4.6w, where w is the width of the thinnest bond in the ﬁgure) by an amount proportional to the magnitude of the tension. The colour on each bond is also set by the tension; it interpolates between blue (negative tensions) and magenta (positive tensions) with gray bonds signifying low or no tension.

The calculation and visualization of modes of the deformed square lattice in Fig. 2b follows a similar proce-

dure. We follow the steps outlined in section B2, starting with a square lattice of 24,766 nodes in a periodic box of dimensions 192a0 × 128a0, and decorate and relax the lattice to get a deformed square lattice of 99,064 points, a small region of which is displayed in Fig. 2b with the soft mode and approximate state of self-stress visualized as described above.

An interesting distinction between the two networks we study numerically in the main text is that the mode count associated with the left dislocation, as predicted by equation (2), is +1 in the deformed kagome lattice and +2 in the deformed square lattice. Fig. S1 veriﬁes the mode count for the square lattice by showing the two lowest eigenmodes of the dynamical matrix for the network used in Fig. 2b, but with pinned boundary conditions. The pinning reduces the interactions between the localized modes and the long-wavelength modes of the system and eliminates the wraparound nature of the long “tail” of the mode in the slow localization direction. This enhances the distinction between the modes localized to the left dislocation and the other low-energy modes, which are not localized to either dislocation. This ﬁgure also shows that pinning the boundary, which creates an overconstrained system which is no longer strictly isostatic, does not eliminate the topological soft modes. This fact is also veriﬁed by the physical prototype based on the deformed kagome lattice.

Appendix D: Zero mode count of a lattice containing a dislocation

Kane and Lubensky [6] proved that the number of zero modes minus the number of states of self-stress in a lattice subsystem S, νS, decomposes into a sum

νS = νLS + νTS, (D1)

where νLS is a “local” count and νTS is a “topological” count. The local count νLS is related to the number of unit cells of the system included in S. If the unit cell is chosen so that the term r0 is zero, then by choosing the subsystem S appropriately, νLS can be arranged to be zero.

If S is bounded by the contour C, Kane and Lubensky [6] showed that νTS is given by the formula

dd−1S Vcell

νTS =

PT · n,ˆ (D2)

C

where nˆ is the inward-pointing normal to the boundary, and Vcell is the d-dimensional volume of the unit cell.

To compute the zero mode count associated with a dislocation, we need to evaluate the integral in Eq. D2 for a path surrounding a single dislocation in a lattice with topological polarization PT (as deﬁned in section A). We consider paths where νLS = 0 to focus on the eﬀects of the dislocation.

We compute this integral by taking into a account the deformations in the lattice due to the dislocation, in the

![image 9](<2014-paulose-topological-modes-bound-dislocations_images/imageFile9.png>)

![image 10](<2014-paulose-topological-modes-bound-dislocations_images/imageFile10.png>)

- FIG. S1. Visualization of the eigenvectors of the dynamical matrix of the network in Fig. 2b with the lowest (left) and next-lowest (right) eigenvalues, when the dynamical matrix is evaluated under pinned boundary conditions. Pinning the boundary is implemented by eliminating the degrees of freedom associated with points within 2a of the boundary, yielding a rigidity matrix with fewer columns. Such a setup replicates the pinned boundary conditions used in the physical prototypes, and results in a system that is overconstrained, yet exhibits soft modes associated with dislocations of the correct orientation.


continuum limit. The dislocation induces a displacement ﬁeld u around it. We can choose a path suﬃciently far away from the dislocation core so that the resulting lattice distortions do not change the topological winding numbers ni from their values in the undistorted lattice. Then, any variation in PT = i niai comes only from changes in the local lattice vectors ai. In the continuum limit (a smaller than the scale of variation of u), these are determined by the displacement ﬁelds, and as a result we have a position-dependent polarization

PTi = PT0i + wji(x)PT0j, (D3) where

wji(x) = ∂ui/∂xj (D4)

is the distortion tensor and P0T is the polarization in the undistorted lattice. Meanwhile, the volume of the dis-

torted unit cell is

Vcell(x) = Vcell0 (1 + wii) (D5) to linear order in the displacements. Writing out Eq. D2 to linear order in wij, we have

dS Vcell0

nˆi PT0i + wjiPT0j − wjjPT0i (D6)

νTS =

∂S

1 Vcell0 S

dA∂i PT0i + wjiPT0j − wjjPT0i (D7)

= −

1 Vcell0 S

dAPT0i [∂iwjj − ∂jwij], (D8)

=

where we use the divergence theorem to convert the line integral to an area integral (note that nˆ is the inward pointing normal to the contour). However, the distortion tensor is related to the Burgers vector via [21]

bk = −

dAεij∂iwjk. (D9)

S

Upon applying the antisymmetric tensor to both sides, we get

εkmbk = −

dAεijεkm∂iwjk (D10)

S

=

=

dA(δimδjk − δikδmj)∂iwjk (D11)

S

dA(∂mwkk − ∂kwmk). (D12)

S

The vector on the left-hand side, obtained by rotating the Burgers vector by π/2 counterclockwise, is the dipole moment associated with the pair of disclinations that make up the dislocation, which we call d. For an elementary dislocation in the hexagonal lattice, this is a vector of length a0 that points from the ﬁvefold to the sevenfold point. Equations D8 and D12 together give the topological count in terms of the disclination dipole moment,

1 Vcell0

PT0iεjibj =

νTS =

1 Vcell0

PT · d. (D13)

Appendix E: Localization properties of topologically protected modes

The numerical results of the main text show that, in certain spatial directions away from the dislocation, the decay of the amplitude of the soft mode associated with a dislocation is much slower than in the other directions (Fig. 3, main text). We observe here that these directions appear to be controlled by the long-wavelength elastic behaviour of the bulk lattice without defects.

The authors of Ref. 6 showed that in the longwavelength limit of the elasticity of the deformed kagome structures with PT = 0, there are two directions in the Brillouin zone which exhibit anomalous dispersion of

![image 11](<2014-paulose-topological-modes-bound-dislocations_images/imageFile11.png>)

#### 11

![image 12](<2014-paulose-topological-modes-bound-dislocations_images/imageFile12.png>)

![image 13](<2014-paulose-topological-modes-bound-dislocations_images/imageFile13.png>)

0.1/a

kx

![image 14](<2014-paulose-topological-modes-bound-dislocations_images/imageFile14.png>)

ky

­0.1/a 0.1/a

![image 15](<2014-paulose-topological-modes-bound-dislocations_images/imageFile15.png>)

0.1/a

![image 16](<2014-paulose-topological-modes-bound-dislocations_images/imageFile16.png>)

kx

ky

­0.1/a 0.1/a

- FIG. S2. Zoomed-out versions of the scatter plots of the mode amplitude from Fig. 3 of the main text. The entire lattice is shown for both the kagome- and square-based topological lattices (consisting of 128 × 64 unit cells for the deformed kagome and 192 × 128 unit cells for the deformed square lattice). The approximate state of self-stress associated with the opposite dislocation is also visualized for each lattice by scaling the thickness of bonds by the magnitude of the tension (green) or compression (red) as in main text Fig. 2. The wrapping of the weak localization direction around the periodic boundaries is apparent. To the top right of each lattice is a density plot of det R as a function of k in the respective Brillouin zone. Below this, a density plot of log det R is shown for a subsection of the Brillouin zone near the origin, to highlight the directions of anomalous dispersion (sharp lines) along


which det R = 0 to quadratic order in (kx, ky). The axes of the Brillouin zone have been swapped to aid the visual comparison of the localization direction in real space and the anomalous dispersion directions in momentum space.

the long-wavelength acoustic modes as a function of the wavevector k = (kx,ky). Along these directions, the bulk modes have a dispersion that scales as ω ∼ k2 rather than the typical situation for acoustic phonon modes which is ω ∼ k. These directions are revealed by expanding the determinant of the Fourier-transformed rigidity matrix R(k) in powers of (kx,ky); along the special directions,

characterized by kx = αiky (i ∈ {1,2}) where α1 and α2 are determined by the unit cell, detR vanishes to quadratic order in k [6]. Therefore, kx = αiky specify lines of modes that are gapless to quadratic order in k, whose energy is made ﬁnite only by the presence of higher-order terms. Such near-gapless lines in the dispersion indicate a multitude of low-energy modes of the

lattice whose associated displacements are constant along the special directions y = αix in real space.

We observe that the directions of weak localization of the topological soft modes in real space tracks these special directions originating in the anomalous dispersion in k-space. Fig. S2 compares the directions of weak localization of the topological modes (dashed lines) to the directions of anomalous dispersion in k-space (sharp lines in density plot). As mentioned earlier, the deformed kagome lattice used for the lattices and prototypes studied in the main text corresponds to (x1,x2,x3) = (.12,−.06,−.06) in the parametrization of Ref. 6. For such a lattice, α1 = −α2 [6] (we obtain speciﬁcally αi = ± (3x1)/(x1 − 4x2) ≈ ±1). We numerically obtain a similar feature in the determinant of the Fourier-transformed rigidity matrix of the deformed square lattice, with the two directions kx = αiky along which detR = 0 to quadratic order in k quantiﬁed by

α1 ≈ 9.995 and α2 ≈ 0.105. In both lattices, the directions of weak localization are consistent with the realspace directions of soft response corresponding to the near-gapless lines, y = αix (the special directions in real space and k-space are related by a π/2 rotation, thus the axes of the Brillouin zone in Fig. S2 have been swapped to make the correspondence more apparent).

This behaviour is conﬁrmed numerically in other members of the class of deformed kagome lattices of Ref. 6, parametrized by (x1,x2,x3) = (x1,−0.1,−0.1), for which α1 = −α2 = (3x1)/(x1 − 4x2). Upon increasing x1 from zero, the weak localization direction in real space tracks the change in anomalous dispersion direction in k-space, as illustrated in Fig. S3, again suggesting that the origin of the former lies in the latter. Establishing the theoretical relation between the two special directions would be an interesting avenue for future work.

(x1,x2,x3) =(0.02,−0.10,−0.10) (x1,x2,x3) =(0.05,−0.10,−0.10)

![image 17](<2014-paulose-topological-modes-bound-dislocations_images/imageFile17.png>)

![image 18](<2014-paulose-topological-modes-bound-dislocations_images/imageFile18.png>)

|![image 19](<2014-paulose-topological-modes-bound-dislocations_images/imageFile19.png>)|
|---|


|![image 20](<2014-paulose-topological-modes-bound-dislocations_images/imageFile20.png>)|
|---|


kx

kx

ky

ky

(x1,x2,x3) =(0.10,−0.10,−0.10) (x1,x2,x3) =(0.20,−0.10,−0.10)

![image 21](<2014-paulose-topological-modes-bound-dislocations_images/imageFile21.png>)

![image 22](<2014-paulose-topological-modes-bound-dislocations_images/imageFile22.png>)

|![image 23](<2014-paulose-topological-modes-bound-dislocations_images/imageFile23.png>)|
|---|


|![image 24](<2014-paulose-topological-modes-bound-dislocations_images/imageFile24.png>)|
|---|


kx

kx

ky

ky

- FIG. S3. Scatter plots similar to Fig. S2 for the numerically-obtained soft mode associated with a dislocation in four diﬀerent


deformed kagome lattice unit cells parametrized by (x1, x2, x3) = (x1, −0.1, −0.1). The lattices are 128 × 64 unit cells in size, and have a dislocation and anti-dislocation with the same orientations and separation as in Fig. 3a of the main text. A section of the defect-free lattice is shown in the upper right corner of each scatter plot to illustrate the unit cell, and a density plot of log det R near the origin of the Brillouin zone is shown in the lower right corner to indicate the directions of anomalous dispersion. The density plot is rendered with kx on the vertical axis to highlight the visual similarity with the directions of weak localization of the soft mode in real space.

