from turtle import Turtle

ALLIGNMENT = 'center'
FONT = ("Courier", 40, "normal")
FONT_GAME_OVER = ("Comic Sans", 40, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 245)
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.print_score()
    
    def update_score(self, side):
        if side == 'r':
            self.r_score += 1
        else:
            self.l_score += 1
    
        self.clear()
        self.print_score()
    
    def print_score(self):
        self.write(f"{self.l_score}        {self.r_score}", align=ALLIGNMENT, font=FONT)
