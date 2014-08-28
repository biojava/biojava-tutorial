# How to calculate all crystal contacts in a PDB structure

## Why crystal contacts?

A protein structure is determined by X-ray diffraction by producing a crystal - an infinite lattice of molecules - of the protein. Thus the end result of the diffraction experiment is a crystal lattice and not just a single molecule. However the PDB file only contains the coordinates of the Asymmetric Unit, defined as the minimum unit needed to reconstruct the full crystal using symmetry operators. 


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

An interface is defined here as any 2 chains with at least a pair of atoms within the given distance cutoff (6 A in the example above)

See [DemoCrystalInterfaces](https://github.com/biojava/biojava/blob/master/biojava3-structure/src/main/java/demo/DemoCrystalInterfaces.java) for a fully working demo of the example above.


