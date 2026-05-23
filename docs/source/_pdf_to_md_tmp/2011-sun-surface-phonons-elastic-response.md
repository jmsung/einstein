arXiv:1112.1109v1[cond-mat.soft]5Dec2011

Isostaticity, auxetic response, surface modes, and conformal invariance in twisted kagome lattices

Kai Sun,1 Anton Souslov,2 Xiaoming Mao,2 and T.C. Lubensky2

1Condensed Matter Theory Center and Joint Quantum Institute, Department of Physics, University of Maryland, College Park, MD 20742, USA 2Department of Physics and Astronomy, University of Pennsylvania, Philadelphia, PA 19104, USA

Model lattices consisting of balls connected by central-force springs provide much of our understanding of mechanical response and phonon structure of real materials. Their stability depends critically on their coordination number z. d-dimensional lattices with z = 2d are at the threshold of mechanical stability and are isostatic. Lattices with z < 2d exhibit zero-frequency “ﬂoppy” modes that provide avenues for lattice collapse. The physics of systems as diverse as architectural structures, network glasses, randomly packed spheres, and biopolymer networks is strongly inﬂuenced by a nearby isostatic lattice. We explore elasticity and phonons of a special class of two-dimensional isostatic lattices constructed by distorting the kagome lattice. We show that the phonon structure of these lattices, characterized by vanishing bulk moduli and thus negative Poisson ratios and auxetic elasticity, depends sensitively on boundary conditions and on the nature of the kagome distortions. We construct lattices that under free boundary conditions exhibit surface ﬂoppy modes only or a combination of both surface and bulk ﬂoppy modes; and we show that bulk ﬂoppy modes present under free boundary conditions are also present under periodic boundary conditions but that surface modes are not. In the the long-wavelength limit, the elastic theory of all these lattices is a conformally invariant ﬁeld theory with holographic properties, and the surface waves are Rayleigh waves. We discuss our results in relation to recent work on jammed systems. Our results highlight the importance of network architecture in determining ﬂoppy-mode structure.

PACS numbers:

I. INTRODUCTION

Networks of balls and springs or frames of nodes connected by compressible struts provide realistic models for physical systems from bridges to condensed solids. Their elastic properties depend on their coordination number z – the average number of nodes each node is connected to. If z is large enough, the networks are elastic solids whose long-wavelength mechanical properties are described by a continuum elastic energy with non-vanishing elastic moduli. If z is small enough, the networks have deformation modes of zero energy – they are ﬂoppy. As z is increased from the ﬂoppy side, a critical value, zc, is reached at which springs provide just enough constraints that the system has no zero-energy “ﬂoppy” modes [1] (or mechanisms [2] in the engineering literature), and the system is isostatic. The phenomenon of rigidity percolation [3, 4] whereby a sample spanning rigid cluster develops upon the addition of springs is one version of this ﬂoppyto-rigid transition. The coordination numbers of whole classes of systems, including engineering structures [5, 6] (bridges and buildings), randomly packed spheres near jamming [7–10], network glasses [1, 11], cristobalites [12], zeolites [13, 14], and biopolymer networks [15–18] are close enough to zc that their elasticity and mode structure is strongly inﬂuenced by those of the isostatic lattice.

Though the isostatic point always separates rigid from ﬂoppy behavior, the properties of isostatic lattices are not universal; rather they depend on lattice architecture. Here we explore the the unusual properties of a particular class of periodic isostatic lattices derived from the

two-dimensional kagome lattice by rigidly rotating triangles through an angle α without changing bond lengths as shown in Fig. 1. The bulk modulus B of these lattices is rigorously zero for all α = 0. As a result, their Poisson ratio acquires its limit value of −1; when stretched in one direction, they expand by an equal amount in the orthogonal direction: they are maximally auxetic [19–22]. These modes represent collapse pathways [23, 24] of the kagome lattice. Modes of isostatic systems are generally very sensitive to boundary conditions [25–27], but the degree of sensitivity depends on the details of lattice structure. For reasons we will discuss more fully below, modes of the square lattice, which is isostatic, are in fact insensitive to changes from free boundary conditions (FBCs) to periodic boundary conditions (PBCs), whereas those of the undistorted kagome lattice are only mildly so. The modes of both, however, change signiﬁcantly when rigid boundary conditions (RGBs) are applied. We show here that in all families of the twisted kagome lattice, modes depend sensitively on whether FBCs, PCBs or RGBs are applied: ﬁnite lattices with free boundaries have ﬂoppy surface modes that are not present in their periodic or rigid spectrum or in that of ﬁnite undistorted kagome lattices. In the long wavelength limit, the surface ﬂoppy modes, which are present in any 2d material with B = 0, reduce to surface Rayleigh waves [28] described by a conformally invariant energy whose analytic eigenfunctions are fully determined by boundary conditions. At shorter wavelengths, the surface waves become sensitive to lattice structure and remain conﬁned to within a distance of the surface that diverges as the undistorted kagome lattice is

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |


- 3

- 3

- 3

3

4

4

4

4

- 4


- 4


- 4


1

2

- e2
- e3


e1

1

2

3

1

2

Ny

3

1

2

1

2 2

2a

a Nx

1

(a) (b)

aL

3

2* 2 1

α

- (c)
- (d)


3*

- FIG. 1: (a) Section of a kagome lattice with Nx = Ny = 4 and Nc = NxNy three-site unit cells. Nearest-neighbor bonds, occupied by harmonic springs, are of length a. The rotated row (second row from the top) represents a ﬂoppy mode. Nextnearest neighbor bonds are shown as dotted lines in the lower


left hexagon. The vectors e1, e2, and e3 indicate symmetry directions of the lattice. The numbers in the triangles indicate those that twist together under PBCs in zero modes along the three symmetry direction. Note that there are only 4 of these modes. (b) Section of a square lattice depicting a ﬂoppy mode in which all sites along a line are displaced uniformly. (c) Twisted kagome lattice, with lattice constant aL = 2a cos α, derived from the undistorted lattice by rigidly rotating triangles through an angle α. A unit cell, bounded by dashed lines, is shown in violet. Arrows depict site displacements for the zone-center, i.e., zero wavenumber, φ mode which has zero (nonzero) frequency under free (periodic) boundary conditions. Sites 1, 2, and 3 undergo no collective rotation about their center of mass whereas sites 1, 2∗, and 3∗ do. (d) Superposed snapshots of the twisted lattice showing decreasing areas with increasing α.

approached. In the simplest twisted kagome lattice, all ﬂoppy modes are surface modes, but in more complicated lattices, including ones with uniaxial symmetry, we construct, there are both surface and bulk ﬂoppy modes.

Arguments due to J.C. Maxwell [29] provide a criterion for network stability: networks in d dimensions consisting of N nodes, each connected with central-force springs to an average of z neighbors, have N0 = dN − 12zN zeroenergy modes when z < 2d (in the absence of redundant bonds - see below). Of these a number, Ntr, which de-

![image 1](<2011-sun-surface-phonons-elastic-response_images/imageFile1.png>)

pends on boundary conditions, are trivial rigid translations and rotations, and the and the remainder are ﬂoppy modes of internal structural rearrangement. Under FBCs an PBCs, Ntr equals d(d+1)/2 and d, respectively. With increasing z, mechanical stability is reached at the isostatic point at which N0 = Ntr. The Maxwell argument is a global one; it does not provide information about the nature of the ﬂoppy modes and does not distinguish between bulk or surface modes.

II. KAGOME ZERO MODES AND ELASTICITY

