# python pgm to draw a square

import turtle

wn = turtle.Screen()  # to call the window
wn.bgcolor("white")   # to set the bg-color
wn.title("Square")  # to give a title to a window
t = turtle.Turtle()  # to call a turtle
t.shape('turtle')
t.color('blue')
colors = ['red', 'blue', 'green', 'yellow']

for i in range(4):
    t.pencolor(colors[i])
    t.forward(100)
    t.right(90)
turtle.done()