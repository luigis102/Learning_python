import string
def rotate(text, key):
    text = list(text)
    plain = string.ascii_lowercase
    cipher = plain[key:] + plain[:key]
    for i in range(len(text)):
        ch = text[i]
        if ch.islower():
            plain, cipher = plain.lower(), cipher.lower()
            table = str.maketrans(plain,cipher)
            text[i] = ch.translate(table)
        elif ch.isupper():
            plain, cipher = plain.upper(), cipher.upper()
            table = str.maketrans(plain,cipher)
            text[i] = ch.translate(table)

    return "".join(text)
            
        
    

