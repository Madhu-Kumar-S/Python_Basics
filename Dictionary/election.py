# Dictionary and counter in Python to find winner of election
from collections import Counter

def winner(i):
    d =dict(Counter(i))
    m = max(d.values())
    l = [ i for i,j in d.items() if j == m ]
    print(l[0],"has won the election!")

input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']
winner(input)