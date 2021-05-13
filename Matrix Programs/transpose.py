# Transpose a matrix in Single line in Python

from numpy import *

r, c = [int(x) for x in input("enter rows and columns:").split()]

str = input("enter elements:\n")

a = reshape(matrix(str), (r, c))

print("original matrix is:\n", a)

print("transpose matrix using transpose() method:\n", a.transpose())

print("transpose matrix using getT() method:\n", a.getT())


