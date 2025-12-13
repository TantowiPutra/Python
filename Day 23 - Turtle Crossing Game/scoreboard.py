from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, level = 0):
        super().__init__()
        self.color("black")
        self.penup()
        self.level = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()

        self.level += 1

        self.goto(0, 250)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 30, "bold"))

    def game_over(self):

        self.clear()
        self.goto(0, 250)
        self.write(f"Game Over...", align="center", font=("Courier", 30, "bold"))