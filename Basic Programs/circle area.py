# Python Program for Program to find area of a circle
import math as m

def area(r):
    a = m.pi * (m.pow(r, 2))
    print("area of circle is {:.4f} sq.units".format(a))



radius = int(input("enter the radius:"))

area(radius)