The kagome lattice of central force springs shown in Fig. 1(a) is one of many locally isostatic lattices, including the familiar square lattice lattice in two dimensions [Fig. 1(b)] and the cubic and pyrochlore lattices in three dimensions, with exactly z = 2d nearest-neighbor (NN) bonds connected to each site not at a boundary. Under PBCs, there are no boundaries, and every site has exactly 2d neighbors. Finite, N-site sections of these lattices have surface sites with fewer than 2d neighbors and of order √N zero modes. The free kagome lattice with Nx and Ny unit cells along its sides [Fig. 1(a)] has N = 3NxNy sites, NB = 6NxNy −2(Nx+Ny)+1 bonds, and N0 = 2(Nx + Ny) − 1 zero modes, all but three of which are ﬂoppy modes. These modes, depicted in Fig. 1(a), consist of coordinated counter rotations of pairs of triangles along the symmetry axes e1, e2 and e3 of the lattice. There are Nx modes associated with lines parallel to e1, Ny associated with lines parallel to e3, and Nx + Ny − 1 modes associated with lines parallel to e2.

![image 2](<2011-sun-surface-phonons-elastic-response_images/imageFile2.png>)

In spite of the large number of ﬂoppy modes in the kagome lattice, its longitudinal and shear Lam´e coeﬃcients, λ and µ, and its Bulk modulus B = λ + µ are nonzero and proportional to the nearest neighbor (NN)

√spring3k/4.constantThe zerok: modesλ = µof= this√3k/lattice8, andcanB =beλused+ µ to= generate an inﬁnite number of distorted lattices with unstretched springs and thus zero energy [24, 30]. We consider only periodic lattices, the simplest of which are the twisted kagome lattices obtained by rotating triangles of the kagome unit cell through an angle α as shown in Figs. 1(c) and (d) [24, 31]. These lattices have C3v rather than C6v symmetry and, like the undistorted kagome lattice, three sites per unit cell. As Fig. 1(d) shows, the lattice constant of these lattices is aL = 2a cosα, and their area Aα decreases as cos2 α as α increases. The maximum value that α can achieve without bond crossings is π/3 so that the maximum relative area change is Aπ/3/A0 = 1/4. Since all springs maintain their rest length, there is no energy cost for changing α, and as a result, B is zero for every α = 0, whereas the shear modulus µ = √3k/8 remains nonzero and unchanged. Thus, the Poisson ratio σ = (B − µ)/(B + µ) attains its smallest possible value of −1. For any α = 0, the addition of next-nearest-neighbor (NNN) springs, with spring constant k′ (or of bending forces between springs) stabilizes

![image 3](<2011-sun-surface-phonons-elastic-response_images/imageFile3.png>)

![image 4](<2011-sun-surface-phonons-elastic-response_images/imageFile4.png>)

![image 5](<2011-sun-surface-phonons-elastic-response_images/imageFile5.png>)

π

|σ<0 σ>0|
|---|


3

π

4

π

α

6

π

12

0.0 0.1 0.2 0.3 0.4

k′/ k

- FIG. 2: phase diagram in the α − k′ plane showing region with negative Poisson ratio σ.


zero-frequency modes and increases B and σ. Nevertheless, for suﬃciently small k′, σ remains negative. Figure 2 shows the region in the k′ − α plane with negative σ.

III. KAGOME PHONON SPECTRUM

We now turn to the linearized phonon spectrum of the kagome and twisted kagome lattices subjected to PBCs. These conditions require displacements at opposite ends of the sample to be identical and thus prohibit distortions of the shape and size of the unit cell and rotations but not uniform translations, leaving two rather than three trivial zero modes. The spectrum [32] of the three lowest frequency modes along symmetry directions of the undistorted kagome lattice with and without NNN springs is shown in Fig. 3(a). When k′ = 0, there is a ﬂoppy mode for each wavenumber q = 0 running along the entire length of the three symmetry-equivalent straight lines running from M to Γ to M in the Brillouin zone [See inset to Fig. 3]. When Nx = Ny, there are exactly Nx − 1 wavenumbers with q = 0 along each of these lines for a total of 3(Nx − 1) ﬂoppy modes. In addition, there are three zero modes at q = 0 corresponding to two rigid translations, and one ﬂoppy mode that changes unit cell area at second but not ﬁrst order in displacements, yielding a total of 3Nx zero modes rather than the 4Nx −1 modes expected from the Maxwell count under FBCs. This is our ﬁrst indication of the importance of boundary conditions. The addition of NNN springs endows the ﬂoppy modes at k′ = 0 with a characteristic frequency ω∗ ∼

√

![image 6](<2011-sun-surface-phonons-elastic-response_images/imageFile6.png>)

k′ and causes them to hybridize with the acoustic phonon modes [Fig. 3(a)] [32]. The result is an isotropic phonon spectrum up to wavenumber q∗ = 1/l∗ ∼

√

![image 7](<2011-sun-surface-phonons-elastic-response_images/imageFile7.png>)

k′ and gaps at Γ and M of order ω∗. Remarkably, at nonzero α and k′ = 0, the mode structure is almost identical to that at α = 0 and k′ > 0 with characteristic frequency ωα ∼

√

![image 8](<2011-sun-surface-phonons-elastic-response_images/imageFile8.png>)

k|sinα| and length lα ∼ 1/ωα. In other words, twisting the kagome lattice through an angle α has essentially the same eﬀect on the spectrum as adding NNN springs with spring constant |sinα|2k. Thus under PBCs, the twisted kagome lattice has no zero modes other than the trivial ones: it is “col-

M K

(a) (b)

Γ

()qω

α=0 α>0

q q

K Γ M K K Γ M K

FIG. 3: (a)Phonon spectrum for the undistorted kagome lattice. Dashed lines depict frequencies at k′ = 0 and full lines at k′ > 0. The inset shows the Brillouin zone with symmetry points Γ, M, and K. Note the line of zero modes along ΓM when k′ = 0, all of which develop nonzero frequencies for wavenumber q > 0 when k′ > 0 reaching ω∗ ∼

√

![image 9](<2011-sun-surface-phonons-elastic-response_images/imageFile9.png>)

k′ on

- a plateau beginning at q ≈ q∗ ∼

√

![image 10](<2011-sun-surface-phonons-elastic-response_images/imageFile10.png>)

k′ deﬁning a length scale l∗ = 1/q∗. (b) Phonon spectrum for α > 0 and k′ = 0. The plateau along ΓM deﬁnes ωα ∼

√

![image 11](<2011-sun-surface-phonons-elastic-response_images/imageFile11.png>)

k| sin α| and its onset at qα ∼ ωα deﬁnes a length lα ∼ 1/| sin α|.

lectively” jammed in the language of references [27, 33], but because it is not rigid with respect to changing the unit cell size, it is not strictly jammed.

IV. MODE COUNTING AND STATES OF SELF STRESS

To understand the origin of the diﬀerences in the zeromode count for diﬀerent boundary conditions, we turn to an elegant formulation [2] of the Maxwell rule that takes into account the existence of redundant bonds (i.e., bonds whose removal does not increase the number of ﬂoppy modes [4]) and states in which springs can be under states of self-stress. Consider a ring network in two dimensions shown in Fig. 4 with N = 4 nodes and Nb = 4 springs with three springs of length a and one spring of length

- b. The Maxwell count yields N0 = 4 = 3 + 1 zero modes: two rigid translations, one rigid rotation, and one internal ﬂoppy mode – all of which are “ﬁnite-amplitude” modes with zero energy even for ﬁnite-amplitude displacements. When b = 3a, the Maxwell rule breaks down. In the zeroenergy conﬁguration, the long spring and the three short ones are colinear, and a prestressed state in which the bspring is under compression and the three a-springs are under tension (or vice versa) but the total force on each node remains zero becomes possible. This is called a state of self-stress. The system still has three ﬁnite amplitude zero modes corresponding to arbitrary rigid translations and rotations, but the ﬁnite-amplitude ﬂoppy mode has disappeared. In the absence of prestress, it is replaced by two “inﬁnitesimal” ﬂoppy modes of displacements of the two internal nodes perpendicular of the now linear network. In the presence of prestress, these two modes have a frequency proportional to the square root of the tension in the springs. Thus, the system now has one state of self stress and one extra zero mode in the absence


