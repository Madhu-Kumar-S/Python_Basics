# Python program to multiply two matrices

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

if c1 == r2:
    print("multiplication of two matrices is")
    print("method 1 using operator")
    c = a * b
    print(c)
    print()
    print("method 2 using dot fun")
    r = dot(a,b)
    print(r)
else:
    print("multiplication not posible due as r1!=c2")



