from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
EXTEND_PERIOD = 300


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_car = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            random_y = random.randint(-250, 250)
            self.add_car((300, random_y))

    def add_car(self, position):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(position)
        self.all_car.append(new_car)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT

    def move(self):
        for car in self.all_car:
            car.backward(self.move_speed)
