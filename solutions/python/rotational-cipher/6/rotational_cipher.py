import string
def rotate(text, key):
    upper, lower = string.ascii_uppercase, string.ascii_lowercase
    ucipher = upper[key:] + upper[:key]
    lcipher = ucipher.lower()

    table = str.maketrans(upper + lower , ucipher + lcipher)

    return text.translate(table)
            
        
    

