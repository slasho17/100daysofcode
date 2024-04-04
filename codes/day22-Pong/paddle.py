from turtle import Turtle
UP = 90
DOWN = 270
class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        
        self.penup()
        if side == "left":
            self.goto(-350, 0)
        if side == "right":
            self.goto(350, 0)
            
    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
        