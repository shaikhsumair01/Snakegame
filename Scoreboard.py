from turtle import Turtle
alignment = "center"
text = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score : {self.score}", align= alignment, font= text)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=alignment, font=text)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
