def is_valid(isbn):
    isbn = list(isbn)

    if "-" in isbn:
        isbn = [i for i in isbn if i != "-"]
    if not len(isbn) == 10:
        return False   
    if isbn[-1] == "X":
        isbn.remove("X")
        isbn.extend(["10"])   
    try:
        l = list(map(int,isbn))
    except:
        return False
        
    r = 10
    check = 0
    while r >= 1:
        check += l[-r] * r
        r -= 1

    if check % 11 == 0:
        return True
    return False
 