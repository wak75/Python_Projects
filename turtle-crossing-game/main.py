import time
from turtle import Screen, goto
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car = CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")
screen.onkey(player.go_right,"Right")
screen.onkey(player.go_left,"Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    #car collision
    for cars in car.all_cars:
        if cars.distance(player)<20:
            game_is_on=False
            score.gameover()

    #turtle crossed
    if player.levelup():
        player.pos_reset()
        car.speed_up()
        score.incre_level()

screen.exitonclick()