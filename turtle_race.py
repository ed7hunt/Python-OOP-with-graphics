import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=500)

all_turtles = []
y = -100
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y)
    all_turtles.append(new_turtle)
    y += 50

answer = screen.textinput(title="Turtle Race", prompt="Which turtle do you think will win? ")
if answer:
    is_race_on = True

while is_race_on:
    for each_turtle in all_turtles:
        spaces = random.randint(0, 10)
        each_turtle.forward(spaces)
        if each_turtle.xcor() >= 230:
            winner = list(each_turtle.color())[0]
            if answer == winner:
                print(f"YOU WIN! The winner is {winner}.")
            else:
                print(f"YOU LOSE! The winner is {winner}.")
            is_race_on = False

screen.exitonclick()
