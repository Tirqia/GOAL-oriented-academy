from turtle import *

def draw_stick_figure(x, y):
    penup()
    goto(x, y)
    pendown()
    circle(10)

    right(90)
    forward(30)
    left(45)
    forward(20)
    backward(20)
    right(90)
    forward(20)
    backward(20)
    left(45)
    forward(20)
    backward(20)
    right(45)
    forward(30)
    backward(30)
    left(90)
    forward(30)
    backward(30)


width(10)

draw_stick_figure(0, 0)

exitonclick()