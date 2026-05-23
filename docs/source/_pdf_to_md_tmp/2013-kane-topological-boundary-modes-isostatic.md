# arXiv:1308.0554v2[cond-mat.mes-hall]12Nov2013

## Topological Boundary Modes in Isostatic Lattices

C. L. Kane and T. C. Lubensky

Dept. of Physics and Astronomy, University of Pennsylvania, Philadelphia, PA 19104

Frames, or lattices consisting of mass points connected by rigid bonds or central-force springs, are important model constructs that have applications in such diverse ﬁelds as structural engineering, architecture, and materials science. The difference between the number of bonds and the number of degrees of freedom of these lattices determines the number of their zero-frequency “ﬂoppy modes”. When these are balanced, the system is on the verge of mechanical instability and is termed isostatic. It has recently been shown that certain extended isostatic lattices exhibit ﬂoppy modes localized at their boundary. These boundary modes are insensitive to local perturbations, and appear to have a topological origin, reminiscent of the protected electronic boundary modes that occur in the quantum Hall effect and in topological insulators. In this paper we establish the connection between the topological mechanical modes and the topological band theory of electronic systems, and we predict the existence of new topological bulk mechanical phases with distinct boundary modes. We introduce model systems in one and two dimensions that exemplify this phenomenon.

Isostatic lattices provide a useful reference point for understanding the properties of a wide range of systems on the verge of mechanical instability, including network glasses1,2, randomly diluted lattices near the rigidity percolation threshold3,4, randomly packed particles near their jamming threshold5–10, and biopolymer networks11–14. There are many periodic lattices, including the square and kagome lattices in d = 2 dimensions and the cubic and pyrochlore lattices in d = 3, that are locally isostatic with coordination number z = 2d for every site under periodic boundary conditions. These lattices, which are the subject of this paper, have a surprisingly rich range of elastic responses and phonon structures15–19 that exhibit different behaviors as bending forces or additional bonds are added.

The analysis of such systems dates to an 1864 paper by James Clerk Maxwell20 that argued that a lattice with Ns mass points and Nb bonds has N0 = dNs − Nb zero modes. Maxwell’s count is incomplete, though, because N0 can exceed dNs − Nb if there are Nss states of self-stress, where springs can be under tension or compression with no net forces on the masses. This occurs, for example, when masses are connected by straight lines of bonds under periodic boundary conditions. A more general Maxwell relation21,

ν ≡ N0 − Nss = dNs − Nb, (1) is valid for inﬁnitesimal distortions.

In a locally isostatic system with periodic boundary conditions, N0 = Nss. The square and kagome lattices have one state of self-stress per straight line of bonds and associated zero modes along lines in momentum space. Cutting a section of N sites from these lattices removes states of selfstress and O(

√

√

N) bonds and necessarily leads to O(

N) zero modes, which are essentially identical to the bulk zero modes. Recently Sun et al.22 studied a twisted kagome lattice in which states of self-stress are removed by rotating adjacent site-sharing triangles in opposite directions. This simple modiﬁcation converts lines of zero modes in the untwisted lattice to gapped modes of nonzero frequency (except for q = 0) and localizes the required zero modes in the cut lattice to its surfaces.

These boundary zero modes are robust and insensitive to local perturbations. Boundary modes also occur in electronic

systems, such as the quantum Hall effect23,24 and topological insulators25–30. In this paper we establish the connection between these two phenomena. Our analysis allows us to predict the existence of new topologically distinct bulk mechanical phases and to characterize the protected modes that occur on their boundary. We introduce a 1D model that illustrates this phenomenon in its simplest form and maps directly to the Su-Schrieffer-Heeger (SSH) model31 for the electronic excitations of polyacetylene ((CH2)n), a linear polymer with alternating single and double bonds between carbon atoms as show in ﬁgure 1 that has toplogically protected electron states at free ends and at interfaces. We then prove an index theorem that generalizes equation (1) and relates the local count of zero modes on the boundary to the topological structure of the bulk. We introduce a deformed version of the kagome lattice model that exhibits distinct topological phases. The predictions of an index theorem are veriﬁed explicitly by solving for the boundary modes in this model. Finally, we show that some of the distinctive features of the topological phases can be understood within a continuum elastic theory.

Mechanical Modes and Topological Band Theory

A mechanical system of masses M connected by springs with spring constant K is characterized by its equilibrium matrix21 Q, which relates forces Fi = QimTm to spring tensions Tm. i labels the dNs force components on the Ns sites, and m labels the Nb bonds. Equivalently, em = QTmiui relates bond extensions em to site displacements ui. The squared normal mode frequencies ωn2 are eigenvalues of the dynamical matrix D = QQT, where we set K/M to unity. Displacements ui that do not lead to stretched bonds satisfy QTui = 0 and deﬁne the null space of QT, or equivalently its kernel ker QT. The dimension of this null space N0 = dim ker QT gives the number of independent zero modes. Similarly, the null space of Q gives the Nss = dim ker Q states of selfstress. The global counts of these two kinds of zero modes are related by the rank-nullity theorem21, which may be expressed as an index theorem32. The index of Q, deﬁned as ν = dim ker QT − dim ker Q, is equal to the difference between the number of rows and columns of Q, and is given by

equation (1).

