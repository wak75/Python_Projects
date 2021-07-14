from turtle import Turtle 
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self,):
        self.all_cars=[]
        self.car_speed=MOVE_INCREMENT

    def create_car(self):
        chance=random.randint(1,6)
        if chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            randomy= random.randint(-250,250)
            new_car.goto(300,randomy)
            self.all_cars.append(new_car)

    def move_cars(self):
        for i in self.all_cars:
            i.backward(self.car_speed)
    
    def speed_up(self):
        self.car_speed+=MOVE_INCREMENT
