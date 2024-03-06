from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
score_board = ScoreBoard()
while score_board.game_is_over is False:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.update_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()

screen.exitonclick()
