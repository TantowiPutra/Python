from turtle import Turtle
import random

class Car(Turtle):
    START_X = 300
    END_X   = -300

    Y_RANGE = [-250 , 290]

    STRETCH_WIDTH = 1
    STRETCH_LEN   = 2

    COLORS = [
        "red", "orange", "yellow", "green", "blue", "purple",
        "pink", "brown", "black"
    ]

    speed      = 10

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.setheading(180)
        self.color(random.choice(self.COLORS))
        self.setpos(( self.START_X, random.randint(self.Y_RANGE[0], self.Y_RANGE[1]) ))
        self.shapesize(stretch_wid=self.STRETCH_WIDTH, stretch_len=self.STRETCH_LEN)

    def is_off_screen(self):
        return self.xcor() <= self.END_X

    def reset_pos(self):
        self.setpos(( self.START_X, random.randint(self.Y_RANGE[0], self.Y_RANGE[1]) ))

    def move_forward(self):
        self.forward(self.speed)

        if self.is_off_screen():
            self.reset_pos()


