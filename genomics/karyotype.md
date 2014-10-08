Parsing a karyotype file from the UCSC genome browser
=====================================================

Karyotype information for the human genome can be read from UCSC's [cytoBand.txt.gz](http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/cytoBand.txt.gz)
file.

```java

        CytobandParser me = new CytobandParser();
		try {
			SortedSet<Cytoband> cytobands = me.getAllCytobands(new URL(http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/cytoBand.txt.gz));
			SortedSet<StainType> types = new TreeSet<StainType>();
			for (Cytoband c : cytobands){
				System.out.println(c);
				if ( ! types.contains(c.getType()))
					types.add(c.getType());
			}
			System.out.println(types);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
```

If a local copy of the file is available you can specify it in the following way:

```java

SortedSet<Cytoband> cytobands = me.getAllCytobands(new URL("file://path/to/local/copy/"));

```
<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 4: The Genomics Module](README.md)
| Chapter 5 : karyotype (cytoband)

Prev: [Chapter 5 : Genebank](genebank.md)

Next: [Chapter 6 : .2bit file format](twobit.md)
