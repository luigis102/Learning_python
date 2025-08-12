def is_armstrong_number(number):
    digits = str(number)
    test = sum(int(ch)**len(digits) for ch in digits)
    return test == number
