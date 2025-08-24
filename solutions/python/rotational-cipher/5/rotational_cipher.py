import string
def rotate(text, key):
    upper = string.ascii_lowercase
    ucipher = upper[key:] + upper[:key]
    lower = string.ascii_uppercase
    lcipher = lower[key:] + lower[:key]

    table = str.maketrans(upper + lower , ucipher + lcipher)

    return text.translate(table)
            
        
    

