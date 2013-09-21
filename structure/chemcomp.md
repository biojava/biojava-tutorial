The Chemical Component Dictionary
=================================

The [Chemical Component Dictionary](http://www.wwpdb.org/ccd.html) is an external reference file describing all residue and small molecule components found in PDB entries. This dictionary contains detailed chemical descriptions for standard and modified amino acids/nucleotides, small molecule ligands, and solvent molecules. 

### How does BioJava decide what groups are amino acids?

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


### How to access Chemical Component definitions
By default BioJava ships with a minimal representation of standard amino acids, which is useful when you just want to work with atoms and a basic data representation. However if you want to work with a  correct representation (e.g. distinguish ligands from the polypeptide chain, correctly resolve chemically modified residues), it is good to tell the library to either

1. fetch missing Chemical Component definitions on the fly (small download and parsing delays every time a new chemical compound is found), or
2. Load all definitions at startup (slow startup, but then no further delays later on, requires more memory)

You can enable the first behaviour by doing using the [FileParsingParameters](http://www.biojava.org/docs/api/org/biojava/bio/structure/io/FileParsingParameters.html) class:

```java
            AtomCache cache = new AtomCache();
            
             // by default all files are stored at a temporary location.
            // you can set this either via at startup with -DPDB_DIR=/path/to/files/
            // or hard code it this way:
            cache.setPath("/tmp/");
            
            FileParsingParameters params = new FileParsingParameters();
            
            params.setLoadChemCompInfo(true);
            cache.setFileParsingParams(params);
            
            StructureIO.setAtomCache(cache);
            
            Structure structure = StructureIO.getStructure(...);
```

If you want to enable the second behaviour (slow loading of all chem comps at startup, but no further small delays later on) you can use the same code but change the behaviour by switching the [ChemCompProvider](http://www.biojava.org/docs/api/org/biojava/bio/structure/io/mmcif/ChemCompProvider.html) implementation in the [ChemCompGroupFactory](http://www.biojava.org/docs/api/org/biojava/bio/structure/io/mmcif/ChemCompGroupFactory.html)

```java
     ChemCompGroupFactory.setChemCompProvider(new AllChemCompProvider());
```
