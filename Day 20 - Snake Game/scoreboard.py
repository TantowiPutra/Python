from turtle import Turtle

class Scoreboard(Turtle):
    ALIGNMENT = "center"
    FONT = ('Courier', 24, "bold")

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=self.ALIGNMENT, font=self.FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        # Move to top score should remain visible if you want
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier', 40, 'bold'))

        self.goto(0, -40)
        self.write(f"Your Score: {self.score}", align="center", font=('Courier', 24, 'normal'))
