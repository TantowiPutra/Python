from turtle import Turtle

class Player(Turtle):
    START_POS = (0, -280)
    END_POS   = (0, 280)

    def __init__(self):
        super().__init__()

        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.setpos(self.START_POS)

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        if self.distance(self.START_POS) > 0:
            self.forward(-10)

    def is_crossed(self):
        if self.ycor() >= self.END_POS[1]:
            return True

        return False

    def reset_position(self):
        self.setpos(self.START_POS)