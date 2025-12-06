import colorgram
import random
from turtle import Turtle, Screen

colors = colorgram.extract("./painting.jpg", 30)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

screen = Screen()
screen.colormode(255)
screen.screensize(500, 500)

tim = Turtle()

def draw_painting(length):
    tim.penup()
    tim.goto(-300, -250)
    is_flip_dir = False

    for _ in range(length):
        for x in range(length):
            tim.dot(20, random.choice(rgb_colors))
            if x != length - 1:
                tim.forward(50)

        tim.setheading(90)
        tim.forward(50)

        if not is_flip_dir:
            tim.setheading(180)
            is_flip_dir = True
        else:
            tim.setheading(0)
            is_flip_dir = False

draw_painting(13)


# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
#
# for _ in range(10):
#     tim.dot(20, random.choice(rgb_colors))
#     tim.forward(50)
#
# tim.setheading(90)
# tim.forward(50)
# tim.setheading(180)
#
# for _ in range(10):
#     tim.dot(20, random.choice(rgb_colors))
#     tim.forward(50)

screen.exitonclick()