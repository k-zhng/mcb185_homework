import random

z1 = 0
z2 = 0
z3 = 0
limit = 1000000

for i in range(limit):
    r = random.gauss(0.0, 1.0)
    if abs(r) > 1: z1 += 1
    if abs(r) > 2: z2 += 1
    if abs(r) > 3: z3 += 1

print(1 - z1/limit)
print(1 - z2/limit)
print(1 - z3/limit)