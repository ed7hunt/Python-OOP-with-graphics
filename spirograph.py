import random
import time
from turtle import Turtle, Screen


def change_color():
    new_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    return new_color


my_screen = Screen()
timmy = Turtle()
timmy.speed("fastest")


def draw_spirograph(gap, num_cir):
    for _ in range(num_cir):
        timmy.color(change_color())
        timmy.circle(100)
        timmy.right(gap)


for count in range(10, 0, -1):
    my_screen.colormode(255)
    number_of_circles = int(360 / count)
    my_screen.title(f"Spirograph gap = {count}º. Number of circles = {number_of_circles}.")
    draw_spirograph(count, number_of_circles)
    time.sleep(1)
    my_screen.clear()

my_screen.title(f"Click screen to exit!")
my_screen.exitonclick()
