from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALLIGNMENT = 'left'
FONT_GAME_OVER = ("Comic Sans", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.goto(-275, 245)
        self.color('black')
        self.hideturtle()
        self.print_score()
        self.game_is_over = False
    
    def update_score(self):
        self.level += 1
        self.clear()
        self.print_score()
    
    def print_score(self):
        self.write(f"Level: {self.level}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=FONT_GAME_OVER)
        self.game_is_over = True
