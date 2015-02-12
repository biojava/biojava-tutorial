## Quick Installation

In the beginning, just one quick paragraph of how to get access to BioJava.

BioJava is open source and you can get the code from [Github](https://github.com/biojava/biojava), however it might be easier this way:

BioJava uses [Maven](http://maven.apache.org/) as a build and distribution system. If you are new to Maven, take a look at the [Getting Started with Maven](http://maven.apache.org/guides/getting-started/index.html)  guide.

As of version 4, BioJava is available in maven central. This is all you would need to add a BioJava dependency to your projects:

```xml
        <dependencies>
                ...

                 <!-- This imports the latest version of BioJava core module -->
                <dependency>

                        <groupId>org.biojava</groupId>
                        <artifactId>biojava-alignment</artifactId>
                        <version>4.0.0</version>
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
| [Book 2: The Alignment module](README.md)
| Chapter 1 : Installation
