from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My pong game")
l_paddle = Paddle("left")
r_paddle = Paddle("right")
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

score = ScoreBoard()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.xcor() > 380:
        ball.reset()
        score.update_score('l')
    
    if ball.xcor() < -380:
        ball.reset()
        score.update_score('r')
    
    if (ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50) and (ball.xcor() > 320 or ball.xcor() < -320 ):
        ball.bounce('x')
        
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')
        


screen.exitonclick()
