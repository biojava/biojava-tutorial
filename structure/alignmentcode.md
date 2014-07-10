Structure Alignment in BioJava
===

## Data Structures

### Legacy AFPChain model

Pairwise structure alignments are currently stored in the `AFPChain` class. The
class functions as a bean, and contains many variables used internally by
various alignment algorithms.

### Proposed MultipleStructureAlignment data model

This data structure introduces a more explicit model for storing structure
alignments. It is more flexible than the AFPChain model, adding support for

* Multiple alignments
* Non-topological alignments, such as circular permutations
* Mutable, while maintaining internal consistency

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

