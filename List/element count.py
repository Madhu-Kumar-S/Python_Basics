# Python | Count occurrences of an element in a list

l = [1, 2, 3, 2, 2, 4, 5]
print("list is ", l)

e = int(input("enter an elemnt to count its occurances:"))

c = 0

for i in l:
    if e == i:
        c = c + 1

print("element {} has occured {} times in list".format(e, c))