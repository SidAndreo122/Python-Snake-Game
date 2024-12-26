## Day 21 Project
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as hscore:
            self.highscore = int(hscore.read())
        self.color("white")
        self.penup()
        self.goto(0, 267)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal")) # puts the score message on screen
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 20, "normal"))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as hscore2:
                hscore2.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()


