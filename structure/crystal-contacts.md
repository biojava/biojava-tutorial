# How to calculate all crystal contacts in a PDB structure

## Why crystal contacts?

A protein structure is determined by X-ray diffraction by producing a crystal - an infinite lattice of molecules - of the protein. Thus the end result of the diffraction experiment is a crystal lattice and not just a single molecule. However the PDB file only contains the coordinates of the Asymmetric Unit, defined as the minimum unit needed to reconstruct the full crystal using symmetry operators. 

[here](http://www.wwpdb.org/news/news_2013.html#22-May-2013)



## Getting the set of unique contacts in the crystal lattice

This code snippet will produce a list of all non-redundant interfaces present in the crystal lattice of PDB entry [1SMT](http://www.rcsb.org/pdb/explore.do?structureId=1SMT):

```java
		AtomCache cache = new AtomCache();
		
		StructureIO.setAtomCache(cache); 
		
		Structure structure = StructureIO.getStructure("1SMT");
			
		CrystalBuilder cb = new CrystalBuilder(structure);
		
		StructureInterfaceList interfaces = cb.getUniqueInterfaces(6);

		interfaces.calcAsas(3000, 1, -1);

		// now interfaces are sorted by areas, we can get the largest interface in the crystal and look at its area
		interfaces.get(1).getTotalArea();

```

An interface is defined here as any 2 chains with at least a pair of atoms within the given distance cutoff (6 A in the example above)



