from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    level = 0

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.sety(270)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.level}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.sety(0)
        self.write(f"Game Over.", align = ALIGNMENT, font = FONT)