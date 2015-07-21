Structure Alignment Data Model
===

## AFPChain Data Model

The `AFPChain` data structure was designed to store pairwise structural
alignments. The class functions as a bean, and contains many variables 
used internally by the alignment algorithms implemented in biojava.

Some of the important stored variables are:
* Algorithm Name
* Optimal Alignment: described later.
* Optimal RMSD: final and total RMSD value of the alignment.
* TM-score
* BlockRotationMatrix: rotation component of the superposition transformation.
* BlockShiftVector: translation component of the superposition transformation.

### The Optimal Alignment

The residue equivalencies of the alignment (EQRs) are described in the optimal 
alignment variable, a triple array of integers, where the indices stand for:

```java
  int[][][] optAln = afpChain.getOptAln();
  int residue = optAln[block][chain][eqr];
```

* **block**: the blocks divide the alignment into different parts. The 
division can be due to non-topological rearrangements (e.g. circular 
permutations) or due to flexible parts (e.g. domain switch). There can 
be any number of blocks in a structural alignment, defined by the structure 
alignment algorithm.
* **chain**: in a pairwise alignment there are only two chains, or structures.
* **eqr**: EQR stands for equivalent residue position, i.e. the alignment 
position. There are as many positions (EQRs) in a block as the length of 
the alignment block, and their number is equal for any of the two chains in 
the same block.

In each entry (combination of the three indices described above) an integer 
is stored, which corresponds to the residue index in the specified chain, i.e.
the index in the Atom array of the chain. In between the same block, the stored
integers (residues) are always in increasing order.

### Examples

Some examples of how to get the basic properties of an `AFPChain`:

```java
  afpChain.getAlgorithmName();          //Name of the algorithm that generated the alignment
  afpChain.getBlockNum();               //Number of blocks
  afpChain.getTMScore();                //TM-score
  afpChain.getTotalRmsdOpt()            //Optimal RMSD 
  afpChain.getBlockRotationMatrix()[0]  //get the rotation matrix of the first block
  afpChain.getBlockShiftVector()[0]     //get the translation vector of the first block
```

### Overview

As an overview, the `AFPChain` data model:

* Only supports **pairwise alignments**, i.e. two chains or structures aligned.
* Can support **flexible alignments** and **non-topological alignments**. 
However, their combinatation (a flexible alignment with topological rearrangements) 
can not be represented, because the blocks mean either one or the other. 
* Can not support **non-sequential alignments**, or they would require a new block 
for each EQR, because sequentiality of the residues is assumed inside each block.

## MultipleAlignment Data Model

Since BioJava 4.1.0, a new data model is available to store structure alignments.
The `MultipleAlignment` data structure is a general model that supports any of the 
following properties, and any combination:

* **Multiple structures**: the model is no longer restricted to pairwise alignments.
* **Non-topological alignments**: such as circular permutations or domain rearrangements.
* **Flexible alignments**: parts of the alignment with different superposition 
transformation.

In addtition, the data structure is not limited in the number and types of scores
it can store, because the scores are stored in a key:value fashion, as it will be
described later.

### Object Hierarchy

The biggest difference with `AFPChain` is that the `MultipleAlignment` data 
structure is object oriented.
The hierarchy of sub-objects is represented below:

<pre>
MultipleAlignmentEnsemble
   |
   MultipleAlignment(s)
        |
        BlockSet(s)
            |
             Block(s)
</pre>

* **MultipleAlignmentEnsemble**: the ensemble is the top level of the hierarchy.
As a top level, it stores information regarding creation properties (algorithm,
version, creation time, etc.), the structures involved in the alignment (Atoms,
structure identifiers, etc.) and cached variables (atomic distance matrices). 
It contains a collection of `MultipleAlignment` that share the same properties 
stored in the ensemble. This construction allows the storage of alternative 
alignments inside the same data structure.

