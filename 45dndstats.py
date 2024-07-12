import random
def dndstats():
    normal = 0
    r1 = 0
    pair = 0
    drop = 0
    num_cases = 100000
    for i in range(num_cases):
        thislist = [0, 0, 0, 0]
        for i in range(3):
            x = random.randint(1,6)
            thislist[i] = x
            normal += x
            if (x != 1):
                r1 += x
            else:
                a = random.randint(1,6)
                while (a == 1):
                    a = random.randint(1,6)
                r1 += a
            y = random.randint(1,6)
            pair += max(x,y)
        new_roll = random.randint(1,6)
        thislist[3] = new_roll
        min_num = 7
        for i in thislist:
            if i < min_num:
                min_num = i
        drop += sum(thislist) - min_num
    print(f'normal is {normal/num_cases}')
    print(f're-roll 1 is {r1/num_cases}')
    print(f'pairs is {pair/num_cases}')
    print(f'four is {drop/num_cases}')
    
dndstats()