
from turtle import Turtle, Screen, shape
import time
from snake1 import Snake
from food import Food
from score import ScoreBoard

screen= Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


gameon=True

while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #food detection and increasing the score
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extendsnake()
        score.increse_score()

    #game over due to wall collsion
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        gameon=False
        score.gameover()

    #gameover due to body collision
    for segment in snake.segment[1:]:
        
        if(snake.head.distance(segment)<10):
            gameon=False
            score.gameover()
        











screen.exitonclick()