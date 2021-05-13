# Ways to remove i’th character from string in Python

print("diff ways to remove ith char from given string")

st = input("enter a string:")

r = input("enter the character which need to be removed:")

print("method 1")
l = []
l.append(st[:st.find(r)])
l.append(st[((st.find(r))+1):])
ns = ''.join(l)
print("after removing {:s} from the string {:s} is {:s}".format(r, st, ns))

print("method 2")
l1 = []
for i in st:
    l1.append(i)
if r in l1:
    l1.remove(r)
ns1 = ''.join(l1)
print("after removing {:s} from the string {:s} is {:s}".format(r, st, ns1))

print("method 3")
ns2 = st[:st.find(r)]+st[((st.find(r))+1):]
print("after removing {:s} from the string {:s} is {:s}".format(r, st, ns2))

print("method 4")
ns3 = st.replace(r, '', st.find(r))
print("after removing {:s} from the string {:s} is {:s}".format(r, st, ns3))