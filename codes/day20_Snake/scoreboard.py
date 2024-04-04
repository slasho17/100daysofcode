from turtle import Turtle

ALLIGNMENT = 'center'
FONT = ("Courier", 24, "normal")
FONT_GAME_OVER = ("Comic Sans", 40, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 265)
        self.color('white')
        self.hideturtle()
        self.print_score()
        self.game_is_over = False
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()
    
    def print_score(self):
        self.write(f"Your score is {self.score}", align=ALLIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALLIGNMENT, font=FONT_GAME_OVER)
        self.game_is_over = True
