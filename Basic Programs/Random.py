# python program to generate random password
import random

n = '1234567890'

s = '!@#$&?'

lca = 'abcdefghijklmnopqrstuvwxyz'

uca = lca.upper()

all = n + s + lca + uca

l = 10

pwd = ''.join(random.sample(all, l))

print("random password is =",pwd)