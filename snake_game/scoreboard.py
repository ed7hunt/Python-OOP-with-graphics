from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", move=False, align="center", font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over_hit_wall(self):
        self.goto(0, 0)
        self.write(f"SNAKE HIT WALL\n  GAME OVER!", move=False, align="center", font=FONT)

    def game_over_collided_with_self(self):
        self.goto(0, 0)
        self.write(f"SNAKE HIT TAIL\n  GAME OVER!", move=False, align="center", font=FONT)
