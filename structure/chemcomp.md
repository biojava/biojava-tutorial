The Chemical Component Dictionary
=================================

The [Chemical Component Dictionary](http://www.wwpdb.org/ccd.html) is an external reference file describing all residue and small molecule components found in PDB entries. This dictionary contains detailed chemical descriptions for standard and modified amino acids/nucleotides, small molecule ligands, and solvent molecules.

### How Does BioJava Decide what Groups Are Amino Acids?

BioJava utilizes the Chem. Comp. Dictionary to achieve a chemically correct representation of each group. To make it clear how this can work, let's take a look at how [Selenomethionine](http://en.wikipedia.org/wiki/Selenomethionine) and water is dealt with:

```java
Structure structure = StructureIO.getStructure("1A62");

for (Chain chain : structure.getChains()){
    for (Group group : chain.getAtomGroups()){
        if ( group.getPDBName().equals("MSE") || group.getPDBName().equals("HOH")){
            System.out.println(group.getPDBName() + " is a group of type " + group.getType());
        }
    }
}
```

This will give this output:

<pre>
MSE is a group of type amino
MSE is a group of type amino
MSE is a group of type amino
HOH is a group of type hetatm
HOH is a group of type hetatm
HOH is a group of type hetatm
...
</pre>

As you can see, although MSE is flaged as HETATM in the PDB file, BioJava still represents it correctly as an amino acid. They key is that the [definition file for MSE](http://www.rcsb.org/pdb/files/ligand/MSE.cif) flags it as "L-PEPTIDE LINKING", which is being used by BioJava.

<table>
    <tr><td>

<img src="img/143px-Selenomethionine-from-xtal-3D-balls.png?raw=true" alt="Selenomethionine is a naturally occurring amino acid containing selenium" />


</td>
    <td>

        Selenomethionine is a naturally occurring amino acid containing selenium. It has the ID <a href="http://www.rcsb.org/pdb/files/ligand/MSE.cif">MSE</a> in the Chemical Component Dictionary. (image source: <a href="http://en.wikipedia.org/wiki/File:Selenomethionine-from-xtal-3D-balls.png">wikipedia</a>)


        </td>
    </tr>
</table>


### How to Access Chemical Component Definitions

By default BioJava will retrieve the full chemical component definitions provided by the Protein Data Bank (see http://www.wwpdb.org/data/ccd). That way BioJava makes sure that the user gets a correct representation e.g. distinguish ligands from the polypeptide chain, correctly resolve chemically modified residues, etc.

The behaviour is configurable by setting a property in the `ChemCompGroupFactory` singleton:

1. Use a minimal built-in set of **Chemical Component Definitions**. Will only deal with most frequent cases of chemical components. Does not guarantee a correct representation, but it is fast and does not require network access.
```java
     ChemCompGroupFactory.setChemCompProvider(new ReducedChemCompProvider());
```
2. Load all **Chemical Component Definitions**  at startup (slow startup, but then no further delays later on, requires more memory)
```java
     ChemCompGroupFactory.setChemCompProvider(new AllChemCompProvider());
```
3. Fetch missing **Chemical Component Definitions** on the fly (small download and parsing delays every time a new chemical compound is found). Default behaviour since 4.2.0.
```java
     ChemCompGroupFactory.setChemCompProvider(new DownloadChemCompProvider());
```


<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 3: The Structure Modules](README.md)
| Chapter 5 : Chemical Component Dictionary

Prev: [Chapter 4 : Local Installations](caching.md)

Next: [Chapter 6 : Work with mmCIF/PDBx Files](mmcif.md)
