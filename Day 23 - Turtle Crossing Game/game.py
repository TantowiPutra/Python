import random
from turtle     import Screen
from player     import Player
from car        import Car
from scoreboard import Scoreboard

class Game:
    level         = 1
    cars          = []
    max_car_count = 10
    speed         = 100

    def __init__(self):
        """ Init Screen """
        self.screen = Screen();
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.screen.listen()

        """ Init Player """
        self.player = Player()
        self.screen.onkey(self.player.move_forward, "Up")
        self.screen.onkey(self.player.move_backward, "Down")

        """ Init Scoreboard """
        self.scoreboard = Scoreboard()

        """ Init Car """
        self.spawn_car()

        self.game_loop()
        self.screen.update()
        self.screen.exitonclick()

    def game_loop(self):
        """ Update Car Position """
        for car in self.cars:
            car.move_forward()

        """ Detect Collision """
        for car in self.cars:
            if car.distance(self.player) < 20:
                self.scoreboard.game_over()
                return

        """ Successful Crossing """
        if self.player.is_crossed():
            self.level_up()

        self.screen.update()
        self.screen.ontimer(self.game_loop, self.speed)

    def level_up(self):
        self.player.reset_position()
        self.level += 1

        if self.level > 5:
            self.cars.append(Car())
        else:
            self.speed -= 20

        self.scoreboard.update_score()

    def spawn_car(self):
        if len(self.cars) < self.max_car_count:
            self.cars.append(Car())
        else:
            return

        delay = random.randint(300, 1200)
        self.screen.ontimer(self.spawn_car, delay)