of prestress, implying N0 = 2N −NB +S, where S is the number of states of self stress.

This simple count is more generally valid as can be shown with the aid of the equilibrium and compatibility matrices [2], denoted, respectively, as H and C ≡ HT. H relates the vector t of NB spring tensions to the vector f of dN forces at nodes via H · t = f, and C relates the the vector d of dN node displacements to the vector e of NB spring stretches via C · d = e. The dynamical matrix determining the phonon spectrum is D = kH·HT. Vectors t0 in the null space of H, (H · t0 = 0), describe states of self-stress whereas vectors d0 in the null space of C represent displacements with no stretch e, i.e., modes of zero energy. Thus the nullspace dimensions of H and C are, respectively, S and N0. The rank-nullity theorem of linear algebra [34] states that the rank r of a matrix plus the dimension of its null space equals its column number. Since the rank of a matrix and its transpose are equal, the H and C matrices, respectively, yield the relations r + S = NB and r + N0 = dN, implying N0 = dN − NB + S. Under PBCs, locally isostatic lattices have z = 2d exactly, and the Maxwell rule yields N0 = 0: there should be no zero modes at all. But we have just seen that both the square and undistorted kagome lattices under PBCs have of order √N zero modes as calculated from the dynamical matrix, which, because it is derived from a harmonic theory, does not distinguish between inﬁnitesimal and ﬁnite-amplitude zero modes. Thus, in order for there to be zero modes, there must be states of self-stress, in fact one state of self-stress for each zero mode.

![image 12](<2011-sun-surface-phonons-elastic-response_images/imageFile12.png>)

In the square lattice under FBCs, N = NxNy and NB = 2NxNy−Nx−Ny, there are no states of self stress, and N0 = Nx + Ny zero modes depicted in Fig. 1(b). Under PBCs, the dimension of the nullspace of H is S = Nx + Ny, and there are also N0 = S = Nx + Ny zero modes that are identical to those under FBCs. We have already seen that there are N0 = 2(Nx + Ny) − 1 zero modes in the free undistorted kagome lattice. Direct evaluations [23] (See Text S1) of the dimension of the null spaces of H and C for the undistorted kagome lattice with PBCs yields S = N0 = 3Nx when Nx = Ny. The zero modes under PBCs are identical to those under FBCs except that the 2Nx−1 modes associated with lines parallel to e2 under FBCs get reduced to Nx modes because of the identiﬁcation of apposite sides of the lattice required by the PBCs as shown in Fig. 1(a). Thus the modes of both the square and kagome lattices do not depend strongly on whether FCBs or PBCs are applied. Under RBC’s, however, the ﬂoppy modes of both disappear. The situation for the twisted kagome lattice is diﬀerent. There are still 2(Nx + Ny) − 1 zero modes under FBCs, but there are only two states of self stress under PBCs and thus only N0 = S = 2 zero modes, as a direct evaluation of the null spaces of H and C veriﬁes (See Appendix for details), in agreement with the results obtained via direct evaluation of the eigenvalues of the dynamical matrix [32, 35]. All of the ﬂoppy modes under

a

a (a) b (b) b

FIG. 4: (a) Ring-network with b > 3a showing internal ﬂoppy mode. (b) Ring-network with b = 3a showing one of the two inﬁnitesimal modes.

FBCs have disappeared.

V. EFFECTIVE THEORY AND EDGE MODES

An eﬀective long-wavelength energy Eeﬀ for the lowenergy acoustic phonons and nearly ﬂoppy distortions provides insight into the nature of the modes of the twisted kagome lattice. The variables in this theory are the vector displacement ﬁeld u(x) of nodes at undistorted positions x and the scalar ﬁeld φ(x) describing nearly ﬂoppy distortions within a unit cell. The detailed form of Eeﬀ depends on which three lattice sites are assigned to a unit cell. Figure 1(c) depicts the lattice distortion φ for the nearly ﬂoppy mode at Γ (with energy proportional to |sinα|2) along with a particular representation of a unit cell, consisting of a central asymmetric hexagon and two equilateral triangles, with 8 sites on its boundary. If sites 1, 2, and 3 are assigned to the unit cell, then the distortion φ involves no rotations of these sites relative to their center of mass, and the harmonic limit of Eeﬀ depends only on the symmetrized and linearized strain uij = (∂iuj + ∂jui)/2 and on φ:

E =

- 1

![image 13](<2011-sun-surface-phonons-elastic-response_images/imageFile13.png>)

- 2


d2x 2µu˜2ij

+K(φ + ξuii)2 + V (∂iφ)2 − WΓijkuij∂kφ , (1)

where u˜ij = uij − 21δijukk is the symmetric-traceless stain tensor, µ = √3k/8, K = 3√3tan2 α/a2, ξ = a cscα/(2√3), W = √3k/4 + O(α2), and V = √3k/8 + O(α2). The last term in which Γijk is a third-rank tensor, whose only non-vanishing components are Γxxx = −Γxyy = −Γyyx = −Γxyx = 1, is invariant under operations of the group C6v but not under arbitrary rotations. The Kξφuii term is the only one that reﬂects the C3v (rather than C6v) symmetry of the lattice. There are several comments to make about this energy. The gauge-like coupling in which the isotropic strain uii appears only in the combination (φ + ξuii)2 guarantees that the bulk modulus vanishes: φ will simply relax to −ξuii to reduce to zero the energy of any state with nonvanishing uii. The coeﬃcient K can be calculated directly from the observation that under φ alone, the length of every spring changes by δa = −

![image 14](<2011-sun-surface-phonons-elastic-response_images/imageFile14.png>)

![image 15](<2011-sun-surface-phonons-elastic-response_images/imageFile15.png>)

![image 16](<2011-sun-surface-phonons-elastic-response_images/imageFile16.png>)

![image 17](<2011-sun-surface-phonons-elastic-response_images/imageFile17.png>)

![image 18](<2011-sun-surface-phonons-elastic-response_images/imageFile18.png>)

![image 19](<2011-sun-surface-phonons-elastic-response_images/imageFile19.png>)

√3φsinα, and this length change is reversed by a homogenous volume change uii = δAα/Aα = −2δa/a. In the α → 0 limit,

![image 20](<2011-sun-surface-phonons-elastic-response_images/imageFile20.png>)

K → 0, and the energy reduces to that of an isotropic solid with bulk modulus B0 = limα→0 Kξ2 = √3k/4 if the V and W terms, which are higher order in gradients, are ignored. The W term gives rise to a term, singular in gradients of u, when φ is integrated out that is responsible for the deviations of the ﬁnite-wavenumber elastic energy from isotropy. At small α, the length scale lα appears in several places in this energy: in the length ξ and in the ratios µ/K, V/K, and W/K. At length scales much larger than lα, the V and W terms can be ignored, and φ relaxes to −ξuii leaving only the shear elastic energy of an elastic solid proportional µu˜2ij. At length scales shorter than lα, φ deviates from −ξuii and contributes signiﬁcantly to the form of the energy spectrum. If 1, 2∗ and 3∗ in Fig. 1(d) are assigned to the unit cell, then φ involves rotations relative to the lattice axes, and the energy develops a Cosserat-like form [36, 37] that is a function of φ − a(∇ × u)z/2 rather than φ.

![image 21](<2011-sun-surface-phonons-elastic-response_images/imageFile21.png>)

