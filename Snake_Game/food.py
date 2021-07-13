from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self,):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("lightblue")
        self.shapesize(0.5,0.5)
        self.setpos(random.randint(280,280),random.randint(-280,280))
        self.speed("fastest")

    def refresh(self):
        ranx=random.randint(-280,280)
        rany=random.randint(-280,280)        
        self.setpos(ranx,rany)