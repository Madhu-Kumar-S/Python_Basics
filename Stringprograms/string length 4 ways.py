# Find length of a string in python (4 ways)
from operator import length_hint

str = input("enter a string:")
print("length of a string")
print("way 1 using len()-fun")
print(len(str))

print("way 2 using counter var")
k = 0
for i in str:
    k = k + 1
print(k)

print("way 3 using length_hint()-fun")
print(length_hint(str))