![image 22](<2011-sun-surface-phonons-elastic-response_images/imageFile22.png>)

![image 23](<2011-sun-surface-phonons-elastic-response_images/imageFile23.png>)

![image 24](<2011-sun-surface-phonons-elastic-response_images/imageFile24.png>)

The modes of our elastic energy in the long-wavelength limit (qlα ≪ 1) are simply those of an elastic medium with B = 0. In this limit, there are transverse and longitudinal bulk sound modes with equal sound velocities cT = µ/ρ = (a/2) k/m and cL = (B + µ)/ρ → cT, where m is the particle mass at each node and ρ is the mass density. In addition there are Rayleigh surface waves [28] in which there is a single decay length (rather than the two at B > 0), and displacements are proportional to e−qyy cos[qxx] with qy = qx for a semi-inﬁnite sample in the right half plane so that the penetration depth into the interior is 1/qx. These waves have zero frequency in two dimensions when B = 0, and they do not appear in the spectrum with PBCs. Thus this simple continuum limit provides us with an explanation for the diﬀerence between the spectrum of the free and periodic twisted kagome lattices. Under FBCs, there are zero-frequency surface modes not present under PBCs.

![image 25](<2011-sun-surface-phonons-elastic-response_images/imageFile25.png>)

![image 26](<2011-sun-surface-phonons-elastic-response_images/imageFile26.png>)

![image 27](<2011-sun-surface-phonons-elastic-response_images/imageFile27.png>)

Further insight into how boundary conditions aﬀect spectrum follows from the observation that the continuum elastic theory with B = 0 depends only on u˜ij. The metric tensor gij(x) of the distorted lattice is related to the strain uij(x) via the simple relation gij(x) = δij + 2uij(x); and u˜ij = [gij(x) − 21δijgkk(x)]/2, which is zero for gij = δij, is invariant, and thus remains equal to zero, under conformal transformations that take the metric tensor from its reference form δij to h(x)δij for any continuous function h(x). The zero modes of the theory thus correspond simply to conformal transformations, which in two dimensions are best represented by the complex position and displacement variables z = x + iy and w(z) = ux(z) + iuy(z). All conformal transformations are described by an analytic displacement ﬁeld w(z). Since by Cauchy’s theorem, analytic functions in the interior of a domain are determined entirely by their values on the domain’s boundary (the “holographic” property [38]), the zero modes of a given sample are simply those analytic functions that satisfy its boundary conditions. For example, a disc with ﬁxed edges (u = 0) has no zero modes because the only analytic function

![image 28](<2011-sun-surface-phonons-elastic-response_images/imageFile28.png>)

satisfying this FBC is the trivial one w(z) = 0; but a disc with free edges (stress and thus strain equal to zero) has one zero mode for each of the analytic functions w(z) = anzn for integer n ≥ 0. The boundary conditions limx→∞ u(x,y) = 0 and u(x,y) = u(x + L,y) on a semiinﬁnite cylinder with axis along x are satisﬁed by the function w(z) = eiqxz = eiqxxe−qxy when qx = 2nπ/L, where n is an integer. This solution is identical to that for classical Rayleigh waves on the same cylinder. Like the Rayleigh theory, the conformal theory puts no restriction on the value of n (or equivalently qx). Both theories break down, however, at qx = qc ≈ min(lα−1,a−1) beyond which the full lattice theory, which yields a complex value of qy = qy′ + iqy′′, is needed.

Figure 5(a) shows an example of a surface wave. At the bottom of this ﬁgure, uy(x) is an almost perfect sinusoid. As y decreases toward the surface, the amplitude grows, and in this picture reaches the nonlinear regime by the time the surface at y = 0 is reached. Figure 5(b) plots qy′ as a function of qx obtained both by direct numerical evaluation and by an analytic transfer matrix procedure [39] for diﬀerent values of α (Text S1). The Rayleigh limit qy′ = qx is reached for all α as qx → 0. Interestingly the Rayleigh limit remains a good approximation up to values of qx that increase with increasing α. The inset to Fig. 5, plots qy′ lα as a function of η = qxlα and shows that in the limit α → 0 (lα/a → ∞), qy′ obeys an αindependent scaling law of the form qy′ = lα−1f(qxlα). The full complex qy obeys a similar equation. This type of behavior is familiar in critical phenomena where scaling occurs when correlation lengths become much larger than microscopic lengths. The function f(η) approaches η as η → 0 and asymptotes to 4/3 for η → ∞. Thus for qxlα ≪ 1, qy′ = qx and for qxlα ≫ 1, qy′ = (4/3)lα−1. As α increases, lα/a is no longer much larger than one, and deviations from the scaling law result. The situation for surfaces along diﬀerent directions (e.g., along x = 0 rather than y = 0) is more complicated and will be treated in a future publication [40].

VI. OTHER LATTICES AND RELATION TO JAMMING

The C3v twisted kagome lattice is the simplest of many lattices that can be formed from the kagome and other periodic isostatic lattices. Figures 6 (a) and (b) show two other examples of isostatic lattices constructed from the kagome lattice. Most intriguing is the lattice with pgg symmetry. Its geometry has uniaxial symmetry, yet its long-wavelength elastic energy is identical to that of the C3v twisted kagome lattice, i.e, it is isotropic with a vanishing bulk modulus, and its mode structure near q = 0 is isotropic as shown in Fig. 6 (c). Thus, this system loses long-wavelength zero-frequency bulk modes of the undistorted kagome lattice to surface modes. However, at large wavenumber, lattice anisotropy becomes apparent, and (inﬁnitesimal) ﬂoppy bulk modes appear. Thus in

(a)

′qayL

(b)

y

x

- 1

0 1 2 3 4 5

- 2


′qlyα

- 0 π/2
- 1
- 2
- 3


qxlα

π

qxaL

FIG. 5: (a)Lattice distortions for a surface wave on a cylinder, showing exponential decay of the surface displacements into the bulk. This ﬁgure was constructed by specifying a small sinusoidal modulation on the bottom boundary and propagating lattice-site positions upward to the free boundary at the top under the constraint of of constant lengths and periodic boundary conditions around the cylinder. Distortions near and at the top boundary, which have become nonlinear, are not described by our linearized treatment. (b) qy′ aL as a function of qxaL for lattice Rayleigh surface waves for α = π/20, π/10, 3π/20, π/5, π/4, in order from bottom to top. Smooth curves are the analytic results from a transfer matrix calculation, and dots are from direct numerical calculations. The dashed line is the continuum Rayleigh limit qy′ = qx. Curves at smaller α break away from this curve at smaller values of qy than do those at large α. At α = π/4, qx′ diverges at qyaL = π. The inset plots qy′ lα as a function of qxlα for diﬀerent α. The lower curve in the inset(black) is the α-independent scaling function of qylα reached in the α → 0 limit. The other curves from top to bottom are for α = π/25, π/12, π/9, and π/6 (chosen to best present results rather than to match the curves in the main ﬁgure). Curves for α < π/15 are essentially indistinguishable from the scaling limit. The curve at α = π/6 stops because qy < π/aL.

this and related systems, a fraction of the zero modes of the under FBCs are bulk modes that are visible under PBCs, and a fraction are surface modes that are not.

Randomly packed spheres above the jamming transition with average coordination number z = 2d + ∆z exhibit a characteristic frequency ω∗ ∼ ∆z and length l∗ ∼ (∆z)−1 and a transition from a Debye-like (∼ ωd−1) to a ﬂat density of states at ω ≈ ω∗ [41, 42]. The square and kagome lattices with randomly added NNN springs have the same properties [43, 44]. A general “cutting” argument [25, 26] provides a procedure for perturbing away from the isostatic limit and an explanation for these properties. However, it only applies provided a ﬁnite fraction of the of order Ld−1 ﬂoppy modes of a sample with sides

