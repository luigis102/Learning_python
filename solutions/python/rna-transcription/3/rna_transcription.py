def to_rna(dna_strand):
    new = str.maketrans("CGTA","GCAU")
    return dna_strand.translate(new)

