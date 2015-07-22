SEQRES and ATOM Records, Mapping to Uniprot (SIFTs)
===================================================

How molecular sequences are linked to experimentally observed atoms.

## Sequences and Atoms

In many experiments not all atoms that are part of the molecule under study can be observed. As such the ATOM records in PDB oftein contain missing atoms or only the part of a molecule that could be experimentally determined. In case of multi-domain proteins the PDB often contains only one of the domains (and in some cases even shorter fragments).

Let's take a look at an example. The [Protein Feature View](https://github.com/andreasprlic/proteinfeatureview) provides a graphical summary of how the regions that have been observed in an experiment and are available in the PDB map to UniProt.

![Screenshot of Protein Feature View at RCSB]
(https://raw.github.com/andreasprlic/proteinfeatureview/master/images/P06213.png "Insulin receptor - P06213 (INSR_HUMAN)")

As you can see, there are three PDB entries (PDB IDs [3LOH](http://www.rcsb.org/pdb/explore.do?structureId=3LOH), [2HR7](http://www.rcsb.org/pdb/explore.do?structureId=2RH7), [3BU3](http://www.rcsb.org/pdb/explore.do?structureId=3BU3)) that cover different regions of the UniProt sequence for the insulin receptor.

The blue-boxes are regions for which atoms records are available. For the grey regions there is sequence information available in the PDB, but no coordinates.

## Seqres and Atom Records

The sequence that has been used in the experiment is stored in the **Seqres** records in the PDB. It is often not the same sequences as can be found in Uniprot, since it can contain cloning-artefacts and modifications that were necessary in order to crystallize a structure.

The **Atom** records provide coordinates where it was possible to observe them.

<pre>
    Seqres groups -> sequence that has been used in the experiment
    Atom groups   -> subset of Seqres groups for which coordinates could be obtained
</pre>    

The *mmCIF/PDBx* file format contains the information how the Seqres and atom records are mapped onto each other. However the *PDB format* does not clearly specify how to resolve this mapping. BioJava contains a utility class that maps the Seqres to the Atom records when parsing PDB files. This class performs an alignment using dynamic programming, which can slow down the parsing process. If you do not require the precise Seqres to Atom mapping, you can turn it off like this:

```java
    AtomCache cache = new AtomCache();
            
    FileParsingParameters params = cache.getFileParsingParams();
            
    params.setAlignSeqRes(false);
            
    Structure structure = StructureIO.getStructure(...);
            
```

## Accessing Seqres and Atom Groups

By default BioJava loads both the Seqres and Atom groups into the [Chain](http://www.biojava.org/docs/api/org/biojava/nbio/structure/Chain.html) 
objects.

<pre>
    Chain   -> Seqres groups
            -> Atom groups
</pre>

Groups that are part of the Seqres sequence as well as of the Atom records are mapped onto each other. This means you
can iterate over all Seqres groups in a chain and check, if they have observed atoms.

## Mapping from Uniprot to Atom Records 

The mapping between PDB and UniProt changes over time, due to the dynamic nature of biological data. The [PDBe](http://www.pdbe.org) has a project that provides up-to-date mappings between the two databases, the [SIFTs](http://www.ebi.ac.uk/pdbe/docs/sifts/) project. 

BioJava contains a parser for the SIFTs XML files. The [SiftsMappingProvider](http://www.biojava.org/docs/api/org/biojava/nbio/structure/io/sifts/SiftsMappingProvider.html) also acts similar to the AtomCache class, that we [discussed earlier](caching.md) and can automatically download and locally install SIFTs files.

Here, how to request the mapping for one particular PDB ID.

```java
    List<SiftsEntity> entities = SiftsMappingProvider.getSiftsMapping("1gc1");
            
    for (SiftsEntity e : entities){
        System.out.println(e.getEntityId() + " " +e.getType());
        
        for ( SiftsSegment seg: e.getSegments()) {
            System.out.println(" Segment: " + seg.getSegId() + " " + seg.getStart() + " " + seg.getEnd()) ;
            
            for ( SiftsResidue res: seg.getResidues() ) {
                System.out.println("  " + res);
            }
        }
        
    }
```

This gives the following output:

<pre>
    C protein
 Segment: 1gc1_C_1_181 1 181
  SiftsResidue [pdbResNum=1, pdbResName=LYS, chainId=C, uniProtResName=K, uniProtPos=26, naturalPos=1, seqResName=LYS, pdbId=1gc1, uniProtAccessionId=P01730, notObserved=false]
  SiftsResidue [pdbResNum=2, pdbResName=LYS, chainId=C, uniProtResName=K, uniProtPos=27, naturalPos=2, seqResName=LYS, pdbId=1gc1, uniProtAccessionId=P01730, notObserved=false]
  SiftsResidue [pdbResNum=3, pdbResName=VAL, chainId=C, uniProtResName=V, uniProtPos=28, naturalPos=3, seqResName=VAL, pdbId=1gc1, uniProtAccessionId=P01730, notObserved=false]
  SiftsResidue [pdbResNum=4, pdbResName=VAL, chainId=C, uniProtResName=V, uniProtPos=29, naturalPos=4, seqResName=VAL, pdbId=1gc1, uniProtAccessionId=P01730, notObserved=false]
  SiftsResidue [pdbResNum=5, pdbResName=LEU, chainId=C, uniProtResName=L, uniProtPos=30, naturalPos=5, seqResName=LEU, pdbId=1gc1, uniProtAccessionId=P01730, notObserved=false]
  SiftsResidue [pdbResNum=6, pdbResName=GLY, chainId=C, uniProtResName=G, uniProtPos=31, naturalPos=6, seqResName=GLY, pdbId=1gc1, uniProtAccessionId=P01730, notObserved=false]
  SiftsResidue [pdbResNum=7, pdbResName=LYS, chainId=C, uniProtResName=K, uniProtPos=32, naturalPos=7, seqResName=LYS, pdbId=1gc1, uniProtAccessionId=P01730, notObserved=false]
  ...
 </pre>   

 As you can see for each residue in the Uniprot / PDB sequence the matching counterpart is provided (if there is one).



<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 3: The Structure modules](README.md)
| Chapter 7 : SEQRES and ATOM records

Prev: [Chapter 6 : work with mmCIF/PDBx files](mmcif.md)

Next: [Chapter 8 : Structure Alignments](alignment.md)
