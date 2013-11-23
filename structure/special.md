# Special Cases When Working with Protein Structures

## Alternate Locations

## Insertion Codes

## Chromophores

A [chromophore](http://en.wikipedia.org/wiki/Chromophore) is the part of a molecule responsible for its color. Several proteins, such as GFP contain a chromopohre that consists of three modified residues. BioJava represents this as a single group in terms of atoms, however as three amino acids when creating the amino acid sequences.

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


