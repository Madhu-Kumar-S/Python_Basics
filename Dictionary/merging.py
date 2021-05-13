# Python | Merging two Dictionaries

d1 = {1:'a', 2:'b'}

d2 = {3:'c', 4:'d', 5:'e'}

# using update()-fun
d1.update(d2)
print(d1)

# using **-kwargs
d = {**d1, **d2}
print(d)