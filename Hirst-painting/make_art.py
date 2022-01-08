import random
from turtle import Turtle, Screen
import time

palette = [(244, 235, 46), (196, 12, 34), (221, 159, 69), (43, 80, 178), (238, 39, 143), (40, 215, 68), (238, 229, 5), (30, 40, 154), (23, 147, 26), (207, 74, 22), (202, 34, 91), (186, 16, 9), (19, 18, 42), (216, 141, 191), (57, 15, 10), (88, 8, 28), (227, 161, 9), (78, 212, 157), (67, 73, 221), (13, 95, 61), (78, 194, 225), (239, 158, 215), (94, 233, 204), (220, 76, 48), (15, 67, 46), (7, 226, 238)]
my_screen = Screen()
my_circle = Turtle()
my_circle.speed("fastest")
my_circle.shape("circle")
diameter = 20
my_circle.width(diameter)
my_screen.colormode(255)
matrix_size = [10, 10]
screen_width = (matrix_size[0] - 1) * (diameter + 50) + diameter
screen_height = (matrix_size[0] - 1) * (diameter + 50) + diameter
print(f"{screen_height}, {screen_height}")
my_screen.setup(screen_width + 50, screen_height + 100, 0, 0)
my_screen.title(f"Make artwork!")
my_circle.penup()
x_start = int(- (screen_width / 2))
x_done = - x_start
print(f"{x_start}, {x_done}")
y_start = int(- (screen_height / 2))
y_done = - y_start
print(f"{y_start}, {y_done}")
x = 0
for y_step in range(y_start, y_done + 1, int((y_done - y_start) / 9)):
    for x_step in range(x_start, x_done + 1, int((x_done - x_start) / 9)):
        x += 1
        print(x_step, int((x_done - x_start) / 10), x)
        my_circle.setposition(x_step , y_step + diameter)
        random_color = random.choice(palette)
        my_circle.color(random_color)
        my_circle.stamp()

my_screen.title(f"Click screen to exit!")
my_screen.exitonclick()