* **MultipleAlignment**: the `MultipleAlignment` stores the core information of a 
multiple structure alignment. It is designed to be the return type of the multiple
structure alignment algorithms. The object contains a collection of `BlockSet` and 
it is linked to its parent `MultipleAlignmentEnsemble`.

* **BlockSet**: the `BlockSet` stores a flexible part of a multiple structure 
alignment. A flexible part needs the residue equivalencies involved, contained in
a collection of `Block`, and a transformation matrix for every structure that 
describes the 3D superposition of all structures. It is linked to its parent
`MultipleAlignment`.

* **Block**: the `Block` stores the aligned positions (equivalent residues) of a 
`BlockSet` that are in sequentially increasing order. Each `Block` represents a 
sequential part of a non-topological alignment, if more than one `Block` is present.
It is linked to its parent `BlockSet`.

### The Optimal Alignment

In the `MultipleAlignment` data structure the aligned residues are stored in a
double List for every `Block`. The indices of the double List are the following:

```java
  List<List<Integer>> optAln = block.getAlnRes();
  Integer residue = optAln.get(chain).get(eqr);
```

The indices mean the same as in the optimal alignment of the `AFPChain`, just to
remember them:

* **chain**: chain or structure index.
* **eqr**: EQR stands for equivalent residue position, i.e. the alignment 
position. There are as many positions (EQRs) in a block as the length of 
the alignment block, and their number is equal for any of the chains in 
the same block.

As in `AFPChain`, each entry (combination of the two indices described above) 
is an Integer that corresponds to the residue index in the specified chain, i.e.
the index in the Atom array of the chain. Caution has to be taken in the code,
because a `MultipleAlignment` can contain gaps, which are represented as `null`
in the List entries.

### Alignment Scores

All the objects in the hierarchy levels implement the `ScoresCache` interface.
This interface allows the storage of any number of scores as a key:value set.
The key is a `String` that describes the score and used to recover it after,
and the value is a double with the calculated score. The interface has only 
two methods: putScore and getScore.

The following lines of code are an example on how to do score manipulations
on a `MultipleAlignment`:

```java
  //Put a score into the alignment and get it back
  alignment.putScore('myRMSD', 1.234);
  double myRMSD = alignment.getScore('myRMSD');
  
  BlockSet bs = alignment.getBlockSets().get(0);
  //The same can be done for BlockSets
  alignment.putScore('bsRMSD', 1.234);
  double bsRMSD = alignment.getScore('bsRMSD');
```

Methods and names for some frequent scores are located in a util class called
`MultipleAlignmentScorer`.

### Overview

As an overview, the `MultipleAlignment` data model:

* Supports any number of aligned structures, **multiple structures**.
* Can support **flexible alignments** and **non-topological alignments**,
and any of their combinatations (e.g. a flexible alignment with topological 
rearrangements).
* Can not support **non-sequential alignments**, or they would require a new 
`Block` for each EQR, because sequentiality of the residues is a requirement
for each `Block`.
* Can store **any score** in any of the four object hierarchy level, making it
easy to adapt to new requirements and algorithms.

For more examples and information about the `MultipleAlignment` data structure 
go to the Demo package on the biojava-structure module or look through the interface 
files, where the javadoc explanations can be found.

## Conversion between Data Models

The conversion from an `AFPChain` to a `MultipleAlignment` is possible trough the
ensemble constructor. An example on how to do it programatically is below:

```java
  AFPChain afpChain;
  Atom[] chain1;
  Atom[] chain2;
  boolean flexible = false;
  MultipleAlignmentEnsemble ensemble = new MultipleAlignmentEnsemble(afpChain, chain1, chain2, false);
  MultipleAlignment converted = ensemble.getMultipleAlignments().get(0);
```

There is no method to convert from a `MultipleAlignment` to an `AFPChain`, because
the first representation supports any number of structures, while the second is 
only supporting pairwise alignments. However, the conversion can be done with some
lines of code if needed (instantiate a new `AFPChain` and copy one by one the 
properties that can be represented from the `MultipleAlignment`.
