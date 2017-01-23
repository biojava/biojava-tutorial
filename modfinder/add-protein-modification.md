How to define a new protein modiifcation?
===

The protmod module automatically loads [a list of protein modifications](supported-protein-modifications.md) into the protein modification registry. In case you have a protein modification that is not preloaded, it is possible to define it by yourself and add it into the registry.

## Example: define and register disulfide bond in java code

```java
// define the involved components, in this case two cystines (CYS) 
List components = new ArrayList(2);
components.add(Component.of("CYS"));
components.add(Component.of("CYS"));

// define the atom linkages between the components, in this case the SG atoms on both CYS groups
ModificationLinkage linkage = new ModificationLinkage(components, 0, “SG”, 1, “SG”);

// define the modification condition, i.e. what components are involved and what atoms are linked between them
ModificationCondition condition = new ModificationConditionImpl(components, Collections.singletonList(linkage));

// build a modification
ProteinModification mod =
       new ProteinModificationImpl.Builder("0018_test", 
       ModificationCategory.CROSS_LINK_2,
       ModificationOccurrenceType.NATURAL,
       condition)
       .setDescription("A protein modification that effectively cross-links two L-cysteine residues to form L-cystine.")
       .setFormula("C 6 H 8 N 2 O 2 S 2")
       .setResidId("AA0025")
       .setResidName("L-cystine")
       .setPsimodId("MOD:00034")
       .setPsimodName("L-cystine (cross-link)")
       .setSystematicName("(R,R)-3,3'-disulfane-1,2-diylbis(2-aminopropanoic acid)")
       .addKeyword("disulfide bond")
       .addKeyword("redox-active center")
   .build();

//register the modification
ProteinModificationRegistry.register(mod);
```

## Example: definedisulfide bond in xml file and register by java code
```xml
<ProteinModifications>
	<Entry>
		<Id>0018</Id>
		<Description>A protein modification that effectively cross-links two L-cysteine residues to form L-cystine.</Description>
		<SystematicName>(R,R)-3,3'-disulfane-1,2-diylbis(2-aminopropanoic acid)</SystematicName>
		<CrossReference>
			<Source>RESID</Source>
			<Id>AA0025</Id>
			<Name>L-cystine</Name>
		</CrossReference>
		<CrossReference>
			<Source>PSI-MOD</Source>
			<Id>MOD:00034</Id>
			<Name>L-cystine (cross-link)</Name>
		</CrossReference>
		<Condition>
			<Component component="1">
				<Id source="PDBCC">CYS</Id>
			</Component>
			<Component component="2">
				<Id source="PDBCC">CYS</Id>
			</Component>
			<Bond>
				<Atom component="1">SG</Atom>
				<Atom component="2">SG</Atom>
			</Bond>
		</Condition>
		<Occurrence>natural</Occurrence>
		<Category>crosslink2</Category>
		<Keyword>redox-active center</Keyword>
		<Keyword>disulfide bond</Keyword>
	</Entry>
</ProteinModifications>
```

```java
FileInputStream fis = new FileInputStream("path/to/file");
ProteinModificationXmlReader.registerProteinModificationFromXml(fis);
```


Navigation:
[Home](../README.md)
| [Book 6: The ModFinder Modules](README.md)
| Chapter 4 - How to define a new protein modiifcation

Prev: [Chapter 3 : How to identify protein modifications in a structure](installation.md)

