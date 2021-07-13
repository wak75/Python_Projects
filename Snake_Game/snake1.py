from turtle import Turtle
import turtle

MOVE_POS=20
STARTPOS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segment=[]
        self.createsnake()
        self.head=self.segment[0]
        self.head.shapesize(1.2,1.2)
    
    def createsnake(self):
        for position in STARTPOS:
            self.add_segment(position)
            

    def add_segment(self,position):
        new_segment=Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)
    
    def extendsnake(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for snake in range(len(self.segment)-1,0,-1):
            newx=self.segment[snake-1].xcor()
            newy=self.segment[snake-1].ycor()
            self.segment[snake].goto(newx,newy)
            '''   similar as 
        for(int i=len(all_sanke)-1;i>=0;i++
        {
            xpos=all_snake[i-1].xcor()//this will give the x coordinates of the second last (i-1)of all the snakes
            ypos=all-snake[i-1].ycor()//y coordinates 
            all_snake[i].goto(xpos,ypos)
        '''

        self.segment[0].forward(MOVE_POS)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)            
        
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
          
    def right(self):
       if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT) 
            
    def left(self):
        if self.head.heading()!=RIGHT:        
            self.head.setheading(LEFT)
            
        

    