At ﬁrst sight, the mechanical problem and the quantum electronic problem appear different. Newton’s laws are second-order equations in time, while the Schrodinger equation is ﬁrst order. The eigenvalues of D are positive deﬁnite, while an electronic Hamiltonian has positive and negative eigenvalues for the conduction and valence bands. To uncover the connection between the two problems we draw our inspiration from Dirac, who famously took the “square root” of the Klein Gordon equation33. To take the square root of the dynamical matrix, note that D = QQT has a supersymmetric partner D˜ = QTQ with the same non-zero eigenvalues. Combining D and D˜ gives a matrix that is a perfect square,

H =

0 Q QT 0

; H2 =

QQT 0 0 QTQ

. (2)

The spectrum of H is identical to that of D, except for the zero modes. Unlike D, the zero modes of H include both the zero modes of QT and Q, which are eigenstates of τz = diag(1dN

) distinguished by their eigenvalue, ±1. (While the concept of supersymmetry is not essential for deriving this result, there is an interesting connection between the analysis leading to equation (2) and the theory of supersymmetric quantum mechanics34,35.)

#### ,−1N

s

b

Viewed as a Hamiltonian, H can be analyzed in the framework of topological band theory29. It has an intrinsic “particle-hole” symmetry, {H,τz} = 0, that guarantees eigenstates come in ±E pairs. Since Qim is real, H = H∗ has “time-reversal” symmetry. These deﬁne symmetry class BDI36. In one-dimension, gapped Hamiltonians in this class, such as the SSH model, are characterized by an integer topological invariant n ∈ Z that is a property of the Bloch Hamiltonian H(k) (or equivalently Q(k)) deﬁned at each wavenumber k in the Brillouin zone (BZ). A mapping of H(k) to the complex plane is provided by detQ(k) = |detQ(k)|eiφ(k). If bulk modes are all gapped then |detQ(k)| is nonzero and Q(k) ∈ GLp, where p is the dimension of Q(k). Q(k) is then classiﬁed by the integer winding number of φ(k) around the BZ: (φ(k + G) − φ(k) = 2πn, where G is a reciprocal lattice vector), which deﬁnes an element of the homotopy group π1(GLp) = Z. A consequence is that a domain wall across which n changes is associated with topologically protected zero modes31,37,38. Below, we present an index theorem that uniﬁes this bulk-boundary correspondence with equation (1) and shows how it can be applied to d-dimensional lattices, which form the analog of weak topological insulators28.

Topological edge modes have been previously predicted in 2D photonic39,40 and phononic41 systems. These differ from the present theory because they occur in systems with bandgaps at ﬁnite frequency and broken time-reversal symmetry (symmetry class A). Localized end modes were found in a time-reversal invariant 1D model (class AI)42. However, the presence of those ﬁnite frequency modes is not topologically guaranteed.

a b

- δθ1 δθ3

- δθ2 δθ4


θ

c d

- f

h

fm

fm

fm ss

θ = + θc

θ = - θc

θ = - θc

θ = + θc

l1

l2

l3

e

- g


FIG. 1: One-dimensional SSH and isostatic lattice models. (a) and (b) depict the SSH model of polyacetalene, with A and B sublattices indicated in blue and red. (a) describes the gapless state with all bonds identical, while (b) describes the gapped AB dimerized state, with double (single) bonds on the AB (BA) bonds. The BA dimerized state with single and double bonds interchanged is not shown. (c) and (d) show the 1D isostatic lattice model in which masses, represented the larger blue dots are connected by springs in red and are constrained to rotate about ﬁxed pivot points represented by small black dots. (c) is the gapless high-symmetry state with θ¯ = 0, and (d) is the gapped lower-symmetry phase with θ¯ > 0. (c) and (d) are equivalent to (a) and (b) if we identify the masses (springs) with the A (B) sublattice sites. (e) shows a domain wall in polyacetalene connecting the AB and BA dimerized states. There is a topologically protected zero-energy state associated with the A sublattice at the defect. (f) shows the equivalent state for the isostatic model with a topologically protected zero-frequency mode at the domain wall. (g) shows domain wall connecting the BA and AB dimerized states, which has a zero energy state associated with the B sublattice. (h) shows the equivalent isostatic state with a state of self-stress at the domain wall.

One-Dimensional Model

Before discussing the index theorem we introduce a simple 1D elastic model, equivalent to the SSH model, that illustrates the topological modes in their simplest setting. Consider a 1D system of springs connecting masses constrained to rotate at a radius R about ﬁxed pivot points. In Fig. 1c the spring lengths are set so that the equilibrium conﬁguration is θi = 0. Fig. 1d shows a conﬁguration with shorter springs with θi = θ¯. Expanding in deviations δθi about θ¯, the extension of spring m is δ m = QTmiδθi, with QTmi = q1(θ¯)δm,i + q2(θ¯)δm,i+1 and q1(2) = r cosθ¯(r sinθ¯±1)/ 4r2 cos2 θ¯+ 1. The normal mode dispersion is ω(k) = |Q(k)|, where Q(k) = q1 +q2eik. When θ¯ = 0, q1 = −q2, and there are gapless bulk modes near k = 0. For a ﬁnite system with N sites and N − 1 springs, there are no states of self stress and only a single extended zero mode, as required by equation (1). For θ¯ = 0 the bulk spectrum has a gap. In this case, the zero mode required by equation (1) is localized at one end or the other, depending on the sign of θ¯. The θ¯ > 0 and θ¯ < 0 phases

