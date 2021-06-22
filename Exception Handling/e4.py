def add(a,b):
    print('sum =', a+b)

def div(a,b):
    print('Division =', a//b)

try:
    a, b = [int(i) for i in input("enter value of a and b:").split()]
    add(a, b)
    div(a, b)
except ValueError as v:
    print('error =', v)
    print('please enter integer value.')
except ZeroDivisionError as z:
    print('error =', z)
    print('please enter non zero value.')

