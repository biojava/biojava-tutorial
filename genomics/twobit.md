Reading a .2bit file
====================

UCSC's .2bit files provide a compact representation of the DNA sequences for a genome. The TwoBitParser class provides
the access to the content of this file.

```java
File f = new File("/path/to/file.2bit");
TwoBitParser p = new TwoBitParser(File f);

String[] names = p.getSequenceNames();
for(int i=0;i<names.length;i++) {
  p.setCurrentSequence(names[i]);
  p.printFastaSequence();
  p.close();
}

```
<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 4: The Genomics Module](README.md)
| Chapter 6 : .2bit file format

Prev: [Chapter 5 : karyotype (cytoband)](karyotype.md)
