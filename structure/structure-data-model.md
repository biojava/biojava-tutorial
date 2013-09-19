# The BioJava-structure data model

A biologically and chemically meaningful data representation of PDB/mmCIF.

## The basics   

BioJava at its core is a collection of file parsers and (in some cases) data models to represent frequently used biological data.  The protein-structure modules represent macromolecular data in a way that should make it easy to work with. The representation is essentially independ of the underlying file format and the user can chose to work with either PDB or mmCIF files and still get an almost identical data representation. (There can be subtile differences between PDB and mmCIF data, for example the atom indices in a few entries are not 100% identical)

## The main hierarchy

BioJava provides a flexible data structure for managing protein structural data. The 
[http://www.biojava.org/docs/api/org/biojava/bio/structure/Structure.html Structure] class is the main container. 

A Structure has a hierarchy of sub-objects:

<pre>
Structure
   |
   Model(s)
        |
        Chain(s)
            |
             Group(s) -> Chemical Component Definition
                 |
                 Atom(s)
</pre>

All structure objects contain one or more "models". That means also X-ray structures contain a "virtual" model which serves as a container for the chains. The most common way to access chains will be via

<pre>
        List < Chain > chains = structure.getChains();
</pre>

This works for both NMR and X-ray based structures and by default the first model is getting accessed.


## Working with atoms

Different ways are provided how to access the data contained in a [Structure](http://www.biojava.org/docs/api/org/biojava/bio/structure/Structure.html).
If you want to directly access an array of [Atoms](http://www.biojava.org/docs/api/org/biojava/bio/structure/Atom.html) you can use the utility class called [StructureTools](http://www.biojava.org/docs/api/org/biojava/bio/structure/StructureTools.html)

<pre>

    // get all C-alpha atoms in the structure
    Atom[] caAtoms = StructureTools.getAtomCAArray(structure);
</pre>

Alternatively you can access atoms also by their parent-group.

## Loop over all the data

//TODO

## Working with groups

The [Group](http://www.biojava.org/docs/api/org/biojava/bio/structure/Group.html) interface defines all methods common to a group of atoms. There are 3 types of Groups:

* [AminoAcid](http://www.biojava.org/docs/api/org/biojava/bio/structure/AminoAcid.html)
* [Nucleotide](http://www.biojava.org/docs/api/org/biojava/bio/structure/NucleotideImpl.html) 
* [Hetatom](http://www.biojava.org/docs/api/org/biojava/bio/structure/HetatomImpl.html) 

In order to get all amino acids that have been observed in a PDB chain, you can use the following utility method:

<pre>
            Chain chain = s.getChainByPDB("A");
            List<Group> groups = chain.getAtomGroups("amino");
            for (Group group : groups) {
                AminoAcid aa = (AminoAcid) group;

                // do something amino acid specific, e.g. print the secondary structure assignment
                System.out.println(aa + " " + aa.getSecStruc());
            }
</pre>


In a similar way you can access all nucleotide groups by
<pre>
            chain.getAtomGroups("nucleotide");
</pre>

The Hetatom groups are access in a similar fashion:
<pre>
            chain.getAtomGroups("hetatm");
</pre>


Since all 3 types of groups are implementing the Group interface, you can also iterate over all groups and check for the instance type:

<pre>
            List<Group> allgroups = chain.getAtomGroups();
            for (Group group : groups) {
                if ( group instanceof AminoAcid) {
                    AminoAcid aa = (AminoAcid) group;
                    System.out.println(aa.getSecStruc());
                }
            }
</pre>









