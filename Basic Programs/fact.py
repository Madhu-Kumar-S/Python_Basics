# Factorial of n natural numbers

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
        print("factorial of {:d} is {:d}".format(i, fact))


factorial(int(input("enter a num:")))
