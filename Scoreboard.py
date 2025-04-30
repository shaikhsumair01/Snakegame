from turtle import Turtle
alignment = "center"
text = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        with open("data.txt", mode = "r") as file:
            previous_score = file.read()
        self.highscore = int(previous_score)
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}, HighScore : {self.highscore}", align= alignment, font= text)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode = "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score+=1

        self.update_score()
