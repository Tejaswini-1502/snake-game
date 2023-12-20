from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=280)
        self.color("white")
        self.hideturtle()
        self.display_score()

    def update_score(self):
        self.clear()
        self.score = self.score + 1
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)