are topologically distinct in the sense that it is impossible to tune between the two phases without passing through a transition where the gap vanishes. The topological distinction is captured by the winding number of the phase of Q(k), which is 1 (0) for |q1| < (>)|q2|.

Viewed as a quantum Hamiltonian, equation (2) for this model is identical to the SSH model31, as indicated in Fig. 1(a,b). The sites and the bonds correspond, respectively, to the A and B sublattices of the SSH model. For θ¯ = 0 the bonds in the SSH model are the same (Fig. 1a), while for θ¯ = 0 they are dimerized (Fig. 1b). The two topological phases correspond to the two dimerization patterns for polyacetalene. As is well known for the SSH model31,37, an interface between the two dimerizations binds a zero mode, as indicated in Fig. 1(e,g). This is most easily seen for θ¯ = ±θc where the springs are colinear with the bars, so that q1 or q2 = 0. Fig. 1f shows a domain wall between +θc and −θc, in which the center two sites share a localized ﬂoppy mode. Fig. 1h shows an interface between −θc and +θc with a state of self-stress localized to the middle three bonds, in addition to ﬂoppy modes localized at either end. As long as there is a bulk gap, the zero modes cannot disappear when θ¯ deviates from ±θc. The zero modes remain exponentially localized, with a localization length that diverges when θ¯ → 0.

Index Theorem

There appear to be two distinct origins for zero modes. In equation (1) they arise because of a mismatch between the number of sites and bonds, while at a domain wall they arise in a location where there is no local mismatch. To unify them, we generalize the index theorem so that it determines the zeromode count νS in a subsystem S of a larger system. This is well deﬁned provided the boundary of S is deep in a gapped phase where zero modes are absent. We will show there are two contributions,

νS = νLS + νTS, (3)

where νLS is a local count of sites and bonds in S and νTS is a topological count, which depends on the topological structure

of the gapped phases on the boundary of S.

To prove equation (3) and to derive formulas for νTS and νLS, we adapt a local version of the index theorem originally introduced by Callias43–46 to allow for the possibility of non-zero νLS. The details of the proof are given in the supplementary material. Here we will focus on the results. Consider a ddimensional system described by a Hamiltonian matrix Hαβ, where α labels a site or a bond centered on rα. The count of zero modes in S may be written

i  H + i 

νS = lim →0

Tr τzρS(ˆr)

, (4)

where ˆrαβ = δαβrα. The region S is deﬁned by the support function ρS(r) = 1 for r ∈ S and 0 otherwise. It is useful to consider ρS(r) to vary smoothly between 1 and 0 on the boundary ∂S. Expanding the trace in terms of eigenstates of H shows that only zero modes with support in S contribute.

In the supplementary material we show that equation (4) can be rewritten as equation (3) with

νLS = Tr ρS(ˆr)τz (5) and

dd−1S Vcell

νTS =

RT · n,ˆ (6)

∂S

where the integral is over the boundary of S with inward pointing normal nˆ. RT = i niai is a Bravais lattice vector characterizing the periodic crystal in the boundary region that can be written in terms of primitive vectors ai and integers

- 1

- 2πi C


- 1

- 2π C


dk·Tr[Q(k)−1∇kQ(k)]. =

dk·∇kφ(k).

ni =

i

i

(7) Here Ci is a cycle of the BZ connecting k and k + bi, where bi is a primitive reciprocal vector satisfying ai · bj = 2πδij. ni are winding numbers of the phase of detQ(k) around the cycles of the BZ, where Q(k) is the equilibrium matrix in a Bloch basis.

To apply equations (6) and (7), it is important that the winding number be independent of path. This is the case if there is a gap in the spectrum. We will also apply this when the gap vanishes for acoustic modes at k = 0. This is okay because the acoustic mode is not topological in the sense that it can be gapped by a weak translational-symmetry-breaking perturbation. This means the winding number is independent of k even near k = 0. It is possible, however, that there can be topologically protected gapless points. These would be point zeros around which the phase of detQ(k) advances by 2π. These lead to topologically protected bulk modes that form the analog of a “Dirac semimetal” in electronic systems like graphene. These singularities could be of interest, but they do not occur in the model we study below.

A second caveat for equation (7) is that, in general, the winding number is not gauge invariant and depends on how the sites and bonds are assigned to unit cells. In the supplementary material we show that for an isostatic lattice with uniform coordination it is possible to adopt a “standard unit cell” with basis vectors di(m) for the ns sites (dns bonds) per cell that satisfy r0 = d i di − m dm = 0. Q(k) is deﬁned using Bloch basis states |k,a = i,m ∝ R expik · (R + da)|R + da , where R is a Bravais lattice vector. In this gauge, RT is uniquely deﬁned and the zero-mode count is given by equations (3) and (5)-(7).

To determine the number of zero modes per unit cell on an edge indexed by a reciprocal lattice vector G, consider a cylinder with axis parallel to G and deﬁne the region S to be the points nearest to one end of the cylinder (See Supplementary Fig. 1). νTS is determined by evaluating equation (6), with the aid of equation (7) on ∂S deep in the bulk of the cylinder. It follows that

ν˜T ≡ νTS/Ncell = G · RT/2π. (8)

The local count, νLS, depends on the details of the termination at the surface and can be determined by evaluating the macro-

scopic “surface charge” that arises when charges +d (−1) are

a2

###### a b

- d2
- d3


x2

x3 x2

s3

R=

s2

e d c 0

