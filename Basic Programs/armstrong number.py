# Python Program to check Armstrong Number
from math import *

def armstrong(no):
    l = []
    for i in no:
        l.append(int(i))
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