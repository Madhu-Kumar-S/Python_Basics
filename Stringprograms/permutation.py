# Python | Permutation of a given string using inbuilt function

from itertools import permutations

s = input("enter a string:")

p = tuple(permutations(s))

print(p)

for i in p:
    ps = ''.join(i)
    print(ps)