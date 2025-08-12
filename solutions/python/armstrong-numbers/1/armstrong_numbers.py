def is_armstrong_number(number):
    digits = list(str(number))
    test = [int(i)**len(digits) for i in digits]
    return sum(test) == number
