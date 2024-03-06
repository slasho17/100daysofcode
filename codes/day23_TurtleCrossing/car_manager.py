from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180

class Car(Turtle):
    def __init__(self, move_speed):
        super().__init__("square")
        self.penup()
        self.goto(300, random.randint(-270, 300))
        self.color(random.choice(COLORS))
        self.setheading(LEFT)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.move_speed = move_speed

    def move(self):
        self.forward(self.move_speed)

class CarManager:
    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.active_cars = []

    def increment_speed(self):
        self.move_speed += MOVE_INCREMENT

    def create_car(self):
        if random.getrandbits(1):
            self.active_cars.append(Car(self.move_speed))