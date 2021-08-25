import re

print("Hi\nEveryone...")
print(r"Hi\nEveryone...")  # r-->raw string
print("............................................")

print("Regular Expression")
# step 1: developing regular expression(re)
regex = r'm\w\w'
# r'b\w\w'-->string/regex
# step 2: compiling re
# m-->starting word starting with m should be matched
# \w-->anyone char in A to Z, a to z, 0 to 9
# we are writing two \w and it represents any two char after m
# so the above string represents words r strings having 3 char starting with m
prog = re.compile(regex)
# prog-->object that contains the re
s = 'cat mat bat rat'
# step 3: run re on the string s using search() or match() method
res = prog.search(s)
print(res.group())  # o/p=mat

print("...........................................")

# for searching once
# using search() method
ns = '1 2 3 4 5'
res = re.search(r'2', ns)
print(res.group())

# for searching many times
ns = 'man mob cat pat'
res = re.findall(r'm\w\w',ns)
print(res)


