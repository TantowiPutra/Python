from turtle import Screen, Turtle

class Game:
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

        """ Bind Keys """
        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_down, "Down")
        self.screen.onkey(self.go_left, "Left")
        self.screen.onkey(self.go_right, "Right")

        self.game_loop()

    def init_snake_body(self):
        sb = []

        init_x = 0
        for _ in range(3):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.setx(init_x)
            sb.append(segment)
            init_x -= 20

        return sb

    def move_snake(self):
        for x in range(len(self.segments) - 1, 0, -1):
            next_pos = self.segments[x - 1].position()
            self.segments[x].goto(*next_pos)

        self.segments[0].forward(20)

    def game_loop(self):
        self.move_snake()
        self.screen.update()
        self.screen.ontimer(self.game_loop, 200)

    def go_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def go_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def go_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def go_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

