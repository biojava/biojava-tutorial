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

The StructureIO and AtomCache classes in Biojava provide access methods to work with either asymmetric unit or biological assembly.

Let's load both representations of hemoglobin PDB ID [1HHO](http://www.rcsb.org/pdb/explore.do?structureId=1hho) and visualize it:

<pre>
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
</pre>


<table>
    <tr>
        <td>
            The asymmetric unit of hemoglobin PDB ID <a href="http://www.rcsb.org/pdb/explore.do?structureId=1hho">1HHO</a>
        </td>
        <td>
            The biological assembly of hemoglobin PDB ID <a href="http://www.rcsb.org/pdb/explore.do?structureId=1hho">1HHO</a>
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

As we can see, the two representations are quite different! When investigating protein interfaces, ligand binding and for many other applications, you always want to work with the biological assemblies!

## Further Reading

The RCSB PDB web site has a great [tutorial on Biological Assemblies](http://www.rcsb.org/pdb/101/static101.do?p=education_discussion/Looking-at-Structures/bioassembly_tutorial.html)
