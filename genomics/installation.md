## Quick Installation

In the beginning, just one quick paragraph of how to get access to BioJava.

BioJava is open source and you can get the code from [Github](https://github.com/biojava/biojava), however it might be easier this way:

BioJava uses [Maven](http://maven.apache.org/) as a build and distribution system. If you are new to Maven, take a look at the [Getting Started with Maven](http://maven.apache.org/guides/getting-started/index.html)  guide.

Currently, we are providing a BioJava specific Maven repository at (http://biojava.org/download/maven/) .

You can add the BioJava repository by adding the following XML to your project pom.xml file:

```xml
        <repositories>
            ...
            <repository>
                <id>biojava-maven-repo</id>
                <name>BioJava repository</name>
                <url>http://www.biojava.org/download/maven/</url>           
            </repository>
        </repositories>
```

We are currently in the process of changing our distribution to Maven Central, which would not even require this configuration step.

```xml
        <dependencies>
                ...

                 <!-- This imports the latest version of BioJava genomics module -->
                <dependency>

                        <groupId>org.biojava</groupId>
                        <artifactId>biojava3-genomics</artifactId>
                        <version>3.0.8</version>
                        <!-- note: the genomics module depends on the BioJava-core module and will import it automatically -->
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
| [Book 4: The Genomics Module](README.md)
| Chapter 1 : Installation

Next: [Chapter 2 : gene names information](genenames.md)
