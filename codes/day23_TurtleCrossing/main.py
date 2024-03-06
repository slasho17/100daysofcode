import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

while not score.game_is_over:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    if player.check_win():
        score.update_score()
        player.reset()
        car_manager.increment_speed()
    for car in car_manager.active_cars:
        if player.distance(car) < 20:
            score.game_over()
        car.move()
        
screen.exitonclick()

