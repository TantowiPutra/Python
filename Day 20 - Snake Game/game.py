from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
import time

class Game:
    MOVE_DISTANCE = 20
    SEGMENT_SIZE  = 1

    def __init__(self):
        """ Set Screen """
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.listen()
        self.screen.tracer(0)

        """ Set Snake Body """
        self.segments = self.init_snake_body()
        self.head     = self.segments[0]
        self.tail     = self.segments[2]

        """ Bind Keys """
        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_down, "Down")
        self.screen.onkey(self.go_left, "Left")
        self.screen.onkey(self.go_right, "Right")

        """ Initialize Food """
        self.food = Food()

        """ Initialize Scoreboard """
        self.scoreboard = Scoreboard()

        self.game_loop()

    def create_segment(self):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.shapesize(stretch_wid=self.SEGMENT_SIZE, stretch_len=self.SEGMENT_SIZE)

        return segment

    def init_snake_body(self):
        sb = []

        init_x = 0
        for _ in range(3):
            segment = self.create_segment()
            segment.setx(init_x)
            sb.append(segment)

            init_x -= 20

        return sb

    def increase_length(self):
        new_segment = self.create_segment()

        new_segment.goto(self.tail.position())
        self.tail = new_segment

        self.segments.append(new_segment)

    def move_snake(self):
        for x in range(len(self.segments) - 1, 0, -1):
            next_pos = self.segments[x - 1].position()
            self.segments[x].goto(*next_pos)

        self.head.forward(self.MOVE_DISTANCE)

    def wrap_snake(self):
        x, y = self.head.xcor(), self.head.ycor()

        if x < -300:
            self.head.setx(300)
        elif x > 300:
            self.head.setx(-300)

        if y < -300:
            self.head.sety(300)
        elif y > 300:
            self.head.sety(-300)

    def game_loop(self):
        is_game_over = False
        self.wrap_snake()
        self.move_snake()

        """ Detect Collision With Food """
        if self.head.distance(self.food) < 10:
            self.food.refresh()
            self.scoreboard.increase_score()
            self.increase_length()

        self.screen.update()

        """ Detect Collision With Tail """
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                self.scoreboard.game_over()
                is_game_over = True

        if is_game_over:
            return

        self.screen.ontimer(self.game_loop, 100)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

