# Calculating Accessible Surface Areas

BioJava can also do calculation of Accessible Surface Areas (ASA) through an implementation of the rolling ball algorithm of Shrake and Rupley [Shrake 1973].

This code will do the ASA calculation and output the values per residue and the total:
```java
    AtomCache cache = new AtomCache();
		cache.setUseMmCif(true);
		
		StructureIO.setAtomCache(cache); 
		
		Structure structure = StructureIO.getStructure("1smt");
		
		AsaCalculator asaCalc = new AsaCalculator(structure, 
				AsaCalculator.DEFAULT_PROBE_SIZE, 
				1000, 1, false);
		
		GroupAsa[] groupAsas = asaCalc.getGroupAsas();
		
		double tot = 0;
		
		for (GroupAsa groupAsa: groupAsas) {
			System.out.printf("%1s\t%5s\t%3s\t%6.2f\n", 
					groupAsa.getGroup().getChainId(),
					groupAsa.getGroup().getResidueNumber(),
					groupAsa.getGroup().getPDBName(), 
					groupAsa.getAsaU());
			tot+=groupAsa.getAsaU();
		}
		
		System.out.printf("Total area: %9.2f\n",tot);
		
```
See [DemoAsa](https://github.com/biojava/biojava/blob/master/biojava3-structure/src/main/java/demo/DemoAsa.java) for a fully working demo.

[Shrake 1973]: http://www.sciencedirect.com/science/article/pii/0022283673900119
