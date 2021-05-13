# Sort the values of first list using second list in Python
import plistlib

l1 = ['e', 'd', 'c', 'b', 'a']
l2 = [5, 4, 3, 2, 1]

print("l1 = ",l1)
print("l2 = ",l2)

d = dict(zip(l1, l2))

nd = sorted(d.items(), key=lambda x: x[1])

sd = dict(nd)
print("Sorted values of first list using second list:")
ll1 = list(sd.keys())
print("l1 = ",ll1)
ll2 = list(sd.values())
print("l2 = ",ll2)
