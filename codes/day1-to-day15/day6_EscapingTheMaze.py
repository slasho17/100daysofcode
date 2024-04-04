# this is a code to complete the challenge in https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Finding the first wall and making sure it is in our right
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    
    elif right_is_clear():
        turn_right()
        move()
        
    else:
        turn_left()
    