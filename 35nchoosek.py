def nchoosek(n, k):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    for i in range(1, k + 1):
        ans /= i
    for i in range(1, n - k + 1):
        ans /= i
    return ans

print(nchoosek(10,2))
print(nchoosek(5,3))