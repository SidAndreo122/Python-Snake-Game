## Day 21 Project
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shape()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # makes the turtle a different size (10 by 10)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.refresh_food()
    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)