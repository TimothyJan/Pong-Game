
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WINNING_SCORE = 3

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")   
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

paddle_hit = 0
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    """Detect collision with wall"""
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    """Is ball in playing zone or paddle zone"""
    if paddle_hit == 0:
        """Detect collision with right/left paddle"""
        if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
            ball.bounce_x()
            paddle_hit = 1
    else:
        if -320 < ball.xcor() < 320:
            paddle_hit = 0
    
    """Detect when right paddle misses"""
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    
    """Detect when left paddle misses"""
    if ball.xcor()<-380:
        ball.reset_position()   
        scoreboard.r_point()
    
    """Game Over"""
    if scoreboard.l_score == WINNING_SCORE or scoreboard.r_score == WINNING_SCORE:
        game_is_on = False
        if scoreboard.l_score == WINNING_SCORE:
            winning_side = "Left"
        else:
            winning_side = "Right"
        scoreboard.game_over(winner=winning_side)

screen.exitonclick()