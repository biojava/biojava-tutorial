# How to find all crystal contacts in a PDB structure

## Why crystal contacts?

A protein structure is determined by X-ray diffraction from a protein crystal, i.e. an infinite lattice of molecules. Thus the end result of the diffraction experiment is a crystal lattice and not just a single molecule. However the PDB file only contains the coordinates of the Asymmetric Unit (AU), defined as the minimum unit needed to reconstruct the full crystal using symmetry operators.

Looking at the AU alone is not enough to understand the crystal structure. For instance the biologically relevant assembly (known as the Biological Unit) can occur through a symmetry operator that can be found looking at the crystal contacts. See for instance [1M4N](http://www.rcsb.org/pdb/explore.do?structureId=1M4N): its biological unit is a dimer that happens through a 2-fold operator and is the largest interface found in the crystal. 

Looking at crystal contacts can also be important in order to assess the quality and reliability of the deposited PDB model: an AU can look perfectly fine but then upon reconstruction of the lattice the molecules can be clashing, which indicates that something is wrong in the model.


## Getting the set of unique contacts in the crystal lattice

This code snippet will produce a list of all non-redundant interfaces present in the crystal lattice of PDB entry [1SMT](http://www.rcsb.org/pdb/explore.do?structureId=1SMT):

```java
		AtomCache cache = new AtomCache();
		
		StructureIO.setAtomCache(cache); 
		
		Structure structure = StructureIO.getStructure("1SMT");
			
		CrystalBuilder cb = new CrystalBuilder(structure);
		
		// 6 is the distance cutoff to consider 2 atoms in contact
		StructureInterfaceList interfaces = cb.getUniqueInterfaces(6);
		
		System.out.println("The crystal contains "+interfaces.size()+" unique interfaces");

		// this calculates the buried surface areas of all interfaces and sorts them by areas
		interfaces.calcAsas(3000, 1, -1);

		// we can get the largest interface in the crystal and look at its area
		interfaces.get(1).getTotalArea();

```

An interface is defined here as any 2 chains with at least a pair of atoms within the given distance cutoff (6 A in the example above). 

The algorithm to find all unique interfaces in the crystal works roughly like this:
+ Reconstructs the full unit cell by applying the matrix operators of the corresponding space group to the Asymmetric Unit.
+ Searches all cells around the original one by applying crystal translations, if any 2 chains in that search is found to contact then the new contact is added to the final list.
+ The search is performend without repeating redundant symmetry operators, making sure that if a contact is found then it is a unique contact.

See [DemoCrystalInterfaces](https://github.com/biojava/biojava/blob/master/biojava3-structure/src/main/java/demo/DemoCrystalInterfaces.java) for a fully working demo of the example above.

## Clustering the interfaces
One can also cluster the interfaces based on their similarity. The similarity is measured through contact overlap: number of common contacts over average number of contact in both chains. The clustering can be done as following:

```java
		List<StructureInterfaceCluster> clusters = interfaces.getClusters();
		for (StructureInterfaceCluster cluster:clusters) {
			System.out.print("Cluster "+cluster.getId()+" members: ");
			for (StructureInterface member:cluster.getMembers()) {
				System.out.print(member.getId()+" ");
			}
			System.out.println();
		}
```