(a)

(b)

(c)

![image 29](<2011-sun-surface-phonons-elastic-response_images/imageFile29.png>)

44 k

0

FIG. 6: (a) Kagome-based lattice with pgg space group symmetry and uniaxial c2v point group symmetry. (b) Lattice with p6 space symmetry but global C6 point-group symmetry. (c) Density plot of the spectrum of the lowest frequency branch of the pgg uniaxial kagome lattice. The spectrum is absolutely isotropic near the origin point Γ, but it has a zero modes on two symmetry related continuous curves at large values of wave-number.

of length L cut from an isostatic lattice with PBCs are extended, i.e., have wave functions that extend across the sample rather than remaining localized either in the interior or at the surface the sample. Clearly the twisted kagome lattice, whose ﬂoppy modes are all surface modes, violates this criterion; and indeed, the density of states of the lattice with ∆z = 0 shows Debye-behavior crossing over to a ﬂat plateau at ω ≈ ωα. Adding next nearest neighbor bonds gives rise to a length lc ≈ (lα−1 + l∗−1)−1 and crossover to the plateau at ωc ∼ lc−1. The pgg lattice in Fig. 6(a), however, has both extended and surface ﬂoppy modes, so its crossover to the a ﬂat plateau occurs at ω ≈ ω∗ rather than at ωα or ωc.

VII. CONNECTIONS TO OTHER SYSTEMS

Our study highlights the rich and remarkable variety of physical properties that isostatic systems can exhibit. Under FBCs, ﬂoppy modes can adopt a variety of forms, from all being extended to all being localized near surfaces to a mixture of the two. Under PBC’s, the presence of ﬂoppy modes depends on whether the lattice can or cannot support states of self stress. When a lattice exhibits a large number of zero-energy edge modes, its mechanical/dynamical properties become extremely sensitive to boundary conditions, much as do the electronic properties of the topological states of matter studied in

quantum systems [45–48]. The zero-energy edge modes observed in our isostatic lattices are collective modes whose amplitudes decay exponentially from the edge with a ﬁnite decay length, in direct contrast to the very localized and trivial ﬂoppy modes arising from dangling bonds. We focussed primarily on high-symmetry lattices derived from the kagome lattice, but the properties they exhibit, namely a deﬁcit of ﬂoppy modes in the bulk and the existence of ﬂoppy surface modes, are shared by any two-dimensional system with a vanishing bulk modulus (or the equivalent in anisotropic systems). Threedimensional analogs of the twisted kagome lattice [30] can be constructed by rotating tetrahedra in pyrochlore and zeolite lattices [13, 14] and in cristobalites [12]. These lattices are anisotropic. With NN forces only, they exhibit a vanishing modulus for compression applied in particu-

lar planes rather than isotropically, but we expect them to exhibit many of the properties the two-dimensional lattices exhibit. Finally, we note that Maxwell’s ideas can be applied to spin systems such as the Heisenberg anti-ferromagnet on the kagome lattice [49, 50], and the possibility of unusual edge states in them is intriguing.

Acknowledgments

We are grateful for informative conversations with Randall Kamien, Andea Liu, and S.D. Guest. This work was supported in part by NSF under grants DMR0804900 (T.C.L. and X.M.), MRSEC DMR-0520020 (T.C.L. and A.S.) and JQI-NSF-PFC (K. S.).

![image 30](<2011-sun-surface-phonons-elastic-response_images/imageFile30.png>)

![image 31](<2011-sun-surface-phonons-elastic-response_images/imageFile31.png>)

Appendix A: Derivation of equilibrium, compatibility, and dynamical matrices.

In this section, we will provide some of the details for calculating the equilibrium and compatibility matrices H and

C and the Dynamical matrix D under periodic boundary conditions. The equilibrium matrix H relates the NB = dN dimensional vector of bond tensions t to the dN dimensional vector f of forces at the nodes via H · t = f. We label

unit cells by the their position vectors l = l1e1 + l2e2, where l1 and l2 are integers and en = (cos φn,sinφn); φn =

2π(n − 1) 3

(A1)

![image 32](<2011-sun-surface-phonons-elastic-response_images/imageFile32.png>)

are the primitive lattice vectors. (Here we take the lattice spacing to be one, i.e., 2a cosα → 1.) Each unit cell has three sites, labeled 1, 2, and 3 as shown in Fig. 7, so we label the 3Nc sites by (l,a), where a = 1,2,3 and Nc = N/3 is the number of unit cells. Forces at the nodes are denoted by fl,a and their 6Nc = 2N components as fl,a,i, where i = x,y. They have to be balanced by stretching forces in the springs located on the bonds. There are six bonds per cell, which we can take to be the six bonds in the distorted hexagon shown in Fig. 7, oriented parallel to the unit vectors

(n − 1)π 3

+ (−1)nα (A2)

bn(α) = (cosψn,sinψn); ψn =

![image 33](<2011-sun-surface-phonons-elastic-response_images/imageFile33.png>)

for n = 1,...,6, where α is the twist angle of the twisted kagome lattice. When α = 0, these vector reduce to the edge vectors of a symmetric hexagon with bp(0) = −bp+3(0).

The 6Nc = 2N bonds, labeled with l,n, are occupied by springs under tension tl,n that exert pulling (for tl,n > 0) forces, direct along the bond vectors ±bn(α), on nodes. We deﬁne vectors tl,n = tl,nbn(α). Because we have periodic boundary conditions, we can express both fl,a and tl,n in terms of their Fourier components,

1 √Nc q

eiq·lfq,n (A3)

fl,a =

![image 34](<2011-sun-surface-phonons-elastic-response_images/imageFile34.png>)

![image 35](<2011-sun-surface-phonons-elastic-response_images/imageFile35.png>)

1 √Nc q

eiq·ltq,n. (A4)

tl,n =

![image 36](<2011-sun-surface-phonons-elastic-response_images/imageFile36.png>)

![image 37](<2011-sun-surface-phonons-elastic-response_images/imageFile37.png>)

The equilibrium matrix is diagonal in q, so it breaks up into independent 6 × 6 blocks for each of the Nc = NxNy independent vectors q. For simplicity, we consider only the case Nx = Ny for which Nc = Nx2 and for which the number of sites is N = 3Nx2.

1. The Equilibrium Matrix

There are four bonds incident on each site. The equations relating fl,a to tl,n follow from Fig. 7:

- fl,1 = tl,1 − tl,6 + tl+e

3,4 − tl+e

3,3 (A5)

- fl,2 = tl,3 − tl,2 + tl+e

1,6 − tl+e

1,5 (A6)

- fl,3 = tl,5 − tl,4 + tl+e


2,2 − tl+e

2,1. (A7)

![image 38](<2011-sun-surface-phonons-elastic-response_images/imageFile38.png>)

FIG. 7: Watch this space

We map (a,i) to a single index m with (a,x) → 2a − 1 and (a,y) → 2a and then Fourier transform. The result is that H breaks up into independent 6 × 6 blocks Hnm(q) for each q. This leads to

fn(q) = Hn,m(q)tm(q), (A8) where

- b1,x(α) 0 −eiq·e

3

b3,x(α) eiq·e

3

b4,x(α) 0 −b6,x(α)

- b1,y(α) 0 −eiq·e






b3,y(α) eiq·e

b4,y(α) 0 −b6,y(α)

3

3

- 0 −b2,x(α) b3,x(α) 0 −eiq·e

1

b5,x(α) eiq·e

1

b6,x(α)

- 0 −b2,y(α) b3,y(α) 0 −eiq·e


. (A9)

