import math
def classify(number):
    try:
        assert int(number) > 0
    except:
        raise ValueError("Classification is only possible for positive integers.")
    divisors = sum(i for i in range(1,number) if number % i == 0)
    if divisors > number:
        return "abundant"
    if divisors == number:
        return "perfect"
    return "deficient"


