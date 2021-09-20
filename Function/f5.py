# Actual arguments used in a fun are four types

# 1 positional arguments
# these are the arguments passed into a fun in correct positional order
# hence the no of arguments & their positions in the function definition should match exactly


def add(a, b):
    print("addtion is:", a+b)


add(2, 3)

# 2 keyword arguments
# arguments identify the parameter by their names
# can be of any order


def sub(a, b):
    print("subtraction is:", a-b)


sub(b=2, a=3)

# 3 default arguments
# these are the arguments present in the fun definition
# if they didn't receive any parameters then default values will be taken
# but non-default parameter should follow default parameter


def mul(a, b=3):
    print("multiplication is:", a*b)


mul(2, 4)
mul(2)

# 4 variable length arguments
# can accept any no of values at a time
# declare * before the formal parameter in fun definition


def sum_n(*args):
    s = 0
    for i in args:
        s = s + i
    print("Sum is:", s)


sum_n(1, 2)
sum_n(1, 2, 3)
sum_n(1, 2, 3, 4)
sum_n(1, 2, 3, 4, 5)

# keyword variable length args
# accepts any no of values but in form of key, value pairs
# declare ** before the formal parameter in fun definition


def display(**kwargs):
    for i, j in kwargs.items():
        print("key={} value={}".format(i, j))


display(name="Avatar", age=21, gender="male")


