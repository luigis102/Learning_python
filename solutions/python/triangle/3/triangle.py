
def is_triangle(a,b,c):
    return b + a >= c and a != 0
        
def equilateral(sides):
    a, b, c = sorted(sides) 
    return is_triangle(a,b,c) and (a == b and b == c)

equilateral([2,2,2])

def isosceles(sides):
    a, b, c = sorted(sides)
    return is_triangle(a,b,c) and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sorted(sides)
    return is_triangle(a,b,c) and (a not in [b,c] and  b not in [a,c])


        