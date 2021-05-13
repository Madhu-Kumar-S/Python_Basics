# Python Program to find largest  and smallest element in an array

from array import *

arr = array('i',[])

n = int(input("enter how many elements:"))

for i in range(n):
    e = int(input("enter an elemnt:"))
    arr.append(e)

def large(a):
    big = a[0]
    for i in range(1, n):
        if a[i] > big:
            big = a[i]
    return big

def small(a):
    smal = a[0]
    for i in range(1, n):
        if a[i] < smal:
            smal = a[i]
    return smal

print("largest number in array is {}".format(large(arr)))

print("smallest number in array is {}".format(small(arr)))