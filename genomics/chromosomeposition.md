Parse Chromosomal Information of Genes
======================================

BioJava contains a parser the [refFlat.txt.gz](http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refFlat.txt.gz)
from the UCSC genome browser that contains a mapping of gene names to chromosome positions.


```java
	try {

			List<GeneChromosomePosition> genePositions=	GeneChromosomePositionParser.getChromosomeMappings();
			System.out.println("got " + genePositions.size() + " gene positions") ;

			for (GeneChromosomePosition pos : genePositions){
				if ( pos.getGeneName().equals("FOLH1")) {
					System.out.println(pos);
					break;
				}
			}

		} catch(Exception e){
			e.printStackTrace();
		}
```

If a local copy of the file is available, it can be provide via this:


```java

        URL url = new URL("file://local/copy/of/file");

		InputStreamProvider prov = new InputStreamProvider();

		InputStream inStream = prov.getInputStream(url);

		GeneChromosomePositionParser.getChromosomeMappings(inStream);



```
<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 4: The Genomics Module](README.md)
| Chapter 3 : chromosomal positions

Prev: [Chapter 2 : gene names information](genenames.md)

Next: [Chapter 4 : GTF and GFF files](gff.md)
