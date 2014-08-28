# Finding contacts within a protein chain: contact maps

Contacts are a useful tool to analyse protein structures. It simplifies the 3-Dimensional view of the structures into a 2-Dimensional set of contacts between its atoms or its residues. The representation of the contacts in a matrix is known as the contact map. Many protein structure analysis and prediction efforts are done by using contacts, see for instance 

## Getting the contact map of a protein chain

This code snippet will produce the set of contacts between all C alpha atoms for chain A of PDB entry [1SMT](http://www.rcsb.org/pdb/explore.do?structureId=1SMT):

```java
		AtomCache cache = new AtomCache();
		StructureIO.setAtomCache(cache); 
		
		Structure structure = StructureIO.getStructure("1SMT");
			
		Chain chain = structure.getChainByPDB("A");
		
		// we want contacts between Calpha atoms only			
		String[] atoms = {" CA "};
		// the distance cutoff we use is 8A
		AtomContactSet contacts = StructureTools.getAtomsInContact(chain, atoms, 8.0);

		System.out.println("Total number of CA-CA contacts: "+contacts.size());


```

The algorithm to find the contacts uses geometric hashing without need to calculate a full distance matrix, thus it scales nicely.

## Getting the contacts between two protein chains

One can also find the contacting atoms between two protein chains. For instance the following code finds the contacts between the first 2 chains of PDB entry [1SMT](http://www.rcsb.org/pdb/explore.do?structureId=1SMT):

```java
		AtomCache cache = new AtomCache();
		StructureIO.setAtomCache(cache); 
		
		Structure structure = StructureIO.getStructure("1SMT");
			
		AtomContactSet contacts = StructureTools.getAtomsInContact(structure.getChain(0), structure.getChain(1), 5, false);
		
		System.out.println("Total number of atom contacts: "+contacts.size());
		
		// the list of atom contacts can be reduced to a list of contacts between groups:
		GroupContactSet groupContacts = new GroupContactSet(contacts);
```


See [DemoContacts](https://github.com/biojava/biojava/blob/master/biojava3-structure/src/main/java/demo/DemoContacts.java) for a fully working demo of the example above.


