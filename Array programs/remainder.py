# Python Program for Find reminder of array multiplication divided by n

from array import *

def getdata():

    arr = array('i', [])

    n = int(input("enter how many elements:"))

    for i in range(n):
        e = int(input("enter an elemnt:"))
        arr.append(e)

    return arr

def cal(a):

    p = 1
    for i in a:
        p = p*i

    rem = p % len(a)
    return rem


remainder = cal(getdata())

print("Remainder of product of elements in array is {}".format(remainder))

