Structure Alignment in BioJava
===

## Data Structures

### AFPChain Data Model (legacy)

The `AFPChain` data structure was designed to store pairwise structural
alignments. The class functions as a bean, and contains many variables 
used internally by the alignment algorithms implemented in biojava.

The residue equivalencies of the alignment are described in the optimal 
alignment variable, a triple array of integers, where the indices stand for:

```java
  int[][][] optAln = new int[block][chain][eqr];
```

* **block**: the blocks divide the alignment into different parts. The division
can be due to non-topological rearrangements (e.g. circular permutations) or
due to flexible parts (e.g. domain switch). There can be any number of blocks
in a structural alignment, defined by the structure alignment algorithm.

* **chain**: in a pairwise alignment there are only two chains, or structures.

* **eqr**: EQR stands for equivalent residue position, i.e. the alignment position.
There are as many positions (EQRs) in a block as the length of the alignment block,
and their number is equal for any of the two chains in the same block.

In each entry (combination of the three indices described above) an integer is
stored, which corresponds to the residue index in the specified chain, i.e. the
Atom index in the chain atom array. In between the same block, the stored integers 
(residues) are always in increasing order.

As an overview, the AFPChain data model:

* Only supports **pairwise alignments**, i.e. two chains or structures aligned.
* Can support **flexible alignments** and **non-topological alignments**. 
However, their combinatation (a flexible alignment with topological rearrangements) 
can not be represented, because the blocks mean either one or the other. 
* Can not support **non-sequential alignments**, or they would require a new block for 
each EQR, because sequentiality of the residues is assumed inside each block.

### MultipleAlignment Data Model

This data structure introduces a more explicit model for storing structure
alignments. It is a general model that supports any of the following properties, 
or their combination:

* Multiple structures: the model is no longer restricted to pairwise alignments.
* Non-topological alignments: such as circular permutations or domain rearrangements.
* Flexible alignments: 

A ***block*** is a series of aligned residues within a structure. A block must
be a sequential alignment; the order of residues within the block should be
strictly increasing. Blocks in the same alignment should be non-overlapping.
Only aligned positions are specified in the block, but individual structures may
have gaps and deletions at any position. A block corresponds most closely to a
traditional, sequential multiple alignment with a row for each structure and a
column for each aligned position.

A ***match*** represents a set of blocks with a single global superposition.
This superposition is stored in a ***pose***, which contains the affine
transform required for the superposition.

Finally, a `MultipleStructureAlignment` associates a set of Structures with one
or more matches.

### Examples

A typical pairwise alignment would be a single match, a single pose, and a
single block of two structures.

