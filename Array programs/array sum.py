# Python Program to find the sum of array

from array import *

arr = array('i',[])

n = int(input("enter how many elements:"))

for i in range(n):
    e = int(input("enter an elemnt:"))
    arr.append(e)

def sum_arr(a):
    print("sum = {}".format(sum(a)))

sum_arr(arr)