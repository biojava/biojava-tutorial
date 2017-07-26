## Quick Installation

In the beginning, just one quick paragraph of how to get access to BioJava.

BioJava is open source and you can get the code from [Github](https://github.com/biojava/biojava), however it might be easier this way:

BioJava uses [Maven](http://maven.apache.org/) as a build and distribution system. If you are new to Maven, take a look at the [Getting Started with Maven](http://maven.apache.org/guides/getting-started/index.html)  guide.

As of version 4, BioJava is available in maven central. This is all you would need to add a BioJava dependency to your projects:

```xml
        <dependencies>
                ...
                <dependency>
                        <!-- This imports the latest SNAPSHOT builds from the protein structure modules of BioJava.
                        -->                        
                        <groupId>org.biojava</groupId>
                        <artifactId>biojava-structure</artifactId>
                        <version>4.2.0</version>
                </dependency>
                <!-- if you want to use the visualisation tools you need also this one: -->
                <dependency>                                         
                        <groupId>org.biojava</groupId>
                        <artifactId>biojava-structure-gui</artifactId>
                        <version>4.2.0</version>
                </dependency>
                <!-- other biojava jars as needed -->
        </dependencies> 
```

If you run 

<pre>
    mvn package
</pre>

 on your project, the BioJava dependencies will be automatically downloaded and installed for you.

### (Optional) Configuration

BioJava can be configured through several properties:

| Property | Description |
| --- | --- |
| `PDB_DIR` | Directory for caching structure files from the PDB. Mirrors the PDB's FTP server directory structure, with `PDB_DIR` equivalent to ftp://ftp.wwpdb.org/pub/pdb/. Default: temp directory |
| `PDB_CACHE_DIR` | Cache directory for other files related to the structure package. Default: temp directory |

These can be set either as java properties or as environmental variables. For example:

```
# This could be added to .bashrc
export PDB_DIR=...
# Or override for a particular execution
java -DPDB_DIR=... -cp ...
```

Note that your IDE may ignore `.bashrc` settings, but should have a preference for passing VM arguments.

<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 3: The Structure Modules](README.md)
| Chapter 1 : Installation

Next: [Chapter 2 : First Steps](firststeps.md)
