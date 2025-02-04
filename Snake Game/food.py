import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shape_size = 0.5
        self.shapesize(self.shape_size, self.shape_size)
        self.speed(0)
        self.refresh()

    def refresh(self):
            random_x=random.randint(-250, 250)
            random_y=random.randint(-250, 250)
            self.goto(random_x, random_y)