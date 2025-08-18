def to_rna(dna_strand):
    dna = list(dna_strand)
    complement = [("C","G"),("G","C"),("T","A"),("A","U")]
    new = [copy for letter in dna for orig,copy in complement if letter == orig]
    return "".join(new)

