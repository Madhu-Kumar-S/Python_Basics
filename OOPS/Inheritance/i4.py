# accessing the super class constructor from sub class

class Father(object):

    def __init__(self):
        self.property = 80_00_000.00

    def display(self):
        print("Father\'s property =", self.property)

class Son(Father):

    pass  # since son doesnot have his own property

s = Son()

s.display()

