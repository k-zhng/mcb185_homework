def oligotemp(acnt, ccnt, gcnt, tcnt):
    size = acnt + ccnt + gcnt + tcnt
    if (size <= 13):
        return (acnt + tcnt) * 2 + (gcnt + ccnt) * 4
    else:
        return 64.9 + 41 * (gcnt + ccnt - 16.4) / (size)
        
print(oligotemp(1,2,3,4))
print(oligotemp(20,30,13,13))