# python program to show the example of encapsulation

class student:

    def __init__(self):  # to declare and initialize variables (or constructor)
        self.name = "rahul"
        self.age = 21

    def display(self):
        print(self.name)
        print(self.age)

s = student()

s.display()

