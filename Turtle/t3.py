# python pgm to draw a hexagon

import turtle

wd = turtle.Screen()
wd.bgcolor("white")
wd.title("Hexogon")

t = turtle.Turtle()

colors = ['red', 'blue', 'green', 'yellow', 'red', 'blue']

for i in range(6):
    t.pencolor(colors[i])
    t.forward(100)
    t.right(60)

turtle.done()