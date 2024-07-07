import math

def shannon_entropy (acnt, ccnt, gcnt, tcnt):
    entropy = 0;
    freqs = [acnt, ccnt, gcnt, tcnt]
    for i in range (len(freqs)):
        if (freqs[i] != 0):
            entropy -= freqs[i] * math.log(freqs[i], 2)
    return entropy

print(shannon_entropy(1,2,3,4))