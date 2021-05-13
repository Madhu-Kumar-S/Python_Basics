# Python | Ways to remove a key from dictionary

d = eval(input("enter a dictionary:")) #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print("available keys are:",[i for i in d.keys()])
k = input("enter which key to remove:")

#removing key-value using pop fun
d1 = d.copy()
d1.pop(k)
print(d1)

# removing k-v using del
d2 = d.copy()
del d2[k]
print(d2)

# using dictionary comphrehension
d3 = d.copy()
res = {key:value for key,value in d3.items() if key != k}
print(res)