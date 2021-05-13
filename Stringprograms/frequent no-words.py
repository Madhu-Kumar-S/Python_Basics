#Python – Words Frequency in String Shorthands
from collections import Counter

st = input("enter a string:")

print("original string is: ",st)

print("method 1")

d = {key:st.count(key) for key in st.split()}

print(d)

print("method 2")

res = Counter(st.split())

print(dict(res))