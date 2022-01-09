import turtle
from turtle import Turtle, Screen

'''
w = forward
a = counter-clockwise
d = clockwise
s = backwards
c = clear drawing
'''

tim = turtle.Turtle()
screen = turtle.Screen()
tim.shape("turtle")

def fw():
    tim.forward(10)
def bw():
    tim.back(10)
def cc():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def cw():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def cls():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim.speed("fast")
screen.listen()
screen.onkeypress(fw, "w")
screen.onkeypress(bw, "s")
screen.onkeypress(cw, "d")
screen.onkeypress(cc, "a")
screen.onkeypress(cls, "space")
screen.exitonclick()
