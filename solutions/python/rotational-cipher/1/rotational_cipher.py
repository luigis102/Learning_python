import string
def rotate(text, key):
    text = list(text)
    avoid = "0123456789.,'!?(); "
    
    rot = ""
    for i in text:
        if avoid.find(i) == -1:
            if i.islower():
                alph = list(string.ascii_lowercase)
            else:
                alph = list(string.ascii_uppercase)
            ind = alph.index(i)
            if ind+key > 25:
                rot += alph[abs(26-(key+ind))]
            else:
                rot += alph[key+ind]
        else:
            rot += i
    return rot


