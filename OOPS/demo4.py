# python program - an example of Inheritance

class A:

    def __init__(self):

        self.x = 10
        self.y = 20

    def display(self):

        print(self.x)
        print(self.y)

class B(A):

    def __init__(self):
        self.z = 30

    def display(self):
        a = A()
        a.display()
        print(self.z)

b = B()

b.display()


