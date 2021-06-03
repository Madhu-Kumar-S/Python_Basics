# pgm to stop overriding the base class constructor and method in subclass

class Father(object):

    def __init__(self, property1=0):
        self.property1 = property1

    def display(self):
        print("Father\'s property =", self.property1)

class Son(Father):

    def __init__(self, property1=0, property2=0):
        super().__init__(property1)
        self.property2 = property2

    def display(self):
        #  super().display() -- to get fathers property too
        print("Son\'s property =", (self.property1 + self.property2))

s = Son(80_00_000.00, 20_00_000.00)
s.display()