from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle()
r_paddle.player1()
l_paddle = Paddle()
l_paddle.player2()
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()
        ball.move_speed *= 0.9
    
    #Detect collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        ball.move_speed *= 0.9

    #Detect out of bounds RHS
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

    #Detect out of bounds LHS
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

screen.exitonclick()     