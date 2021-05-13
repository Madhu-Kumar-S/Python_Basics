# Python program to find the sum of all items in a dictionary

d = eval(input("enter a dictionary format:")) #{'a':1,'b':2,'c':3,'d':4,'e':5}

print(d)

print("sum of all items using sum() fun:",sum(d.values()))

j = 0
for i in d.values():
    j = i + j

print("sum of all items using for loop:",j)