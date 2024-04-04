from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_dir = 5
        self.y_dir = 5
        self.move_speed = 0.01
    
    def move(self):
        self.goto(self.xcor() + self.x_dir , self.ycor() + self.y_dir)
        
    def bounce(self, coordinate):
        self.move_speed *= 0.1
        if coordinate == 'x':
            self.x_dir *= -1
        elif coordinate == 'y':
            self.y_dir *= -1 
            
    def reset(self):
        self.hideturtle()
        self.goto(0,0)
        self.bounce('x')
        self.showturtle()
        self.move_speed = 0.01
        