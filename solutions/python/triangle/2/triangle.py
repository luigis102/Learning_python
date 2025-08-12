
def equilateral(sides):
    a, b, c = sorted(sides)
    if b + a >= c and a != 0:
        return a == b and b == c
    else:
        return False

equilateral([2,2,2])

def isosceles(sides):
    a, b, c = sorted(sides)
    if b + a >= c:
        return a == b or a == c or b == c
    else:
        return False

def scalene(sides):
    a, b, c = sorted(sides)
    if b + a >= c:
        return a not in [b,c] and  b not in [a,c]
    else:
        return False

        