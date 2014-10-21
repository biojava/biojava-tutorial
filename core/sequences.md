Sequences in BioJava
=====================

BioJava supports a number of basic biological sequence types: DNA, RNA, and protein sequences.

## Create a basic sequence object

Create a DNA sequence

```java    
    DNASequence seq = new DNASequence("GTAC"); 
```   

In addition to the basic DNA sequence class there are specialized classes that extend DNASequence: 
ChromosomeSequence, GeneSequence, IntronSequence, ExonSequence, TranscriptSequence

Create a RNA sequence

```java    
    RNASequence seq = new RNASequence("GUAC"); 
```   

Create a protein sequence

```java    
    ProteinSequence seq = new ProteinSequence("MSTNPKPQRKTKRNTNRRPQDVKFPGG"); 
```   

## Ambiguity codes

In particular when dealing with nucleotide sequences, sometimes the exact nucleotides are not known. 
BioJava supports standard conventions for dealing with such ambiguity. 
For example to represent the nucleotides "A or T" often "W" is getting used.
The expected set of compounds in a sequence by default is strict, however it takes only one line of code to switch to supporting
ambiguity codes.


```java            
        // this throws an error
        DNASequence dna2 = new DNASequence("WWW");

        // however this works:
        AmbiguityDNACompoundSet ambiguityDNACompoundSet = AmbiguityDNACompoundSet.getDNACompoundSet();
        DNASequence dna2 = new DNASequence("WWW",ambiguityDNACompoundSet);
```   


## Protein sequences and ambiguity
The default AminoAcidCompoundSet already supports "Asparagine or Aspartic acid" and related ambiguities. 
It also contains support for Selenocysteine and Pyrrolysine



## More details 

See the Cookbook for [more details on dealing with sequences] (http://biojava.org/wiki/BioJava:CookBook:Core:Overview)