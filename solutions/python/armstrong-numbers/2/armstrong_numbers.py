def is_armstrong_number(number):
    digits = str(number)
    test = [int(i)**len(digits) for i in digits]
    return sum(test) == number
