# Passing variable to fun as object reference
# note:
# int, float, string, tuple --> immutable objects
# value is not available outside the function
# list, dict --> mutable objects
# value is available outside the function

def modify1(x):
    x = 10
    print(x, id(x))


x = 15
modify1(x)
print(x, id(x))


def modify2(l):
    l[0] = 10
    print(l, id(l))


l = [1, 2, 3, 4, 5]
modify2(l)
print(l, id(l))


def modify3(l):
    l = [6, 7, 8]
    # if we create a new list inside function
    # the list inside function will override and process
    print(l, id(l))


l = [1, 2, 3, 4, 5]
modify3(l)
print(l, id(l))
