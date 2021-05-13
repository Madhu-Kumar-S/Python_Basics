# Python program to add and sub two Matrices

from numpy import*

r1, c1 = [int(x) for x in input(("enter no of rows and columns:")).split()]

str1 = input("enter matrix elements:\n")

a = reshape(matrix(str1), (r1, c1))

print(a)

r2, c2 = [int(x) for x in input(("enter no of rows and columns:")).split()]

str2 = input("enter matrix elements:\n")

b = reshape(matrix(str2), (r2, c2))

print(b)
print()

if (r1 == r2) and (c1 == c2):
    print("addition of two matrices using operator")
    c = a + b
    print(c)
    print("subtraction of two matrices using operator")
    d = a - b
    print(d)
    print("addition of two matrices using ")
    print(add(a, b))
    print("subtraction of two matrices")
    print(subtract(a, b))
else:
    print("rows and coloumns of both the arrays should be equal for adding two matrices")







