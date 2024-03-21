from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-240, 250)
        self.score()
        self.hideturtle()

    def score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)