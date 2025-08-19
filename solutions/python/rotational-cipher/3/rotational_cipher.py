def rotate(text, key):
    shift = {}
    for i in list(text):
        loc = ord(i)
        if 65 <= loc <= 90:
            if loc+key > 90:
                shift.update({i: loc+key-26})
            else:
                shift.update({i: loc+key})
        if 97 <= loc <= 122:
            if loc+key > 122:
                shift.update({i: loc+key-26})
            else:
                shift.update({i: loc+key}) 
                
    table = str.maketrans(shift)
    return text.translate(table)
            
        
    

