import random
import sys

games = 1000000
log = games // 100
total = 0
zeroes = 0
for i in range(games):
    if i % log == 0: print(f'{100 * i/games:.0f}')
    score = 0
    for target in range(2,13):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if (d1 + d2 == target):
            score += target
    if score == 0: zeroes += 1
    total += score

print(total / games)
print(zeroes / games)