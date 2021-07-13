from turtle import Turtle, screensize
ALIGNMENT="center"
FONT=("ROBOTO", 18, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()  
        self.goto(-20,260)    
        self.printscore()
        
    def printscore(self):
        self.write(f"score={self.score}",align=ALIGNMENT,move=False,font=FONT)

    def gameover(self):
        self.clear()
        self.goto(-10,30)
        self.write(f"GAME OVER\nFinal Score={self.score}",align=ALIGNMENT,move=False,font=("Algerian", 18, "normal"))
        
    
    def increse_score(self):
        self.score+=1
        self.clear()
        self.printscore()    