The Protein-Disorder Module of BioJava
=====================================================

A tutorial for the protein-disorder module of [BioJava](http://www.biojava.org)

## About
<table>
    <tr>
        <td>

        </td>
        <td>
            The <i>protein-disorder module</i> of BioJava provide an API that allows to
            <ul>
                <li>predict protein-disorder using the JRONN algorithm</li>
            </ul>


        </td>
    </tr>
</table>   

## How can I predict disordered regions on a protein sequence?
-----------------------------------------------------------

BioJava provide a module *biojava-protein-disorder* for prediction
disordered regions from a protein sequence. Biojava-protein-disorder
module for now contains one method for the prediction of disordered
regions. This method is based on the Java implementation of
[RONN](http://www.strubi.ox.ac.uk/RONN) predictor.

This code has been originally developed for use with
[JABAWS](http://www.compbio.dundee.ac.uk/jabaws). We call this code
*JRONN*. *JRONN* is based on the C implementation of RONN algorithm and
uses the same model data, therefore gives the same predictions. JRONN
based on RONN version 3.1 which is still current in time of writing
(August 2011). Main motivation behind JRONN development was providing an
implementation of RONN more suitable to use by the automated analysis
pipelines and web services. Robert Esnouf has kindly allowed us to
explore the RONN code and share the results with the community.

Original version of RONN is described in [Yang,Z.R., Thomson,R.,
McMeil,P. and Esnouf,R.M. (2005) RONN: the bio-basis function neural
network technique applied to the detection of natively disordered
regions in proteins. Bioinformatics 21:
3369-3376](http://bioinformatics.oxfordjournals.org/content/21/16/3369.full)

Examples of use are provided below. For more information please refer to
JronnExample testcases.

Finally instead of an API calls you can use a [ command line
utility](http://biojava.org/wikis/BioJava:CookBook3:ProteinDisorderCLI/ "wikilink"), which is
likely to give you a better performance as it uses multiple threads to
perform calculations.

Example 1: Calculate the probability of disorder for every residue in the sequence
----------------------------------------------------------------------------------

```java
FastaSequence fsequence = new FastaSequence("name",
  "LLRGRHLMNGTMIMRPWNFLNDHHFPKFFPHLIEQQAIWLADWWRKKHC" +
  "RPLPTRAPTMDQWDHFALIQKHWTANLWFLTFPFNDKWGWIWFLKDWTPGSADQAQRACTWFFCHGHDTN");

float[] rawProbabilityScores = Jronn.getDisorderScores(fsequence);
```

Example 2: Calculate the probability of disorder for every residue in the sequence for all proteins from the FASTA input file
-----------------------------------------------------------------------------------------------------------------------------

```java
final List<FastaSequence> sequences = SequenceUtil.readFasta(new FileInputStream("src/test/resources/fasta.in"));
Map<FastaSequence, float[]> rawProbabilityScores = Jronn.getDisorderScores(sequences); 
```

Example 3: Get the disordered regions of the protein for a single protein sequence
----------------------------------------------------------------------------------

```java
FastaSequence fsequence = new FastaSequence("Prot1", "LLRGRHLMNGTMIMRPWNFLNDHHFPKFFPHLIEQQAIWLADWWRKKHC" +
               "RPLPTRAPTMDQWDHFALIQKHWTANLWFLTFPFNDKWGWIWFLKDWTPGSADQAQRACTWFFCHGHDTN" +
               "CQIIFEGRNAPERADPMWTGGLNKHIIARGHFFQSNKFHFLERKFCEMAEIERPNFTCRTLDCQKFPWDDP");

Range[] ranges = Jronn.getDisorder(fsequence);
```

Example 4: Calculate the disordered regions for the proteins from FASTA file
----------------------------------------------------------------------------

```java
final List<FastaSequence> sequences = SequenceUtil.readFasta(new FileInputStream("src/test/resources/fasta.in"));
Map<FastaSequence, Range[]> ranges = Jronn.getDisorder(sequences);

```

## Please cite

**BioJava: an open-source framework for bioinformatics in 2012**<br/>
*Andreas Prlic; Andrew Yates; Spencer E. Bliven; Peter W. Rose; Julius Jacobsen; Peter V. Troshin; Mark Chapman; Jianjiong Gao; Chuan Hock Koh; Sylvain Foisy; Richard Holland; Gediminas Rimsa; Michael L. Heuer; H. Brandstatter-Muller; Philip E. Bourne; Scooter Willis* <br/>
[Bioinformatics (2012) 28 (20): 2693-2695.](http://bioinformatics.oxfordjournals.org/content/28/20/2693.abstract) <br/>
[![doi](http://img.shields.io/badge/doi-10.1093%2Fbioinformatics%2Fbts494-blue.svg?style=flat)](http://bioinformatics.oxfordjournals.org/content/28/20/2693.abstract) [![pubmed](http://img.shields.io/badge/pubmed-22877863-blue.svg?style=flat)](http://www.ncbi.nlm.nih.gov/pubmed/22877863)

## License

The content of this tutorial is available under the [CC-BY](http://creativecommons.org/licenses/by/3.0/) license.

[view license](../license.md)



<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| Book 3: The Protein Structure modules

Prev: [Book 4: The Genomics Module](../genomics/README.md)
| Next: [Book 6: The ModFinder Module](../modfinder/README.md)
