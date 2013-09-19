External Databases
==================

Biojava provides access to a number of external structural databases. These often use [caching](caching.md) to reduce the amount of data which must be downloaded from the database.

SCOP
----

<div style="float:right; margin-left:auto; border: grey 1px;">
	<img src="img/1dan_scop.png" width=300 /><br/>
	<p style="width:300px; font-size:80%;">(Top) The structure 1DAN contains four chains. (Bottom) These chains are broken up into six SCOP domains. The green chain L becomes 3 domains, while a combination of chains U (red) and T (orange) go to form the central purpal domain.</p>
</div>

The Structural Classification of Proteins (SCOP) is a manually curated classification of protein structural domains. It provides two pieces of data:

* The breakdown of a protein into structural domains
* A classification of domains according to their structure.

Domains are referred to by a 7-letter identifier consisting of the letter 'd', the pdb id of the structure, the chain identifier (or '.' for multichain domains), and a alphanumeric domain identifier (or '_' for single-domain chains). Domains are classified into a heirarchy according to their structural similarity. From least similar to most similar, the levels are:

1. __Class__ Similar secondary structure composition
2. __Fold__ Major structural similarity
3. __Superfamily__ Probably evolutionarily related
4. __Family__ Clearly evolutionarily related
5. __Domain__ Unique domain