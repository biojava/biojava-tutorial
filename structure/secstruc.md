Protein Secondary Structure
===========================

## What is Protein Secondary Structure?

Protein secondary structure (SS) is the general three-dimensional form of local segments of proteins. 
Secondary structure can be formally defined by the pattern of hydrogen bonds of the protein 
(such as alpha helices and beta sheets) that are observed in an atomic-resolution structure. 

More specifically, the secondary structure is defined by the patterns of hydrogen bonds formed between 
amine hydrogen (-NH) and carbonyl oxygen (C=O) atoms contained in the backbone peptide bonds of the protein. 

For more info see the Wikipedia article on [protein secondary structure]
(https://en.wikipedia.org/wiki/Protein_secondary_structure).

## Secondary Structure Annotation

### Information Sources

There are various ways to obtain the SS annotation of a protein structure:

- **Authors assignment**: the authors of the structure describe the SS, usually identifying helices 
and beta-sheets, and they assign the corresponding type to each residue involved. The authors assignment
can be found in the `PDB` and `mmCIF` file formats deposited in the PDB, and it can be parsed in **BioJava**
when a `Structure` is loaded.

- **Prediction from Atom coordinates**: there exist various programs to predict the SS of a protein. 
The algorithms use the atom coordinates of the aminoacids to detemine hydrogen bonds and geometrical patterns 
that define the different types of protein secondary structure. One of the first and most popular algorithms 
is `DSSP` (Dictionary of Secondary Structure of Proteins). **BioJava** has an implementation of the algorithm, 
written originally in C++, which will be described in the next section.

- **Prediction from sequence**: Other algorithms use only the aminoacid sequence (primary structure) of the protein,
nd predict the SS using the SS propensities of each aminoacid and multiple alignments with homologous sequences 
(i.e. [PSIPRED](http://bioinf.cs.ucl.ac.uk/psipred/)). At the moment **BioJava** does not have an implementation 
of this type, which would be more suitable for the sequence and alignment modules.

### Secondary Structure Types

Following the `DSSP` convention, **BioJava** defines 8 types of secondary structure:

    E = extended strand, participates in β ladder
    B = residue in isolated β-bridge
    H = α-helix
    G = 3-helix (3-10 helix)
    I = 5-helix (π-helix)
    T = hydrogen bonded turn
    S = bend
    _ = loop (any other type)

## Parsing Secondary Structure in BioJava

Currently there exist two alternatives to parse the secondary structure in **BioJava**: either from the PDB/mmCIF
files of deposited structures (author assignment) or from the output file of a DSSP prediction. Both file types
can be obtained from the PDB serevers, if available, so they can be automatically fetched by BioJava. 

As an example,you can find here the links of the structure **5PTI** to its 
[PDB file](http://www.rcsb.org/pdb/files/5PTI.pdb) (search for the HELIX and SHEET lines) and its 
[DSSP file](http://www.rcsb.org/pdb/files/5PTI.dssp).

Note that the DSSP prediction output is more detailed and complete than the authors assignment. 
The choice of one or the other will depend on the use case. 

Below you can find some examples of how to parse and assign the SS of a `Structure`:

```java
    String pdbID = "5pti";
    FileParsingParameters params = new FileParsingParameters();
    //Only change needed to the normal Structure loading
    params.setParseSecStruc(true); //this is false as DEFAULT

    AtomCache cache = new AtomCache();
    cache.setFileParsingParams(params);

    //The loaded Structure contains the SS assigned
    Structure s = cache.getStructure(pdbID);
    
    //If the more detailed DSSP prediction is required call this afterwards
    DSSPParser.fetch(pdbID, s, true); //Second parameter true overrides the previous SS
```

For more examples search in the **demo** package for `DemoLoadSecStruc`.

## Prediction of Secondary Structure in BioJava

### Algorithm

The algorithm implemented in BioJava for the prediction of SS is `DSSP`. It is described in the paper from 
[Kabsch W. & Sander C. in 1983](http://onlinelibrary.wiley.com/doi/10.1002/bip.360221211/abstract) 
[![pubmed](http://img.shields.io/badge/in-pubmed-blue.svg?style=flat)](http://www.ncbi.nlm.nih.gov/pubmed/6667333).
A brief explanation of the algorithm and the output format can be found
[here](http://swift.cmbi.ru.nl/gv/dssp/DSSP_3.html).

The interface is very easy: a single method, named *predict()*, calculates the SS and can assign it to the
input Structure overriding any previous annotation, like in the DSSPParser. An example can be found below:

```java
    String pdbID = "5pti";
    AtomCache cache = new AtomCache();
    
    //Load structure without any SS assignment
    Structure s = cache.getStructure(pdbID);
        
    //Predict and assign the SS of the Structure
    SecStrucPred ssp = new SecStrucPred(); //Instantiation needed
    ssp.predict(s, true); //true assigns the SS to the Structure
```

BioJava Class: [org.biojava.nbio.structure.secstruc.SecStrucPred]
(http://www.biojava.org/docs/api/org/biojava/nbio/structure/secstruc/SecStrucPred.html)

### Storage and Data Structures

Because there are different sources of SS annotation, the Sata Structure in **BioJava** that stores SS assignments 
has two levels. The top level `SecStrucInfo` is very general and only contains two properties: **assignment**
(String describing the source of information) and **type** the SS type.

However, there is an extended container `SecStrucState`, which is a subclass of `SecStrucInfo`, that stores
all the information of the hydrogen bonding, turns, bends, etc. used for the SS prediction and present in the
DSSP output file format. This information is only used in certain applications, and that is the reason for the
more general `SecStrucInfo` class being used by default.

In order to access the SS information of a `Structure`, the `SecStrucInfo` object needs to be obtained from the
`Group` properties. Below you find an example of how to access and print residue by residue the SS information of 
a `Structure`:

```java
    //This structure should have SS assigned (by any of the methods described)
    Structure s;

    for (Chain c : s.getChains()) {
        for (Group g: c.getAtomGroups()){
            if (g.hasAminoAtoms()){ //Only AA store SS
                //Obtain the object that stores the SS
                SecStrucInfo ss = (SecStrucInfo) g.getProperty(Group.SEC_STRUC);
                //Print information: chain+resn+name+SS
                System.out.println(c.getChainID()+" "+
                    g.getResidueNumber()+" "+
                    g.getPDBName()+" -> "+ss);
            }
        }
    }
```

### Output Formats

Once the SS has been assigned (either loaded or predicted), there exist in **BioJava** some formats to visualize it:

- **DSSP format**: the SS can be printed as a DSSP oputput file format, following the standards so that it can be
parsed again. It is the safest way to serialize a SS annotation and recover it later, but it is probably the most 
complicated to visualize.

<pre>
  #  RESIDUE AA STRUCTURE BP1 BP2  ACC     N-H-->O    O-->H-N    N-H-->O    O-->H-N    TCO  KAPPA ALPHA  PHI   PSI    X-CA   Y-CA   Z-CA 
    1    1 A R              0   0  168      0, 0.0    54,-0.1     0, 0.0     5,-0.1   0.000 360.0 360.0 360.0 139.2   32.2   14.7  -11.8
    2    2 A P    >   -     0   0   45      0, 0.0     3,-1.8     0, 0.0     4,-0.3  -0.194 360.0-122.0 -61.4 144.9   34.9   13.6   -9.4
    3    3 A D  G >  S+     0   0  122      1,-0.3     3,-1.6     2,-0.2     4,-0.2   0.790 108.3  71.4 -62.8 -28.5   35.8   10.0   -9.5
    4    4 A F  G >  S+     0   0   26      1,-0.3     3,-1.7     2,-0.2    -1,-0.3   0.725  83.7  70.4 -64.1 -23.3   35.0    9.7   -5.9
</pre>

- **FASTA format**: simple format that prints the SS type of each residue sequentially in the order of the aminoacids.
It is the easiest to visualize, but the less informative of all.

<pre>
>5PTI_SS-annotation
  GGGGS     S    EEEEEEETTTTEEEEEEE SSS  SS BSSHHHHHHHH   
</pre>

- **Helix Summary**: similar to the FASTA format, but contain also information about the helical turns.

<pre>
3 turn:  >>><<<                                                   
4 turn:                        >444<                  >>>>XX<<<<  
5 turn:                        >5555<                             
SS:       GGGGS     S    EEEEEEETTTTEEEEEEE SSS  SS BSSHHHHHHHH   
AA:     RPDFCLEPPYTGPCKARIIRYFYNAKAGLCQTFVYGGCRAKRNNFKSAEDCMRTCGGA
</pre>

- **Secondary Structure Elements**: another way to visualize the SS annotation is by compacting those sequential residues that share the same SS type and assigning an ID to the range. In this way, a structure can be described by
a collection of helices, strands, turns, etc. and each one of the elements can be identified by an ID (i.e. helix 1 (H1), beta-strand 6 (E6), etc).

<pre>
G1: 3 - 6
S1: 7 - 7
S2: 13 - 13
E1: 18 - 24
T1: 25 - 28
E2: 29 - 35
S3: 37 - 39
S4: 42 - 43
B1: 45 - 45
S5: 46 - 47
H1: 48 - 55
</pre>

You can find examples of how to get the different file formats in the class `DemoSecStrucPred` in the **demo**
package.

<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 3: The Structure Modules](README.md)
| Chapter 15 : Protein Secondary Structure

Prev: [Chapter 14 : Protein Symmetry](symmetry.md)

Next: [Chapter 17 : Special Cases](special.md)
