import colorgram
from turtle import Turtle, Screen
import time

colors = colorgram.extract("download.jpg", 30)
print(colors)
palette = []
for each_color in colors:
    red = each_color.rgb.r
    green = each_color.rgb.g
    blue = each_color.rgb.b
    color_tuple = (red, green, blue)
    print(color_tuple)
    palette.append(color_tuple)

my_screen = Screen()
my_circle = Turtle()
my_circle.shape("circle")
my_circle.shapesize(100)
my_screen.colormode(255)
final_palette = []
for sample in palette:
    my_screen.title(f"Sample = {sample}")
    my_circle.color(sample)
    answer = input("Keep color Y/N? ").lower()
    if answer == "y":
        final_palette.append(sample)
    time.sleep(1)

print(final_palette)