d1

x1

a3

s1

x3

a1

x1

c (.1,.1,.1;0) d (0,.1,.1;0) e (-.1,.1,.1;0)

- FIG. 2: Deformed kagome lattice model. a shows our convention for labeling the states. b is a ternary plot of the phase diagram for


ﬁxed x1 + x2 + x3 > 0. The phases are labeled by R, which is zero in the central phase and a nearest neighbor lattice vector in the other phases. c, d and e show representative structures for R = 0 (c) and R = 0 (e) and the transition between them (d). The insets are density plots of the smallest mode frequency as a function of k in the BZ. In c the gap vanishes only at k = 0, while in d it vanishes on the line kx = 0. In e the gap vanishes only at k = 0, but has a quadratic dependence in some directions for small k.

placed on the sites (bonds) in a manner analogous to the “pebble game”4. This can be found by deﬁning a bulk unit cell with basis vectors d˜a that accommodates the surface with no leftover sites or bonds (see Fig. 4a below). Note that this unit cell depends on the surface termination and, in general, will be different from the “standard” unit cell used for νTS. The local count is then the surface polarization charge given by the dipole moment per unit cell. We ﬁnd

ν˜L ≡ νLS/Ncell = G · RL/2π, (9) where

d˜i −

d˜m. (10)

RL = d

sites i

bonds m

RL is similar to r0 deﬁned above (which is assumed to be zero), but it is in general a different Bravais lattice vector. The total zero mode count on the surface then follows from equations (3), (8), and (9).

Deformed Kagome Lattice Model

We now illustrate the topological boundary modes of a twodimensional lattice with the connectivity of the kagome lattice, but with deformed positions. The deformed kagome lattice is speciﬁed by its Bravais lattice and basis vectors for the three atoms per unit cell. For simplicity, we ﬁx the Bravais lattice to be hexagonal with primitive vectors ap+1 = (cos2πp/3,sin2πp/3). We parameterize the basis vectors as d1 = a1/2 + s2, d2 = a2/2 − s1 and d3 = a3/2. Deﬁning s3 = −s1 − s2, sp describe the displacement of

dp−1 relative to the midpoint of the line along ap that connects its neighbors at dp+1 ± ap∓1 (with p deﬁned mod 3), as indicated in Fig. 2a. sp are speciﬁed by 6 parameters with 2 constraints. A symmetrical representation is to take sp = xp(ap−1 − ap+1) + ypap and to use independent variables (x1,x2,x3;z) with z = y1 + y2 + y3. The constraints then determine yp = z/3 + xp−1 − xp+1. xp describes the buckling of the line of bonds along ap, so that when xp = 0 the line of bonds is straight. z describes the asymmetry in the sizes of the two triangles. (0,0,0;0) is the undistorted kagome lattice, while (x,x,x;0) is the twisted kagome lattice, studied in22, with twist angle θ = tan−1(2√3x).

It is straightforward to solve for the bulk normal modes of the periodic lattice. When any of the xp are zero the gap vanishes on the line k·ap = 0 in the BZ. This line of zero modes is a special property of this model that follows from the presence of straight lines of bonds along ap. When xp = 0 the system is at a critical point separating topologically distinct bulk phases. The phase diagram features the eight octants speciﬁed by the signs of x1,2,3. (+ + +) and (− − −) describe states, topologically equivalent to the twisted kagome lattice, with RT = 0. The remaining 6 octants are states that are topologically distinct, but are related to each other by C6 rotations. We ﬁnd

RT =

3

apsgnxp/2 (11)

p=1

is independent of z. Fig. 2b shows a ternary plot of the phase diagram as a function of x1,x2,x3 for z = 0 and a ﬁxed value of x1 +x2 +x3. Fig. 2c,d,e show representative structures for the RT = 0 phase (Fig. 2c), the RT = 0 phase (Fig. 2e), and the transition between them (Fig. 2d). The insets show density plots of the lowest frequency mode, which highlight the gapless point due to the acoustic mode in Fig. 2c and the gapless line due to states of self stress in Fig. 2d. In Fig. 2e, the gap vanishes only at the origin, but the cross arises because acoustic modes vary quadratically rather than linearly with k along its axes. This behavior will be discussed in the next section.

We next examine the boundary modes of the deformed kagome lattice. Fig. 3 shows a system with periodic boundary conditions in both directions that has domain walls separating (.1,.1,.1;0) from (.1,.1,−.1;0). Since there are no broken bonds, the local count is νSL = 0. On the two domain walls, equation (8) predicts

ν˜T = G · (R1T − R2T) = +1(−1), (12)

for the left (right) domain wall, where R1T and R2T characterize the material to the left and right of the domain wall,

respectively (See ﬁg. 1 in the supplementary material). Note that the indices of the two domain walls are opposite in sign so that the total index ν of equation (1) is zero as required. Fig. 2c shows the spectrum of H (which has both positive and negative eigenvalues) as a function of the momentum kx parallel to the domain wall. The zero modes of H include both the ﬂoppy modes and the states of self-stress. In the vicinity of kx = 0 the zero modes on the two domain walls couple

| | |
|---|---|


0.2

ω

x

0.1

0

- -0.1
- -0.2


a b

RT=0 RT= RT=0

-π 0 π

kx

