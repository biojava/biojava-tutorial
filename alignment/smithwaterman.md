Smith Waterman - Local Alignment
################################

BioJava contains implementation for various protein sequence and 3D structure alignment algorithms. Here is how to run a local, Smith-Waterman, alignment of two protein sequences:



```java
public static void main(String[] args) throws Exception {

		String uniprotID1 = "P69905";
		String uniprotID2 = "P68871";

		ProteinSequence s1 = getSequenceForId(uniprotID1);
		ProteinSequence s2 = getSequenceForId(uniprotID2);

		SubstitutionMatrix<AminoAcidCompound> matrix = SubstitutionMatrixHelper.getBlosum65();

		GapPenalty penalty = new SimpleGapPenalty();

		int gop = 8;
		int extend = 1;
		penalty.setOpenPenalty(gop);
		penalty.setExtensionPenalty(extend);


		PairwiseSequenceAligner<ProteinSequence, AminoAcidCompound> smithWaterman =
				Alignments.getPairwiseAligner(s1, s2, PairwiseSequenceAlignerType.LOCAL, penalty, matrix);

		SequencePair<ProteinSequence, AminoAcidCompound> pair = smithWaterman.getPair();


		System.out.println(pair.toString(60));


	}

	private static ProteinSequence getSequenceForId(String uniProtId) throws Exception {
		URL uniprotFasta = new URL(String.format("https://www.uniprot.org/uniprot/%s.fasta", uniProtId));
		ProteinSequence seq = FastaReaderHelper.readFastaProteinSequence(uniprotFasta.openStream()).get(uniProtId);
		System.out.printf("id : %s %s%s%s", uniProtId, seq, System.getProperty("line.separator"), seq.getOriginalHeader());
		System.out.println();

		return seq;
	}
```
