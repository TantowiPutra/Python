from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.l_score = 0
        self.r_score = 0

        # Create Dashed Line
        line = Turtle()
        line.color("red")
        line.penup()
        line.goto(0, -280)
        line.setheading(90)
        line.pendown()
        line.hideturtle()
        line.pensize(5)

        for i in range(10):
            line.forward(30)
            line.penup()
            line.forward(30)
            line.pendown()

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))

    def incr_l(self):
        self.l_score += 1

    def incr_r(self):
        self.r_score += 1