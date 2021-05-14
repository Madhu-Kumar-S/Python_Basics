# K’th Non-repeating Character in Python using List Comprehension and OrderedDict
from collections import *
from operator import itemgetter
s = "geeksforgeeks"

d = OrderedDict.fromkeys(s,0)

for ch in s:
    d[ch] = d[ch] + 1

m = min(d.values())

d = dict(d)

l = [k for k,v in d.items() if v==m]

print("'{}' is the K’th Non-repeating Character".format(l[-1]))

print("............................................................")
print("another way")
dt = dict(Counter(s))
dt = dict(sorted(dt.items(), key=lambda x: x[1]))
m = min(dt.values())
ll = [k for k,v in dt.items() if v == m]
print("'{}' is the K’th Non-repeating Character".format(ll[-1]))
