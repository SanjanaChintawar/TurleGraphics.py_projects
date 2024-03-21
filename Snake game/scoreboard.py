from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Score = {self.score}", align="center", font=("Courier", 22, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"   Game Over\n Your score is {self.score}", align="center", font=("Courier", 26, "normal"))
