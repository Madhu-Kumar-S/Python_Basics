a = 1  # global var


def myfun():
    a = 2  # local var
    x = globals()['a']

    print("global var=", x)
    print("local var=", a)


myfun()
print("global var=", a)