import math
def quadsolver(a, b, c):
    disc = b*b - 4*a*c
    if (disc < 0):
        return math.nan, math.nan
    else:
        ans1 = (-b + math.sqrt(disc))/(2*a)
        ans2 = (-b - math.sqrt(disc))/(2*a)
        return ans1, ans2
        
print(quadsolver(1,4,4))