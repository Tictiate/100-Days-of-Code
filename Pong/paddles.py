from turtle import Turtle

XCOR = 350

class Paddle(Turtle):
    def __init__(self, shape = "square"):
        super().__init__(shape)
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def player1(self):
        self.teleport(XCOR,0)

    def player2(self):
        self.teleport(-XCOR,0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)