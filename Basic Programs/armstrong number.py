# Python Program to check Armstrong Number
from math import *

def armstrong(no):
    l = list(no)
    l = [int(i) for i in l]
    o = len(l)
    n = 0
    for i in l:
        n = n + pow(i, o)

    return int(n)

no = input("enter a number:")

result = armstrong(no)

if result == int(no):
    print("{} is armstrong number".format(result))
else:
    print(("{} is not armstrong number".format(int(no))))