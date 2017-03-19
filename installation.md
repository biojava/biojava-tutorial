## Quick Installation

In the beginning, just one quick paragraph of how to get access to BioJava.

BioJava is open source and you can get the code from [Github](https://github.com/biojava/biojava), however it might be easier this way:

BioJava uses [Maven](http://maven.apache.org/) as a build and distribution system. If you are new to Maven, take a look at the [Getting Started with Maven](http://maven.apache.org/guides/getting-started/index.html)  guide.

As of version 4, BioJava is available in maven central. This is all you would need to add a BioJava dependency to your projects:

```xml
        <dependencies>
                ...

                 <!-- This imports the latest version of BioJava genomics module -->
                <dependency>

                        <groupId>org.biojava</groupId>
                        <artifactId>biojava-genome</artifactId>
                        <version>4.2.0</version>
                        <!-- note: the genomics module depends on the BioJava-core module and will import it automatically -->
                </dependency>


                <!-- other biojava jars as needed -->


                <!-- This imports the latest version of BioJava structure module -->
                 <dependency>

                       <groupId>org.biojava</groupId>
                       <artifactId>biojava-structure</artifactId>
                        <version>4.2.0</version>
                  </dependency>
        </dependencies> 
```

If you run 

<pre>
    mvn package
</pre>

 on your project, the BioJava dependencies will be automatically downloaded and installed for you.

