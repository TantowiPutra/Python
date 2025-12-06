import turtle
from turtle import Turtle, Screen

timy_the_turtle = Turtle()
screen = Screen()

turtle.colormode(255)
timy_the_turtle.shape("turtle")
timy_the_turtle.color(255, 105, 180)

""" Square """
# for i in range(4):
#     timy_the_turtle.forward(100)
#     timy_the_turtle.right(90)

""" Dashed Line """
# for i in range(10):
#     timy_the_turtle.forward(10)
#     timy_the_turtle.penup()
#     timy_the_turtle.forward(10)
#     timy_the_turtle.pendown()

""" Square """
# for i in range(4):
#     timy_the_turtle.forward(100)
#     angle = 360 / 4
#     timy_the_turtle.right(angle)

""" Pentagon """
# for i in range(5):
#     angle = 360 / 5
#     timy_the_turtle.forward(100)
#     timy_the_turtle.right(angle)

# def draw_shapes(sides):
#     for i in range(sides):
#         angle = 360 / sides
#         timy_the_turtle.forward(100)
#         timy_the_turtle.right(angle)
#
# for i in range(3, 12):
#     draw_shapes(i)

import random

""" Random Walk """
def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

timy_the_turtle.speed("fastest")
# timy_the_turtle.pensize(10)

# for _ in range(500):
#     timy_the_turtle.color(random_color())
#     timy_the_turtle.forward(30)
#     timy_the_turtle.setheading(random.choice(directions))

# Spirograph
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timy_the_turtle.color(random_color())
        timy_the_turtle.circle(100)
        current_heading = timy_the_turtle.heading()
        timy_the_turtle.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen.exitonclick()