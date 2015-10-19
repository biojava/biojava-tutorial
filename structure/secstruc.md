Protein Secondary Structure
===========================

## What is Protein Secondary Structure?

Protein secondary structure (SS) is the general three-dimensional form of local segments of proteins. 
Secondary structure can be formally defined by the pattern of hydrogen bonds of the protein 
(such as alpha helices and beta sheets) that are observed in an atomic-resolution structure. 

More specifically, the secondary structure is defined by the patterns of hydrogen bonds formed between 
amine hydrogen (-NH) and carbonyl oxygen (C=O) atoms contained in the backbone peptide bonds of the protein. 

![alpha-beta](http://oregonstate.edu/instruction/bi314/summer09/Fig-02-19-0.jpg)

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

## Prediction of SS in BioJava

### Algorithm

The algorithm implemented in BioJava for the prediction of SS is `DSSP`. It is described in the paper from 
[Kabsch W. & Sander C. in 1983](http://onlinelibrary.wiley.com/doi/10.1002/bip.360221211/abstract) 
[![pubmed](http://img.shields.io/badge/in-pubmed-blue.svg?style=flat)](http://www.ncbi.nlm.nih.gov/pubmed/6667333).

### Data Structures



<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 3: The Structure Modules](README.md)
| Chapter 15 : Protein Secondary Structure

Prev: [Chapter 14 : Protein Symmetry](symmetry.md)

Next: [Chapter 17 : Special Cases](special.md)
