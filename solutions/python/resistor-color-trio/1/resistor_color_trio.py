names = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
    }

suffix = ["kilo","mega","giga"]

def label(colors):
    value = names[colors[0]]*10 + names[colors[1]]
    total = (10 ** names[colors[2]]) * value

    divis = [total % 10**i == 0 and total != 0 for i in [3,6,9]]
    
    if True in divis:
        zeros = divis.index(True)
        if divis.count(True) > 2:
            zeros += 2
        elif divis.count(True) > 1:
            zeros += 1
        return f"{int(total/10**(3*(zeros+1)))} {suffix[zeros]}ohms" 

    return f"{total} ohms"



    
