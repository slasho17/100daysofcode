from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
colors = ['red', 'yellow', 'green', 'blue', 'pink']
turtles = []
for t_index in range(len(colors)):
    turtles.append(Turtle(shape='turtle'))
    turtles[t_index].penup()  # Lift the pen to avoid drawing
    turtles[t_index].color(colors[t_index])
    turtles[t_index].goto(-200, (t_index * 100) -200)

guess = screen.textinput(title="Make a bet", prompt="Choose the turtle you think will win, choose between: red, yellow, green, blue, and pink")

points = []
for _ in turtles:
    points.append(0) 


def draw_text_input(text, t, x):
    t.penup()
    t.goto(-100, 0)  # Position the text input
    t.write(text, align="left", font=("Arial", x, "normal"))  # Write the text
x = 0
while True:
    for i, turtle in enumerate(turtles):
        
        if random.getrandbits(1):
            turtle.forward(10)
            points[i] += 1
            if points[i] == 40:
                if turtle.color() == guess:
                    screen.textinput(title="yay", prompt="You win")
                else:
                    x +=5
                    draw_text_input("oh no! you lose", turtle, x)
                    break
                    
screen.mainloop()


                    
