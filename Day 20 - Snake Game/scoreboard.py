from turtle import Turtle

class Scoreboard(Turtle):
    ALIGNMENT = "center"
    FONT = ('Courier', 24, "bold")

    def __init__(self):
        super().__init__()

        with open("./data.txt") as file:
            prev_high_score = file.read()
            self.high_score = int(prev_high_score)

        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=self.ALIGNMENT, font=self.FONT)

    def increase_score(self):
        self.score += 1
        self.is_new_high()
        self.update_scoreboard()

    def is_new_high(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as file:
                file.write(str(self.high_score))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier', 40, 'bold'))

        self.goto(0, -40)
        self.write(f"Your Score: {self.score}", align="center", font=('Courier', 24, 'normal'))
