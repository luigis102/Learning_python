def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    distance = 0
    for base in range(len(strand_a)):
        if strand_a[base] != strand_b[base]:
            distance += 1
    return distance