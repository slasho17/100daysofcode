###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

screen = turtle.Screen()
h = 900
w = 900
space_between = 75
dot_size = 25
screen.setup(height=h, width=w)
screen.bgcolor("white")
screen.colormode(255)

t = turtle.Turtle()
t.speed(100)

canvas_width = screen.window_width() // 2
canvas_height = screen.window_height() // 2

t.penup()  # Lift the pen to avoid drawing

for i in range(int (w / space_between) -1):
    t.goto(-canvas_width + space_between, -canvas_height + space_between * (i + 1) )  # Move to the calculated position
    for _ in range(int(h / space_between) - 1):
        t.pendown()
        t.dot(dot_size, random.choice(rgb_colors))
        t.penup()
        t.forward(space_between)

screen.mainloop()