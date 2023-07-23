from turtle import Turtle, Screen
import random

FOOD_SHAPE = "coffee.gif"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.random_x = None
        self.random_z = None
        self.shape(FOOD_SHAPE)
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)  # we want the food object to be smaller than a turtle
        self.penup()
        self.speed("fastest")
        self.reposition()

    def reposition(self):
        self.random_x = random.randint(-260, 260)
        self.random_z = random.randint(-260, 260)
        self.goto(self.random_x, self.random_z)
