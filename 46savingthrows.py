import random

def saving(dc):
    normal = 0
    advantage = 0
    disadvantage = 0
    total = 100000
    for i in range(total):
        first = random.randint(1,20)
        second = random.randint(1,20)
        if (first >= dc): normal += 1
        if (max(first, second) >= dc): advantage += 1
        if (min(first, second) >= dc): disadvantage += 1
    return (str(dc) + 
    "\t" + str(normal/total) + "\t" + 
    str(advantage/total) + "\t" + str(disadvantage/total))

print("DC\tNormal\tAdvantage\tDisadvantage")
print(saving(5))
print(saving(10))
print(saving(15))