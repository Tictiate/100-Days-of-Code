import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(turtle.up, "Up")
screen.onkeypress(turtle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move()

    #Check Level up
    if turtle.ycor() > 280:
        turtle.reset()
        scoreboard.update_score()
        car_manager.level_up()

    #Check Collision
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
