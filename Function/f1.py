# program on function

def add1(x, y):  # fun definition, here x, y --> formal arguments
    print("Addition of 2 numbers is:", x+y)


a = 2
b = 3
add1(a, b)  # fun call, here a, b --> actual arguments


def add2(a, b):
    return a+b  # fun returning values


result = add2(2, 3)
print("Addition of 2 numbers is:", result)
