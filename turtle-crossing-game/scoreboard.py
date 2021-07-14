from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.current_level=1

        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-230,260)
        self.write(f"Level: {self.current_level}",align="center", font=FONT)

    def incre_level(self):
        self.clear()
        self.current_level+=1
        self.write(f"Level: {self.current_level}",align="center", font=FONT)

    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Max Level: {self.current_level}\n GAME OVER",align="center", font=FONT)
        