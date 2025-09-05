def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    distance = sum(1 for item in zip(strand_a,strand_b) if item[0] != item[1])
    return distance