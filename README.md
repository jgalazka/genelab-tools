# genelab-tools
Scripts for working with GeneLab data.

# (1) combine_sample_assay.py
https://github.com/jgalazka/genelab-tools/blob/main/combine_sample_assay.py
Python script. Takes one Sample and on Assay csv from a GLDS study as inputs. Exports one csv showing factors and parameters shared in all samples. Export and 2nd csv showing factors and parameters than vary across samples.

# (2) build_biotype_dictionary.ipynb
https://github.com/jgalazka/genelab-tools/blob/main/build_biotype_dictionary.ipynb
Jupyter notebook. Downloads gtf file and builds dictionary to associate gene biotype to gene id. Exports as json.

# (3) add_biotype_to_raw_counts.ipynb
https://github.com/jgalazka/genelab-tools/blob/main/add_biotype_to_raw_counts.ipynb
Jupyter notebook. Add biotype to raw counts file and then filter out rRNA genes export raw counts and raw counts without rRNA genes.
