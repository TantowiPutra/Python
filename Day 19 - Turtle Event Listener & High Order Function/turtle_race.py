import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

screen.setup(width= 500, height= 400)

total_turtle = int(screen.textinput(title="How many number of turtles? ", prompt="Input turtle amount: "))
user_bet     = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a number: ")

def generate_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def init_turtle(cnt):
    init_pos    = 180
    turtle_list = [Turtle(shape="turtle") for _ in range(cnt)]

    for turtle in turtle_list:
        turtle.color(generate_color())

        turtle.penup()
        turtle.setpos(-230, init_pos)

        init_pos -= 30

    return turtle_list

def start_race(turtle_list):
    is_race_on  = True
    race_finish = 220
    turtle_won  = -1

    while is_race_on:
        is_race_on = False

        for x in range(0, len(turtle_list)):
            turtle_position     = int(turtle_list[x].position()[0])
            new_turtle_position = min(turtle_position + random.randint(0, 10), race_finish)

            turtle_list[x].setx(new_turtle_position)

            if turtle_won == -1 and new_turtle_position == race_finish:
                turtle_won = x

            if new_turtle_position != race_finish:
                is_race_on = True

    return turtle_won

turtle_list = init_turtle(total_turtle)
turtle_won = start_race(turtle_list)
print(f"Turtle {turtle_won + 1} won the race!")
if user_bet == turtle_won:
    print("You win your bet!")
else:
    print("You lost your bet!")

screen.exitonclick()