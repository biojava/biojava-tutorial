Protein Symmetry using BioJava
================================================================

BioJava can be used to detect, analyze, and visualize **symmetry** and
**pseudo-symmetry** in the **quaternary** (biological assembly) and tertiary
(**internal**) structural levels of proteins.

## Quaternary Symmetry

The **quaternary symmetry** of a structure defines the relation and arrangement of the individual chains or groups of chains that are part of a biological assembly. 
For a more exhaustive explanation about protein quaternary symmetery and the different types visit the [PDB help page](http://www.rcsb.org/pdb/staticHelp.do?p=help/viewers/jmol_symmetry_view.html).

In the **quaternary symmetry** detection problem, we are given a set of chains (subunits) that are part of a biological assembly as input, defined by their atomic coordinates, and we are required to find the higest overall symmetry group that
relates them as ouptut. 
The solution is divided into the following steps:

1. First, we need to identify the chains that are identical (or similar
in the pseudo-symmetry case). For that purpose, we perform a pairwise alignment of all
chains and identify **clusters of identical or similar subunits**.
2. Next, we reduce each of the polypeptide chains to a single point, their **centroid** (center of mass).
3. Afterwards, we try different **symmetry operations** using a grid search to superimpose the chain centroids
and score them using the RMSD.
4. Finally, based on the parameters (cutoffs), we determine the **overall symmetry** of the
structure, with the symmetry relations obtained in the previous step.
5. In case of asymmetric structure, we discard combinatorially a number of chains and try
to detect any **local symmetries** present (symmetry that does not involve all subunits of the biological assembly).

The **quaternary symmetry** detection algorithm is implemented in the biojava class
[QuatSymmetryDetector](http://www.biojava.org/docs/api/org/biojava/nbio/structure/symmetry/core/QuatSymmetryDetector).
An example of how to use it programatically is shown below:

```java
// First download the structure in the biological assembly form
Structure s;

// Set some parameters if needed different than DEFAULT - see descriptions
QuatSymmetryParameters parameters = new QuatSymmetryParameters();
SubunitClustererParameters clusterParams = new SubunitClustererParameters();

// Instantiate the detector
QuatSymmetryDetector detector = QuatSymmetryDetector(s, parameters, clusterParams);

// Static methods in QuatSymmetryDetector perform the calculation
QuatSymmetryResults globalResults = QuatSymmetryDetector.getGlobalSymmetry(s, parameters, clusterParams);
List<QuatSymmetryResults> localResults = QuatSymmetryDetector.getLocalSymmetries(s, parameters, clusterParams);

```
See also the [demo](https://github.com/biojava/biojava/blob/885600670be75b7f6bc5216bff52a93f43fff09e/biojava-structure/src/main/java/demo/DemoSymmetry.java#L37-L59) provided in **BioJava** for a real case working example.

The returned `QuatSymmetryResults` object contains all the information of the subunit clustering and structural symmetry.
This object will be used later to obtain axes of symmetry, point group name, stoichiometry or even display the results in Jmol.
The return object of quaternary symmetry (`QuatSymmetryResults`) contains the 
In case of asymmetrical structure, the result is a C1 point group.
The return type of the local symmetry is a `List` because there can be multiple valid options of local symmetry.
The list will be empty if there exist no local symmetries in the structure.


### Global Symmetry

In the **global symmetry** mode all chains have to be part of the symmetry result.

#### Point Group

In a **point group** a single or multiple rotation axes define the overall symmetry
operations, with the property that all the axes coincide in the same point.

![PDB ID 1VYM](img/symm_pg.png)

#### Helical

In **helical** symmetry there is a single axis with rotation and translation
components.

![PDB ID 4UDV](img/symm_helical.png)

### Local Symmetry

In **local symmetry** a number of chains is left out, so that the symmetry only applies to a subset of chains.

![PDB ID 4F88](img/symm_local.png)

### Pseudo-Symmetry

In **pseudo-symmetry** the chains related by the symmetry are not completely
identical, but they share a sequence or structural similarity above the pseudo-symmetry
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

The **CE-Symm** algorithm was originally developed by [Myers-Turnbull D., Bliven SE.,
Rose PW., Aziz ZK., Youkharibache P., Bourne PE. & Prlić A. in 2014]
(http://www.sciencedirect.com/science/article/pii/S0022283614001557)  [![pubmed](http://img.shields.io/badge/in-pubmed-blue.svg?style=flat)](http://www.ncbi.nlm.nih.gov/pubmed/24681267).
As the name of the algorithm explicitly states, **CE-Symm** uses the Combinatorial
Extension (**CE**) algorithm to generate an alignment of the structure chain to itself,
disabling the identity alignment (the diagonal of the **DotPlot** representation of a
structure alignment). This allows the identification of alternative self-alignments,
which are related to symmetry and/or structural repeats inside the chain.

By a procedure called **refinement**, the subunits of the chain that are part of the symmetry
are defined and a **multiple alignment** is created. This process can be thought as to
divide the chain into other subchains, and then superimposing each subchain to each other to
create a multiple alignment of the subunits, respecting the symmetry axes.

The **internal symmetry** detection algorithm is implemented in the biojava class
[CeSymm](http://www.biojava.org/docs/api/org/biojava/nbio/structure/symmetry/internal/CeSymm).
It returns a `MultipleAlignment` object, see the explanation of the model in [Data Models](alignment-data-model.md),
that describes the similarity of the internal repeats. In case of no symmetry detected, the
returned alignment represents the optimal self-alignment produced by the first step of the **CE-Symm**
algorithm.

```java
//Input the atoms in a chain as an array
Atom[] atoms = StructureTools.getRepresentativeAtomArray(chain);

//Initialize the algorithm
CeSymm ceSymm = new CeSymm();

//Choose some parameters
CESymmParameters params = ceSymm.getParameters();
params.setRefineMethod(RefineMethod.SINGLE);
params.setOptimization(true);
params.setMultipleAxes(true);

//Run the symmetry analysis - alignment as an output
MultipleAlignment symmetry = ceSymm.analyze(atoms, params);

//Test if the alignment returned was refined with
boolean refined = SymmetryTools.isRefined(symmetry);

//Get the axes of symmetry from the aligner
SymmetryAxes axes = ceSymm.getSymmetryAxes();

//Display the results in jmol with the SymmetryDisplay
SymmetryDisplay.display(symmetry, axes);

//Show the point group, if any of the internal symmetry
QuatSymmetryResults pg = SymmetryTools.getQuaternarySymmetry(symmetry);
System.out.println(pg.getSymmetry());

```

To enable some extra features in the display, a `SymmetryDisplay`
class has been created, although the `MultipleAlignmentDisplay` method
can also be used for that purpose (it will not show symmetry axes or
symmetry menus).

Lastly, the `SymmetryGUI` class in the **structure-gui** package
provides a GUI to trigger internal symmetry analysis, equivalent
to the GUI to trigger structure alignments.

### Symmetry Display

The symmetry display is similar to the **quaternary symmetry**, because
part of the code is shared. See for example this beta-propeller (1U6D),
where the repeated beta-sheets are connected by a linker forming a C6
point group internal symmetry:

![PDB ID 1U6D](img/symm_internal.png)

#### Hierarchical Symmetry

One additional feature of the **internal symmetry** display is the representation
of hierarchical symmetries and repeats. Contrary to point groups, some structures
have different **levels** of symmetry. That is, the whole strucutre has, e.g. C2
symmetry and, at the same time, each of the two parts has C2 symmetry, but the axes
of both levels are not related by a point group (i.e. they do not cross to a single
point).

A very clear example are the beta-gamma-crystallins, like 4GCR:

![PDB ID 4GCR](img/symm_hierarchy.png)

#### Subunit Multiple Alignment

Another feature of the display is the option to show the **multiple alignment** of
the symmetry related subunits created during the **refinement** process. Search for
the option *Subunit Superposition* in the *symmetry* menu of the Jmol window. For
the previous example the display looks like that:

![PDB ID 4GCR](img/symm_subunits.png)

The subunit display highlights the differences and similarities between the symmetry
related subunits of the chain, and helps the user to identify conseved and divergent
regions, with the help of the *Sequence Alignment Panel*.

## Quaternary + Internal Overall Symmetry

Finally, the internal and quaternary symmetries can be merged to obtain the
overall combined symmetry. As we have seen before, the protein 1VYM is a DNA-clamp that
has three chains arranged in a C3 symmetry. 
Each chain is internally fourfold symmetric with two levels of symmetry. We can analyze the overall symmetry of the structure by considering together the C3 quaternary symmetry and the fourfold internal symmetry. 
In this case, the internal symmetry **augments** the point group of the quaternary symmetry to a D6 overall symmetry, as we can see in the figure below:

![PDB ID 1VYM](img/symm_combined.png)

An example of how to toggle the **combined symmetry** (quaternary + internal symmetries) programatically is shown below:

```java
// First download the structure in the biological assembly form
Structure s;

// Initialize default parameters
QuatSymmetryParameters parameters = new QuatSymmetryParameters();
SubunitClustererParameters clusterParams = new SubunitClustererParameters();

// In SubunitClustererParameters set the clustering method to STRUCTURE and the internal symmetry option to true
clusterParams.setClustererMethod(SubunitClustererMethod.STRUCTURE);
clusterParams.setInternalSymmetry(true);

// You can lower the default structural coverage to improve the recall
clusterParams.setStructureCoverageThreshold(0.75);

// Instantiate the detector
QuatSymmetryDetector detector = QuatSymmetryDetector(s, parameters, clusterParams);

// Static methods in QuatSymmetryDetector perform the calculation
QuatSymmetryResults overallResults = QuatSymmetryDetector.getGlobalSymmetry(s, parameters, clusterParams);

```

See also the [test](https://github.com/biocryst/biojava/blob/df22da37a86a0dba3fb35bee7e17300d402ab469/biojava-integrationtest/src/test/java/org/biojava/nbio/structure/test/symmetry/TestQuatSymmetryDetectorExamples.java#L167-L192) provided in **BioJava** for a real case working example.


## Please Cite

**Analyzing the symmetrical arrangement of structural repeats in proteins with CE-Symm**<br/>
*Spencer E Bliven, Aleix Lafita, Peter W Rose, Guido Capitani, Andreas Prlić, & Philip E Bourne* <br/>
[PLOS Computational Biology (2019) 15 (4):e1006842.](https://journals.plos.org/ploscompbiol/article/citation?id=10.1371/journal.pcbi.1006842) <br/>
[![doi](https://img.shields.io/badge/doi-10.1371%2Fjournal.pcbi.1006842-blue.svg?style=flat)](https://doi.org/10.1371/journal.pcbi.1006842) [![pubmed](https://img.shields.io/badge/pubmed-31009453-blue.svg?style=flat)](http://www.ncbi.nlm.nih.gov/pubmed/31009453)



<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 3: The Structure Modules](README.md)
| Chapter 14 : Protein Symmetry

Prev: [Chapter 13 - Finding all Interfaces in Crystal: Crystal Contacts](crystal-contacts.md)

Next: [Chapter 15 : Protein Secondary Structure](secstruc.md)
