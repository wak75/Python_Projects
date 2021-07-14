from turtle import Turtle, Screen, shapesize
from paddle import Paddle
from ball import Ball
import time
import random
from score import ScoreBoard



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)


r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
score=ScoreBoard()


screen.listen()
screen.onkey(r_paddle.moveup,"Up")
screen.onkey(r_paddle.movedown,"Down")

screen.onkey(l_paddle.moveup,"w")
screen.onkey(l_paddle.movedown,"s")


gameon=True
while gameon:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    #colliosion with the right paddle
    elif (ball.distance(r_paddle)<80 and ball.xcor() > 320) or (ball.distance(l_paddle)<50 and ball.xcor()< -320):
        ball.bounce_x()

    if ball.xcor()>380:
        score.lpoint()
        ball.reset_position()
        
        #gameon=False
    elif ball.xcor()<-380:
        score.rpoint()
        ball.reset_position()
       # gaemon=False
         
    
    
screen.exitonclick()