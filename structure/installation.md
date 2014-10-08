## Quick Installation

In the beginning, just one quick paragraph of how to get access to BioJava.

BioJava is open source and you can get the code from [Github](https://github.com/biojava/biojava), however it might be easier this way:

BioJava uses [Maven](http://maven.apache.org/) as a build and distribution system. If you are new to Maven, take a look at the [Getting Started with Maven](http://maven.apache.org/guides/getting-started/index.html)  guide.

We are providing a BioJava specific Maven repository at (http://biojava.org/download/maven/) .

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
        <dependencies>
                ...
                <dependency>
                        <!-- This imports the latest SNAPSHOT builds from the protein structure modules of BioJava.
                        -->                        
                        <groupId>org.biojava</groupId>
                        <artifactId>biojava3-structure</artifactId>
                        <version>3.0.8</version>
                </dependency>
                <!-- if you want to use the visualisation tools you need also this one: -->
                <dependency>                                         
                        <groupId>org.biojava</groupId>
                        <artifactId>biojava3-structure-gui</artifactId>
                        <version>3.0.8</version>
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
| [Book 3: The Protein Structure modules](README.md)
| Chapter 1 : Installation

Next: [Chapter 2 : First Steps](firststeps.md)
