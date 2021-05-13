# Handling missing keys in Python dictionaries
from collections import defaultdict as dd
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

print(country_code.get('India','Not found')) # if key is found
print(country_code.get('China','Not found')) # if key is not found

# Set a default value for Japan
country_code.setdefault('Japan', 'Not Present')
# search dictionary for country code of India
print(country_code['India'])
# search dictionary for country code of Japan
print(country_code['Japan'])

d = dd(lambda : 'key not found')
d['a'] = 1
d['b'] = 2
print(dict(d))
print(d['c'])