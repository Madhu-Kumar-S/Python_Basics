# Function are first class objects

# Assigning a function to a variable


def fun1():
    return "Hello World!"


result = fun1()
print(result)

# Define one function inside another function


def fun2():
    var = "Welcome..."

    def sub_fun2():
        return " to Python programming."
    return var + sub_fun2()


print(fun2())

# Passing a function as a parameter to another function


def fun3():
    return "Dog"


def fun4(a):
    return a + " is more loyal towards its owner."


print(fun4(fun3()))

# function returning another function


def fun5():
    def sub_fun5():
        return "Bye...C u all."
    return sub_fun5


res = fun5()
print(res())
