from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 28, "normal")
SCREEN_TOP = (0, 270)
SCREEN_CENTRE = (0, 0)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(SCREEN_TOP)
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.display_score()

    def game_over(self):
        self.goto(SCREEN_CENTRE)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