- FIG. 3: Zero modes at domain walls. a shows a lattice with periodic boundary conditions and two domain walls, the left one between (.1, .1, .1, 0) and (.1, .1, −.1, 0) with zero modes and the right one between (.1, .1, −.1, 0) and (.1, .1, +.1, 0) with states of self stress.

The zero mode eigenvectors at kx = π are indicated for the ﬂoppy mode (arrows) and the state of self-stress (red (+) and green (-) thickened bonds). b shows the vibrational mode dispersion as a function of kx.

|(c)|υT = 0 υL = +1<br><br>~ ~|
|---|---|


|(b)|υT = -2 υL = +2<br><br>~ ~|
|---|---|


|(d)|υT = +1 υL = +2<br><br>~ ~|
|---|---|


0

0.1

0.2

-π 0 π

0

0.1

0.2

-π 0 π

0

0.1

0.2

-π 0 π

r0=0

RL(b)

RL(d)

RL(c)

(a) RT

- FIG. 4: Zero modes at the edge. a shows a (−.05, .05, .05, 0) lattice indicating three edges. b, c and d show the vibrational mode spectrum computed for a strip with one edge as shown in a and the other edge with a clamped boundary condtion. The zero mode count on each surface is compared with equations (3,8,9).


and split because their penetration depth diverges as kx → 0. The eigenvectors for the zero modes at kx = π are indicated in Fig. 3a by the arrows and the thickened bonds.

Fig. 4a shows a segment of a (−.05,.05,.05;0) lattice with three different different edges. For each edge, a unit cell that accommodates the edge is shown, along with the corresponding RL, from which ν˜L is determined. In the interior, a “standard” unit cell, with r0 = 0 is shown. Figs. 4b, c, d show the spectrum for a strip with one edge given by the corresponding edge in Fig. 4a with free boundary conditions. The other edge of the strip is terminated with clamped boundary conditions, so that the ﬂoppy modes are due solely to the free edge. The number of zero modes per unit cell agrees with equations (8) and (9) for each surface given RL, RT. The zero modes acquire a ﬁnite frequency when the penetration length of the zero mode approaches the strip width, which leads to Gaussian “bumps” near k = 0, which will be discussed in the next section. In Fig. 4d, one of the three zero modes can be identiﬁed as a localized “rattler”, which remains localized on the surface sites, even for k → 0.

Continuum Elasticity Theory

Unlike electronic spectra, phonon spectra have acoustic modes whose frequencies vanish as k → 0. These excitations along with macroscopic elastic distortions and longwavelength surface Rayleigh waves are described by a continuum elastic energy quadratic in the elastic strain tensor uij. Elastic energies are restricted to small wavenumber and cannot by themselves determine topological characteristics, like those we are considering, that depend on properties across the BZ. Nevertheless the elastic energies of our model isostatic lattices fall into distinct classes depending on the topological class of the lattice. For simplicity we focus on (x1,x2,x2;0) states, where x2 > 0 is ﬁxed and x1 is allowed to vary. The elastic energy density f can be written

K 2

[(uxx − a1uyy)2 + 2a4u2xy]. (13)

f =

We ﬁnd that a1 ∝ x1 for small x1, while a4 > 0 and K are positive and smoothly varying near x1 = 0. Thus, the RT = 0 and RT = 0 sectors are distinguished by the sign of a1. f = 0 for shape distortions with uxx = a1uyy and uxy = 0. When a1 > 0, the distortion has a negative Poisson ratio47, expanding or contracting in orthogonal directions (a feature shared by the twisted kagome lattice22); when a1 < 0, the distortion has the more usual positive Poisson ratio. Finally when a1 = 0, uniaxial compressions along y costs no energy.

Expanding detQT for small k provides useful information about the bulk- and surface-mode structure. To order k3,

detQT = A[kx2 + a1ky2 + ic(kx3 − 3kxky2)] + O(k4), (14)

where A,c > 0 for small x1. a1 is the same as in equation (13). Long-wavelength zero modes are solutions of detQT = 0. The quadratic term, which corresponds to the elastic theory, equation (13), reveals an important difference between the bulk acoustic modes of RT = 0 and RT = 0. In the former case, a1 > 0, detQT = 0 only at k = 0. For a1 < 0, though, to order k2, detQT = 0 for kx = ± |a1|ky, so the elastic theory predicts lines of gapless bulk modes. The degeneracy is lifted by the k3 term, leading to a k2 dispersion along those lines, which can be seen by the cross in the density map of Fig. 2e.

detQT(k → 0) vanishes for complex wavenumbers associated with zero-frequency Rayleigh surface waves. Writing k = k⊥nˆ + k||zˆ × nˆ for a surface whose outward normal nˆ makes an angle θ with xˆ, there is an ω = 0 Rayleigh wave with penetration depth |Imk⊥|−1 if Imk⊥ < 0. To order k||2 there are two solutions,

sinθ ± i√a1 cosθ cosθ ∓ i√a1 sinθ

i(3 + a1)d 2(cosθ ± i√a1 sinθ)3

k⊥± =

k||2.

k|| +

(15) When a1 > 0, the linear term is always ﬁnite and nonzero, and Im k⊥± have opposite signs, indicating that there can be acoustic surface zero modes on all surfaces. These are the classical Rayleigh waves predicted by the elastic theory, with penetration depth O(k||−1). When a1 < 0, the linear term in

k|| is real and Imk⊥± ∝ k||2. The number of long wavelength surface zero modes depends on the angle of the surface. When

