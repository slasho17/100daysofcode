import turtle
import pandas as pd
FONT = ("Comic Sans", 10, "normal")

screen = turtle.Screen()

screen.title("US Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("50_states.csv")
states["state"] = states["state"].str.lower()

tur = turtle.Turtle()
tur.penup()
tur.hideturtle()
counter = 0
game_on = True

while game_on:
    answer_state = screen.textinput(title=f"Guess the State ({counter}/50)", prompt="What's another state's name").lower()
    answer = states[states["state"] == answer_state]

    if not answer.empty:
        tur.goto(answer.x.to_list()[0], answer.y.to_list()[0])
        tur.write(f"{answer_state}", align='center', font=FONT)
        counter += 1
        states = states.drop(answer.index[0])
    elif answer_state == 'exit':
        game_on = False
    
    if counter == 50:
        tur.goto(answer.x.to_list()[0], answer.y.to_list()[0])
        tur.write(f"{answer_state}", align='center', font=FONT)
        game_on = False
screen.exitonclick()
