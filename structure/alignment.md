Protein Structure Alignment
===========================

## What is a structure alignment?

A **Structural alignment** attempts to establish equivalences between two or more polymer structures based on their shape and three-dimensional conformation. In contrast to simple structural superposition (see below), where at least some equivalent residues of the two structures are known, structural alignment requires no a priori knowledge of equivalent positions. 

Structural alignment is a valuable tool for the comparison of proteins with low sequence similarity, where evolutionary relationships between proteins cannot be easily detected by standard sequence alignment techniques. Structural alignment can therefore be used to imply evolutionary relationships between proteins that share very little common sequence. However, caution should be exercised when using the results as evidence for shared evolutionary ancestry, because of the possible confounding effects of convergent evolution by which multiple unrelated amino acid sequences converge on a common tertiary structure.

For more info see the Wikipedia article on [protein structure alignment](http://en.wikipedia.org/wiki/Structural_alignment).

## Alignment Algorithms supported by BioJava

BioJava comes with implementations of the Combinatorial Extension (CE) and FATCAT algorithms. Both algorithms come in two variations, as such one can say that BioJava supports the following four algorithms.

1. Combinatorial Extension (CE)
2. Combinatorial Extension with Circular Permutation (CE-CP)
3. FATCAT - rigid
4. FATCAT - flexible.

## Alignment User Interface

Before going the details how to use the algorithms programmatically, let's take a look at the user interface that cames with the *biojava-structure-gui* module.

<pre>
        AlignmentGui.getInstance();
</pre>    

shows the following user interface. 

![Alignment GUI](img/alignment_gui.png)

You can manually select protein chains, domains, or custom files to be aligned. Try to align 2hyn vs. 1zll. This will show the results in a graphical way, in 3D:

![3D Alignment of PDB IDs 2hyn and 1zll](img/2hyn_1zll.png)

and also a 2D display, that interacts with the 3D display

![2D Alignment of PDB IDs 2hyn and 1zll](img/alignmentpanel.png)

The functionality to perform and visualize these alignments can of course be used also from your own code. Let's first have a look at the alignment algorithms:

## The Alignment Algorithms

### Combinatorial Extension (CE)

The Combinatorial Extension (CE) algorithm was originally developed by [Shindyalov and Bourne in 1998](http://peds.oxfordjournals.org/content/11/9/739.short). 

### Combinatorial Extension with Circular Permutation (CE-CP)

This is a new variation of CE that can detect circular permutations in proteins.

### FATCAT - rigid

This is a Java implementation of the original FATCAT algorithm. [Yuzhen Ye &amp; Adam Godzik in 2003] (http://bioinformatics.oxfordjournals.org/content/19/suppl_2/ii246.abstract)

### FATCAT - flexible

Just as FATCAT - rigid, a Java implementation of the original FATCAT algorithm.

## Acknowledgements

Thanks to P. Bourne, Yuzhen Ye and A. Godzik for granting permission to freely use and redistribute their algorithms.