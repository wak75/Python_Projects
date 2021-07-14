from math import trunc
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    def go_right(self):
        self.right(90)
        self.go_up()
        self.left(90)
        
    def go_left(self):
       self.left(90)
       self.go_up()
       self.right(90)

    def levelup(self):
        if self.ycor()>280:
            return True
        else:
            return False

    def pos_reset(self):
        self.goto(STARTING_POSITION)

   