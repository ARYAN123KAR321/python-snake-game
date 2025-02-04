# main.py
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game.")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.reset, "r")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increse_score()
        snake.extend()

    # detect collision with wall
    if (snake.head.xcor() > 280 or
            snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or
            snake.head.ycor() < -280):
        score.reset()
        snake.game_over()
        game_is_on=False

    #detect collision with own tail
    for block in snake.turtles[1:]:
        if snake.head.distance(block) < 10:
            score.reset()
            snake.game_over()

screen.mainloop()