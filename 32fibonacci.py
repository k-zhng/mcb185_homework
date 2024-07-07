def fibonacci(num):
    ans = ""
    first = 0
    second = 1
    if (num == 1):
        return str(first)
    elif (num == 2):
        return str(first) + " " + str(second)
    else:
        ans += str(first) + " " + str(second) + " "
        for i in range(0, num - 2):
            (first, second) = (second, first + second)
            ans += str(second) + " "
        return ans
        
print(fibonacci(10))