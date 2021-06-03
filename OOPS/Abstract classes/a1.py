# pgm to create abstract class and sub classes which implement the abstract method of the abstarct class
import math
from abc import ABC, abstractmethod
import math

class Abstract(ABC):

    @abstractmethod
    def calculate(self):
        pass

class Square(Abstract):

    def calculate(self, x):
        print("Square of {:.2f} is {:.2f}".format(x, math.pow(x, 2)))

class Cube(Abstract):

    def calculate(self, x):
        print("Cube of {:.2f} is {:.2f}".format(x, math.pow(x, 3)))

class Sqrt(Abstract):

    def calculate(self, x):
        print("Square of {:.2f} is {:.2f}".format(x, math.sqrt(x)))

s = Square()
s.calculate(2)
c = Cube()
c.calculate(3)
sq = Sqrt()
sq.calculate(4)