def score(x, y):
    sumsq = x**2 + y**2
    if 25 < sumsq <= 100:
        return 1
    if 1 < sumsq <= 25:
        return 5
    if 0 <= sumsq <= 1:
        return 10
    return 0
