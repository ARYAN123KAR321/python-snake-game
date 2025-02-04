# snake.py
from turtle import Turtle

class Snake:
    def __init__(self):
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        self.head.setheading(0)
        self.game_over_turtle = Turtle()
        self.game_over_turtle.hideturtle()
        self.game_over_turtle.color("white")
        self.game_over_turtle.penup()

    def create_snake(self):
        for p in self.position:
            self.create_block(p)

    def create_block(self, p):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(p)
        self.turtles.append(t)

    def extend(self):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        self.turtles.append(new_block)
        new_block.goto(self.turtles[-2].position())
        


    def move(self):
        for t_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[t_num - 1].xcor()
            new_y = self.turtles[t_num - 1].ycor()
            self.turtles[t_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for t in self.turtles:
            t.goto(1000, 1000)
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        self.head.setheading(0)
        self.game_over_turtle = Turtle()
        self.game_over_turtle.hideturtle()
        self.game_over_turtle.color("white")
        self.game_over_turtle.penup()

    def game_over(self):
        self.game_over_turtle.goto(0, 0)
        self.game_over_turtle.write("GAME OVER", align="center", font=("Arial", 24, "normal"))