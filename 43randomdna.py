import random
def random_dna(num):
    ans = ""
    heading = ">seq-"
    for i in range(num):
        ans += heading + str(i+1) + "\n"
        length = random.randint(50,60)
        for i in range (length):
            ans += random.choice('ACGT')
        ans += "\n"
    return ans

print(random_dna(5))