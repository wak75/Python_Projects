from time import sleep
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lscore,align="center",font=("courier",80,"normal"))

        self.goto(100,200)
        self.write(self.rscore,align="center",font=("courier",80,"normal"))
        
    def lpoint(self):
        self.lscore+=1
        self.update_score()
        
    def rpoint(self):
        self.rscore+=1
        self.update_score()