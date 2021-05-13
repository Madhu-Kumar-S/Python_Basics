# Ways to sort list of dictionaries by values in Python
from operator import itemgetter
# using itemgetter()-fun
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 21 },
{ "name" : "Nikhil" , "age" : 19 }]

print("sorting by age:")
print(sorted(lis, key=itemgetter('age')))

# using lambda fun

print(sorted(lis, key=lambda x: x['age']))
print(sorted(lis, key=lambda x: x['name']))
print(sorted(lis, key=lambda x: x['age'],reverse=True))
