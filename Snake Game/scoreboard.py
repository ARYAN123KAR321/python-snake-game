import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial",24,"normal"))

    def increse_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        self.score = 0
        self.update_score()