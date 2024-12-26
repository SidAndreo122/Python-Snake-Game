## Day 20 Project

from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game") # creates name on the top of the window
screen.tracer(0) # turns off animations

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() # refreshes animations
    time.sleep(0.1) # slows down refresh
    snake.move()

# TODO 1: Detect Collision with Food.
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()
# TODO 2: Detect Collision with Wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
# TODO 3: Detect Collision with tail.
    for seg in snake.segments: # or [1:]: and remove first if statement
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.reset()



screen.exitonclick()