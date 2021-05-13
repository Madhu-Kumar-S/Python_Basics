# Python Program for factorial of a number using recursion

def factorial(n):

    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        return result

n = int(input("enter a no:"))

fact = factorial(n)

print("factorial of {} is {}".format(n, fact))

