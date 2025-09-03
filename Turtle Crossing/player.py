from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape = "turtle"):
        super().__init__(shape)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def down(self):
        self.backward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)