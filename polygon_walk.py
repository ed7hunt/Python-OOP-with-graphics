import random
from turtle import Turtle, Screen


def change_color():
    return random.randint(1, 256), random.randint(1, 256), random.randint(1, 256)


my_screen = Screen()
my_screen.colormode(255)
print(my_screen.canvwidth)
timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.color("black")

for polygon in range(3, 11):
    timmy.color(change_color())
    for x in range(polygon):
        timmy.right(360 / polygon)
        timmy.forward(70)

my_screen.exitonclick()
