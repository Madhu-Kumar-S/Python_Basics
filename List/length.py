# Python diff Ways to find length of list
from operator import length_hint

def m1(l):
    print("method 1 using len() fun")
    print(len(l))

def m2(l):
    print("method 2 using Naive mehod")
    counter = 0
    for i in l:
        counter = counter + 1
    print(counter)

def m3(l):
    print("method 3 using length_hint()")
    print(length_hint(l))

l= [1, 2, 3, 4, 5]

print("Diff ways to find length of list:")
m1(l)
m2(l)
m3(l)