H(q) =

b5,y(α) eiq·e

b6,y(α) −eiq·e

1

1

 

 

b2,x(α) eiq·e

b1,x(α) 0 b5,x(α) −b4,x(α) 0 −eiq·e

2

2

b2,y(α) eiq·e

b1,y(α) 0 b5,y(α) −b4,y(α) 0

2

2

The null space of this matrix is easily calculated with the aid of Mathematica.

- Case 1, α = 0: This is the untwisted kagome lattice. When q = 0, the null space of H(q) is empty unless q is perpendicular to one of the primitive lattice vectors:


q = q⊥,ne⊥,n = q(− sinφn,cosφn), n = 1,2,3, (A10) and q · en = q||,n = 0, in which case there is a single vector,

- t1(q) = Ncδq

![image 39](<2011-sun-surface-phonons-elastic-response_images/imageFile39.png>)

- ||,1,0(1,0,0,e−iq⊥,1 e3·e⊥,1,0,0) (A11)

t2(q) = Ncδq

![image 40](<2011-sun-surface-phonons-elastic-response_images/imageFile40.png>)

- ||,2,0(0,1,0,0,e−iq⊥,2e1·e⊥,2,0) (A12)

t3(q) = Ncδq

![image 41](<2011-sun-surface-phonons-elastic-response_images/imageFile41.png>)

- ||,3,0(0,0,1,0,0,e−iq⊥,3e2·e⊥,3), (A13)




where Nc is the number of cells, for each n and q⊥,n in the null space. When q = 0, there are three vectors, (1,0,0,1,0,0), (0,1,0,0,1,0), and (0,0,1,0,0,1) in the null space. These are the q = 0 limits of t1(q), t2(q), and t3(q), respectively. We can, therefore, take the set of null-space vectors of H to be t1(q), t2(q), and t2(q) for the Nx values of q, which include q = 0. Linear combinations of these vectors are also null-space vectors, and we can use

them to construct vectors conﬁned to a single line of bonds. For example the vector

1 Nc q

t1(l) =

![image 42](<2011-sun-surface-phonons-elastic-response_images/imageFile42.png>)

eiq·lt1(q) = (δl

y,0,0,0,δl

y,−

√3/2,0,0) (A14)

![image 43](<2011-sun-surface-phonons-elastic-response_images/imageFile43.png>)

corresponds to a state in which springs on all 1-bond in cells with centers at l = l1e1 for any l1 and on all 4-bonds in cells with centers at l = l1e1 +e3 = (l1 −(1/2),−

√3/2) are all under the same tension. This is a state of self-stress in which all bonds along a particular straight line parallel to the e1-axis are under tension. Similar states of self-stress for any of the 3Nx lines of bonds can be constructed.

![image 44](<2011-sun-surface-phonons-elastic-response_images/imageFile44.png>)

- Case 2, α > 0: This is the twisted lattice. The null space of H(q) is empty for all q > 0, and it contains only two vectors when q = 0. These correspond to two states of self-stress in which the stress the stress on the six bonds take on both positive and negative values that are identical in all unit cells.


2. The Compatibility Matrix

The compatibility matrix C relates the dN displacements d to the Nb stretches sl,a. The displacements are labeled the same way as the forces, i.e. as dl,a and the stretches in the same way as the bond tensions, i.e. as sl,n. The equations relating dl,a and sl,n ≡ −sl,nbn(α) are

2,3 − dl,1 = sl,1 = −sl,1b1(α)

dl−e

- dl,2 − dl−e

2,3 = sl,2 = −sl,2b2(α) dl−e

3,1 − dl,2 = sl,3 = −sl,3b3(α)

- dl,3 − dl−e


3,1 = sl,4 = −sl,4b4(α) dl−e

1,2 − dl,3 = sl,5 = −sl,5b5(α) dl,1 − dl−e

1,2 = sl,6 = −sl,6b6(α). (A15)

Fourier transforming and using the same (n,m) notation as for the equilibrium matrix, we obtain

Cmn(q)dn(q) = sm(q), (A16)

where Cmn(q) = Hnm(−q) = H†

mn(q) as required by the constraint C = HT.

3. The Dynamical Matrix

Finally, the dynamical matrix is D(q) = kH(q) · C(q), whose components are

- D11(q) =

- 1

![image 45](<2011-sun-surface-phonons-elastic-response_images/imageFile45.png>)

- 2


[cos(2α) + 4]

- D12(q) = = −

- 1

![image 46](<2011-sun-surface-phonons-elastic-response_images/imageFile46.png>)

- 2


√

![image 47](<2011-sun-surface-phonons-elastic-response_images/imageFile47.png>)

3 cos(2α)

- D13(q) = = D31∗ (q) = −e−i

qx

![image 48](<2011-sun-surface-phonons-elastic-response_images/imageFile48.png>)

2 +

√3qy

![image 49](<2011-sun-surface-phonons-elastic-response_images/imageFile49.png>)

![image 50](<2011-sun-surface-phonons-elastic-response_images/imageFile50.png>)

2 sin2

π 6 − α − e−iq

![image 51](<2011-sun-surface-phonons-elastic-response_images/imageFile51.png>)

x

sin2 α +

π 6

![image 52](<2011-sun-surface-phonons-elastic-response_images/imageFile52.png>)

- D14(q) = D41∗ (q) =

- 1

![image 53](<2011-sun-surface-phonons-elastic-response_images/imageFile53.png>)

- 2


e−iq

x

cos

π 6 − 2α +

![image 54](<2011-sun-surface-phonons-elastic-response_images/imageFile54.png>)

- 1

![image 55](<2011-sun-surface-phonons-elastic-response_images/imageFile55.png>)

- 2


e−i

qx

![image 56](<2011-sun-surface-phonons-elastic-response_images/imageFile56.png>)

2 +

√3qy

![image 57](<2011-sun-surface-phonons-elastic-response_images/imageFile57.png>)

![image 58](<2011-sun-surface-phonons-elastic-response_images/imageFile58.png>)

2 cos 2α +

π 6

![image 59](<2011-sun-surface-phonons-elastic-response_images/imageFile59.png>)

- D15(q) = D51∗ (q) = −2e−

- 1

![image 60](<2011-sun-surface-phonons-elastic-response_images/imageFile60.png>)

- 2i√3qy cos2(α)cos


![image 61](<2011-sun-surface-phonons-elastic-response_images/imageFile61.png>)

qx 2

![image 62](<2011-sun-surface-phonons-elastic-response_images/imageFile62.png>)

- D16(q) = D61∗ (q) = ie−


- 1

![image 63](<2011-sun-surface-phonons-elastic-response_images/imageFile63.png>)

- 2i√3qy sin(2α)sin


qx 2

![image 64](<2011-sun-surface-phonons-elastic-response_images/imageFile64.png>)

![image 65](<2011-sun-surface-phonons-elastic-response_images/imageFile65.png>)

- D22(q) = 2 sin2(α) + cos2

π 6 − α + cos2 α +

![image 66](<2011-sun-surface-phonons-elastic-response_images/imageFile66.png>)

π 6

![image 67](<2011-sun-surface-phonons-elastic-response_images/imageFile67.png>)

- D23(q) = D32∗ (q) =

- 1

![image 68](<2011-sun-surface-phonons-elastic-response_images/imageFile68.png>)

- 2


e−iq

x

cos

π 6 − 2α +

![image 69](<2011-sun-surface-phonons-elastic-response_images/imageFile69.png>)

1 2

![image 70](<2011-sun-surface-phonons-elastic-response_images/imageFile70.png>)

e−i

qx

![image 71](<2011-sun-surface-phonons-elastic-response_images/imageFile71.png>)

2 +

√3qy

