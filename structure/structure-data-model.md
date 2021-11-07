# The BioJava-Structure Data Model

A biologically and chemically meaningful data representation of PDB/mmCIF.

## The Basics   

BioJava at its core is a collection of file parsers and (in some cases) data models to represent frequently used biological data. The protein-structure modules represent macromolecular data in a way that should make it easy to work with. The representation is essentially independent of the underlying file format and the user can chose to work with either PDB or mmCIF files and still get an almost identical data representation. (There can be subtile differences between PDB and mmCIF data, for example the atom indices in a few entries are not 100% identical)

## The Main Hierarchy

BioJava provides a flexible data structure for managing protein structural data. The 
[Structure](http://www.biojava.org/docs/api/org/biojava/nbio/structure/Structure.html) class is the main container. 

A `Structure` has a hierarchy of sub-objects:

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

All `Structure` objects contain one or more `Models`. That means also X-ray structures contain a "virtual" model which serves as a container for the chains. This allows to represent multi-model X-ray structures, e.g. from time-series analysis. The most common way to access chains is via:

```java
        List<Chain> chains = structure.getChains();
```

This works for both NMR and X-ray based structures and by default the first `Model` is getting accessed.

## Working with Atoms

Different ways are provided how to access the data contained in a [Structure](http://www.biojava.org/docs/api/org/biojava/nbio/structure/Structure.html).
If you want to directly access an array of representative [Atoms](http://www.biojava.org/docs/api/org/biojava/nbio/structure/Atom.html) (CA for proteins, P in nucleotides),you can use the utility class called [StructureTools](http://www.biojava.org/docs/api/org/biojava/nbio/structure/StructureTools.html)

```java
    // get all representative atoms in the structure, one for residue
    Atom[] caAtoms = StructureTools.getRepresentativeAtomArray(structure);
```

Alternatively you can access atoms also by their parent-group.

## Loop over All the Data

Here an example that loops over the whole data model and prints out the HEM groups of hemoglobin:

```java
			Structure structure = StructureIO.getStructure("4hhb");			

			List<Chain> chains = structure.getChains();

			System.out.println(" # chains: " + chains.size());

			for (Chain c : chains) {
				
				System.out.println("   Chain: " + c.getId() + " # groups with atoms: " + c.getAtomGroups().size());

				for (Group g: c.getAtomGroups()){

					if ( g.getPDBName().equalsIgnoreCase("HEM")) {

						System.out.println("   " + g);

						for (Atom a: g.getAtoms()) {

							System.out.println("    " + a);

						}
					}
				}
			}
```

## Working with Groups

The [Group](http://www.biojava.org/docs/api/org/biojava/nbio/structure/Group.html) interface defines all methods common to a group of atoms. There are 3 types of Groups:

* [AminoAcid](http://www.biojava.org/docs/api4.2.1/org/biojava/nbio/structure/AminoAcid.html)
* [Nucleotide](http://www.biojava.org/docs/api4.2.1/org/biojava/nbio/structure/NucleotideImpl.html) 
* [Hetatom](http://www.biojava.org/docs/api4.2.1/org/biojava/nbio/structure/HetatomImpl.html) 

In order to get all amino acids that have been observed in a PDB chain, you can use the following utility method:

```java
            Chain chain = structure.getPolyChainByPDB("A");
            List<Group> groups = chain.getAtomGroups(GroupType.AMINOACID);
            for (Group group : groups) {
                SecStrucInfo secStrucInfo = (SecStrucInfo) group.getProperty(Group.SEC_STRUC);

                // print the secondary structure assignment
                System.out.println(group + " -- " + secStrucInfo);
            }
```

In a similar way you can access all nucleotide groups by
```java
            chain.getAtomGroups(GroupType.NUCLEOTIDE);
```

The Hetatom groups are access in a similar fashion:
```java
            chain.getAtomGroups(GroupType.HETATM);
```


Since all 3 types of groups are implementing the Group interface, you can also iterate over all groups and check for the instance type:

```java
            List<Group> allgroups = chain.getAtomGroups();
            for (Group group : allgroups) {
                if (group.isAminoAcid()) {
                    SecStrucInfo secStrucInfo = (SecStrucInfo) group.getProperty(Group.SEC_STRUC);
                    System.out.println(group + " -- " + secStrucInfo);
                }
            }
```

## A Note

The detection of the groups works really well in connection with the [Chemical Component Dictionary](checmcomp.md), as we will discuss in the next section. Without this dictionary, there can be inconsistencies in particular with chemically modified residues.

## Entities and Chains

Entities are the distinct chemical components of structures in the PDB. 
Unlike chains, entities do not include duplicate copies and each entity is different from every other 
entity in the structure. There are different types of entities. Polymer entities include Protein, DNA, 
and RNA. Ligands are smaller chemical components that are not part of a polymer entity. 

<pre>
	Structure -> Entity -> Chain
</pre>

To explain this with an example, hemoglobin (e.g. PDB ID 4HHB) has two components, alpha 
and beta. Each of the entities has two copies (= chains) in the structure. IN 4HHB, alpha 
has the two chains with the IDs A, and C and beta the chains B, and D. In total, hemoglobin is 
built up out of four chains.

This prints all the entities in a structure
```java
			Structure structure = StructureIO.getStructure("4hhb");			

			System.out.println(structure);
						
			System.out.println(" # of compounds (entities) " + structure.getEntityInfos().size());

			for ( EntityInfo entity: structure.getEntityInfos()) {
				System.out.println("   " + entity);
			}
```







<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 3: The Structure Modules](README.md)
| Chapter 3 : Structure Data Model

Prev: [Chapter 2 : First Steps](firststeps.md)

Next: [Chapter 4 : Local Installations](caching.md)
