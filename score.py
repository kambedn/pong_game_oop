from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 40, 'bold')
HEIGHT = 240
WINNING_SCORE = 1


class Score(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x_pos, HEIGHT)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def is_winner(self):
        return self.score == WINNING_SCORE


class HalfLine(Turtle):
    def __init__(self, y):
        super().__init__()
        self.shape("square")
        self.turtlesize(0.8, 0.2, 2)
        self.penup()
        self.goto(0, y)
        self.color("white")
        self.speed("fastest")


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")

    def write_game_over(self, winner):
        self.write("GAME OVER", align=ALIGNMENT, font=('Courier', 20, 'bold'))
        self.goto(0, -25)
        self.write(f"The {winner} player is the winner!", align=ALIGNMENT, font=('Courier', 16, 'bold'))
