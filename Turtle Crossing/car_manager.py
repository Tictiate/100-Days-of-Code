from turtle import Turtle
import random
import math

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.upper_bound = 6

    def create_car(self):
        random_choice = random.randint(1, math.floor(self.upper_bound))
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250,250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        self.upper_bound *= 0.9

