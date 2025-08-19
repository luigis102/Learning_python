def to_rna(dna_strand):
    complement = {"C":"G","G":"C","T":"A","A":"U"}
    new = str.maketrans(complement)
    return dna_strand.translate(new)

