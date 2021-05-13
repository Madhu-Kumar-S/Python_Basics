# Python | Sort Python Dictionaries by Key or Value

d = {'a':5, 'c':4, 'b':3, 'd':2}

print(dict(sorted(d.items(), key=lambda x: x[0])))# sorting according to keys
print(dict(sorted(d.items(), key=lambda x: x[1])))# sorting according to values
print(dict(sorted(d.items(), key=lambda x: x[0], reverse=True)))

d = {"Nandini": 20, "Manjeet": 21, "Nikhil": 19}
print(dict(sorted(d.items(), key=lambda x: x[0])))
print(dict(sorted(d.items(), key=lambda x: x[1])))
print(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))