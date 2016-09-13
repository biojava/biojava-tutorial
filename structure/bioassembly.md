Asymmetric Unit and Biological Assembly
=======================================

For many proteins, the asymmetric unit and the biological assembly are the same. However there are quite a few proteins where they are not identical and depending on what you are interested in, it might be important that you work with the biological assembly, instead of the asymmetric unit.

## Asymmetric Unit

The asymmetric unit is the smallest portion of a crystal structure to which symmetry operations can be applied in order to generate the complete unit cell (the crystal repeating unit). 

A crystal asymmetric unit may contain:

* one biological assembly
* a portion of a biological assembly
* multiple biological assemblies

## Biological Assembly

The biological assembly (also sometimes referred to as the biological unit) is the macromolecular assembly that has either been shown to be or is believed to be the functional form of the molecule For example, the functional form of hemoglobin has four chains.

The [StructureIO](http://www.biojava.org/docs/api/org/biojava/nbio/structure/StructureIO.html) and [AtomCache](http://www.biojava.org/docs/api/org/biojava/nbio/structure/align/util/AtomCache.html) classes in Biojava provide access methods to work with either asymmetric unit or biological assembly.

Let's load both representations of hemoglobin PDB ID [1HHO](http://www.rcsb.org/pdb/explore.do?structureId=1hho) and visualize it:

```java
    public static void main(String[] args){

        try {
            Structure asymUnit = StructureIO.getStructure("1hho");

            showStructure(asymUnit);
            
            Structure bioAssembly = StructureIO.getBiologicalAssembly("1hho");
            
            showStructure(bioAssembly);
            
        } catch (Exception e){
            e.printStackTrace();
        }

    }

    public static void showStructure(Structure structure){

        StructureAlignmentJmol jmolPanel = new StructureAlignmentJmol();

        jmolPanel.setStructure(structure);

        // send some commands to Jmol
        jmolPanel.evalString("select * ; color chain;");            
        jmolPanel.evalString("select *; spacefill off; wireframe off; cartoon on;  ");
        jmolPanel.evalString("select ligands; cartoon off; wireframe 0.3; spacefill 0.5; color cpk;");

    }
```

<table>
    <tr>
        <td>
            The <b>asymmetric unit</b> of hemoglobin PDB ID <a href="http://www.rcsb.org/pdb/explore.do?structureId=1hho">1HHO</a>
        </td>
        <td>
            The <b>biological assembly</b> of hemoglobin PDB ID <a href="http://www.rcsb.org/pdb/explore.do?structureId=1hho">1HHO</a>
        </td>
    </tr>
    <tr>
        <td>
            <img src="img/1hho_asym.png"/>
        </td>
        <td>
            <img src="img/1hho_biounit.png"/>
        </td>
    </tr>
</table>

As we can see, the two representations are quite different! When investigating protein interfaces, ligand binding and for many other applications, you always want to work with the biological assemblies.

Here another example, the bacteriophave GA protein capsid PDB ID [1GAV](http://www.rcsb.org/pdb/explore.do?structureId=1gav)

<table>
    <tr>
        <td>
            The <b>asymmetric unit</b> of bacteriophave GA protein capsid PDB ID  <a href="http://www.rcsb.org/pdb/explore.do?structureId=1gav">1GAV</a>
        </td>
        <td>
            The <b>biological assembly</b> of bacteriophave GA protein capsid PDB ID  <a href="http://www.rcsb.org/pdb/explore.do?structureId=1gav">1GAV</a>
        </td>
    </tr>
    <tr>
        <td>
            <img src="img/1gav_asym.png"/>
        </td>
        <td>
            <img src="img/1gav_biounit.png"/>
        </td>
    </tr>
</table>

## Re-creating Biological Assemblies

Since biological assemblies can be accessed via the StructureIO interface, in principle there is no need to access the lower-level code in BioJava that allows to re-create biological assemblies. If you are interested in looking at the gory details of this, here a couple of pointers into the code. In principle there are two ways for how to get to a biological assembly:

1. The biological assembly needs to be re-built and the atom coordinates of the asymmetric unit need to be rotated according to the instructions in the files. The information required to re-create the biological assemblies is available in both the PDB an mmCIF/PDBx files. In PDB files the relevant transformations are stored in the *REMARK 350* records. For mmCIF/PDBx, the *_pdbx_struct_assembly* and *_pdbx_struct_oper_list* categories store the corresponding rules.

2. There is also a pre-computed file available from the PDB that contains an assembled version of a structure. This file can be parsed directly, without having to perform rotation operations on coordinates.

As of version 5.0 BioJava contains utility classes to re-create biological assemblies for both PDB and mmCIF files.

Take a look at the method `getBiologicalAssembly()` in [StructureIO](http://www.biojava.org/docs/api/org/biojava/nbio/structure/StructureIO.html)  to see how the underlying *BiologicalAssemblyBuilder* is called.

## Memory consumption

This example in the next section loads the structure of the PBCV-1 virus capsid (PDB ID [1M4X](http://www.rcsb.org/pdb/explore.do?structureId=1m4x)). It consists of 16 million atoms and has one of the largest, if not the largest biological assembly that is currently available in the PDB. Needless to say it is important to change the maximum heap size parameter, otherwise you will not be able to load it. It requires a minimum of 9GB RAM to load (measured on Java 1.7 on OSX). You can change the heap size by providing the following startup parameter (and assuming you have 10G or more of RAM available on your system)
<pre>
    -Xmx10G 
</pre>

Note: when loading this structure with 9GB of memory, the Java VM spends a significant amount of time in garbage collection (GC). If you provide more RAM than the minimum requirement, then GC is triggered less often and the biological assembly loads faster.

<table>
    <tr>
        <td>
          <img src="img/1m4x_bio_r_250.jpg"/>
        </td>       
    </tr>
    <tr>
        <td>
            The biological assembly of the PBCV-1 virus capsid. (image source: <a href="http://www.rcsb.org/pdb/explore.do?structureId=1m4x">RCSB</a>)
        </td>
    </tr>
</table>

## Representing symmetry related chains
Chains are identified by chain identifiers which serve to distinguish the different molecular entities present in the asymmetric unit. Once a biological assembly is built it can be composed of chains from both the asymmetric unit or from chains resulting in applying a symmetry operator (this chains are also called "symmetry mates"). The problem with that is that the symmetry mates will get the same chain identifiers as the untransformed chains. 

In order to solve that issue there are 2 solutions:

1. Assign new chain identifiers. In BioJava the new chain identifiers assigned are of the form `<original chain id>_<symmetry operator id>`.
2. Place the symmetry partners into different models. This is the solution taken by the pre-computed biounit files available from the PDB. 

Since version 5.0 BioJava uses approach 1) to store the biounit in a single `Structure` object. Because the chain identifiers are then of more than 1 character, the Structure can only be written out in mmCIF format (PDB format is limited to 1 character chain identifiers).

In BioJava one can still produce a biounit using approach 2) by passing a boolean parameter to the `getBiologicalAssembly` method:
```java
Structure struct = StructureIO.getBiologicalAssembly(pdbId, true);
```
## PDB entries with more than 1 biological assemblies
Many PDB entries are assigned more than 1 biological assemblies. This is due to many factors: sometimes the authors disagree with the annotators, sometimes the authors are not sure about which biological assembly is the right one, sometimes there are several equivalent biological assemblies present in the asymmetric unit (but with slightly different  conformations) and each of those is annotated as a different biological assembly.

To get all biological assemblies for a given PDB entry one needs to use:
```java
List<Structure> bioAssemblies = StructureIO.getBiologicalAssemblies(pdbId);
```

## Further Reading

The RCSB PDB web site has a great [tutorial on Biological Assemblies](http://www.rcsb.org/pdb/101/static101.do?p=education_discussion/Looking-at-Structures/bioassembly_tutorial.html).

<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 3: The Structure Modules](README.md)
| Chapter 9 : Biological Assemblies

Prev: [Chapter 8 : Structure Alignments](alignment.md)

Next: [Chapter 10 : External Databases](externaldb.md)
