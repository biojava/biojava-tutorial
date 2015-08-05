Protein Symmetry using BioJava
================================================================

BioJava can be used to detect, analyze, and visualize **symmetry** and 
**pseudo-symmetry** in the quaternary (biological assembly) and tertiary 
(internal) structural levels.

## Quaternary Symmetry

The **quaternary symmetry** of a structure defines the relations between 
its individual chains or groups of chains. For a more extensive explanation 
about symmetery visit the [PDB help page]
(http://www.rcsb.org/pdb/staticHelp.do?p=help/viewers/jmol_symmetry_view.html).

In the **quaternary symmetry** detection problem, we are given a set of chains
with its `Atom` coordinates and we are asked to find the higest overall symmetry that
relates them. The solution is divided into the following steps:

1. First, we need to identify the chains that are identical (or similar
in the pseudo-symmetry case). For that, we perform a pairwise alignment of all
chains and determine **clusters of identical chains**.
2. Next, we reduce the each chains to a single point, its **centroid** (center of mass).
3. After that, we try different **symmetry relations** to superimpose the chain centroids 
and obtain their RMSD.
4. At last, based on the parameters (cutoffs), we determine the **overall symmetry** of the
structure, with the symmetry relations obtained in the previous step.
5. In case of asymmetric structure, we discard combinatorially a number of chains and try
to detect any **local symmetries** present.

The **quaternary symmetry** detection algorithm is implemented in the biojava class
[QuatSymmetryDetector](http://www.biojava.org/docs/api/org/biojava/nbio/structure/symmetry/core/QuatSymmetryDetector).
An example of how to use it programatically is shown below:

```java
//First download the structure in the biological assembly form
Structure s;

//Set some parameters if needed different than DEFAULT - see descriptions
QuatSymmetryParameters parameters = new QuatSymmetryParameters();
parameters.setVerbose(true); //print information

//Instantiate the detector and calculate symmetry
CalcBioAssemblySymmetry calc = new CalcBioAssemblySymmetry(s, parameters);
QuatSymmetryDetector detector = calc.orient();

//Calculate and return global and local results
List<QuatSymmetryResults> globalResults = detector.getGlobalSymmetry();
List<List<QuatSymmetryResults>> localResults = detector.getLocalSymmetries();

```

The `QuatSymmetryResults` object contains all the information of the symmetry.
This object will be used later to obtain axes of symmetry, point group name,
stoichiometry or even display the results in Jmol.

### Global Symmetry

In **global symmetry** all chains have to be part of the symmetry description.

#### Point Group

In a **point group** a single or multiple rotation axes define the overall symmetry
operations, with the property that all the axes coincide in the same point.

![PDB ID 1G63](img/1G63.jpg)

#### Helical

In **helical** symmetry there is a single axis with rotation and translation
components.

![PDB ID 4UDV](img/symm_helical.png)

### Local Symmetry

In **local symmetry** a number of chains is left out, so that the symmetry
only applies to a subset of chains.

![PDB ID 4F88](img/symm_local.png)

### Pseudo-Symmetry

In **pseudo-symmetry** the chains related by the symmetry are not completely
identical, but they share a sequence similarity above the pseudo-symmetry 
similarity threshold. 
If we consider hemoglobin, at a 95% sequence identity threshold the alpha and 
beta subunits are considered different, which correspond to an A2B2 stoichiometry 
and a C2 point group. At the structural similarity level, all four chains are 
considered homologous (~45% sequence identity) with an A4 pseudostoichiometry and 
D2 pseudosymmetry. 

![PDB ID 4HHB](img/symm_pseudo.png)

## Internal Symmetry

**Internal symmetry** refers to the symmetry present in a single chain, that is, 
the tertiary structure. The algorithm implemented in biojava to detect internal 
symmetry is called **CE-Symm**.

### CE-Symm

`CeSymm`

### 
 
![SCOP ID d1jlya1](https://raw.github.com/rcsb/symmetry/master/docu/img/CeSymmScreenshotd1jlya1.png)
