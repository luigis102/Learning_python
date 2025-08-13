def convert(number):
    words = [("Pling",3), ("Plang",5), ("Plong",7)]
    n = [words[i][0] for i in range(3) if number % words[i][1] == 0]
    if n: 
        return "".join(n)
    return str(number)
    



    


