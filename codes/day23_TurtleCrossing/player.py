from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.color('black')
        self.setheading(UP)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def check_win(self):
        return FINISH_LINE_Y < self.ycor()
    
    def reset(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()
