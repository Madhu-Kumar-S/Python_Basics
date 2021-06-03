# pgm to access super class constructor and method in sub class

class Square(object):

    def __init__(self, x):
        self.x = x

    def area(self):
        print("Area of square =", (self.x * self.x))

class Reactangle(Square):

    def __init__(self, x, y):
        super().__init__(x)
        self.x = x
        self.y = y

    def area(self):
        super().area()
        print("Area of rectangle =", (self.x * self.y))

a, b = [float(x) for x in input("Enter length and breadth:").split()]
r = Reactangle(a, b)
r.area()