import imp
from turtle import Screen
from Paddle import Paddle
from Ball import Ball
import time
from Scoreboard import Scoreboard

# All turtle starts as 20/20


# Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)
screen.listen()

# Scoreboard
scoreboard = Scoreboard()

# Paddle
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

# Ball
ball = Ball()

# Event Listners
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

# Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(0.1)

# Ball Bounce on wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# To detect collison with the r_paddle amd l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.inc_speed()
        print(ball.speed())

# Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.clear()
        scoreboard.l_point()

# Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.clear()
        scoreboard.r_point()

screen.exitonclick()
