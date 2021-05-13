# Python program to find sum and product of elements in list
from functools import *

def add1(l):
    print("sum of all elements in list is :",end=' ')
    print(sum(l))

def add2(l):
    print("sum of all elements in list is :",reduce(lambda x,y: x+y , l))


def mul1(l):
    print("product of all elements in list is :",end=' ')
    p = 1
    for i in l:
        p = p * i
    print(p)

def mul2(l):
    print("product of all elements in list is :",reduce(lambda x, y: x*y, l))


lst = [1, 2, 3, 4, 5]

add1(lst)
mul1(lst)
add2(lst)
mul2(lst)


