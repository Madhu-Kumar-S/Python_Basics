# pgm on multiple inheritance to access both the class instance variables(i.e constructors)

class Father(object):

    def __init__(self):
        self.name = "Father"
        print(self.name)
        super().__init__()

class Mother(object):

    def __init__(self):
        self.name = "Mother"
        print(self.name)
        super().__init__()

class Child(Father, Mother):

    def __init__(self):
        self.name = 'Child'
        print(self.name)
        super().__init__()

c = Child()
print(Child.mro())