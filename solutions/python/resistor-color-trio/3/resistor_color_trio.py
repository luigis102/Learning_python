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

def label(colors):
    value = color_values[colors[0]]*10 + color_values[colors[1]]
    total = (10 ** color_values[colors[2]]) * value
    
    if total != 0:
        if total % 10**9 == 0:
            return f"{int(total/10**9)} gigaohms"
        if total % 10**6 == 0:
            return f"{int(total/10**6)} megaohms"
        if total % 10**3 == 0:
            return f"{int(total/10**3)} kiloohms"
        return f"{total} ohms"
    return f"{total} ohms"



    
