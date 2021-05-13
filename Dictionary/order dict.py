# Python – Insertion at the beginning in OrderedDict

from collections import OrderedDict as od

d = od({1:'a', 2:'b', 3:'c', 4:'....'})
d1 = d.copy()
ad = od({0:'null'})

# Method #1: Using OrderedDict.move_to_end()
d.update(ad)
d.move_to_end(0,last=False)
print(dict(d))
# Method #2: Using Naive Approach
print(od(list(ad.items()) + list(d1.items())))
print(dict(od(list(ad.items()) + list(d1.items()))))
