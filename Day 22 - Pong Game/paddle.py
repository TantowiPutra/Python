from turtle import Turtle

class Paddle(Turtle):
    PADDLE_WIDTH  = 5
    PADDLE_HEIGHT = 1

    def __init__(self, pos):
        super().__init__()

        """ Initialize Paddle """
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid = self.PADDLE_WIDTH, stretch_len = self.PADDLE_HEIGHT)

        self.penup()
        self.goto(pos)

    def up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 30)

    def down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 30)
