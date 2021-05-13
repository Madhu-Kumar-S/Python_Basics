# Python | Get Kth Column of Matrix

from numpy import *

a = array([[1, 2, 3],[4, 5, 6],[7, 8, 9]],int)

print(a)
c  = int(input("enter which column:"))
for i in range(len(a)):
    print(a[i][c-1])


print(a[0:,(c-1):c])