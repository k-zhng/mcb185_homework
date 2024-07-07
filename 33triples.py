import math
def triple_find():
    count = 0;
    for i in range(1, 100):
        for j in range(i, 100):
            c = math.sqrt(i**2 + j**2)
            if (c % 1 == 0):
                count += 1;
                #print (str(i) + " " + str(j) + " " + str(c))
    return count

print(triple_find())