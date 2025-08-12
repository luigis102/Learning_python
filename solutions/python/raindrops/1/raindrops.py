def convert(number):
    words = ["Pling","Plang","Plong"]
    div = [3,5,7]
    n = [words[div.index(i)] for i in div if number % i == 0]
    if n : return "".join(n)
    else:
        return str(number)



    


