# Python – Extract Unique values dictionary values

d = {'a': [1, 2, 9], 'b': [4, 5, 6],'c': [7, 8, 3]}

# using concatination
print(sorted(d['a'] + d['b'] + d['c']))

# using list comprehension

res = sorted(j for i in d.values() for j in i)

print(res)