import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(600, 500)
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_new_car_maybe()
    car_manager.move_cars()


    if player.ycor() < -250:
        player.go_to_start()

    if player.ycor() > 260:
        scoreboard.score_up()
        player.go_to_start()
        car_manager.increase_car_speed()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()