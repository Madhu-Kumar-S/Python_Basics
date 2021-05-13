# Python Program for Sum of squares and cubes of first n natural numbers

import math as m

def square(n):
    print("Square of 1st {} natural no is:".format(n))
    sum = 0
    for i in range(1,n+1):
        sum = sum + m.pow(i,2)
    print(int(sum))

def cube(n):
    print("Cubee of 1st {} natural no is:".format(n))
    sum = 0
    for i in range(1,n+1):
        sum = sum + m.pow(i, 3)
    print(int(sum))

n = int(input("enter how many natural numbers:"))

square(n)

cube(n)
