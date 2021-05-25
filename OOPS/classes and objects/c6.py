# Python program on Static methods
from math import sqrt

class Myclass:

    counter = 0  # class or static variable

    def __init__(self):

        Myclass.counter = Myclass.counter + 1

    @staticmethod  # static method
    def display():

        print("no of instances created is {:d}".format(Myclass.counter))

for i in range(3):
    m = Myclass()

Myclass.display()

print("..............................................")

# program to find square root value of a given number

class demo:

    @staticmethod
    def sqr(value):
        result = int(sqrt(value))
        return result

value = int(input("enter a value:"))
print("Square root value of {:d} is {:d}".format(value, demo.sqr(value)))


