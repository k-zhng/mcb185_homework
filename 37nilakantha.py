def nilakantha(num_terms):
    ans = 3
    sign = 1
    for i in range (num_terms):
        ans += sign * 4 / ((i+1) * 2 * ((i+1) * 2 + 1) * ((i+1) * 2 + 2))
        sign *= -1
    return ans
    
for i in range (10):
    print(i)
    print(nilakantha(i))