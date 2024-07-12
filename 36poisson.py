import math

def poisson (k, n):
    return (n ** k) * (math.e ** (-n)) / math.factorial(k)

print(poisson(2,2))
    