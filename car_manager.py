from turtle import Turtle
import random


COLORS = ["red", "blue", "orange"]


class CarManager:

    def __init__(self):

        self.all_cars = []
        self.car_speed = 5

    def create_new_car_maybe(self):
        dice = random.randint(1, 6)
        random_y = random.randint(-200, 200)
        if dice == 6:
            self.car = Turtle("square")
            self.car.penup()
            self.car.shapesize(stretch_len=2, stretch_wid=1)
            self.car.color("black", random.choice(COLORS))
            self.car.goto(280, random_y)
            self.all_cars.append(self.car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += 3