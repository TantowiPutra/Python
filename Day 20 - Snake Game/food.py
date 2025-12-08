from turtle import Turtle
from random import choice

class Food(Turtle):
    RAND_POS = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.goto(choice(self.RAND_POS), choice(self.RAND_POS))

    def refresh(self):
        random_x = choice(self.RAND_POS)
        random_y = choice(self.RAND_POS)

        self.goto(random_x, random_y)