![image 72](<2011-sun-surface-phonons-elastic-response_images/imageFile72.png>)

![image 73](<2011-sun-surface-phonons-elastic-response_images/imageFile73.png>)

2 cos 2α +

π 6

![image 74](<2011-sun-surface-phonons-elastic-response_images/imageFile74.png>)

- D24(q) = D42∗ (q) = −e−i


√3qy

![image 75](<2011-sun-surface-phonons-elastic-response_images/imageFile75.png>)

π 6 − α − e−iq

qx

2 +

![image 76](<2011-sun-surface-phonons-elastic-response_images/imageFile76.png>)

![image 77](<2011-sun-surface-phonons-elastic-response_images/imageFile77.png>)

2 cos2

x

![image 78](<2011-sun-surface-phonons-elastic-response_images/imageFile78.png>)

- D2,5(q) = D5∗,2(q) = ie−

- 1

![image 79](<2011-sun-surface-phonons-elastic-response_images/imageFile79.png>)

- 2i√3qy sin(2α)sin


![image 80](<2011-sun-surface-phonons-elastic-response_images/imageFile80.png>)

qx 2

![image 81](<2011-sun-surface-phonons-elastic-response_images/imageFile81.png>)

- D2,6(q) = D6∗,2(q) = −2e−


- 1

![image 82](<2011-sun-surface-phonons-elastic-response_images/imageFile82.png>)

- 2i√3qy sin2(α)cos


qx 2

![image 83](<2011-sun-surface-phonons-elastic-response_images/imageFile83.png>)

![image 84](<2011-sun-surface-phonons-elastic-response_images/imageFile84.png>)

- D33(q) = 2 sin2

π 6 − α + 2 sin2 α +

![image 85](<2011-sun-surface-phonons-elastic-response_images/imageFile85.png>)

π 6

![image 86](<2011-sun-surface-phonons-elastic-response_images/imageFile86.png>)

- D34(q) = D43∗ (q) = 0


π 6

cos2 α +

![image 87](<2011-sun-surface-phonons-elastic-response_images/imageFile87.png>)

- D3,5(q) = D5,3(q) = −e−i

√3qy

![image 88](<2011-sun-surface-phonons-elastic-response_images/imageFile88.png>)

![image 89](<2011-sun-surface-phonons-elastic-response_images/imageFile89.png>)

2 −q2x sin2

![image 90](<2011-sun-surface-phonons-elastic-response_images/imageFile90.png>)

π 6 − α − eiq

![image 91](<2011-sun-surface-phonons-elastic-response_images/imageFile91.png>)

x

sin2 α +

π 6

![image 92](<2011-sun-surface-phonons-elastic-response_images/imageFile92.png>)

- D3,6(q) = D6∗,3(q) = −


- 1

![image 93](<2011-sun-surface-phonons-elastic-response_images/imageFile93.png>)

- 2


eiq

- D4,4(q) = 2 cos2

π 6 − α + 2 cos2 α +

![image 94](<2011-sun-surface-phonons-elastic-response_images/imageFile94.png>)

π 6

![image 95](<2011-sun-surface-phonons-elastic-response_images/imageFile95.png>)

- D4,5(q) = D5∗,4(q) = −

- 1

![image 96](<2011-sun-surface-phonons-elastic-response_images/imageFile96.png>)

- 2


eiq

x

cos

π 6 − 2α −

![image 97](<2011-sun-surface-phonons-elastic-response_images/imageFile97.png>)

- 1

![image 98](<2011-sun-surface-phonons-elastic-response_images/imageFile98.png>)

- 2


ei

qx

![image 99](<2011-sun-surface-phonons-elastic-response_images/imageFile99.png>)

2 −

√3qy

![image 100](<2011-sun-surface-phonons-elastic-response_images/imageFile100.png>)

![image 101](<2011-sun-surface-phonons-elastic-response_images/imageFile101.png>)

2 cos 2α +

π 6

![image 102](<2011-sun-surface-phonons-elastic-response_images/imageFile102.png>)

- D4,6(q) = D6∗,4(q) = −ei


- D5,5(q) = sin2

π 6 − α + sin2 α +

![image 103](<2011-sun-surface-phonons-elastic-response_images/imageFile103.png>)

π 6

![image 104](<2011-sun-surface-phonons-elastic-response_images/imageFile104.png>)

+ 2 cos2(α)

- D5,6(q) = D6∗,5(q) =


- 1

![image 105](<2011-sun-surface-phonons-elastic-response_images/imageFile105.png>)

- 2


cos

D6,6(q) = 2 sin2(α) + cos2

cos

x

π 6 − 2α −

![image 106](<2011-sun-surface-phonons-elastic-response_images/imageFile106.png>)

- 1

![image 107](<2011-sun-surface-phonons-elastic-response_images/imageFile107.png>)

- 2


ei

√3qy

![image 108](<2011-sun-surface-phonons-elastic-response_images/imageFile108.png>)

π 6

qx

2 −

![image 109](<2011-sun-surface-phonons-elastic-response_images/imageFile109.png>)

![image 110](<2011-sun-surface-phonons-elastic-response_images/imageFile110.png>)

2 cos 2α +

![image 111](<2011-sun-surface-phonons-elastic-response_images/imageFile111.png>)

√3qy

![image 112](<2011-sun-surface-phonons-elastic-response_images/imageFile112.png>)

qx

2 −

![image 113](<2011-sun-surface-phonons-elastic-response_images/imageFile113.png>)

![image 114](<2011-sun-surface-phonons-elastic-response_images/imageFile114.png>)

2 cos2

π 6 − α − eiq

x

![image 115](<2011-sun-surface-phonons-elastic-response_images/imageFile115.png>)

π 6

cos2 α +

![image 116](<2011-sun-surface-phonons-elastic-response_images/imageFile116.png>)

- 1

![image 117](<2011-sun-surface-phonons-elastic-response_images/imageFile117.png>)

- 2


π 6

π 6 − 2α +

cos 2α +

![image 118](<2011-sun-surface-phonons-elastic-response_images/imageFile118.png>)

![image 119](<2011-sun-surface-phonons-elastic-response_images/imageFile119.png>)

π 6 − α + cos2 α +

π 6

![image 120](<2011-sun-surface-phonons-elastic-response_images/imageFile120.png>)

![image 121](<2011-sun-surface-phonons-elastic-response_images/imageFile121.png>)

(A17)

Its eigenvalue spectrum can easily be calculated with the aid of Mathematica. The results are shown in Fig. 3 of the main text.

Appendix B: Surface Modes

Surface modes decay exponentially into the bulk. They are characterized by a wavevector q|| parallel to the plane of the surface, their frequency ωs(q||), their decay length l(q||) perpendicular to the surface. In lattices with nearestneighbor forces only, ωs(q||) and l(q||) can be determined by setting q = q|| + q⊥, where q is the wavevector that

appears in the dynamical matrix and q⊥ ≡ q⊥e⊥ is the component of q perpendicular to the surface (e⊥ is the unit vector perpendicular to the surface), setting q⊥ = il−1, requiring

det[ω2I − D(q||,il−1)] = 0, (B1)

where I is the unit matrix, and that the equation of motion of the surface layer be satisﬁed. In the case of surface modes of with zero frequency, the relation det[D(q||,il−1)] = 0 determines l as a function of q||. The surface modes of the twisted kagome lattice have zero frequency, so we need only solve this equation. We consider only the case in which the surface is perpendicular to the y-direction and set qx = q and r = ei

√3/(2l). We ﬁnd

√3qy/2 ≡ e−

![image 122](<2011-sun-surface-phonons-elastic-response_images/imageFile122.png>)

![image 123](<2011-sun-surface-phonons-elastic-response_images/imageFile123.png>)

