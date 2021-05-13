# Python – Convert key-values list to flat dictionary

d = {'month' : [1, 2, 3], 'name' : ['Jan', 'Feb', 'March']}

# using zip() and dict() method
nd = dict(zip(d['name'], d['month']))

print(nd)