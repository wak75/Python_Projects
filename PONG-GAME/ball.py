from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(2)
        self.movex=10
        self.movey=10
        self.movespeed=0.1
        
    
    def move(self):
        self.x=self.xcor()+self.movex
        self.y=self.ycor()+self.movey
        self.goto(self.x,self.y)

    def bounce_y(self):
        self.movey*=-1
        self.movespeed*=0.9

    def bounce_x(self):
        self.movex*=-1
        self.movespeed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.movespeed=0.1
        self.bounce_x()