9 64

a(q) r + r−1 − 2g(q) r + r−1 − 2g∗(q) , (B2)

det[D(q,r)] =

![image 124](<2011-sun-surface-phonons-elastic-response_images/imageFile124.png>)

where

a(q) = 2[2 − cosq + (1 − 2 cosq)cos(4α)] (B3) g(q) =

cos(q/2)[3 − 2 cosp + cosp cos(4α)] + 2i√3sin3(3q/2)sin(4α) 2 − cosq + (1 − 2 cosq)cos(4α)

![image 125](<2011-sun-surface-phonons-elastic-response_images/imageFile125.png>)

(B4)

![image 126](<2011-sun-surface-phonons-elastic-response_images/imageFile126.png>)

Solving for r in Eq. (B2) and to a lattice spacing of 2a cosα, we obtain

1 a√3cosα

![image 127](<2011-sun-surface-phonons-elastic-response_images/imageFile127.png>)

ky ≡ l−1 =

log[−g(2aq cosα) + g(2aq cosα)2 − 1]. (B5)

![image 128](<2011-sun-surface-phonons-elastic-response_images/imageFile128.png>)

![image 129](<2011-sun-surface-phonons-elastic-response_images/imageFile129.png>)

This is the function that is plotted in Fig. 5(b) in the text. Note that ky has both a real and an imaginary part, but that in the limit q → 0, ky = q.

![image 130](<2011-sun-surface-phonons-elastic-response_images/imageFile130.png>)

![image 131](<2011-sun-surface-phonons-elastic-response_images/imageFile131.png>)

![image 132](<2011-sun-surface-phonons-elastic-response_images/imageFile132.png>)

![image 133](<2011-sun-surface-phonons-elastic-response_images/imageFile133.png>)

![image 134](<2011-sun-surface-phonons-elastic-response_images/imageFile134.png>)

![image 135](<2011-sun-surface-phonons-elastic-response_images/imageFile135.png>)

- [1] M. F. Thorpe, J. Non-Cryst. Solids 57, 355 (1983).
- [2] C. R. Calladine, Int. J. Solids and Structures 14,161

(1978).

- [3] S. Feng and P. N. Sen Phys. Rev. Lett. 52, 216 (1984).
- [4] D. J. Jacobs and M. F. Thorpe, Phys. Rev. Lett. 75, 4051 (1995).
- [5] J. Heyman, The Science of Structural Engineering (Cengage Learning, Stamford CT,2005).
- [6] A. Kassimali, Structural Analysis (Cengage Learning, Stamford CT, 2005).
- [7] A. J. Liu and S. R. Nagel, Nature 396, 21 (1998).
- [8] A. J. Liu and S. R. Nagel, Soft Matter 6, 2869 (2010).
- [9] A. J. Liu and S. R. Nagel, Annu. Rev. Condens. Matter Phys. 1, 347 (2010).
- [10] S. Torquato and F. H. Stillinger, Rev. Mod. Phys. 82, 2633 (2010).
- [11] J. C. Phillips, J. Non-Cryst. Solids 43, 37 (1981).
- [12] K. D. Hammonds, M. T. Dove, A. P.Giddy, V. Heine and B. Winkler, American Mineralogist 81, 1057 (1996).
- [13] S. M. Auerbach, K. A. Carrado and P. K. Dutta, eds Zeolite Science and Technology (Taylor and Francis, New York, 2005).
- [14] A. Sartbaeva, S. A. Wells, M. M. J. Treacy and M. F. Thorpe, Nature Materials 5, 962 (2006).
- [15] J. Wilhelm and E. Frey, Phys. Rev. Lett. 91, 108103

(2003).

- [16] C. Heussinger and E. Frey, Phys. Rev. Lett. 97, 105501

(2006).

- [17] L. Huisman and T. Lubensky Phys. Rev. Lett. 106, 088301, (2011).


- [18] C. P. Broedersz, X. Mao, T.C. Lubensky and F. C. MacKintosh, Nature Physics 7, 983 (2011).
- [19] R. Lakes, Science 235,1038 (1987).
- [20] K. E. Evans, M. A. Nkansah, I. J. Hutchinson and S. C. Rogers, Nature 353, 124 (1991).
- [21] C. P. Chen and R. S. Lakes, Journal of Materials Science 26, 5397 (1991).
- [22] G. Greaves, A. Greer, R. Lakes and T. Rouxe, Nature Materials 10,823 (2011).
- [23] R. G. Hutchinson and N. A. Fleck, Journal of the Mechanics and Physics of Solids 54, 756 (2006).
- [24] V. Kapko, M. M. J. Treacy, M. F. Thorpe and S. D. Guest, Proc. Royal Soc. A 465, 3517 (2009).
- [25] M. Wyart, S. R. Nagel and T. A. Witten, Europhys. Lett. 72, 486 (2005).
- [26] M. Wyart, Ann. Phys. (Paris) 30, 1 (2005).
- [27] S. Torquato and F. H. Stillinger, J. Phys. Chem B 105 11849 (2001).
- [28] L. Landau and E. Lifshitz, Theory of Elasticity, 3rd Edition (Pergamon Press, New York, 1986).
- [29] J. C. Maxwell, Philos. Mag. 27, 294 (1865).
- [30] A. Souslov and T. C. Lubensky, (unpublished).
- [31] J. N. Grima, A. Alderson and K. E. Evans, Phys. Status Solidi B 242 561 (2005).
- [32] A. Souslov, A. J. Liu and T. C. Lubensky, Phys. Rev. Lett. 103, 205503 (2009).
- [33] A. Donev, S. Torquato, F. H. Stillinger, and R. Connelly, J. Appl. Phys. 95, 989 (2004).
- [34] G. Birkhoﬀ and S. MacLane, A Survey of Modern Algebra (Taylor and Francis (A K Peters/CRC Press), New York,


- 1998).
- [35] S. D. Guest and J. W. Hutchinson, J. Mech. Phys. Solids 51, 383 (2003).
- [36] E. Cosserat and F. Cosserat, Th´eorie des Corps D´eformables (Hermann et Fils, Paris, 1909).
- [37] I. Kunin, Elstic Media and Microstructure II (SpringerVerlag, Berlin, 1983).
- [38] L. Susskind, J. Math. Phys. 36, 6377 (1995).
- [39] D.-H. Lee and J. D. Joannopoulos, Phys. Rev. B 23, 4988 (1981).
- [40] K. Sun, X. Mao and T. C. Lubensky (unpublished).
- [41] C. S. O’Hern, L. E. Silbert, A. J. Liu and S. R. Nagel, Phys. Rev. E 68, 011306 (2003).
- [42] L. E. Silbert, A. J. Liu and S. R. Nagel, Phys. Rev. Lett. 95, 098301 (2005).
- [43] X. M. Mao, N. Xu and T. C. Lubensky, Phys. Rev. Lett.


- 104, 085504 (2010).
- [44] X. M. Mao and T. C. Lubensky, Phys. Rev. E 83, 011111

(2011).

- [45] C. Kane and M. P. Fisher, in Perspectives in Quantum Hall Eﬀects, eds Das Sarma S, Pinczuk A (John Wiley and Sons, Inc., New York, 1997).
- [46] J. K. Jain, Composite Fermions (Cambridge Universit Press, New York, 2007).
- [47] M. Z. Hasan and C. L. Kane, Rev. Mod. Phys. 82, 3045

(2011).

- [48] X.-L.Qi and S.-C. Zhang, Rev. Mod. Phys. 83, 1057

(2011)

- [49] Moessner R and Chalker JT, Phys. Rev. B 58, 12049

(1998).

- [50] M. J. Lawler, arXiv:1104.0721, (unpublished).


