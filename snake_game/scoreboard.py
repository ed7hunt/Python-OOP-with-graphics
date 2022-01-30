from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("high_score.txt") as file:
                self.high_score = int(file.read())
                file.close()
        except FileNotFoundError:
            self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}      High Score: {self.high_score}", move=False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
                file.close()
        self.score = 0
        self.update_scoreboard()

    def increment(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



    def game_over_collided_with_self(self):
        self.goto(0, 0)
        self.write(f"SNAKE HIT TAIL\n  GAME OVER!", move=False, align="center", font=FONT)
