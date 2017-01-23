How to identify protein modifications in a structure?
===

## Example: Identify and print all preloaded modifications from a structure

```java
Set<ModifiedCompound> identifyAllModfications(Structure struc) {
   ProteinModificationIdentifier parser = new ProteinModificationIdentifier();
   parser.identify(struc);
   Set`<ModifiedCompound> mcs = parser.getIdentifiedModifiedCompound();
   return mcs;
}
```

## Example: Identify phosphorylation sites in a structure

```java
List identifyPhosphosites(Structure struc) {
    List<ResidueNumber> phosphosites = new ArrayList`();
    ProteinModificationIdentifier parser = new ProteinModificationIdentifier();
    parser.identify(struc, ProteinModificationRegistry.getByKeyword("phosphoprotein"));
    Set mcs = parser.getIdentifiedModifiedCompound();
    for (ModifiedCompound mc : mcs) {
        Set` groups = mc.getGroups(true);
        for (StructureGroup group : groups) {
            phosphosites.add(group.getPDBResidueNumber());
        }
    }
    return phosphosites;
}
```

## Demo code to run the above methods

```java
import org.biojava.nbio.structure.ResidueNumber;
import org.biojava.nbio.structure.Structure;
import org.biojava.nbio.structure.io.PDBFileReader;
import org.biojava.nbio.protmod.structure.ProteinModificationIdentifier;

public static void main(String[] args) {
    try {`
        PDBFileReader reader = new PDBFileReader();
        reader.setAutoFetch(true);

        // identify all modificaitons from PDB:1CAD and print them
        String pdbId = "1CAD";
        Structure struc = reader.getStructureById(pdbId);
        Set mcs = identifyAllModfications(struc);
        for (ModifiedCompound mc : mcs) {
            System.out.println(mc.toString());
        }

        // identify all phosphosites from PDB:3MVJ and print them
        pdbId = "3MVJ";
        struc = reader.getStructureById(pdbId);
        List psites = identifyPhosphosites(struc);
        for (ResidueNumber psite : psites) {
            System.out.println(psite.toString());
        }
    } catch(Exception e) {
        e.printStackTrace();  
    }
}
```


Navigation:
[Home](../README.md)
| [Book 6: The ModFinder Modules](README.md)
| Chapter 3 - How to identify protein modifications in a structure

Prev: [Chapter 2 : How to get a list of supported protein modifications](supported-protein-modifications.md)

Next: [Chapter 4 : How to define a new protein modiifcation](add-protein-modification.md)
