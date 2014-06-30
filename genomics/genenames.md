Parse Gene Name Information
===========================

The following code parses [a file from the www.genenames.org](http://www.genenames.org/cgi-bin/download?title=HGNC+output+data&hgnc_dbtag=on&col=gd_app_sym&col=gd_app_name&col=gd_status&col=gd_prev_sym&col=gd_prev_name&col=gd_aliases&col=gd_pub_chrom_map&col=gd_pub_acc_ids&col=md_mim_id&col=gd_pub_refseq_ids&col=md_ensembl_id&col=md_prot_id&col=gd_hgnc_id" +
                                                             			 "&status=Approved&status_opt=2&where=((gd_pub_chrom_map%20not%20like%20%27%patch%%27%20and%20gd_pub_chrom_map%20not%20like%20%27%ALT_REF%%27)%20or%20gd_pub_chrom_map%20IS%20NULL)%20and%20gd_locus_group%20%3d%20%27protein-coding%20gene%27&order_by=gd_app_sym_sort&format=text&limit=&submit=submit&.cgifields=&.cgifields=chr&.cgifields=status&.cgifields=hgnc_dbtag)
website that contains a mapping of human gene names to other databases.


```java
    /** parses a file from the genenames website
	 *
	 * @param args
	 */
	public static void main(String[] args) {

		try {

			List<GeneName> geneNames = GeneNamesParser.getGeneNames();

			System.out.println("got " + geneNames.size() + " gene names");


			for ( GeneName g : geneNames){
				if ( g.getApprovedSymbol().equals("FOLH1"))
					System.out.println(g);
			}
			// and returns a list of beans that contains key-value pairs for each gene name

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
```

If you have a local copy of this file, then you can just provide an input stream for it:

```java

        URL url = new URL("file:///local/copy/of/file");

		InputStreamProvider prov = new InputStreamProvider();

		InputStream inStream = prov.getInputStream(url);

	    GeneNamesParser.getGeneNames(inStream);


```