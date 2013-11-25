# Special Cases When Working with Protein Structures

## Alternate Locations

Some PDB entries contain alternate conformations for parts of a structure or a group. BioJava merges alternate conformations into a single group, for which alternative groups are available.

```java
			
			Structure s = StructureIO.getStructure("1AAC");

			Chain a = s.getChainByPDB("A");

			Group g = a.getGroupByPDB( ResidueNumber.fromString("27"));

			System.out.println(g);
			for (Atom atom : g.getAtoms()) {
				System.out.print(atom.toPDB());
			}
			
			
			int pos = 0;
			for (Group alt: g.getAltLocs()) {
				pos++;
				System.out.println("altLoc: " + pos + " " + alt);
				for (Atom atom : alt.getAtoms()) {
					System.out.print(atom.toPDB());
				}
			} 
```			

## Insertion Codes

Insertion codes were introduced in the PDB, when people wanted to compare the "same" protein between different species. As it turned out the "same" protein was not showing exactly the same sequence in different species and in some cases insertions were found, resulting in a longer sequences. For the comparison of the proteins the numbering was considered important to be preserved. This was so one could say that for example "HIS 75" is an important residue. To make up for the mismatch in the lengths of the sequences insertion codes were introduced.  As a consequence, in PDB, a particular residue is identified uniquely by three data items: chain identifier, residue number, and insertion code. 

BioJava contains the ResidueNumber object to help with characterizing each group in a file. PDB ID 1IGY contains some extra residues around chain B position 82. BioJava can represent these like this:

```java
			Structure s1 = StructureIO.getStructure("1IGY");
			
			Chain b = s1.getChainByPDB("B");
			
			for (Group g : b.getAtomGroups()){
				System.out.println(g.getResidueNumber() + " " + g.getPDBName() + " " + g.getResidueNumber().getInsCode());
			}
			
```

This will display the following table: (residuenumber, name, insertion code)

```
		...
			81 HIS null
			82 LEU null
			82A SER A
			82B SER B
			82C LEU C
			83 THR null
			84 SER null
		...	
```


## Chromophores

A [chromophore](http://en.wikipedia.org/wiki/Chromophore) is the part of a molecule responsible for its color. Some proteins, such as GFP contain a chromopohre that consists of three modified residues. BioJava represents this as a single group in terms of atoms, however as three amino acids when creating the amino acid sequences.

```java
			
						
			// make sure we download chemical component definitions
			// which is required for correctly representing the chromophore
			FileParsingParameters params = new FileParsingParameters();			
			params.setLoadChemCompInfo(true);						
			
			// now register the parameters in the cache
			AtomCache cache = new AtomCache();			
			cache.setFileParsingParams(params);						
			StructureIO.setAtomCache(cache);
			
			
			// request a GFP protein
			Structure s1 = StructureIO.getStructure("2pxw");
			
			// and print out the internals
			System.out.println(s1.getPDBHeader().toPDB());
						
			// chromophore is at PDB residue number 66
			for ( Chain c : s1.getChains()) {
			
				System.out.println("Chain " + c.getChainID() + 
						" internal " + c.getInternalChainID() +
						" ligands " + c.getAtomLigands().size());
				System.out.println("         10        20        30        40        50        60");
				System.out.println("1234567890123456789012345678901234567890123456789012345678901234567890");
				System.out.println(c.getAtomSequence());
				
				int pos = 0 ;
				for (Group g: c.getAtomGroups()) {
					pos++;					
					System.out.println(pos + " " + g.getResidueNumber() + " " + g.getPDBName() + " " + g.getType()  + " " + g.getChemComp().getOne_letter_code() + " " + g.getChemComp().getType() );									
				}				
			}
```

This will give this output, note 'DYG' at position 63.

```		
           60
		...01234567890
		...AAFDYGNRVFTEY...
```

DYG is an unusual group - it has 3 characters as a result of .getOne_letter_code()

```
	...
		62 65 PHE amino F L-PEPTIDE LINKING
		63 66 DYG amino DYG L-PEPTIDE LINKING
		64 69 ASN amino N L-PEPTIDE LINKING
	...
```

## Microheterogeneity


