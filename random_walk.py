import random
from turtle import Turtle, Screen


def change_color():
    random_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    return random_color

my_screen = Screen()
my_screen.colormode(255)
my_screen.setup(1000, 800, 0, 0)
print(my_screen.canvwidth)
timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.width(20)
timmy.speed(0)

while True:
    direction = random.randrange(0, 270, 90)
    timmy.right(direction)
    timmy.color(change_color())
    timmy.forward(20)

my_screen.exitonclick()

