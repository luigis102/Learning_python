
words = [("Pling",3), ("Plang",5), ("Plong",7)]
def convert(number):
    drops = [pl for (pl,n) in words if number % n == 0]
    if drops:
        return "".join(drops)
    return str(number)