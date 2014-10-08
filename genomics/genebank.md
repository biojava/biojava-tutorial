Reading and writing a Genbank file
==================================

There are multiple ways how to read a Genbank file.

## Method 1: Read a Genbank file using the GenbankProxySequenceReader

```java

	GenbankProxySequenceReader<AminoAcidCompound> genbankProteinReader
	= new GenbankProxySequenceReader<AminoAcidCompound>("/tmp", "NP_000257", AminoAcidCompoundSet.getAminoAcidCompoundSet());
	ProteinSequence proteinSequence = new ProteinSequence(genbankProteinReader);
	genbankProteinReader.getHeaderParser().parseHeader(genbankProteinReader.getHeader(), proteinSequence);
	System.out.println("Sequence" + "(" + proteinSequence.getAccession() + "," + proteinSequence.getLength() + ")=" +
proteinSequence.getSequenceAsString().substring(0, 10) + "...");

	GenbankProxySequenceReader<NucleotideCompound> genbankDNAReader
	= new GenbankProxySequenceReader<NucleotideCompound>("/tmp", "NM_001126", DNACompoundSet.getDNACompoundSet());
	DNASequence dnaSequence = new DNASequence(genbankDNAReader);
	genbankDNAReader.getHeaderParser().parseHeader(genbankDNAReader.getHeader(), dnaSequence);
	System.out.println("Sequence" + "(" + dnaSequence.getAccession() + "," + dnaSequence.getLength() + ")=" +
dnaSequence.getSequenceAsString().substring(0, 10) + "...");

```


## Method 2: Read a Genbank file using GenbankReaderHelper

```java
	File dnaFile = new File("src/test/resources/NM_000266.gb");
	File protFile = new File("src/test/resources/BondFeature.gb");

	LinkedHashMap<String, DNASequence> dnaSequences = GenbankReaderHelper.readGenbankDNASequence( dnaFile );
	for (DNASequence sequence : dnaSequences.values()) {
	    	System.out.println( sequence.getSequenceAsString() );
	}

	LinkedHashMap<String, ProteinSequence> protSequences = GenbankReaderHelper.readGenbankProteinSequence(protFile);
	for (ProteinSequence sequence : protSequences.values()) {
		System.out.println( sequence.getSequenceAsString() );
	}

```

## Method 3: Read a Genbank file using the GenbankReader Object

```java

	FileInputStream is = new FileInputStream(dnaFile);
	GenbankReader<DNASequence, NucleotideCompound> dnaReader = new GenbankReader<DNASequence, NucleotideCompound>(
	        is,
	        new GenericGenbankHeaderParser<DNASequence,NucleotideCompound>(),
	        new DNASequenceCreator(DNACompoundSet.getDNACompoundSet())
	);
	dnaSequences = dnaReader.process();
	is.close();
	System.out.println(dnaSequences);

	is = new FileInputStream(protFile);
	GenbankReader<ProteinSequence, AminoAcidCompound> protReader = new GenbankReader<ProteinSequence, AminoAcidCompound>(
	        is,
	        new GenericGenbankHeaderParser<ProteinSequence,AminoAcidCompound>(),
	        new ProteinSequenceCreator(AminoAcidCompoundSet.getAminoAcidCompoundSet())
	);
	protSequences = protReader.process();
	is.close();
	System.out.println(protSequences);

	```


# Write a Genbank file


Use the GenbankWriterHelper to write DNA sequences into a Genbank file.

```java

        // First let's read dome DNA sequences from a genbank file

		File dnaFile = new File("src/test/resources/NM_000266.gb");
		LinkedHashMap<String, DNASequence> dnaSequences = GenbankReaderHelper.readGenbankDNASequence( dnaFile );
		ByteArrayOutputStream fragwriter = new ByteArrayOutputStream();
		ArrayList<DNASequence> seqs = new ArrayList<DNASequence>();
		for(DNASequence seq : dnaSequences.values()) {
			seqs.add(seq);
		}

		// ok now we got some DNA sequence data. Next step is to write it

		GenbankWriterHelper.writeNucleotideSequence(fragwriter, seqs,
				GenbankWriterHelper.LINEAR_DNA);

        // the fragwriter object now contains a string representation in the Genbank format
        // and you could write this into a file
        // or print it out on the console
		System.out.println(fragwriter.toString());

```
<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 4: The Genomics Module](README.md)
| Chapter 5 : Genebank

Prev: [Chapter 4 : GTF and GFF files](gff.md)

Next: [Chapter 5 : karyotype (cytoband)](karyotype.md)
