def fizzbuzz():
    ans = ""
    for i in range(1, 100):
        if (i % 3 == 0):
            if (i % 5 == 0):
                ans += "FizzBuzz "
            else:
                ans += "Fizz "
        elif (i % 5 == 0):
            ans += "Buzz "
        else: 
            ans += str(i) + " "
    return ans
print(fizzbuzz())