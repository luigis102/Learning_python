import math
def steps(number):
    n = number
    steps = 0
    try:
        n / n
    except:
        raise ValueError("Only positive integers are allowed")
    
    if n < 0:
        raise ValueError("Only positive integers are allowed")

    if n == 1:
        return 0

    while n > 1:
        if n % 2 == 0:
            n = n/2
            steps += 1
        else:
            n = (n * 3) + 1
            steps += 1 
    return steps

steps(1409)
