from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor) :
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(5.0,1.0,1)
        self.penup()
        self.goto(xcor,ycor)


    def moveup(self):
        newy =self.ycor()+20
        self.goto(self.xcor(),newy)

    def movedown(self):
        newy =self.ycor()-20
        self.goto(self.xcor(),newy)