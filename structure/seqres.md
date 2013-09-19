SEQRES and ATOM records, mapping to Uniprot (SIFTs)
===================================================

How molecular sequences are linked to experimentally observed atoms.

## Sequences and Atoms

In many experiments not all atoms that are part of the molecule udner study can be observed. As such the ATOM records in PDB oftein contain missing atoms or only the part of a molecule that could be experimentally determined. In case of multi-domain proteins the PDB often contains only one of the domains (and in some cases even shorter fragments).

Let's take a look at an example. The [Protein Feature View](https://github.com/andreasprlic/proteinfeatureview) provides a graphical summary of how the regions that have been observed in an experiment and are available in the PDB map to UniProt.

![Screenshot of Protein Feature View at RCSB]
(https://raw.github.com/andreasprlic/proteinfeatureview/master/images/P06213.png "Insulin receptor - P06213 (INSR_HUMAN)")

As you can see, there are three PDB entries (PDB IDs [3LOH](http://www.rcsb.org/pdb/explore.do?structureId=3LOH), [2HR7](http://www.rcsb.org/pdb/explore.do?structureId=2RH7), [3BU3](http://www.rcsb.org/pdb/explore.do?structureId=3BU3)) that cover different regions of the UniProt sequence for the insulin receptor.

The blue-boxes are regions for which atoms records are available. For the grey regions there is sequence information available in the PDB, but no coordinates.

## Seqres and Atom records

The sequence that has been used in the experiment is stored in the **Seqres** records in the PDB. It is often not the same sequences as can be found in Uniprot, since it can contain cloning-artefacts and modifications that were necessary in order to crystallize a structure.

The **Atom** records provide coordinates where it was possible to observe them.

The *mmCIF/PDBx* file format contains the information how the Seqres and atom records are mapped onto each other. However the *PDB format* does not clearly specify how to resolve this mapping. BioJava contains a utility class that maps the Seqres to the Atom records when parsing PDB files. This class performs an alignment using dynamic programming, which can slow down the parsing process. If you do not require the precise Seqres to Atom mapping, you can turn it off like this:

<pre>
    AtomCache cache = new AtomCache();
            
    FileParsingParameters params = cache.getFileParsingParams();
            
    params.setAlignSeqRes(false);
            
    Structure structure = StructureIO.getStructure(...);
            
</pre>



