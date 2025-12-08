from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong")
        self.screen.tracer(0)

        """ Create Paddle """
        self.p1 = Paddle((-350, 0))
        self.p2 = Paddle((350, 0))
        self.bounced = False

        self.screen.update()

        """ Bind Event Listeners """
        self.screen.listen()
        self.screen.onkey(self.p1.up, 'w')
        self.screen.onkey(self.p1.down, 's')
        self.screen.onkey(self.p2.up, 'Up')
        self.screen.onkey(self.p2.down, 'Down')

        """ Create Scoreboard """
        self.scoreboard = Scoreboard()

        """ Create Ball """
        self.ball = Ball((0, 0))

        self.game_loop()
        self.screen.exitonclick()

    def game_loop(self):
        self.screen.update()
        self.ball.move()

        # Detect Collision with Wall
        if self.ball.ycor() > 280 or self.ball.ycor() < - 280:
            self.ball.bounce_y()

        # Detect Collision with Paddles
        # Right paddle

        if self.ball.distance(self.p2) < 50 and self.ball.xcor() > 320:
            self.ball.bounce_x()
            self.ball.inc_speed()
            self.ball.setx(320)

        # Left paddle
        if self.ball.distance(self.p1) < 50 and self.ball.xcor() < -320:
            self.ball.bounce_x()
            self.ball.inc_speed()
            self.ball.setx(-320)


        # p2 Misses
        if self.ball.xcor() > 380:
            self.ball.bounce_x()
            self.ball.reset_position()
            self.ball.reset_speed()
            self.scoreboard.incr_l()
            self.scoreboard.update_scoreboard()

        # p1 Misses
        if self.ball.xcor() < -380:
            self.ball.bounce_x()
            self.ball.reset_position()
            self.ball.reset_speed()
            self.scoreboard.incr_r()
            self.scoreboard.update_scoreboard()


        self.screen.ontimer(self.game_loop, 30)