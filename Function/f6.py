# local and global variables
a = 10  # global variable


def display():
    a = 20  # local variable
    print("value of a inside function:", a)


display()
print("value of a outside the function:", a)