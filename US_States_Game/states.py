from turtle import Screen, Turtle
FONT = ("Courier", 12, "normal")


class AddState(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    def set_location(self, x, y):
        self.goto(x, y)

    def write_state(self, state):
        self.write(state)
