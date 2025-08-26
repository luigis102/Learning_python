color_values = {
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

exp_prefix = [(9,"gigaohms"),(6,"megaohms"),(3,"kiloohms")]

def label(colors):
    value = color_values[colors[0]]*10 + color_values[colors[1]]
    total = (10 ** color_values[colors[2]]) * value

    for exp,prefix in exp_prefix:
        if total % 10**exp == 0 and total != 0:
            return f"{total//10**exp} {prefix}"
    return f"{total} ohms"



    
