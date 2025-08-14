def score(x, y):
    sumsq = x**2 + y**2
    if 0 <= sumsq <= 1:
        return 10
    if sumsq <= 25:
        return 5
    if sumsq <= 100:
        return 1
    return 0
