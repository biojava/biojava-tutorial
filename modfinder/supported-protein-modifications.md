How to get a list of supported protein modifications?
===

The protmod module contains [an XML file](https://github.com/biojava/biojava/blob/master/biojava-modfinder/src/main/resources/org/biojava/nbio/protmod/ptm_list.xml), defining a list of protein modifications, retrieved from [Protein Data Bank Chemical Component Dictionary](http://www.wwpdb.org/ccd.html), [RESID](http://pir.georgetown.edu/resid/), and [PSI-MOD](http://www.psidev.info/MOD). It contains many common modifications such glycosylation, phosphorylation, acelytation, methylation, etc. Crosslinks are also included, such disulfide bonds and iso-peptide bonds.

The protmod maintains a registry of supported protein modifications. The list of protein modifications contained in the XML file will be automatically loaded. You can [define and register a new protein modification](add-protein-modification.md) if it has not been defined in the XML file. From the protein modification registry, a user can retrieve:
- all protein modifications,
- a protein modification by ID,
- a set of protein modifications by RESID ID,
- a set of protein modifications by PSI-MOD ID,
- a set of protein modifications by PDBCC ID,
- a set of protein modifications by category (attachment, modified residue, crosslink1, crosslink2, …, crosslink7),
- a set of protein modifications by occurrence type (natural or hypothetical),
- a set of protein modifications by a keyword (glycoprotein, phosphoprotein, sulfoprotein, …),
- a set of protein modifications by involved components.

## Examples

```java 
// a protein modification by ID 
ProteinModification mod = ProteinModificationRegistry.getById(“0001”);

Set mods;

// all protein modifications 
mods = ProteinModificationRegistry.allModifications();

// a set of protein modifications by RESID ID 
mods = ProteinModificationRegistry.getByResidId(“AA0151”);

// a set of protein modifications by PSI-MOD ID 
mods = ProteinModificationRegistry.getByPsimodId(“MOD:00305”);

// a set of protein modifications by PDBCC ID 
mods = ProteinModificationRegistry.getByPdbccId(“SEP”);

// a set of protein modifications by category 
mods = ProteinModificationRegistry.getByCategory(ModificationCategory.ATTACHMENT);

// a set of protein modifications by occurrence type 
mods = ProteinModificationRegistry.getByOccurrenceType(ModificationOccurrenceType.NATURAL);

// a set of protein modifications by a keyword 
mods = ProteinModificationRegistry.getByKeyword(“phosphoprotein”);

// a set of protein modifications by involved components. 
mods = ProteinModificationRegistry.getByComponent(Component.of(“FAD”));

```

Navigation:
[Home](../README.md)
| [Book 6: The ModFinder Modules](README.md)
| Chapter 2 - How to get a list of supported protein modifications

Prev: [Chapter 1 : Installation](installation.md)

Next: [Chapter 3 : How to identify protein modifications in a structure](identify-protein-modifications.md)
