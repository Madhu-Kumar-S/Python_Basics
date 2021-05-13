# Python Program to check if given array is Monotonic

from array import *

print("Method 1")

def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

A = array('i', [6, 5, 4, 4])

print("monotonic condition of an given array is {}".format(isMonotonic(A)))

print("Method 2")

c1 = []
c2 = []

for i in range(len(A)-1):
    c1.append(A[i] >= A[i + 1])
    c2.append(A[i] <= A[i + 1])

print("monotonic condition of an given array is {}".format(all(c1) or all(c2)))