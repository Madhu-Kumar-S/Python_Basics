import numpy as np

r1, c1 = [int(x) for x in input("enter the row and columns of 1st matrix:").split()]
s1 = input("enter elements:")
m1 = np.reshape(np.matrix(s1), (r1, c1))
print(m1)

r2, c2 = [int(x) for x in input("enter the row and columns 2nd matrix:").split()]
s2 = input("enter elements:")
m2 = np.reshape(np.matrix(s2), (r2, c2))
print(m2)

print()
if r1 == r1 and c1 == c2:
    print("addition is:")
    print(m1+m2)
    print("subtraction is:")
    print(m1-m2)
    print("division is:")
    print(m1//m2)

if c1 == r2:
    print("multiplication is:")
    print(m1*m2)
