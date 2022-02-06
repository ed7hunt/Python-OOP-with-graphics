from turtle import Turtle
FONT = ("Courier", 12, "normal")
FONT2 = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.bad_guesses = 0
        self.color("black")
        self.hideturtle()
        self.penup()

    def update_scoreboard(self, unique_correct_guesses):
        self.clear()
        self.goto(0, 270)
        self.write(f"Correctly Named States: {unique_correct_guesses}", align="center", font=FONT)
        self.goto(0, 250)
        self.write(f"Wrong Guesses: {self.bad_guesses}", align="center", font=FONT)

    def wrong_guess(self):
        self.bad_guesses += 1

    def you_win(self):
        self.goto(0, -270)
        self.write(f"YOU WIN! GOOD JOB!", align="center", font=FONT2)