|θ| < θc = cot−1 |a1|, Imk⊥± are both positive, and there are no acoustic surface zero modes. The opposite surface, |θ−

π| < θc, has two acoustic surface modes. For θc < θ < π − θc Imk⊥± have opposite sign, so there is one mode. This is consistent with the mode structure in Fig. 4: The O(k||−2) penetration depth explains the Gaussian proﬁle of the k → 0 bumps in the zero modes, which are due to the ﬁnite strip width. In (b) a θ = 0 surface has no zero modes. (c) shows a θ = π/2 > θc surface with one long-wavelength surface zero mode. (d) shows the spectrum with π − θ = π/6 < θc with two bumps indicating two deeply penetrating longwavelength zero modes in addition to one non-acoustic mode localized at that surface.

Conclusions

We have developed a general theory of topological phases of isostatic lattices, which explains the boundary zero modes and connects to the topological band theory of electronic sys-

tems. This points to several directions for future studies. It will be interesting to study 3D lattice models, as well as lattices that support point singularities in detQ(k) analogous to Dirac semimetals. Finally, it will be interesting to explore connections with theories of frustrated magnetism48.

Correspondence and requests for materials should be sent to Tom Lubensky.

Acknowledgments

TCL is grateful for the hospitality of the Newton Institute, where some of this work was carried out. This work was supported in part by a Simons Investigator award to CLK from the Simons Foundation and by the National Science Foundation under DMR-1104707 (TCL) and DMR-0906175 (CLK).

Author contributions: CLK and TCL contributed to the formulation of the problem, theoretical calculations, and the preparation of the manuscript.

Competing ﬁnancial interests statement: The authors have no competing ﬁnancial interests to declare.

