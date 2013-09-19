Local PDB Installations
=======================

BioJava can automatically download and install most of the data files required. Those downloads 
will happen only once. Future requests for the data file will re-use the local copy.

The main class that provides this functionality is the [AtomCache](http://www.biojava.org/docs/api/org/biojava/bio/structure/align/util/AtomCache.html).

It is hidden inside the StructureIO class, that we already encountered earlier.

<pre>
  Structure structure = StructureIO.getStructure("4hhb");			
</pre>

is the same as

<pre>
  AtomCache cache = new AtomCache();
  cache.getStructure("4hhb");
</pre>


## Where are the files getting written to?

By default the AtomCache writes all files into a temporary location (The system temp directory "java.io.tempdir"). 

If you already have a local PDB installation, or you want to use a more permanent location to store the files,
you can configure the AtomCache by setting the PDB_DIR system property

<pre>
    -DPDB_DIR=/wherever/you/want/
</pre>

An alternative is to hard-code the path in this way:

<pre>
			AtomCache cache = new AtomCache();

			cache.setPath("/path/to/pdb/files/");
</pre>

