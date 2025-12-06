from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)
    
def move_clockwise():
    tim.right(10)
    
def move_counter_clockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key="s", fun=move_backward)
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()