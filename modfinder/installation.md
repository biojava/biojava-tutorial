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
                <dependency>
                        <!-- This imports the latest SNAPSHOT builds from the protein modfinder modules of BioJava.
                        -->                        
                        <groupId>org.biojava</groupId>
                        <artifactId>biojava-modfinder</artifactId>
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


<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 6: The ModFinder Modules](README.md)
| Chapter 1 : Installation

Next: [Chapter 2 : How to get the list of supported protein modifications](supported-protein-modifications.md)
