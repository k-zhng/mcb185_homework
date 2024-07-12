import random
import math
def randompi(iters):
    total = 0
    count = 0
    while True:
        x = random.random()
        y = random.random()
        total += 1
        
        if (math.sqrt(x ** 2 + y ** 2) < 1):
            count += 1
        print(4 * count / total)

randompi(0)