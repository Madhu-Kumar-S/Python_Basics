# local and global variables
a = 10  # global variable


def display():
    global a  # to access global var inside fun
    print("value of global var a inside function:", a)
    a = 20  # modify global var
    print("value of local var a inside function:", a)


print("value of a outside the function before modifying:", a)
display()
print("value of a outside the function after declaring global inside fun:", a)
