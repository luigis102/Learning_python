
def is_triangle(sides):
    a, b, c = sorted(sides) 
    return b + a >= c and a != 0 
        
def equilateral(sides):
    return is_triangle(sides) and (len(set(sides)) == 1)

def isosceles(sides):
    return is_triangle(sides) and (len(set(sides)) <= 2)


def scalene(sides):
    return is_triangle(sides) and (len(set(sides)) == 3)


        