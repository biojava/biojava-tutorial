External Databases
==================

Biojava provides access to a number of external structural databases. These often use [caching](caching.md) to reduce the amount of data which must be downloaded from the database.

SCOP
----

<div style="float:right; margin-left:auto; border: grey 1px;">
	<img src="img/1dan_scop.png" width=300 /><br/>
	<p style="width:300px; font-size:80%;">(Top) The structure 1DAN contains four chains. (Bottom) These chains are broken up into six SCOP domains. The green chain L becomes 3 domains, while a combination of chains U (red) and T (orange) go to form the central purpal domain.</p>
</div>

The Structural Classification of Proteins (SCOP) is a manually curated classification of protein structural domains. It provides two pieces of data:

* The breakdown of a protein into structural domains
* A classification of domains according to their structure.

The structure for a known SCOP domain can be fetched via its 7-letter domain ID (eg 'd2bq6a1') via ```StructureIO.getStructure()```, as described in [Local PDB Installations](caching.md#Caching of other SCOP, CATH).

The SCOP classification can be accessed through the [```ScopDatabase```](http://www.biojava.org/docs/api/org/biojava/bio/structure/scop/ScopDatabase.html) class.

    ScopDatabase scop = ScopFactory.getSCOP();

### Inspecting SCOP domains

A list of domains can be retrieved for a given protein.

    List<ScopDomain> domains = scop.getDomainsForPDB("4HHB");

You can get lots of useful information from the [```ScopDomain```](http://www.biojava.org/docs/api/org/biojava/bio/structure/scop/ScopDomain.html) object. 

    ScopDomain domain = domains.get(0);
    String scopID = domain.getScopId(); // d4hhba_
    String classification = domain.getClassificationId(); // a.1.1.2
    int sunId = domain.getSunId(); // 15251

### Viewing the SCOP hierarchy

The full hierarchy is available as a tree of [```ScopNode```](http://www.biojava.org/docs/api/org/biojava/bio/structure/scop/ScopNode.html)s, which can be easily traversed using their ```getParentSunid()``` and ```getChildren()``` methods.

    ScopNode node = scop.getScopNode(sunId);
    while (node != null){
        System.out.println(scop.getScopDescriptionBySunid(node.getSunid()));
        node = scop.getScopNode(node.getParentSunid());
    }

ScopDatabase also provides access to all nodes at a particular level.

    List<ScopDescription> superfams = scop.getByCategory(ScopCategory.Superfamily);
    System.out.println("Total nr. of superfamilies:" + superfams.size());

### Types of ScopDatabase

Several types of ```ScopDatabase``` are available. These can be instantiated manually when more control is needed.

* __RemoteScopInstallation__ (default) Fetches data one node at a time from the internet. Useful when perfoming a small number of operations.
* __ScopeInstallation__ Downloads all SCOP data as a batch and caches it for later use. Much faster when performing many operations.

Several internal BioJava classes use ```ScopFactory.getSCOP()``` when they encounter references to SCOP domains, so it is always a good idea to notify the ```ScopFactory``` when using a custom ```ScopDatabase``` instance.

    ScopDatabase scop = new ScopInstallation();
    ScopFactory.setScopDatabase(scop);

Several versions of SCOP are available.

    // Use Steven Brenner's updated version of SCOP
    scop = ScopFactory.getSCOP(ScopFactory.VERSION_1_75B);
    // Use an old version globally, perhaps for an older benchmark
    ScopFactory.setScopDatabase(ScopFactory.VERSION_1_69);


