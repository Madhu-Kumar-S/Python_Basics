# python pgm to draw a star

import turtle

wn = turtle.Screen()  # to call the window
wn.bgcolor("white")   # to set the bg-color
wn.title("Star")  # to give a title to a window
t = turtle.Turtle()  # to call a turtle
colors = ['red', 'blue', 'green', 'yellow', 'red']

for i in range(5):
    t.pencolor(colors[i])
    t.forward(100)
    t.right(144)

turtle.done()