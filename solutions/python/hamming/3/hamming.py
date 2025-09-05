def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(1 for chr_a,chr_b in zip(strand_a,strand_b) if chr_a != chr_b)