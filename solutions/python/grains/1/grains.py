def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    grains = (2**(number-1))
    return grains

def total():
    grains = 0
    for i in range(1,65):
        grains += (2**(i-1))
    return grains
