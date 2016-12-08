Reading and Writing of Basic sequence file formats
==================================================


TODO: needs more examples


## FASTA

A quick way of parsing a FASTA file is using the FastaReaderHelper class. 

Here an example that parses a UniProt FASTA file into a protein sequence.

```java
public static ProteinSequence getSequenceForId(String uniProtId) throws Exception {
		URL uniprotFasta = new URL(String.format("http://www.uniprot.org/uniprot/%s.fasta", uniProtId));
		ProteinSequence seq = FastaReaderHelper.readFastaProteinSequence(uniprotFasta.openStream()).get(uniProtId);
		System.out.printf("id : %s %s%s%s", uniProtId, seq, System.getProperty("line.separator"), seq.getOriginalHeader());
		System.out.println();

		return seq;
	}
```


BioJava can also be used to parse large FASTA files. The example below can parse a 1GB (compressed) version of TREMBL with standard memory settings.


```java
    
    
    
     /** Download a large file, e.g. ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz
     * and pass in path to local location of file
     *
     * @param args
     */
        public static void main(String[] args) {

            if ( args.length < 1) {
                System.err.println("First argument needs to be path to fasta file");
                return;
            }

            File f = new File(args[0]);

            if ( ! f.exists()) {
                System.err.println("File does not exist " + args[0]);
                return;
            }

            try {

                // automatically uncompresses files using InputStreamProvider
                InputStreamProvider isp = new InputStreamProvider();
                
                InputStream inStream = isp.getInputStream(f);
                
                FastaReader<ProteinSequence, AminoAcidCompound> fastaReader = new FastaReader<ProteinSequence, AminoAcidCompound>(
                        inStream,
                        new GenericFastaHeaderParser<ProteinSequence, AminoAcidCompound>(),
                        new ProteinSequenceCreator(AminoAcidCompoundSet.getAminoAcidCompoundSet()));
                
                LinkedHashMap<String, ProteinSequence> b;


                int nrSeq = 0;
                
                while ((b = fastaReader.process(10)) != null) {
                    for (String key : b.keySet()) {
                        nrSeq++;
                        System.out.println(nrSeq + " : " + key + " " + b.get(key));
                    }

                }
            } catch (Exception ex) {
                Logger.getLogger(ParseFastaFileDemo.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
```



<!--automatically generated footer-->

---

Navigation:
[Home](../README.md)
| [Book 1: The Core Module](README.md)
| Chapter 3 : Reading and Writing sequences

Prev: [Chapter 2 : Basic Sequence types](sequences.md)

Next: [Chapter 4 : Translating](translating.md)
