def factorial(n):
    if n < 2: # Base Case
        return 1
    else:
        return n * factorial(n-1)


for i in range(10):
    print(factorial(i))