- 1 Phillips, J. C. Topology of Covalent Non-Crystalline Solids 2. Medium-Range Order in Chalcogenide Alloys and α − Si((Ge). Journal of Non-Crystalline Solids 43, 37–77 (1981).
- 2 Thorpe, M. F. Continuous Deformations in Random Networks. Journal of Non-Crystalline Solids 57, 355–370 (1983).
- 3 Feng, S. & Sen, P. N. Percolation on Elastic Networks - New Exponent and Threshold. Physical Review Letters 52, 216–219

(1984).

- 4 Jacobs, D. J. & Thorpe, M. F. Generic Rigidity Percolation - the Pebble Game. Physical Review Letters 75, 4051–4054 (1995).
- 5 Liu, A. J. & Nagel, S. R. Nonlinear dynamics - Jamming is not just cool any more. Nature 396, 21–22 (1998).
- 6 Liu, A. J. & Nagel, S. R. Granular and jammed materials. Soft Matter 6, 2869–2870 (2010).
- 7 Liu, A. J. & Nagel, S. R. The Jamming Transition and the Marginally Jammed Solid. Annual Review of Condensed Matter Physics 1, 347–369 (2010).
- 8 Torquato, S. & Stillinger, F. H. Jammed hard-particle packings: From Kepler to Bernal and beyond. Reviews of Modern Physics 82, 2633–2672 (2010).
- 9 Wyart, M., Nagel, S. R. & Witten, T. A. Geometric origin of excess low-frequency vibrational modes in weakly connected amorphous solids. Europhysics Letters 72, 486–492 (2005).
- 10 Wyart, M. On the rigidity of amorphous solids. Annales De Physique 30, 1–96 (2005).
- 11 Wilhelm, J. & Frey, E. Elasticity of stiff polymer networks. Physical Review Letters 91, 108103 (2003).
- 12 Heussinger, C. & Frey, E. Floppy modes and nonafﬁne deformations in random ﬁber networks. Physical Review Letters 97, 105501 (2006).
- 13 Huisman, L. & Lubensky, T. C. Internal stresses, normal modes and non-afﬁnity in three-dimensional biopolymer networks. Physical Review Letters 106, 088301 (2011).
- 14 Broedersz, C., Mao, X., Lubensky, T. C. & MacKintosh, F. C. Criticality and isostaticity in ﬁber networks. Nature Physics 7,


- 983–988 (2011).
- 15 Souslov, A., Liu, A. J. & Lubensky, T. C. Elasticity and response in nearly isostatic periodic lattices. Physical Review Letters 103, 205503 (2009).
- 16 Mao, X. M., Xu, N. & Lubensky, T. C. Soft Modes and Elasticity of Nearly Isostatic Lattices: Randomness and Dissipation. Physical Review Letters 104, 085504 (2010).
- 17 Mao, X. M. & Lubensky, T. C. Coherent potential approximation of random nearly isostatic kagome lattice. Physical Review E 83, 011111 (2011).
- 18 Mao, X. M., Stenull, O. & Lubensky, T. C. Elasticity of a ﬁlamentous kagome lattice. Physical Review E 87, 042602 (2013).
- 19 Kapko, V., Treacy, M. M. J., Thorpe, M. F. & Guest, S. D. On the collapse of locally isostatic networks. Proc. Royal Soc. A 465, 3517–3530 (2009).
- 20 Maxwell, J. C. On the Calculaton of the Equilibirum Stiffness of Frames. Philosophical Magazine 27, 294-299 (1865).
- 21 Calladine, C. R. Buckminster Fuller’s “Tensegrity” Structures and Clerk Maxwell’s Rules for the Construction of Stiff Frames. International Journal of Solids and Structures 14, 161–172 (1978).
- 22 Sun, K., Mao, X. & Lubensky, T. C. Surface phonons, elastic response, and conformal invariance in twisted kagome lattices. PNAS 109, 12369–12374 (2012).
- 23 Halperin, B. I. Quantized Hall Conductance, Current-Carrying Edge States, and the Existence of Extended States in a TwoDimensional Disordered Potential. Physical Review B 25, 2185– 2190 (1982).
- 24 Haldane, F. D. M. Model for a Quantum Hall Effect Without Landau Levels - Condensed Matter Realization of the Parity Anomaly. Physical Review Letters 61, 2015–2018 (1988).
- 25 Kane, C. L. & Mele, E. J. Z(2) topological order and the quantum spin Hall effect. Physical Review Letters 95, 146802 (2005).
- 26 Bernevig, B. A., Hughes, T. L. & Zhang, S.-C. Quantum Spin Hall Effect and Topological Phase Transition in HgTe Quantum Wells. Science 314, 1757–1761 (2006).


- 27 Moore, J. E. & Balents, L. Topological invariants of time-reversalinvariant band structures. Physical Review B 75, 121306 (2007).
- 28 Fu, L., Kane, C. L. & Mele, E. J. Topological Insulators in Three Dimensions. Physical Review Letters 98, 106803 (2007).
- 29 Hasan, M. Z. & Kane, C. L. Colloquium: Topological insulators. Reviews of Modern Physics 82, 3045–3067 (2010).
- 30 Qi, X.-L. & Zhang, S.-C. Topological insulators and superconductors. Reviews of Modern Physics 83, 1057–1110 (2011).
- 31 Su, W. P., Schrieffer, J. R. & Heeger, A. J. Solitons in Polyacetalene. Physical Review Letters 42, 1698 (1979).
- 32 Nakahara, M. Geometry, Topology and Physics (Hilger, Bristol, 1990).
- 33 Dirac, P. A. M. The Quantum Theory of the Electron. Royal Society of London Proceedings Series A 117, 610–624 (1928).
- 34 Witten, E. Dynamical breaking of supersymmetry. Nuclear Physics B 188, 513 – 554 (1981).
- 35 Cooper, F., Khare, A. & Sukhatme, U. Supersymmetry and quantum mechanics. Physics Reports 251, 267 – 385 (1995).
- 36 Schnyder, A. P., Ryu, S., Furusaki, A. & Ludwig, A. W. W. Classiﬁcation of topological insulators and superconductors in three spatial dimensions. Physical Review B 78, 195125 (2008).
- 37 Jackiw, R. & Rebbi, C. Solitons with Fermion Number 1/2. Physical Review D 13, 3398–3409 (1976).
- 38 Volovik, G. E. The Universe in a Helium Droplet (Clarenden, Oxford, 2003).
- 39 Haldane, F. D. M. & Raghu, S. Possible Realization of Directional Optical Waveguides in Photonic Crystals with Broken Time-Reversal Symmetry. Physical Review Letters 100, 013904

(2008).

- 40 Wang, Z., Chong, Y. D., Joannopoulos, J. D. & Soljaˇci´c, M. Reﬂection-Free One-Way Edge Modes in a Gyromagnetic Photonic Crystal. Physical Review Letters 100, 013905 (2008).
- 41 Prodan, E. & Prodan, C. Topological Phonon Modes and Their Role in Dynamic Instability of Microtubules. Physical Review Letters 103, 248101 (2009).
- 42 Berg, N., Joel, K., Koolyk, M. & Prodan, E. Topological phonon modes in ﬁlamentary structures. Physical Review E 83, 021913

(2011).

- 43 Callias, C. Axial Anomalies and Index Theorems on Open Spaces. Communications in Mathematical Physics 62, 213–234 (1978).
- 44 Bott, R. & Seeley, R. Some Remarks on Paper of Callias. Communications in Mathematical Physics 62, 235–245 (1978).
- 45 Hirayama, M. & Torii, T. Fermion Fractionalization and Index Theorem. Progress of Theoretical Physics 68, 1354–1364 (1982).
- 46 Niemi, A. J. & Semenoff, G. W. Fermion Number Fractionalization in Quantum Field Theory. Physics Reports 135, 99–193

(1986).

- 47 Lakes, R. Foam Structures with a Negative Poisson’s Ratio. Science 235, 1038–1040 (1987).
- 48 Lawler, M. J. Emergent gauge dynamics of highly frustrated magnets. New Journal of Physics 15, 043043 (2013).


SUPPLEMENTARY ONLINE MATERIALS

Proof of Index Theorem

In this appendix we provide details of the proof of the index theorem discussed in the text. Our starting point is equation (4), which describes the zero-mode count in a region S of a larger system. Using the fact that {H,τz} = [ρS(ˆr),τz] = 0

it is straightforward to check that equations (3-5) imply that

1 H + i 

- 1

- 2


Tr τz

[ρS(ˆr),H] . (16)

νTS =

lim

→0

Since [ρS,H] = 0 for ρS = 1, and H has a ﬁnite range a, νTS comes only from the boundary of region S where ρS(r) varies. If we assume that the boundary region is gapped and that ρ(r) varies slowly on the scale L a, then we safely take to zero and expand to leading order in a/L. Since [ρS(ˆr),H]αβ = Hαβ(ρS(rα) − ρS(rβ)) ∼ Hαβ(rα − rβ) · ∇ρ(rβ), we may write

- 1

- 2


Tr τz∇ρ(ˆr) · H−1[ˆr,H] . (17)

νTS =

We next suppose that in the boundary region the lattice is periodic, so that the trace may be evaluated in a basis of plane waves:

1 √

|k,a =

N R

expik · (R + da)|R + da , (18)

where R is a Bravais lattice vector in a system with periodic boundary conditions and N unit cells. da are basis vectors for the dns + nb sites and bonds per unit cell. The phases are chosen such that the position operator is ˆr ∼ i∇k. In this basis, the Bloch Hamiltonian H(k) is a dns + nb square matrix with off diagonal blocks Q(k) and Q†(k), where

Qab(k) = k,a|Q|k,b . (19) νTS then has the form

νTS =

dd−1S PT · nˆ (20)

∂S

where the integral is over the boundary of S with inward normal nˆ, and

PT =

BZ

It is useful, to write

ddk (2π)d

Im Tr[Q−1∇kQ]. (21)

ImTr[Q−1∇kQ] = ∇kImlog detQ. (22) It is then straightforward to show that

detQ(k + G) = detQ(k)exp[−iG · r0], (23) where

dm. (24)

di −

r0 = d

sites i

bonds m

For a general lattice, r0 is non zero. However, if the coordination number of site i is zi then r0 = i(d − zi/2)di + R, where R is a Bravais lattice vector. Thus, for an isostatic lattice with uniform coordination z = 2d, r0 is a Bravais lattice vector, and it is always possible to shift dm by lattice vectors to make r0 = 0. In the text of the paper, we assumed r0 = 0.

1 2

RT RT

n^ n^

G

∂S ∂S

S

- a ρS(r) = 0 ρS(r) = 1 ρS(r) = 0

- b


Vcell

n^ G

### ∂S A

cell

S

dcell

ρS(r) = 0 ρS(r) = 1

FIG. 1: Evaluating the zero mode count. a Cylindrical geometry for evaluating the zero mode count for a domain wall between R1T and R2T, indicated by the dashed line. b Cylindrical geometry for evaluating the zero mode count for a surface indexed by reciprocal lattice vector G. The region S covers half the cylinder. The boundary ∂S is deep in the interior. b also shows our notation for the surface unit cell.

Here we will keep it general, and show that while r0 affects νTS, its effect is canceled by a compensating term in νLS.

For the general case, let us write detQ(k) = q0(k)exp[−ik · r0], where q0(k) = q0(k + G) is periodic in the BZ. Equation (21) then involves two pieces:

1 Vcell

[−r0 + RT]. (25)

PT =

Here RT is a Bravias lattice vector describing the winding numbers of the phase of q0(k) around the cycles of the BZ. It may be written RT = i niai with

- 1

- 2πi C


ni =

i

dk · ∇k log q0(k) (26)

where as in the text, we assume that for a given cycle Ci of the BZ the winding number is path indpendent.

Application to zero modes at a domain wall

To determine the zero mode count at a domain wall be-

tween topological states R1T and R2T, we consider a cylinder perpendicular to the domain wall (or a similar construc-

tion for d dimensions). We expect the zero mode count to be proportional to the “area” A (or length in 2D) of the domain wall. We will, therefore, be interested in the zero mode count per unit cell, νS/Ncell, where Ncell = A/Acell,

and Acell = Vcell/dcell is the projected area of the surface unit cell, which can be expressed in terms of the volume of

the bulk unit cell Vcell and the distance dcell between Bragg planes. Referring to Supplementary Fig. 1a, we use equation (25) to evaluate equation (20) away from the domain wall to give νT = (A/Vcell)(R1T − R2T) · nˆ, where nˆ is the unit vector pointing to the right. The zero mode count per unit cell can be expressed in terms of the reciprocal lattice vector G = 2πn/dˆ cell that indexes the domain wall as

#### νTS/Ncell = G · (R1T − R2T)/2π. (27)

Application to zero modes at the edge

We next determine the number of zero modes localized on a surface (or edge in 2d) indexed by a reciprocal lattice vector G. Consider a cylinder with axis perpendicular to G and deﬁne the region S to be the points nearest to one end of the cylinder, as shown in Supplementary Fig. 1b. A similar construction can be used to count the zero modes on a surface in d dimensions.

νTS is determined by evaluating equation (6) deep in the bulk of the cylinder where the lattice is periodic. From equation

(21) we may write

νTS/Ncell = G · (RT − r0)/2π. (28)

The local count, νLS, depends on the details of the termination at the surface and is given by the macroscopic “surface charge” that arises when positive charges +d are placed on the sites and negative charges −1 are placed on the bonds. As discussed in the text, it can be determined by evaluating the dipole moment of a unit cell with site and bond vectors d˜a that is deﬁned so that the surface can be accomodated with no left over sites or bonds. This unit cell is in general different from the unit cell used to compute νTS, and its dipole moment is in general not quantized. However, since the difference is due to a redeﬁnition of which bond is associated with which unit cell, the dipole moment differs from r0 by a Bravais lattice vector,

d˜i −

RL = d

sites i

d˜m − r0. (29)

bonds m

It follows that the local count may be written

νLS/Ncell = G · (RL + r0)/2π. (30) The total zero mode count on the edge is then

νS/Ncell = G · (RL + RT)/2π. (31)

It can be seen that the dependence on r0, which depends on the arbitrary unit cell used to deﬁne νTS cancels.

