def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(998))

'''
Recursion practice:
Example: factorial(3)
Base case not reached, call factorial(2)
Base case not reached, call factorial(1)
Base case reached, return 1
Go back up to factorial 2, return 2 * factorial(1), which is 1
Go back up to factorial 3, return 3 * factorial(2), which is 2
Return 6, 3! = 6
'''